import { useState } from "react";

import { Button } from "@/components/ui/button.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";

import { getDeviceProperties } from "@/api";
import { IGetConnectionSizeReq } from "@/models/get_connection_size.ts";

export interface IGetDeviceProperties {
    token: string;
}

export function GetDeviceProperties({ token }: IGetDeviceProperties) {
    const [resText, setResText] = useState("");

    const handleGetDeviceProperties = async (event: any) => {
        event.preventDefault();
        const msg: IGetConnectionSizeReq = {
            token: token,
        };

        const response = await getDeviceProperties(msg);
        const response_stringify = JSON.stringify(response, null, "\t");
        console.log(response_stringify);
        setResText(response_stringify);
    };

    return (
        <>
            <AccordionItemWrapper title="Get device properties">
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Retrieve the device properties of a device located at the
                    specified IP address. The function returns a Response class
                    instance with the attributes: .TagName, .Value, and .Status.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleGetDeviceProperties}
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
            </AccordionItemWrapper>
        </>
    );
}
