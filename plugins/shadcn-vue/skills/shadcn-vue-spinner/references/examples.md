# Examples

## Basic

Default spinner and a larger variant.

```vue
<!-- SpinnerBasic.vue -->
<script setup lang="ts">
import { Spinner } from "@/components/ui/spinner"
</script>

<template>
  <div class="flex items-center gap-6">
    <Spinner />
    <Spinner class="size-6" />
  </div>
</template>
```

## In Buttons

Use inside `<Button>` to indicate loading state.

```vue
<!-- SpinnerInButtons.vue -->
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Spinner } from "@/components/ui/spinner"
</script>

<template>
  <div class="flex flex-wrap items-center gap-4">
    <Button>
      <Spinner data-icon="inline-start" /> Submit
    </Button>
    <Button disabled>
      <Spinner data-icon="inline-start" /> Disabled
    </Button>
    <Button variant="outline" disabled>
      <Spinner data-icon="inline-start" /> Outline
    </Button>
    <Button variant="outline" size="icon" disabled>
      <Spinner data-icon="inline-start" />
      <span class="sr-only">Loading...</span>
    </Button>
  </div>
</template>
```

## In Badges

```vue
<!-- SpinnerInBadges.vue -->
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
import { Spinner } from "@/components/ui/spinner"
</script>

<template>
  <div class="flex flex-wrap items-center justify-center gap-4">
    <Badge>
      <Spinner data-icon="inline-start" />
      Badge
    </Badge>
    <Badge variant="secondary">
      <Spinner data-icon="inline-start" />
      Badge
    </Badge>
    <Badge variant="destructive">
      <Spinner data-icon="inline-start" />
      Badge
    </Badge>
    <Badge variant="outline">
      <Spinner data-icon="inline-start" />
      Badge
    </Badge>
  </div>
</template>
```

## In Input Group

Spinner inside an `InputGroupAddon`.

```vue
<!-- SpinnerInInputGroup.vue -->
<script setup lang="ts">
import { Field, FieldLabel } from "@/components/ui/field"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
} from "@/components/ui/input-group"
import { Spinner } from "@/components/ui/spinner"
</script>

<template>
  <Field>
    <FieldLabel html-for="input-group-spinner">
      Input Group
    </FieldLabel>
    <InputGroup>
      <InputGroupInput id="input-group-spinner" />
      <InputGroupAddon>
        <Spinner />
      </InputGroupAddon>
    </InputGroup>
  </Field>
</template>
```

## In Empty State

Spinner as media icon in an empty state.

```vue
<!-- SpinnerInEmpty.vue -->
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
import { Spinner } from "@/components/ui/spinner"
</script>

<template>
  <Empty class="min-h-[300px]">
    <EmptyHeader>
      <EmptyMedia variant="icon">
        <Spinner />
      </EmptyMedia>
      <EmptyTitle>No projects yet</EmptyTitle>
      <EmptyDescription>
        You haven't created any projects yet. Get started by creating
        your first project.
      </EmptyDescription>
    </EmptyHeader>
    <EmptyContent>
      <div class="flex gap-2">
        <Button :as-child="true">
          <a href="#">Create project</a>
        </Button>
        <Button variant="outline">
          Import project
        </Button>
      </div>
    </EmptyContent>
  </Empty>
</template>
```

Sources:
- `registry/bases/reka/examples/spinner/SpinnerBasic.vue`
- `registry/bases/reka/examples/spinner/SpinnerInButtons.vue`
- `registry/bases/reka/examples/spinner/SpinnerInBadges.vue`
- `registry/bases/reka/examples/spinner/SpinnerInInputGroup.vue`
- `registry/bases/reka/examples/spinner/SpinnerInEmpty.vue`
