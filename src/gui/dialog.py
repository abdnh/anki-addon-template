from typing import Optional

from aqt.qt import *

from ..ankiutils.gui import dialog


class Dialog(dialog.Dialog):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
        flags: Qt.WindowType = Qt.WindowType.Dialog,
    ) -> None:
        super().__init__(__name__, parent, flags)
