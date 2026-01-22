from .patches import patch_certifi

patch_certifi()

# ruff: noqa: E402
from aqt import QMenu, mw

from . import deckbrowser
from .backend.server import init_server
from .consts import consts
from .errors import setup_error_handler, upload_logs_and_notify_user
from .gui.hello import HelloWebDialog
from .log import logger


def on_hello() -> None:
    HelloWebDialog(parent=mw).show()


def on_upload_logs() -> None:
    upload_logs_and_notify_user(mw)


def add_menu() -> None:
    menu = QMenu(consts.name, mw)
    menu.addAction("Say hello", on_hello)
    menu.addAction("Upload logs", on_upload_logs)
    mw.form.menuTools.addMenu(menu)


def init() -> None:
    setup_error_handler(lambda: logger.info("Hello world!", addon=consts.name))
    add_menu()
    deckbrowser.init_hooks()
    init_server()
