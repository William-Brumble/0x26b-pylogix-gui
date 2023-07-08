import { discover } from "@/api";
import { IDiscoverReq, IDiscoverRes } from "@/models/discover.ts";
import { useLoaderData } from "react-router-dom";

import { columns } from "@/components/SourcesColumns.tsx";
import { SourceDataTable } from "@/components/SourcesDataTable.tsx";

export function Source() {
    const { error, error_message, data }: any = useLoaderData();
    const encoded = data as IDiscoverRes;

    if (error) {
        alert(error_message);
    }

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

export const loader = async (payload: any) => {
    const params = new URL(payload.request.url).searchParams;
    const token = params.get("token");

    if (token) {
        const msg: IDiscoverReq = {
            token: token,
        };

        const sources = await discover(msg);

        return {
            error: false,
            error_message: "no error message",
            data: sources,
            token: token,
        };
    } else {
        throw new Response("Not Found", { status: 404 });
    }
};
