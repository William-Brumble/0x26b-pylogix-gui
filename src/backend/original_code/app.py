from logging import getLogger, NullHandler
from pylogix import PLC as RealPylogixPLC

from mocklogix import PLC as MockPylogixPLC
from utils import common_exception_handler, common_connection_protection
from models import *

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class App:

    def __init__(self, simulate: bool = False):
        self._simulate = simulate

        if self._simulate:
            self._plc = MockPylogixPLC()
        else:
            self._plc = RealPylogixPLC()

    def initialize(self):
        return True

    def connect(self, req: ConnectReqDTO) -> ConnectResDTO:
        logger.debug(f"Connect called with: {req}")

        logger.debug("Checking to see if simulate mode is enabled")
        if self._simulate:
            logger.debug("Simulate mode is enabled")

            logger.debug("Creating mock plc object")
            self._plc = MockPylogixPLC(
                    ip_address=req.ip_address,
                    slot=req.slot,
                    timeout=req.timeout,
                    Micro800=req.Micro800
            )
        else:
            logger.debug("Simulate mode is not enabled")

            logger.debug("Creating real plc object")
            self._plc = RealPylogixPLC(
                    ip_address=req.ip_address,
                    slot=req.slot,
                    timeout=req.timeout,
                    Micro800=req.Micro800
            )

        return ConnectResDTO(status="200 OK")

    @common_connection_protection
    def close(self, req: CloseReqDTO) -> CloseResDTO:
        logger.debug(f"Close called with: {req}")

        logger.debug(f"Closing the connection to the PLC")
        self._plc.Close()

        if self._simulate:
            self._plc = MockPylogixPLC()
        else:
            self._plc = RealPylogixPLC()

        return CloseResDTO(status="200 OK")

    @common_connection_protection
    def get_connection_size(self, req: GetConnectionSizeReqDTO) -> GetConnectionSizeResDTO:
        logger.debug(f"Get connection size called with: {req}")

        connection_size = self._plc.ConnectionSize
        logger.debug(f"Got response: {connection_size}")

        response = PLCConnectionSizeDTO(connection_size=connection_size)

        return GetConnectionSizeResDTO(status="200 OK", response=response) 

    @common_connection_protection
    def set_connection_size(self, req: SetConnectionSizeReqDTO) -> SetConnectionSizeResDTO:
        logger.debug(f"Set connection size called with: {req}")

        logger.debug(f"Setting the connection size")
        self._plc.ConnectionSize = req.connection_size

        return SetConnectionSizeResDTO(status="200 OK")

    @common_connection_protection
    def read(self, req: ReadReqDTO) -> ReadResDTO:
        """ At the moment we are only implementing reading a single tag. """
        logger.debug(f"Read called with: {req}")

        responses = self._plc.Read(req.tag, req.count, req.datatype)
        logger.debug(f"Got the following response: {responses}")

        payload = self._process_plc_response(responses)
        logger.debug(f"Processed the following response: {payload}")

        return ReadResDTO(
            status="200 OK",
            response=payload
        )

    @common_connection_protection
    def write(self, req: WriteReqDTO) -> WriteResDTO:
        """ At the moment we are only implementing writing a single tag. """
        logger.debug(f"Write called with: {req}")

        responses = self._plc.Write(req.tag, req.value, req.datatype)
        logger.debug(f"Got the following response: {responses}")

        payload = self._process_plc_response(responses)
        logger.debug(f"Processed the following response: {payload}")

        return WriteResDTO(
            status="200 OK",
            response=payload
        )

    def _process_plc_response(self, responses: Response | list[Response]) -> list[PLCResponseDTO]:
        """ Unpack the raw response from the PLC to an internally defined ResponseDTO. """
        logger.debug(f"Processing the plc response: {responses}")
        payload: list[PLCResponseDTO] = []

        logger.debug("Checking if the input responses is a list")
        if isinstance(responses, list):

            logger.debug("Input responses is a list")
            for response in responses:

                output = self._process_individual(response)

                logger.debug(f"Adding one of the responses to the list: {output}")
                payload.append(output)

        else:
            logger.debug("Input responses is not a list")

            output = self._process_individual(responses)

            logger.debug(f"Adding the response to the list: {output}")
            payload.append(output)

        logger.debug(f"Processing finished with the following payload: {payload}")
        return payload

    def _process_individual(self, input_response: Response):
        logger.debug(f"Process individual called with: {input_response}")

        logger.debug("Checking to see if the response was a success")

        if input_response.Status == "Success":
            logger.debug("The response was successful")
        else:
            logger.debug("The response was not successful")

        logger.debug(f"Packing the raw data structure into a data transfer object")
        encoded = PLCResponseDTO(
            TagName=input_response.TagName,
            Value=input_response.Value,
            Status=input_response.Status
        )

        logger.debug(f"Adding the response to the list: {encoded}")

        return encoded

    @common_connection_protection
    def get_plc_time(self, req: GetPlcTimeReqDTO) -> GetPlcTimeResDTO:
        logger.debug(f"Get plc time called with: {req}")

        response = self._plc.GetPLCTime(raw=req.raw)
        logger.debug(f"Got response: {response}")

        encoded = self._pack_response(response)

        return GetPlcTimeResDTO(error=False, status="200 OK", response=encoded)

    @common_connection_protection
    def set_plc_time(self, req: SetPlcTimeReqDTO) -> SetPlcTimeResDTO:
        logger.debug(f"Set plc time called with: {req}")

        response = self._plc.SetPLCTime()
        logger.debug(f"Got response: {response}")

        encoded = self._pack_response(response)

        return SetPlcTimeResDTO(error=False, status="200 OK", response=encoded)

    @common_connection_protection
    def get_tag_list(self, req: GetTagListReqDTO) -> GetTagListResDTO:
        logger.debug(f"Get tag list called with: {req}")

        response = self._plc.GetTagList(allTags=req.all_tags)
        logger.debug(f"Got response: {response}")

        encoded = self._pack_raw_tags(response)

        return GetTagListResDTO(error=False, status="200 OK", response=encoded)

    @common_connection_protection
    def get_program_tag_list(self, req: GetProgramTagListReqDTO) -> GetProgramTagListResDTO:
        logger.debug(f"Get program tag list called with: {req}")

        response = self._plc.GetProgramTagList(programName=req.program_name)

        logger.debug(f"Got response: {response}")

        encoded = self._pack_raw_tags(response)

        return GetProgramTagListResDTO(error=False, status="200 OK", response=encoded)

    @common_connection_protection
    def get_programs_list(self, req: GetProgramsListReqDTO) -> GetProgramsListResDTO:
        logger.debug(f"Get programs list called with: {req}")

        response = self._plc.GetProgramsList()
        logger.debug(f"Got response: {response}")
        
        encoded = self._pack_response(response)

        return GetProgramsListResDTO(error=False, status="200 OK", response=encoded)

    def discover(self, req: DiscoverReqDTO) -> DiscoverResDTO:
        logger.debug(f"Discover called with: {req}")

        response = self._plc.Discover()
        logger.debug(f"Got response: {response}")

        logger.debug(f"Filtering to only include PLC device types")
        response.Value = [x for x in response.Value if x.DeviceID == 14]

        encoded = self._pack_raw_devices(response)

        return DiscoverResDTO(error=False, status="200 OK", response=encoded)

    @common_connection_protection
    def get_module_properties(self, req: GetModulePropertiesReqDTO) -> GetModulePropertiesResDTO:
        logger.debug(f"Get module properties called with: {req}")

        response = self._plc.GetModuleProperties(slot=req.slot)
        logger.debug(f"Got response: {response}")

        encoded = self._pack_raw_devices(response)

        return GetModulePropertiesResDTO(error=False, status="200 OK", response=encoded)

    @common_connection_protection
    def get_device_properties(self, req: GetDevicePropertiesReqDTO) -> GetDevicePropertiesResDTO:
        logger.debug(f"Get device properties called with: {req}")

        response = self._plc.GetDeviceProperties()
        logger.debug(f"Got response: {response}")

        encoded = self._pack_raw_devices(response)

        return GetDevicePropertiesResDTO(error=False, status="200 OK", response=encoded)

    def _pack_response(self, response: Response) -> PLCResponseDTO:
        logger.debug(f"Packing the raw response data structures into a data transfer object")
        encoded = PLCResponseDTO(**response.__dict__)

        return encoded

    def _pack_raw_tags(self, response: Response) -> list[PLCResponseDTO]:
        logger.debug(f"Packing the raw tag data structures into a data transfer objects")
        allowed_datatypes = [item.value for item in PylogixDataType]
        container: list[PLCTagDTO] = []

        if isinstance(response.Value, list):
            for tag in response.Value:
                if tag.DataTypeValue in allowed_datatypes:
                    if tag.Array:
                        for index in range(tag.Size):
                            temp_tag = PLCTagDTO(**tag.__dict__)
                            temp_tag.TagName += f"[{index}]"
                            container.append(temp_tag)
                    else:
                        container.append(
                            PLCTagDTO(**tag.__dict__)
                        )
        else:
            if tag.DataTypeValue in allowed_datatypes:
                if tag.Array:
                    for index in range(tag.Size):
                        temp_tag = PLCTagDTO(**tag.__dict__)
                        temp_tag.TagName += f"[{index}]"
                        container.append(temp_tag)
                else:
                    container.append(
                        PLCTagDTO(**response.Value.__dict__)
                    )
        
        logger.debug(f"Packing the raw response data structures into a data transfer object")
        encoded = PLCResponseDTO(
            TagName=response.TagName,
            Status=response.Status,
            Value=container
        )

        return encoded

    def _pack_raw_devices(self, response: Response) -> list[PLCResponseDTO]:
        logger.debug(f"Packing the raw device data structures into a data transfer objects")

        container: list[PLCDeviceDTO] = []
        if isinstance(response.Value, list):
            for device in response.Value:
                container.append(
                    PLCDeviceDTO(**device.__dict__)
                )
        else:
            device = PLCDeviceDTO(**response.Value.__dict__)
            container.append(device)
        
        logger.debug(f"Packing the raw response data structures into a data transfer object")
        encoded = PLCResponseDTO(
            TagName=response.TagName,
            Status=response.Status,
            Value=container
        )

        return encoded

