#!/usr/bin/env bash
# DanceXR website local preview
# Usage: ./preview.sh [port]
#
# Requirements: Ruby (>= 3.0), Bundler
#   gem install bundler

set -e

PORT=${1:-4000}
SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SITE_DIR"

echo "──────────────────────────────────────"
echo "  DanceXR local preview"
echo "──────────────────────────────────────"

# Install / update gems
if [ ! -f Gemfile.lock ] || [ Gemfile -nt Gemfile.lock ]; then
  echo "→ Installing gems..."
  bundle install
fi

echo "→ Starting Jekyll on http://localhost:$PORT"
echo "  (Press Ctrl+C to stop)"
echo ""

bundle exec jekyll serve \
  --port "$PORT" \
  --livereload \
  --open-url \
  --config "_config.yml,_config.dev.yml" 2>/dev/null \
  || bundle exec jekyll serve \
       --port "$PORT" \
       --open-url \
       --config "_config.yml,_config.dev.yml"
