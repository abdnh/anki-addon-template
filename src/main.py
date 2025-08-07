from .patches import patch_certifi

patch_certifi()

# ruff: noqa: E402
from aqt import QMenu, mw
from aqt.utils import showInfo

from .consts import consts
from .errors import setup_error_handler
from .log import logger


def on_action() -> None:
    showInfo("Hello world!")


def add_menu() -> None:
    menu = QMenu(consts.name, mw)
    menu.addAction("Hello", on_action)
    mw.form.menuTools.addMenu(menu)


def init() -> None:
    setup_error_handler()
    logger.debug("Hello world!", addon=consts.name)
    add_menu()
