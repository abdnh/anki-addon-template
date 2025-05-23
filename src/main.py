import os
import sys

from aqt.utils import showInfo

sys.path.append(os.path.join(os.path.dirname(__file__), "vendor"))

from .consts import consts
from .errors import setup_error_handler
from .log import logger


def init() -> None:
    setup_error_handler()
    msg = f"Hello from {consts.name}!"
    logger.debug(msg)
    showInfo(msg)
