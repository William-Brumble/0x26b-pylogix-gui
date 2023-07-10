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
    darkMode: getLocalStorageValue("darkMode", false),
    devMode: getLocalStorageValue("devMode", false),
    refreshRate: getLocalStorageValue("refreshRate", 5000),
};

export const SettingsContext =
    createContext<Partial<SettingContextType>>(defaultState);
