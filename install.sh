#!/usr/bin/env bash
# Installs the Lucid script to ~/.local/bin
# Project: https://github.com/alishanaminnnn/Lucid
set -e

REPO_URL="https://github.com/alishanaminnnn/Lucid"
NAME="deepseek"                      # command name; change it if you like
DEST="$HOME/.local/bin"
SRC="$(cd "$(dirname "$0")" && pwd)/deepseek.sh"

if [ ! -f "$SRC" ]; then
    echo "Error: deepseek.sh not found next to install.sh" >&2
    echo "Download the full project from: $REPO_URL" >&2
    exit 1
fi

# Warn about missing dependencies (does not stop the install)
for cmd in google-chrome-stable wl-paste wtype; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Warning: '$cmd' is not installed" >&2
    fi
done

mkdir -p "$DEST"
install -m 755 "$SRC" "$DEST/$NAME"
echo "Installed: $DEST/$NAME"

# Make sure the folder is in PATH
case ":$PATH:" in
    *":$DEST:"*) ;;
    *) echo "Note: $DEST is not in your PATH" >&2 ;;
esac

echo
echo "Run it with: $NAME"
echo "Docs and updates: $REPO_URL"
