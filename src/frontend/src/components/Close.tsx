import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion.tsx";
import { Label } from "@/components/ui/label.tsx";
import { Button } from "@/components/ui/button.tsx";
import { Textarea } from "@/components/ui/textarea";

import { close } from "@/api";
import { ICloseReq } from "@/models/close.ts";

export interface IClose {
    token: string;
}

export function Close({ token }: IClose) {
    const handleClose = async () => {
        const payload: ICloseReq = {
            token: token,
        };
        const response = await close(payload);

        response.error;
        response.status;
        response.error_message;
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Close
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            Terminate the connection to the Programmable Logic
                            Controller (PLC).
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
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
                    </AccordionContent>
                </AccordionItem>
            </Accordion>

            <div className="grid w-full gap-1.5">
                <Label htmlFor="message">Response:</Label>
                <Textarea placeholder="Type your message here." id="message" />
            </div>
        </>
    );
}
