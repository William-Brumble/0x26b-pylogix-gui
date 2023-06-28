import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import {
    IGetConnectionSizeReq,
    IGetConnectionSizeRes,
} from "@/models/get_connection_size.ts";

export const getConnectionSize = async (
    msg: IGetConnectionSizeReq
): Promise<IGetConnectionSizeRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/get-connection-size`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
            }),
        }
    );

    const objectified: IGetConnectionSizeRes = await response.json();
    return objectified;
};
