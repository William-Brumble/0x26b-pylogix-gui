import zmq
import json
from dataclasses import asdict
from logging import getLogger, DEBUG, NullHandler
from logging.handlers import QueueHandler
from pylogix import PLC as RealPylogixPLC

from process_pylogix._utils import *
from process_pylogix._models import *
from process_pylogix._mocklogix import PLC as MockPylogixPLC


class Pylogix:
    def __init__(self, pylogix_url="", queue=None, simulate=True, enable_network=True):
        self._simulate = simulate
        if self._simulate:
            self._plc = MockPylogixPLC()
        else:
            self._plc = RealPylogixPLC()

        self._logger = getLogger("pylogix-process")
        self._logger.setLevel(DEBUG)
        self._logger.addHandler(NullHandler())
        if queue:
            self._handler = QueueHandler(queue)
            self._logger.addHandler(self._handler)

        if enable_network:
            self._context = zmq.Context()
            self._socket = self._context.socket(zmq.REP)
            self._socket.setsockopt(zmq.LINGER, 0)
            self._socket.connect(pylogix_url)

    def work(self):
        try:
            while True:
                msg = self._socket.recv()
                decoded_message = msg.decode("utf-8")
                objectified_message = json.loads(decoded_message)
                if objectified_message["command"] == "stop":  # sentinel
                    break

                response = self._delegate(**objectified_message)

                stringified_response = json.dumps(asdict(response))
                self._logger.info(f"Responding with: {stringified_response}")
                encoded_response = stringified_response.encode("utf-8")
                self._socket.send(encoded_response)

            self._socket.close()
            self._context.term()
        except Exception as e:
            print(e)
            self._logger.error(f"pylogix process encountered exception: {e}")
        finally:
            self._socket.close()
            self._context.term()

    @common_payload_protection(Command)
    def _delegate(self, request: Command):
        match request.command:
            case "connect":
                response = self._connect(**request.payload)
            case "close":
                response = self._close()
            case "get_connection_size":
                response = self._get_connection_size()
            case "set_connection_size":
                response = self._set_connection_size(**request.payload)
            case "read":
                response = self._read(**request.payload)
            case "write":
                response = self._write(**request.payload)
            case "get_plc_time":
                response = self._get_plc_time(**request.payload)
            case "set_plc_time":
                response = self._set_plc_time()
            case "get_tag_list":
                response = self._get_tag_list(**request.payload)
            case "get_program_tag_list":
                response = self._get_program_tag_list(**request.payload)
            case "get_programs_list":
                response = self._get_programs_list()
            case "discover":
                response = self._discover()
            case "get_module_properties":
                response = self._get_module_properties(**request.payload)
            case "get_device_properties":
                response = self._get_device_properties()
            case _:
                response = json.dumps({}).encode("utf-8")
        return response

    @common_payload_protection(Connect)
    def _connect(self, request: Connect):
        self._logger.debug(f"Connect called with: {request}")

        self._logger.debug("Checking to see if simulate mode is enabled")
        if self._simulate:
            self._logger.debug("Simulate mode is enabled")

            self._logger.debug("Creating mock plc object")
            self._plc = MockPylogixPLC(
                ip_address=request.ip_address,
                slot=request.slot,
                timeout=request.timeout,
                Micro800=request.Micro800,
            )
        else:
            self._logger.debug("Simulate mode is not enabled")

            self._logger.debug("Creating real plc object")
            self._plc = RealPylogixPLC(
                ip_address=request.ip_address,
                slot=request.slot,
                timeout=request.timeout,
                Micro800=request.Micro800,
            )

        return ServerResponse()

    def _close(self):
        self._logger.debug(f"Close called")

        self._logger.debug(f"Closing the connection to the PLC")
        self._plc.Close()

        if self._simulate:
            self._plc = MockPylogixPLC()
        else:
            self._plc = RealPylogixPLC()

        return ServerResponse()

    def _get_connection_size(self):
        self._logger.debug(f"Get connection size called")

        connection_size = self._plc.ConnectionSize
        self._logger.debug(f"Got response: {connection_size}")

        return ServerResponse(response=ConnectionSize(connection_size=connection_size))

    @common_payload_protection(ConnectionSize)
    def _set_connection_size(self, request: ConnectionSize):
        self._logger.debug(f"Set connection size called with: {request}")

        self._logger.debug(f"Setting the connection size")
        self._plc.ConnectionSize = request.connection_size

        return ServerResponse()

    @common_payload_protection(Read)
    def _read(self, request: Read):
        self._logger.debug(f"Read called with: {request}")

        responses = self._plc.Read(request.tag, request.count, request.datatype)
        self._logger.debug(f"Got the following response: {responses}")

        payload = self._process_plc_response(responses)
        self._logger.debug(f"Processed the following response: {payload}")

        return ServerResponse(response=payload)

    @common_payload_protection(Write)
    def _write(self, request: Write):
        """At the moment we are only implementing writing a single tag."""
        self._logger.debug(f"Write called with: {request}")

        responses = self._plc.Write(request.tag, request.value, request.datatype)
        self._logger.debug(f"Got the following response: {responses}")

        payload = self._process_plc_response(responses)
        self._logger.debug(f"Processed the following response: {payload}")

        return ServerResponse(response=payload)

    def _process_plc_response(
        self, responses: Response | list[Response]
    ) -> list[ResponseAsDataclass]:
        """Unpack the raw response from the PLC to an internally defined ResponseDTO."""
        self._logger.debug(f"Processing the plc response: {responses}")
        payload: list[Response] = []

        self._logger.debug("Checking if the input responses is a list")
        if isinstance(responses, list):
            self._logger.debug("Input responses is a list")
            for response in responses:
                output = self._process_individual(response)

                self._logger.debug(f"Adding one of the responses to the list: {output}")
                payload.append(output)

        else:
            self._logger.debug("Input responses is not a list")

            output = self._process_individual(responses)

            self._logger.debug(f"Adding the response to the list: {output}")
            payload.append(output)

        self._logger.debug(f"Processing finished with the following payload: {payload}")
        return payload

    def _process_individual(self, input_response: Response):
        self._logger.debug(f"Process individual called with: {input_response}")

        self._logger.debug("Checking to see if the response was a success")

        if input_response.Status == "Success":
            self._logger.debug("The response was successful")
        else:
            self._logger.debug("The response was not successful")

        self._logger.debug(
            f"Packing the raw data structure into a data transfer object"
        )
        encoded = ResponseAsDataclass(
            TagName=input_response.TagName,
            Value=input_response.Value,
            Status=input_response.Status,
        )

        return encoded

    @common_payload_protection(PlcTime)
    def _get_plc_time(self, request):
        self._logger.debug(f"Get plc time called with: {request}")

        response = self._plc.GetPLCTime(raw=request.raw)
        self._logger.debug(f"Got response: {response}")

        if isinstance(response.Value, datetime):
            response.Value = str(response.Value)

        return ServerResponse(response=self._pack_response(response))

    def _set_plc_time(self):
        self._logger.debug(f"Set plc time called")

        response = self._plc.SetPLCTime()
        self._logger.debug(f"Got response: {response}")

        return ServerResponse(response=self._pack_response(response))

    @common_payload_protection(TagList)
    def _get_tag_list(self, request):
        self._logger.debug(f"Get tag list called with: {request}")

        response = self._plc.GetTagList(allTags=request.all_tags)
        self._logger.debug(f"Got response: {response}")

        encoded = self._pack_raw_tags(response)

        return ServerResponse(response=encoded)

    @common_payload_protection(ProgramTagList)
    def _get_program_tag_list(self, request):
        self._logger.debug(f"Get program tag list called with: {request}")

        response = self._plc.GetProgramTagList(programName=request.program_name)

        self._logger.debug(f"Got response: {response}")

        encoded = self._pack_raw_tags(response)

        return ServerResponse(response=encoded)

    def _get_programs_list(self):
        self._logger.debug(f"Get programs list called")

        response = self._plc.GetProgramsList()
        self._logger.debug(f"Got response: {response}")

        return ServerResponse(response=self._pack_response(response))

    def _discover(self):
        self._logger.debug(f"Discover called")

        response = self._plc.Discover()
        self._logger.debug(f"Got response: {response}")

        self._logger.debug(f"Filtering to only include PLC device types")
        response.Value = [x for x in response.Value if x.DeviceID == 14]

        encoded = self._pack_raw_devices(response)

        return ServerResponse(response=encoded)

    @common_payload_protection(ModuleProperties)
    def _get_module_properties(self, request):
        self._logger.debug(f"Get module properties called with: {request}")

        response = self._plc.GetModuleProperties(slot=request.slot)
        self._logger.debug(f"Got response: {response}")

        encoded = self._pack_raw_devices(response)

        return ServerResponse(response=encoded)

    def _get_device_properties(self):
        self._logger.debug(f"Get device properties called")

        response = self._plc.GetDeviceProperties()
        self._logger.debug(f"Got response: {response}")

        encoded = self._pack_raw_devices(response)

        return ServerResponse(response=encoded)

    def _pack_response(self, response: Response) -> ResponseAsDataclass:
        self._logger.debug(
            f"Packing the raw response data structures into a data transfer object"
        )
        encoded = ResponseAsDataclass(**response.__dict__)

        return encoded

    def _pack_raw_tags(self, response: Response) -> ResponseAsDataclass:
        self._logger.debug(
            f"Packing the raw tag data structures into a data transfer objects"
        )
        allowed_datatypes = [item.value for item in PylogixDataType]
        container: list[TagAsDataclass] = []

        if isinstance(response.Value, list):
            for tag in response.Value:
                if tag.DataTypeValue in allowed_datatypes:
                    if tag.Array:
                        for index in range(tag.Size):
                            temp_tag = TagAsDataclass(**tag.__dict__)
                            temp_tag.TagName += f"[{index}]"
                            container.append(temp_tag)
                    else:
                        container.append(TagAsDataclass(**tag.__dict__))
        else:
            if response.Value.DataTypeValue in allowed_datatypes:
                if response.Value.Array:
                    for index in range(response.Value.Size):
                        temp_tag = TagAsDataclass(**tag.__dict__)
                        temp_tag.TagName += f"[{index}]"
                        container.append(temp_tag)
                else:
                    container.append(TagAsDataclass(**response.Value.__dict__))

        self._logger.debug(
            f"Packing the raw response data structures into a data transfer object"
        )
        encoded = ResponseAsDataclass(
            TagName=response.TagName, Status=response.Status, Value=container
        )

        return encoded

    def _pack_raw_devices(self, response: Response) -> ResponseAsDataclass:
        self._logger.debug(
            f"Packing the raw device data structures into a data transfer objects"
        )

        container: list[DeviceAsDataclass] = []
        if isinstance(response.Value, list):
            for device in response.Value:
                container.append(DeviceAsDataclass(**device.__dict__))
        else:
            device = DeviceAsDataclass(**response.Value.__dict__)
            container.append(device)

        self._logger.debug(
            f"Packing the raw response data structures into a data transfer object"
        )
        encoded = ResponseAsDataclass(
            TagName=response.TagName, Status=response.Status, Value=container
        )

        return encoded
