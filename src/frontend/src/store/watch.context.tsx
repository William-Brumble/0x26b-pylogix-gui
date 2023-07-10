import { createContext } from "react";
import { getLocalStorageValue } from "@/utilities/get-local-storage-value.ts";

import { IWatchTag } from "@/models/watch_tag.ts";

export interface WatchContextType {
    watchTags: Map<string, IWatchTag>;
    add: (tag: IWatchTag) => void;
    remove: (tag: IWatchTag) => void;
    update: (tag: IWatchTag) => void;
}

export const defaultState = {
    watchTags: getLocalStorageValue("watchTags", new Map()),
};

export const WatchContext =
    createContext<Partial<WatchContextType>>(defaultState);
