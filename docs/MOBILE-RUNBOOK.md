# Mobile Photo Publishing Runbook

Use this from an SSH session on the VPS.

## 1. Update the isolated Photos checkout

```bash
cd /tmp
rm -rf MyZubster-Photos
git clone git@github.com:MyZubster-Ecosystem/MyZubster-Photos.git
cd MyZubster-Photos
```

## 2. Check how many uploaded images exist

```bash
find /root/myzubster/public/uploads -type f \
  \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.webp' -o -iname '*.bmp' -o -iname '*.tif' -o -iname '*.tiff' \) \
  | wc -l
```

## 3. Ensure Pillow is available

```bash
python3 -c "from PIL import Image; print('Pillow OK')"
```

If it is missing, install the distribution package appropriate for the VPS before continuing.

## 4. Dry run

```bash
python3 scripts/publish-sanitized-photos.py
```

The dry run only counts candidates. It does not write files.

## 5. Generate sanitized public copies

```bash
python3 scripts/publish-sanitized-photos.py --apply
```

The script:

- never deletes or changes originals;
- re-encodes images before publication;
- strips EXIF/GPS metadata;
- does not publish original filenames;
- orders public copies under `photos/YYYY/MM/` using file mtime;
- computes SHA-256;
- writes `metadata/photos.json` and `metadata/skipped.json`.

## 6. Review before publishing

```bash
cat metadata/skipped.json
find photos -type f | wc -l
git status --short
```

Do not publish if skipped items or privacy concerns require review.

## 7. Publish to GitHub

```bash
git add photos metadata/photos.json metadata/skipped.json
git commit -m "feat: publish sanitized MyZubster photo archive"
git push origin main
```

## Privacy boundary

This repository is public. Raw uploads must not be copied directly into it. Sanitization removes embedded metadata, but human review may still be needed for visible faces, plates, sensitive locations, private evidence, or confidential infrastructure.

Publication of an image does not prove bounty verification, MYZ reward recording, XMR/token payment, or settlement.
