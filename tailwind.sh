#!/bin/bash
case "$1" in
    watch)
      bun run tailwindcss -i ./tailwind.styles.css -o ./static/css/app.css --watch --minify
      ;;
    *)
      bun run tailwindcss -i ./tailwind.styles.css -o ./static/css/app.css --minify
      ;;
esac
