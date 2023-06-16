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

class App:

    def __init__(self):
        self._plc: Pylogix | None = None

    def initialize(self):
        # perform heavy stuff here
        return True

    def connect(self, req: ConnectReqDTO) -> ConnectResDTO:
        try:
            self._plc = Pylogix(
                    ip_address=req.ip_address,
                    slot=req.slot,
                    timeout=req.timeout,
                    Micro800=req.Micro800
            )
            return ConnectResDTO(error=False, status="200 OK")
        except Exception as e:
            logger.error(f"exception while trying to connect: {e}")
            return ConnectResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def close(self, req: CloseReqDTO) -> CloseResDTO:
        try:
            if self._plc:
                self._plc.Close()
                return CloseResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to close: {e}")
            return CloseResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def get_connection_size(self, req: GetConnectionSizeReqDTO) -> GetConnectionSizeResDTO:
        try:
            if self._plc:
                self._plc.
                return GetConnectionSizeResDTO(error=False, status="200 OK")
            else:
        except Exception as e:
            logger.error(f"exception while trying to get_connection_size: {e}")
            return GetConnectionSizeResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def set_connection_size(self, req: SetConnectionSizeReqDTO) -> SetConnectionSizeResDTO:
        try:
            if self._plc:
                self._plc.
                return SetConnectionSizeResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to set connection size: {e}")
            return SetConnectionSizeResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def read(self, req: ReadReqDTO) -> ReadResDTO:
        try:
            if self._plc:
                self._plc.
                return ReadResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to read: {e}")
            return ReadResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def write(self, req: WriteReqDTO) -> WriteResDTO:
        try:
            if self._plc:
                self._plc.
                return WriteResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to write: {e}")
            return WriteResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def get_plc_time(self, req: GetPlcTimeReqDTO) -> GetPlcTimeResDTO:
        try:
            if self._plc:
                self._plc.
                return GetPlcTimeResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to get plc time: {e}")
            return GetPlcTimeResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def set_plc_time(self, req: SetPlcTimeReqDTO) -> SetPlcTimeResDTO:
        try:
            if self._plc:
                self._plc.
                return SetPlcTimeResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to set plc time: {e}")
            return SetPlcTimeResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def get_tag_list(self, req: GetTagListReqDTO) -> GetTagListResDTO:
        try:
            if self._plc:
                self._plc.
                return GetTagListResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to get tag list: {e}")
            return GetTagListResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def get_program_tag_list(self, req: GetProgramTagListReqDTO) -> GetProgramTagListResDTO:
        try:
            if self._plc:
                self._plc.
                return GetProgramTagListResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to get program tag list: {e}")
            return GetProgramTagListResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def get_programs_list(self, req: GetProgramsListReqDTO) -> GetProgramsListResDTO:
        try:
            if self._plc:
                self._plc.
                return GetProgramsListResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to get programs list: {e}")
            return GetProgramsListResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def discover(self, req: DiscoverReqDTO) -> DiscoverResDTO:
        try:
            if self._plc:
                self._plc.
                return DiscoverResDTO(error=False, status="200 OK")
        except Exception as e
            logger.error(f"exception while trying to discover: {e}")
            return DiscoverResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def get_module_properties(self, req: GetModulePropertiesReqDTO) -> GetModulePropertiesResDTO:
        try:
            if self._plc:
                self._plc.
                return GetModulePropertiesResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to get module properties: {e}")
            return GetModulePropertiesResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

    def get_device_properties(self, req: GetDevicePropertiesReqDTO) -> GetDevicePropertiesResDTO:
        try:
            if self._plc:
                self._plc.
                return GetDevicePropertiesResDTO(error=False, status="200 OK")
            else:
        except Exception as e
            logger.error(f"exception while trying to get device properties: {e}")
            return GetDevicePropertiesResDTO(error=True, status="500 Internal Server Error", error_message=str(e))

