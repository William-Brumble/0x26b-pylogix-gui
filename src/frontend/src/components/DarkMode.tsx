import { ReactNode, useContext } from "react";
import { SettingsContext } from "@/store/settings.context.tsx";

type DarkModeProps = {
    children: ReactNode;
};

export function DarkMode({ children }: DarkModeProps) {
    /* Gets the dark mode settings from the settings context
     * and sets the dark tailwind css variable if enabled */
    const settings = useContext(SettingsContext);

    if (settings.darkMode) {
        document.body.classList.add("dark");
    } else {
        document.body.classList.remove("dark");
    }

    return <>{children}</>;
}
