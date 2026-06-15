# Sidebar Blocks 01–04: Vollstaendiger Code

---

## Block: sidebar-01

**Description:** Simple sidebar with navigation grouped by sections + VersionSwitcher + SearchForm

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-01
```

**File tree:**
```
sidebar-01/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── VersionSwitcher.vue
    └── SearchForm.vue
```

### page.vue
```vue
<script lang="ts">
export const iframeHeight = "800px"
export const description
  = "A simple sidebar with navigation grouped by section."
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-01/components/AppSidebar.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/registry/new-york-v4/ui/breadcrumb"
import { Separator } from "@/registry/new-york-v4/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <SidebarProvider>
    <AppSidebar />
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 border-b px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator
          orientation="vertical"
          class="mr-2 data-[orientation=vertical]:h-4"
        />
        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem class="hidden md:block">
              <BreadcrumbLink href="#">
                Building Your Application
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem>
              <BreadcrumbPage>Data Fetching</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>
      <div class="flex flex-1 flex-col gap-4 p-4">
        <div class="grid auto-rows-min gap-4 md:grid-cols-3">
          <div class="bg-muted/50 aspect-video rounded-xl" />
          <div class="bg-muted/50 aspect-video rounded-xl" />
          <div class="bg-muted/50 aspect-video rounded-xl" />
        </div>
        <div class="bg-muted/50 min-h-[100vh] flex-1 rounded-xl md:min-h-min" />
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
```

### components/VersionSwitcher.vue
```vue
<script setup lang="ts">
import { Check, ChevronsUpDown, GalleryVerticalEnd } from "@lucide/vue"

import { ref } from "vue"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"

import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<{
  versions: string[]
  defaultVersion: string
}>()

const selectedVersion = ref(props.defaultVersion)
</script>

<template>
  <SidebarMenu>
    <SidebarMenuItem>
      <DropdownMenu>
        <DropdownMenuTrigger as-child>
          <SidebarMenuButton
            size="lg"
            class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
          >
            <div class="bg-sidebar-primary text-sidebar-primary-foreground flex aspect-square size-8 items-center justify-center rounded-lg">
              <GalleryVerticalEnd class="size-4" />
            </div>
            <div class="flex flex-col gap-0.5 leading-none">
              <span class="font-medium">Documentation</span>
              <span class="">v{{ selectedVersion }}</span>
            </div>
            <ChevronsUpDown class="ml-auto" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent
          class="w-(--reka-dropdown-menu-trigger-width)"
          align="start"
        >
          <DropdownMenuItem
            v-for="version in versions"
            :key="version"
            @select="selectedVersion = version"
          >
            v{{ version }}
            <Check v-if="version === selectedVersion" class="ml-auto" />
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
```

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"
import SearchForm from "@/registry/new-york-v4/blocks/sidebar-01/components/SearchForm.vue"
import VersionSwitcher from "@/registry/new-york-v4/blocks/sidebar-01/components/VersionSwitcher.vue"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<SidebarProps>()

// This is sample data.
const data = {
  versions: ["1.0.1", "1.1.0-alpha", "2.0.0-beta1"],
  navMain: [
    {
      title: "Getting Started",
      url: "#",
      items: [
        { title: "Installation", url: "#" },
        { title: "Project Structure", url: "#" },
      ],
    },
    {
      title: "Building Your Application",
      url: "#",
      items: [
        { title: "Routing", url: "#" },
        { title: "Data Fetching", url: "#", isActive: true },
        { title: "Rendering", url: "#" },
        { title: "Caching", url: "#" },
        { title: "Styling", url: "#" },
        { title: "Optimizing", url: "#" },
        { title: "Configuring", url: "#" },
        { title: "Testing", url: "#" },
        { title: "Authentication", url: "#" },
        { title: "Deploying", url: "#" },
        { title: "Upgrading", url: "#" },
        { title: "Examples", url: "#" },
      ],
    },
    {
      title: "API Reference",
      url: "#",
      items: [
        { title: "Components", url: "#" },
        { title: "File Conventions", url: "#" },
        { title: "Functions", url: "#" },
        { title: "next.config.js Options", url: "#" },
        { title: "CLI", url: "#" },
        { title: "Edge Runtime", url: "#" },
      ],
    },
    {
      title: "Architecture",
      url: "#",
      items: [
        { title: "Accessibility", url: "#" },
        { title: "Fast Refresh", url: "#" },
        { title: "Next.js Compiler", url: "#" },
        { title: "Supported Browsers", url: "#" },
        { title: "Turbopack", url: "#" },
      ],
    },
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <VersionSwitcher
        :versions="data.versions"
        :default-version="data.versions[0]!"
      />
      <SearchForm />
    </SidebarHeader>
    <SidebarContent>
      <SidebarGroup v-for="item in data.navMain" :key="item.title">
        <SidebarGroupLabel>{{ item.title }}</SidebarGroupLabel>
        <SidebarGroupContent>
          <SidebarMenu>
            <SidebarMenuItem v-for="childItem in item.items" :key="childItem.title">
              <SidebarMenuButton as-child :is-active="childItem.isActive">
                <a :href="childItem.url">{{ childItem.title }}</a>
              </SidebarMenuButton>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
    </SidebarContent>
    <SidebarRail />
  </Sidebar>
</template>
```

