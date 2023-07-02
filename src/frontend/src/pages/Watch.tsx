import { useContext } from "react";
import { cn } from "@/components/lib/utils.ts";
import { SettingsContext } from "@/store/settings.context.tsx";

export function Watch() {
    const settings = useContext(SettingsContext);

    return (
        <div
            className={cn(
                settings.darkMode ? "dark" : null,
                "bg-background p-5"
            )}
        >
            <h2 className="text-foreground mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">
                Watch
            </h2>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                These are actively monitored tags; you can filter, observe, and
                manipulate live values here.
            </p>
        </div>
    );
}
