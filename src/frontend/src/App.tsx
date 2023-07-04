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

function Root() {
    const token = window?.pywebview?.token ? window.pywebview.token : "test";

    return (
        <ConfigurationProvider>
            <DarkMode>
                <NavigationMenuDesktop token={token} />
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
        ],
    },
]);

function App() {
    return <RouterProvider router={router} />;
}

export default App;