### components/SearchForm.vue
```vue
<script setup lang="ts">
import { Search } from "@lucide/vue"
import { Label } from "@/registry/new-york-v4/ui/label"
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarInput,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <form>
    <SidebarGroup class="py-0">
      <SidebarGroupContent class="relative">
        <Label for="search" class="sr-only">
          Search
        </Label>
        <SidebarInput
          id="search"
          placeholder="Search the docs..."
          class="pl-8"
        />
        <Search class="pointer-events-none absolute top-1/2 left-2 size-4 -translate-y-1/2 opacity-50 select-none" />
      </SidebarGroupContent>
    </SidebarGroup>
  </form>
</template>
```

---

## Block: sidebar-02

**Description:** Sidebar with collapsible subnavigation, inset style

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-02
```

**File tree:**
```
sidebar-02/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── VersionSwitcher.vue
    └── SearchForm.vue
```

### page.vue
```vue
<script lang="ts">
export const iframeHeight = "800px"
export const description = "A sidebar with collapsible sections."
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-02/components/AppSidebar.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/registry/new-york-v4/ui/breadcrumb"
import { Separator } from "@/registry/new-york-v4/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <SidebarProvider>
    <AppSidebar />
    <SidebarInset>
      <header class="bg-background sticky top-0 flex h-16 shrink-0 items-center gap-2 border-b px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mr-2 h-4" />
        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem class="hidden md:block">
              <BreadcrumbLink href="#">
                Building Your Application
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem>
              <BreadcrumbPage>Data Fetching</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>
      <div class="flex flex-1 flex-col gap-4 p-4">
        <div
          v-for="i in 24"
          :key="i"
          class="aspect-video h-12 w-full rounded-lg bg-muted/50"
        />
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
```

### components/VersionSwitcher.vue
```vue
<script setup lang="ts">
import { Check, ChevronsUpDown, GalleryVerticalEnd } from "@lucide/vue"

import { ref } from "vue"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"
import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<{
  versions: string[]
  defaultVersion: string
}>()

const selectedVersion = ref(props.defaultVersion)
</script>

