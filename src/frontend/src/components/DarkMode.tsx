import { ReactNode, useContext } from "react";
import { SettingsContext } from "@/store/settings.context.tsx";
import { cn } from "@/components/lib/utils.ts";

type DarkModeProps = {
    children: ReactNode;
};

export function DarkMode({ children }: DarkModeProps) {
    /* Gets the dark mode settings from the settings context
     * and sets the dark tailwind css variable if enabled */
    const settings = useContext(SettingsContext);

    return (
        <div
            className={cn(
                settings.darkMode ? "dark" : null,
                "bg-background p-5 w-full h-max min-h-full"
            )}
        >
            {children}
        </div>
    );
}
