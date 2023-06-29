import { FormEvent, useState } from "react";

import { Label } from "@/components/ui/label.tsx";
import { Checkbox } from "@/components/ui/checkbox.tsx";
import { Button } from "@/components/ui/button.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";

import { getTagList } from "@/api";
import { IGetTagListReq } from "@/models/get_tag_list.ts";

export interface IGetTagList {
    token: string;
}

interface CustomElements extends HTMLFormControlsCollection {
    all_tags: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

export function GetTagList({ token }: IGetTagList) {
    const [formState, setFormState] = useState({
        token: "",
        all_tags: true,
    });
    const [resText, setResText] = useState("");

    const handleGetTagList = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const target = event.currentTarget.elements;

        const msg: IGetTagListReq = {
            token: token,
            all_tags: target.all_tags.checked,
        };

        setFormState(msg);

        const response = await getTagList(msg);

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
                    Retrieve the tag list from the PLC, with the optional
                    parameter allTags. If allTags is set to False, only
                    controller tags are returned; otherwise, both controller
                    tags and program tags are returned. The function returns a
                    Response class instance (.TagName, .Value, .Status).
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleGetTagList}
                >
                    <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                        <Checkbox name="allTags" checked={formState.all_tags} />
                        <Label
                            htmlFor="allTags"
                            className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                            ALL TAGS
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
            <AccordionItemWrapper title="Get tag list" children={<Form />} />
        </>
    );
}
