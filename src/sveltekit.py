from .consts import consts
from .log import logger
from .vendor.ankiutils import sveltekit

server: sveltekit.SveltekitServer | None = None


def init_server() -> sveltekit.SveltekitServer:
    global server
    if server is None:
        server = sveltekit.init_server(consts, logger)
    return server


def get_server() -> sveltekit.SveltekitServer:
    if server is None:
        raise sveltekit.SveltekitServerNotInitializedError()
    return server
