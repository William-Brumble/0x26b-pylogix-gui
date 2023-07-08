import { IPylogixDevice } from "@/models/pylogix.ts";

export interface IGetDevicePropertiesReq {
    token: string;
}

export interface IGetDevicePropertiesRes {
    error: boolean;
    error_message: string;
    status: string;
    response: {
        Status: string;
        TagName: undefined;
        Value: IPylogixDevice[];
    };
}
