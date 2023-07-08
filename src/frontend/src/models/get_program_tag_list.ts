import { IPylogixTag } from "@/models/pylogix.ts";

export interface IGetProgramTagListReq {
    token: string;
    program_name: string;
}

export interface IGetProgramTagListRes {
    error: boolean;
    error_message: string;
    status: string;
    response: {
        Status: string;
        TagName: undefined;
        Value: IPylogixTag[];
    };
}
