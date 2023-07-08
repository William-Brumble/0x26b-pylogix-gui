import * as React from "react";
import { Link } from "react-router-dom";

import { cn } from "@/components/lib/utils";
import { useLockBody } from "@/hooks/use-lock-body.ts";
import { useContext } from "react";
import { SettingsContext } from "@/store/settings.context.tsx";

interface MobileNavProps {
    children?: React.ReactNode;
}

export function NavigationMenuMobile({ children }: MobileNavProps) {
    const settings = useContext(SettingsContext);
    useLockBody();

    return (
        <div
            className={cn(
                "fixed inset-0 top-16 z-50 grid h-[calc(100vh-4rem)] grid-flow-row auto-rows-max overflow-auto p-6 pb-32 shadow-md animate-in slide-in-from-bottom-80 md:hidden"
            )}
        >
            <div className="relative z-20 grid gap-6 rounded-md bg-popover p-4 text-popover-foreground shadow-md">
                <Link
                    to={`/?token=${settings.token}`}
                    className="flex items-center space-x-2"
                >
                    {/*<Icons.logo />*/}
                    <span className="text-foreground font-bold">w/LOGIX</span>
                </Link>
                <nav className="grid grid-flow-row auto-rows-max text-sm">
                    <Link
                        to={`/?token=${settings.token}`}
                        className={cn(
                            "flex w-full items-center rounded-md p-2 text-sm font-medium hover:underline"
                        )}
                    >
                        Watch
                    </Link>
                    <Link
                        to={`/tags?token=${settings.token}`}
                        className={cn(
                            "flex w-full items-center rounded-md p-2 text-sm font-medium hover:underline"
                        )}
                    >
                        Tags
                    </Link>
                    {/*
                    <Link
                        to={`/collections?token=${settings.token}`}
                        className={cn(
                            "flex w-full items-center rounded-md p-2 text-sm font-medium hover:underline"
                        )}
                    >
                        Collections
                    </Link>
                    */}
                    <Link
                        to={`/source?token=${settings.token}`}
                        className={cn(
                            "flex w-full items-center rounded-md p-2 text-sm font-medium hover:underline"
                        )}
                    >
                        Source
                    </Link>
                    <Link
                        to={`/manual-operation?token=${settings.token}`}
                        className={cn(
                            "flex w-full items-center rounded-md p-2 text-sm font-medium hover:underline"
                        )}
                    >
                        Manual
                    </Link>
                    <Link
                        to={`/settings?token=${settings.token}`}
                        className={cn(
                            "flex w-full items-center rounded-md p-2 text-sm font-medium hover:underline"
                        )}
                    >
                        Settings
                    </Link>
                </nav>
                {children}
            </div>
        </div>
    );
}
