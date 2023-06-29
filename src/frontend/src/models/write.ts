import { IPylogixResponse } from "@/models/pylogix.ts";

export interface IWriteReq {
    token: string;
    tag: string;
    value: number;
    datatype: number;
}

export interface IWriteRes {
    error: boolean;
    error_message: string;
    status: string;
    response: IPylogixResponse[];
}
