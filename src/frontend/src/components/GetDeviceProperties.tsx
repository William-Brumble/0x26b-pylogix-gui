import { useState } from "react";

import { Button } from "@/components/ui/button.tsx";
import { TextAreaWrapper } from "@/components/TextAreaWrapper.tsx";
import { AccordionItemWrapper } from "@/components/AccordionItemWrapper.tsx";

import { getDeviceProperties } from "@/api";
import { IGetConnectionSizeReq } from "@/models/get_connection_size.ts";

export interface IGetDeviceProperties {
    token: string;
}

export function GetDeviceProperties({ token }: IGetDeviceProperties) {
    const [resText, setResText] = useState("");

    const handleGetDeviceProperties = async (event: any) => {
        event.preventDefault();
        const msg: IGetConnectionSizeReq = {
            token: token,
        };

        const response = await getDeviceProperties(msg);

        const result = `BACKEND RESPONSE
        response.error: ${response.error}
        response.error_message: ${response.error_message}
        response.status: ${response.status}
        PYLOGIX RESPONSE
        response.response.error: ${response.response.error}
        response.response.error_message: ${response.response.error_message}
        response.response.status: ${response.response.status}
        response.response.Status: ${response.response.Status}
        response.response.TagName: ${response.response.TagName}
        DEVICE
        response.response.Value.DeviceID: ${response.response.Value.DeviceID}
        response.response.Value.EcapsualtionVesrion: ${response.response.Value.EncapsulationVersion}
        response.response.Value.IPAddress: ${response.response.Value.IPAddress}
        response.response.Value.Length: ${response.response.Value.Length}
        response.response.Value.ProductCode: ${response.response.Value.ProductCode}
        response.response.Value.ProductName: ${response.response.Value.ProductName}
        response.response.Value.ProductNameLength: ${response.response.Value.ProductNameLength}
        response.response.Value.Revision: ${response.response.Value.Revision}
        response.response.Value.SerialNumber: ${response.response.Value.SerialNumber}
        response.response.Value.State: ${response.response.Value.State}
        response.response.Value.Status: ${response.response.Value.Status}
        response.response.Value.Vendor: ${response.response.Value.Vendor}
        response.response.Value.VendorID: ${response.response.Value.VendorID}`;

        setResText(result);
    };

    const Form = () => {
        return (
            <>
                <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                    Retrieve the device properties of a device located at the
                    specified IP address. The function returns a Response class
                    instance with the attributes: .TagName, .Value, and .Status.
                </p>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleGetDeviceProperties}
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
            <AccordionItemWrapper
                title="Get device properties"
                children={<Form />}
            />
        </>
    );
}
