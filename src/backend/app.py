from dataclasses import asdict
from logging import getLogger, NullHandler
from pylogix import PLC as RealPylogixPLC

from mocklogix import PLC as MockPylogixPLC
from utils import common_exception_handler
from models import (
        ResponseDTO, PLCResponseDTO,
        ConnectReqDTO, ConnectResDTO,
        CloseReqDTO, CloseResDTO,
        GetConnectionSizeReqDTO, GetConnectionSizeResDTO,
        SetConnectionSizeReqDTO, SetConnectionSizeResDTO,
        ReadReqDTO, ReadResDTO, StatusDTO,
        WriteReqDTO, WriteResDTO,
        GetPlcTimeReqDTO, GetPlcTimeResDTO,
        SetPlcTimeReqDTO, SetPlcTimeResDTO,
        GetTagListReqDTO, GetTagListResDTO,
        GetProgramTagListReqDTO, GetProgramTagListResDTO,
        GetProgramsListReqDTO, GetProgramsListResDTO,
        DiscoverReqDTO, DiscoverResDTO,
        GetModulePropertiesReqDTO, GetModulePropertiesResDTO,
        GetDevicePropertiesReqDTO, GetDevicePropertiesResDTO
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

def common_connection_protection(ResponseClass):
    """ Returns error message if not connected to a PLC """
    def wrap(f):
        def modified_f(self, *args, **kwargs):
            if self._plc:
                return f(self, *args, **kwargs)
            else:
                logger.warning(f"412 Precondition Failed: You must be connected to a PLC before sending a request")
                return StatusDTO(error=True, status="412 Precondition Failed", error_message="You must be connected to a PLC before sending a request")
        return modified_f
    return wrap

class App:

    def __init__(self, simulate: bool = False):
        self._simulate = simulate
        self._plc: MockPylogixPLC | RealPylogixPLC | None = None

    def initialize(self):
        return True

    @common_exception_handler(ConnectResDTO)
    def connect(self, req: ConnectReqDTO) -> ConnectResDTO:
        if self._simulate:
            self._plc = MockPylogixPLC(
                    ip_address=req.ip_address,
                    slot=req.slot,
                    timeout=req.timeout,
                    Micro800=req.Micro800
            )
        else:
            self._plc = RealPylogixPLC(
                    ip_address=req.ip_address,
                    slot=req.slot,
                    timeout=req.timeout,
                    Micro800=req.Micro800
            )
        return ConnectResDTO(error=False, status="200 OK")

    @common_exception_handler(CloseResDTO)
    @common_connection_protection(CloseResDTO)
    def close(self, req: CloseReqDTO) -> CloseResDTO:
        self._plc.Close()
        return CloseResDTO(error=False, status="200 OK")

    @common_exception_handler(GetConnectionSizeResDTO)
    @common_connection_protection(GetConnectionSizeResDTO)
    def get_connection_size(self, req: GetConnectionSizeReqDTO) -> GetConnectionSizeResDTO:
        connection_size = self._plc.ConnectionSize
        return GetConnectionSizeResDTO(error=False, status="200 OK", connection_size=connection_size)

    @common_exception_handler(SetConnectionSizeResDTO)
    @common_connection_protection(SetConnectionSizeResDTO)
    def set_connection_size(self, req: SetConnectionSizeReqDTO) -> SetConnectionSizeResDTO:
        self._plc.ConnectionSize = req.connection_size
        return SetConnectionSizeResDTO(error=False, status="200 OK")

    @common_exception_handler(ReadResDTO)
    @common_connection_protection(ReadResDTO)
    def read(self, req: ReadReqDTO) -> ReadResDTO:
        """ At the moment we are only implementing reading a single tag. """
        logger.debug(f"Read called with: {req}")
        responses = self._plc.Read(req.tag, req.count, req.datatype)
        logger.debug(f"Got the following response: {responses}")
        payload = self._process_plc_response(responses)
        logger.debug(f"Processed the following response: {payload}")
        return ReadResDTO(
            status="200 OK",
            responses=payload
        )

    @common_exception_handler(WriteResDTO)
    @common_connection_protection(WriteResDTO)
    def write(self, req: WriteReqDTO) -> WriteResDTO:
        """ At the moment we are only implementing writing a single tag. """
        logger.debug(f"Write called with: {req}")
        responses = self._plc.Write(req.tag, req.value, req.datatype)
        logger.debug(f"Got the following response: {responses}")
        payload = self._process_plc_response(responses)
        logger.debug(f"Processed the following response: {payload}")
        return WriteResDTO(
            status="200 OK",
            responses=payload
        )

    def _process_plc_response(self, responses: PLCResponseDTO | list[PLCResponseDTO]) -> list[ResponseDTO]:
        """ Unpack the raw response from the PLC to an internally defined ResponseDTO. """
        logger.debug(f"Processing the plc response: {responses}")
        payload: list[ResponseDTO] = []

        logger.debug("Checking if the input responses is a list")
        if isinstance(responses, list):
            logger.debug("Input responses is a list")
            for response in responses:
                logger.debug("Checking to see if the response was a success")
                if response.Status == "Success":
                    logger.debug("The response was successful")
                    temp = ResponseDTO(
                        tag=response.TagName,
                        value=response.Value,
                        status=response.Status,
                        error=False 
                    )
                    logger.debug(f"Adding the response to the list: {temp}")
                    payload.append(temp)
                else:
                    logger.debug("The response was not successful")
                    temp = ResponseDTO(
                        tag=response.TagName,
                        value=response.Value,
                        status=response.Status,
                        error=True
                    )
                    logger.debug(f"Adding the response to the list: {temp}")
                    payload.append(temp)
        else:
            logger.debug("Input responses is not a list")
            logger.debug("Checking to see if the response was a success")
            if responses.Status == "Success":
                logger.debug("The response was successful")
                response = ResponseDTO(
                        tag=responses.TagName,
                        value=responses.Value,
                        status=responses.Status,
                        error=False
                )
                logger.debug(f"Adding the response to the list: {response}")
                payload = [response,]
            else:
                logger.debug("The response was not successful")
                response = ResponseDTO(
                        tag=responses.TagName,
                        value=responses.Value,
                        status=responses.Status,
                        error=True
                )
                logger.debug(f"Adding the response to the list: {response}")
                payload = [response,]
        logger.debug(f"Processing finished with the following payload: {payload}")
        return payload

    @common_exception_handler(GetPlcTimeResDTO)
    @common_connection_protection(GetPlcTimeResDTO)
    def get_plc_time(self, req: GetPlcTimeReqDTO) -> GetPlcTimeResDTO:
        response = self._plc.GetPLCTime(raw=req.raw)
        return GetPlcTimeResDTO(error=False, status="200 OK", response=response)

    @common_exception_handler(SetPlcTimeResDTO)
    @common_connection_protection(SetPlcTimeResDTO)
    def set_plc_time(self, req: SetPlcTimeReqDTO) -> SetPlcTimeResDTO:
        response = self._plc.SetPLCTime()
        return SetPlcTimeResDTO(error=False, status="200 OK", response=response)

    @common_exception_handler(GetTagListResDTO)
    @common_connection_protection(GetTagListResDTO)
    def get_tag_list(self, req: GetTagListReqDTO) -> GetTagListResDTO:
        response = self._plc.GetTagList(allTags=req.all_tags)
        return GetTagListResDTO(error=False, status="200 OK", response=response)

    @common_exception_handler(GetProgramTagListResDTO)
    @common_connection_protection(GetProgramTagListResDTO)
    def get_program_tag_list(self, req: GetProgramTagListReqDTO) -> GetProgramTagListResDTO:
        response = self._plc.GetProgramTagList(programName=req.program_name)
        return GetProgramTagListResDTO(error=False, status="200 OK", response=response)

    @common_exception_handler(GetProgramsListResDTO)
    @common_connection_protection(GetProgramsListResDTO)
    def get_programs_list(self, req: GetProgramsListReqDTO) -> GetProgramsListResDTO:
        response = self._plc.GetProgramsList()
        return GetProgramsListResDTO(error=False, status="200 OK", response=response)

    @common_exception_handler(DiscoverResDTO)
    @common_connection_protection(DiscoverResDTO)
    def discover(self, req: DiscoverReqDTO) -> DiscoverResDTO:
        response = self._plc.Discover()
        return DiscoverResDTO(error=False, status="200 OK", response=response)

    @common_exception_handler(GetModulePropertiesResDTO)
    @common_connection_protection(GetModulePropertiesResDTO)
    def get_module_properties(self, req: GetModulePropertiesReqDTO) -> GetModulePropertiesResDTO:
        response = self._plc.GetModuleProperties(slot=req.slot)
        return GetModulePropertiesResDTO(error=False, status="200 OK", response=response)

    @common_exception_handler(GetDevicePropertiesResDTO)
    @common_connection_protection(GetDevicePropertiesResDTO)
    def get_device_properties(self, req: GetDevicePropertiesReqDTO) -> GetDevicePropertiesResDTO:
        response = self._plc.GetDeviceProperties()
        return GetDevicePropertiesResDTO(error=False, status="200 OK", response=response)

