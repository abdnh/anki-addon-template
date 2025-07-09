#!/usr/bin/env bash

uv sync --locked --dev
sudo apt-get update
sudo apt install libxcb-xinerama0 libxcb-cursor0 libegl1
curl -fsSL https://dprint.dev/install.sh | sh -s > /dev/null 2>&1
echo "$HOME/.dprint/bin" >> $GITHUB_PATH
