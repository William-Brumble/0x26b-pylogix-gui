import { Suspense, useEffect } from "react";
import {
    LoaderFunction,
    LoaderFunctionArgs,
    redirect,
    useLoaderData,
    defer,
    Await,
    useNavigate,
} from "react-router-dom";

import { discover } from "@/api";
import { IDiscoverReq, IDiscoverRes } from "@/models/discover.ts";
import { columns } from "@/components/SourcesColumns.tsx";
import { SourceDataTable } from "@/components/SourcesDataTable.tsx";
import { Loading } from "@/components/Loading.tsx";

export function Source() {
    const { discover_response }: any = useLoaderData();
    const encoded = discover_response as IDiscoverRes;

    return (
        <Suspense
            fallback={
                <Loading text="Scanning the network for available sources..." />
            }
        >
            <Await resolve={encoded}>{(data) => <Table data={data} />}</Await>
        </Suspense>
    );
}

type TableProps = {
    data: IDiscoverRes;
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
        return <SourceDataTable columns={columns} data={data.response.Value} />;
    }
};

export const loader: LoaderFunction = async ({
    request,
}: LoaderFunctionArgs) => {
    try {
        const params = new URL(request.url).searchParams;
        const token = params.get("token");

        const msg: IDiscoverReq = {
            token: token ? token : "",
        };

        const sources = discover(msg);

        return defer({
            discover_response: sources,
        });
    } catch (error) {
        return redirect(`/error?title=${"418 I'm a teapot"}&message=${error}`);
    }
};
