# shadcn/ui — Theming

shadcn/ui uses CSS variables for theming by default. This gives semantic theme
tokens that components use. Override those tokens in your CSS to change the look
of your app without rewriting component classes.

```tsx
<div className="bg-background text-foreground" />
<div className="bg-primary text-primary-foreground" />
```

## Token Convention

Background/foreground pairs. The base token controls the surface color; the
`-foreground` variant controls the text color on that surface.

```css
--primary: oklch(0.205 0 0);
--primary-foreground: oklch(0.985 0 0);
```

```tsx
<div className="bg-primary text-primary-foreground">Hello</div>
```

## All Theme Tokens

| Token | What it controls | Used by |
|-------|-----------------|---------|
| `background` / `foreground` | Default app background and text | Page shell, sections, default text |
| `card` / `card-foreground` | Elevated surfaces | Card, dashboard panels |
| `popover` / `popover-foreground` | Floating surfaces | Popover, DropdownMenu, ContextMenu |
| `primary` / `primary-foreground` | High-emphasis, brand surfaces | Default Button, selected states, badges |
| `secondary` / `secondary-foreground` | Lower-emphasis filled actions | Secondary buttons, badges |
| `muted` / `muted-foreground` | Subtle surfaces and subdued content | Descriptions, placeholders, helper text |
| `accent` / `accent-foreground` | Hover/focus/active surfaces | Ghost buttons, menu highlight, hovered rows |
| `destructive` | Destructive actions and error emphasis | Destructive buttons, invalid states |
| `border` | Default borders and separators | Cards, menus, tables |
| `input` | Form control borders | Input, Textarea, Select |
| `ring` | Focus rings | Buttons, inputs, checkboxes |
| `chart-1` ... `chart-5` | Chart palette | Charts |
| `sidebar` / `sidebar-foreground` | Sidebar base | Sidebar container |
| `sidebar-primary` / `sidebar-primary-foreground` | Sidebar high-emphasis | Active items, badges |
| `sidebar-accent` / `sidebar-accent-foreground` | Sidebar hover/selected | Sidebar menu hover states |
| `sidebar-border` | Sidebar borders | Sidebar headers, groups |
| `sidebar-ring` | Sidebar focus rings | Focused controls in sidebar |
| `radius` | Base corner radius scale | Cards, inputs, buttons |

## Reference files

- [TOKENS.md](TOKENS.md)
- [FULL-THEME.md](FULL-THEME.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/theming.mdx`
