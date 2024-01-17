#!/bin/bash
# shellcheck disable=1091,2153

source "$SCRIPTS_DIR/link_config.sh"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

link_config "$SCRIPT_DIR/.bash_profile" "$HOME/.bash_profile"
link_config "$SCRIPT_DIR/.bash_logout" "$HOME/.bash_logout"
link_config "$SCRIPT_DIR/.bashrc" "$HOME/.bashrc"

echo "Bash configuration linked."
