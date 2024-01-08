#!/bin/bash

link_config() {
	local source=$1
	local destination=$2

	if [ -d "$source" ]; then
		echo "Linking directory: $source -> $destination"
	elif [ -f "$source" ]; then
		echo "Linking file: $source -> $destination"
	else
		echo "Error: Source is neither a file nor a directory."
		return 1
	fi

	if [ -e "$destination" ] || [ -L "$destination" ]; then
		if [ "$(readlink -- "$destination")" = "$source" ]; then
			echo "The link already exists and points to the correct location."
			return 0
		fi

		read -p "The destination already exists. Do you want to override it? (y/n): " -r override
		if [ "$override" != "y" ]; then
			echo "Linking aborted."
			return 1
		fi

		rm -rf "$destination"
	fi

	ln -s "$source" "$destination"
	echo "Link created successfully."
}
