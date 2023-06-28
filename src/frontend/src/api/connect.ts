import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import { IConnectReq, IConnectRes } from "@/models/connect.ts";

export const connect = async (msg: IConnectReq): Promise<IConnectRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/connect`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
                ip_address: msg.ip_address,
                slot: msg.slot,
                timeout: msg.timeout,
                Micro800: msg.Micro800,
            }),
        }
    );

    const objectified: IConnectRes = await response.json();
    return objectified;
};
