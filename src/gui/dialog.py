from typing import Optional

from aqt.qt import Qt, QWidget

from ..consts import consts
from ..vendor.ankiutils.gui import dialog


class Dialog(dialog.Dialog):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
        flags: Qt.WindowType = Qt.WindowType.Dialog,
        subtitle: str = "",
    ) -> None:
        self.subtitle = subtitle
        super().__init__(__name__, parent, flags)

    def setup_ui(self) -> None:
        super().setup_ui()
        title = consts.name
        if self.subtitle:
            title += f" - {self.subtitle}"
        self.setWindowTitle(title)
