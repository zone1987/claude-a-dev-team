# Sidebar Blocks 13–16: Vollstaendiger Code

---

## Block: sidebar-13

**Description:** Sidebar embedded inside a Dialog (settings panel)

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-13
```

**File tree:**
```
sidebar-13/
├── page.vue
└── components/
    └── SettingsDialog.vue
```

### page.vue
```vue
<script lang="ts">
export const description = "A sidebar in a dialog."
export const iframeHeight = "800px"
</script>

<script setup lang="ts">
import SettingsDialog from "@/registry/new-york-v4/blocks/sidebar-13/components/SettingsDialog.vue"
</script>

<template>
  <div class="flex h-svh items-center justify-center">
    <SettingsDialog />
  </div>
</template>
```

### components/SettingsDialog.vue
```vue
<script setup lang="ts">
import {
  Bell,
  Check,
  Globe,
  Home,
  Keyboard,
  Link,
  Lock,
  Menu,
  MessageCircle,
  Paintbrush,
  Settings,
  Video,
} from "@lucide/vue"

import { ref } from "vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/registry/new-york-v4/ui/breadcrumb"
import { Button } from "@/registry/new-york-v4/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogTitle,
  DialogTrigger,
} from "@/registry/new-york-v4/ui/dialog"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarProvider,
} from "@/registry/new-york-v4/ui/sidebar"

const data = {
  nav: [
    { name: "Notifications", icon: Bell },
    { name: "Navigation", icon: Menu },
    { name: "Home", icon: Home },
    { name: "Appearance", icon: Paintbrush },
    { name: "Messages & media", icon: MessageCircle },
    { name: "Language & region", icon: Globe },
    { name: "Accessibility", icon: Keyboard },
    { name: "Mark as read", icon: Check },
    { name: "Audio & video", icon: Video },
    { name: "Connected accounts", icon: Link },
    { name: "Privacy & visibility", icon: Lock },
    { name: "Advanced", icon: Settings },
  ],
}

const open = ref(true)
</script>

<template>
  <Dialog v-model:open="open">
    <DialogTrigger as-child>
      <Button size="sm">
        Open Dialog
      </Button>
    </DialogTrigger>
    <DialogContent class="overflow-hidden p-0 md:max-h-[500px] md:max-w-[700px] lg:max-w-[800px]">
      <DialogTitle class="sr-only">
        Settings
      </DialogTitle>
      <DialogDescription class="sr-only">
        Customize your settings here.
      </DialogDescription>
      <SidebarProvider class="items-start">
        <Sidebar collapsible="none" class="hidden md:flex">
          <SidebarContent>
            <SidebarGroup>
              <SidebarGroupContent>
                <SidebarMenu>
                  <SidebarMenuItem v-for="item in data.nav" :key="item.name">
                    <SidebarMenuButton
                      as-child
                      :is-active="item.name === 'Messages & media'"
                    >
                      <a href="#">
                        <component :is="item.icon" />
                        <span>{{ item.name }}</span>
                      </a>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                </SidebarMenu>
              </SidebarGroupContent>
            </SidebarGroup>
          </SidebarContent>
        </Sidebar>
        <main class="flex h-[480px] flex-1 flex-col overflow-hidden">
          <header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
            <div class="flex items-center gap-2 px-4">
              <Breadcrumb>
                <BreadcrumbList>
                  <BreadcrumbItem class="hidden md:block">
                    <BreadcrumbLink href="#">
                      Settings
                    </BreadcrumbLink>
                  </BreadcrumbItem>
                  <BreadcrumbSeparator class="hidden md:block" />
                  <BreadcrumbItem>
                    <BreadcrumbPage>Messages & media</BreadcrumbPage>
                  </BreadcrumbItem>
                </BreadcrumbList>
              </Breadcrumb>
            </div>
          </header>
          <div class="flex flex-1 flex-col gap-4 overflow-y-auto p-4 pt-0">
            <div
              v-for="i in 10"
              :key="i"
              class="aspect-video max-w-3xl rounded-xl bg-muted/50"
            />
          </div>
        </main>
      </SidebarProvider>
    </DialogContent>
  </Dialog>
</template>
```

---

## Block: sidebar-14

**Description:** Right-side sidebar with Table of Contents navigation

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-14
```

**File tree:**
```
sidebar-14/
├── page.vue
└── components/
    └── AppSidebar.vue
```

