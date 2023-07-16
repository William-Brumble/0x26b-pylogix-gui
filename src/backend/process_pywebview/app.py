import zmq
import json
import multiprocessing
from logging import getLogger, NullHandler, DEBUG
from logging.handlers import QueueHandler

from process_pywebview._utils import *
from process_pywebview._models import *


class App:
    def __init__(
        self,
        pywebview_url: str,
        queue: multiprocessing.Queue = None,
    ):
        self.logger = getLogger("pywebview-process-app")
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(NullHandler())
        if queue:
            self.handler = QueueHandler(queue)
            self.logger.addHandler(self.handler)

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.connect(pywebview_url)

    def __del__(self):
        self.socket.close()
        self.context.term()

    @common_payload_protection(Connect)
    def _connect(self, request: Connect):
        msg = json.dumps(
            {
                "command": "connect",
                "payload": {
                    "ip_address": request.ip_address,
                    "slot": request.slot,
                    "timeout": request.timeout,
                    "Micro800": request.Micro800,
                },
            }
        ).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()

        return ServerResponse()

    def _close(self):
        msg = json.dumps({"command": "close", "payload": None}).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse()

    def _get_connection_size(self):
        msg = json.dumps({"command": "get_connection_size", "payload": None}).encode(
            "utf-8"
        )

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=ConnectionSize(connection_size=connection_size))

    @common_payload_protection(ConnectionSize)
    def _set_connection_size(self, request: ConnectionSize):
        msg = json.dumps(
            {
                "command": "set_connection_size",
                "payload": {"connection_size": request.connection_size},
            }
        ).encode("utf-8")
        return ServerResponse()

    @common_payload_protection(Read)
    def _read(self, request: Read):
        msg = json.dumps(
            {
                "command": "read",
                "payload": {
                    "tag": request.tag,
                    "count": request.count,
                    "datatype": request.datatype,
                },
            }
        ).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=payload)

    @common_payload_protection(Write)
    def _write(self, request: Write):
        msg = json.dumps(
            {
                "command": "write",
                "payload": {
                    "tag": request.tag,
                    "value": request.value,
                    "datatype": request.datatype,
                },
            }
        ).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=payload)

    @common_payload_protection(PlcTime)
    def _get_plc_time(self, request: PlcTime):
        msg = json.dumps(
            {"command": "get_plc_time", "payload": {"raw": request.raw}}
        ).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=self._pack_response(response))

    def _set_plc_time(self):
        msg = json.dumps({"command": "set_plc_time", "payload": None}).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=self._pack_response(response))

    @common_payload_protection(TagList)
    def _get_tag_list(self, request: TagList):
        msg = json.dumps(
            {"command": "get_tag_list", "payload": {"all_tags": request.all_tags}}
        ).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=encoded)

    @common_payload_protection(ProgramTagList)
    def _get_program_tag_list(self, request: ProgramTagList):
        msg = json.dumps(
            {
                "command": "get_program_tag_list",
                "payload": {"program_name": request.program_name},
            }
        ).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=encoded)

    def _get_programs_list(self):
        msg = json.dumps({"command": "get_programs_list", "payload": None}).encode(
            "utf-8"
        )

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=self._pack_response(response))

    def _discover(self):
        msg = json.dumps({"command": "discover", "payload": None}).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=encoded)

    @common_payload_protection(ModuleProperties)
    def _get_module_properties(self, request: ModuleProperties):
        msg = json.dumps(
            {"command": "get_module_properties", "payload": {"slot": request.slot}}
        ).encode("utf-8")

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=encoded)

    def _get_device_properties(self):
        msg = json.dumps({"command": "get_device_properties", "payload": None}).encode(
            "utf-8"
        )

        self.socket.send(msg)
        message = self.socket.recv()

        return ServerResponse(response=encoded)
