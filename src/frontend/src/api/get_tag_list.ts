import { BACKEND_ADDRESS, BACKEND_PORT } from "@/utilities/environment.ts";
import { IGetTagListReq, IGetTagListRes } from "@/models/get_tag_list.ts";

export const getTagList = async (
    msg: IGetTagListReq
): Promise<IGetTagListRes> => {
    const response = await fetch(
        `http://${BACKEND_ADDRESS}:${BACKEND_PORT}/get-tag-list`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                token: msg.token,
                all_tags: msg.all_tags,
            }),
        }
    );

    const objectified: IGetTagListRes = await response.json();
    return objectified;
};
