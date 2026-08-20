# Breadcrumb — API Reference

## Contents

- [Anatomy](#anatomy)
- [Breadcrumb](#breadcrumb)
- [BreadcrumbList](#breadcrumblist)
- [BreadcrumbItem](#breadcrumbitem)
- [BreadcrumbLink](#breadcrumblink)
- [BreadcrumbPage](#breadcrumbpage)
- [BreadcrumbSeparator](#breadcrumbseparator)
- [BreadcrumbEllipsis](#breadcrumbellipsis)

## Anatomy

```vue
<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink href="/">Home</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbPage>Current Page</BreadcrumbPage>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

---

## Breadcrumb

Root `<nav>` element. Provides the landmark and accessible label for the breadcrumb trail.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

**Accessibility:** Renders `aria-label="breadcrumb"` on the `<nav>` element, identifying it as a navigation landmark to assistive technologies.

**Slots:** `default`

---

## BreadcrumbList

`<ol>` container for all breadcrumb items and separators. Provides horizontal flex layout with wrapping.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

**Base classes:** `text-muted-foreground flex flex-wrap items-center gap-1.5 text-sm break-words sm:gap-2.5`

**Slots:** `default`

---

## BreadcrumbItem

`<li>` wrapper for an individual breadcrumb segment. Use it around `BreadcrumbLink`, `BreadcrumbPage`, or `BreadcrumbEllipsis`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

**Base classes:** `inline-flex items-center gap-1.5`

**Slots:** `default`

---

## BreadcrumbLink

Polymorphic link element built on reka-ui `Primitive`. Defaults to `<a>` but can render any element or component via `as` / `asChild`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `as` | `string \| Component` | `"a"` | Element or component to render |
| `asChild` | `boolean` | `false` | Merge props onto the child element instead of rendering a wrapper |
| `class` | `string` | — | Additional CSS classes |
| `href` | `string` | — | URL (when `as="a"`, the default) |

**Base classes:** `hover:text-foreground transition-colors`

**asChild pattern** — Use when you need a framework-native link:

```vue
<!-- NuxtLink -->
<BreadcrumbLink as-child>
  <NuxtLink to="/components">Components</NuxtLink>
</BreadcrumbLink>

<!-- Vue Router -->
<BreadcrumbLink as-child>
  <RouterLink to="/components">Components</RouterLink>
</BreadcrumbLink>
```

**Slots:** `default`

---

## BreadcrumbPage

Marks the current (last) page in the breadcrumb trail. Renders as `<span>` — not an anchor, because the current page should not be a navigable link.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

**Base classes:** `text-foreground font-normal`

**Accessibility attributes (always set):**

| Attribute | Value | Purpose |
|-----------|-------|---------|
| `role` | `"link"` | Semantically communicates it is the current link destination |
| `aria-disabled` | `"true"` | Signals the link is not interactive |
| `aria-current` | `"page"` | Tells screen readers this is the currently active page |

**Slots:** `default`

---

## BreadcrumbSeparator

Visual divider between breadcrumb items. Renders as `<li>` but is hidden from assistive technologies.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

**Base classes:** `[&>svg]:size-3.5` (sizes any SVG icon inside the separator to 14 px)

**Default slot content:** `<ChevronRight />` from `@lucide/vue`

**Custom separator:**

```vue
<BreadcrumbSeparator>
  <SlashIcon />
</BreadcrumbSeparator>

<!-- or with a text character -->
<BreadcrumbSeparator>/</BreadcrumbSeparator>
```

**Accessibility attributes (always set):**

| Attribute | Value | Purpose |
|-----------|-------|---------|
| `role` | `"presentation"` | Removes element from accessibility tree |
| `aria-hidden` | `"true"` | Hides from screen readers |

**Slots:** `default` (override to provide a custom separator icon or character)

---

## BreadcrumbEllipsis

Indicator for collapsed / hidden intermediate segments. Use inside a `BreadcrumbItem` alongside a `DropdownMenu` or tooltip to reveal the hidden pages.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

**Base classes:** `flex size-9 items-center justify-center`

**Default slot content:** `<MoreHorizontal class="size-4" />` from `@lucide/vue`

**Screen-reader text:** Always renders `<span class="sr-only">More</span>` inside, regardless of the slot.

**Accessibility attributes (always set):**

| Attribute | Value | Purpose |
|-----------|-------|---------|
| `role` | `"presentation"` | Removes element from accessibility tree |
| `aria-hidden` | `"true"` | Hides from screen readers (sr-only span provides the label) |

**Slots:** `default` (override to provide a custom icon)

---

Source: shadcn-vue breadcrumb component
