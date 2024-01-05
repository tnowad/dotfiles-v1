#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SOURCE_DIR="$SCRIPT_DIR/config"
CONFIG_DIR="$HOME/.config/i3"

echo "Linking: $SOURCE_DIR -> $CONFIG_DIR"
ln -s "$SOURCE_DIR" "$CONFIG_DIR"

echo "i3 configuration linked."
