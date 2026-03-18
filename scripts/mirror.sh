#!/bin/bash
set -e

TARGET_URL="http://www.bellavitacaregiving.com"
OUTPUT_DIR="site-mirror"

mkdir -p "$OUTPUT_DIR"

wget --mirror --convert-links --adjust-extension --page-requisites --no-parent --directory-prefix="$OUTPUT_DIR" "$TARGET_URL"

echo "Mirror complete. Files saved in $OUTPUT_DIR"
