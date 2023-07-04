import { discover } from "@/api";
import { IDiscoverReq, IDiscoverRes } from "@/models/discover.ts";
import { redirect, useLoaderData } from "react-router-dom";

import { columns } from "@/components/SourcesColumns.tsx";
import { SourceDataTable } from "@/components/SourcesDataTable.tsx";

export function Source() {
    const { error, error_message, data }: any = useLoaderData();
    const encoded = data as IDiscoverRes;

    if (error) {
        alert(error_message);
    }

    return (
        <div className="bg-background p-5">
            <h2 className="text-foreground mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">
                Source
            </h2>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                These are all the found PLC sources on your local area network;
                you can select a tag source here.
            </p>
            <div className="w-full h-full min-h-full py-10">
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
        return redirect("/error");
    }
};
