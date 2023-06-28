import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import {
    IGetModulePropertiesReq,
    IGetModulePropertiesRes,
} from "@/models/get_module_properties.ts";

export const getModuleProperties = async (
    msg: IGetModulePropertiesReq
): Promise<IGetModulePropertiesRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/get-module-properties`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
                slot: msg.slot,
            }),
        }
    );

    const objectified: IGetModulePropertiesRes = await response.json();
    return objectified;
};
