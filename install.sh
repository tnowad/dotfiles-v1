#!/bin/bash
DOTFILES_DIR="config"

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/scripts"
export SCRIPTS_DIR

echo "Starting dotfiles installation..."

for dir in "$DOTFILES_DIR"/*/; do
	if [ -d "$dir" ]; then
		install_script="$dir/install.sh"
		if [ -f "$install_script" ]; then
			(cd "$dir" && ./install.sh)
		else
			echo "No install script found for $(basename "$dir"), skipping..."
		fi
	fi
done

echo "All applicable dotfiles installations have been processed."
