import json
from logging import (
    NullHandler,
    getLogger,
    DEBUG,
    StreamHandler,
    Formatter,
)
from logging.handlers import QueueHandler, QueueListener
import time
import multiprocessing
import zmq

from utils import *
from models import *

root_logger = getLogger()
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

root_stream_handler = StreamHandler()
root_stream_handler.setLevel(DEBUG)
root_stream_handler.setFormatter(formatter)
root_logger.addHandler(root_stream_handler)


class PylogixProcess:
    __instance = None
    __lock = multiprocessing.Lock()

    @staticmethod
    def get_instance():
        if PylogixProcess.__instance is None:
            with PylogixProcess.__lock:
                if PylogixProcess.__instance is None:
                    PylogixProcess.__instance = PylogixProcess()
        return PylogixProcess.__instance

    def __init__(
        self, pQueue, pUrl: str = "tcp://127.0.0.1:5555", pTopic: str = "pylogix"
    ):
        self._process = multiprocessing.Process(
            target=self._init,
            kwargs={"pQueue": pQueue, "pUrl": pUrl, "pTopic": pTopic},
        )

    def start(self):
        self._process.start()

    def join(self):
        self._process.join()

    def _init(self, pQueue: multiprocessing.Queue, pUrl: str, pTopic: str):
        self.logger = getLogger("pylogix-process")
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(NullHandler())
        if pQueue:
            self.handler = QueueHandler(pQueue)
            self.logger.addHandler(self.handler)

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(pUrl)

        self.socket.setsockopt(zmq.SUBSCRIBE, pTopic.encode("utf-8"))


    def _notify(self,):
        while True:
            try:
                _, msg = self.socket.recv_multipart()
                decoded_message = msg.decode("utf-8")
                self.logger.error(decoded_message)
                objectified_message = json.loads(decoded_message)
                if objectified_message.command == "stop":  # sentinel
                    break
            except Exception as e:
                print("exception", e)
            # self._delegate(objectified_message)

        # closing
        self.socket.close(linger=5)
        self.context.term()

    def _delegate(self, pMessage):
        match pMessage.command:
            case "connect":
                response = self._connect(pMessage.payload)
            case "close":
                response = self._close(pMessage.payload)
            case "get_connection_size":
                response = self._get_connection_size(pMessage.payload)
            case "set_connection_size":
                response = self._set_connection_size(pMessage.payload)
            case "read":
                response = self._read(pMessage.payload)
            case "write":
                response = self._write(pMessage.payload)
            case "get_plc_time":
                response = self._get_plc_time(pMessage.payload)
            case "set_plc_time":
                response = self._set_plc_time(pMessage.payload)
            case "get_tag_list":
                response = self._get_tag_list(pMessage.payload)
            case "get_program_tag_list":
                response = self._get_program_tag_list(pMessage.payload)
            case "get_programs_list":
                response = self._get_programs_list(pMessage.payload)
            case "discover":
                response = self._discover(pMessage.payload)
            case "get_module_properties":
                response = self._get_module_properties(pMessage.payload)
            case "get_device_properties":
                response = self._get_device_properties(pMessage.payload)
            case _:
                response = json.dumps({}).encode("utf-8")

        encoded_response = self._encode(response)
        return encoded_response

    def _encode(self, pResponse):
        stringified_response = json.dumps(pResponse)
        encoded_response = stringified_response.encode("utf-8")
        return encoded_response

    @common_payload_protection(ConnectReqDTO)
    def _connect(self, pPayload):
        self.logger.info("connect")

    @common_payload_protection(CloseReqDTO)
    def _close(self, pPayload):
        pass

    @common_payload_protection(GetConnectionSizeReqDTO)
    def _get_connection_size(self, pPayload):
        pass

    @common_payload_protection(SetConnectionSizeReqDTO)
    def _set_connection_size(self, pPayload):
        pass

    @common_payload_protection(ReadReqDTO)
    def _read(self, pPayload):
        pass

    @common_payload_protection(WriteReqDTO)
    def _write(self, pPayload):
        pass

    def _process_plc_response(self, pPayload):
        pass

    def _process_individual(self, pPayload):
        pass

    @common_payload_protection(GetPlcTimeReqDTO)
    def _get_plc_time(self, pPayload):
        pass

    @common_payload_protection(SetPlcTimeReqDTO)
    def _set_plc_time(self, pPayload):
        pass

    @common_payload_protection(GetTagListReqDTO)
    def _get_tag_list(self, pPayload):
        pass

    @common_payload_protection(GetProgramsListReqDTO)
    def _get_program_tag_list(self, pPayload):
        pass

    @common_payload_protection(GetProgramsListReqDTO)
    def _get_programs_list(self, pPayload):
        pass

    @common_payload_protection(DiscoverReqDTO)
    def _discover(self, pPayload):
        pass

    @common_payload_protection(GetModulePropertiesReqDTO)
    def _get_module_properties(self, pPayload):
        pass

    @common_payload_protection(GetDevicePropertiesReqDTO)
    def _get_device_properties(self, pPayload):
        pass

    def _pack_response(self, pPayload):
        pass

    def _pack_raw_tags(self, pPayload):
        pass

    def _pack_raw_devices(self, pPayload):
        pass


if __name__ == "__main__":
    pub_sub_url = "tcp://127.0.0.1:65534"
    pub_sub_topic = "pylogix"

    logging_queue = multiprocessing.Queue(-1)
    queue_listener = QueueListener(logging_queue, root_logger)

    main_logger = getLogger("main-process")
    main_logger.setLevel(DEBUG)
    handler = QueueHandler(logging_queue)
    main_logger.addHandler(handler)

    # main zeromq publisher
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(pub_sub_url)

    # Create a worker process
    pylogix_worker = PylogixProcess(
        pQueue=logging_queue, pUrl=pub_sub_url, pTopic=pub_sub_topic
    )
    pylogix_worker.start()

    time.sleep(0.1)  # give subscriber some time to start

    payload = {"command": "connect", "payload": "value"}
    stringified_payload = json.dumps(payload)
    encoded_payload = stringified_payload.encode("utf-8")

    for iteration in range(10):
        main_logger.info(f"sending message: {payload}")
        socket.send_multipart(
            [pub_sub_topic.encode("utf-8"), encoded_payload]
        )
        time.sleep(1)

    payload = {"command": "stop", "payload": "value"}
    stringified_payload = json.dumps(payload)
    encoded_payload = stringified_payload.encode("utf-8")
    socket.send_multipart(
        [
            pub_sub_topic.encode("utf-8"),
            encoded_payload,
        ]
    )

    pylogix_worker.join()

    main_logger.info("main is finished")
