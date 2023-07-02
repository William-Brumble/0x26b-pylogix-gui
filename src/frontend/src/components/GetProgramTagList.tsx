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
    const [programName, setProgramName] = useState("");
    const [resText, setResText] = useState("");

    const handleGetProgramTagList = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const msg: IGetProgramTagListReq = {
            token: token,
            program_name: programName,
        };

        const response = await getProgramTagList(msg);
        const response_stringify = JSON.stringify(response, null, "\t");
        console.log(response_stringify);
        setResText(response_stringify);
    };

    const handleProgramNameChange = (event: any) => {
        setProgramName(event.target.value);
    };

    return (
        <>
            <AccordionItemWrapper title="Get program tag list">
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
                            className="text-foreground"
                            type="text"
                            name="program_name"
                            placeholder="program name"
                            value={programName}
                            onInput={handleProgramNameChange}
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
