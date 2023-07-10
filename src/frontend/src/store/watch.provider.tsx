import { ReactNode, useState } from "react";

import {
    WatchContextType,
    WatchContext,
    defaultState,
} from "@/store/watch.context.tsx";
import { IWatchTag } from "@/models/watch_tag.ts";

type Props = {
    children: ReactNode;
};

export const WatchProvider = ({ children }: Props) => {
    const [watchTags, setWatchTagsState] = useState<Map<string, IWatchTag>>(
        defaultState.watchTags
    );

    const addTag = (tag: IWatchTag) => {
        const local = new Map(watchTags.set(tag.TagName, tag));
        setWatchTagsState(local);
        localStorage.setItem("watchTags", JSON.stringify([...local]));
    };

    const removeTag = (tag: IWatchTag) => {
        const local = new Map(watchTags);
        local.delete(tag.TagName);
        setWatchTagsState(local);
        localStorage.setItem("watchTags", JSON.stringify([...local]));
    };

    const updateTag = (tag: IWatchTag) => {
        const local = new Map(watchTags);
        local.set(tag.TagName, tag);
        setWatchTagsState(local);
        localStorage.setItem("watchTags", JSON.stringify([...local]));
    };

    const values: WatchContextType = {
        watchTags: watchTags,
        add: addTag,
        remove: removeTag,
        update: updateTag,
    };

    return (
        <WatchContext.Provider value={values}>{children}</WatchContext.Provider>
    );
};
