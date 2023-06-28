import { FormEvent, useState } from "react";

import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion.tsx";
import { Label } from "@/components/ui/label.tsx";
import { Input } from "@/components/ui/input.tsx";
import { Checkbox } from "@/components/ui/checkbox.tsx";
import { Button } from "@/components/ui/button.tsx";
import { connect } from "@/api";
import { Textarea } from "@/components/ui/textarea.tsx";
import { IConnectReq } from "@/models/connect.ts";

export interface IConnect {
    token: string;
}
interface CustomElements extends HTMLFormControlsCollection {
    ip_address: HTMLInputElement;
    slot: HTMLInputElement;
    timeout: HTMLInputElement;
    Micro800: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

export function Connect({ token }: IConnect) {
    const [formState, setFormState] = useState({
        token: "",
        ip_address: "",
        slot: 0,
        timeout: 0,
        Micro800: false,
    });
    const [resText, setResText] = useState("");

    const handleConnect = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const target = event.currentTarget.elements;

        const msg: IConnectReq = {
            token: token,
            ip_address: target.ip_address.value,
            slot: parseInt(target.slot.value),
            timeout: parseInt(target.timeout.value),
            Micro800: target.Micro800.checked,
        };

        setFormState(msg);

        const response = await connect(msg);

        setResText(`Error: ${response.error}
        Status: ${response.status}
        Error message: ${response.error_message}`);
    };

    return (
        <>
            <Accordion type="single" collapsible>
                <AccordionItem value="item-1">
                    <AccordionTrigger className="text-foreground">
                        Connect
                    </AccordionTrigger>
                    <AccordionContent>
                        <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                            Instantiate a pylogix PLC object and establish a
                            connection with the target Programmable Logic
                            Controller (PLC).
                        </p>
                        <form
                            className="flex flex-col justify-start gap-3 p-1 m-1"
                            onSubmit={handleConnect}
                        >
                            <div className="grid max-w-sm items-center gap-1.5">
                                <Label
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                    htmlFor="ip_address"
                                >
                                    IP:
                                </Label>
                                <Input
                                    type="text"
                                    name="ip_address"
                                    placeholder="ip address"
                                    value={formState.ip_address}
                                />
                            </div>
                            <div className="grid w-full max-w-sm items-center gap-1.5">
                                <Label className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                                    SLOT:
                                </Label>
                                <Input
                                    type="number"
                                    name="slot"
                                    placeholder="slot"
                                    value={formState.slot}
                                />
                            </div>
                            <div className="grid w-full max-w-sm items-center gap-1.5">
                                <Label className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                                    TIMEOUT:
                                </Label>
                                <Input
                                    type="number"
                                    name="timeout"
                                    placeholder="timeout"
                                    value={formState.timeout}
                                />
                            </div>
                            <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                                <Checkbox
                                    name="micro800"
                                    checked={formState.Micro800}
                                />
                                <Label
                                    htmlFor="Micro800"
                                    className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                >
                                    MICRO800
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
                <Textarea
                    placeholder="Type your message here."
                    id="message"
                    value={resText}
                />
            </div>
        </>
    );
}
