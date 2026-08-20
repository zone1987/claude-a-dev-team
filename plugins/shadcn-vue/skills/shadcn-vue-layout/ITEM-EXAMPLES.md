# Item — Examples

## Contents

- [Example 1: Basic Item (ItemBasic.vue)](#example-1-basic-item-itembasicvue)
- [Example 2: Item with Actions (ItemWithActions.vue)](#example-2-item-with-actions-itemwithactionsvue)
- [Sources](#sources)

## Example 1: Basic Item (ItemBasic.vue)

Basic usage of `Item` with `ItemMedia`, `ItemContent`, `ItemTitle` and `ItemDescription`.

```vue
<script setup lang="ts">
import {
  Item,
  ItemContent,
  ItemDescription,
  ItemGroup,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"
import { UserIcon } from "@lucide/vue"
</script>

<template>
  <ItemGroup class="w-full max-w-md">
    <Item>
      <ItemMedia>
        <UserIcon />
      </ItemMedia>
      <ItemContent>
        <ItemTitle>John Doe</ItemTitle>
        <ItemDescription>Software Engineer</ItemDescription>
      </ItemContent>
    </Item>

    <Item>
      <ItemMedia>
        <MailIcon />
      </ItemMedia>
      <ItemContent>
        <ItemTitle>Email Notifications</ItemTitle>
        <ItemDescription>Receive email updates about your account</ItemDescription>
      </ItemContent>
    </Item>

    <Item>
      <ItemMedia>
        <BellIcon />
      </ItemMedia>
      <ItemContent>
        <ItemTitle>Push Notifications</ItemTitle>
        <ItemDescription>Receive push notifications on your device</ItemDescription>
      </ItemContent>
    </Item>
  </ItemGroup>
</template>
```

---

## Example 2: Item with Actions (ItemWithActions.vue)

`ItemActions` with ghost buttons for file actions (Download, Delete, Share).

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import {
  Item,
  ItemActions,
  ItemContent,
  ItemDescription,
  ItemGroup,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"
import { FileIcon, DownloadIcon, TrashIcon, ImageIcon, EyeIcon, Share2Icon, VideoIcon, PlayIcon, MoreHorizontalIcon } from "@lucide/vue"
</script>

<template>
  <ItemGroup class="w-full max-w-md">
    <Item>
      <ItemMedia>
        <FileIcon />
      </ItemMedia>
      <ItemContent>
        <ItemTitle>Document.pdf</ItemTitle>
        <ItemDescription>Updated 2 hours ago</ItemDescription>
      </ItemContent>
      <ItemActions>
        <Button variant="ghost" size="sm">
          <DownloadIcon />
        </Button>
        <Button variant="ghost" size="sm">
          <TrashIcon />
        </Button>
      </ItemActions>
    </Item>

    <Item>
      <ItemMedia>
        <ImageIcon />
      </ItemMedia>
      <ItemContent>
        <ItemTitle>Screenshot.png</ItemTitle>
        <ItemDescription>Updated yesterday</ItemDescription>
      </ItemContent>
      <ItemActions>
        <Button variant="ghost" size="sm">
          <EyeIcon />
        </Button>
        <Button variant="ghost" size="sm">
          <Share2Icon />
        </Button>
      </ItemActions>
    </Item>

    <Item>
      <ItemMedia>
        <VideoIcon />
      </ItemMedia>
      <ItemContent>
        <ItemTitle>Presentation.mp4</ItemTitle>
        <ItemDescription>Updated last week</ItemDescription>
      </ItemContent>
      <ItemActions>
        <Button variant="ghost" size="sm">
          <PlayIcon />
        </Button>
        <Button variant="ghost" size="sm">
          <MoreHorizontalIcon />
        </Button>
      </ItemActions>
    </Item>
  </ItemGroup>
</template>
```

---

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/item/ItemBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/item/ItemWithActions.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/item/ItemExample.vue`
