export function Collections() {
    return (
        <div className="bg-background p-5">
            <h2 className="text-foreground mt-10 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0">
                Collections
            </h2>
            <p className="text-foreground leading-7 [&:not(:first-child)]:mt-6 pb-4">
                These are the user-defined collections; you can create
                collections for grouping tags here.
            </p>
        </div>
    );
}
