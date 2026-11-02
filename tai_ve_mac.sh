#!/usr/bin/env bash
# Tai toan bo video Rio Animation bo 2 ve may (macOS/Linux): bash tai_ve_mac.sh
# Ket qua: RioAnimation_Bo2/01_Video_Dai_01-30, 02_Shorts_01-30, 03_Shorts_31-60 (moi thu muc: video MP4 + 00_THONG_TIN_DANG_YOUTUBE.txt)
# va RioAnimation_Bo2/04_Anh_Bia_Phu_De (anh bia + phu de SRT cua tung video). Chay lai bat ky luc nao: file da co se bo qua.
set -e
REPO=cskh-ctrl/rioanimation602t11
ROOT="$(cd "$(dirname "$0")" && pwd)/RioAnimation_Bo2"
get() { # tag folder
  J=$(curl -fsSL "https://api.github.com/repos/$REPO/releases/tags/$1"); mkdir -p "$ROOT/$2"
  echo "$J" | python3 -c "import sys,json;[print(a['name'],a['size'],a['browser_download_url']) for a in sorted(json.load(sys.stdin)['assets'],key=lambda a:a['name']) if not a['name'].startswith('info_')]" | while read n s u; do
    f="$ROOT/$2/$n"
    if [ -f "$f" ] && [ "$(wc -c < "$f" | tr -d ' ')" = "$s" ]; then echo "Da co: $n"; continue; fi
    echo "Dang tai $2 / $n ..."; curl -fL -o "$f" "$u"
  done
}
for t in g01 g02 g03; do
  NAME=$(curl -fsSL "https://api.github.com/repos/$REPO/releases/tags/$t" | python3 -c "import sys,json;print(json.load(sys.stdin)['name'])")
  get $t "$NAME"
done
get meta "04_Anh_Bia_Phu_De"
echo "Xong! Thu muc: $ROOT"
