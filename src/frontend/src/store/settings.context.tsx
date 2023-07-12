import { createContext } from "react";
import { getLocalStorageValue } from "@/utilities/get-local-storage-value.ts";

export interface SettingContextType {
    token: string;
    setToken: (token: string) => void;
    darkMode: boolean;
    setDarkMode: (enable: boolean) => void;
    devMode: boolean;
    setDevMode: (enable: boolean) => void;
    refreshRate: number;
    setRefreshRate: (rate: number) => void;
}

export const defaultState = {
    token: "development_token",
    setToken: (token: string) => console.log(token),
    darkMode: getLocalStorageValue("darkMode", false),
    setDarkMode: (enable: boolean) => console.log(enable),
    devMode: getLocalStorageValue("devMode", false),
    setDevMode: (enable: boolean) => console.log(enable),
    refreshRate: getLocalStorageValue("refreshRate", 5000),
    setRefreshRate: (rate: number) => console.log(rate),
};

export const SettingsContext = createContext<SettingContextType>(defaultState);
