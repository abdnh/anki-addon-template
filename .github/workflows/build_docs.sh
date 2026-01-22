#!/bin/bash

MDBOOK_VERSION="0.5.2"

export PATH="$HOME/.cargo/bin:$PATH"

install_if_needed() {
    local binary=$1
    local install_cmd=$2
    
    if [ "$GITHUB_ACTIONS" = "true" ]; then
        # avoid recompiling if cached
        if ! command -v $binary &> /dev/null; then
            eval $install_cmd
        fi
    else
        eval $install_cmd
    fi
}

install_if_needed "mdbook" "cargo install mdbook --version $MDBOOK_VERSION"

mdbook --version
cd docs
mdbook build
