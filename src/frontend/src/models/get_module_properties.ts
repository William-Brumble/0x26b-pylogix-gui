import { IPylogixDevice } from "@/models/pylogix.ts";

export interface IGetModulePropertiesReq {
    token: string;
    slot: number;
}

export interface IGetModulePropertiesRes {
    error: boolean;
    error_message: string;
    status: string;
    response: {
        Status: string;
        TagName: undefined;
        Value: IPylogixDevice[];
    };
}
