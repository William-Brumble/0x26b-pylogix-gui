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
        self._logger = getLogger("pywebview-app")
        self._logger.setLevel(DEBUG)
        self._logger.addHandler(NullHandler())
        if queue:
            self.handler = QueueHandler(queue)
            self._logger.addHandler(self.handler)

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.connect(pywebview_url)

    def __del__(self):
        self.socket.close()
        self.context.term()

    def _decoded_message(self, message):
        message_decoded = message.decode("utf-8")
        message_objectified = json.loads(message_decoded)
        return message_objectified

    @common_payload_protection(Connect)
    def connect(self, request: Connect):
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
        message_decoded = self._decoded_message(message)

        return ServerResponse(**message_decoded)

    def close(self):
        msg = json.dumps({"command": "close", "payload": None}).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(**message_decoded)

    def get_connection_size(self):
        msg = json.dumps({"command": "get_connection_size", "payload": None}).encode(
            "utf-8"
        )

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=ConnectionSizeResponse(
                connection_size=message_decoded["response"]["connection_size"]
            ),
        )

    @common_payload_protection(ConnectionSize)
    def set_connection_size(self, request: ConnectionSize):
        msg = json.dumps(
            {
                "command": "set_connection_size",
                "payload": {"connection_size": request.connection_size},
            }
        ).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(**message_decoded)

    @common_payload_protection(Read)
    def read(self, request: Read):
        self._logger.warn(
            "context ----------------------------------------------------"
        )
        self._logger.warn(self.context)
        self._logger.warn(self.socket)
        self._logger.warn(
            "context ----------------------------------------------------"
        )

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
        message_decoded = self._decoded_message(message)

        container: list[Response] = []
        for response in message_decoded["response"]:
            container.append(ResponseAsDataclass(**response))

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=container,
        )

    @common_payload_protection(Write)
    def write(self, request: Write):
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
        message_decoded = self._decoded_message(message)

        container: list[Response] = []
        for response in message_decoded["response"]:
            container.append(ResponseAsDataclass(**response))

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=container,
        )

    @common_payload_protection(PlcTime)
    def get_plc_time(self, request: PlcTime):
        msg = json.dumps(
            {"command": "get_plc_time", "payload": {"raw": request.raw}}
        ).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=self._unpack_response(message_decoded["response"]),
        )

    def set_plc_time(self):
        msg = json.dumps({"command": "set_plc_time", "payload": None}).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=self._unpack_response(message_decoded["response"]),
        )

    @common_payload_protection(TagList)
    def get_tag_list(self, request: TagList):
        msg = json.dumps(
            {"command": "get_tag_list", "payload": {"all_tags": request.all_tags}}
        ).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=self._unpack_raw_tags(message_decoded["response"]),
        )

    @common_payload_protection(ProgramTagList)
    def get_program_tag_list(self, request: ProgramTagList):
        msg = json.dumps(
            {
                "command": "get_program_tag_list",
                "payload": {"program_name": request.program_name},
            }
        ).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=self._unpack_raw_tags(message_decoded["response"]),
        )

    def get_programs_list(self):
        msg = json.dumps({"command": "get_programs_list", "payload": None}).encode(
            "utf-8"
        )

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=self._unpack_response(message_decoded["response"]),
        )

    def discover(self):
        msg = json.dumps({"command": "discover", "payload": None}).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=self._unpack_raw_devices(message_decoded["response"]),
        )

    @common_payload_protection(ModuleProperties)
    def get_module_properties(self, request: ModuleProperties):
        msg = json.dumps(
            {"command": "get_module_properties", "payload": {"slot": request.slot}}
        ).encode("utf-8")

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=self._unpack_raw_devices(message_decoded["response"]),
        )

    def get_device_properties(self):
        msg = json.dumps({"command": "get_device_properties", "payload": None}).encode(
            "utf-8"
        )

        self.socket.send(msg)

        message = self.socket.recv()
        message_decoded = self._decoded_message(message)

        return ServerResponse(
            status=message_decoded["status"],
            error=message_decoded["error"],
            error_message=message_decoded["error_message"],
            response=self._unpack_raw_devices(message_decoded["response"]),
        )

    def _unpack_response(self, response: dict) -> Response:
        self._logger.debug(
            f"Packing the raw response data structures into a data transfer object"
        )

        encoded = ResponseAsDataclass(**response)

        return encoded

    def _unpack_raw_tags(self, response: dict) -> Response:
        self._logger.debug(
            f"Packing the raw tag data structures into a data transfer objects"
        )
        container: list[Tag] = []

        if isinstance(response["Value"], list):
            for tag in response["Value"]:
                if tag["Array"]:
                    for index in range(tag.Size):
                        temp_tag = TagAsDataclass(**tag)
                        temp_tag.TagName += f"[{index}]"
                        container.append(temp_tag)
                else:
                    container.append(TagAsDataclass(**tag))
        else:
            if response["Value"]["Array"]:
                for index in range(response["Value"]["Size"]):
                    temp_tag = TagAsDataclass(**response["Value"])
                    temp_tag.TagName += f"[{index}]"
                    container.append(temp_tag)
            else:
                container.append(TagAsDataclass(**response["Value"]))

        self._logger.debug(
            f"Packing the raw response data structures into a data transfer object"
        )
        encoded = ResponseAsDataclass(
            TagName=response["TagName"], Status=response["Status"], Value=container
        )

        return encoded

    def _unpack_raw_devices(self, response: dict) -> Response:
        self._logger.debug(
            f"Unpacking the raw device data structures into a data transfer objects"
        )

        container: list[DeviceAsDataclass] = []
        if isinstance(response["Value"], list):
            if len(response["Value"]) > 0:
                for device in response["Value"]:
                    container.append(DeviceAsDataclass(**device))
            else:
                self._logger.debug(f"Got an empty list of devices back from pylogix")
        else:
            device = DeviceAsDataclass(**response["Value"])
            container.append(device)

        self._logger.debug(
            f"Packing the raw response data structures into a data transfer object"
        )

        encoded = ResponseAsDataclass(
            TagName=response["TagName"], Status=response["Status"], Value=container
        )

        return encoded
