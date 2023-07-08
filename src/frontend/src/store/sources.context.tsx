import { createContext } from "react";

export interface SourcesContextType {
    selectedSource: string | undefined;
    setSelectedSource: (device: string) => void;
}

const defaultState = {
    selectedSource: undefined,
};

export const SourcesContext =
    createContext<Partial<SourcesContextType>>(defaultState);
