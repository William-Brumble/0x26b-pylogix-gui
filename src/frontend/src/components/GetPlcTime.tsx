import * as React from "react";
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion.tsx";
import { Label } from "@/components/ui/label.tsx";
import { Checkbox } from "@/components/ui/checkbox.tsx";
import { Button } from "@/components/ui/button.tsx";

import { getPlcTime } from "@/api";
import { Textarea } from "@/components/ui/textarea.tsx";

export function GetPlcTime() {
    const handleGetPlcTime = async (e: any) => {
        const response = await getPlcTime();
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Get plc time
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            Retrieve the controller clock time and obtain it in
                            a human-readable format (default) or in raw format
                            if the raw parameter is set to True.
                            <br />
                            The function returns an instance of the Response
                            class, which includes the following attributes:
                            .TagName, .Value, and .Status.
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
                            onSubmit={handleGetPlcTime}
                        >
                            <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                                <Checkbox name="raw" />
                                <Label
                                    htmlFor="raw"
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                >
                                    RAW
                                </Label>
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
