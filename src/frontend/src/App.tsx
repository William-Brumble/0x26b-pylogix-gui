import { Outlet, createBrowserRouter, RouterProvider } from "react-router-dom";

import { Watch } from "@/pages/Watch.tsx";
import { Error } from "@/pages/Error.tsx";
import { Settings } from "@/pages/Settings.tsx";
import { ManualOperation } from "@/pages/ManualOperation.tsx";
import { NavigationMenuDesktop } from "@/components/NavigationMenuDesktop.tsx";
import { DarkMode } from "@/components/DarkMode.tsx";
import { ConfigurationProvider } from "@/store/settings.provider.tsx";
import { Source } from "@/pages/Source.tsx";
import { Tags } from "@/pages/Tags.tsx";
//import { Collections } from "@/pages/Collections.tsx";
import { loader as loaderSource } from "@/pages/Source.tsx";
import { loader as loaderManual } from "@/pages/ManualOperation.tsx";
import { loader as loaderTags } from "@/pages/Tags.tsx";
import { loader as loaderError } from "@/pages/Error.tsx";
import { useContext, useEffect } from "react";
import { SettingsContext } from "@/store/settings.context.tsx";
import { SourcesProvider } from "@/store/sources.provider.tsx";
import { TagsProvider } from "@/store/tags.provider.tsx";

function Root() {
    const settings = useContext(SettingsContext);

    useEffect(() => {
        /*
            On linux this isn't an issue, but on winblows
            you need to reference the global pywebview object after
            component has mounted fully.
         */
        const token = window?.pywebview?.token;
        if (token) {
            settings.setToken?.(token);
        }
    }, []);

    return (
        <ConfigurationProvider>
            <SourcesProvider>
                <TagsProvider>
                    <DarkMode>
                        <NavigationMenuDesktop />
                        <Outlet />
                    </DarkMode>
                </TagsProvider>
            </SourcesProvider>
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
