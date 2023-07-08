import { ReactNode, useState } from "react";
import {
    SettingContextType,
    SettingsContext,
    defaultState,
} from "@/store/settings.context.tsx";

type Props = {
    children: ReactNode;
};

export const ConfigurationProvider = ({ children }: Props) => {
    const [token, setTokenState] = useState(defaultState.token);
    const setToken = (token: string) => {
        setTokenState(token);
    };

    const [refreshRate, setRefreshRateState] = useState(
        defaultState.refreshRate
    );
    const setRefreshRate = (refreshRate: number) => {
        setRefreshRateState(refreshRate);
        localStorage.setItem("refreshRate", JSON.stringify(refreshRate));
    };

    const [darkMode, setDarkModeState] = useState(defaultState.darkMode);
    const setDarkMode = (darkMode: boolean) => {
        setDarkModeState(darkMode);
        localStorage.setItem("darkMode", JSON.stringify(darkMode));
    };

    const [devMode, setDevModeState] = useState(defaultState.devMode);
    const setDevMode = (devMode: boolean) => {
        setDevModeState(devMode);
        localStorage.setItem("devMode", JSON.stringify(devMode));
    };

    const values: SettingContextType = {
        token: token,
        setToken: setToken,
        darkMode: darkMode,
        setDarkMode: setDarkMode,
        devMode: devMode,
        setDevMode: setDevMode,
        refreshRate: refreshRate,
        setRefreshRate: setRefreshRate,
    };

    return (
        <SettingsContext.Provider value={values}>
            {children}
        </SettingsContext.Provider>
    );
};
