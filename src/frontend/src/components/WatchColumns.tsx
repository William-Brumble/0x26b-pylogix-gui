import { Column, ColumnDef, Row } from "@tanstack/react-table";
import { ArrowUpDown } from "lucide-react";

import { Checkbox } from "@/components/ui/checkbox";
import { Input } from "@/components/ui/input.tsx";
import { Button } from "@/components/ui/button";
import { useCallback, useContext, useState } from "react";
import { WatchContext } from "@/store/watch.context.tsx";
import { IWatchTag } from "@/models/watch_tag.ts";
import { IReadReq } from "@/models/read.ts";
import { read } from "@/api";
import { useIntervalAsync } from "@/hooks/use-interval-async.ts";
import { SettingsContext } from "@/store/settings.context.tsx";
import { SourcesContext } from "@/store/sources.context.tsx";

type ISortableHeaderProps = {
    column: Column<IWatchTag>;
    name: string;
};
const SortableHeader = ({ column, name }: ISortableHeaderProps) => {
    return (
        <Button
            variant="ghost"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
            {name}
            <ArrowUpDown className="ml-2 h-4 w-4" />
        </Button>
    );
};

type IFormattedCellProps = {
    row: Row<IWatchTag>;
    name: string;
};
const FormattedCell = ({ row, name }: IFormattedCellProps) => {
    const value: string | number | undefined = row.getValue(name);
    return <div className="text-foreground">{value}</div>;
};

export const columns: ColumnDef<IWatchTag>[] = [
    {
        id: "select",
        cell: function Cell({ row }) {
            const watch = useContext(WatchContext);
            const hasTagName = watch.tags_map.has(row.original.TagName);

            const handleChecked = () => {
                watch.remove(row.original);
            };

            return (
                <Checkbox
                    checked={hasTagName}
                    onCheckedChange={handleChecked}
                    aria-label="Select row"
                />
            );
        },
        enableSorting: false,
        enableHiding: false,
    },
    {
        accessorKey: "TagName",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Tag Name" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"TagName"} />;
        },
    },
    {
        accessorKey: "Value",
        header: "Live Value",
        cell: function Cell({ row }) {
            const settings = useContext(SettingsContext);
            const source = useContext(SourcesContext);

            const [value, setValue] = useState<string | number | undefined>(
                "unread"
            );

            const poll = useCallback(async () => {
                const msg: IReadReq = {
                    token: settings.token ? settings.token : "",
                    tag: row.original.TagName,
                    count: 1,
                    datatype: row.original.DataTypeValue,
                };

                if (source.selectedSource) {
                    const response = await read(msg);
                    console.log("response", response);

                    if (!response.error) {
                        setValue(response.response[0].Value);
                    } else {
                        setValue(response.status);
                    }
                } else {
                    setValue("unread");
                }
                console.log("value", value);
                console.log("source", source.selectedSource);
            }, []);

            useIntervalAsync(poll, settings.refreshRate);

            return (
                <Input
                    className="text-foreground w-1/2 min-w-fit"
                    type="text"
                    placeholder="unread"
                    value={value}
                    readOnly
                />
            );
        },
    },
    {
        accessorKey: "InstanceID",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Instance ID" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"InstanceID"} />;
        },
    },
    {
        accessorKey: "SymbolType",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Symbol Type" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"SymbolType"} />;
        },
    },
    {
        accessorKey: "DataTypeValue",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Datatype Value" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"DataTypeValue"} />;
        },
    },
    {
        accessorKey: "DataType",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Datatype" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"DataType"} />;
        },
    },
    {
        accessorKey: "Array",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Array" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Array"} />;
        },
    },
    {
        accessorKey: "Struct",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Struct" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Struct"} />;
        },
    },
    {
        accessorKey: "Size",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Size" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Size"} />;
        },
    },
    {
        accessorKey: "AccessRight",
        header: ({ column }) => {
            return <SortableHeader column={column} name="AccessRight" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"AccessRight"} />;
        },
    },
    {
        accessorKey: "Internal",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Internal" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Internal"} />;
        },
    },
    {
        accessorKey: "Meta",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Meta" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Meta"} />;
        },
    },
    {
        accessorKey: "Scope0",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Scope0" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Scope0"} />;
        },
    },
    {
        accessorKey: "Scope1",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Scope1" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Scope1"} />;
        },
    },
    {
        accessorKey: "Bytes",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Bytes" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Bytes"} />;
        },
    },
];
