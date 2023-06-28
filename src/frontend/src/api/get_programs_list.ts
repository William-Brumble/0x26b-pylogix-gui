import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import {
    IGetProgramsListReq,
    IGetProgramsListRes,
} from "@/models/get_programs_list.ts";

export const getProgramsList = async (
    msg: IGetProgramsListReq
): Promise<IGetProgramsListRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/get-programs-list`,
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

    const objectified: IGetProgramsListRes = await response.json();
    return objectified;
};
