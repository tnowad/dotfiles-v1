#!/bin/bash
# shellcheck disable=1091,2153

source "$SCRIPTS_DIR/link_config.sh"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

link_config "$SCRIPT_DIR/.gitconfig" "$HOME/.gitconfig"

echo "Git configuration linked."
