import { FormEvent, useState } from "react";

import { Label } from "@/components/ui/label.tsx";
import { Input } from "@/components/ui/input.tsx";
import { Button } from "@/components/ui/button.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";

import { setConnectionSize } from "@/api";
import { ISetConnectionSizeReq } from "@/models/set_connection_size.ts";

export interface ISetConnectionSize {
    token: string;
}

interface CustomElements extends HTMLFormControlsCollection {
    connection_size: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

export function SetConnectionSize({ token }: ISetConnectionSize) {
    const [formState, setFormState] = useState({
        connection_size: 508,
    });
    const [resText, setResText] = useState("");

    const handleSetConnectionSize = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const target = event.currentTarget.elements;

        const msg: ISetConnectionSizeReq = {
            token: token,
            connection_size: parseInt(target.connection_size.value),
        };

        setFormState(msg);

        const response = await setConnectionSize(msg);

        const result = `BACKEND RESPONSE
        response.error: ${response.error}
        response.status: ${response.status}
        response.error_message: ${response.error_message}`;

        setResText(result);
    };

    const Form = () => {
        return (
            <>
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Please ensure to appropriately configure the
                    "ConnectionSize" parameter prior to initiating the first
                    call that necessitates the use of "conn.connect()". By
                    default, the system attempts a Large Forward Open followed
                    by a Small Forward Open. In case an Explicit (Unconnected)
                    session is utilized, a sensible default option will be
                    automatically selected.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleSetConnectionSize}
                >
                    <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                        <Label
                            htmlFor="connection_size"
                            className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                            CONNECTION SIZE:
                        </Label>
                        <Input
                            type="number"
                            name="connection_size"
                            placeholder="connection size"
                            defaultValue={formState.connection_size}
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
                title="Set connection size"
                children={<Form />}
            />
        </>
    );
}
