# shadcn-vue: Changelog

## Contents

- [November 2025 - Catch up](#november-2025---catch-up)
- [October 2025 - New Components](#october-2025---new-components)
- [February 2025 - Reka UI & npx shadcn-vue@latest init](#february-2025---reka-ui-npx-shadcn-vuelatest-init)

## November 2025 - Catch up

shadcn-vue.com upgraded to Nuxt v4 and Tailwind v4. The site now uses the upgraded
`new-york` components. Minor design updates for speed and navigation.

### Chart

The Chart component was refactored to match the original shadcn/ui Chart component,
sticking to its API as closely as possible.

---

## October 2025 - New Components

Seven new components targeting everyday UI patterns.

### Spinner

An indicator to show a loading state.

```bash
npx shadcn-vue@latest add spinner
```

```vue
<script setup lang="ts">
import { Spinner } from '@/components/ui/spinner'
</script>

<template>
  <Spinner />
</template>
```

Also works inside buttons. The spinner code is open — replace with your own spinner.

### Kbd

Renders a keyboard key or group of keys.

```bash
npx shadcn-vue@latest add kbd
```

```vue
<script setup lang="ts">
import { Kbd, KbdGroup } from '@/components/ui/kbd'
</script>

<template>
  <Kbd>Ctrl</Kbd>
</template>
```

Group keys with `KbdGroup`:

```vue
<template>
  <KbdGroup>
    <Kbd>Ctrl</Kbd>
    <Kbd>B</Kbd>
  </KbdGroup>
</template>
```

Can be added to buttons, tooltips, input groups, and more.

### ButtonGroup

Groups related buttons together with consistent styling. Useful for action groups
and split buttons.

```bash
npx shadcn-vue@latest add button-group
```

```vue
<script setup lang="ts">
import { ButtonGroup } from '@/components/ui/button-group'
</script>

<template>
  <ButtonGroup>
    <Button>Button 1</Button>
    <Button>Button 2</Button>
  </ButtonGroup>
</template>
```

Nested groups for complex layouts:

```vue
<template>
  <ButtonGroup>
    <ButtonGroup>
      <Button>Button 1</Button>
      <Button>Button 2</Button>
    </ButtonGroup>
    <ButtonGroup>
      <Button>Button 3</Button>
      <Button>Button 4</Button>
    </ButtonGroup>
  </ButtonGroup>
</template>
```

Split buttons with `ButtonGroupSeparator`:

```vue
<template>
  <ButtonGroup>
    <ButtonGroupText>Prefix</ButtonGroupText>
    <Input placeholder="Type something here..." />
    <Button>Button</Button>
  </ButtonGroup>
</template>
```

### InputGroup

Adds icons, buttons, text, labels, and more to inputs.

```bash
npx shadcn-vue@latest add input-group
```

```vue
<script setup lang="ts">
import { InputGroup, InputGroupAddon, InputGroupInput } from '@/components/ui/input-group'
</script>

<template>
  <InputGroup>
    <InputGroupInput placeholder="Search..." />
    <InputGroupAddon>
      <SearchIcon />
    </InputGroupAddon>
  </InputGroup>
</template>
```

Supports: icons, buttons, text/labels/tooltips, textareas, spinners.

### Field

A component for building complex forms. Works with all form libraries: Vee Validate,
TanStack Form, and custom solutions.

```bash
npx shadcn-vue@latest add field
```

Basic field:

```vue
<script setup lang="ts">
import {
  Field,
  FieldDescription,
  FieldError,
  FieldLabel,
} from '@/components/ui/field'
</script>

<template>
  <Field>
    <FieldLabel html-for="username">Username</FieldLabel>
    <Input id="username" placeholder="Max Leiter" />
    <FieldDescription>Choose a unique username for your account.</FieldDescription>
  </Field>
</template>
```

Grouping fields:

```vue
<template>
  <FieldSet>
    <FieldLegend />
    <FieldGroup>
      <Field />
      <Field />
    </FieldGroup>
  </FieldSet>
</template>
```

Responsive layout via `orientation="responsive"`:
switches between vertical/horizontal layouts based on container width.

### Item

A flexible container for lists, cards, and more.

```bash
npx shadcn-vue@latest add item
```

```vue
<script setup lang="ts">
import {
  Item,
  ItemContent,
  ItemDescription,
  ItemMedia,
  ItemTitle,
} from '@/components/ui/item'
</script>

<template>
  <Item>
    <ItemMedia variant="icon">
      <HomeIcon />
    </ItemMedia>
    <ItemContent>
      <ItemTitle>Dashboard</ItemTitle>
      <ItemDescription>Overview of your account and activity.</ItemDescription>
    </ItemContent>
  </Item>
</template>
```

As a link using `asChild`:

```vue
<template>
  <Item as-child>
    <a href="/dashboard">
      <ItemMedia variant="icon"><HomeIcon /></ItemMedia>
      <ItemContent>
        <ItemTitle>Dashboard</ItemTitle>
        <ItemDescription>Overview of your account and activity.</ItemDescription>
      </ItemContent>
    </a>
  </Item>
</template>
```

### Empty

Displays empty states in your app.

```bash
npx shadcn-vue@latest add empty
```

```vue
<script setup lang="ts">
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyMedia,
  EmptyTitle,
} from '@/components/ui/empty'
</script>

<template>
  <Empty>
    <EmptyMedia variant="icon">
      <InboxIcon />
    </EmptyMedia>
    <EmptyTitle>No messages</EmptyTitle>
    <EmptyDescription>You don't have any messages yet.</EmptyDescription>
    <EmptyContent>
      <Button>Send a message</Button>
    </EmptyContent>
  </Empty>
</template>
```

---

## February 2025 - Reka UI & npx shadcn-vue@latest init

### Major Changes

- Updated registry to support **Reka UI** instead of Radix Vue
- New CLI available: `npx shadcn-vue@latest init`
- Components now ship their own dependencies (e.g. Accordion ships its Tailwind keyframes)
- Install remote components via URL:
  ```bash
  npx shadcn-vue add https://acme.com/registry/navbar.json
  ```
- New schema for custom component registries (supports private distribution)
- Better error handling and monorepo support

### Reka UI note

As of `shadcn-vue@latest`, Reka UI v2 is used. To keep using Radix Vue:
```bash
# Visit https://radix.shadcn-vue.com and use:
npx shadcn-vue@radix
```

### Example: init with components

```bash
npx shadcn-vue@latest init Sidebar01 Login01
```

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/10.changelog.md`
