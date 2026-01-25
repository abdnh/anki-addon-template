from __future__ import annotations

from aqt import gui_hooks, mw
from aqt.deckbrowser import DeckBrowser
from aqt.webview import WebContent

from .consts import consts


def on_webview_will_set_content(web_content: WebContent, context: object | None) -> None:
    if isinstance(context, DeckBrowser):
        web_base = f"/_addons/{consts.module}/web/build"
        web_content.js.append(f"{web_base}/deckbrowser.js")
        web_content.css.append(f"{web_base}/deckbrowser.css")


def on_deck_browser_did_render(deckbrowser: DeckBrowser) -> None:
    deckbrowser.web.eval("MyAddon.initDeckbrowser()")


def init_hooks() -> None:
    gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
    gui_hooks.deck_browser_did_render.append(on_deck_browser_did_render)
    mw.addonManager.setWebExports(__name__, r"web/.*")
