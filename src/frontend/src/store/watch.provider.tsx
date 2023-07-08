import { ReactNode, useState } from "react";

import {
    WatchContextType,
    WatchContext,
    defaultState,
} from "@/store/watch.context.tsx";
import { IPylogixTag } from "@/models/pylogix.ts";

type Props = {
    children: ReactNode;
};

export const WatchProvider = ({ children }: Props) => {
    const [watchTags, setWatchTagsState] = useState<Map<string, IPylogixTag>>(
        defaultState.watchTags
    );

    const addTag = (tag: IPylogixTag) => {
        const local = new Map(watchTags.set(tag.TagName, tag));
        setWatchTagsState(local);
        localStorage.setItem("watchTags", JSON.stringify([...local]));
    };

    const removeTag = (tag: IPylogixTag) => {
        const local = new Map(watchTags);
        local.delete(tag.TagName);
        setWatchTagsState(new Map(local));
        localStorage.setItem("watchTags", JSON.stringify([...local]));
    };

    const values: WatchContextType = {
        watchTags: watchTags,
        add: addTag,
        remove: removeTag,
    };

    return (
        <WatchContext.Provider value={values}>{children}</WatchContext.Provider>
    );
};
