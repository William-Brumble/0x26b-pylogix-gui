import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import {
    ISetConnectionSizeReq,
    ISetConnectionSizeRes,
} from "@/models/set_connection_size.ts";

export const setConnectionSize = async (
    msg: ISetConnectionSizeReq
): Promise<ISetConnectionSizeRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/set-connection-size`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
                connection_size: msg.connection_size,
            }),
        }
    );

    const objectified: ISetConnectionSizeRes = await response.json();
    return objectified;
};
