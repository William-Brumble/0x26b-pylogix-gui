import { columns } from "@/components/WatchColumns.tsx";
import { WatchDataTable } from "@/components/WatchDataTable.tsx";
import { useContext } from "react";
import { TagsContext } from "@/store/tags.context.tsx";

export function Watch() {
    const tags = useContext(TagsContext);

    if (tags.tags) {
        const tagsList = Array.from(tags.tags?.values());
        return <WatchDataTable columns={columns} data={tagsList} />;
    } else {
        return <div>No tags found</div>;
    }
}
