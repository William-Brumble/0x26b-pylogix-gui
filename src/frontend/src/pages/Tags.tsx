import { Suspense, useEffect } from "react";
import {
    defer,
    LoaderFunction,
    LoaderFunctionArgs,
    redirect,
    useLoaderData,
    useNavigate,
    Await,
} from "react-router-dom";

import { IGetTagListReq, IGetTagListRes } from "@/models/get_tag_list.ts";
import { getTagList } from "@/api";
import { TagDataTable } from "@/components/TagsDataTable.tsx";
import { columns } from "@/components/TagsColumns.tsx";
import { Loading } from "@/components/Loading.tsx";

export function Tags() {
    const { tags_response }: any = useLoaderData();
    const encoded = tags_response as IGetTagListRes;

    return (
        <Suspense
            fallback={
                <Loading text="Fetching all of the tags from the source PLC..." />
            }
        >
            <Await resolve={encoded}>{(data) => <Table data={data} />}</Await>
        </Suspense>
    );
}

type TableProps = {
    data: IGetTagListRes;
};
const Table = ({ data }: TableProps) => {
    const navigate = useNavigate();

    useEffect(() => {
        if (data.error) {
            navigate(
                `/error?title=${data.status}&message=${data.error_message}`
            );
        }
    }, []);

    if (!data.error) {
        return <TagDataTable columns={columns} data={data.response.Value} />;
    }
};

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

        const tags = getTagList(reqPayload);

        return defer({
            tags_response: tags,
        });
    } catch (error) {
        return redirect(`/error?title=${"418 I'm a teapot"}&message=${error}`);
    }
};