<template>
  <SidebarMenu>
    <SidebarMenuItem>
      <DropdownMenu>
        <DropdownMenuTrigger as-child>
          <SidebarMenuButton
            size="lg"
            class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
          >
            <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
              <GalleryVerticalEnd class="size-4" />
            </div>
            <div class="flex flex-col gap-0.5 leading-none">
              <span class="font-medium">Documentation</span>
              <span class="">v{{ selectedVersion }}</span>
            </div>
            <ChevronsUpDown class="ml-auto" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent
          class="w-(--reka-dropdown-menu-trigger-width)"
          align="start"
        >
          <DropdownMenuItem
            v-for="version in versions"
            :key="version"
            @select="selectedVersion = version"
          >
            v{{ version }}
            <Check v-if="selectedVersion === version" class="ml-auto" />
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
```

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"
import { ChevronRight } from "@lucide/vue"
import SearchForm from "@/registry/new-york-v4/blocks/sidebar-02/components/SearchForm.vue"
import VersionSwitcher from "@/registry/new-york-v4/blocks/sidebar-02/components/VersionSwitcher.vue"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/registry/new-york-v4/ui/collapsible"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<SidebarProps>()

// This is sample data.
const data = {
  versions: ["1.0.1", "1.1.0-alpha", "2.0.0-beta1"],
  navMain: [
    {
      title: "Getting Started",
      url: "#",
      items: [
        { title: "Installation", url: "#" },
        { title: "Project Structure", url: "#" },
      ],
    },
    {
      title: "Building Your Application",
      url: "#",
      items: [
        { title: "Routing", url: "#" },
        { title: "Data Fetching", url: "#", isActive: true },
        { title: "Rendering", url: "#" },
        { title: "Caching", url: "#" },
        { title: "Styling", url: "#" },
        { title: "Optimizing", url: "#" },
        { title: "Configuring", url: "#" },
        { title: "Testing", url: "#" },
        { title: "Authentication", url: "#" },
        { title: "Deploying", url: "#" },
        { title: "Upgrading", url: "#" },
        { title: "Examples", url: "#" },
      ],
    },
    {
      title: "API Reference",
      url: "#",
      items: [
        { title: "Components", url: "#" },
        { title: "File Conventions", url: "#" },
        { title: "Functions", url: "#" },
        { title: "next.config.js Options", url: "#" },
        { title: "CLI", url: "#" },
        { title: "Edge Runtime", url: "#" },
      ],
    },
    {
      title: "Architecture",
      url: "#",
      items: [
        { title: "Accessibility", url: "#" },
        { title: "Fast Refresh", url: "#" },
        { title: "Next.js Compiler", url: "#" },
        { title: "Supported Browsers", url: "#" },
        { title: "Turbopack", url: "#" },
      ],
    },
    {
      title: "Community",
      url: "#",
      items: [
        { title: "Contribution Guide", url: "#" },
      ],
    },
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <VersionSwitcher
        :versions="data.versions"
        :default-version="data.versions[0]!"
      />
      <SearchForm />
    </SidebarHeader>
    <SidebarContent class="gap-0">
      <Collapsible
        v-for="item in data.navMain"
        :key="item.title"
        :title="item.title"
        default-open
        class="group/collapsible"
      >
        <SidebarGroup>
          <SidebarGroupLabel
            as-child
            class="group/label text-sm text-sidebar-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
          >
            <CollapsibleTrigger>
              {{ item.title }}
              <ChevronRight class="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-90" />
            </CollapsibleTrigger>
          </SidebarGroupLabel>
          <CollapsibleContent>
            <SidebarGroupContent>
              <SidebarMenu>
                <SidebarMenuItem v-for="childItem in item.items" :key="childItem.title">
                  <SidebarMenuButton as-child :is-active="childItem.isActive">
                    <a :href="item.url">{{ childItem.title }}</a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              </SidebarMenu>
            </SidebarGroupContent>
          </CollapsibleContent>
        </SidebarGroup>
      </Collapsible>
    </SidebarContent>
    <SidebarRail />
  </Sidebar>
</template>
```

### components/SearchForm.vue
```vue
<script setup lang="ts">
import { Search } from "@lucide/vue"
import { Label } from "@/registry/new-york-v4/ui/label"
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarInput,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <form>
    <SidebarGroup class="py-0">
      <SidebarGroupContent class="relative">
        <Label for="search" class="sr-only">
          Search
        </Label>
        <SidebarInput
          id="search"
          placeholder="Search the docs..."
          class="pl-8"
        />
        <Search class="pointer-events-none absolute left-2 top-1/2 size-4 -translate-y-1/2 select-none opacity-50" />
      </SidebarGroupContent>
    </SidebarGroup>
  </form>
</template>
```

---

## Block: sidebar-03

**Description:** Sidebar with collapsible subnavigation, floating style

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-03
```

**File tree:**
```
sidebar-03/
├── page.vue
└── components/
    └── AppSidebar.vue
