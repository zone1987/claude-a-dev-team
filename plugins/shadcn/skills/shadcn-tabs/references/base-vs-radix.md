# Tabs — new-york-v4 vs Radix Base

Both variants are built on the same Radix UI Tabs primitive (`radix-ui`) and export the same four components plus `tabsListVariants`. The differences are in how orientation state is communicated via data attributes and how the theme system is attached.

## Orientation data attributes

| | new-york-v4 | Radix base |
|---|---|---|
| Attribute written to Root | `data-orientation="horizontal"` / `data-orientation="vertical"` | `data-orientation="horizontal"` / `data-orientation="vertical"` (set by Radix itself when orientation prop is passed) |
| `orientation` prop forwarded to Root | Yes — `orientation={orientation}` is passed explicitly | No — the base omits forwarding the prop; Radix sets `data-orientation` internally based on prop but the wrapper does not re-forward it |
| Tailwind selectors on Tabs Root | `data-[orientation=horizontal]:flex-col` | `data-horizontal:flex-col` |
| Tailwind selectors on child components | `group-data-[orientation=vertical]/tabs:...` | `group-data-vertical/tabs:...` |

The new-york-v4 variant uses the full `data-[orientation=...]` attribute selector form required by standard Tailwind v3 arbitrary-value syntax.

The radix base variant uses the shorter `data-horizontal` / `data-vertical` form enabled by Tailwind v4's new data-attribute variant shorthand (`data-<value>`), where boolean-style attributes match if the attribute is present with any value or with the exact value.

## Theme system classes (`cn-*`)

The radix base adds `cn-tabs`, `cn-tabs-list`, `cn-tabs-list-variant-default`, `cn-tabs-list-variant-line`, `cn-tabs-trigger`, and `cn-tabs-content` CSS classes to each element. These are semantic marker classes used by the shadcn theme/token system to target specific components for theming overrides without relying on Tailwind utility class specificity.

The new-york-v4 variant does not include these `cn-*` marker classes. It relies entirely on Tailwind utilities and `data-slot` attributes for styling.

## `data-slot` attributes

Both variants set identical `data-slot` attributes:

| Component | `data-slot` value |
|---|---|
| `Tabs` | `"tabs"` |
| `TabsList` | `"tabs-list"` |
| `TabsTrigger` | `"tabs-trigger"` |
| `TabsContent` | `"tabs-content"` |

These allow parent components or CSS to target Tabs parts generically via `[data-slot="tabs-trigger"]` selectors.

## Active state selectors

| | new-york-v4 | Radix base |
|---|---|---|
| Active trigger | `data-[state=active]:...` | `data-active:...` |
| Line indicator visible | `group-data-[variant=line]/tabs-list:data-[state=active]:after:opacity-100` | `group-data-[variant=line]/tabs-list:data-active:after:opacity-100` |

Radix UI sets `data-state="active"` on the active trigger. In new-york-v4 this is matched with `data-[state=active]`. In the radix base, the shorter `data-active` form is used (Tailwind v4 shorthand that matches `data-state="active"` via the presence of an attribute whose value equals "active").

## Summary

Use new-york-v4 when targeting Tailwind v3 projects or the standard shadcn registry output. Use the radix base when building within the shadcn base registry for Tailwind v4 projects that use the `cn-*` theme class system and the short `data-<value>` attribute variant syntax.

Both variants expose the same public API: `Tabs`, `TabsList`, `TabsTrigger`, `TabsContent`, and `tabsListVariants`.
