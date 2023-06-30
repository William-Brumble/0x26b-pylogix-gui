import { FormEvent, useState } from "react";

import { Label } from "@/components/ui/label.tsx";
import { Input } from "@/components/ui/input.tsx";
import { Button } from "@/components/ui/button.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";

import { getModuleProperties } from "@/api";
import { IGetModulePropertiesReq } from "@/models/get_module_properties.ts";

export interface IGetModuleProperties {
    token: string;
}

interface CustomElements extends HTMLFormControlsCollection {
    slot: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

export function GetModuleProperties({ token }: IGetModuleProperties) {
    const [slot, setSlot] = useState(0);
    const [resText, setResText] = useState("");

    const handleGetModuleProperties = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const msg: IGetModulePropertiesReq = {
            token: token,
            slot: slot,
        };

        const response = await getModuleProperties(msg);
        const response_stringify = JSON.stringify(response, null, "\t");
        console.log(response_stringify);
        setResText(response_stringify);
    };

    const handleSlotChange = (event: any) => {
        setSlot(parseInt(event.target.value));
    };

    return (
        <>
            <AccordionItemWrapper title="Get module properties">
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Retrieve the properties of the module located in the
                    specified slot. The function returns a Response class
                    instance with the attributes: .TagName, .Value, and .Status.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
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
                            value={slot}
                            onInput={handleSlotChange}
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
                <TextAreaWrapper resText={resText} />
            </AccordionItemWrapper>
        </>
    );
}
