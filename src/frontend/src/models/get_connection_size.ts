export interface IGetConnectionSizeReq {
    token: string;
}

export interface IGetConnectionSizeRes {
    error: boolean;
    error_message: string;
    status: string;
    response: {
        connection_size: number;
    };
}
