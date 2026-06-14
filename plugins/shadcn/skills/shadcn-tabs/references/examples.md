# Tabs — Examples

## Default Demo (`tabs-demo.tsx`)

Full demo showing account/password tabs with Card content, Input fields, Labels, and a save Button.

```tsx
import { AppWindowIcon, CodeIcon } from "lucide-react"

import { Button } from "@/registry/new-york-v4/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/registry/new-york-v4/ui/card"
import { Input } from "@/registry/new-york-v4/ui/input"
import { Label } from "@/registry/new-york-v4/ui/label"
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/registry/new-york-v4/ui/tabs"

export default function TabsDemo() {
  return (
    <div className="flex w-full max-w-sm flex-col gap-6">
      <Tabs defaultValue="account">
        <TabsList>
          <TabsTrigger value="account">Account</TabsTrigger>
          <TabsTrigger value="password">Password</TabsTrigger>
        </TabsList>
        <TabsContent value="account">
          <Card>
            <CardHeader>
              <CardTitle>Account</CardTitle>
              <CardDescription>
                Make changes to your account here. Click save when you&apos;re
                done.
              </CardDescription>
            </CardHeader>
            <CardContent className="grid gap-6">
              <div className="grid gap-3">
                <Label htmlFor="tabs-demo-name">Name</Label>
                <Input id="tabs-demo-name" defaultValue="Pedro Duarte" />
              </div>
              <div className="grid gap-3">
                <Label htmlFor="tabs-demo-username">Username</Label>
                <Input id="tabs-demo-username" defaultValue="@peduarte" />
              </div>
            </CardContent>
            <CardFooter>
              <Button>Save changes</Button>
            </CardFooter>
          </Card>
        </TabsContent>
        <TabsContent value="password">
          <Card>
            <CardHeader>
              <CardTitle>Password</CardTitle>
              <CardDescription>
                Change your password here. After saving, you&apos;ll be logged
                out.
              </CardDescription>
            </CardHeader>
            <CardContent className="grid gap-6">
              <div className="grid gap-3">
                <Label htmlFor="tabs-demo-current">Current password</Label>
                <Input id="tabs-demo-current" type="password" />
              </div>
              <div className="grid gap-3">
                <Label htmlFor="tabs-demo-new">New password</Label>
                <Input id="tabs-demo-new" type="password" />
              </div>
            </CardContent>
            <CardFooter>
              <Button>Save password</Button>
            </CardFooter>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}
```

## Line Variant

Use `variant="line"` on `TabsList` to render a minimal underline-style indicator instead of the default pill/card background.

```tsx
<Tabs defaultValue="preview">
  <TabsList variant="line">
    <TabsTrigger value="preview">Preview</TabsTrigger>
    <TabsTrigger value="code">Code</TabsTrigger>
  </TabsList>
  <TabsContent value="preview">
    <p>Preview content here.</p>
  </TabsContent>
  <TabsContent value="code">
    <pre><code>const x = 1</code></pre>
  </TabsContent>
</Tabs>
```

## Vertical Orientation

Use `orientation="vertical"` on `Tabs` to stack `TabsList` and `TabsContent` side by side. The list renders vertically and triggers expand to full width.

```tsx
<Tabs defaultValue="general" orientation="vertical" className="w-full max-w-lg">
  <TabsList>
    <TabsTrigger value="general">General</TabsTrigger>
    <TabsTrigger value="security">Security</TabsTrigger>
    <TabsTrigger value="billing">Billing</TabsTrigger>
  </TabsList>
  <TabsContent value="general">
    <p>General settings panel.</p>
  </TabsContent>
  <TabsContent value="security">
    <p>Security settings panel.</p>
  </TabsContent>
  <TabsContent value="billing">
    <p>Billing settings panel.</p>
  </TabsContent>
</Tabs>
```

## Disabled Tab

Add `disabled` to a `TabsTrigger` to prevent interaction. The trigger becomes non-clickable and is rendered at reduced opacity.

```tsx
<Tabs defaultValue="active">
  <TabsList>
    <TabsTrigger value="active">Active</TabsTrigger>
    <TabsTrigger value="disabled" disabled>
      Disabled
    </TabsTrigger>
    <TabsTrigger value="other">Other</TabsTrigger>
  </TabsList>
  <TabsContent value="active">This tab is active.</TabsContent>
  <TabsContent value="disabled">You cannot reach this tab.</TabsContent>
  <TabsContent value="other">Other content here.</TabsContent>
</Tabs>
```

## With Icons

Include icons inside `TabsTrigger` alongside label text. SVG icons are automatically sized to `size-4` when no explicit size class is set.

```tsx
import { AppWindowIcon, CodeIcon } from "lucide-react"

<Tabs defaultValue="preview">
  <TabsList>
    <TabsTrigger value="preview">
      <AppWindowIcon />
      Preview
    </TabsTrigger>
    <TabsTrigger value="code">
      <CodeIcon />
      Code
    </TabsTrigger>
  </TabsList>
  <TabsContent value="preview">
    <p>Rendered output.</p>
  </TabsContent>
  <TabsContent value="code">
    <pre><code>// source code</code></pre>
  </TabsContent>
</Tabs>
```

## Controlled Tabs

Use `value` and `onValueChange` to control the active tab from outside the component.

```tsx
import { useState } from "react"

export function ControlledTabs() {
  const [tab, setTab] = useState("overview")

  return (
    <>
      <button onClick={() => setTab("settings")}>Go to Settings</button>
      <Tabs value={tab} onValueChange={setTab}>
        <TabsList>
          <TabsTrigger value="overview">Overview</TabsTrigger>
          <TabsTrigger value="settings">Settings</TabsTrigger>
        </TabsList>
        <TabsContent value="overview">Overview content.</TabsContent>
        <TabsContent value="settings">Settings content.</TabsContent>
      </Tabs>
    </>
  )
}
```

## Force Mounted Content

Use `forceMount` on `TabsContent` to keep content in the DOM even when the tab is inactive. Useful for animations or preserving form state.

```tsx
<Tabs defaultValue="a">
  <TabsList>
    <TabsTrigger value="a">Tab A</TabsTrigger>
    <TabsTrigger value="b">Tab B</TabsTrigger>
  </TabsList>
  <TabsContent value="a" forceMount>
    Always mounted, hidden via CSS when inactive.
  </TabsContent>
  <TabsContent value="b" forceMount>
    Always mounted, hidden via CSS when inactive.
  </TabsContent>
</Tabs>
```
