import { createContext } from "react";

import { IPylogixTag } from "@/models/pylogix.ts";

export interface TagsContextType {
    tags: Map<string, IPylogixTag>;
    add: (tag: IPylogixTag) => void;
    remove: (tag: IPylogixTag) => void;
}

const defaultState = {
    tags: new Map(),
    add: (tag: IPylogixTag) => {
        console.log(tag);
    },
    remove: (tag: IPylogixTag) => {
        console.log(tag);
    },
};

export const TagsContext =
    createContext<Partial<TagsContextType>>(defaultState);
