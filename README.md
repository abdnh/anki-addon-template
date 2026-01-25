# Anki Add-on Template

Anki add-on template for my projects.

## Overview

- The [ankiscripts](https://github.com/abdnh/ankiscripts) project is used for various tasks, such as installing dependencies, generating forms and packaging the add-on.
- Source files are in the [src](src) folder. The add-on zip contains all contents of this folder.
- Qt Designer files (if any) are in [designer](designer) folder. Generated Python forms are written to src/forms.
- An [addon.json](addon.json) file is used for metadata, similar to [Glutanimate's add-on builder](https://github.com/glutanimate/anki-addon-builder). [manifest.json](https://addon-docs.ankiweb.net/sharing.html#sharing-outside-ankiweb) is produced from this file.
- [Uv](https://docs.astral.sh/uv/) is used to manage requirements in [pyproject.toml](pyproject.toml).
- [Ruff](https://docs.astral.sh/ruff/) is used for linting and formatting.
- Tests are in the [tests](tests) folder.
- a [justfile](justfile) is used to run build & lint commands.
- There's optional support for TypeScript/Svelte/SvelteKit under the [ts](ts/) folder.
- [CHANGELOG.md](CHANGELOG.md) follows the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.
- The description for the AnkiWeb listing is in [ankiweb_page.html](ankiweb_page.html). [ankiwebify-readme](https://github.com/abdnh/ankiwebify-readme) can be used to convert some sections of README.md to the HTML accepted by AnkiWeb.
- [mdBook](https://github.com/rust-lang/mdBook) is used for docs generation. See the [docs](docs/) folder.
- The add-on is [licensed](LICENSE) under [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/).

## Setup

- Set up Python environment using [uv](https://docs.astral.sh/uv/): `uv sync`.
- Run the `ankiscripts.init` script to update add-on metadata: `uv run -m ankiscripts.init --name Foo --package foo`. This script updates `addon.json` and performs basic find/replace to change the add-on name/package. It also sets up the `.vscode` folder for VS Code.
- Run the add-on using VS Code's launch configuration or manually using the command: `uv run -m ankiscripts.run -b ankidata`. This creates a symlink to the add-on's `src` folder inside the `ankidata` Anki data base folder and launches Anki.
