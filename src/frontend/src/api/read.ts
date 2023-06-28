import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import { IReadReq, IReadRes } from "@/models/read.ts";

export const read = async (msg: IReadReq): Promise<IReadRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/read`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
                tag: msg.tag,
                count: msg.count,
                datatype: msg.datatype,
            }),
        }
    );

    const data: IReadRes = await response.json();
    return data;
};
