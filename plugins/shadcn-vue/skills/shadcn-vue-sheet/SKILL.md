---
name: shadcn-vue-sheet
description: >
  shadcn-vue Sheet component (reka-ui DialogRoot, slide-in panel, Tailwind v4 Vue SFC).
  Triggers: "shadcn-vue sheet", "sheet component vue", "slide panel vue",
  "drawer vue", "side panel vue", "sheet reka-ui", "einschubpanel vue shadcn"
---

# shadcn-vue Sheet Component

## Overview

The `Sheet` component extends the Dialog component to display content that slides in from
any side of the screen (top, right, bottom, left). It is built on reka-ui's `DialogRoot`
and reuses the same primitives as the Dialog component.

## Sub-components

| Component | reka-ui Primitive | Purpose |
|---|---|---|
| Sheet | DialogRoot | Root state container |
| SheetTrigger | DialogTrigger | Opens the sheet |
| SheetContent | DialogContent + DialogPortal | Slide-in panel with overlay |
| SheetOverlay | DialogOverlay | Backdrop overlay |
| SheetClose | DialogClose | Closes the sheet |
| SheetHeader | div | Sticky header area |
| SheetFooter | div | Sticky footer area |
| SheetTitle | DialogTitle | Accessible title |
| SheetDescription | DialogDescription | Accessible description |

## Usage

```vue
<script setup lang="ts">
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet'
</script>

<template>
  <Sheet>
    <SheetTrigger>Open</SheetTrigger>
    <SheetContent>
      <SheetHeader>
        <SheetTitle>Edit profile</SheetTitle>
        <SheetDescription>
          Make changes to your profile here.
        </SheetDescription>
      </SheetHeader>
    </SheetContent>
  </Sheet>
</template>
```

## Sides

Use the `side` prop on `SheetContent` to control the slide direction:

```vue
<SheetContent side="right">...</SheetContent>  <!-- default -->
<SheetContent side="left">...</SheetContent>
<SheetContent side="top">...</SheetContent>
<SheetContent side="bottom">...</SheetContent>
```

## Controlled

```vue
<script setup lang="ts">
import { ref } from 'vue'
const open = ref(false)
</script>
<template>
  <Sheet v-model:open="open">
    ...
  </Sheet>
</template>
```
