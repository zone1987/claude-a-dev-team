# Breadcrumb — Examples

## Contents

- [Basic](#basic)
- [With Dropdown (collapsed items)](#with-dropdown-collapsed-items)
- [With Custom Links (asChild + BreadcrumbEllipsis)](#with-custom-links-aschild-breadcrumbellipsis)

## Basic

A standard three-segment breadcrumb: Home > Components > Breadcrumb.
Uses `BreadcrumbLink` for navigable ancestors and `BreadcrumbPage` for the current page.

```vue
<script setup lang="ts">
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
</script>

<template>
  <Breadcrumb>
    <BreadcrumbList>
      <BreadcrumbItem>
        <BreadcrumbLink href="/">Home</BreadcrumbLink>
      </BreadcrumbItem>
      <BreadcrumbSeparator />
      <BreadcrumbItem>
        <BreadcrumbLink href="/components">Components</BreadcrumbLink>
      </BreadcrumbItem>
      <BreadcrumbSeparator />
      <BreadcrumbItem>
        <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
      </BreadcrumbItem>
    </BreadcrumbList>
  </Breadcrumb>
</template>
```

---

## With Dropdown (collapsed items)

When the breadcrumb trail is long, collapse intermediate segments behind a `DropdownMenu`
triggered by `BreadcrumbEllipsis`. The user can click the ellipsis to reveal the hidden pages.

```vue
<script setup lang="ts">
import {
  Breadcrumb,
  BreadcrumbEllipsis,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
</script>

<template>
  <Breadcrumb>
    <BreadcrumbList>
      <!-- First visible segment -->
      <BreadcrumbItem>
        <BreadcrumbLink href="/">Home</BreadcrumbLink>
      </BreadcrumbItem>
      <BreadcrumbSeparator />

      <!-- Collapsed segments behind a dropdown -->
      <BreadcrumbItem>
        <DropdownMenu>
          <DropdownMenuTrigger class="flex items-center gap-1">
            <BreadcrumbEllipsis />
            <span class="sr-only">Toggle menu</span>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="start">
            <DropdownMenuItem>
              <BreadcrumbLink href="/docs">Documentation</BreadcrumbLink>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <BreadcrumbLink href="/docs/themes">Themes</BreadcrumbLink>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <BreadcrumbLink href="/docs/themes/colors">Colors</BreadcrumbLink>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </BreadcrumbItem>
      <BreadcrumbSeparator />

      <!-- Last visible ancestor -->
      <BreadcrumbItem>
        <BreadcrumbLink href="/docs/components">Components</BreadcrumbLink>
      </BreadcrumbItem>
      <BreadcrumbSeparator />

      <!-- Current page -->
      <BreadcrumbItem>
        <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
      </BreadcrumbItem>
    </BreadcrumbList>
  </Breadcrumb>
</template>
```

---

## With Custom Links (asChild + BreadcrumbEllipsis)

Use `as-child` on `BreadcrumbLink` to render framework-native links (NuxtLink, RouterLink)
without extra DOM wrappers. Combine with `BreadcrumbEllipsis` for paths with many segments.

```vue
<script setup lang="ts">
import {
  Breadcrumb,
  BreadcrumbEllipsis,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
// NuxtLink is auto-imported in Nuxt projects
// RouterLink is auto-imported in Vue Router projects
</script>

<template>
  <Breadcrumb>
    <BreadcrumbList>
      <!-- NuxtLink via asChild -->
      <BreadcrumbItem>
        <BreadcrumbLink as-child>
          <NuxtLink to="/">Home</NuxtLink>
        </BreadcrumbLink>
      </BreadcrumbItem>
      <BreadcrumbSeparator>
        <!-- Custom separator: slash instead of chevron -->
        <span aria-hidden="true">/</span>
      </BreadcrumbSeparator>

      <!-- Ellipsis for collapsed middle segments -->
      <BreadcrumbItem>
        <BreadcrumbEllipsis />
      </BreadcrumbItem>
      <BreadcrumbSeparator>
        <span aria-hidden="true">/</span>
      </BreadcrumbSeparator>

      <!-- RouterLink via asChild -->
      <BreadcrumbItem>
        <BreadcrumbLink as-child>
          <RouterLink to="/components">Components</RouterLink>
        </BreadcrumbLink>
      </BreadcrumbItem>
      <BreadcrumbSeparator>
        <span aria-hidden="true">/</span>
      </BreadcrumbSeparator>

      <!-- Current page (no link) -->
      <BreadcrumbItem>
        <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
      </BreadcrumbItem>
    </BreadcrumbList>
  </Breadcrumb>
</template>
```

---

Source: shadcn-vue breadcrumb component
