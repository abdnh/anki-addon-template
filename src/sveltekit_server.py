import mimetypes
import threading
from http import HTTPStatus

import flask
from waitress.server import create_server

from .consts import consts
from .log import logger


class SveltekitServerError(Exception):
    pass


class SveltekitServerNotInitializedError(SveltekitServerError):
    def __init__(self) -> None:
        super().__init__("Sveltekit server is not initialized")


app = flask.Flask(__name__)


def _sveltekit_data(path: str) -> bytes:
    full_path = consts.dir / "web" / "sveltekit" / path
    return full_path.read_bytes()


def _text_response(code: HTTPStatus, text: str) -> flask.Response:
    resp = flask.make_response(text, code)
    resp.headers["Content-type"] = "text/plain"
    return resp


@app.route("/<path:path>", methods=["GET", "POST"])
def index(path: str) -> flask.Response:
    immutable = "immutable" in path
    if not immutable:
        path = "index.html"
    mimetype, _encoding = mimetypes.guess_type(path)
    if not mimetype:
        mimetype = "application/octet-stream"
    try:
        data = _sveltekit_data(path)
        response = flask.Response(data, mimetype=mimetype)
        if immutable:
            response.headers["Cache-Control"] = "max-age=31536000"
    except FileNotFoundError:
        logger.error("Sveltekit request returned 404", path=path)
        resp = _text_response(HTTPStatus.NOT_FOUND, f"Invalid path: {path}")
        resp.headers["Content-type"] = "text/plain"
        return resp
    except Exception as error:
        logger.exception("Sveltekit server exception", path=path)
        return _text_response(HTTPStatus.INTERNAL_SERVER_ERROR, str(error))
    return response


class SveltekitServer(threading.Thread):
    _ready = threading.Event()
    daemon = True

    def __init__(self) -> None:
        super().__init__()
        self.is_shutdown = False

    def run(self) -> None:
        try:
            self.server = create_server(
                app,
                host="127.0.0.1",
                port=0,
                clear_untrusted_proxy_headers=True,
            )
            print(
                f"Started Sveltekit server at http://{self.server.effective_host}:{self.server.effective_port}",  # type: ignore
            )

            self._ready.set()
            self.server.run()

        except Exception:
            if not self.is_shutdown:
                raise

    def shutdown(self) -> None:
        self.is_shutdown = True
        sockets = list(self.server._map.values())  # type: ignore
        for socket in sockets:
            socket.handle_close()
        self.server.task_dispatcher.shutdown()

    def get_port(self) -> int:
        self._ready.wait()
        return int(self.server.effective_port)  # type: ignore

    def get_host(self) -> str:
        self._ready.wait()
        return self.server.effective_host  # type: ignore

    def get_url(self) -> str:
        return f"http://{self.get_host()}:{self.get_port()}"


server: SveltekitServer | None = None


def init_sveltekit_server() -> SveltekitServer:
    global server
    if server is None:
        server = SveltekitServer()
        server.start()
    return server


def get_sveltekit_server() -> SveltekitServer:
    if server is None:
        raise SveltekitServerNotInitializedError()
    return server
