import { useContext } from "react";
import * as z from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";

import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { Input } from "@/components/ui/input.tsx";
import {
    Form,
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form";
import { SettingsContext } from "@/store/settings.context.tsx";

const FormSchema = z.object({
    dark_mode: z.boolean(),
    refresh_rate: z.coerce.number(),
});

export function Settings() {
    const settings = useContext(SettingsContext);

    const form = useForm<z.infer<typeof FormSchema>>({
        resolver: zodResolver(FormSchema),
        defaultValues: {
            dark_mode: settings.darkMode,
            refresh_rate: settings.refreshRate,
        },
    });

    function onSubmit(data: z.infer<typeof FormSchema>) {
        settings.setRefreshRate?.(data.refresh_rate);
        settings.setDarkMode?.(data.dark_mode);
    }

    return (
        <div className="bg-background p-5">
            <Form {...form}>
                <form
                    onSubmit={form.handleSubmit(onSubmit)}
                    className="w-full space-y-6"
                >
                    <div>
                        <div className="space-y-4">
                            <FormField
                                control={form.control}
                                name="dark_mode"
                                render={({ field }) => (
                                    <FormItem className="flex flex-row items-center justify-between rounded-lg border p-4">
                                        <div className="space-y-0.5">
                                            <FormLabel className="text-base text-foreground">
                                                Dark mode
                                            </FormLabel>
                                            <FormDescription>
                                                Toggle Dark Mode in Settings for
                                                a sleek and easy-on-the-eyes
                                                interface.
                                            </FormDescription>
                                        </div>
                                        <FormControl>
                                            <Switch
                                                checked={field.value}
                                                onCheckedChange={field.onChange}
                                            />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="refresh_rate"
                                render={({ field }) => (
                                    <FormItem className="flex flex-row items-center justify-between rounded-lg border p-4">
                                        <div className="space-y-0.5">
                                            <FormLabel className="text-base text-foreground">
                                                Refresh rate
                                            </FormLabel>
                                            <FormDescription>
                                                Fine-tune the time delay between
                                                tag reads with the Refresh Rate
                                                setting
                                            </FormDescription>
                                            <FormMessage />
                                        </div>
                                        <FormControl>
                                            <Input
                                                className="text-foreground"
                                                type="number"
                                                placeholder="Input refresh rate"
                                                {...field}
                                            />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                        </div>
                    </div>
                    <Button type="submit">Submit</Button>
                </form>
            </Form>
        </div>
    );
}
