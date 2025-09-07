from __future__ import annotations

from typing import Any

from aqt.qt import QWidget

from .. import sveltekit
from ..consts import consts
from ..log import logger
from ..vendor.ankiutils.gui import sveltekit_web


class SveltekitWebDialog(sveltekit_web.SveltekitWebDialog):
    def __init__(self, path: str, parent: QWidget | None = None, subtitle: str = ""):
        self.path = path
        super().__init__(
            consts=consts,
            logger=logger,
            server=sveltekit.get_server(),
            path=path,
            parent=parent,
            subtitle=subtitle,
        )

    def on_bridge_command(self, message: str) -> Any:
        if message == "hello":
            return "Hello, world!"
        return super().on_bridge_command(message)
