#!/usr/bin/env bash
set -euo pipefail

REPO="${REPO:-/tmp/MyZubster-Photos}"
SOURCE="${SOURCE:-/root/myzubster/public/uploads}"
EXPECTED_REMOTE="MyZubster-Ecosystem/MyZubster-Photos.git"

cd "$REPO"

REMOTE="$(git remote get-url origin)"
case "$REMOTE" in
  *"$EXPECTED_REMOTE") ;;
  *)
    echo "Refusing to push: unexpected origin: $REMOTE" >&2
    exit 2
    ;;
esac

python3 - <<'PY'
try:
    import PIL
except Exception:
    raise SystemExit("Pillow missing. Install with: apt-get update && apt-get install -y python3-pil")
print("Pillow OK")
PY

python3 scripts/publish-sanitized-photos.py --source "$SOURCE" --repo "$REPO" --apply

SKIPPED="$(python3 - <<'PY'
import json
from pathlib import Path
p = Path('metadata/skipped.json')
print(json.loads(p.read_text()).get('count', 0))
PY
)"

TOTAL="$(python3 - <<'PY'
import json
from pathlib import Path
p = Path('metadata/photos.json')
print(json.loads(p.read_text()).get('count', 0))
PY
)"

echo "Sanitized photos: $TOTAL"
echo "Skipped photos:   $SKIPPED"

if [ "$SKIPPED" != "0" ]; then
  echo "Not pushing because some images were skipped. Review metadata/skipped.json first." >&2
  exit 3
fi

if [ "$TOTAL" = "0" ]; then
  echo "No photos found; nothing to publish." >&2
  exit 4
fi

git add photos metadata/photos.json metadata/skipped.json

if git diff --cached --quiet; then
  echo "No new photo changes to commit."
  exit 0
fi

git commit -m "feat: publish sanitized MyZubster photo archive"
git push origin main

echo "Photo archive published successfully to MyZubster-Ecosystem/MyZubster-Photos."
