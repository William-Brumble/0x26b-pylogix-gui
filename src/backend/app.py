import logging
from logging import NullHandler

from src.backend.mock import MockPLC as Pylogix
from src.backend.models import (
        ConnectReqDTO, ConnectResDTO,
        CloseReqDTO, CloseResDTO,
        GetConnectionSizeReqDTO, GetConnectionSizeResDTO,
        SetConnectionSizeReqDTO, SetConnectionSizeResDTO,
        ReadReqDTO, ReadResDTO,
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

logger = logging.getLogger()
logger.addHandler(NullHandler())

def common_exception_handler(ResponseClass):
    """ Returns error message if an exception occurs """
    def wrap(f):
        def modified_f(self, *args, **kwargs):
            try:
                return f(self, *args, **kwargs)
            except Exception as e:
                logger.error(f"exception in method {f.__name__}: {e}")
                return ResponseClass(error=True, status="500 Internal Server Error", error_message=str(e))
        return modified_f
    return wrap

def common_connection_protection(ResponseClass):
    """ Returns error message if not connected to a PLC """
    def wrap(f):
        def modified_f(self, *args, **kwargs):
            if self._plc:
                return f(self, *args, **kwargs)
            else:
                return CloseResDTO(error=True, status="412 Precondition Failed", error_message="You must be connected to a PLC before sending a request")
        return modified_f
    return wrap

class App:

    def __init__(self):
        self._plc: Pylogix | None = None

    def initialize(self):
        # perform heavy stuff here
        return True

    @common_exception_handler(ConnectResDTO)
    def connect(self, req: ConnectReqDTO) -> ConnectResDTO:
        self._plc = Pylogix(
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
        self._plc.
        return GetConnectionSizeResDTO(error=False, status="200 OK")

    @common_exception_handler(SetConnectionSizeResDTO)
    @common_connection_protection(SetConnectionSizeResDTO)
    def set_connection_size(self, req: SetConnectionSizeReqDTO) -> SetConnectionSizeResDTO:
        self._plc.
        return SetConnectionSizeResDTO(error=False, status="200 OK")

    @common_exception_handler(ReadResDTO)
    @common_connection_protection(ReadResDTO)
    def read(self, req: ReadReqDTO) -> ReadResDTO:
        self._plc.
        return ReadResDTO(error=False, status="200 OK")

    @common_exception_handler(WriteResDTO)
    @common_connection_protection(WriteResDTO)
    def write(self, req: WriteReqDTO) -> WriteResDTO:
        self._plc.
        return WriteResDTO(error=False, status="200 OK")

    @common_exception_handler(GetPlcTimeResDTO)
    @common_connection_protection(GetPlcTimeResDTO)
    def get_plc_time(self, req: GetPlcTimeReqDTO) -> GetPlcTimeResDTO:
        self._plc.
        return GetPlcTimeResDTO(error=False, status="200 OK")

    @common_exception_handler(SetPlcTimeResDTO)
    @common_connection_protection(SetPlcTimeResDTO)
    def set_plc_time(self, req: SetPlcTimeReqDTO) -> SetPlcTimeResDTO:
        self._plc.
        return SetPlcTimeResDTO(error=False, status="200 OK")

    @common_exception_handler(GetTagListResDTO)
    @common_connection_protection(GetTagListResDTO)
    def get_tag_list(self, req: GetTagListReqDTO) -> GetTagListResDTO:
        self._plc.
        return GetTagListResDTO(error=False, status="200 OK")

    @common_exception_handler(GetProgramTagListResDTO)
    @common_connection_protection(GetProgramTagListResDTO)
    def get_program_tag_list(self, req: GetProgramTagListReqDTO) -> GetProgramTagListResDTO:
        self._plc.
        return GetProgramTagListResDTO(error=False, status="200 OK")

    @common_exception_handler(GetProgramsListResDTO)
    @common_connection_protection(GetProgramsListResDTO)
    def get_programs_list(self, req: GetProgramsListReqDTO) -> GetProgramsListResDTO:
        self._plc.
        return GetProgramsListResDTO(error=False, status="200 OK")

    @common_exception_handler(DiscoverResDTO)
    @common_connection_protection(DiscoverResDTO)
    def discover(self, req: DiscoverReqDTO) -> DiscoverResDTO:
        self._plc.
        return DiscoverResDTO(error=False, status="200 OK")

    @common_exception_handler(GetModulePropertiesResDTO)
    @common_connection_protection(GetModulePropertiesResDTO)
    def get_module_properties(self, req: GetModulePropertiesReqDTO) -> GetModulePropertiesResDTO:
        self._plc.
        return GetModulePropertiesResDTO(error=False, status="200 OK")

    @common_exception_handler(GetDevicePropertiesResDTO)
    @common_connection_protection(GetDevicePropertiesResDTO)
    def get_device_properties(self, req: GetDevicePropertiesReqDTO) -> GetDevicePropertiesResDTO:
        self._plc.
        return GetDevicePropertiesResDTO(error=False, status="200 OK")

