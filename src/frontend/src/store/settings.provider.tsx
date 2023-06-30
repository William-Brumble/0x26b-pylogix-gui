import { ReactNode, useState } from "react";
import { SettingsContext } from "@/store/settings.context.tsx";

type Props = {
    children: ReactNode;
};

export const ConfigurationProvider = ({ children }: Props) => {
    const [refreshRate, setRefreshRateState] = useState(1);
    const setRefreshRate = (rate: number) => {
        setRefreshRateState(rate);
    };

    return (
        <SettingsContext.Provider value={{ refreshRate, setRefreshRate }}>
            {children}
        </SettingsContext.Provider>
    );
};
