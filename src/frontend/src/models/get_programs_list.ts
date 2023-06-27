export interface IGetProgramsListReq {
    token: string;
}

export interface IGetProgramsListRes {
    error: boolean;
    error_message: string;
    status: string;
    Status: string;
    TagName: undefined;
    Value: string[];
}
