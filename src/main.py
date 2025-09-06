from .patches import patch_certifi

patch_certifi()

# ruff: noqa: E402
from aqt import QMenu, mw

from .consts import consts
from .errors import setup_error_handler
from .gui.sveltekit_web import SveltekitWebDialog
from .log import logger
from .sveltekit_server import init_sveltekit_server


def on_action() -> None:
    SveltekitWebDialog("hello", parent=mw, subtitle="Hello world!").show()


def add_menu() -> None:
    menu = QMenu(consts.name, mw)
    menu.addAction("Say hello", on_action)
    mw.form.menuTools.addMenu(menu)


def init() -> None:
    setup_error_handler()
    logger.debug("Hello world!", addon=consts.name)
    add_menu()
    init_sveltekit_server()
