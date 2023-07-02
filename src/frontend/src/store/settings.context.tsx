import { createContext } from "react";

export interface SettingContextType {
    darkMode: boolean;
    setDarkMode: (rate: boolean) => void;
    refreshRate: number;
    setRefreshRate: (rate: number) => void;
}

const defaultState = {
    darkMode: false,
    refreshRate: 1,
};

export const SettingsContext =
    createContext<Partial<SettingContextType>>(defaultState);
