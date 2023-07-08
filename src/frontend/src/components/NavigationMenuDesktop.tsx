import * as React from "react";
import { Link } from "react-router-dom";

import { cn } from "@/components/lib/utils.ts";
import { NavigationMenuMobile } from "@/components/NavigationMenuMobile.tsx";
import { useContext } from "react";
import { SettingsContext } from "@/store/settings.context.tsx";

export type NavItem = {
    title: string;
    href: string;
    disabled?: boolean;
};

export type MainNavItem = NavItem;

interface MainNavProps {
    children?: React.ReactNode;
}

export function NavigationMenuDesktop({ children }: MainNavProps) {
    const settings = useContext(SettingsContext);
    const [showMobileMenu, setShowMobileMenu] = React.useState<boolean>(false);

    return (
        <div className="flex gap-6 md:gap-10">
            <Link
                to={`/?token=${settings.token}`}
                className="hidden items-center space-x-2 md:flex"
            >
                {/*<Icons.logo />*/}
                <span className="hidden text-foreground font-bold sm:inline-block">
                    w/LOGIX
                </span>
            </Link>
            <nav className="hidden gap-6 md:flex">
                <Link
                    to={`/?token=${settings.token}`}
                    className={cn(
                        "flex items-center text-lg font-medium transition-colors hover:text-foreground/80 sm:text-sm",
                        "text-foreground"
                    )}
                >
                    Watch
                </Link>
                <Link
                    to={`/tags?token=${settings.token}`}
                    className={cn(
                        "flex items-center text-lg font-medium transition-colors hover:text-foreground/80 sm:text-sm",
                        "text-foreground"
                    )}
                >
                    Tags
                </Link>
                {/*
                <Link
                    to={`/collections?token=${settings.token}`}
                    className={cn(
                        "flex items-center text-lg font-medium transition-colors hover:text-foreground/80 sm:text-sm",
                        "text-foreground"
                    )}
                >
                    Collections
                </Link>
                */}
                <Link
                    to={`/source?token=${settings.token}`}
                    className={cn(
                        "flex items-center text-lg font-medium transition-colors hover:text-foreground/80 sm:text-sm",
                        "text-foreground"
                    )}
                >
                    Source
                </Link>
                <Link
                    to={`/manual-operation?token=${settings.token}`}
                    className={cn(
                        "flex items-center text-lg font-medium transition-colors hover:text-foreground/80 sm:text-sm",
                        "text-foreground"
                    )}
                >
                    Manual
                </Link>
                <Link
                    to={`/settings?token=${settings.token}`}
                    className={cn(
                        "flex items-center text-lg font-medium transition-colors hover:text-foreground/80 sm:text-sm",
                        "text-foreground"
                    )}
                >
                    Settings
                </Link>
            </nav>
            <button
                className="flex items-center space-x-2 md:hidden"
                onClick={() => setShowMobileMenu(!showMobileMenu)}
            >
                {/*{showMobileMenu ? <Icons.close /> : <Icons.logo />}*/}
                <span className="font-bold text-foreground">Menu</span>
            </button>
            {showMobileMenu && (
                <NavigationMenuMobile>{children}</NavigationMenuMobile>
            )}
        </div>
    );
}
