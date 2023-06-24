import type { Meta, StoryObj } from "@storybook/react";

import { Button } from "@/components/buttons/Button.tsx";

const meta = {
    title: "shadcn/button",
    component: Button,
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
    args: {
        variant: "destructive",
    },
};
