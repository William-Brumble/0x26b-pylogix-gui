import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import {
    IGetProgramTagListReq,
    IGetProgramTagListRes,
} from "@/models/get_program_tag_list.ts";

export const getProgramTagList = async (
    msg: IGetProgramTagListReq
): Promise<IGetProgramTagListRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/get-program-tag-list`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
                program_name: msg.program_name,
            }),
        }
    );

    const objectified: IGetProgramTagListRes = await response.json();
    return objectified;
};
