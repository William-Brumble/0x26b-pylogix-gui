import time
from datetime import datetime
from string import ascii_letters
from random import randint, getrandbits, choice, uniform

from process_pylogix._models import *


class PLC:
    def __init__(
        self,
        ip_address: str = "",
        slot: int = 0,
        timeout: int = 5.0,
        Micro800: bool = False,
    ) -> None:
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

    def Read(self, tag, count=1, datatype=None) -> Response | list[Response]:
        time.sleep(0.1)

        if datatype:
            datatype = PylogixDataType(datatype)
        if isinstance(tag, list):
            container: list[Response] = []
            for x in tag:
                match datatype:
                    case PylogixDataType.BOOL:
                        val = bool(getrandbits(1))
                    case PylogixDataType.SINT:
                        val = randint(-128, 127)
                    case PylogixDataType.INT:
                        val = randint(-32768, 32767)
                    case PylogixDataType.DINT:
                        val = randint(-2147483648, 2147483647)
                    case PylogixDataType.REAL:
                        val = uniform(-162142900000000000000, 162142900000000000000)
                    case PylogixDataType.STRING:
                        val = "".join(choice(ascii_letters) for i in range(10))
                    case _:
                        val = None
                container.append(Response(TagName=x, Value=val, Status="Success"))
            return container
        else:
            match datatype:
                case PylogixDataType.BOOL:
                    val = bool(getrandbits(1))
                case PylogixDataType.SINT:
                    val = randint(-128, 127)
                case PylogixDataType.INT:
                    val = randint(-32768, 32767)
                case PylogixDataType.DINT:
                    val = randint(-2147483648, 2147483647)
                case PylogixDataType.REAL:
                    val = uniform(-162142900000000000000, 162142900000000000000)
                case PylogixDataType.STRING:
                    val = "".join(choice(ascii_letters) for i in range(10))
                case _:
                    val = None
            return Response(TagName=tag, Value=val, Status="Success")

    def Write(self, tag, value=None, datatype=None) -> Response | list[Response]:
        time.sleep(0.1)

        if datatype:
            datatype = PylogixDataType(datatype)
        if isinstance(tag, list):
            container: list[Response] = []
            for x in tag:
                container.append(Response(TagName=x[0], Value=x[1], Status="Success"))
            return container
        else:
            return Response(TagName=tag, Value=value, Status="Success")

    def GetPLCTime(self, raw=False) -> Response:
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
        allowedPylogixDataTypes = [item.value for item in PylogixDataType]

        values: list[str] = []
        for i in range(randint(1, 1000)):
            selectedPylogixDataType_value = choice(allowedPylogixDataTypes)
            selectedPylogixDataType_name = PylogixDataType(
                selectedPylogixDataType_value
            ).name
            temp_tag = Tag(TagName=f"tag-{selectedPylogixDataType_name}-{i}")
            temp_tag.DataType = selectedPylogixDataType_name
            temp_tag.DataTypeValue = selectedPylogixDataType_value
            values.append(temp_tag)

        return Response(TagName=None, Value=values, Status="Success")

    def GetProgramTagList(self, programName: str) -> Response:
        time.sleep(uniform(0.1, 5))
        allowedPylogixDataTypes = [item.value for item in PylogixDataType]

        values: list[str] = []
        for i in range(randint(1, 1000)):
            selectedPylogixDataType_value = choice(allowedPylogixDataTypes)
            selectedPylogixDataType_name = PylogixDataType(
                selectedPylogixDataType_value
            ).name
            temp_tag = Tag(
                TagName=f"Program:{programName}.tag-{selectedPylogixDataType_name}-{i}"
            )
            temp_tag.DataType = selectedPylogixDataType_name
            temp_tag.DataTypeValue = selectedPylogixDataType_value
            values.append(temp_tag)

        return Response(TagName=None, Value=values, Status="Success")

    def GetProgramsList(self) -> Response:
        time.sleep(uniform(0.1, 5))

        values: list[str] = []
        for i in range(randint(1, 1000)):
            values.append(f"Program:program-{i}")

        return Response(TagName=None, Value=values, Status="Success")

    def Discover(self) -> Response:
        time.sleep(uniform(0.1, 5))

        values: list[LGXDevice] = []
        for i in range(255):
            values.append(
                LGXDevice(IPAddress=f"192.168.1.{i + 1}"),
            )

        return Response(TagName=None, Value=values, Status="Success")

    def GetModuleProperties(self, slot) -> Response:
        time.sleep(0.1)

        device = LGXDevice(IPAddress=f"192.168.1.{randint(1, 255)}")
        return Response(TagName=None, Value=device, Status="Success")

    def GetDeviceProperties(self) -> Response:
        time.sleep(0.1)

        device = LGXDevice(IPAddress=self.IPAddress)
        return Response(TagName=None, Value=device, Status="Success")
