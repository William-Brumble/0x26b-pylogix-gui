import { ReactNode, useContext } from "react";
import { Outlet, createBrowserRouter, RouterProvider } from "react-router-dom";

import { Watch } from "@/pages/Watch.tsx";
import { Error } from "@/pages/Error.tsx";
import { Settings } from "@/pages/Settings.tsx";
import { ManualOperation } from "@/pages/ManualOperation.tsx";
import { NavigationMenuDesktop } from "@/components/NavigationMenuDesktop.tsx";
import { cn } from "@/components/lib/utils.ts";

import { ConfigurationProvider } from "@/store/settings.provider.tsx";
import { Source } from "@/pages/Source.tsx";
import { Tags } from "@/pages/Tags.tsx";
import { Collections } from "@/pages/Collections.tsx";
import { SettingsContext } from "@/store/settings.context.tsx";

type DarkModeProps = {
    children: ReactNode;
};

function DarkMode({ children }: DarkModeProps) {
    const settings = useContext(SettingsContext);

    return (
        <div
            className={cn(
                settings.darkMode ? "dark" : null,
                "bg-background p-5 w-full h-full"
            )}
        >
            {children}
        </div>
    );
}

function Root() {
    return (
        <ConfigurationProvider>
            <DarkMode>
                <NavigationMenuDesktop />
                <Outlet />
            </DarkMode>
        </ConfigurationProvider>
    );
}

const router = createBrowserRouter([
    {
        path: "/",
        element: <Root />,
        errorElement: <Error />,
        children: [
            {
                index: true,
                element: <Watch />,
                errorElement: <Error />,
            },
            {
                path: "/settings",
                element: <Settings />,
                errorElement: <Error />,
            },
            {
                path: "/tags",
                element: <Tags />,
                errorElement: <Error />,
            },
            {
                path: "/collections",
                element: <Collections />,
                errorElement: <Error />,
            },
            {
                path: "/source",
                element: <Source />,
                errorElement: <Error />,
            },
            {
                path: "/manual-operation",
                element: <ManualOperation />,
                errorElement: <Error />,
            },
        ],
    },
]);

function App() {
    return <RouterProvider router={router} />;
}

export default App;
