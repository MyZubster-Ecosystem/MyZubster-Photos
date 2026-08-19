#!/usr/bin/env python3
"""Publish sanitized copies of MyZubster uploads into this repository.

Safety properties:
- originals are never deleted or modified;
- original filenames are not published;
- images are re-encoded, dropping EXIF/GPS metadata;
- output is ordered by file mtime into photos/YYYY/MM/;
- SHA-256 and public metadata are generated;
- --apply is required before writing files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageOps

SUPPORTED = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def candidates(source: Path) -> Iterable[Path]:
    items = [
        p for p in source.rglob("*")
        if p.is_file() and p.suffix.lower() in SUPPORTED
    ]
    return sorted(items, key=lambda p: (p.stat().st_mtime, str(p)))


def encode_sanitized(src: Path, dest: Path) -> None:
    with Image.open(src) as original:
        image = ImageOps.exif_transpose(original)
        fmt = (original.format or "").upper()

        if fmt in {"JPEG", "JPG"}:
            if image.mode not in {"RGB", "L"}:
                image = image.convert("RGB")
            image.save(dest, "JPEG", quality=92, optimize=True, exif=b"")
            return

        if fmt == "WEBP":
            image.save(dest, "WEBP", quality=92, method=6, exif=b"")
            return

        if image.mode not in {"1", "L", "LA", "P", "RGB", "RGBA"}:
            image = image.convert("RGB")
        image.save(dest, "PNG", optimize=True)


def output_extension(src: Path) -> str:
    with Image.open(src) as im:
        fmt = (im.format or "").upper()
    if fmt in {"JPEG", "JPG"}:
        return ".jpg"
    if fmt == "WEBP":
        return ".webp"
    return ".png"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="/root/myzubster/public/uploads")
    parser.add_argument("--repo", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    repo = Path(args.repo).resolve()
    photos_dir = repo / "photos"
    metadata_dir = repo / "metadata"

    if not source.exists():
        raise SystemExit(f"Source not found: {source}")

    files = list(candidates(source))
    print(f"Found {len(files)} candidate image(s) in {source}")

    if not args.apply:
        print("Dry run only. Re-run with --apply to write sanitized copies.")
        return 0

    photos_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)

    published = []
    skipped = []

    for index, src in enumerate(files, 1):
        temp = None
        try:
            uploaded = datetime.fromtimestamp(src.stat().st_mtime, timezone.utc)
            folder = photos_dir / uploaded.strftime("%Y") / uploaded.strftime("%m")
            folder.mkdir(parents=True, exist_ok=True)

            ext = output_extension(src)
            temp = folder / f".sanitize-{os.getpid()}-{index}{ext}"
            encode_sanitized(src, temp)
            digest = sha256(temp)
            filename = f"{uploaded.strftime('%Y%m%dT%H%M%SZ')}-{digest[:12]}{ext}"
            dest = folder / filename

            if dest.exists():
                temp.unlink(missing_ok=True)
            else:
                temp.replace(dest)

            with Image.open(dest) as check:
                exif = check.getexif()
                if exif and len(exif):
                    raise RuntimeError(f"EXIF still present ({len(exif)} entries)")

            rel = dest.relative_to(repo).as_posix()
            published.append({
                "id": digest,
                "order": index,
                "path": rel,
                "uploadedAt": uploaded.isoformat(),
                "sha256": digest,
                "sizeBytes": dest.stat().st_size,
                "privacy": {
                    "exifStripped": True,
                    "gpsMetadataPublished": False,
                    "originalFilenamePublished": False
                }
            })
            print(f"OK   {index:04d} {rel}")
        except Exception as exc:
            if temp is not None:
                temp.unlink(missing_ok=True)
            skipped.append({"order": index, "reason": str(exc)})
            print(f"SKIP {index:04d} {exc}")

    catalog = {
        "schemaVersion": "1.0.0",
        "ecosystem": "MyZubster",
        "repository": "MyZubster-Ecosystem/MyZubster-Photos",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "ordering": "upload-file-mtime-ascending",
        "sourceNamesPublished": False,
        "exifPolicy": "stripped-before-publication",
        "count": len(published),
        "photos": published
    }

    (metadata_dir / "photos.json").write_text(
        json.dumps(catalog, indent=2) + "\n",
        encoding="utf-8"
    )
    (metadata_dir / "skipped.json").write_text(
        json.dumps({"count": len(skipped), "items": skipped}, indent=2) + "\n",
        encoding="utf-8"
    )

    print(f"Published: {len(published)}")
    print(f"Skipped:   {len(skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
