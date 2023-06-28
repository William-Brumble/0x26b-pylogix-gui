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

import { getModuleProperties } from "@/api";
import { Textarea } from "@/components/ui/textarea.tsx";

export function GetModuleProperties() {
    const handleGetModuleProperties = async (e: any) => {
        const response = await getModuleProperties();
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Get module properties
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            Retrieve the properties of the module located in the
                            specified slot. The function returns a Response
                            class instance with the attributes: .TagName,
                            .Value, and .Status.
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
                            onSubmit={handleGetModuleProperties}
                        >
                            <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                                <Label
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                    htmlFor="slot"
                                >
                                    SLOT:
                                </Label>
                                <Input
                                    type="number"
                                    name="slot"
                                    placeholder="slot"
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
