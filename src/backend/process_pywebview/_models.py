from datetime import datetime
from enum import Enum
from typing import Any
from dataclasses import dataclass


@dataclass(kw_only=True)
class Command:
    command: str
    payload: dict


@dataclass(kw_only=True)
class Status:
    status: str = "200 OK"
    error: bool = False
    error_message: str = "No error"


@dataclass(kw_only=True)
class ServerResponse(Status):
    response: Any = None


@dataclass(kw_only=True)
class Connect:
    ip_address: str
    slot: int
    timeout: int
    Micro800: bool


@dataclass(kw_only=True)
class ConnectionSize:
    connection_size: int


@dataclass(kw_only=True)
class Read:
    tag: str
    count: int = 1
    datatype: int | None = None


@dataclass(kw_only=True)
class Write:
    tag: str
    value: bool | int | str
    datatype: int | None = None


@dataclass(kw_only=True)
class PlcTime:
    raw: bool = False


@dataclass(kw_only=True)
class TagList:
    all_tags: bool = True


@dataclass(kw_only=True)
class ProgramTagList:
    program_name: str


@dataclass(kw_only=True)
class ModuleProperties:
    slot: int


class PylogixDataType(Enum):
    UNKNOWN = 0x00
    STRUCT = 0xA0
    BOOL = 0xC1
    SINT = 0xC2
    INT = 0xC3
    DINT = 0xC4
    LINT = 0xC5
    USINT = 0xC6
    UINT = 0xC7
    UDINT = 0xC8
    LWORD = 0xC9
    REAL = 0xCA
    LREAL = 0xCB
    DWORD = 0xD3
    STRING = 0xDA

@dataclass(kw_only=True)
class DeviceAsDataclass:
    Length: int = 0
    EncapsulationVersion: int = 0
    IPAddress: str
    VendorID: int = 1
    Vendor: str = 'Rockwell Automation/Allen-Bradley'
    DeviceID: int = 14
    DeviceType: str ="Programmable Logic Controller"
    ProductCode: int = 167
    Revision: float = 20.00
    Status: int = 12384
    SerialNumber: int = 0xffffff
    ProductNameLength: int = 11
    ProductName: str = "1756-L84E/B"
    State: int = 66

    def __repr__(self):
        props = ''
        props += 'Length={}, '.format(self.Length)
        props += 'EncapsulationVersion={}, '.format(self.EncapsulationVersion)
        props += 'IPAddress={}, '.format(self.IPAddress)
        props += 'VendorID={}, '.format(self.VendorID)
        props += 'Vendor={}, '.format(self.Vendor)
        props += 'DeviceID={}, '.format(self.DeviceID)
        props += 'DeviceType={}, '.format(self.DeviceType)
        props += 'ProductCode={}, '.format(self.ProductCode)
        props += 'Revision={}, '.format(self.Revision)
        props += 'Status={}, '.format(self.Status)
        props += 'SerialNumber={}, '.format(self.SerialNumber)
        props += 'ProductNameLength={}, '.format(self.ProductNameLength)
        props += 'ProductName={}, '.format(self.ProductName)
        props += 'State={}'.format(self.State)
        return 'LGXDevice({})'.format(props)

    def __str__(self):
        ret = "{} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(
                 self.Length,
                 self.EncapsulationVersion,
                 self.IPAddress,
                 self.VendorID,
                 self.Vendor,
                 self.DeviceID,
                 self.DeviceType or "",
                 self.ProductCode,
                 self.Revision,
                 self.Status,
                 self.SerialNumber,
                 self.ProductNameLength,
                 self.ProductName,
                 self.State)
        return ret


class LGXDevice:
    def __init__(
        self,
        IPAddress: str,
        Length: int = 0,
        EncapsulationVersion: int = 0,
        VendorID: int = 1,
        Vendor: str = "Rockwell Automation/Allen-Bradley",
        DeviceID: int = 14,
        DeviceType: str | None = None,
        ProductCode: int = 167,
        Revision: float = 20.00,
        Status: int = 12384,
        SerialNumber: int = 0xFFFFFF,
        ProductNameLength: int = 11,
        ProductName: str = "1756-L84E/B",
        State: int = 66,
    ):
        self.IPAddress = IPAddress
        self.Length = Length
        self.EncapsulationVersion = EncapsulationVersion
        self.VendorID = VendorID
        self.Vendor = Vendor
        self.DeviceID = DeviceID
        self.DeviceType = DeviceType
        self.ProductCode = ProductCode
        self.Revision = Revision
        self.Status = Status
        self.SerialNumber = SerialNumber
        self.ProductNameLength = ProductNameLength
        self.ProductName = ProductName
        self.State = State

    def __repr__(self):
        props = ""
        props += "Length={}, ".format(self.Length)
        props += "EncapsulationVersion={}, ".format(self.EncapsulationVersion)
        props += "IPAddress={}, ".format(self.IPAddress)
        props += "VendorID={}, ".format(self.VendorID)
        props += "Vendor={}, ".format(self.Vendor)
        props += "DeviceID={}, ".format(self.DeviceID)
        props += "DeviceType={}, ".format(self.DeviceType or "")
        props += "ProductCode={}, ".format(self.ProductCode)
        props += "Revision={}, ".format(self.Revision)
        props += "Status={}, ".format(self.Status)
        props += "SerialNumber={}, ".format(self.SerialNumber)
        props += "ProductNameLength={}, ".format(self.ProductNameLength)
        props += "ProductName={}, ".format(self.ProductName)
        props += "State={}".format(self.State)
        return "LGXDevice({})".format(props)

    def __str__(self):
        ret = "{} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(
            self.Length,
            self.EncapsulationVersion,
            self.IPAddress,
            self.VendorID,
            self.Vendor,
            self.DeviceID,
            self.DeviceType or "",
            self.ProductCode,
            self.Revision,
            self.Status,
            self.SerialNumber,
            self.ProductNameLength,
            self.ProductName,
            self.State,
        )
        return ret

