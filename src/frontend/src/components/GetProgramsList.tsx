import { useState } from "react";

import { Button } from "@/components/ui/button.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";

import { getProgramsList } from "@/api";
import { IGetProgramsListReq } from "@/models/get_programs_list.ts";

export interface IGetProgramsList {
    token: string;
}

export function GetProgramsList({ token }: IGetProgramsList) {
    const [resText, setResText] = useState("");

    const handleGetProgramsList = async (event: any) => {
        event.preventDefault();

        const msg: IGetProgramsListReq = {
            token: token,
        };

        const response = await getProgramsList(msg);
        const response_stringify = JSON.stringify(response, null, "\t");
        console.log(response_stringify);
        setResText(response_stringify);
    };

    return (
        <>
            <AccordionItemWrapper title="Get programs list">
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Retrieve a program names list from the PLC. Perform a sanity
                    check to verify if the programNames parameter is empty, and
                    then execute the _getTagList function. The function returns
                    a Response class instance (.TagName, .Value, .Status).
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleGetProgramsList}
                >
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
