export interface IConnectReq {
    token: string;
    ip_address: string;
    slot: number;
    timeout: number;
    Micro800: boolean;
}

export interface IConnectRes {
    error: boolean;
    error_message: string;
    status: string;
}
