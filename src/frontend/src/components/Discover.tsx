import { useState } from "react";

import { Button } from "@/components/ui/button.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";

import { discover } from "@/api";
import { IDiscoverReq } from "@/models/discover.ts";

export interface IDiscover {
    token: string;
}

export function Discover({ token }: IDiscover) {
    const [resText, setResText] = useState("");

    const handleDiscover = async (event: any) => {
        event.preventDefault();
        const msg: IDiscoverReq = {
            token: token,
        };

        const response = await discover(msg);
        const response_stringify = JSON.stringify(response, null, "\t");
        console.log(response_stringify);
        setResText(response_stringify);
    };

    return (
        <>
            <AccordionItemWrapper title="Discover">
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Perform a network-wide query to discover all the EIP
                    (EtherNet/IP) devices present on the network. The function
                    target.raw.checkedreturns a Response class instance
                    containing the attributes: .TagName, .Value, and .Status.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleDiscover}
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
