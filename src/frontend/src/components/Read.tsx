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

import { read } from "@/api";
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select.tsx";
import { Textarea } from "@/components/ui/textarea.tsx";

export function Read() {
    const handleRead = async (e: any) => {
        const response = await read();
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Read
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            The function offers two reading options: retrieving
                            a single tag or an array of tags. It returns a
                            Response instance with attributes such as .TagName,
                            .Value, and .Status, providing relevant read
                            operation information. Note that only single tag
                            retrieval is currently supported; array retrieval is
                            not implemented.
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
                            onSubmit={handleRead}
                        >
                            <div className="grid w-full max-w-sm items-center gap-1.5">
                                <Label
                                    htmlFor="tag"
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                >
                                    TAG:
                                </Label>
                                <Input
                                    type="text"
                                    name="tag"
                                    placeholder="tag"
                                />
                            </div>
                            <div className="grid w-full max-w-sm items-center gap-1.5">
                                <Label
                                    htmlFor="count"
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                >
                                    COUNT:
                                </Label>
                                <Input
                                    type="number"
                                    name="count"
                                    placeholder="count"
                                />
                            </div>
                            <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                                <Label
                                    htmlFor="datatype"
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                >
                                    DATATYPE:
                                </Label>
                                <Select name="datatype">
                                    <SelectTrigger className="text-foreground w-full max-w-sm">
                                        <SelectValue placeholder="Datatype" />
                                    </SelectTrigger>
                                    <SelectContent>
                                        <SelectItem value={"0xc1"}>
                                            BOOL
                                        </SelectItem>
                                        <SelectItem value={"0xc2"}>
                                            SINT
                                        </SelectItem>
                                        <SelectItem value={"0xc3"}>
                                            INT
                                        </SelectItem>
                                        <SelectItem value={"0xc4"}>
                                            DINT
                                        </SelectItem>
                                        <SelectItem value={"0xca"}>
                                            REAL
                                        </SelectItem>
                                    </SelectContent>
                                </Select>
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
