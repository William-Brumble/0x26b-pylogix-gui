import { Column, ColumnDef, Row } from "@tanstack/react-table";
import { ArrowUpDown } from "lucide-react";

import { Checkbox } from "@/components/ui/checkbox";
import { Input } from "@/components/ui/input.tsx";
import { Button } from "@/components/ui/button";
import { useContext } from "react";
import { WatchContext } from "@/store/watch.context.tsx";
import { IWatchTag } from "@/models/watch_tag.ts";

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

            const tag = row.original;
            const tagName = row.original.TagName;
            const hasTagName = watch.watchTags?.has(tagName);

            const handleChecked = (value: any) => {
                if (value) {
                    watch.add?.(tag);
                } else {
                    watch.remove?.(tag);
                }

                row.toggleSelected(!!value);
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
        cell: ({ row }) => {
            const value: string | number | undefined = row.getValue("Value");
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
