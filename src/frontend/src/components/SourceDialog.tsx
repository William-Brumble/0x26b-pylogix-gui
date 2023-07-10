import { FormEvent, useContext } from "react";
import { Row } from "@tanstack/react-table";
import { MoreHorizontal } from "lucide-react";
import { redirect } from "react-router-dom";

import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/components/ui/dialog";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    //DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { DialogClose } from "@radix-ui/react-dialog";
import { Checkbox } from "@/components/ui/checkbox.tsx";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { connect } from "@/api";
import { IPylogixDevice } from "@/models/pylogix.ts";
import { IConnectReq } from "@/models/connect.ts";
import { SettingsContext } from "@/store/settings.context.tsx";
import { SourcesContext } from "@/store/sources.context.tsx";
import { cn } from "@/components/lib/utils.ts";

interface CustomElements extends HTMLFormControlsCollection {
    ip_address: HTMLInputElement;
    slot: HTMLInputElement;
    timeout: HTMLInputElement;
    Micro800: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

type ISourceDialogProps = {
    row: Row<IPylogixDevice>;
};
export function SourceDialog({ row }: ISourceDialogProps) {
    const settings = useContext(SettingsContext);
    const sources = useContext(SourcesContext);

    const handleConnect = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();
        const target = event.currentTarget.elements;

        const msg: IConnectReq = {
            token: settings.token ? settings.token : "",
            ip_address: target.ip_address.value,
            slot: parseInt(target.slot.value),
            timeout: parseInt(target.timeout.value),
            Micro800: target.Micro800.checked,
        };

        const response = await connect(msg);

        if (response.error) {
            return redirect(
                `/error?title=${response.status}&message=${response.error_message}`
            );
        } else {
            sources.setSelectedSource?.(msg.ip_address);
        }
    };

    return (
        <Dialog>
            <DropdownMenu>
                <DropdownMenuTrigger asChild>
                    <Button
                        variant="ghost"
                        className="bg-background text-foreground h-8 w-8 p-0"
                    >
                        <span className="sr-only text-foreground">
                            Open menu
                        </span>
                        <MoreHorizontal className="h-4 w-4" />
                    </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end">
                    <DropdownMenuLabel>Actions</DropdownMenuLabel>
                    <DialogTrigger asChild>
                        <DropdownMenuItem className="bg-background text-foreground">
                            Set as active source
                        </DropdownMenuItem>
                    </DialogTrigger>
                </DropdownMenuContent>
            </DropdownMenu>
            <DialogContent
                className={cn("bg-background stroke-0 sm:max-w-[425px]")}
            >
                <DialogHeader>
                    <DialogTitle className="text-foreground">
                        Connect
                    </DialogTitle>
                    <DialogDescription className="text-foreground">
                        Instantiate a pylogix PLC object and establish a
                        connection with the target Programmable Logic Controller
                        (PLC).
                    </DialogDescription>
                </DialogHeader>
                <form
                    className="flex flex-col justify-start gap-3 p-1 pb-4 m-1"
                    onSubmit={handleConnect}
                >
                    <div className="grid max-w-sm items-center gap-1.5">
                        <Label
                            className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            htmlFor="ip_address"
                        >
                            IP:
                        </Label>
                        <Input
                            className="text-foreground"
                            type="text"
                            name="ip_address"
                            placeholder="ip address"
                            defaultValue={row.getValue("IPAddress")}
                            readOnly
                            required
                        />
                    </div>
                    <div className="grid w-full max-w-sm items-center gap-1.5">
                        <Label className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                            SLOT:
                        </Label>
                        <Input
                            className="text-foreground"
                            type="number"
                            name="slot"
                            placeholder="slot"
                            defaultValue="0"
                            required
                        />
                    </div>
                    <div className="grid w-full max-w-sm items-center gap-1.5">
                        <Label className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                            TIMEOUT:
                        </Label>
                        <Input
                            className="text-foreground"
                            type="number"
                            name="timeout"
                            placeholder="timeout"
                            defaultValue="5"
                            required
                        />
                    </div>
                    <div className="flex w-full items-center space-x-2 text-foreground pb-4">
                        <Checkbox name="Micro800" />
                        <Label
                            htmlFor="Micro800"
                            className="text-foreground text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                            MICRO800
                        </Label>
                    </div>
                    <DialogFooter>
                        <DialogClose
                            className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md"
                            type="submit"
                        >
                            Save changes
                        </DialogClose>
                    </DialogFooter>
                </form>
            </DialogContent>
        </Dialog>
    );
}
