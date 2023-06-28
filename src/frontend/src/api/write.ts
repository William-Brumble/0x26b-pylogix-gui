import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import { IWriteReq, IWriteRes } from "@/models/write.ts";

export const write = async (msg: IWriteReq): Promise<IWriteRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/write`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
                tag: msg.tag,
                value: msg.value,
                datatype: msg.datatype,
            }),
        }
    );

    const objectified: IWriteRes = await response.json();
    return objectified;
};
