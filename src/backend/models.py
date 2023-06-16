from dataclasses import dataclass

@dataclass
class _StatusDTO:
    status: str
    error: bool
    error_message: str = "No error"

@dataclass
class ConnectReqDTO:
    ip_address: str
    slot: int
    timeout: int
    Micro800: bool

@dataclass
class ConnectResDTO(_StatusDTO):
    pass

@dataclass
class CloseReqDTO:
    pass

@dataclass
class CloseResDTO(_StatusDTO):
    pass

@dataclass
class GetConnectionSizeReqDTO:
    pass

@dataclass
class GetConnectionSizeResDTO(_StatusDTO):
    pass

@dataclass
class SetConnectionSizeReqDTO:
    pass

@dataclass
class SetConnectionSizeResDTO(_StatusDTO):
    pass

@dataclass
class ReadReqDTO:
    pass

@dataclass
class ReadResDTO(_StatusDTO):
    pass

@dataclass
class WriteReqDTO:
    pass

@dataclass
class WriteResDTO(_StatusDTO):
    pass

@dataclass
class GetPlcTimeReqDTO:
    pass

@dataclass
class GetPlcTimeResDTO(_StatusDTO):
    pass

@dataclass
class SetPlcTimeReqDTO:
    pass

@dataclass
class SetPlcTimeResDTO(_StatusDTO):
    pass

@dataclass
class GetTagListReqDTO:
    pass

@dataclass
class GetTagListResDTO(_StatusDTO):
    pass

@dataclass
class GetProgramTagListReqDTO:
    pass

@dataclass
class GetProgramTagListResDTO(_StatusDTO):
    pass

@dataclass
class GetProgramsListReqDTO:
    pass

@dataclass
class GetProgramsListResDTO(_StatusDTO):
    pass

@dataclass
class DiscoverReqDTO:
    pass

@dataclass
class DiscoverResDTO(_StatusDTO):
    pass

@dataclass
class GetModulePropertiesReqDTO:
    pass

@dataclass
class GetModulePropertiesResDTO(_StatusDTO):
    pass

@dataclass
class GetDevicePropertiesReqDTO:
    pass

@dataclass
class GetDevicePropertiesResDTO(_StatusDTO):
    pass

