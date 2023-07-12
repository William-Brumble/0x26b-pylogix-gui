import { createContext } from "react";
import { getLocalStorageValue } from "@/utilities/get-local-storage-value.ts";

import { IWatchTag } from "@/models/watch_tag.ts";

export interface WatchContextType {
    tags_map: Map<string, IWatchTag>;
    tags_array: IWatchTag[];
    add: (tag: IWatchTag) => void;
    remove: (tag: IWatchTag) => void;
    update: (tag: IWatchTag) => void;
}

export const defaultState = {
    tags_map: getLocalStorageValue("tags_map", new Map()),
    tags_array: getLocalStorageValue("tags_array", []),
    add: (tag: IWatchTag) => console.log(tag),
    remove: (tag: IWatchTag) => console.log(tag),
    update: (tag: IWatchTag) => console.log(tag),
};

export const WatchContext = createContext<WatchContextType>(defaultState);
