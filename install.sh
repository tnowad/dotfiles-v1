#!/bin/bash

DOTFILES_DIR="config"

echo "Starting dotfiles installation..."

for dir in "$DOTFILES_DIR"/*/; do
	if [ -d "$dir" ]; then
		install_script="$dir/install.sh"
		if [ -f "$install_script" ]; then
			echo "Installing dotfiles from $(basename "$dir"): running $install_script"
			(cd "$dir" && ./install.sh)
			echo "Installation completed for $(basename "$dir")."
		else
			echo "No install script found for $(basename "$dir"), skipping..."
		fi
	fi
done

echo "All applicable dotfiles installations have been processed."
