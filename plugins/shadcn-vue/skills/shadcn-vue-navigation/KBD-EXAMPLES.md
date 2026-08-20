# Kbd — Beispiele

## Contents

- [Beispiel 1: Basic Kbd (KbdBasic.vue)](#beispiel-1-basic-kbd-kbdbasicvue)
- [Beispiel 2: Kbd with Group (KbdWithGroup.vue)](#beispiel-2-kbd-with-group-kbdwithgroupvue)
- [Quellen](#quellen)

## Beispiel 1: Basic Kbd (KbdBasic.vue)

Einzelne Tasten fur haufige Tastaturkurzel.

```vue
<script setup lang="ts">
import { Kbd } from "@/components/ui/kbd"
</script>

<template>
  <div class="flex flex-wrap items-center gap-4">
    <div class="flex items-center gap-2">
      <span class="text-sm">Save:</span>
      <Kbd>Ctrl</Kbd>
      <span>+</span>
      <Kbd>S</Kbd>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Copy:</span>
      <Kbd>Ctrl</Kbd>
      <span>+</span>
      <Kbd>C</Kbd>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Paste:</span>
      <Kbd>Ctrl</Kbd>
      <span>+</span>
      <Kbd>V</Kbd>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Undo:</span>
      <Kbd>Ctrl</Kbd>
      <span>+</span>
      <Kbd>Z</Kbd>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Search:</span>
      <Kbd>/</Kbd>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Escape:</span>
      <Kbd>Esc</Kbd>
    </div>
  </div>
</template>
```

---

## Beispiel 2: Kbd with Group (KbdWithGroup.vue)

`KbdGroup` kombiniert mehrere Tasten ohne sichtbares Trennzeichen.

```vue
<script setup lang="ts">
import { Kbd, KbdGroup } from "@/components/ui/kbd"
</script>

<template>
  <div class="flex flex-col gap-4">
    <div class="flex items-center gap-2">
      <span class="text-sm">Select all:</span>
      <KbdGroup>
        <Kbd>Ctrl</Kbd>
        <Kbd>A</Kbd>
      </KbdGroup>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Open command palette:</span>
      <KbdGroup>
        <Kbd>Ctrl</Kbd>
        <Kbd>K</Kbd>
      </KbdGroup>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Find and replace:</span>
      <KbdGroup>
        <Kbd>Ctrl</Kbd>
        <Kbd>H</Kbd>
      </KbdGroup>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Multiple selection:</span>
      <KbdGroup>
        <Kbd>Ctrl</Kbd>
        <Kbd>Shift</Kbd>
        <Kbd>L</Kbd>
      </KbdGroup>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-sm">Toggle terminal:</span>
      <KbdGroup>
        <Kbd>Ctrl</Kbd>
        <Kbd>`</Kbd>
      </KbdGroup>
    </div>
  </div>
</template>
```

---

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/kbd/KbdBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/kbd/KbdWithGroup.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/kbd/KbdExample.vue`
