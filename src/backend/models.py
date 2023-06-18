from datetime import datetime
from dataclasses import dataclass

@dataclass(kw_only=True)
class StatusDTO:
    status: str = "200 OK"
    error: bool = False
    error_message: str = "No error"

@dataclass(kw_only=True)
class ConnectReqDTO:
    ip_address: str
    slot: int
    timeout: int
    Micro800: bool

@dataclass(kw_only=True)
class ConnectResDTO(StatusDTO):
    pass

@dataclass(kw_only=True)
class CloseReqDTO:
    pass

@dataclass(kw_only=True)
class CloseResDTO(StatusDTO):
    pass

@dataclass(kw_only=True)
class GetConnectionSizeReqDTO:
    pass

@dataclass(kw_only=True)
class GetConnectionSizeResDTO(StatusDTO):
    pass

@dataclass(kw_only=True)
class SetConnectionSizeReqDTO:
    connection_size: int

@dataclass
@dataclass(kw_only=True)
class SetConnectionSizeResDTO(StatusDTO):
    pass

@dataclass(kw_only=True)
class ReadReqDTO:
    tag: str
    count: int = 1
    datatype: int | None = None

@dataclass(kw_only=True)
class PLCTagDTO:
    TagName: str
    InstanceID: int = 10
    SymbolType: int = 214
    DataTypeValue: int = 1750
    DataType: str = "AB:ETHERNET_MODULE:C:O"
    Array: int = 0
    Struct: int = 1
    Size: int = 0
    AccessRight = None
    Internal = None
    Meta = None
    Scope0 = None
    Scope1 = None
    Bytes = None

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
class PLCDeviceDTO:
    Length: int = 0
    EncapsulationVersion: int = 0
    IPAddress: str
    VendorID: int = 1
    Vendor: str = 'Rockwell Automation/Allen-Bradley'
    DeviceID: int = 14
    DeviceType=None
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
                 self.DeviceType,
                 self.ProductCode,
                 self.Revision,
                 self.Status,
                 self.SerialNumber,
                 self.ProductNameLength,
                 self.ProductName,
                 self.State)

@dataclass(kw_only=True)
class PLCResponseDTO(StatusDTO):
    TagName: str | None
    Value: bool | int | str | list[str] | float | datetime | list[PLCTagDTO] | PLCDeviceDTO | list[PLCDeviceDTO] | None
    Status: str | None

    def __repr__(self):
        return 'Response(TagName={}, Value={}, Status={})'.format(
            self.TagName, self.Value, self.Status)

    def __str__(self):
        return '{} {} {}'.format(self.TagName, self.Value, self.Status)

@dataclass(kw_only=True)
class ResponseDTO(StatusDTO):
    tag: str | None
    value: bool | int | str | list[str] | float | datetime | list[PLCTagDTO] | PLCDeviceDTO | list[PLCDeviceDTO] | None
    status: str | None
    error: bool

@dataclass(kw_only=True)
class ReadResDTO(StatusDTO):
    responses: list[ResponseDTO]

@dataclass(kw_only=True)
class WriteReqDTO:
    tag: str
    value: bool | int | str
    datatype: int | None = None

@dataclass(kw_only=True)
class WriteResDTO(StatusDTO):
    responses: list[ResponseDTO]

@dataclass(kw_only=True)
class GetPlcTimeReqDTO:
    raw: bool = False

@dataclass(kw_only=True)
class GetPlcTimeResDTO(StatusDTO):
    response: PLCResponseDTO

@dataclass(kw_only=True)
class SetPlcTimeReqDTO:
    pass

@dataclass(kw_only=True)
class SetPlcTimeResDTO(StatusDTO):
    response: PLCResponseDTO

@dataclass(kw_only=True)
class GetTagListReqDTO:
    all_tags: bool = True

@dataclass(kw_only=True)
class GetTagListResDTO(StatusDTO):
    response: PLCResponseDTO

@dataclass(kw_only=True)
class GetProgramTagListReqDTO:
    program_name: str

@dataclass(kw_only=True)
class GetProgramTagListResDTO(StatusDTO):
    response: PLCResponseDTO

@dataclass(kw_only=True)
class GetProgramsListReqDTO:
    pass

@dataclass(kw_only=True)
class GetProgramsListResDTO(StatusDTO):
    response: PLCResponseDTO

@dataclass(kw_only=True)
class DiscoverReqDTO:
    pass

@dataclass(kw_only=True)
class DiscoverResDTO(StatusDTO):
    response: PLCResponseDTO

@dataclass(kw_only=True)
class GetModulePropertiesReqDTO:
    slot: int

@dataclass(kw_only=True)
class GetModulePropertiesResDTO(StatusDTO):
    response: PLCResponseDTO

@dataclass(kw_only=True)
class GetDevicePropertiesReqDTO:
    pass

@dataclass(kw_only=True)
class GetDevicePropertiesResDTO(StatusDTO):
    response: PLCResponseDTO

