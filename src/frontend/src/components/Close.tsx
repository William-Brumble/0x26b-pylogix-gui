import { useState } from "react";

import { Button } from "@/components/ui/button.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";

import { close } from "@/api";
import { ICloseReq } from "@/models/close.ts";

export interface IClose {
    token: string;
}

export function Close({ token }: IClose) {
    const [resText, setResText] = useState("");

    const handleClose = async (event: any) => {
        event.preventDefault();

        const msg: ICloseReq = {
            token: token,
        };

        const response = await close(msg);

        const result = `BACKEND RESPONSE
        response.error: ${response.error}
        response.status: ${response.status}
        response.error_message: ${response.error_message}`;

        setResText(result);
    };

    const Form = () => {
        return (
            <>
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Terminate the connection to the Programmable Logic
                    Controller (PLC).
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleClose}
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
            <AccordionItemWrapper title="Close" children={<Form />} />
        </>
    );
}
