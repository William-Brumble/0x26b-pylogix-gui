export interface ICloseReq {
    token: string;
}

export interface ICloseRes {
    error: boolean;
    error_message: string;
    status: string;
}