@dataclass(kw_only=True)
class TagAsDataclass:
    TagName: str
    InstanceID: int = 10
    SymbolType: int = 214
    DataTypeValue: int = 0xca
    DataType: str = "REAL"
    Array: int = 0
    Struct: int = 1
    Size: int = 0
    AccessRight: None = None
    Internal: None = None
    Meta: None = None
    Scope0: None = None
    Scope1: None = None
    Bytes: None = None

    def __repr__(self):
        props = ''
        props += 'TagName={}, '.format(self.TagName)
        props += 'InstanceID={}, '.format(self.InstanceID)
        props += 'SymbolType={}, '.format(self.SymbolType)
        props += 'DataTypeValue={}, '.format(self.DataTypeValue)
        props += 'DataType={}, '.format(self.DataType)
        props += 'Array={}, '.format(self.Array)
        props += 'Struct={}, '.format(self.Struct)
        props += 'Size={} '.format(self.Size)
        props += 'AccessRight={} '.format(self.AccessRight)
        props += 'Internal={} '.format(self.Internal)
        props += 'Meta={} '.format(self.Meta)
        props += 'Scope0={} '.format(self.Scope0)
        props += 'Scope1={} '.format(self.Scope1)
        props += 'Bytes={}'.format(self.Bytes)

        return 'Tag({})'.format(props)

    def __str__(self):

        return '{} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(
                self.TagName,
                self.InstanceID,
                self.SymbolType,
                self.DataTypeValue,
                self.DataType,
                self.Array,
                self.Struct,
                self.Size,
                self.AccessRight,
                self.Internal,
                self.Meta,
                self.Scope0,
                self.Scope1,
                self.Bytes)

class Tag:
    def __init__(self,
                 TagName: str,
                 InstanceID: int = 10,
                 SymbolType: int = 214,
                 DataTypeValue: int = 0xca,
                 DataType: str = "REAL",
                 Array: int = 0,
                 Struct: int = 1,
                 Size: int = 0,
                 AccessRight = None,
                 Internal = None,
                 Meta = None,
                 Scope0 = None,
                 Scope1 = None,
                 Bytes = None):
        self.TagName = TagName
        self.InstanceID = InstanceID
        self.SymbolType = SymbolType
        self.DataTypeValue = DataTypeValue
        self.DataType = DataType
        self.Array = Array
        self.Struct = Struct
        self.Size = Size
        self.AccessRight = AccessRight
        self.Internal = Internal
        self.Meta = Meta
        self.Scope0 = Scope0
        self.Scope1 = Scope1
        self.Bytes = Bytes

    def __repr__(self):
        props = ''
        props += 'TagName={}, '.format(self.TagName)
        props += 'InstanceID={}, '.format(self.InstanceID)
        props += 'SymbolType={}, '.format(self.SymbolType)
        props += 'DataTypeValue={}, '.format(self.DataTypeValue)
        props += 'DataType={}, '.format(self.DataType)
        props += 'Array={}, '.format(self.Array)
        props += 'Struct={}, '.format(self.Struct)
        props += 'Size={} '.format(self.Size)
        props += 'AccessRight={} '.format(self.AccessRight)
        props += 'Internal={} '.format(self.Internal)
        props += 'Meta={} '.format(self.Meta)
        props += 'Scope0={} '.format(self.Scope0)
        props += 'Scope1={} '.format(self.Scope1)
        props += 'Bytes={}'.format(self.Bytes)

        return 'Tag({})'.format(props)

    def __str__(self):

        return '{} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(
                self.TagName,
                self.InstanceID,
                self.SymbolType,
                self.DataTypeValue,
                self.DataType,
                self.Array,
                self.Struct,
                self.Size,
                self.AccessRight,
                self.Internal,
                self.Meta,
                self.Scope0,
                self.Scope1,
                self.Bytes)

@dataclass(kw_only=True)
class ResponseAsDataclass:
    TagName: str | None
    Value: bool | int | str | list[str] | float | datetime | list[Tag] | LGXDevice | list[LGXDevice] | None
    Status: str | None

    def __repr__(self):

        return 'Response(TagName={}, Value={}, Status={})'.format(
            self.TagName, self.Value, self.Status)

    def __str__(self):

        return '{} {} {}'.format(self.TagName, self.Value, self.Status)

class Response:
    def __init__(
        self,
        TagName: str | None,
        Value: bool
        | int
        | str
        | list[str]
        | float
        | datetime
        | list[Tag]
        | LGXDevice
        | list[LGXDevice]
        | None,
        Status: str | None,
    ):
        self.TagName = TagName
        self.Value = Value
        self.Status = Status

    def __repr__(self):
        return "Response(TagName={}, Value={}, Status={})".format(
            self.TagName, self.Value, self.Status
        )

    def __str__(self):
        return "{} {} {}".format(self.TagName, self.Value, self.Status)
