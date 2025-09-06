from __future__ import annotations

from aqt.qt import Qt, QUrl, QVBoxLayout, QWidget
from aqt.webview import AnkiWebView

from .. import sveltekit
from ..consts import consts
from ..log import logger
from .dialog import Dialog


class SveltekitWebDialog(Dialog):
    def __init__(self, path: str, parent: QWidget | None = None, subtitle: str = ""):
        self.web: AnkiWebView
        self.path = path
        super().__init__(parent=parent, flags=Qt.WindowType.Window, subtitle=subtitle)

    def setup_ui(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)
        title = f"{consts.name} - {self.subtitle}"
        self.web = AnkiWebView(self, title)
        self.web.set_title(title)
        layout.addWidget(self.web)
        self.web.set_bridge_command(self.on_bridge_command, self)
        super().setup_ui()
        self._load_page()

    def on_bridge_command(self, message: str) -> None:
        logger.warning("Unhandled bridge command", message=message)

    def _load_page(self) -> None:
        self.web.set_open_links_externally(False)
        self.web.load_url(QUrl(f"{sveltekit.get_server().get_url()}/{self.path}"))
        self.web.add_dynamic_styling_and_props_then_show()
