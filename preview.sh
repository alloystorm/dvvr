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

# Added --verbose to track which file causes the crash
bundle exec jekyll serve \
  --port "$PORT" \
  --livereload \
  --open-url \
  --trace \
  --verbose \
  --config "_config.yml,_config.dev.yml"