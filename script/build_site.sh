#!/usr/bin/env sh
# Keep the JSON media mapping and generated indexes current for every HTML build.
set -eu
cd "$(dirname "$0")/.."
python3 script/generate_features.py --features-only
bundle exec jekyll build "$@"
