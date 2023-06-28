import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import { IGetPlcTimeReq, IGetPlcTimeRes } from "@/models/get_plc_time.ts";

export const getPlcTime = async (
    msg: IGetPlcTimeReq
): Promise<IGetPlcTimeRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/get-plc-time`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
                raw: msg.raw,
            }),
        }
    );

    const objectified: IGetPlcTimeRes = await response.json();
    return objectified;
};
