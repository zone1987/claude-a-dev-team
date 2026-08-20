# Accordion — Base UI vs Radix UI

## Dependency

| | Radix UI | Base UI |
|---|---|---|
| Package | `radix-ui` | `@base-ui/react` |
| Import | `from "radix-ui"` | `from "@base-ui/react/accordion"` |

## Component API differences

| | Radix UI | Base UI |
|---|---|---|
| Content type | `AccordionPrimitive.Content` | `AccordionPrimitive.Panel` |
| Open/closed detection | `data-[state=open]` | `aria-expanded` group selector |
| Multiple open | `type="multiple"` | `multiple` boolean prop |
| Chevron | Single rotating chevron | Two separate icons (up/down), icon-swapped |
| Animation classes | `animate-accordion-up/down` | `h-(--accordion-panel-height) data-starting-style:h-0` |
| Style approach | Direct Tailwind classes | `cn-*` CSS class tokens |

## render prop

Radix uses standard React children composition. Base UI supports the `render`
prop pattern for polymorphic rendering.

## Icon system

Base version uses `IconPlaceholder` component supporting multiple icon
libraries (Lucide, Tabler, HugeIcons, Phosphor, RemixIcon). Radix version
hard-codes `ChevronDownIcon` from `lucide-react`.

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/accordion.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/accordion.tsx`
