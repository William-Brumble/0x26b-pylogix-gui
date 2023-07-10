import { ReactNode, useContext, useEffect, useState } from "react";
import { SettingsContext } from "@/store/settings.context.tsx";

type TokenProps = {
    children: ReactNode;
};

export function Token({ children }: TokenProps) {
    /* Sets the context token for the rest of the
     * application allowing routes to consume the
     * correct token, when not running from pywebview
     * the value is set to default context,
     * otherwise this value is a random has set
     * by the backend */
    const settings = useContext(SettingsContext);
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        const handleLoad = () => {
            setIsLoaded(true);
        };

        if (document.readyState === "complete") {
            setIsLoaded(true);
        } else {
            document.addEventListener("DOMContentLoaded", handleLoad);
        }

        return () => {
            document.removeEventListener("DOMContentLoaded", handleLoad);
        };
    }, []);

    if (isLoaded) {
        const window_token = window?.pywebview?.token;
        if (window_token) {
            settings.setToken?.(window_token);
        }
        return <>{children}</>;
    } else {
        return <>Loading...</>;
    }
}
