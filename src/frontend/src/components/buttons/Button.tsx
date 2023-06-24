import {
    ButtonProps,
    buttonVariants,
} from "@/components/shadcn/components/ui/button.tsx";
import { cn } from "@/components/shadcn/lib/lib.ts";

export function Button({ className, variant, ...props }: ButtonProps) {
    return (
        <button className={cn(buttonVariants({ variant }), {}, className)}>
            Primary
        </button>
    );
}
