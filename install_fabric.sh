#!/bin/bash

# Check if Python3 and pip are installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

if ! command -v pip3 &>/dev/null; then
    echo "pip3 is not installed. Please install pip3 and try again."
    exit 1
fi

# Install Fabric
pip3 install fabric

# Check if Fabric installation was successful
if ! command -v fab &>/dev/null; then
    echo "Fabric installation failed. Please check your Python/pip setup."
    exit 1
fi

# Add the directory containing 'fab' to PATH
pip3_bin_dir=$(python3 -c "import site; print(site.USER_BASE)")/bin
if [[ ":$PATH:" != *":$pip3_bin_dir:"* ]]; then
    echo "Adding $pip3_bin_dir to PATH..."
    echo "export PATH=\$PATH:$pip3_bin_dir" >> ~/.bashrc
    source ~/.bashrc
    echo "PATH updated. You can now use 'fab' command."
else
    echo "The directory $pip3_bin_dir is already in your PATH."
fi

