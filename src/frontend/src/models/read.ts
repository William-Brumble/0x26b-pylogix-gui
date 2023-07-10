import { IPylogixResponse } from "@/models/pylogix.ts";

export interface IReadReq {
    token: string;
    tag: string;
    count: number;
    datatype: number | string;
}

export interface IReadRes {
    error: boolean;
    error_message: string;
    status: string;
    response: IPylogixResponse[];
}
