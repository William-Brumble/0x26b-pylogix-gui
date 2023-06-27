export interface ISetPlcTime {
    token: string;
}

export interface ISetPlcTimeRes {
    error: boolean;
    error_message: string;
    status: string;
    Status: string;
    TagName: undefined;
    Value: number;
}
