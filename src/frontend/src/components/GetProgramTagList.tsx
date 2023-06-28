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

import { getProgramTagList } from "@/api";
import { Textarea } from "@/components/ui/textarea.tsx";

export function GetProgramTagList() {
    const handleGetProgramTagList = async (e: any) => {
        const response = await getProgramTagList();
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Get program tag list
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            Retrieve a program tag list from the PLC using the
                            programName parameter ("Program:ExampleProgram").
                            The function returns a Response class instance
                            (.TagName, .Value, .Status).
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
                            onSubmit={handleGetProgramTagList}
                        >
                            <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                                <Label
                                    htmlFor="programName"
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                >
                                    PROGRAM NAME:
                                </Label>
                                <Input
                                    type="text"
                                    name="programName"
                                    placeholder="program name"
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
