import { IPylogixTag } from "@/models/pylogix.ts";

export interface IGetTagListReq {
    token: string;
    all_tags: boolean;
}

export interface IGetTagListRes {
    error: boolean;
    error_message: string;
    status: string;
    response?: {
        Status?: string;
        TagName?: undefined;
        Value?: IPylogixTag[];
    };
}
