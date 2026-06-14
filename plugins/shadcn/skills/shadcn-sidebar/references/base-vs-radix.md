# Sidebar — Base vs Radix

The Sidebar is the most complex shadcn/ui component. Both variants share the same architecture
but differ in their dependent component implementations.

## Dependency chain differences

| Aspect                | new-york-v4 (Radix)                    | base variant (Base UI)                         |
| --------------------- | -------------------------------------- | ---------------------------------------------- |
| `Sheet` primitive     | `Dialog` from `radix-ui`               | `Dialog` from `@base-ui/react/dialog`          |
| `Tooltip` import      | `TooltipProvider` included             | No `TooltipProvider` wrapper                   |
| `Slot` import         | `Slot` from `radix-ui`                 | `useRender` from `@base-ui/react/use-render` + `mergeProps` |
| Icon in Trigger       | `PanelLeftIcon` from lucide-react      | `IconPlaceholder` (theme-switchable)           |

## Context and hook

Both variants define the same `SidebarContext` and `useSidebar` hook with identical shape.

## SidebarMenuButton tooltip

**Radix variant**: uses `Tooltip`, `TooltipTrigger`, `TooltipContent` from shadcn/ui tooltip (wrapping Radix).

**Base variant**: uses different tooltip implementation from `@base-ui/react`.

## Mobile behavior

Both use `Sheet` for mobile sidebar. The Radix variant uses `SheetContent` with `data-sidebar="sidebar"` and `[&>button]:hidden` to hide the default close button.

## Structural identical parts

The following components are structurally identical between variants:
- `SidebarProvider` context management and cookie persistence
- `useSidebar` hook
- `SidebarProvider` CSS variable injection
- All layout components: Header, Footer, Content, Group, Menu hierarchy
- State data attributes: `data-state`, `data-collapsible`, `data-variant`, `data-side`

## Source files

- `registry/new-york-v4/ui/sidebar.tsx`
- `registry/bases/base/ui/sidebar.tsx`
