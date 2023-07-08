export interface ISetPlcTimeReq {
    token: string;
}

export interface ISetPlcTimeRes {
    error: boolean;
    error_message: string;
    status: string;
    response: {
        Status: string;
        TagName: undefined;
        Value: number;
    };
}
