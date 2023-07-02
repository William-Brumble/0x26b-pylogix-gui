import { Label } from "@/components/ui/label.tsx";
import { Textarea } from "@/components/ui/textarea.tsx";

export interface IResponseTextArea {
    resText: string;
}

export function TextAreaWrapper({ resText }: IResponseTextArea) {
    return (
        <>
            <div className="grid w-full gap-1.5">
                <Label htmlFor="message">Response:</Label>
                <Textarea
                    className="text-foreground"
                    placeholder="Response message will show up here."
                    id="message"
                    readOnly
                    value={resText}
                />
            </div>
        </>
    );
}
