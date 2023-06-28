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

import { getTagList } from "@/api";
import { Textarea } from "@/components/ui/textarea.tsx";

export function GetTagList() {
    const handleGetTagList = async (e: any) => {
        const response = await getTagList();
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Get tag list
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            Retrieve the tag list from the PLC, with the
                            optional parameter allTags. If allTags is set to
                            False, only controller tags are returned; otherwise,
                            both controller tags and program tags are returned.
                            The function returns a Response class instance
                            (.TagName, .Value, .Status).
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
                            onSubmit={handleGetTagList}
                        >
                            <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                                <Checkbox name="allTags" />
                                <Label
                                    htmlFor="allTags"
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                >
                                    ALL TAGS
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
