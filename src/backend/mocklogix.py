import time
from enum import Enum
from datetime import datetime
from string import ascii_letters
from random import randint, getrandbits, choice
from logging import getLogger, NullHandler

logger = getLogger(__name__)
logger.addHandler(NullHandler())

from models import (
    PLCResponseDTO,
    PLCTagDTO,
    PLCDeviceDTO
)

class _DataType(Enum):
    UNKNOWN = 0x00
    STRUCT  = 0xa0
    BOOL    = 0xc1
    SINT    = 0xc2
    INT     = 0xc3
    DINT    = 0xc4
    LINT    = 0xc5
    USINT   = 0xc6
    UINT    = 0xc7
    UDINT   = 0xc8
    LWORD   = 0xc9
    REAL    = 0xca
    LREAL   = 0xcb
    DWORD   = 0xd3
    STRING  = 0xda


class PLC:
    def __init__(self,
                 ip_address: str,
                 slot: int = 0,
                 timeout: int = 5,
                 Micro800: bool = False) -> None:
        self.IPAddress = ip_address
        self.ProcessorSlot = slot
        self.SocketTimeout = timeout
        self.Micro800 = Micro800
        self._ConnectionSize: int | None = None

    @property
    def ConnectionSize(self) -> int | None:
        return self._ConnectionSize

    @ConnectionSize.setter
    def ConnectionSize(self, connection_size: int) -> None:
        self._ConnectionSize = connection_size or 508

    def Close(self) -> None:
        return

    def Read(self, tag, count = 1, datatype = None) -> PLCResponseDTO | list[PLCResponseDTO]:
        if datatype:
            datatype = _DataType(datatype)
        if isinstance(tag, list):
            container: list[PLCResponseDTO] = []
            for x in tag:
                match datatype:
                    case _DataType.BOOL:
                        val = bool(getrandbits(1))
                    case _DataType.SINT:
                        val = randint(-128, 127)
                    case _DataType.INT:
                        val = randint(-32768, 32767)
                    case _DataType.DINT:
                        val = randint(-2147483648, 2147483647)
                    case _DataType.STRING:
                        val = ''.join(choice(ascii_letters) for i in range(10))
                    case _:
                        val = None
                container.append(
                    PLCResponseDTO(TagName=x, Value=val, Status="Success")
                )
            return container
        else:
            match datatype:
                case _DataType.BOOL:
                    val = bool(getrandbits(1))
                case _DataType.SINT:
                    val = randint(-128, 127)
                case _DataType.INT:
                    val = randint(-32768, 32767)
                case _DataType.DINT:
                    val = randint(-2147483648, 2147483647)
                case _DataType.STRING:
                    val = ''.join(choice(ascii_letters) for i in range(10))
                case _:
                    val = None
            return PLCResponseDTO(TagName=tag, Value=val, Status="Success")

    def Write(self, tag, value = None, datatype = None) -> PLCResponseDTO | list[PLCResponseDTO]:
        if datatype:
            datatype = _DataType(datatype)
        if isinstance(tag, list):
            container: list[PLCResponseDTO] = []
            for x in tag:
                container.append(
                    PLCResponseDTO(TagName=x[0], Value=x[1], Status="Success")
                )
            return container
        else:
            return PLCResponseDTO(TagName=tag, Value=value, Status="Success")

    def GetPLCTime(self, raw = False) -> PLCResponseDTO:
        if raw:
            return PLCResponseDTO(TagName=None, Value=time.time(), Status="Success")
        else:
            return PLCResponseDTO(TagName=None, Value=datetime.now(), Status="Success")

    def SetPLCTime(self) -> PLCResponseDTO:
        return PLCResponseDTO(TagName=None, Value=time.time(), Status="Success")

    def GetTagList(self, allTags: bool = True) -> PLCResponseDTO:
        values=[
                PLCTagDTO(TagName="tag-one"),
                PLCTagDTO(TagName="tag-two"),
                PLCTagDTO(TagName="tag-three")
        ]
        return PLCResponseDTO(
            TagName=None, 
            Value=values,
            Status="Success"
        )

    def GetProgramTagList(self, programName: str) -> PLCResponseDTO:
        values=[
                PLCTagDTO(TagName="Program:tag-one"),
                PLCTagDTO(TagName="Program:tag-two"),
                PLCTagDTO(TagName="Program:tag-three")
        ]

        return PLCResponseDTO(
            TagName=None, 
            Value=values,
            Status="Success"
        )

    def GetProgramsList(self) -> PLCResponseDTO:
        return PLCResponseDTO(
            TagName=None, 
            Value=[
                "Program:program-one",
                "Program:program-two",
                "Program:program-three"
            ],
            Status="Success"
        )

    def Discover(self) -> PLCResponseDTO:
        values=[
                PLCDeviceDTO(IPAddress="192.168.1.100"),
                PLCDeviceDTO(IPAddress="192.168.1.101"),
                PLCDeviceDTO(IPAddress="192.168.1.102")
        ]

        return PLCResponseDTO(
            TagName=None, 
            Value=values,
            Status="Success"
        )

    def GetModuleProperties(self, slot) -> PLCResponseDTO:
        device = PLCDeviceDTO(IPAddress="192.168.1.100")
        return PLCResponseDTO(
            TagName=None, 
            Value=device,
            Status="Success"
        )

    def GetDeviceProperties(self) -> PLCResponseDTO:
        device = PLCDeviceDTO(IPAddress="192.168.1.100")
        return PLCResponseDTO(
            TagName=None, 
            Value=device,
            Status="Success"
        )
