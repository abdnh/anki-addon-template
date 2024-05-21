from anki.hooks import wrap
from aqt import gui_hooks, mw
from aqt.qt import *

from .config import config
from .consts import consts
from .log import logger


def _on_profile_did_open() -> None:
    try:
        import ankiutils.errors

        ankiutils.errors.setup_error_handler(consts, config, logger)
    except ImportError:
        logger.warning("ankiutils.errors not found; error handling is disabled.")


def _before_exit() -> None:
    import atexit
    import logging

    # Fix 'RuntimeError: wrapped C/C++ object of type ErrorHandler has been deleted' on shutdown
    atexit.unregister(logging.shutdown)
    logging.shutdown()


def setup_error_handler() -> None:
    gui_hooks.profile_did_open.append(_on_profile_did_open)
    mw.cleanupAndExit = wrap(mw.cleanupAndExit, _before_exit, "before")  # type: ignore
