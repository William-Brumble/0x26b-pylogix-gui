// @ts-ignore
import React, { useEffect, useState } from "react";

import "./App.css";

import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion";
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select";
import { Separator } from "./components/ui/separator";
import { Input } from "./components/ui/input";
import { Checkbox } from "./components/ui/checkbox";
import { Label } from "./components/ui/label";
import { Button } from "./components/ui/button";

// TODO: Create interfaces for the handler events.

function App() {
    const [token, setToken] = useState("");
    const port = window.location.port;

    useEffect(() => {
        setToken(window?.pywebview?.token);
    }, []);

    return (
        <div className="bg-background p-5">
            <h2 className="text-foreground mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">
                Manual Operation
            </h2>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                This particular section is designated exclusively for manual
                operation, primarily intended to facilitate the testing of
                interprocess communication between the frontend and backend
                processes.
            </p>

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />

            <Separator />
        </div>
    );
}

export default App;
