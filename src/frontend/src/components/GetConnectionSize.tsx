import { useState } from "react";

import { Button } from "@/components/ui/button.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";

import { IGetConnectionSizeReq } from "@/models/get_connection_size.ts";
import { getConnectionSize } from "@/api";

export interface IGetConnectionSize {
    token: string;
}

export function GetConnectionSize({ token }: IGetConnectionSize) {
    const [resText, setResText] = useState("");

    const handleGetConnectionSize = async (event: any) => {
        event.preventDefault();
        const msg: IGetConnectionSizeReq = {
            token: token,
        };

        const response = await getConnectionSize(msg);

        const result = `BACKEND RESPONSE
        response.error: ${response.error}
        response.status: ${response.status}
        response.error_message: ${response.error_message}
        PYLOGIX RESPONSE
        response.response.connection_size: ${response.response.connection_size}`;

        setResText(result);
    };

    const Form = () => {
        return (
            <>
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    The "getConnectionSize" function retrieves and returns the
                    current connection size parameter value. It provides access
                    to the configured connection size setting, determining the
                    size of the established connection. Call this function to
                    access the specific connection size value set for your
                    system's requirements.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleGetConnectionSize}
                >
                    <Button
                        className="w-full max-w-sm"
                        type="submit"
                        value="Submit"
                    >
                        SUBMIT
                    </Button>
                </form>
                <TextAreaWrapper resText={resText} />
            </>
        );
    };

    return (
        <>
            <AccordionItemWrapper
                title="Get connection size"
                children={<Form />}
            />
        </>
    );
}
