import { ReactNode, useState } from "react";

import { WatchContextType, WatchContext } from "@/store/tags.context.tsx";
import { IPylogixTag } from "@/models/pylogix.ts";

type Props = {
    children: ReactNode;
};

export const WatchProvider = ({ children }: Props) => {
    const [watchTags, setWatchTagsState] = useState<Map<string, IPylogixTag>>(
        new Map()
    );

    const addTag = (tag: IPylogixTag) => {
        setWatchTagsState(new Map(watchTags.set(tag.TagName, tag)));
    };

    const removeTag = (tag: IPylogixTag) => {
        const local = new Map(watchTags);
        local.delete(tag.TagName);
        setWatchTagsState(new Map(local));
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
