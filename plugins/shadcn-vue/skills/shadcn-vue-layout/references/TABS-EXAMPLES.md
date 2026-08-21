# Examples

## Contents

- [Basic](#basic)
- [Line Variant](#line-variant)
- [With Content](#with-content)
- [Vertical](#vertical)
- [Disabled Tab](#disabled-tab)
- [With Icons](#with-icons)
- [With Dropdown (Overflow)](#with-dropdown-overflow)

## Basic

Two tabs without content panels.

```vue
<!-- TabsBasic.vue -->
<script setup lang="ts">
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
</script>

<template>
  <Tabs default-value="home">
    <TabsList>
      <TabsTrigger value="home">Home</TabsTrigger>
      <TabsTrigger value="settings">Settings</TabsTrigger>
    </TabsList>
  </Tabs>
</template>
```

## Line Variant

Underline-style tabs using `variant="line"`.

```vue
<!-- TabsLine.vue -->
<script setup lang="ts">
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
</script>

<template>
  <Tabs default-value="overview">
    <TabsList variant="line">
      <TabsTrigger value="overview">Overview</TabsTrigger>
      <TabsTrigger value="analytics">Analytics</TabsTrigger>
      <TabsTrigger value="reports">Reports</TabsTrigger>
    </TabsList>
  </Tabs>
</template>
```

## With Content

Tabs with content panels.

```vue
<!-- TabsWithContent.vue -->
<script setup lang="ts">
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
</script>

<template>
  <Tabs default-value="account">
    <TabsList>
      <TabsTrigger value="account">Account</TabsTrigger>
      <TabsTrigger value="password">Password</TabsTrigger>
      <TabsTrigger value="notifications">Notifications</TabsTrigger>
    </TabsList>
    <div class="border rounded-lg p-4">
      <TabsContent value="account">
        Manage your account preferences and profile information.
      </TabsContent>
      <TabsContent value="password">
        Update your password to keep your account secure.
      </TabsContent>
      <TabsContent value="notifications">
        Configure how you receive notifications and alerts.
      </TabsContent>
    </div>
  </Tabs>
</template>
```

## Vertical

Vertical layout with `orientation="vertical"`.

```vue
<!-- TabsVertical.vue -->
<script setup lang="ts">
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
</script>

<template>
  <Tabs default-value="account" orientation="vertical">
    <TabsList>
      <TabsTrigger value="account">Account</TabsTrigger>
      <TabsTrigger value="password">Password</TabsTrigger>
      <TabsTrigger value="notifications">Notifications</TabsTrigger>
    </TabsList>
    <div class="border rounded-lg p-4">
      <TabsContent value="account">
        Manage your account preferences and profile information.
      </TabsContent>
      <TabsContent value="password">
        Update your password to keep your account secure. Use a strong
        password with a mix of letters, numbers, and symbols.
      </TabsContent>
      <TabsContent value="notifications">
        Configure how you receive notifications and alerts.
      </TabsContent>
    </div>
  </Tabs>
</template>
```

## Disabled Tab

One tab in disabled state.

```vue
<!-- TabsDisabled.vue -->
<script setup lang="ts">
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
</script>

<template>
  <Tabs default-value="home">
    <TabsList>
      <TabsTrigger value="home">Home</TabsTrigger>
      <TabsTrigger value="settings" :disabled="true">Disabled</TabsTrigger>
    </TabsList>
  </Tabs>
</template>
```

## With Icons

Tabs with icon + label.

```vue
<!-- TabsWithIcons.vue -->
<script setup lang="ts">
import { AppWindowIcon, CodeIcon } from "@lucide/vue"
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
</script>

<template>
  <Tabs default-value="preview">
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
  </Tabs>
</template>
```

## With Dropdown (Overflow)

Tabs combined with an overflow dropdown menu.

```vue
<!-- TabsWithDropdown.vue -->
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import {
  DropdownMenu, DropdownMenuContent, DropdownMenuItem,
  DropdownMenuSeparator, DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
</script>

<template>
  <Tabs default-value="overview">
    <div class="flex items-center justify-between">
      <TabsList>
        <TabsTrigger value="overview">Overview</TabsTrigger>
        <TabsTrigger value="analytics">Analytics</TabsTrigger>
        <TabsTrigger value="reports">Reports</TabsTrigger>
      </TabsList>
      <DropdownMenu>
        <DropdownMenuTrigger :as-child="true">
          <Button variant="ghost" size="icon" class="size-8">...</Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end">
          <DropdownMenuItem>Settings</DropdownMenuItem>
          <DropdownMenuItem>Export</DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuItem>Archive</DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
    <div class="border rounded-lg p-4">
      <TabsContent value="overview">View your dashboard metrics.</TabsContent>
      <TabsContent value="analytics">Detailed analytics and insights.</TabsContent>
      <TabsContent value="reports">Generate and view custom reports.</TabsContent>
    </div>
  </Tabs>
</template>
```

Sources:
- `registry/bases/reka/examples/tabs/TabsBasic.vue`
- `registry/bases/reka/examples/tabs/TabsLine.vue`
- `registry/bases/reka/examples/tabs/TabsWithContent.vue`
- `registry/bases/reka/examples/tabs/TabsVertical.vue`
- `registry/bases/reka/examples/tabs/TabsDisabled.vue`
- `registry/bases/reka/examples/tabs/TabsWithIcons.vue`
- `registry/bases/reka/examples/tabs/TabsIconOnly.vue`
- `registry/bases/reka/examples/tabs/TabsMultiple.vue`
- `registry/bases/reka/examples/tabs/TabsLineWithContent.vue`
- `registry/bases/reka/examples/tabs/TabsLineDisabled.vue`
- `registry/bases/reka/examples/tabs/TabsWithDropdown.vue`
- `registry/bases/reka/examples/tabs/TabsVariantsComparison.vue`
- `registry/bases/reka/examples/tabs/TabsWithInputAndButton.vue`
