#!/usr/bin/env python3
"""Migrate already-public MyZubster photos from a checked-out source repository.

The tool intentionally copies rather than deletes source files. Each image is
re-encoded so EXIF/GPS and other source metadata are not propagated. The
original semantic directory structure below public/media/rimini is retained.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageOps

SUPPORTED = {".jpg", ".jpeg", ".png", ".webp"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sanitized_save(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as original:
        image = ImageOps.exif_transpose(original)
        suffix = dest.suffix.lower()

        if suffix in {".jpg", ".jpeg"}:
            if image.mode not in {"RGB", "L"}:
                image = image.convert("RGB")
            image.save(dest, "JPEG", quality=92, optimize=True, exif=b"")
        elif suffix == ".webp":
            image.save(dest, "WEBP", quality=92, method=6, exif=b"")
        else:
            if image.mode not in {"1", "L", "LA", "P", "RGB", "RGBA"}:
                image = image.convert("RGB")
            image.save(dest, "PNG", optimize=True)

    with Image.open(dest) as check:
        exif = check.getexif()
        if exif and len(exif):
            raise RuntimeError(f"EXIF remained in {dest}: {len(exif)} entries")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Path to source public/media/rimini")
    parser.add_argument("--repo", required=True, help="Path to MyZubster-Photos checkout")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    repo = Path(args.repo).resolve()
    destination_root = repo / "photos" / "italy" / "emilia-romagna" / "rimini"
    metadata_dir = repo / "metadata"

    if not source.is_dir():
        raise SystemExit(f"Source directory not found: {source}")

    files = sorted(
        p for p in source.rglob("*")
        if p.is_file() and p.suffix.lower() in SUPPORTED
    )
    if not files:
        raise SystemExit(f"No supported photos found in {source}")

    records = []
    for src in files:
        rel = src.relative_to(source)
        dest = destination_root / rel
        sanitized_save(src, dest)
        digest = sha256(dest)
        records.append({
            "sourcePath": f"public/media/rimini/{rel.as_posix()}",
            "destinationPath": dest.relative_to(repo).as_posix(),
            "sha256": digest,
            "sizeBytes": dest.stat().st_size,
            "privacy": {
                "exifStripped": True,
                "gpsMetadataPublished": False
            }
        })
        print(f"OK {rel.as_posix()} -> {dest.relative_to(repo).as_posix()}")

    metadata_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schemaVersion": "1.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": {
            "repository": "MyZubster-Ecosystem/myzubster",
            "branch": "main",
            "root": "public/media/rimini",
            "alreadyPublicOnGitHub": True
        },
        "destination": "MyZubster-Ecosystem/MyZubster-Photos",
        "mode": "sanitized-copy",
        "sourceDeletion": False,
        "count": len(records),
        "photos": records
    }
    (metadata_dir / "github-core-migration.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Migrated {len(records)} sanitized photo(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
