export {};
declare global {
    interface Window {
        pywebview: {
            token: string;
        };
    }

}
window.pywebview = window.pywebview || {};