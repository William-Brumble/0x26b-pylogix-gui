import { FormEvent, useState } from "react";

import { Label } from "@/components/ui/label.tsx";
import { Input } from "@/components/ui/input.tsx";
import { Button } from "@/components/ui/button.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";

import { getProgramTagList } from "@/api";
import { IGetProgramTagListReq } from "@/models/get_program_tag_list.ts";

export interface IGetProgramTagList {
    token: string;
}

interface CustomElements extends HTMLFormControlsCollection {
    program_name: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

export function GetProgramTagList({ token }: IGetProgramTagList) {
    const [formState, setFormState] = useState({
        token: "",
        program_name: "",
    });
    const [resText, setResText] = useState("");

    const handleGetProgramTagList = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const target = event.currentTarget.elements;

        const msg: IGetProgramTagListReq = {
            token: token,
            program_name: target.program_name.value,
        };

        setFormState(msg);

        const response = await getProgramTagList(msg);

        let result = `BACKEND RESPONSE
        error: ${response.error}
        error_message: ${response.error_message}
        status: ${response.status}
        PYLOGIX RESPONSE
        Status: ${response.Status}
        TagName: ${response.TagName}`;
        for (let i = 0; i < response.Value.length; i++) {
            result += `---
            TAG: ${i}
            Array: ${response.Value[i].Array}
            DataType: ${response.Value[i].DataType}
            DataTypeValue: ${response.Value[i].DataTypeValue}
            InstanceID: ${response.Value[i].InstanceID}
            Size: ${response.Value[i].Size}
            Struct: ${response.Value[i].Struct}
            SymbolType: ${response.Value[i].SymbolType}
            TagName: ${response.Value[i].TagName}`;
        }

        setResText(result);
    };

    const Form = () => {
        return (
            <>
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Retrieve a program tag list from the PLC using the
                    programName parameter ("Program:ExampleProgram"). The
                    function returns a Response class instance (.TagName,
                    .Value, .Status).
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleGetProgramTagList}
                >
                    <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                        <Label
                            htmlFor="program_name"
                            className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                            PROGRAM NAME:
                        </Label>
                        <Input
                            type="text"
                            name="program_name"
                            placeholder="program name"
                            defaultValue={formState.program_name}
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
                title="Get program tag list"
                children={<Form />}
            />
        </>
    );
}
