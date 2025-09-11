from typing import Any

from aqt.qt import QWidget

from ..proto.backend_pb2 import SayHelloRequest, SayHelloResponse
from .sveltekit_web import SveltekitWebDialog


class HelloWebDialog(SveltekitWebDialog):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(path="hello", parent=parent, subtitle="Hello world!")
        self.server.add_proto_handler_for_dialog(
            self, "ankiaddon.backend.BackendService", "SayHello", self.on_say_hello
        )

    def on_say_hello(self, data: bytes) -> bytes:
        request = SayHelloRequest.FromString(data)
        return SayHelloResponse(message=f"Hello, {request.name}!").SerializeToString()

    def on_bridge_command(self, message: str) -> Any:
        if message == "hello":
            return "Hello, world!"
        return super().on_bridge_command(message)
