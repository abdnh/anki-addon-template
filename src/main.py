from .patches import patch_certifi

patch_certifi()

# ruff: noqa: E402
from aqt import QMenu, mw

from . import deckbrowser
from .backend.server import init_server
from .consts import consts
from .errors import setup_error_handler
from .gui.hello import HelloWebDialog
from .log import logger


def on_action() -> None:
    HelloWebDialog(parent=mw).show()


def add_menu() -> None:
    menu = QMenu(consts.name, mw)
    menu.addAction("Say hello", on_action)
    mw.form.menuTools.addMenu(menu)


def init() -> None:
    setup_error_handler()
    logger.debug("Hello world!", addon=consts.name)
    add_menu()
    deckbrowser.init_hooks()
    init_server()
