import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import { IDiscoverReq, IDiscoverRes } from "@/models/discover.ts";

export const discover = async (msg: IDiscoverReq): Promise<IDiscoverRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/discover`,
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

    const objectified: IDiscoverRes = await response.json();
    return objectified;
};
