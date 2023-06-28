import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import { ICloseReq, ICloseRes } from "@/models/close.ts";

export const close = async (msg: ICloseReq): Promise<ICloseRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/close`,
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

    const objectified: ICloseRes = await response.json();
    return objectified;
};
