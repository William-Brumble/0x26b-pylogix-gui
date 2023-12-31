export interface IGetPlcTimeReq {
    token: string;
    raw: boolean;
}

export interface IGetPlcTimeRes {
    error: boolean;
    error_message: string;
    status: string;
    response: {
        Status: string;
        TagName: undefined;
        Value: number | Date;
    };
}
