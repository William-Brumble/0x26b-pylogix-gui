import { useLoaderData } from "react-router-dom";

import { ErrorAlert } from "@/components/ErrorAlert.tsx";

export function Error() {
    const { title, message }: any = useLoaderData();

    return (
        <div className="bg-background p-0 m-0 p-5">
            <ErrorAlert title={title} description={message} />
        </div>
    );
}
export const loader = async (payload: any) => {
    try {
        const params = new URL(payload.request.url).searchParams;
        const title = params.get("title");
        const message = params.get("message");

        return { title: title, message: message };
    } catch (error) {
        return {
            title: "Error",
            response: error,
        };
    }
};
