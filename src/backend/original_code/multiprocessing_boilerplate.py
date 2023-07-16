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

    def __init__(self,
              pQueue: multiprocessing.Queue, 
              pRequest_url: str, pRequest_topic: str, 
              pResponse_url: str, pResponse_topic: str):
        self._process = multiprocessing.Process(
            daemon=True,
            target=self._init,
            kwargs={
                "pQueue": pQueue, 
                "pRequest_url": pRequest_url, 
                "pRequest_topic": pRequest_topic, 
                "pResponse_url": pResponse_url, 
                "pResponse_topic":pResponse_topic 
            },
        )

    def start(self):
        self._process.start()

    def join(self):
        self._process.join()

    def _init(self, 
              pQueue: multiprocessing.Queue, 
              pRequest_url: str, pRequest_topic: str, 
              pResponse_url: str, pResponse_topic: str):
        """This init takes place after multiprocessing copies python state
        to the new process and is needed to allow this new process to own
        these member variables"""
        self.logger = getLogger("pylogix-process")
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(NullHandler())
        if pQueue:
            self.handler = QueueHandler(pQueue)
            self.logger.addHandler(self.handler)

        self.context = zmq.Context()
        self.request_socket = self.context.socket(zmq.SUB)
        self.request_socket.connect(pRequest_url)
        self.request_socket.setsockopt(zmq.SUBSCRIBE, pRequest_topic.encode("utf-8"))

        self.response_context = zmq.Context()
        self.response_socket = context.socket(zmq.PUB)
        self.response_socket.bind("tcp://127.0.0.1:5112")
        self.response_topic = "response_topic"

        self._notify()

    def _notify(self):
        try:
            x = 0
            while True:
                time.sleep(0.1)
                x + 1
                if x > 100:
                    break
                """
                _, msg = self.request_socket.recv_multipart()
                decoded_message = msg.decode("utf-8")
                objectified_message = json.loads(decoded_message)
                if objectified_message.command == "stop":  # sentinel
                    break

                response = self._delegate(objectified_message)
                self.logger.info(f"Got message: {response}")


                stringified_response = json.dumps(response)
                encoded_response = stringified_response.encode("utf-8")
                self.request_socket.send_multipart([self.response_topic.encode("utf-8"), encoded_response])
                """

            self.request_socket.close(linger=5)
            self.context.term()
        except Exception as e:
            self.logger.error("exception", e)
            self.request_socket.close(linger=5)
            self.context.term()
            

    @common_payload_protection(PylogixCommandDTO)
    def _delegate(self, request: PylogixCommandDTO):
        match request.command:
            case "connect":
                response = self._connect(request.payload)
            case "close":
                response = self._close(request.payload)
            case "get_connection_size":
                response = self._get_connection_size(request.payload)
            case "set_connection_size":
                response = self._set_connection_size(request.payload)
            case "read":
                response = self._read(request.payload)
            case "write":
                response = self._write(request.payload)
            case "get_plc_time":
                response = self._get_plc_time(request.payload)
            case "set_plc_time":
                response = self._set_plc_time(request.payload)
            case "get_tag_list":
                response = self._get_tag_list(request.payload)
            case "get_program_tag_list":
                response = self._get_program_tag_list(request.payload)
            case "get_programs_list":
                response = self._get_programs_list(request.payload)
            case "discover":
                response = self._discover(request.payload)
            case "get_module_properties":
                response = self._get_module_properties(request.payload)
            case "get_device_properties":
                response = self._get_device_properties(request.payload)
            case _:
                response = json.dumps({}).encode("utf-8")

        encoded_response = self._encode(response)
        return encoded_response

    def _encode(self, pResponse):
        stringified_response = json.dumps(pResponse)
        encoded_response = stringified_response.encode("utf-8")
        return encoded_response

    @common_payload_protection(ConnectReqDTO)
    def _connect(self, request):
        self.logger.info("connect")

    @common_payload_protection(CloseReqDTO)
    def _close(self, request):
        pass

    @common_payload_protection(GetConnectionSizeReqDTO)
    def _get_connection_size(self, request):
        pass

    @common_payload_protection(SetConnectionSizeReqDTO)
    def _set_connection_size(self, request):
        pass

    @common_payload_protection(ReadReqDTO)
    def _read(self, request):
        pass

    @common_payload_protection(WriteReqDTO)
    def _write(self, request):
        pass

    def _process_plc_response(self, request):
        pass

    def _process_individual(self, request):
        pass

    @common_payload_protection(GetPlcTimeReqDTO)
    def _get_plc_time(self, request):
        pass

    @common_payload_protection(SetPlcTimeReqDTO)
    def _set_plc_time(self, request):
        pass

    @common_payload_protection(GetTagListReqDTO)
    def _get_tag_list(self, request):
        pass

    @common_payload_protection(GetProgramsListReqDTO)
    def _get_program_tag_list(self, request):
        pass

    @common_payload_protection(GetProgramsListReqDTO)
    def _get_programs_list(self, request):
        pass

    @common_payload_protection(DiscoverReqDTO)
    def _discover(self, request):
        pass

    @common_payload_protection(GetModulePropertiesReqDTO)
    def _get_module_properties(self, request):
        pass

    @common_payload_protection(GetDevicePropertiesReqDTO)
    def _get_device_properties(self, request):
        pass

    def _pack_response(self, request):
        pass

    def _pack_raw_tags(self, request):
        pass

    def _pack_raw_devices(self, request):
        pass


if __name__ == "__main__":

    try:
        response_topic = "response"
        port = 65025
        response_url = f"tcp://127.0.0.1:{port}"
        request_topic = "request"
        request_url = f"tcp://127.0.0.1:{port + 1}"

        logging_queue = multiprocessing.Queue(-1)
        queue_listener = QueueListener(logging_queue, root_logger)

        main_logger = getLogger("main-process")
        main_logger.setLevel(DEBUG)
        handler = QueueHandler(logging_queue)
        main_logger.addHandler(handler)

        # main zeromq publisher
        context = zmq.Context()
        request_socket = context.socket(zmq.PUB)
        request_socket.bind(request_url)
        response_socket = context.socket(zmq.SUB)
        response_socket.connect(response_url)
        response_socket.setsockopt(zmq.SUBSCRIBE, response_topic.encode("utf-8"))

        # Create a worker process
        pylogix_worker = PylogixProcess(
            pQueue=logging_queue,
            pRequest_url=request_url,
            pRequest_topic=request_topic,
            pResponse_url=response_url,
            pResponse_topic=response_topic
        )
        pylogix_worker.start()

        """
        time.sleep(.1)  # give subscriber some time to start

        payload = {"command": "connect", "payload": "value"}
        stringified_payload = json.dumps(payload)
        encoded_payload = stringified_payload.encode("utf-8")

        main_logger.info(f"sending message: {payload}")
        request_socket.send_multipart([request_topic.encode("utf-8"), encoded_payload])

        _, msg = response_socket.recv_multipart()
        decoded_message = msg.decode("utf-8")
        objectified_message = json.loads(decoded_message)
        main_logger.info(f"Got response {objectified_message}")

        time.sleep(0.1)

        payload = {"command": "stop", "payload": "value"}
        stringified_payload = json.dumps(payload)
        encoded_payload = stringified_payload.encode("utf-8")
        main_logger.info(f"sending message: {payload}")
        request_socket.send_multipart(
            [
                request_topic.encode("utf-8"),
                encoded_payload,
            ]
        )

        """
        pylogix_worker.join()

        main_logger.info("main is finished")
    except Exception as e:
        print(e)
