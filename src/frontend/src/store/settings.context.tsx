import { createContext } from "react";

export interface SettingContextType {
    refreshRate: number;
    setRefreshRate: (rate: number) => void;
}

const defaultState = {
    refreshRate: 1,
};

export const SettingsContext =
    createContext<Partial<SettingContextType>>(defaultState);
