import time
from enum import Enum
from datetime import datetime
from string import ascii_letters
from random import randint, getrandbits, choice, uniform
from logging import getLogger, NullHandler

logger = getLogger(__name__)
logger.addHandler(NullHandler())

from models import *

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
                 ip_address: str = "",
                 slot: int = 0,
                 timeout: int = 5.0,
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

    def Read(self, tag, count = 1, datatype = None) -> Response | list[Response]:
        time.sleep(0.1)

        if datatype:
            datatype = _DataType(datatype)
        if isinstance(tag, list):
            container: list[Response] = []
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
                    case _DataType.REAL:
                        val = uniform(-162142900000000000000, 162142900000000000000)
                    case _DataType.STRING:
                        val = ''.join(choice(ascii_letters) for i in range(10))
                    case _:
                        val = None
                container.append(
                    Response(TagName=x, Value=val, Status="Success")
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
                case _DataType.REAL:
                    val = uniform(-162142900000000000000, 162142900000000000000)
                case _DataType.STRING:
                    val = ''.join(choice(ascii_letters) for i in range(10))
                case _:
                    val = None
            return Response(TagName=tag, Value=val, Status="Success")

    def Write(self, tag, value = None, datatype = None) -> Response | list[Response]:
        time.sleep(0.1)

        if datatype:
            datatype = _DataType(datatype)
        if isinstance(tag, list):
            container: list[Response] = []
            for x in tag:
                container.append(
                    Response(TagName=x[0], Value=x[1], Status="Success")
                )
            return container
        else:
            return Response(TagName=tag, Value=value, Status="Success")

    def GetPLCTime(self, raw = False) -> Response:
        time.sleep(0.1)
        if raw:
            return Response(TagName=None, Value=time.time(), Status="Success")
        else:
            return Response(TagName=None, Value=datetime.now(), Status="Success")

    def SetPLCTime(self) -> Response:
        time.sleep(0.1)

        return Response(TagName=None, Value=time.time(), Status="Success")

    def GetTagList(self, allTags: bool = True) -> Response:
        time.sleep(uniform(0.1, 5))
        allowed_datatypes = [item.value for item in _DataType]

        values: list[str] = []
        for i in range(randint(1, 1000)):
            logger.warn("one")
            selected_datatype_value = choice(allowed_datatypes)
            logger.warn("two")
            selected_datatype_name = _DataType(selected_datatype_value).name
            logger.warn("three")
            temp_tag = Tag(TagName=f"tag-{selected_datatype_name}-{i}")
            logger.warn("four")
            temp_tag.DataType = selected_datatype_name
            logger.warn("five")
            temp_tag.DataTypeValue = selected_datatype_value
            logger.warn("six")
            values.append(temp_tag)

        return Response(
            TagName=None, 
            Value=values,
            Status="Success"
        )

    def GetProgramTagList(self, programName: str) -> Response:
        time.sleep(uniform(0.1, 5))
        allowed_datatypes = [item.value for item in _DataType]

        values: list[str] = []
        for i in range(randint(1, 1000)):
            selected_datatype_value = choice(allowed_datatypes)
            selected_datatype_name = _DataType(selected_datatype_value).name
            temp_tag = Tag(TagName=f"Program:{programName}.tag-{selected_datatype_name}-{i}")
            temp_tag.DataType = selected_datatype_name
            temp_tag.DataTypeValue = selected_datatype_value
            values.append(temp_tag)

        return Response(
            TagName=None, 
            Value=values,
            Status="Success"
        )

    def GetProgramsList(self) -> Response:
        time.sleep(uniform(0.1, 5))

        values: list[str] = []
        for i in range(randint(1, 1000)):
            values.append(f"Program:program-{i}")

        return Response(
            TagName=None, 
            Value=values,
            Status="Success"
        )

    def Discover(self) -> Response:
        time.sleep(uniform(0.1, 5))

        values: list[LGXDevice] = []
        for i in range(255):
            values.append(
                LGXDevice(IPAddress=f"192.168.1.{i + 1}"),
            )

        return Response(
            TagName=None, 
            Value=values,
            Status="Success"
        )

    def GetModuleProperties(self, slot) -> Response:
        time.sleep(0.1)

        device = LGXDevice(IPAddress=f"192.168.1.{randint(1, 255)}")
        return Response(
            TagName=None, 
            Value=device,
            Status="Success"
        )

    def GetDeviceProperties(self) -> Response:
        time.sleep(0.1)

        device = LGXDevice(IPAddress=self.IPAddress)
        return Response(
            TagName=None, 
            Value=device,
            Status="Success"
        )
