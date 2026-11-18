#!/usr/bin/env python3
"""Verify the frozen MM v1.0.2 public site snapshot without executing its contents.

Standard library only. Read-only. Does not extract ZIP members, run scientific
software, access the network, or alter files. Verifies the packaged release
and its per-member SHA-256, Git blob SHA-1, mode, and reconstructed Git tree.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from collections import defaultdict
from pathlib import Path, PurePosixPath

DEFAULT_SNAPSHOT = Path(
    "releases/v1.0.2/"
    "MM_METHODOLOGY_V102_DEDICATED_GHPAGES_SITE_NOT_DEPLOYED_v1.0.0.zip"
)
DEFAULT_MANIFEST = Path("PUBLIC_RELEASE_MANIFEST.json")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    payload = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    return hashlib.sha1(payload).hexdigest()


def git_tree_sha1(entries: dict[str, str]) -> str:
    """Compute Git's recursive tree ID for regular 100644 files."""
    tree: dict[str, object] = {}
    for path, blob in entries.items():
        parts = PurePosixPath(path).parts
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})  # type: ignore[assignment]
        node[parts[-1]] = blob

    def digest(node: dict[str, object]) -> str:
        sort_key = lambda key: (key + ("/" if isinstance(node[key], dict) else "")).encode()
        payload = bytearray()
        for key in sorted(node, key=sort_key):
            value = node[key]
            if isinstance(value, dict):
                mode, target = "40000", digest(value)
            else:
                mode, target = "100644", value
            payload += mode.encode("ascii") + b" " + key.encode("utf-8") + b"\0"
            payload += bytes.fromhex(target)
        raw = bytes(payload)
        return hashlib.sha1(b"tree " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

    return digest(tree)


def safe_member(path: str) -> bool:
    if not path or path.startswith("/") or "\\" in path or "\x00" in path:
        return False
    parts = path.split("/")
    return all(part not in ("", ".", "..") for part in parts)


def verify(snapshot: Path, manifest_file: Path) -> None:
    m = json.loads(manifest_file.read_text(encoding="utf-8"))
    metadata = m["site_release"]
    records = m["files"]
    expected = {record["path"]: record for record in records}
    if len(expected) != len(records) or not all(safe_member(p) for p in expected):
        raise ValueError("Manifest contains duplicate or unsafe member paths")
    if len(records) != metadata["entries"]:
        raise ValueError("Manifest file count differs from site_release.entries")

    snapshot_bytes = snapshot.read_bytes()
    if len(snapshot_bytes) != metadata["size_bytes"]:
        raise ValueError("Snapshot byte count does not match frozen manifest")
    if sha256(snapshot_bytes) != metadata["sha256"]:
        raise ValueError("Snapshot SHA-256 does not match frozen manifest")

    blobs = {}
    with zipfile.ZipFile(snapshot) as archive:
        members = archive.infolist()
        names = [i.filename for i in members]
        if len(names) != len(set(names)) or not all(safe_member(p) for p in names):
            raise ValueError("ZIP contains duplicate or unsafe paths")
        if set(names) != set(expected):
            raise ValueError(
                f"ZIP/member manifest mismatch: missing={sorted(set(expected)-set(names))}, "
                f"unexpected={sorted(set(names)-set(expected))}"
            )
        if archive.testzip() is not None:
            raise ValueError("ZIP CRC verification failed")
        for item in members:
            if item.is_dir():
                raise ValueError(f"Directory entry is not an approved regular file: {item.filename}")
            if item.flag_bits & 0x1:
                raise ValueError(f"Encrypted member is forbidden: {item.filename}")
            data = archive.read(item)
            record = expected[item.filename]
            if len(data) != record["size_bytes"]:
                raise ValueError(f"Size mismatch: {item.filename}")
            if sha256(data) != record["sha256"]:
                raise ValueError(f"SHA-256 mismatch: {item.filename}")
            blob = git_blob_sha1(data)
            if blob != record["git_blob_sha1"]:
                raise ValueError(f"Git blob SHA-1 mismatch: {item.filename}")
            blobs[item.filename] = blob

    tree = git_tree_sha1(blobs)
    if tree != metadata["expected_git_tree_sha1"]:
        raise ValueError("Reconstructed Git tree SHA-1 differs from approved tree")
    supplement = expected["downloads/mm-methodology-v1.0.2-reproducibility-supplement.zip"]
    print("PASS: MM public release snapshot integrity")
    print(f"version={m['scientific_version']}")
    print(f"snapshot_sha256={metadata['sha256']}")
    print(f"verified_files={len(records)}")
    print(f"git_tree_sha1={tree}")
    print(f"supplement_sha256={supplement['sha256']}")
    print("scope=static_snapshot_integrity_only; no scientific runtime executed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=Path, default=DEFAULT_SNAPSHOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    try:
        verify(args.snapshot, args.manifest)
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"HOLD: release verification failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
