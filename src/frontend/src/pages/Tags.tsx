import { redirect, useLoaderData } from "react-router-dom";

import { IGetTagListReq, IGetTagListRes } from "@/models/get_tag_list.ts";
import { getTagList } from "@/api";
import { TagDataTable } from "@/components/TagsDataTable.tsx";
import { columns } from "@/components/TagsColumns.tsx";

export function Tags() {
    const { data }: any = useLoaderData();
    const encoded = data as IGetTagListRes;

    return (
        <div className="bg-background p-5">
            <h2 className="text-foreground mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">
                Tags
            </h2>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                These are all the tags found in the source PLC; you can select
                tags for monitoring here.
            </p>
            <div className="w-full h-full min-h-full py-10">
                <TagDataTable columns={columns} data={encoded.response.Value} />
            </div>
        </div>
    );
}
export const loader = async (payload: any) => {
    const params = new URL(payload.request.url).searchParams;
    const token = params.get("token");

    if (token) {
        const msg: IGetTagListReq = {
            token: token,
            all_tags: true,
        };

        const sources = await getTagList(msg);

        if (sources.error) {
            if (sources.status === "412 Precondition Failed") {
                alert(sources.error_message);
                return redirect("/source");
            }
        }

        return {
            data: sources,
            token: token,
        };
    } else {
        return redirect("/error");
    }
};
