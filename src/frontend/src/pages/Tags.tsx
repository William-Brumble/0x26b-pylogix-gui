import {
    LoaderFunction,
    LoaderFunctionArgs,
    redirect,
    useLoaderData,
} from "react-router-dom";

import { IGetTagListReq, IGetTagListRes } from "@/models/get_tag_list.ts";
import { getTagList } from "@/api";
import { TagDataTable } from "@/components/TagsDataTable.tsx";
import { columns } from "@/components/TagsColumns.tsx";

export function Tags() {
    const { tags_response }: any = useLoaderData();
    const encoded = tags_response as IGetTagListRes;

    return <TagDataTable columns={columns} data={encoded.response.Value} />;
}

export const loader: LoaderFunction = async ({
    request,
}: LoaderFunctionArgs) => {
    try {
        const params = new URL(request.url).searchParams;
        const token = params.get("token");

        const reqPayload: IGetTagListReq = {
            token: token ? token : "",
            all_tags: true,
        };

        const tags = await getTagList(reqPayload);

        if (tags.error) {
            return redirect(
                `/error?title=${tags.status}&message=${tags.error_message}`
            );
        }

        return {
            tags_response: tags,
        };
    } catch (error) {
        return redirect(`/error?title=${"418 I'm a teapot"}&message=${error}`);
    }
};
