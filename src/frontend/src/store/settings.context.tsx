import { createContext } from "react";

export interface SettingContextType {
    token: string;
    setToken: (token: string) => void;
    darkMode: boolean;
    setDarkMode: (rate: boolean) => void;
    refreshRate: number;
    setRefreshRate: (rate: number) => void;
}

const defaultState = {
    token: "test",
    darkMode: false,
    refreshRate: 1,
};

export const SettingsContext =
    createContext<Partial<SettingContextType>>(defaultState);
