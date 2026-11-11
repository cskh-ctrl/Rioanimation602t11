#!/usr/bin/env bash
# CI entry: install everything, then render one video. All output goes to the log.
set -euxo pipefail
KIND=$1; N=$2
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"
nproc; free -g; df -h . | tail -1
# apt mirrors on the runner sometimes fail to resolve: retry, and fall back to a static ffmpeg build
apt_retry() { for i in 1 2 3 4 5; do sudo apt-get update -qq && sudo apt-get install -y -qq --fix-missing "$@" && return 0; echo "apt failed, retry $i"; sleep $((i * 20)); done; return 1; }
which ffmpeg || apt_retry ffmpeg || (curl -fsSL https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz | tar -xJ -C /tmp && sudo cp /tmp/ffmpeg-*-static/ffmpeg /tmp/ffmpeg-*-static/ffprobe /usr/local/bin/)
ffmpeg -version | head -1
if [ ! -s models/kokoro-v1.0.onnx ]; then
  mkdir -p models
  for f in kokoro-v1.0.onnx voices-v1.0.bin; do curl -fsSL --retry 3 -o models/$f https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f; done
fi
ls -la models
python3 -m pip install -q --break-system-packages kokoro-onnx soundfile numpy scipy faster-whisper nltk
(cd studio && npm install --no-audit --no-fund && (for i in 1 2 3 4 5; do npx playwright install --with-deps chromium && break; echo "playwright deps failed, retry $i"; sleep $((i * 20)); done; npx playwright install chromium))
set +x
WORKERS=${WORKERS:-4} bash pipeline/run_one.sh "$KIND" "$N"
