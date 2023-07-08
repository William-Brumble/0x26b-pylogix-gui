import { ReactNode, useState } from "react";

import {
    SourcesContextType,
    SourcesContext,
} from "@/store/sources.context.tsx";

type Props = {
    children: ReactNode;
};

export const SourcesProvider = ({ children }: Props) => {
    const [source, setSourceState] = useState<string | undefined>(undefined);

    const setSource = (source: string) => {
        setSourceState(source);
    };

    const values: SourcesContextType = {
        selectedSource: source,
        setSelectedSource: setSource,
    };

    return (
        <SourcesContext.Provider value={values}>
            {children}
        </SourcesContext.Provider>
    );
};
