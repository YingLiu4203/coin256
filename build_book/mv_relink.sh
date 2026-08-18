#!/usr/bin/env bash

# Create destination directory if it doesn't exist
mkdir -p ./content/images

# Enable nullglob to avoid literal wildcard if no files exist
shopt -s nullglob

# Move all files and subdirectories from any ./content/*/imgs/ to ./content/images/
for file in ./content/*/imgs/*; do
    # Skip moving into itself if target directory happens to match
    [ -e "$file" ] && mv  "$file" ./content/images
done

echo "Move complete."

# Find all .md and .markdown files in ./content and perform in-place replacement
find ./content -type f \( -name "*.md" -o -name "*.markdown" \) -exec sed -i.bak 's|(\./imgs|(content/images|g' {} +

# Clean up automatic backup files (.bak) created by sed
find ./content -type f -name "*.bak" -delete

echo "Link replacement complete."
