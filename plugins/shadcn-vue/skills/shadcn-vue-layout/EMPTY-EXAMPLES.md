# Empty — Beispiele

Quellen: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/empty/`

## Contents

- [Basic (EmptyBasic.vue)](#basic-emptybasicvue)
- [Mit Icon (EmptyWithIcon.vue)](#mit-icon-emptywithiconvue)
- [Mit Rahmen (EmptyWithBorder.vue)](#mit-rahmen-emptywithbordervue)
- [Mit Hintergrund (EmptyWithMutedBackground.vue)](#mit-hintergrund-emptywithmutedbackgroundvue)
- [In Card (EmptyInCard.vue)](#in-card-emptyincardvue)

## Basic (EmptyBasic.vue)

Einfacher leerer Zustand ohne Icon, nur mit Titel und Beschreibung.

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

## Mit Icon (EmptyWithIcon.vue)

EmptyMedia mit `variant="icon"` fuer einen gestylten Icon-Container.

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

## Mit Rahmen (EmptyWithBorder.vue)

`class="border"` auf `Empty` fuer einen sichtbaren Rand.

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

## Mit Hintergrund (EmptyWithMutedBackground.vue)

`class="bg-muted"` fuer grauen Hintergrund.

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

Empty-State innerhalb einer Card-Komponente mit Icon.

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

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/empty/`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/empty.md`
