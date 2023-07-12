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
    const [tags_map, setTagsMap] = useState<Map<string, IWatchTag>>(
        defaultState.tags_map
    );

    const [tags_array, setTagsArray] = useState<IWatchTag[]>(
        defaultState.tags_array
    );

    const addTag = (tag: IWatchTag) => {
        const local_map = new Map(tags_map.set(tag.TagName, tag));
        setTagsMap(local_map);
        localStorage.setItem("tags_map", JSON.stringify([...local_map]));

        const local_array = Array.from(local_map.values());
        setTagsArray(local_array);
        localStorage.setItem("tags_array", JSON.stringify(local_array));
    };

    const removeTag = (tag: IWatchTag) => {
        const local_map = new Map(tags_map);
        local_map.delete(tag.TagName);
        setTagsMap(local_map);
        localStorage.setItem("local_map", JSON.stringify([...local_map]));

        const local_array = Array.from(local_map.values());
        setTagsArray(local_array);
        localStorage.setItem("tags_array", JSON.stringify(local_array));
    };

    const updateTag = (tag: IWatchTag) => {
        const local_map = new Map(tags_map);
        local_map.set(tag.TagName, tag);
        setTagsMap(local_map);
        localStorage.setItem("watchTags", JSON.stringify([...local_map]));

        const local_array = Array.from(local_map.values());
        setTagsArray(local_array);
        localStorage.setItem("tags_array", JSON.stringify(local_array));
    };

    const values: WatchContextType = {
        tags_map: tags_map,
        tags_array: tags_array,
        add: addTag,
        remove: removeTag,
        update: updateTag,
    };

    return (
        <WatchContext.Provider value={values}>{children}</WatchContext.Provider>
    );
};
