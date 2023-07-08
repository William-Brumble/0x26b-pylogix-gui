import { Column, Row, ColumnDef } from "@tanstack/react-table";
import { ArrowUpDown } from "lucide-react";

import { Button } from "@/components/ui/button";
import { IPylogixDevice } from "@/models/pylogix.ts";
import { SourceDialog } from "@/components/SourceDialog.tsx";

type ISortableHeaderProps = {
    column: Column<IPylogixDevice>;
    name: string;
};
const SortableHeader = ({ column, name }: ISortableHeaderProps) => {
    return (
        <Button
            className="text-foreground"
            variant="ghost"
            onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
            {name}
            <ArrowUpDown className="ml-2 h-4 w-4" />
        </Button>
    );
};

type IFormattedCellProps = {
    row: Row<IPylogixDevice>;
    name: string;
};
const FormattedCell = ({ row, name }: IFormattedCellProps) => {
    const value: string | number | undefined = row.getValue(name);

    return <div className="text-foreground">{value}</div>;
};

export const columns: ColumnDef<IPylogixDevice>[] = [
    {
        id: "actions",
        cell: ({ row }) => {
            return <SourceDialog row={row} />;
        },
    },
    {
        accessorKey: "Length",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Length" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Length"} />;
        },
    },
    {
        accessorKey: "EncapsulationVersion",
        header: ({ column }) => {
            return (
                <SortableHeader column={column} name="Encapsulation Version" />
            );
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"EncapsulationVersion"} />;
        },
    },
    {
        accessorKey: "IPAddress",
        header: ({ column }) => {
            return <SortableHeader column={column} name="IP Address" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"IPAddress"} />;
        },
    },
    {
        accessorKey: "VendorID",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Vendor ID" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"VendorID"} />;
        },
    },
    {
        accessorKey: "Vendor",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Vendor" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Vendor"} />;
        },
    },
    {
        accessorKey: "DeviceID",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Device ID" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"DeviceID"} />;
        },
    },
    {
        accessorKey: "DeviceType",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Device Type" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"DeviceType"} />;
        },
    },
    {
        accessorKey: "ProductCode",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Product Code" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"ProductCode"} />;
        },
    },
    {
        accessorKey: "Revision",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Revision" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Revision"} />;
        },
    },
    {
        accessorKey: "Status",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Status" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"Status"} />;
        },
    },
    {
        accessorKey: "SerialNumber",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Serial Number" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"SerialNumber"} />;
        },
    },
    {
        accessorKey: "ProductNameLength",
        header: ({ column }) => {
            return (
                <SortableHeader column={column} name="Product Name Length" />
            );
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"ProductNameLength"} />;
        },
    },
    {
        accessorKey: "ProductName",
        header: ({ column }) => {
            return <SortableHeader column={column} name="Product Name" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"ProductName"} />;
        },
    },
    {
        accessorKey: "State",
        header: ({ column }) => {
            return <SortableHeader column={column} name="State" />;
        },
        cell: ({ row }) => {
            return <FormattedCell row={row} name={"State"} />;
        },
    },
];
