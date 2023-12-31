import { FormEvent, useState } from "react";

import { Label } from "@/components/ui/label.tsx";
import { Input } from "@/components/ui/input.tsx";
import { Checkbox } from "@/components/ui/checkbox.tsx";
import { Button } from "@/components/ui/button.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";

import { connect } from "@/api";
import { IConnectReq } from "@/models/connect.ts";

export interface IConnect {
    token: string;
}

export interface IForm {
    ip_address: string;
    slot: number;
    timeout: number;
    Micro800: boolean;
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
    const [ipAddress, setIpAddress] = useState("");
    const [slot, setSlot] = useState(0);
    const [timeout, setTimeout] = useState(5);
    const [Micro800, setMicro800] = useState(false);
    const [resText, setResText] = useState("");

    const handleConnect = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const msg: IConnectReq = {
            token: token,
            ip_address: ipAddress,
            slot: slot,
            timeout: timeout,
            Micro800: Micro800,
        };

        const response = await connect(msg);
        const response_stringify = JSON.stringify(response, null, "\t");
        console.log(response_stringify);
        setResText(response_stringify);
    };

    const handleIpAddressChange = (event: any) => {
        setIpAddress(event.target.value);
    };

    const handleSlotChange = (event: any) => {
        setSlot(parseInt(event.target.value));
    };

    const handleTimeoutChange = (event: any) => {
        setTimeout(parseInt(event.target.value));
    };

    const handleMicro800Change = (_: any) => {
        setMicro800(!Micro800);
    };

    return (
        <>
            <AccordionItemWrapper title="Connect">
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Instantiate a pylogix PLC object and establish a connection
                    with the target Programmable Logic Controller (PLC).
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
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
                            className="text-foreground"
                            type="text"
                            name="ip_address"
                            placeholder="ip address"
                            value={ipAddress}
                            onInput={handleIpAddressChange}
                            required
                        />
                    </div>
                    <div className="grid w-full max-w-sm items-center gap-1.5">
                        <Label className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                            SLOT:
                        </Label>
                        <Input
                            className="text-foreground"
                            type="number"
                            name="slot"
                            placeholder="slot"
                            value={slot}
                            onInput={handleSlotChange}
                            required
                        />
                    </div>
                    <div className="grid w-full max-w-sm items-center gap-1.5">
                        <Label className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                            TIMEOUT:
                        </Label>
                        <Input
                            className="text-foreground"
                            type="number"
                            name="timeout"
                            placeholder="timeout"
                            value={timeout}
                            onInput={handleTimeoutChange}
                            required
                        />
                    </div>
                    <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                        <Checkbox
                            name="Micro800"
                            checked={Micro800}
                            onCheckedChange={handleMicro800Change}
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
                <TextAreaWrapper resText={resText} />
            </AccordionItemWrapper>
        </>
    );
}
