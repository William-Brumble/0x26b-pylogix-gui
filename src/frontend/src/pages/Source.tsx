import { discover } from "@/api";
import { IDiscoverReq, IDiscoverRes } from "@/models/discover.ts";
import {
    LoaderFunction,
    LoaderFunctionArgs,
    redirect,
    useLoaderData,
} from "react-router-dom";

import { columns } from "@/components/SourcesColumns.tsx";
import { SourceDataTable } from "@/components/SourcesDataTable.tsx";

export function Source() {
    const { discover_response }: any = useLoaderData();
    const encoded = discover_response as IDiscoverRes;

    return (
        <div className="bg-background p-0 m-0">
            <div className="w-full h-full min-h-full py-2">
                <SourceDataTable
                    columns={columns}
                    data={encoded.response.Value}
                />
            </div>
        </div>
    );
}

export const loader: LoaderFunction = async ({
    request,
}: LoaderFunctionArgs) => {
    try {
        const params = new URL(request.url).searchParams;
        const token = params.get("token");

        const msg: IDiscoverReq = {
            token: token ? token : "",
        };

        const sources = await discover(msg);

        if (sources.error) {
            return redirect(
                `/error?title=${sources.status}&message=${sources.error_message}`
            );
        }

        return {
            discover_response: sources,
        };
    } catch (error) {
        return redirect(`/error?title=${"418 I'm a teapot"}&message=${error}`);
    }
};
