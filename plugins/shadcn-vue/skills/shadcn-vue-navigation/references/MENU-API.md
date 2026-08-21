# NavigationMenu — API reference

## Contents

- [NavigationMenu (Root)](#navigationmenu-root)
- [NavigationMenuList](#navigationmenulist)
- [NavigationMenuItem](#navigationmenuitem)
- [NavigationMenuTrigger](#navigationmenutrigger)
- [NavigationMenuContent](#navigationmenucontent)
- [NavigationMenuLink](#navigationmenulink)
- [NavigationMenuViewport](#navigationmenuviewport)
- [NavigationMenuIndicator](#navigationmenuindicator)
- [Exported utility](#exported-utility)
- [reka-ui reference](#reka-ui-reference)

## NavigationMenu (Root)

Based on reka-ui `NavigationMenuRoot`. Automatically includes `NavigationMenuViewport`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `viewport` | `boolean` | `true` | Include the viewport component |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |
| All `NavigationMenuRootProps` | — | Forwarded |

### Emits

| Event | Type | Description |
|---|---|---|
| All `NavigationMenuRootEmits` | — | Forwarded |

---

## NavigationMenuList

Horizontal list of the menu entries.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `NavigationMenuListProps` | — | Forwarded |

---

## NavigationMenuItem

Single navigation entry. Can contain `Trigger + Content` or a direct `Link`.

### Props

| Prop | Type | Description |
|---|---|---|
| `value` | `string` | Unique value (for controlled mode) |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## NavigationMenuTrigger

Button with a ChevronDown icon that rotates on `data-[state=open]`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `NavigationMenuTriggerProps` | — | Forwarded |

---

## NavigationMenuContent

Dropdown panel content. Animations are based on `data-motion`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `NavigationMenuContentProps` | — | Forwarded |

---

## NavigationMenuLink

Active-state-aware link. Detects `data-active` automatically.

### Props

| Prop | Type | Description |
|---|---|---|
| `active` | `boolean` | Active state |
| `asChild` | `boolean` | Renders as child (for `<a>` tags) |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## NavigationMenuViewport

Animated floating panel. Normally included automatically by `NavigationMenu`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## NavigationMenuIndicator

Animated arrow indicator below the active trigger.

---

## Exported utility

```ts
export const navigationMenuTriggerStyle = cva("...")
// Returns a CVA class name string, usable on standalone links
```

### Usage

```vue
<NavigationMenuLink
  :class="navigationMenuTriggerStyle()"
  href="/docs"
>
  Documentation
</NavigationMenuLink>
```

## reka-ui reference
- https://reka-ui.com/docs/components/navigation-menu
