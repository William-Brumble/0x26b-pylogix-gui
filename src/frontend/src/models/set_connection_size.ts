export interface ISetConnectionSizeReq {
    token: string;
    connection_size: string;
}

export interface ISetConnectionSizeRes {
    error: boolean;
    error_message: string;
    status: string;
}
