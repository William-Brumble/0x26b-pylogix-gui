export interface IPylogixDevice {
    DeviceID: number;
    EncapsulationVersion: number;
    IPAddress: string;
    Length: number;
    ProductCode: number;
    ProductName: string;
    ProductNameLength: number;
    Revision: number;
    SerialNumber: number;
    State: number;
    Status: number;
    Vendor: string;
    VendorID: number;
}

export interface IPylogixTag {
    Array: number;
    DataType: string;
    DataTypeValue: number | string;
    InstanceID: number;
    Size: number;
    Struct: number;
    SymbolType: number;
    TagName: string;
}

export interface IPylogixResponse {
    Status: string;
    TagName: string;
    Value: number | string | undefined;
}
