import { createContext } from "react";
import { getLocalStorageValue } from "@/utilities/get-local-storage-value.ts";

import { IPylogixTag } from "@/models/pylogix.ts";

export interface WatchContextType {
    watchTags: Map<string, IPylogixTag>;
    add: (tag: IPylogixTag) => void;
    remove: (tag: IPylogixTag) => void;
}

const defaultState = {
    watchTags: getLocalStorageValue("watchTags", new Map()),
};

export const WatchContext =
    createContext<Partial<WatchContextType>>(defaultState);