```

### page.vue
```vue
<script lang="ts">
export const iframeHeight = "800px"
export const description = "A sidebar with submenus."
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-03/components/AppSidebar.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/registry/new-york-v4/ui/breadcrumb"
import { Separator } from "@/registry/new-york-v4/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <SidebarProvider>
    <AppSidebar />
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 border-b">
        <div class="flex items-center gap-2 px-3">
          <SidebarTrigger />
          <Separator orientation="vertical" class="mr-2 h-4" />
          <Breadcrumb>
            <BreadcrumbList>
              <BreadcrumbItem class="hidden md:block">
                <BreadcrumbLink href="#">
                  Building Your Application
                </BreadcrumbLink>
              </BreadcrumbItem>
              <BreadcrumbSeparator class="hidden md:block" />
              <BreadcrumbItem>
                <BreadcrumbPage>Data Fetching</BreadcrumbPage>
              </BreadcrumbItem>
            </BreadcrumbList>
          </Breadcrumb>
        </div>
      </header>
      <div class="flex flex-1 flex-col gap-4 p-4">
        <div class="grid auto-rows-min gap-4 md:grid-cols-3">
          <div class="bg-muted/50 aspect-video rounded-xl" />
          <div class="bg-muted/50 aspect-video rounded-xl" />
          <div class="bg-muted/50 aspect-video rounded-xl" />
        </div>
        <div class="bg-muted/50 min-h-[100vh] flex-1 rounded-xl md:min-h-min" />
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
```

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"

import { GalleryVerticalEnd } from "@lucide/vue"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarRail,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<SidebarProps>()

// This is sample data.
const data = {
  navMain: [
    {
      title: "Getting Started",
      url: "#",
      items: [
        { title: "Installation", url: "#" },
        { title: "Project Structure", url: "#" },
      ],
    },
    {
      title: "Building Your Application",
      url: "#",
      items: [
        { title: "Routing", url: "#" },
        { title: "Data Fetching", url: "#", isActive: true },
        { title: "Rendering", url: "#" },
        { title: "Caching", url: "#" },
        { title: "Styling", url: "#" },
        { title: "Optimizing", url: "#" },
        { title: "Configuring", url: "#" },
        { title: "Testing", url: "#" },
        { title: "Authentication", url: "#" },
        { title: "Deploying", url: "#" },
        { title: "Upgrading", url: "#" },
        { title: "Examples", url: "#" },
      ],
    },
    {
      title: "API Reference",
      url: "#",
      items: [
        { title: "Components", url: "#" },
        { title: "File Conventions", url: "#" },
        { title: "Functions", url: "#" },
        { title: "next.config.js Options", url: "#" },
        { title: "CLI", url: "#" },
        { title: "Edge Runtime", url: "#" },
      ],
    },
    {
      title: "Architecture",
      url: "#",
      items: [
        { title: "Accessibility", url: "#" },
        { title: "Fast Refresh", url: "#" },
        { title: "Next.js Compiler", url: "#" },
        { title: "Supported Browsers", url: "#" },
        { title: "Turbopack", url: "#" },
      ],
    },
    {
      title: "Community",
      url: "#",
      items: [
        { title: "Contribution Guide", url: "#" },
      ],
    },
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton size="lg" as-child>
            <a href="#">
              <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                <GalleryVerticalEnd class="size-4" />
              </div>
              <div class="flex flex-col gap-0.5 leading-none">
                <span class="font-medium">Documentation</span>
                <span class="">v1.0.0</span>
              </div>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarHeader>
    <SidebarContent>
      <SidebarGroup>
        <SidebarMenu>
          <SidebarMenuItem v-for="item in data.navMain" :key="item.title">
            <SidebarMenuButton as-child>
              <a :href="item.url" class="font-medium">
                {{ item.title }}
              </a>
            </SidebarMenuButton>
            <SidebarMenuSub v-if="item.items.length">
              <SidebarMenuSubItem v-for="childItem in item.items" :key="childItem.title">
                <SidebarMenuSubButton as-child :is-active="childItem.isActive">
                  <a :href="childItem.url">{{ childItem.title }}</a>
                </SidebarMenuSubButton>
              </SidebarMenuSubItem>
            </SidebarMenuSub>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarGroup>
    </SidebarContent>
    <SidebarRail />
  </Sidebar>
</template>
```

---

## Block: sidebar-04

