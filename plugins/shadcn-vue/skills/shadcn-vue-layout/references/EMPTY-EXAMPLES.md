# Empty — Examples

Sources: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/empty/`

## Contents

- [Basic (EmptyBasic.vue)](#basic-emptybasicvue)
- [With Icon (EmptyWithIcon.vue)](#with-icon-emptywithiconvue)
- [With Border (EmptyWithBorder.vue)](#with-border-emptywithbordervue)
- [With Background (EmptyWithMutedBackground.vue)](#with-background-emptywithmutedbackgroundvue)
- [In Card (EmptyInCard.vue)](#in-card-emptyincardvue)

## Basic (EmptyBasic.vue)

Simple empty state without an icon, only with title and description.

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyTitle,
} from "@/registry/bases/reka/ui/empty"
</script>

<template>
  <Empty>
    <EmptyHeader>
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
        <Button variant="outline">Import project</Button>
      </div>
    </EmptyContent>
  </Empty>
</template>
```

## With Icon (EmptyWithIcon.vue)

EmptyMedia with `variant="icon"` for a styled icon container.

```vue
<script setup lang="ts">
import { FolderIcon } from "@lucide/vue"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/registry/bases/reka/ui/empty"
</script>

<template>
  <Empty class="border">
    <EmptyHeader>
      <EmptyMedia variant="icon">
        <FolderIcon />
      </EmptyMedia>
      <EmptyTitle>Nothing to see here</EmptyTitle>
      <EmptyDescription>
        No posts have been created yet.
        <a href="#">Create your first post</a>.
      </EmptyDescription>
    </EmptyHeader>
    <EmptyContent>
      <Button variant="outline">New Post</Button>
    </EmptyContent>
  </Empty>
</template>
```

## With Border (EmptyWithBorder.vue)

`class="border"` on `Empty` for a visible border.

```vue
<template>
  <Empty class="border">
    <EmptyHeader>
      <EmptyTitle>404 - Not Found</EmptyTitle>
      <EmptyDescription>
        The page you're looking for doesn't exist.
      </EmptyDescription>
    </EmptyHeader>
    <EmptyContent>
      <InputGroup class="w-3/4">
        <InputGroupInput placeholder="Try searching for pages..." />
      </InputGroup>
    </EmptyContent>
  </Empty>
</template>
```

## With Background (EmptyWithMutedBackground.vue)

`class="bg-muted"` for a gray background.

```vue
<template>
  <Empty class="bg-muted">
    <EmptyHeader>
      <EmptyTitle>No results found</EmptyTitle>
      <EmptyDescription>
        No results found for your search. Try adjusting your search terms.
      </EmptyDescription>
    </EmptyHeader>
    <EmptyContent>
      <Button>Try again</Button>
    </EmptyContent>
  </Empty>
</template>
```

## In Card (EmptyInCard.vue)

Empty state inside a Card component with an icon.

```vue
<script setup lang="ts">
import { FolderIcon } from "@lucide/vue"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/registry/bases/reka/ui/empty"
</script>

<template>
  <Empty>
    <EmptyHeader>
      <EmptyMedia variant="icon">
        <FolderIcon />
      </EmptyMedia>
      <EmptyTitle>No projects yet</EmptyTitle>
      <EmptyDescription>
        You haven't created any projects yet.
      </EmptyDescription>
    </EmptyHeader>
    <EmptyContent>
      <div class="flex gap-2">
        <Button :as-child="true">
          <a href="#">Create project</a>
        </Button>
        <Button variant="outline">Import project</Button>
      </div>
    </EmptyContent>
  </Empty>
</template>
```

Sources:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/empty/`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/empty.md`
