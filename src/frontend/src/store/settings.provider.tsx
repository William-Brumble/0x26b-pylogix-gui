import { ReactNode, useState } from "react";
import { SettingsContext } from "@/store/settings.context.tsx";

type Props = {
    children: ReactNode;
};

export const ConfigurationProvider = ({ children }: Props) => {
    const [refreshRate, setRefreshRateState] = useState(1);
    const [darkMode, setDarkModeState] = useState(false);

    const setRefreshRate = (rate: number) => {
        setRefreshRateState(rate);
    };

    const setDarkMode = (mode: boolean) => {
        setDarkModeState(mode);
    };

    return (
        <SettingsContext.Provider
            value={{ darkMode, setDarkMode, refreshRate, setRefreshRate }}
        >
            {children}
        </SettingsContext.Provider>
    );
};
