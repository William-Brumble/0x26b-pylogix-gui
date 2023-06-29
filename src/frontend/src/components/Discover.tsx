import { useState } from "react";

import { Button } from "@/components/ui/button.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";

import { discover } from "@/api";
import { IDiscoverReq } from "@/models/discover.ts";

export interface IDiscover {
    token: string;
}

export function Discover({ token }: IDiscover) {
    const [resText, setResText] = useState("");

    const handleDiscover = async (event: any) => {
        event.preventDefault();
        const msg: IDiscoverReq = {
            token: token,
        };

        const response = await discover(msg);

        let result = `BACKEND RESPONSE
        response.error: ${response.error}
        response.status: ${response.status}
        response.error_message: ${response.error_message}
        PYLOGIX RESPONSE
        response.response.error: ${response.response.error}
        response.response.error_message: ${response.response.error_message}
        response.response.status: ${response.response.status}
        response.response.Status: ${response.response.Status}
        response.response.TagName:${response.response.TagName}`;
        for (let i = 0; i < response.response.Value.length; i++) {
            result += `----
            DEVICE ${i}
            response.response.Value[${i}].DeviceID: ${response.response.Value[i].DeviceID}
            response.response.Value[${i}].EncapsulationVersion: ${response.response.Value[i].EncapsulationVersion}
            response.response.Value[${i}].IPAddress: ${response.response.Value[i].IPAddress}
            response.response.Value[${i}].Lenth: ${response.response.Value[i].Length}
            response.response.Value[${i}].ProductCode: ${response.response.Value[i].ProductCode}
            response.response.Value[${i}].ProductName: ${response.response.Value[i].ProductName}
            response.response.Value[${i}].ProductNameLength: ${response.response.Value[i].ProductNameLength}
            response.response.Value[${i}].Revision: ${response.response.Value[i].Revision}
            response.response.Value[${i}].SerialNumber: ${response.response.Value[i].SerialNumber}
            response.response.Value[${i}].State: ${response.response.Value[i].State}
            response.response.Value[${i}].Status: ${response.response.Value[i].Status}
            response.response.Value[${i}].Vendor: ${response.response.Value[i].Vendor}
            response.response.Value[${i}].VendorID: ${response.response.Value[i].VendorID}`;
        }

        setResText(result);
    };

    const Form = () => {
        return (
            <>
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Perform a network-wide query to discover all the EIP
                    (EtherNet/IP) devices present on the network. The function
                    returns a Response class instance containing the attributes:
                    .TagName, .Value, and .Status.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleDiscover}
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
            </>
        );
    };

    return (
        <>
            <AccordionItemWrapper title="Discover" children={<Form />} />
        </>
    );
}
