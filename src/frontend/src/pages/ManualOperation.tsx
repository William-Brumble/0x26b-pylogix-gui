import { Separator } from "@/components/ui/separator.tsx";
import { Close } from "@/components/Close.tsx";
import { Connect } from "@/components/Connect.tsx";
import { Discover } from "@/components/Discover.tsx";
import { GetConnectionSize } from "@/components/GetConnectionSize.tsx";
import { GetDeviceProperties } from "@/components/GetDeviceProperties.tsx";
import { GetModuleProperties } from "@/components/GetModuleProperties.tsx";
import { GetPlcTime } from "@/components/GetPlcTime.tsx";
import { GetProgramsList } from "@/components/GetProgramsList.tsx";
import { GetProgramTagList } from "@/components/GetProgramTagList.tsx";
import { GetTagList } from "@/components/GetTagList.tsx";
import { Read } from "@/components/Read.tsx";
import { SetConnectionSize } from "@/components/SetConnectionSize.tsx";
import { SetPlcTime } from "@/components/SetPlcTime.tsx";
import { Write } from "@/components/Write.tsx";
import { useLoaderData, redirect } from "react-router-dom";

export function ManualOperation() {
    const { error, error_message, token }: any = useLoaderData();

    if (error) {
        alert(error_message);
    }

    return (
        <div className="bg-background p-5">
            <h2 className="text-foreground mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">
                Manual Operation
            </h2>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                This particular section is designated exclusively for manual
                operation, primarily intended to facilitate the testing of
                interprocess communication between the frontend, backend, and
                PLC.
            </p>

            <Connect token={token} />
            <Separator />

            <Close token={token} />
            <Separator />

            <Read token={token} />
            <Separator />

            <Write token={token} />
            <Separator />

            <Discover token={token} />
            <Separator />

            <GetProgramsList token={token} />
            <Separator />

            <GetProgramTagList token={token} />
            <Separator />

            <GetTagList token={token} />
            <Separator />

            <GetDeviceProperties token={token} />
            <Separator />

            <GetModuleProperties token={token} />
            <Separator />

            <GetConnectionSize token={token} />
            <Separator />

            <SetConnectionSize token={token} />
            <Separator />

            <GetPlcTime token={token} />
            <Separator />

            <SetPlcTime token={token} />
            <Separator />
        </div>
    );
}

export const loader = async (payload: any) => {
    const params = new URL(payload.request.url).searchParams;
    const token = params.get("token");

    if (token) {
        return {
            error: false,
            error_message: "no error message",
            token: token,
            data: undefined,
        };
    } else {
        return redirect("/error");
    }
};
