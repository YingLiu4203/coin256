#!/bin/bash

# Find all markdown files recursively in content/ sorted naturally
FILES=$(find content -type f -name "*.md" | sort)

echo "Compiling the following files:"
echo "$FILES"

# Run Pandoc to generate the Word document
pandoc $FILES \
  -o coin_book.docx \
  --reference-doc=custom_template.docx \
  --toc \
  --toc-depth=2 \
  --resource-path=.:content:content/images

echo "Done! Output saved to coin_book.docx"
