import { Progress } from "@/components/ui/progress";

type LoadingProps = {
    text: string;
};
export function Loading({ text }: LoadingProps) {
    return (
        <>
            <p className="py-4">{text}</p>
            <Progress />
        </>
    );
}
