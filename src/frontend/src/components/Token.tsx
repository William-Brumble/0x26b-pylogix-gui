import { ReactNode, useContext, useEffect } from "react";
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

    const window_token = window?.pywebview?.token;
    useEffect(() => {
        settings.setToken?.(window_token);
    }, [window_token]);

    return <>{children}</>;
}
