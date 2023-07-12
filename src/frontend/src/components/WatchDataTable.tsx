import { FormEvent, useContext, useState } from "react";
import {
    ColumnDef,
    flexRender,
    getCoreRowModel,
    useReactTable,
    getPaginationRowModel,
    SortingState,
    getSortedRowModel,
    ColumnFiltersState,
    getFilteredRowModel,
    VisibilityState,
} from "@tanstack/react-table";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table";
import {
    DropdownMenu,
    DropdownMenuCheckboxItem,
    DropdownMenuContent,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { WatchContext } from "@/store/watch.context.tsx";
import { IWatchTag } from "@/models/watch_tag.ts";

interface CustomElements extends HTMLFormControlsCollection {
    importer: HTMLInputElement;
}

interface CustomForm extends HTMLFormElement {
    readonly elements: CustomElements;
}

interface DataTableProps<TData, TValue> {
    columns: ColumnDef<TData, TValue>[];
    data: TData[];
}

export function WatchDataTable<TData, TValue>({
    columns,
    data,
}: DataTableProps<TData, TValue>) {
    const watch = useContext(WatchContext);
    const [sorting, setSorting] = useState<SortingState>([]);
    const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([]);
    const [rowSelection, setRowSelection] = useState({});
    const [columnVisibility, setColumnVisibility] = useState<VisibilityState>({
        InstanceID: false,
        SymbolType: false,
        DataTypeValue: false,
        Array: false,
        Struct: false,
        Size: false,
        AccessRight: false,
        Internal: false,
        Meta: false,
        Scope0: false,
        Scope1: false,
        Bytes: false,
    });

    const table = useReactTable({
        data,
        columns,
        getCoreRowModel: getCoreRowModel(),
        getPaginationRowModel: getPaginationRowModel(),
        onSortingChange: setSorting,
        getSortedRowModel: getSortedRowModel(),
        onColumnFiltersChange: setColumnFilters,
        getFilteredRowModel: getFilteredRowModel(),
        onColumnVisibilityChange: setColumnVisibility,
        onRowSelectionChange: setRowSelection,
        initialState: {
            pagination: {
                pageSize: 20,
            },
        },
        state: {
            sorting,
            columnFilters,
            columnVisibility,
            rowSelection,
        },
    });

    const handleExport = () => {
        const data = table.getRowModel().rows;
        const parsed_data: IWatchTag[] = [];
        data.forEach((row) => {
            parsed_data.push(row.original as IWatchTag);
        });
        const json_data = JSON.stringify(parsed_data);
        const encoded_data = encodeURIComponent(json_data);
        const jsonString = `data:text/json;chatset=utf-8,${encoded_data}`;
        const link = document.createElement("a");
        link.href = jsonString;
        link.download = "export.json";
        link.click();
    };

    const handleImport = async (event: FormEvent<CustomForm>) => {
        event.preventDefault();
        const target = event.currentTarget.elements;
        const file = target.importer.files?.[0];
        if (file) {
            const data = await file.text();
            if (data) {
                const json_data = JSON.parse(data);
                json_data.forEach((tag: IWatchTag) => {
                    watch.add(tag);
                });
            }
        }
    };

    return (
        <div>
            <div className="flex flex-row justify-between items-end py-4">
                <Input
                    placeholder="Filter tag names..."
                    value={
                        (table
                            .getColumn("TagName")
                            ?.getFilterValue() as string) ?? ""
                    }
                    onChange={(event) =>
                        table
                            .getColumn("TagName")
                            ?.setFilterValue(event.target.value)
                    }
                    className="max-w-sm text-foreground"
                />

                <div className="flex flex-row gap-2 items-end p-0">
                    <DropdownMenu>
                        <DropdownMenuTrigger asChild>
                            <Button
                                variant="outline"
                                className="ml-auto text-foreground"
                            >
                                Columns
                            </Button>
                        </DropdownMenuTrigger>
                        <DropdownMenuContent align="end">
                            {table
                                .getAllColumns()
                                .filter((column) => column.getCanHide())
                                .map((column) => {
                                    return (
                                        <DropdownMenuCheckboxItem
                                            key={column.id}
                                            className="capitalize"
                                            checked={column.getIsVisible()}
                                            onCheckedChange={(value) =>
                                                column.toggleVisibility(!!value)
                                            }
                                        >
                                            {column.id}
                                        </DropdownMenuCheckboxItem>
                                    );
                                })}
                        </DropdownMenuContent>
                    </DropdownMenu>

                    <form
                        onSubmit={handleImport}
                        className="hidden md:flex md:flex-row items-end gap-2"
                    >
                        <div className="grid w-full max-w-sm items-center gap-1.5">
                            <Input
                                id="importer"
                                type="file"
                                accept=".json"
                                className="file:text-foreground hover:bg-accent hover:text-accent-foreground"
                            />
                        </div>
                        <Button
                            type="submit"
                            variant="outline"
                            className="ml-auto text-foreground"
                        >
                            Import
                        </Button>
                    </form>

                    <Button
                        variant="outline"
                        className="hidden md:inline-flex ml-auto text-foreground"
                        onClick={handleExport}
                    >
                        Export
                    </Button>
                </div>
            </div>
            <div className="rounded-md border">
                <Table>
                    <TableHeader>
                        {table.getHeaderGroups().map((headerGroup) => (
                            <TableRow key={headerGroup.id}>
                                {headerGroup.headers.map((header) => {
                                    return (
                                        <TableHead key={header.id}>
                                            {header.isPlaceholder
                                                ? null
                                                : flexRender(
                                                      header.column.columnDef
                                                          .header,
                                                      header.getContext()
                                                  )}
                                        </TableHead>
                                    );
                                })}
                            </TableRow>
                        ))}
                    </TableHeader>
                    <TableBody>
                        {table.getRowModel().rows?.length ? (
                            table.getRowModel().rows.map((row) => {
                                return (
                                    <TableRow key={row.id}>
                                        {row.getVisibleCells().map((cell) => (
                                            <TableCell key={cell.id}>
                                                {flexRender(
                                                    cell.column.columnDef.cell,
                                                    cell.getContext()
                                                )}
                                            </TableCell>
                                        ))}
                                    </TableRow>
                                );
                            })
                        ) : (
                            <TableRow>
                                <TableCell
                                    colSpan={columns.length}
                                    className="h-24 text-center"
                                >
                                    No results.
                                </TableCell>
                            </TableRow>
                        )}
                    </TableBody>
                </Table>
            </div>
            <div className="flex items-center justify-end space-x-2 py-4">
                <Button
                    className="text-foreground"
                    variant="outline"
                    size="sm"
                    onClick={() => table.previousPage()}
                    disabled={!table.getCanPreviousPage()}
                >
                    Previous
                </Button>
                <Button
                    className="text-foreground"
                    variant="outline"
                    size="sm"
                    onClick={() => table.nextPage()}
                    disabled={!table.getCanNextPage()}
                >
                    Next
                </Button>
            </div>
        </div>
    );
}
