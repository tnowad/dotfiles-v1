#!/bin/bash
DOTFILES_DIR="config"

IGNORE_DIRS=("qtile")

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/scripts"
export SCRIPTS_DIR

echo "Checking dotfiles installation..."

INSTALL_FOLDERS=()
IGNORE_FOLDERS=()

for dir in "$DOTFILES_DIR"/*/; do
	dir_name=$(basename "$dir")

	if [[ " ${IGNORE_DIRS[*]} " =~ $dir_name ]]; then
		IGNORE_FOLDERS+=("$dir_name")
		continue
	fi

	if [ -d "$dir" ]; then
		INSTALL_FOLDERS+=("$dir_name")
	fi
done

echo "Folders to install:"
for folder in "${INSTALL_FOLDERS[@]}"; do
	echo "- $folder"
done

echo -e "\nFolders to ignore:"
for folder in "${IGNORE_FOLDERS[@]}"; do
	echo "- $folder"
done

read -p "Do you want to proceed with the installation? (y/n): " -r proceed
if [ "$proceed" != "y" ]; then
	echo "Installation aborted."
	exit 0
fi

echo -e "\nStarting dotfiles installation..."
for dir in "${INSTALL_FOLDERS[@]}"; do
	dir_path="$DOTFILES_DIR/$dir"
	install_script="$dir_path/install.sh"

	if [ -f "$install_script" ]; then
		(cd "$dir_path" && ./install.sh)
	else
		echo "No install script found for $dir, skipping..."
	fi
done

echo -e "\nAll applicable dotfiles installations have been processed."