### page.vue
```vue
<script lang="ts">
export const iframeHeight = "800px"
export const description = "A sidebar on the right."
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-14/components/AppSidebar.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/registry/new-york-v4/ui/breadcrumb"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <SidebarProvider>
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 border-b px-4">
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
        <SidebarTrigger class="-mr-1 ml-auto rotate-180" />
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
    <AppSidebar side="right" />
  </SidebarProvider>
</template>
```

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type {
  SidebarProps,
} from "@/registry/new-york-v4/ui/sidebar"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
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
    <SidebarContent>
      <SidebarGroup>
        <SidebarGroupLabel>Table of Contents</SidebarGroupLabel>
        <SidebarGroupContent>
          <SidebarMenu>
            <SidebarMenuItem v-for="item in data.navMain" :key="item.title">
              <SidebarMenuButton as-child>
                <a :href="item.url" class="font-medium">
                  {{ item.title }}
                </a>
              </SidebarMenuButton>
              <SidebarMenuSub v-if="item.items.length">
                <SidebarMenuSubItem v-for="subItem in item.items" :key="subItem.title">
                  <SidebarMenuSubButton
                    as-child
                    :is-active="subItem.isActive"
                  >
                    <a :href="subItem.url">{{ subItem.title }}</a>
                  </SidebarMenuSubButton>
                </SidebarMenuSubItem>
              </SidebarMenuSub>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
    </SidebarContent>
    <SidebarRail />
  </Sidebar>
</template>
```

---

## Block: sidebar-15

**Description:** Dual sidebar layout with left nav sidebar and right calendar sidebar

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-15
```

**File tree:**
```
sidebar-15/
├── page.vue
└── components/
    ├── SidebarLeft.vue
    ├── SidebarRight.vue
    ├── NavFavorites.vue
    ├── NavMain.vue
    ├── NavSecondary.vue
    ├── NavWorkspaces.vue
    ├── NavUser.vue
    ├── Calendars.vue
    ├── DatePicker.vue
    └── TeamSwitcher.vue
```

### page.vue
```vue
<script lang="ts">
export const iframeHeight = "800px"
export const description = "A left and right sidebar."
</script>

<script setup lang="ts">
import SidebarLeft from "@/registry/new-york-v4/blocks/sidebar-15/components/SidebarLeft.vue"
import SidebarRight from "@/registry/new-york-v4/blocks/sidebar-15/components/SidebarRight.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbPage,
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
    <SidebarLeft />
    <SidebarInset>
      <header class="sticky top-0 flex h-14 shrink-0 items-center gap-2 bg-background">
        <div class="flex flex-1 items-center gap-2 px-3">
          <SidebarTrigger />
          <Separator
            orientation="vertical"
            class="mr-2 data-[orientation=vertical]:h-4"
          />
          <Breadcrumb>
            <BreadcrumbList>
              <BreadcrumbItem>
                <BreadcrumbPage class="line-clamp-1">
                  Project Management & Task Tracking
                </BreadcrumbPage>
              </BreadcrumbItem>
            </BreadcrumbList>
          </Breadcrumb>
        </div>
      </header>
      <div class="flex flex-1 flex-col gap-4 p-4">
        <div class="mx-auto h-24 w-full max-w-3xl rounded-xl bg-muted/50" />
        <div class="mx-auto h-[100vh] w-full max-w-3xl rounded-xl bg-muted/50" />
      </div>
    </SidebarInset>
    <SidebarRight />
  </SidebarProvider>
</template>
```

### components/SidebarLeft.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"

import {
  AudioWaveform,
  Blocks,
  Calendar,
  Command,
  Home,
  Inbox,
  MessageCircleQuestion,
  Search,
  Settings2,
  Sparkles,
  Trash2,
} from "@lucide/vue"

