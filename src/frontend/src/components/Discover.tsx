import * as React from "react";
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion.tsx";
import { Label } from "@/components/ui/label.tsx";
import { Button } from "@/components/ui/button.tsx";

import { discover } from "@/api";
import { Textarea } from "@/components/ui/textarea.tsx";

export function Discover() {
    const handleDiscover = async (e: any) => {
        const response = await discover();
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Discover
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            Perform a network-wide query to discover all the EIP
                            (EtherNet/IP) devices present on the network. The
                            function returns a Response class instance
                            containing the attributes: .TagName, .Value, and
                            .Status.
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
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
