from aqt.utils import showInfo

from .patches import patch_certifi

patch_certifi()

# ruff: noqa: E402
from .consts import consts
from .errors import setup_error_handler
from .log import logger


def init() -> None:
    setup_error_handler()
    msg = f"Hello from {consts.name}!"
    logger.debug(msg)
    showInfo(msg)