import NavFavorites from "@/registry/new-york-v4/blocks/sidebar-15/components/NavFavorites.vue"
import NavMain from "@/registry/new-york-v4/blocks/sidebar-15/components/NavMain.vue"
import NavSecondary from "@/registry/new-york-v4/blocks/sidebar-15/components/NavSecondary.vue"
import NavWorkspaces from "@/registry/new-york-v4/blocks/sidebar-15/components/NavWorkspaces.vue"
import TeamSwitcher from "@/registry/new-york-v4/blocks/sidebar-15/components/TeamSwitcher.vue"
import {
  Sidebar,
  SidebarContent,
  SidebarHeader,
  SidebarRail,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<SidebarProps>()

// This is sample data.
const data = {
  teams: [
    { name: "Acme Inc", logo: Command, plan: "Enterprise" },
    { name: "Acme Corp.", logo: AudioWaveform, plan: "Startup" },
    { name: "Evil Corp.", logo: Command, plan: "Free" },
  ],
  navMain: [
    { title: "Search", url: "#", icon: Search },
    { title: "Ask AI", url: "#", icon: Sparkles },
    { title: "Home", url: "#", icon: Home, isActive: true },
    { title: "Inbox", url: "#", icon: Inbox, badge: "10" },
  ],
  navSecondary: [
    { title: "Calendar", url: "#", icon: Calendar },
    { title: "Settings", url: "#", icon: Settings2 },
    { title: "Templates", url: "#", icon: Blocks },
    { title: "Trash", url: "#", icon: Trash2 },
    { title: "Help", url: "#", icon: MessageCircleQuestion },
  ],
  favorites: [
    { name: "Project Management & Task Tracking", url: "#", emoji: "📊" },
    { name: "Family Recipe Collection & Meal Planning", url: "#", emoji: "🍳" },
    { name: "Fitness Tracker & Workout Routines", url: "#", emoji: "💪" },
    { name: "Book Notes & Reading List", url: "#", emoji: "📚" },
    { name: "Sustainable Gardening Tips & Plant Care", url: "#", emoji: "🌱" },
    { name: "Language Learning Progress & Resources", url: "#", emoji: "🗣️" },
    { name: "Home Renovation Ideas & Budget Tracker", url: "#", emoji: "🏠" },
    { name: "Personal Finance & Investment Portfolio", url: "#", emoji: "💰" },
    { name: "Movie & TV Show Watchlist with Reviews", url: "#", emoji: "🎬" },
    { name: "Daily Habit Tracker & Goal Setting", url: "#", emoji: "✅" },
  ],
  workspaces: [
    {
      name: "Personal Life Management",
      emoji: "🏠",
      pages: [
        { name: "Daily Journal & Reflection", url: "#", emoji: "📔" },
        { name: "Health & Wellness Tracker", url: "#", emoji: "🍏" },
        { name: "Personal Growth & Learning Goals", url: "#", emoji: "🌟" },
      ],
    },
    {
      name: "Professional Development",
      emoji: "💼",
      pages: [
        { name: "Career Objectives & Milestones", url: "#", emoji: "🎯" },
        { name: "Skill Acquisition & Training Log", url: "#", emoji: "🧠" },
        { name: "Networking Contacts & Events", url: "#", emoji: "🤝" },
      ],
    },
    {
      name: "Creative Projects",
      emoji: "🎨",
      pages: [
        { name: "Writing Ideas & Story Outlines", url: "#", emoji: "✍️" },
        { name: "Art & Design Portfolio", url: "#", emoji: "🖼️" },
        { name: "Music Composition & Practice Log", url: "#", emoji: "🎵" },
      ],
    },
    {
      name: "Home Management",
      emoji: "🏡",
      pages: [
        { name: "Household Budget & Expense Tracking", url: "#", emoji: "💰" },
        { name: "Home Maintenance Schedule & Tasks", url: "#", emoji: "🔧" },
        { name: "Family Calendar & Event Planning", url: "#", emoji: "📅" },
      ],
    },
    {
      name: "Travel & Adventure",
      emoji: "🧳",
      pages: [
        { name: "Trip Planning & Itineraries", url: "#", emoji: "🗺️" },
        { name: "Travel Bucket List & Inspiration", url: "#", emoji: "🌎" },
        { name: "Travel Journal & Photo Gallery", url: "#", emoji: "📸" },
      ],
    },
  ],
}
</script>

<template>
  <Sidebar class="border-r-0" v-bind="props">
    <SidebarHeader>
      <TeamSwitcher :teams="data.teams" />
      <NavMain :items="data.navMain" />
    </SidebarHeader>
    <SidebarContent>
      <NavFavorites :favorites="data.favorites" />
      <NavWorkspaces :workspaces="data.workspaces" />
      <NavSecondary :items="data.navSecondary" class="mt-auto" />
    </SidebarContent>
    <SidebarRail />
  </Sidebar>
</template>
```

### components/SidebarRight.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"

import { Plus } from "@lucide/vue"
import Calendars from "@/registry/new-york-v4/blocks/sidebar-15/components/Calendars.vue"
import DatePicker from "@/registry/new-york-v4/blocks/sidebar-15/components/DatePicker.vue"
import NavUser from "@/registry/new-york-v4/blocks/sidebar-15/components/NavUser.vue"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarSeparator,
} from "@/registry/new-york-v4/ui/sidebar"

const props = withDefaults(defineProps<SidebarProps>(), {
  collapsible: "none",
})

// This is sample data.
const data = {
  user: {
    name: "shadcn",
    email: "m@example.com",
    avatar: "/avatars/shadcn.jpg",
  },
  calendars: [
    { name: "My Calendars", items: ["Personal", "Work", "Family"] },
    { name: "Favorites", items: ["Holidays", "Birthdays"] },
    { name: "Other", items: ["Travel", "Reminders", "Deadlines"] },
  ],
}
</script>

<template>
  <Sidebar
    class="sticky hidden lg:flex top-0 h-svh border-l"
    v-bind="props"
  >
    <SidebarHeader class="h-16 border-b border-sidebar-border">
      <NavUser :user="data.user" />
    </SidebarHeader>
    <SidebarContent>
      <DatePicker />
      <SidebarSeparator class="mx-0" />
      <Calendars :calendars="data.calendars" />
    </SidebarContent>
    <SidebarFooter>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton>
            <Plus />
            <span>New Calendar</span>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarFooter>
  </Sidebar>
</template>
```

### components/NavFavorites.vue
```vue
<script setup lang="ts">
import {
  ArrowUpRight,
  Link,
  MoreHorizontal,
  StarOff,
  Trash2,
} from "@lucide/vue"

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"
import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/registry/new-york-v4/ui/sidebar"

defineProps<{
  favorites: {
    name: string
    url: string
    emoji: string
  }[]
}>()

const { isMobile } = useSidebar()
</script>

<template>
  <SidebarGroup class="group-data-[collapsible=icon]:hidden">
    <SidebarGroupLabel>Favorites</SidebarGroupLabel>
    <SidebarMenu>
      <SidebarMenuItem v-for="item in favorites" :key="item.name">
        <SidebarMenuButton as-child>
          <a :href="item.url" :title="item.name">
            <span>{{ item.emoji }}</span>
            <span>{{ item.name }}</span>
          </a>
        </SidebarMenuButton>
        <DropdownMenu>
          <DropdownMenuTrigger as-child>
            <SidebarMenuAction show-on-hover>
              <MoreHorizontal />
              <span class="sr-only">More</span>
            </SidebarMenuAction>
          </DropdownMenuTrigger>
          <DropdownMenuContent
            class="w-56 rounded-lg"
            :side="isMobile ? 'bottom' : 'right'"
            :align="isMobile ? 'end' : 'start'"
          >
            <DropdownMenuItem>
              <StarOff class="text-muted-foreground" />
              <span>Remove from Favorites</span>
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>
              <Link class="text-muted-foreground" />
              <span>Copy Link</span>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <ArrowUpRight class="text-muted-foreground" />
              <span>Open in New Tab</span>
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>
              <Trash2 class="text-muted-foreground" />
              <span>Delete</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>

      <SidebarMenuItem>
        <SidebarMenuButton class="text-sidebar-foreground/70">
          <MoreHorizontal />
          <span>More</span>
        </SidebarMenuButton>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarGroup>
</template>
```

### components/NavMain.vue
```vue
<script setup lang="ts">
import type { LucideIcon } from "@lucide/vue"

import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

defineProps<{
  items: {
    title: string
    url: string
    icon: LucideIcon
    isActive?: boolean
  }[]
}>()
</script>

<template>
  <SidebarMenu>
    <SidebarMenuItem v-for="item in items" :key="item.title">
      <SidebarMenuButton as-child :is-active="item.isActive">
        <a :href="item.url">
          <component :is="item.icon" />
          <span>{{ item.title }}</span>
        </a>
      </SidebarMenuButton>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
```

### components/NavSecondary.vue
```vue
<script setup lang="ts">
import type { LucideIcon } from "@lucide/vue"

import type { Component } from "vue"
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

defineProps<{
  items: {
    title: string
    url: string
    icon: LucideIcon
    badge?: Component
  }[]
}>()
</script>

<template>
  <SidebarGroup>
    <SidebarGroupContent>
      <SidebarMenu>
        <SidebarMenuItem v-for="item in items" :key="item.title">
          <SidebarMenuButton as-child>
            <a :href="item.url">
              <component :is="item.icon" />
              <span>{{ item.title }}</span>
            </a>
          </SidebarMenuButton>
          <SidebarMenuBadge v-if="item.badge">
            <component :is="item.badge" />
          </SidebarMenuBadge>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarGroupContent>
  </SidebarGroup>
</template>
```

### components/NavWorkspaces.vue
```vue
<script setup lang="ts">
import { ChevronRight, MoreHorizontal, Plus } from "@lucide/vue"

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/registry/new-york-v4/ui/collapsible"
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
} from "@/registry/new-york-v4/ui/sidebar"

defineProps<{
  workspaces: {
    name: string
    emoji: string
    pages: {
      name: string
      emoji: string
    }[]
  }[]
}>()
</script>

<template>
  <SidebarGroup>
    <SidebarGroupLabel>Workspaces</SidebarGroupLabel>
    <SidebarGroupContent>
      <SidebarMenu>
        <Collapsible v-for="workspace in workspaces" :key="workspace.name">
          <SidebarMenuItem>
            <SidebarMenuButton as-child>
              <a href="#">
                <span>{{ workspace.emoji }}</span>
                <span>{{ workspace.name }}</span>
              </a>
            </SidebarMenuButton>
            <CollapsibleTrigger as-child>
              <SidebarMenuAction
                class="left-2 bg-sidebar-accent text-sidebar-accent-foreground data-[state=open]:rotate-90"
                show-on-hover
              >
                <ChevronRight />
              </SidebarMenuAction>
            </CollapsibleTrigger>
            <SidebarMenuAction show-on-hover>
              <Plus />
            </SidebarMenuAction>
            <CollapsibleContent>
              <SidebarMenuSub>
                <SidebarMenuSubItem v-for="page in workspace.pages" :key="page.name">
                  <SidebarMenuSubButton as-child>
                    <a href="#">
                      <span>{{ page.emoji }}</span>
                      <span>{{ page.name }}</span>
                    </a>
                  </SidebarMenuSubButton>
                </SidebarMenuSubItem>
              </SidebarMenuSub>
            </CollapsibleContent>
          </SidebarMenuItem>
        </Collapsible>

        <SidebarMenuItem>
          <SidebarMenuButton class="text-sidebar-foreground/70">
            <MoreHorizontal />
            <span>More</span>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarGroupContent>
  </SidebarGroup>
</template>
```

### components/NavUser.vue
```vue
<script setup lang="ts">
import {
  BadgeCheck,
  Bell,
  ChevronsUpDown,
  CreditCard,
  LogOut,
  Sparkles,
} from "@lucide/vue"

import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/registry/new-york-v4/ui/avatar"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"
import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<{
  user: {
    name: string
    email: string
    avatar: string
  }
}>()

const { isMobile } = useSidebar()
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
            <Avatar class="h-8 w-8 rounded-lg">
              <AvatarImage :src="user.avatar" :alt="user.name" />
              <AvatarFallback class="rounded-lg">
                CN
              </AvatarFallback>
            </Avatar>
            <div class="grid flex-1 text-left text-sm leading-tight">
              <span class="truncate font-medium">{{ user.name }}</span>
              <span class="truncate text-xs">{{ user.email }}</span>
            </div>
            <ChevronsUpDown class="ml-auto size-4" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent
          class="w-(--reka-dropdown-menu-trigger-width) min-w-56 rounded-lg"
          :side="isMobile ? 'bottom' : 'right'"
          align="start"
          :side-offset="4"
        >
          <DropdownMenuLabel class="p-0 font-normal">
            <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
              <Avatar class="h-8 w-8 rounded-lg">
                <AvatarImage :src="user.avatar" :alt="user.name" />
                <AvatarFallback class="rounded-lg">
                  CN
                </AvatarFallback>
              </Avatar>
              <div class="grid flex-1 text-left text-sm leading-tight">
                <span class="truncate font-medium">{{ user.name }}</span>
                <span class="truncate text-xs">{{ user.email }}</span>
              </div>
            </div>
          </DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <Sparkles />
              Upgrade to Pro
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <BadgeCheck />
              Account
            </DropdownMenuItem>
            <DropdownMenuItem>
              <CreditCard />
              Billing
            </DropdownMenuItem>
            <DropdownMenuItem>
              <Bell />
              Notifications
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem>
            <LogOut />
            Log out
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
```

### components/Calendars.vue
```vue
<script setup lang="ts">
import { Check, ChevronRight } from "@lucide/vue"

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/registry/new-york-v4/ui/collapsible"
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarSeparator,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<{
  calendars: {
    name: string
    items: string[]
  }[]
}>()
</script>

<template>
  <template v-for="(calendar, index) in calendars" :key="calendar.name">
    <SidebarGroup class="py-0">
      <Collapsible
        :default-open="index === 0"
        class="group/collapsible"
      >
        <SidebarGroupLabel
          as-child
          class="group/label w-full text-sm text-sidebar-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
        >
          <CollapsibleTrigger>
            {{ calendar.name }}
            <ChevronRight class="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-90" />
          </CollapsibleTrigger>
        </SidebarGroupLabel>
        <CollapsibleContent>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem v-for="(item, index) in calendar.items" :key="item">
                <SidebarMenuButton>
                  <div
                    :data-active="index < 2"
                    class="group/calendar-item flex aspect-square size-4 shrink-0 items-center justify-center rounded-sm border border-sidebar-border text-sidebar-primary-foreground data-[active=true]:border-sidebar-primary data-[active=true]:bg-sidebar-primary"
                  >
                    <Check class="hidden size-3 group-data-[active=true]/calendar-item:block" />
                  </div>
                  {{ item }}
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </CollapsibleContent>
      </Collapsible>
    </SidebarGroup>
    <SidebarSeparator class="mx-0" />
  </template>
</template>
```

### components/DatePicker.vue
```vue
<script setup lang="ts">
import { Calendar } from "@/registry/new-york-v4/ui/calendar"
import {
  SidebarGroup,
  SidebarGroupContent,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <SidebarGroup class="px-0">
    <SidebarGroupContent>
      <Calendar class="[&_[role=gridcell].bg-accent]:bg-sidebar-primary [&_[role=gridcell].bg-accent]:text-sidebar-primary-foreground [&_[role=gridcell]]:w-[33px]" />
    </SidebarGroupContent>
  </SidebarGroup>
</template>
```

### components/TeamSwitcher.vue
```vue
<script setup lang="ts">
import type { Component } from "vue"

import { ChevronDown, Plus } from "@lucide/vue"
import { ref } from "vue"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"

import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<{
  teams: {
    name: string
    logo: Component
    plan: string
  }[]
}>()

const activeTeam = ref(props.teams[0]!)
</script>

<template>
  <SidebarMenu>
    <SidebarMenuItem>
      <DropdownMenu>
        <DropdownMenuTrigger as-child>
          <SidebarMenuButton class="w-fit px-1.5">
            <div class="flex aspect-square size-5 items-center justify-center rounded-md bg-sidebar-primary text-sidebar-primary-foreground">
              <component :is="activeTeam.logo" class="size-3" />
            </div>
            <span class="truncate font-semibold">{{ activeTeam.name }}</span>
            <ChevronDown class="opacity-50" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent
          class="w-64 rounded-lg"
          align="start"
          side="bottom"
          :side-offset="4"
        >
          <DropdownMenuLabel class="text-xs text-muted-foreground">
            Teams
          </DropdownMenuLabel>

          <DropdownMenuItem
            v-for="(team, index) in teams"
            :key="team.name"
            class="gap-2 p-2"
            @click="activeTeam = team"
          >
            <div class="flex size-6 items-center justify-center rounded-xs border">
              <component :is="team.logo" class="size-4 shrink-0" />
            </div>
            {{ team.name }}
            <DropdownMenuShortcut>⌘{{ index + 1 }}</DropdownMenuShortcut>
          </DropdownMenuItem>

          <DropdownMenuSeparator />
          <DropdownMenuItem class="gap-2 p-2">
            <div class="flex size-6 items-center justify-center rounded-md border bg-background">
              <Plus class="size-4" />
            </div>
            <div class="font-medium text-muted-foreground">
              Add team
            </div>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
```

---

## Block: sidebar-16

**Description:** Sidebar with sticky site header containing search, breadcrumb and sidebar toggle

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-16
```

**File tree:**
```
sidebar-16/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── SiteHeader.vue
    ├── NavMain.vue
    ├── NavProjects.vue
    ├── NavSecondary.vue
    ├── NavUser.vue
    └── SearchForm.vue
```

### page.vue
```vue
<script lang="ts">
export const iframeHeight = "800px"
export const description = "A sidebar with a header and a search form."
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-16/components/AppSidebar.vue"
import SiteHeader from "@/registry/new-york-v4/blocks/sidebar-16/components/SiteHeader.vue"
import {
  SidebarInset,
  SidebarProvider,
} from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <div class="[--header-height:calc(--spacing(14))]">
    <SidebarProvider class="flex flex-col">
      <SiteHeader />
      <div class="flex flex-1">
        <AppSidebar />
        <SidebarInset>
          <div class="flex flex-1 flex-col gap-4 p-4">
            <div class="grid auto-rows-min gap-4 md:grid-cols-3">
              <div class="bg-muted/50 aspect-video rounded-xl" />
              <div class="bg-muted/50 aspect-video rounded-xl" />
              <div class="bg-muted/50 aspect-video rounded-xl" />
            </div>
            <div class="bg-muted/50 min-h-[100vh] flex-1 rounded-xl md:min-h-min" />
          </div>
        </SidebarInset>
      </div>
    </SidebarProvider>
  </div>
</template>
```

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"

import {
  BookOpen,
  Bot,
  Command,
  Frame,
  LifeBuoy,
  Map,
  PieChart,
  Send,
  Settings2,
  SquareTerminal,
} from "@lucide/vue"

import NavMain from "@/registry/new-york-v4/blocks/sidebar-16/components/NavMain.vue"
import NavProjects from "@/registry/new-york-v4/blocks/sidebar-16/components/NavProjects.vue"
import NavSecondary from "@/registry/new-york-v4/blocks/sidebar-16/components/NavSecondary.vue"
import NavUser from "@/registry/new-york-v4/blocks/sidebar-16/components/NavUser.vue"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<SidebarProps>()

const data = {
  user: {
    name: "shadcn",
    email: "m@example.com",
    avatar: "/avatars/shadcn.jpg",
  },
  navMain: [
    {
      title: "Playground",
      url: "#",
      icon: SquareTerminal,
      isActive: true,
      items: [
        { title: "History", url: "#" },
        { title: "Starred", url: "#" },
        { title: "Settings", url: "#" },
      ],
    },
    {
      title: "Models",
      url: "#",
      icon: Bot,
      items: [
        { title: "Genesis", url: "#" },
        { title: "Explorer", url: "#" },
        { title: "Quantum", url: "#" },
      ],
    },
    {
      title: "Documentation",
      url: "#",
      icon: BookOpen,
      items: [
        { title: "Introduction", url: "#" },
        { title: "Get Started", url: "#" },
        { title: "Tutorials", url: "#" },
        { title: "Changelog", url: "#" },
      ],
    },
    {
      title: "Settings",
      url: "#",
      icon: Settings2,
      items: [
        { title: "General", url: "#" },
        { title: "Team", url: "#" },
        { title: "Billing", url: "#" },
        { title: "Limits", url: "#" },
      ],
    },
  ],
  navSecondary: [
    { title: "Support", url: "#", icon: LifeBuoy },
    { title: "Feedback", url: "#", icon: Send },
  ],
  projects: [
    { name: "Design Engineering", url: "#", icon: Frame },
    { name: "Sales & Marketing", url: "#", icon: PieChart },
    { name: "Travel", url: "#", icon: Map },
  ],
}
</script>

<template>
  <Sidebar
    class="top-(--header-height) h-[calc(100svh-var(--header-height))]!"
    v-bind="props"
  >
    <SidebarHeader>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton size="lg" as-child>
            <a href="#">
              <div class="bg-sidebar-primary text-sidebar-primary-foreground flex aspect-square size-8 items-center justify-center rounded-lg">
                <Command class="size-4" />
              </div>
              <div class="grid flex-1 text-left text-sm leading-tight">
                <span class="truncate font-medium">Acme Inc</span>
                <span class="truncate text-xs">Enterprise</span>
              </div>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="data.navMain" />
      <NavProjects :projects="data.projects" />
      <NavSecondary :items="data.navSecondary" class="mt-auto" />
    </SidebarContent>
    <SidebarFooter>
      <NavUser :user="data.user" />
    </SidebarFooter>
  </Sidebar>
</template>
```

### components/SiteHeader.vue
```vue
<script setup lang="ts">
import { SidebarIcon } from "@lucide/vue"

import SearchForm from "@/registry/new-york-v4/blocks/sidebar-16/components/SearchForm.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/registry/new-york-v4/ui/breadcrumb"
import { Button } from "@/registry/new-york-v4/ui/button"
import { Separator } from "@/registry/new-york-v4/ui/separator"
import { useSidebar } from "@/registry/new-york-v4/ui/sidebar"

const { toggleSidebar } = useSidebar()
</script>

<template>
  <header class="bg-background sticky top-0 z-50 flex w-full items-center border-b">
    <div class="flex h-(--header-height) w-full items-center gap-2 px-4">
      <Button
        class="h-8 w-8"
        variant="ghost"
        size="icon"
        @click="toggleSidebar"
      >
        <SidebarIcon />
      </Button>
      <Separator orientation="vertical" class="mr-2 h-4" />
      <Breadcrumb class="hidden sm:block">
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink href="#">
              Building Your Application
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>Data Fetching</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
      <SearchForm class="w-full sm:ml-auto sm:w-auto" />
    </div>
  </header>
</template>
```

### components/NavMain.vue
```vue
<script setup lang="ts">
import type { LucideIcon } from "@lucide/vue"
import { ChevronRight } from "@lucide/vue"

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/registry/new-york-v4/ui/collapsible"

import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
} from "@/registry/new-york-v4/ui/sidebar"

defineProps<{
  items: {
    title: string
    url: string
    icon: LucideIcon
    isActive?: boolean
    items?: {
      title: string
      url: string
    }[]
  }[]
}>()
</script>

<template>
  <SidebarGroup>
    <SidebarGroupLabel>Platform</SidebarGroupLabel>
    <SidebarMenu>
      <Collapsible v-for="item in items" :key="item.title" as-child :default-open="item.isActive">
        <SidebarMenuItem>
          <SidebarMenuButton as-child :tooltip="item.title">
            <a :href="item.url">
              <component :is="item.icon" />
              <span>{{ item.title }}</span>
            </a>
          </SidebarMenuButton>
          <template v-if="item.items?.length">
            <CollapsibleTrigger as-child>
              <SidebarMenuAction class="data-[state=open]:rotate-90">
                <ChevronRight />
                <span class="sr-only">Toggle</span>
              </SidebarMenuAction>
            </CollapsibleTrigger>
            <CollapsibleContent>
              <SidebarMenuSub>
                <SidebarMenuSubItem v-for="subItem in item.items" :key="subItem.title">
                  <SidebarMenuSubButton as-child>
                    <a :href="subItem.url">
                      <span>{{ subItem.title }}</span>
                    </a>
                  </SidebarMenuSubButton>
                </SidebarMenuSubItem>
              </SidebarMenuSub>
            </CollapsibleContent>
          </template>
        </SidebarMenuItem>
      </Collapsible>
    </SidebarMenu>
  </SidebarGroup>
</template>
```

### components/NavProjects.vue
```vue
<script setup lang="ts">
import type { LucideIcon } from "@lucide/vue"
import {
  Folder,
  MoreHorizontal,
  Share,
  Trash2,
} from "@lucide/vue"

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"
import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/registry/new-york-v4/ui/sidebar"

defineProps<{
  projects: {
    name: string
    url: string
    icon: LucideIcon
  }[]
}>()

const { isMobile } = useSidebar()
</script>

<template>
  <SidebarGroup class="group-data-[collapsible=icon]:hidden">
    <SidebarGroupLabel>Projects</SidebarGroupLabel>
    <SidebarMenu>
      <SidebarMenuItem v-for="item in projects" :key="item.name">
        <SidebarMenuButton as-child>
          <a :href="item.url">
            <component :is="item.icon" />
            <span>{{ item.name }}</span>
          </a>
        </SidebarMenuButton>
        <DropdownMenu>
          <DropdownMenuTrigger as-child>
            <SidebarMenuAction show-on-hover>
              <MoreHorizontal />
              <span class="sr-only">More</span>
            </SidebarMenuAction>
          </DropdownMenuTrigger>
          <DropdownMenuContent
            class="w-48"
            :side="isMobile ? 'bottom' : 'right'"
            :align="isMobile ? 'end' : 'start'"
          >
            <DropdownMenuItem>
              <Folder class="text-muted-foreground" />
              <span>View Project</span>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <Share class="text-muted-foreground" />
              <span>Share Project</span>
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>
              <Trash2 class="text-muted-foreground" />
              <span>Delete Project</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
      <SidebarMenuItem>
        <SidebarMenuButton>
          <MoreHorizontal />
          <span>More</span>
        </SidebarMenuButton>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarGroup>
</template>
```

### components/NavSecondary.vue
```vue
<script setup lang="ts">
import type { LucideIcon } from "@lucide/vue"

import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<{
  items: {
    title: string
    url: string
    icon: LucideIcon
  }[]
}>()
</script>

<template>
  <SidebarGroup v-bind="props">
    <SidebarGroupContent>
      <SidebarMenu>
        <SidebarMenuItem v-for="item in items" :key="item.title">
          <SidebarMenuButton as-child size="sm">
            <a :href="item.url">
              <component :is="item.icon" />
              <span>{{ item.title }}</span>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarGroupContent>
  </SidebarGroup>
</template>
```

### components/NavUser.vue
```vue
<script setup lang="ts">
import {
  BadgeCheck,
  Bell,
  ChevronsUpDown,
  CreditCard,
  LogOut,
  Sparkles,
} from "@lucide/vue"

import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/registry/new-york-v4/ui/avatar"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"
import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<{
  user: {
    name: string
    email: string
    avatar: string
  }
}>()

const { isMobile } = useSidebar()
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
            <Avatar class="h-8 w-8 rounded-lg">
              <AvatarImage :src="user.avatar" :alt="user.name" />
              <AvatarFallback class="rounded-lg">
                CN
              </AvatarFallback>
            </Avatar>
            <div class="grid flex-1 text-left text-sm leading-tight">
              <span class="truncate font-medium">{{ user.name }}</span>
              <span class="truncate text-xs">{{ user.email }}</span>
            </div>
            <ChevronsUpDown class="ml-auto size-4" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent
          class="w-(--reka-dropdown-menu-trigger-width) min-w-56 rounded-lg"
          :side="isMobile ? 'bottom' : 'right'"
          align="start"
          :side-offset="4"
        >
          <DropdownMenuLabel class="p-0 font-normal">
            <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
              <Avatar class="h-8 w-8 rounded-lg">
                <AvatarImage :src="user.avatar" :alt="user.name" />
                <AvatarFallback class="rounded-lg">
                  CN
                </AvatarFallback>
              </Avatar>
              <div class="grid flex-1 text-left text-sm leading-tight">
                <span class="truncate font-medium">{{ user.name }}</span>
                <span class="truncate text-xs">{{ user.email }}</span>
              </div>
            </div>
          </DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <Sparkles />
              Upgrade to Pro
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <BadgeCheck />
              Account
            </DropdownMenuItem>
            <DropdownMenuItem>
              <CreditCard />
              Billing
            </DropdownMenuItem>
            <DropdownMenuItem>
              <Bell />
              Notifications
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem>
            <LogOut />
            Log out
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
```

### components/SearchForm.vue
```vue
<script setup lang="ts">
import { Search } from "@lucide/vue"

import { Label } from "@/registry/new-york-v4/ui/label"
import { SidebarInput } from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <form>
    <div class="relative">
      <Label for="search" class="sr-only">
        Search
      </Label>
      <SidebarInput
        id="search"
        placeholder="Type to search..."
        class="h-8 pl-7"
      />
      <Search class="pointer-events-none absolute top-1/2 left-2 size-4 -translate-y-1/2 opacity-50 select-none" />
    </div>
  </form>
</template>
```
