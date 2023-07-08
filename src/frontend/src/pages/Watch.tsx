import { columns } from "@/components/WatchColumns.tsx";
import { WatchDataTable } from "@/components/WatchDataTable.tsx";
import { useContext } from "react";
import { WatchContext } from "@/store/watch.context.tsx";

export function Watch() {
    const watch = useContext(WatchContext);

    if (watch.watchTags) {
        const tagsList = Array.from(watch.watchTags?.values());
        return (
            <WatchDataTable columns={columns} data={tagsList ? tagsList : []} />
        );
    } else {
        return <WatchDataTable columns={columns} data={[]} />;
    }
}
