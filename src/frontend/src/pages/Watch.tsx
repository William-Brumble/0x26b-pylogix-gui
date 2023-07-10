import { columns } from "@/components/WatchColumns.tsx";
import { WatchDataTable } from "@/components/WatchDataTable.tsx";
import { useCallback, useContext, useEffect, useState } from "react";
import { WatchContext } from "@/store/watch.context.tsx";
import { useIntervalAsync } from "@/hooks/use-interval-async.ts";
import { read } from "@/api";
import { IReadReq } from "@/models/read.ts";
import { SettingsContext } from "@/store/settings.context.tsx";
import { SourcesContext } from "@/store/sources.context.tsx";
import { IWatchTag } from "@/models/watch_tag.ts";

export function Watch() {
    const watch = useContext(WatchContext);
    const settings = useContext(SettingsContext);
    const source = useContext(SourcesContext);
    const [tagList, setTagList] = useState<IWatchTag[]>([]);

    useEffect(() => {
        let tagList: IWatchTag[] = [];
        if (watch.watchTags) {
            tagList = Array.from(watch.watchTags?.values());
        }
        setTagList(tagList);
    }, []);

    const poll = useCallback(async () => {
        if (watch.watchTags && watch.update) {
            const tagNames = Array.from(watch.watchTags.keys());

            for (let i = 0; i < tagNames.length; i++) {
                const tag = watch.watchTags.get(tagNames[i]);

                if (tag) {
                    const msg: IReadReq = {
                        token: settings.token ? settings.token : "",
                        tag: tag.TagName,
                        count: 1,
                        datatype: tag.DataTypeValue,
                    };

                    if (source.selectedSource) {
                        const response = await read(msg);

                        if (!response.error) {
                            tag.Value = response.response[0].Value;
                        } else {
                            tag.Value = response.status;
                        }
                    } else {
                        tag.Value = "unread";
                    }

                    watch.update(tag);
                }
            }
            const tagList = Array.from(watch.watchTags?.values());
            setTagList(tagList);
        }
    }, [setTagList]);

    let refreshRate = 5000;
    if (settings.refreshRate) {
        refreshRate = settings.refreshRate;
    }

    useIntervalAsync(poll, refreshRate);

    return <WatchDataTable columns={columns} data={tagList} />;
}
