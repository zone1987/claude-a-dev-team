# Collapsible — Examples

## 1. File Tree (nested collapsible file browser)

```vue
<script setup lang="ts">
import IconPlaceholder from "@/components/IconPlaceholder.vue"
import { Button } from "@/registry/bases/reka/ui/button"
import { Card, CardContent, CardHeader } from "@/registry/bases/reka/ui/card"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/registry/bases/reka/ui/collapsible"
import { Tabs, TabsList, TabsTrigger } from "@/registry/bases/reka/ui/tabs"
import { Example } from "~/registry/bases/reka/components/example"

type FileTreeItem = { name: string } | { name: string, items: FileTreeItem[] }

const fileTree: FileTreeItem[] = [
  {
    name: "components",
    items: [
      {
        name: "ui",
        items: [
          { name: "button.tsx" },
          { name: "card.tsx" },
          { name: "dialog.tsx" },
          { name: "input.tsx" },
          { name: "select.tsx" },
          { name: "table.tsx" },
        ],
      },
      { name: "login-form.tsx" },
      { name: "register-form.tsx" },
    ],
  },
  {
    name: "lib",
    items: [{ name: "utils.ts" }, { name: "cn.ts" }, { name: "api.ts" }],
  },
  {
    name: "hooks",
    items: [
      { name: "use-media-query.ts" },
      { name: "use-debounce.ts" },
      { name: "use-local-storage.ts" },
    ],
  },
  {
    name: "types",
    items: [{ name: "index.d.ts" }, { name: "api.d.ts" }],
  },
  {
    name: "public",
    items: [
      { name: "favicon.ico" },
      { name: "logo.svg" },
      { name: "images" },
    ],
  },
  { name: "app.tsx" },
  { name: "layout.tsx" },
  { name: "globals.css" },
  { name: "package.json" },
  { name: "tsconfig.json" },
  { name: "README.md" },
  { name: ".gitignore" },
]
</script>

<template>
  <Example title="File Tree" class="items-center">
    <Card class="mx-auto w-full max-w-[16rem] gap-2" size="sm">
      <CardHeader>
        <Tabs default-value="explorer">
          <TabsList class="w-full">
            <TabsTrigger value="explorer">Explorer</TabsTrigger>
            <TabsTrigger value="settings">Outline</TabsTrigger>
          </TabsList>
        </Tabs>
      </CardHeader>
      <CardContent>
        <div class="flex flex-col gap-1">
          <template v-for="item in fileTree" :key="item.name">
            <Collapsible v-if="'items' in item">
              <CollapsibleTrigger :as-child="true">
                <Button variant="ghost" size="sm" class="group hover:bg-accent hover:text-accent-foreground w-full justify-start transition-none">
                  Folder: {{ item.name }}
                </Button>
              </CollapsibleTrigger>
              <CollapsibleContent class="mt-1 ml-5">
                <div class="flex flex-col gap-1">
                  <Button v-for="child in item.items" :key="child.name" variant="link" size="sm" class="text-foreground w-full justify-start gap-2">
                    {{ child.name }}
                  </Button>
                </div>
              </CollapsibleContent>
            </Collapsible>
            <Button v-else variant="link" size="sm" class="text-foreground w-full justify-start gap-2">
              {{ item.name }}
            </Button>
          </template>
        </div>
      </CardContent>
    </Card>
  </Example>
</template>
```

## 2. Settings (controlled open state with v-model:open)

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/registry/bases/reka/ui/card"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/registry/bases/reka/ui/collapsible"
import { Field, FieldGroup, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"
import { Example } from "~/registry/bases/reka/components/example"

const isOpen = ref(false)
</script>

<template>
  <Example title="Settings" class="items-center">
    <Card class="mx-auto w-full max-w-xs" size="sm">
      <CardHeader>
        <CardTitle>Radius</CardTitle>
        <CardDescription>Set the corner radius of the element.</CardDescription>
      </CardHeader>
      <CardContent>
        <Collapsible
          v-model:open="isOpen"
          class="flex items-start gap-2"
        >
          <FieldGroup class="grid w-full grid-cols-2 gap-2">
            <Field>
              <FieldLabel html-for="radius-x" class="sr-only">Radius X</FieldLabel>
              <Input id="radius" placeholder="0" :default-value="0" />
            </Field>
            <Field>
              <FieldLabel html-for="radius-y" class="sr-only">Radius Y</FieldLabel>
              <Input id="radius" placeholder="0" :default-value="0" />
            </Field>
            <CollapsibleContent class="col-span-full grid grid-cols-subgrid gap-2">
              <Field>
                <FieldLabel html-for="radius-x" class="sr-only">Radius X</FieldLabel>
                <Input id="radius" placeholder="0" :default-value="0" />
              </Field>
              <Field>
                <FieldLabel html-for="radius-y" class="sr-only">Radius Y</FieldLabel>
                <Input id="radius" placeholder="0" :default-value="0" />
              </Field>
            </CollapsibleContent>
          </FieldGroup>
          <CollapsibleTrigger :as-child="true">
            <Button variant="outline" size="icon">
              {{ isOpen ? 'Collapse' : 'Expand' }}
            </Button>
          </CollapsibleTrigger>
        </Collapsible>
      </CardContent>
    </Card>
  </Example>
</template>
```

Source: `registry/new-york-v4/ui/collapsible/`, `registry/bases/reka/examples/collapsible/`
