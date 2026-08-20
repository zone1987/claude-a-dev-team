# InputGroup — Examples

Sources: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/input-group/`

## Contents

- [Basic — Icons and Text (InputGroupBasic.vue)](#basic--icons-and-text-inputgroupbasicvue)
- [With Buttons (InputGroupWithButton.vue)](#with-buttons-inputgroupwithbuttonvue)
- [With Textarea (InputGroupWithTextarea.vue)](#with-textarea-inputgroupwithtextareavue)
- [Custom Input with data-slot](#custom-input-with-data-slot)

## Basic — Icons and Text (InputGroupBasic.vue)

```vue
<script setup lang="ts">
import { MailIcon } from "@lucide/vue"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
} from "@/registry/bases/reka/ui/input-group"
</script>

<template>
  <div class="grid w-full max-w-sm items-center gap-4">
    <!-- Icon leading -->
    <InputGroup>
      <InputGroupAddon align="inline-start">
        <MailIcon />
      </InputGroupAddon>
      <InputGroupInput type="email" placeholder="Email" />
    </InputGroup>

    <!-- Text trailing -->
    <InputGroup>
      <InputGroupInput type="text" placeholder="Username" />
      <InputGroupAddon align="inline-end">
        @example.com
      </InputGroupAddon>
    </InputGroup>

    <!-- Text leading -->
    <InputGroup>
      <InputGroupAddon align="inline-start">
        https://
      </InputGroupAddon>
      <InputGroupInput type="text" placeholder="example.com" />
    </InputGroup>
  </div>
</template>
```

## With Buttons (InputGroupWithButton.vue)

```vue
<script setup lang="ts">
import { CopyIcon, SearchIcon } from "@lucide/vue"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  InputGroup,
  InputGroupButton,
  InputGroupInput,
} from "@/registry/bases/reka/ui/input-group"
</script>

<template>
  <div class="grid w-full max-w-sm items-center gap-4">
    <!-- Search Button -->
    <InputGroup>
      <InputGroupInput type="text" placeholder="Search..." />
      <InputGroupButton>
        <Button>
          <SearchIcon />
        </Button>
      </InputGroupButton>
    </InputGroup>

    <!-- Copy Button -->
    <InputGroup>
      <InputGroupButton>
        <Button variant="outline">
          <CopyIcon />
        </Button>
      </InputGroupButton>
      <InputGroupInput type="text" placeholder="Copy this text" />
    </InputGroup>

    <!-- Increment/Decrement -->
    <InputGroup>
      <InputGroupButton>
        <Button variant="outline" size="sm">-</Button>
      </InputGroupButton>
      <InputGroupInput type="number" placeholder="0" />
      <InputGroupButton>
        <Button variant="outline" size="sm">+</Button>
      </InputGroupButton>
    </InputGroup>
  </div>
</template>
```

## With Textarea (InputGroupWithTextarea.vue)

Textarea with `block-start` / `block-end` addons.

```vue
<script setup lang="ts">
import { MessageSquareIcon, SendIcon } from "@lucide/vue"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupTextarea,
} from "@/registry/bases/reka/ui/input-group"
</script>

<template>
  <div class="grid w-full max-w-sm items-center gap-4">
    <!-- Icon leading (block) -->
    <InputGroup>
      <InputGroupAddon align="inline-start">
        <MessageSquareIcon />
      </InputGroupAddon>
      <InputGroupTextarea placeholder="Type your message here..." />
    </InputGroup>

    <!-- Send icon trailing -->
    <InputGroup>
      <InputGroupTextarea placeholder="Add a comment..." rows="4" />
      <InputGroupAddon align="inline-end">
        <SendIcon />
      </InputGroupAddon>
    </InputGroup>
  </div>
</template>
```

## Custom Input with data-slot

```vue
<template>
  <div class="grid w-full max-w-sm gap-6">
    <InputGroup>
      <textarea
        data-slot="input-group-control"
        class="flex field-sizing-content min-h-16 w-full resize-none rounded-md bg-transparent px-3 py-2.5 text-base transition-[color,box-shadow] outline-none md:text-sm"
        placeholder="Autoresize textarea..."
      />
      <InputGroupAddon align="block-end">
        <InputGroupButton class="ml-auto" size="sm" variant="default">
          Submit
        </InputGroupButton>
      </InputGroupAddon>
    </InputGroup>
  </div>
</template>
```

Sources:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/input-group/`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/input-group.md`
