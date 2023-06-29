import { FormEvent, useState } from "react";

import { Label } from "@/components/ui/label.tsx";
import { Checkbox } from "@/components/ui/checkbox.tsx";
import { Button } from "@/components/ui/button.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";

import { getPlcTime } from "@/api";
import { IGetPlcTimeReq } from "@/models/get_plc_time.ts";

export interface IGetPlcTime {
    token: string;
}

interface CustomElements extends HTMLFormControlsCollection {
    raw: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

export function GetPlcTime({ token }: IGetPlcTime) {
    const [formState, setFormState] = useState({
        raw: false,
    });
    const [resText, setResText] = useState("");

    const handleGetPlcTime = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const target = event.currentTarget.elements;

        const msg: IGetPlcTimeReq = {
            token: token,
            raw: target.raw.checked,
        };

        setFormState(msg);

        const response = await getPlcTime(msg);

        const result = `BACKEND RESPONSE
        response.error: ${response.error}
        response.error_message: ${response.error_message}
        response.status: ${response.status}
        PYLOGIX RESPONSE
        response.Status: ${response.Status}
        response.TagName: ${response.TagName}
        response.Value: ${response.Value}`;

        setResText(result);
    };

    const Form = () => {
        return (
            <>
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Retrieve the controller clock time and obtain it in a
                    human-readable format (default) or in raw format if the raw
                    parameter is set to True.
                    <br />
                    The function returns an instance of the Response class,
                    which includes the following attributes: .TagName, .Value,
                    and .Status.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleGetPlcTime}
                >
                    <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                        <Checkbox name="raw" checked={formState.raw} />
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
                <TextAreaWrapper resText={resText} />
            </>
        );
    };

    return (
        <>
            <AccordionItemWrapper title="Get plc time" children={<Form />} />
        </>
    );
}
