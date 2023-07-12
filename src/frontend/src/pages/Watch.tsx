import { useContext } from "react";

import { columns } from "@/components/WatchColumns.tsx";
import { WatchDataTable } from "@/components/WatchDataTable.tsx";
import { WatchContext } from "@/store/watch.context.tsx";

export function Watch() {
    const watch = useContext(WatchContext);

    return <WatchDataTable columns={columns} data={watch.tags_array} />;
}
