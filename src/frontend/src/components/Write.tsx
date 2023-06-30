import { FormEvent, useState } from "react";

import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select.tsx";
import { Label } from "@/components/ui/label.tsx";
import { Input } from "@/components/ui/input.tsx";
import { Button } from "@/components/ui/button.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";

import { write } from "@/api";
import { IWriteReq } from "@/models/write.ts";

export interface IWrite {
    token: string;
}

interface CustomElements extends HTMLFormControlsCollection {
    tag: HTMLInputElement;
    value: HTMLInputElement;
    datatype: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

export function Write({ token }: IWrite) {
    const [tag, setTag] = useState("");
    const [value, setValue] = useState(1);
    const [datatype, setDatatype] = useState("0xc3");
    const [resText, setResText] = useState("");

    const handleWrite = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();

        const target = event.currentTarget.elements;

        const msg: IWriteReq = {
            token: token,
            tag: target.tag.value,
            value: Number(target.value.value),
            datatype: parseInt(target.datatype.value),
        };

        const response = await write(msg);
        const response_stringify = JSON.stringify(response, null, "\t");
        console.log(response_stringify);
        setResText(response_stringify);
    };

    const handleTagChange = (event: any) => {
        setTag(event.target.value);
    };

    const handleValueChange = (event: any) => {
        setValue(Number(event.target.value));
    };

    const handleDatatypeChange = (event: any) => {
        setDatatype(event);
    };

    return (
        <>
            <AccordionItemWrapper title="Write">
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    This function offers two writing options: generating a
                    single tag or an array. The output is a Response class
                    instance (.TagName, .Value, .Status). Note that only single
                    value writing is currently supported; array writing is not
                    implemented.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleWrite}
                >
                    <div className="grid w-full max-w-sm items-center gap-1.5">
                        <Label
                            htmlFor="tag"
                            className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                            TAG:
                        </Label>
                        <Input
                            type="text"
                            name="tag"
                            placeholder="tag"
                            value={tag}
                            onInput={handleTagChange}
                        />
                    </div>
                    <div className="grid w-full max-w-sm items-center gap-1.5">
                        <Label
                            htmlFor="value"
                            className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                            VALUE:
                        </Label>
                        <Input
                            type="number"
                            name="value"
                            placeholder="value"
                            value={value}
                            onInput={handleValueChange}
                        />
                    </div>
                    <div className="grid w-full max-w-sm items-center gap-1.5 pb-4">
                        <Label
                            htmlFor="datatype"
                            className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                            DATATYPE:
                        </Label>
                        <Select
                            name="datatype"
                            value={datatype}
                            onValueChange={handleDatatypeChange}
                        >
                            <SelectTrigger className="text-foreground w-full max-w-sm">
                                <SelectValue placeholder="Select a datatype" />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value={"0xc1"}>BOOL</SelectItem>
                                <SelectItem value={"0xc2"}>SINT</SelectItem>
                                <SelectItem value={"0xc3"}>INT</SelectItem>
                                <SelectItem value={"0xc4"}>DINT</SelectItem>
                                <SelectItem value={"0xca"}>REAL</SelectItem>
                            </SelectContent>
                        </Select>
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
