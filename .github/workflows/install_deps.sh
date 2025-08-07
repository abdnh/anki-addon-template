#!/usr/bin/env bash

uv sync --locked --dev
sudo apt-get update
sudo apt install libxcb-xinerama0 libxcb-cursor0 libegl1
curl -fsSL https://dprint.dev/install.sh | sh -s > /dev/null 2>&1
echo "$HOME/.dprint/bin" >> $GITHUB_PATH

# For llvm-lipo
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
sudo ./llvm.sh 20
echo "/usr/lib/llvm-20/bin" >> $GITHUB_PATH
# For restart_anki script
sudo apt install gcc-mingw-w64-x86-64
echo "CC=x86_64-w64-mingw32-gcc" >> $GITHUB_ENV
