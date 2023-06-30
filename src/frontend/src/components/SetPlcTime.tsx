import { useState } from "react";

import { Button } from "@/components/ui/button.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";

import { setPlcTime } from "@/api";
import { ISetPlcTimeReq } from "@/models/set_plc_time.ts";

export interface ISetPlcTime {
    token: string;
}

export function SetPlcTime({ token }: ISetPlcTime) {
    const [resText, setResText] = useState("");

    const handleSetPlcTime = async (event: any) => {
        event.preventDefault();

        const msg: ISetPlcTimeReq = {
            token: token,
        };

        const response = await setPlcTime(msg);
        const response_stringify = JSON.stringify(response, null, "\t");
        console.log(response_stringify);
        setResText(response_stringify);
    };

    return (
        <>
            <AccordionItemWrapper title="Set plc time">
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    This function is utilized to set the controller clock time.
                    <br />
                    Upon execution, the function returns an instance of the
                    Response class, which encompasses the following attributes:
                    .TagName, .Value, and .Status.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleSetPlcTime}
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
