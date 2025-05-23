# Anki Add-on Template

Anki add-on template for my projects.

## Structure

- My [ankiscripts](https://github.com/abdnh/ankiscripts) project is used for various tasks, such as setting up dev environment, packaging, and updating dependencies.
- Source files are in the [src](src) folder. The add-on zip contains all contents of this folder.
- Qt Designer files (if any) are in [designer](designer) folder. Generated Python forms are written to src/forms.
- An [addon.json](addon.json) file is used for metadata, similar to [Glutanimate's add-on builder](https://github.com/glutanimate/anki-addon-builder). [manifest.json](https://addon-docs.ankiweb.net/sharing.html#sharing-outside-ankiweb) is produced from this file.
- [Ruff](https://docs.astral.sh/ruff/) is used for linting and formatting.
- Tests are in the [tests](tests) folder.
- a [Makefile](Makefile) is used to run build & lint commands.
- [uv](https://docs.astral.sh/uv/) is used to manage requirements in [pyproject.toml](pyproject.toml).
- [CHANGELOG.md](CHANGELOG.md) follows the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.
- The description for the AnkiWeb listing is in [ankiweb_page.html](ankiweb_page.html). [ankiwebify-readme](https://github.com/abdnh/ankiwebify-readme) can be used to convert some sections of README.md to the HTML accepted by AnkiWeb.
- The add-on is [licensed](LICENSE) under [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/).

**_Below sections are what should be modified and included in the actual add-on's README.md._**

[BEGINNING OF TEMPLATE]

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes.

## Support & feature requests

Please post any questions, bug reports, or feature requests in the [support page](https://forums.ankiweb.net/c/add-ons/11) or the [issue tracker](https://github.com/abdnh/anki-addon-template/issues).

If you want priority support for your feature/help request, I'm available for hire.
Get in touch via [email](mailto:abdo@abdnh.net) or the UpWork link below.

## Support me

Consider supporting me if you like my work:

<a href="https://github.com/sponsors/abdnh"><img height='36' src="https://i.imgur.com/dAgtzcC.png"></a>
<a href="https://www.patreon.com/abdnh"><img height='36' src="https://i.imgur.com/mZBGpZ1.png"></a>
<a href="https://www.buymeacoffee.com/abdnh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" height="36" ></a>

I'm also available for freelance add-on development:

<a href="https://www.upwork.com/freelancers/~01d764ac58a0eccc5c"><img height='36' src="https://i.imgur.com/z9lPvHb.png"></a>
