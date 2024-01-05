#!/bin/bash

link_config() {
	local source_dir=$1
	local config_dir=$2

	echo "Linking: $source_dir -> $config_dir"
	if [ -e "$config_dir" ] || [ -L "$config_dir" ]; then
		if [ "$(readlink -- "$config_dir")" = "$source_dir" ]; then
			echo "The link already exists and points to the correct directory."
			return 0
		fi
		read -p "The destination directory already exists. Do you want to override it? (y/n): " -r override
		if [ "$override" != "y" ]; then
			echo "Linking aborted."
			return 1
		fi
		rm -rf "$config_dir"
	fi

	ln -s "$source_dir" "$config_dir"
	echo "Configuration linked."
}
