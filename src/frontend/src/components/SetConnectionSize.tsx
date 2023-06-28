import * as React from "react";
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion.tsx";
import { Label } from "@/components/ui/label.tsx";
import { Input } from "@/components/ui/input.tsx";
import { Button } from "@/components/ui/button.tsx";

import { setConnectionSize } from "@/api";
import { Textarea } from "@/components/ui/textarea.tsx";

export function SetConnectionSize() {
    const handleSetConnectionSize = async (e: any) => {
        const response = await setConnectionSize();
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Set connection size
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            Please ensure to appropriately configure the
                            "ConnectionSize" parameter prior to initiating the
                            first call that necessitates the use of
                            "conn.connect()". By default, the system attempts a
                            Large Forward Open followed by a Small Forward Open.
                            In case an Explicit (Unconnected) session is
                            utilized, a sensible default option will be
                            automatically selected.
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
                            onSubmit={handleSetConnectionSize}
                        >
                            <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                                <Label
                                    htmlFor="connectionSize"
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                >
                                    CONNECTION SIZE:
                                </Label>
                                <Input
                                    type="number"
                                    name="connectionSize"
                                    placeholder="connection size"
                                />
                            </div>
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
