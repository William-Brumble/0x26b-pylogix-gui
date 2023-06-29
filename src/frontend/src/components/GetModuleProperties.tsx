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
    const [formState, setFormState] = useState({
        slot: 0,
    });
    const [resText, setResText] = useState("");

    const handleGetModuleProperties = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const target = event.currentTarget.elements;

        const msg: IGetModulePropertiesReq = {
            token: token,
            slot: parseInt(target.slot.value),
        };

        setFormState(msg);

        const response = await getModuleProperties(msg);

        const result = `BACKEND RESPONSE
        response.error: ${response.error}
        response.status: ${response.status}
        response.error_message: ${response.error_message}
        PYLOGIX RESPONSE
        ${response.response.Status}
        ${response.response.TagName}
        DEVICE
        DeviceID: ${response.response.Value.DeviceID}
        EncapsulationVersion: ${response.response.Value.EncapsulationVersion}
        IPAddress: ${response.response.Value.IPAddress}
        Length: ${response.response.Value.Length}
        ProductCode: ${response.response.Value.ProductCode}
        ProductName: ${response.response.Value.ProductName}
        ProductNameLength: ${response.response.Value.ProductNameLength}
        Revision: ${response.response.Value.Revision}
        SerialNumber: ${response.response.Value.SerialNumber}
        State: ${response.response.Value.State}
        Status: ${response.response.Value.Status}
        Vendor: ${response.response.Value.Vendor}
        VendorID: ${response.response.Value.VendorID}`;

        setResText(result);
    };

    const Form = () => {
        return (
            <>
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
                            defaultValue={formState.slot}
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
            </>
        );
    };

    return (
        <>
            <AccordionItemWrapper
                title="Get module properties"
                children={<Form />}
            />
        </>
    );
}
