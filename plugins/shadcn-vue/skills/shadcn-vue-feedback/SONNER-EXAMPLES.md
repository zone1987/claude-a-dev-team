# Examples

## Contents

- [Basic Toast](#basic-toast)
- [Toast with Description](#toast-with-description)
- [Success Toast](#success-toast)
- [Error Toast](#error-toast)
- [Full Example (SonnerExample.vue)](#full-example-sonnerexamplevue)

## Basic Toast

```vue
<script setup lang="ts">
import { toast } from 'vue-sonner'
import { Button } from '@/components/ui/button'
</script>

<template>
  <Button variant="outline" @click="() => toast('Event has been created')">
    Show Toast
  </Button>
</template>
```

## Toast with Description

```vue
<script setup lang="ts">
import { toast } from 'vue-sonner'
import { Button } from '@/components/ui/button'
</script>

<template>
  <Button
    variant="outline"
    @click="() => toast('Event has been created', {
      description: 'Monday, January 3rd at 6:00pm',
    })"
  >
    Show Toast
  </Button>
</template>
```

## Success Toast

```vue
<script setup lang="ts">
import { toast } from 'vue-sonner'
import { Button } from '@/components/ui/button'
</script>

<template>
  <Button
    variant="outline"
    @click="() => toast.success('Event has been created')"
  >
    Show Success Toast
  </Button>
</template>
```

## Error Toast

```vue
<script setup lang="ts">
import { toast } from 'vue-sonner'
import { Button } from '@/components/ui/button'
</script>

<template>
  <Button
    variant="outline"
    @click="() => toast.error('Something went wrong')"
  >
    Show Error Toast
  </Button>
</template>
```

## Full Example (SonnerExample.vue)

```vue
<!-- SonnerExample.vue -->
<script setup lang="ts">
import { toast } from "vue-sonner"
import { Button } from "@/components/ui/button"

function showBasicToast() {
  toast("Event has been created")
}

function showDescriptionToast() {
  toast("Event has been created", {
    description: "Monday, January 3rd at 6:00pm",
  })
}

function showSuccessToast() {
  toast.success("Event has been created")
}

function showErrorToast() {
  toast.error("Something went wrong")
}
</script>

<template>
  <div class="flex flex-wrap gap-2">
    <Button variant="outline" @click="showBasicToast">
      Show Toast
    </Button>
    <Button variant="outline" @click="showDescriptionToast">
      Show Toast with Description
    </Button>
    <Button variant="outline" @click="showSuccessToast">
      Show Success Toast
    </Button>
    <Button variant="outline" @click="showErrorToast">
      Show Error Toast
    </Button>
  </div>
</template>
```

Sources:
- `registry/bases/reka/examples/sonner/SonnerExample.vue`
