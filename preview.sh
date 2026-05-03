#!/usr/bin/env bash
# DanceXR website local preview
# Usage: ./preview.sh [port] [--no-check] [--external]
#
#   --no-check   skip dead-link and orphan checks and serve immediately
#   --external   also check external URLs (slow)
#
# Requirements: Ruby (>= 3.0), Bundler, Python 3
#   gem install bundler

set -e

PORT=${1:-4000}
SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKIP_CHECK=false
CHECK_EXTERNAL=false

for arg in "$@"; do
  case "$arg" in
    --no-check)  SKIP_CHECK=true ;;
    --external)  CHECK_EXTERNAL=true ;;
  esac
done

cd "$SITE_DIR"

echo "──────────────────────────────────────"
echo "  DanceXR local preview"
echo "──────────────────────────────────────"

# Install / update gems
if [ ! -f Gemfile.lock ] || [ Gemfile -nt Gemfile.lock ]; then
  echo "→ Installing gems..."
  bundle install
fi

if [ "$SKIP_CHECK" = false ]; then
  # ── 1. Start Jekyll in the background ────────────────────────────────────
  echo "→ Starting Jekyll server..."
  bundle exec jekyll serve \
    --port "$PORT" \
    --livereload \
    --open-url \
    --config "_config.yml,_config.dev.yml" &
  JEKYLL_PID=$!
  trap "kill $JEKYLL_PID 2>/dev/null" EXIT INT TERM

  # ── 2. Wait until the server is ready ────────────────────────────────────
  echo -n "  Waiting for server"
  until curl -sf "http://localhost:$PORT/" > /dev/null 2>&1; do
    # Exit early if Jekyll crashed
    if ! kill -0 "$JEKYLL_PID" 2>/dev/null; then
      echo ""
      echo "  Jekyll exited unexpectedly." >&2
      exit 1
    fi
    echo -n "."
    sleep 1
  done
  echo " ready."
  echo ""

  # ── 3. Check dead links and orphan pages against the live server ──────────
  echo "→ Checking links and orphan pages (crawling http://localhost:$PORT)..."
  EXTRA=""
  [ "$CHECK_EXTERNAL" = true ] && EXTRA="--external"
  python3 "$SITE_DIR/script/check_links.py" \
    "http://localhost:$PORT" "$SITE_DIR/_site" $EXTRA || true
  echo ""
  echo "  Checks complete. Server still running at http://localhost:$PORT"
  echo "  (Press Ctrl+C to stop)"

  # ── 4. Keep serving until Ctrl+C ─────────────────────────────────────────
  wait "$JEKYLL_PID" || true

else
  # ── Just serve ─────────────────────────────────────────────────────────────
  echo "→ Starting Jekyll on http://localhost:$PORT"
  echo "  (Press Ctrl+C to stop)"
  echo ""
  bundle exec jekyll serve \
    --port "$PORT" \
    --livereload \
    --open-url \
    --config "_config.yml,_config.dev.yml"
fi