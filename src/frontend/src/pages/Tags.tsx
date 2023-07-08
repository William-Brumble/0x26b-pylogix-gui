import { redirect, useLoaderData } from "react-router-dom";

import { IGetTagListReq, IGetTagListRes } from "@/models/get_tag_list.ts";
import { getTagList } from "@/api";
import { TagDataTable } from "@/components/TagsDataTable.tsx";
import { columns } from "@/components/TagsColumns.tsx";

export function Tags() {
    const data: any = useLoaderData();
    const encoded = data as IGetTagListRes;

    if (encoded.response?.Value) {
        return <TagDataTable columns={columns} data={encoded.response.Value} />;
    } else {
        return <div>No tags found</div>;
    }
}

export const loader = async (payload: any) => {
    try {
        const params = new URL(payload.request.url).searchParams;
        const token = params.get("token");

        const reqPayload: IGetTagListReq = {
            token: token ? token : "",
            all_tags: true,
        };

        const response: IGetTagListRes = {
            error: false,
            error_message: "200 Ok",
            status: "",
            response: {
                Status: undefined,
                TagName: undefined,
                Value: undefined,
            },
        };

        const sources = await getTagList(reqPayload);

        if (sources.error) {
            return redirect(
                `/error?title=${sources.status}&message=${sources.error_message}`
            );
        }

        response.error = sources.error;
        response.error_message = sources.error_message;
        response.status = sources.status;
        response.response = sources.response;

        return response;
    } catch (error) {
        return {
            error: true,
            error_message: `${error}`,
            status: "418 I'm a teapot",
            response: undefined,
        };
    }
};
