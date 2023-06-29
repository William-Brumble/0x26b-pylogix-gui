import { IPylogixDevice } from "@/models/pylogix.ts";

export interface IGetDevicePropertiesReq {
    token: string;
}

export interface IGetDevicePropertiesRes {
    error: boolean;
    error_message: string;
    status: string;
    response: {
        error: boolean;
        error_message: string;
        status: string;
        Status: string;
        TagName: undefined;
        Value: IPylogixDevice;
    };
}
