import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import { ISetPlcTimeReq, ISetPlcTimeRes } from "@/models/set_plc_time.ts";

export const setPlcTime = async (
    msg: ISetPlcTimeReq
): Promise<ISetPlcTimeRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/set-plc-time`,
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

    const objectified: ISetPlcTimeRes = await response.json();
    return objectified;
};
