#!/bin/sh
# Pre-render hook (see _quarto.yml): stamps the build date into the footer.
# Runs on every `quarto render`, so the published date always matches the
# latest deploy. LC_ALL=C keeps month names in English.
set -e
cd "$(dirname "$0")/.."
mkdir -p _includes
printf '<div class="demopast-updated">Last updated: %s</div>\n' \
  "$(LC_ALL=C date '+%-d %B %Y')" > _includes/last_updated.html
