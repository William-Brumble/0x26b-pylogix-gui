import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import {
    IGetDevicePropertiesReq,
    IGetDevicePropertiesRes,
} from "@/models/get_device_properties.ts";

export const getDeviceProperties = async (
    msg: IGetDevicePropertiesReq
): Promise<IGetDevicePropertiesRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/get-device-properties`,
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

    const objectified: IGetDevicePropertiesRes = await response.json();
    return objectified;
};
