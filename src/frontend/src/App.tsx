import { ReactNode } from "react";
import { Outlet, createBrowserRouter, RouterProvider } from "react-router-dom";

import { Home } from "@/pages/Home.tsx";
import { Error } from "@/pages/Error.tsx";
import { Settings } from "@/pages/Settings.tsx";
import { ManualOperation } from "@/pages/ManualOperation.tsx";
import { NavigationMenuDesktop } from "@/components/NavigationMenuDesktop.tsx";

import { ConfigurationProvider } from "@/store/settings.provider.tsx";

type ProviderProps = {
    children: ReactNode;
};

function Providers({ children }: ProviderProps) {
    return <ConfigurationProvider>{children}</ConfigurationProvider>;
}

function Root() {
    return (
        <Providers>
            <div className="bg-background p-5">
                <NavigationMenuDesktop />
                <Outlet />
            </div>
        </Providers>
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
                element: <Home />,
                errorElement: <Error />,
            },
            {
                path: "/settings",
                element: <Settings />,
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
