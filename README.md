# Anki Add-on Template

Anki add-on template for my projects.

## Structure

-   My [ankiscripts](https://github.com/abdnh/ankiscripts) project is used for various tasks, such as setting up dev environment, packaging, and updating dependencies.
-   Source files are in the [src](src) folder. The add-on zip contains all contents of this folder.
-   Qt Designer files (if any) are in [designer](designer) folder. Generated Python forms are written to src/forms.
-   An [addon.json](addon.json) file is used for metadata, similar to [Glutanimate's add-on builder](https://github.com/glutanimate/anki-addon-builder). [manifest.json](https://addon-docs.ankiweb.net/sharing.html#sharing-outside-ankiweb) is produced from this file.
-   [pylint](.pylintrc), [mypy](mypy.ini), black, and [isort](.isort.cfg) are used for linting and formatting.
-   Tests are in the [tests](tests) folder.
-   a [Makefile](Makefile) is used to run build & lint commands.
-   Requirements are specified in \*.in files inside the [requirements](requirements) subfolder. [pip-tools](https://github.com/jazzband/pip-tools) is used to update and pin dependencies, generating corresponding .txt files.
-   [CHANGELOG.md](CHANGELOG.md) follows the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.
-   The description for the AnkiWeb listing is in [ankiweb_page.html](ankiweb_page.html). [ankiwebify-readme](https://github.com/abdnh/ankiwebify-readme) can be used to convert some sections of README.md to the HTML accepted by AnkiWeb.
-   The add-on is [licensed](LICENSE) under [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/).

**_Below sections are what should be modified and included in the actual add-on's README.md._**

[BEGINNING OF TEMPLATE]

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes.

## Support & feature requests

Please post any questions, bug reports, or feature requests in the [support page](https://forums.ankiweb.net/c/add-ons/11) or the [issue tracker](https://github.com/abdnh/anki-addon-template/issues).

If you want priority support for your feature/help request, I'm available for hire.
You can get in touch from the aforementioned pages, via [email](mailto:abdo@abdnh.net) or on [Fiverr](https://www.fiverr.com/abd_nh).

## Support me

Consider supporting me if you like my work:

<a href="https://github.com/sponsors/abdnh"><img height='36' src="https://i.imgur.com/dAgtzcC.png"></a>
<a href="https://www.patreon.com/abdnh"><img height='36' src="https://i.imgur.com/mZBGpZ1.png"></a>
<a href="https://www.buymeacoffee.com/abdnh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" height="36" ></a>

I'm also available for freelance add-on development on Fiverr:

<a href="https://www.fiverr.com/abd_nh/develop-an-anki-addon"><img height='36' src="https://i.imgur.com/0meG4dk.png"></a>
