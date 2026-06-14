# Sidebar — Theming

## CSS Variables

```css
@layer base {
  :root {
    --sidebar-background: 0 0% 98%;
    --sidebar-foreground: 240 5.3% 26.1%;
    --sidebar-primary: 240 5.9% 10%;
    --sidebar-primary-foreground: 0 0% 98%;
    --sidebar-accent: 240 4.8% 95.9%;
    --sidebar-accent-foreground: 240 5.9% 10%;
    --sidebar-border: 220 13% 91%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }

  .dark {
    --sidebar-background: 240 5.9% 10%;
    --sidebar-foreground: 240 4.8% 95.9%;
    --sidebar-primary: 0 0% 98%;
    --sidebar-primary-foreground: 240 5.9% 10%;
    --sidebar-accent: 240 3.7% 15.9%;
    --sidebar-accent-foreground: 240 4.8% 95.9%;
    --sidebar-border: 240 3.7% 15.9%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }
}
```

## CSS Structural Variables

Set by `SidebarProvider` on the wrapper `div`:

| Variable                 | Default  | Description                     |
| ------------------------ | -------- | ------------------------------- |
| `--sidebar-width`        | `16rem`  | Desktop sidebar width           |
| `--sidebar-width-icon`   | `3rem`   | Width when collapsed to icons   |

Mobile width is set inline on the `SheetContent`:

| Variable                 | Default  | Description                     |
| ------------------------ | -------- | ------------------------------- |
| `--sidebar-width`        | `18rem`  | Mobile sheet width (overrides desktop) |

## Styling patterns

### Hide group when icon-collapsed

```tsx
<SidebarGroup className="group-data-[collapsible=icon]:hidden" />
```

### Show action only on hover

```tsx
<SidebarMenuAction
  className="peer-data-[active=true]/menu-button:opacity-100"
/>
```

### Collapsible group with Collapsible component

```tsx
<Collapsible defaultOpen className="group/collapsible">
  <SidebarGroup>
    <SidebarGroupLabel asChild>
      <CollapsibleTrigger>
        Help
        <ChevronDown className="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180" />
      </CollapsibleTrigger>
    </SidebarGroupLabel>
    <CollapsibleContent>
      <SidebarGroupContent />
    </CollapsibleContent>
  </SidebarGroup>
</Collapsible>
```

## RTL support

Pass `dir` prop to `Sidebar` and update positioning classes:

```tsx
<Sidebar dir="rtl" side="right">
  {/* ... */}
</Sidebar>
```

RTL changes require:
1. `dir` prop forwarded to `SheetContent` for mobile
2. `data-side={side}` attribute on container
3. Updated container positioning to use `data-[side=left]:left-0 data-[side=right]:right-0`
4. Updated `SidebarRail` to use `ltr:-translate-x-1/2 rtl:-translate-x-1/2`
5. `PanelLeftIcon className="rtl:rotate-180"` in `SidebarTrigger`

## Source files

- `registry/new-york-v4/ui/sidebar.tsx`
- `content/docs/components/base/sidebar.mdx`
