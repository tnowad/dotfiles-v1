#!/bin/bash
# shellcheck disable=1091,2153

source "$SCRIPTS_DIR/link_config.sh"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SOURCE_DIR="$SCRIPT_DIR/config"
CONFIG_DIR="$HOME/.config/i3blocks"

link_config "$SOURCE_DIR" "$CONFIG_DIR"

echo "I3 configuration linked."