**Description:** Sidebar with collapsible subnavigation, no sidebar header

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-04
```

**File tree:**
```
sidebar-04/
├── page.vue
└── components/
    └── AppSidebar.vue
```

### page.vue
```vue
<script lang="ts">
export const iframeHeight = "800px"
export const description = "A floating sidebar with submenus."
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-04/components/AppSidebar.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/registry/new-york-v4/ui/breadcrumb"
import { Separator } from "@/registry/new-york-v4/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <SidebarProvider :style="{ '--sidebar-width': '19rem' }">
    <AppSidebar />
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator
          orientation="vertical"
          class="mr-2 data-[orientation=vertical]:h-4"
        />
        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem class="hidden md:block">
              <BreadcrumbLink href="#">
                Building Your Application
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem>
              <BreadcrumbPage>Data Fetching</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <div class="grid auto-rows-min gap-4 md:grid-cols-3">
          <div class="bg-muted/50 aspect-video rounded-xl" />
          <div class="bg-muted/50 aspect-video rounded-xl" />
          <div class="bg-muted/50 aspect-video rounded-xl" />
        </div>
        <div class="bg-muted/50 min-h-[100vh] flex-1 rounded-xl md:min-h-min" />
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
```

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"

import { GalleryVerticalEnd } from "@lucide/vue"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
} from "@/registry/new-york-v4/ui/sidebar"

const props = withDefaults(defineProps<SidebarProps>(), {
  variant: "floating",
})

// This is sample data.
const data = {
  navMain: [
    {
      title: "Getting Started",
      url: "#",
      items: [
        { title: "Installation", url: "#" },
        { title: "Project Structure", url: "#" },
      ],
    },
    {
      title: "Building Your Application",
      url: "#",
      items: [
        { title: "Routing", url: "#" },
        { title: "Data Fetching", url: "#", isActive: true },
        { title: "Rendering", url: "#" },
        { title: "Caching", url: "#" },
        { title: "Styling", url: "#" },
        { title: "Optimizing", url: "#" },
        { title: "Configuring", url: "#" },
        { title: "Testing", url: "#" },
        { title: "Authentication", url: "#" },
        { title: "Deploying", url: "#" },
        { title: "Upgrading", url: "#" },
        { title: "Examples", url: "#" },
      ],
    },
    {
      title: "API Reference",
      url: "#",
      items: [
        { title: "Components", url: "#" },
        { title: "File Conventions", url: "#" },
        { title: "Functions", url: "#" },
        { title: "next.config.js Options", url: "#" },
        { title: "CLI", url: "#" },
        { title: "Edge Runtime", url: "#" },
      ],
    },
    {
      title: "Architecture",
      url: "#",
      items: [
        { title: "Accessibility", url: "#" },
        { title: "Fast Refresh", url: "#" },
        { title: "Next.js Compiler", url: "#" },
        { title: "Supported Browsers", url: "#" },
        { title: "Turbopack", url: "#" },
      ],
    },
    {
      title: "Community",
      url: "#",
      items: [
        { title: "Contribution Guide", url: "#" },
      ],
    },
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton size="lg" as-child>
            <a href="#">
              <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                <GalleryVerticalEnd class="size-4" />
              </div>
              <div class="flex flex-col gap-0.5 leading-none">
                <span class="font-medium">Documentation</span>
                <span class="">v1.0.0</span>
              </div>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarHeader>
    <SidebarContent>
      <SidebarGroup>
        <SidebarMenu class="gap-2">
          <SidebarMenuItem v-for="item in data.navMain" :key="item.title">
            <SidebarMenuButton as-child>
              <a :href="item.url" class="font-medium">
                {{ item.title }}
              </a>
            </SidebarMenuButton>
            <SidebarMenuSub v-if="item.items.length" class="ml-0 border-l-0 px-1.5">
              <SidebarMenuSubItem v-for="childItem in item.items" :key="childItem.title">
                <SidebarMenuSubButton as-child :is-active="childItem.isActive">
                  <a :href="childItem.url">{{ childItem.title }}</a>
                </SidebarMenuSubButton>
              </SidebarMenuSubItem>
            </SidebarMenuSub>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarGroup>
    </SidebarContent>
  </Sidebar>
</template>
```
