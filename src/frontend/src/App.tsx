import { Outlet, createBrowserRouter, RouterProvider } from "react-router-dom";

import { Watch } from "@/pages/Watch.tsx";
import { Error } from "@/pages/Error.tsx";
import { Settings } from "@/pages/Settings.tsx";
import { ManualOperation } from "@/pages/ManualOperation.tsx";
import { NavigationMenuDesktop } from "@/components/NavigationMenuDesktop.tsx";
import { DarkMode } from "@/components/DarkMode.tsx";
import { Token } from "@/components/Token.tsx";
import { ConfigurationProvider } from "@/store/settings.provider.tsx";
import { Source } from "@/pages/Source.tsx";
import { Tags } from "@/pages/Tags.tsx";
//import { Collections } from "@/pages/Collections.tsx";
import { loader as loaderSource } from "@/pages/Source.tsx";
import { loader as loaderManual } from "@/pages/ManualOperation.tsx";
import { loader as loaderTags } from "@/pages/Tags.tsx";
import { loader as loaderError } from "@/pages/Error.tsx";
import { SourcesProvider } from "@/store/sources.provider.tsx";
import { WatchProvider } from "@/store/watch.provider.tsx";
import { ReactNode } from "react";

type ProvidersProps = {
    children: ReactNode;
};
const Providers = ({ children }: ProvidersProps) => {
    /* Wraps app in settings, sources, and tags providers */

    return (
        <ConfigurationProvider>
            <SourcesProvider>
                <WatchProvider>{children}</WatchProvider>
            </SourcesProvider>
        </ConfigurationProvider>
    );
};

function Root() {
    return (
        <Providers>
            <Token>
                <DarkMode>
                    <NavigationMenuDesktop />
                    <Outlet />
                </DarkMode>
            </Token>
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
                loader: loaderTags,
            },
            /*{
                path: "/collections",
                element: <Collections />,
                errorElement: <Error />,
            },
            */
            {
                path: "/source",
                element: <Source />,
                errorElement: <Error />,
                loader: loaderSource,
            },
            {
                path: "/manual-operation",
                element: <ManualOperation />,
                errorElement: <Error />,
                loader: loaderManual,
            },
            {
                path: "/error",
                element: <Error />,
                errorElement: <Error />,
                loader: loaderError,
            },
        ],
    },
]);

function App() {
    return <RouterProvider router={router} />;
}

export default App;
