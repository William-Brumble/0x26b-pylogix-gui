import { ReactNode } from "react";
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion.tsx";

export interface IResponseTextArea {
    title: string;
    children?: ReactNode;
}

export function AccordionItemWrapper({ title, children }: IResponseTextArea) {
    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        {title}
                    </AccordionTrigger>
                    <AccordionContent>{children}</AccordionContent>
                </AccordionItem>
            </Accordion>
        </>
    );
}
