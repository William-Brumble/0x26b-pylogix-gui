import { IPylogixDevice } from "@/models/pylogix.ts";

export interface IDiscoverReq {
    token: string;
}

export interface IDiscoverRes {
    error: boolean;
    error_message: string;
    status: string;
    response: {
        error: boolean;
        error_message: string;
        status: string;
        Status: string;
        TagName: undefined;
        Value: IPylogixDevice[];
    };
}
