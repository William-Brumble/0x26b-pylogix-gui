import { ReactNode, useState } from "react";
import {
    SettingContextType,
    SettingsContext,
} from "@/store/settings.context.tsx";

type Props = {
    children: ReactNode;
};

export const ConfigurationProvider = ({ children }: Props) => {
    const [token, setTokenState] = useState("test");
    const setToken = (token: string) => {
        setTokenState(token);
    };

    const [refreshRate, setRefreshRateState] = useState(1);
    const setRefreshRate = (rate: number) => {
        setRefreshRateState(rate);
    };

    const [darkMode, setDarkModeState] = useState(false);
    const setDarkMode = (mode: boolean) => {
        setDarkModeState(mode);
    };

    const values: SettingContextType = {
        token: token,
        setToken: setToken,
        darkMode: darkMode,
        setDarkMode: setDarkMode,
        refreshRate: refreshRate,
        setRefreshRate: setRefreshRate,
    };

    return (
        <SettingsContext.Provider value={values}>
            {children}
        </SettingsContext.Provider>
    );
};
