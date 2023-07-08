export function getLocalStorageValue(key: string, defaultValue: any) {
    /* gets a value from local storage */
    const storageValue = localStorage.getItem(key);
    if (storageValue) {
        return JSON.parse(storageValue, (_, v) => {
            if (typeof v === "object") {
                return new Map(JSON.parse(storageValue));
            } else {
                return v;
            }
        });
    } else {
        return defaultValue;
    }
}
