from __future__ import annotations

import atexit
import logging

from anki.hooks import wrap
from aqt import gui_hooks, mw

from .config import config
from .consts import consts
from .log import logger
from .vendor.ankiutils import errors

REGISTERED_ERROR_HANDLER = False


def _on_profile_did_open() -> None:
    global REGISTERED_ERROR_HANDLER

    if not REGISTERED_ERROR_HANDLER:
        errors.setup_error_handler(consts, config, logger)
        REGISTERED_ERROR_HANDLER = True


def _before_exit() -> None:
    # Fix 'RuntimeError: wrapped C/C++ object of type ErrorHandler has been deleted'
    # on shutdown
    atexit.unregister(logging.shutdown)
    logging.shutdown()


def setup_error_handler() -> None:
    gui_hooks.profile_did_open.append(_on_profile_did_open)
    mw.cleanupAndExit = wrap(mw.cleanupAndExit, _before_exit, "before")  # type: ignore


def report_exception_and_upload_logs(exception: BaseException) -> str | None:
    return errors.report_exception_and_upload_logs(exception, consts, config, logger)
