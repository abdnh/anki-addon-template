#!/usr/bin/env bash

pip install uv
uv sync
sudo apt-get update
sudo apt install libxcb-xinerama0 libxcb-cursor0 libegl1
