export interface ISetConnectionSizeReq {
    token: string;
    connection_size: number;
}

export interface ISetConnectionSizeRes {
    error: boolean;
    error_message: string;
    status: string;
}
