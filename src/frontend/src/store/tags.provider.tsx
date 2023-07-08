import { ReactNode, useState } from "react";

import { TagsContextType, TagsContext } from "@/store/tags.context.tsx";
import { IPylogixTag } from "@/models/pylogix.ts";

type Props = {
    children: ReactNode;
};

export const TagsProvider = ({ children }: Props) => {
    const [tags, setTagsState] = useState<Map<string, IPylogixTag>>(new Map());

    const addTag = (tag: IPylogixTag) => {
        setTagsState(new Map(tags.set(tag.TagName, tag)));
    };

    const removeTag = (tag: IPylogixTag) => {
        const local = new Map(tags);
        local.delete(tag.TagName);
        setTagsState(new Map(local));
    };

    const values: TagsContextType = {
        tags: tags,
        add: addTag,
        remove: removeTag,
    };

    return (
        <TagsContext.Provider value={values}>{children}</TagsContext.Provider>
    );
};
