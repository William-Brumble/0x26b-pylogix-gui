import { useEffect, useState } from "react";

import "./App.css";

import { ManualOperation } from "@/pages/ManualOperation.tsx";

// TODO: Create interfaces for the handler events.

function App() {
    const [token, setToken] = useState("");

    useEffect(() => {
        setToken(window?.pywebview?.token);
    }, []);

    return (
        <div className="bg-background p-5">
            <ManualOperation token={token} />
        </div>
    );
}

export default App;
