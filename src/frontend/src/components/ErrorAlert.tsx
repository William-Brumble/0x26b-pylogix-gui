import { Terminal } from "lucide-react";

import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";

type IProps = {
    title: string;
    description: string;
};

export function ErrorAlert({ title, description }: IProps) {
    return (
        <Alert>
            <Terminal className="h-4 w-4" />
            <AlertTitle>{title}</AlertTitle>
            <AlertDescription>{description}</AlertDescription>
        </Alert>
    );
}
