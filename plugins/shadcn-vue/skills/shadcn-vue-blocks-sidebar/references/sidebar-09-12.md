# Sidebar Blocks 09–12: Vollstaendiger Code

---

## Block: sidebar-09

**Description:** Double sidebar with icon-rail nav and mail preview panel

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-09
```

**File tree:**
```
sidebar-09/
├── page.vue
└── components/
    ├── AppSidebar.vue
    └── NavUser.vue
```

### page.vue
```vue
<script lang="ts">
export const description = "Collapsible nested sidebars."
export const iframeHeight = "800px"
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-09/components/AppSidebar.vue"
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
  <SidebarProvider
    :style="{
      '--sidebar-width': '350px',
    }"
  >
    <AppSidebar />
    <SidebarInset>
      <header class="bg-background sticky top-0 flex shrink-0 items-center gap-2 border-b p-4">
        <SidebarTrigger class="-ml-1" />
        <Separator
          orientation="vertical"
          class="mr-2 data-[orientation=vertical]:h-4"
        />
        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem class="hidden md:block">
              <BreadcrumbLink href="#">
                All Inboxes
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem>
              <BreadcrumbPage>Inbox</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>
      <div class="flex flex-1 flex-col gap-4 p-4">
        <div
          v-for="index in 24"
          :key="index"
          class="aspect-video h-12 w-full rounded-lg bg-muted/50"
        />
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
```

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"
import { ArchiveX, Command, File, Inbox, Send, Trash2 } from "@lucide/vue"
import { h, ref } from "vue"
import NavUser from "@/registry/new-york-v4/blocks/sidebar-09/components/NavUser.vue"
import { Label } from "@/registry/new-york-v4/ui/label"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarHeader,
  SidebarInput,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/registry/new-york-v4/ui/sidebar"
import { Switch } from "@/registry/new-york-v4/ui/switch"

const props = withDefaults(defineProps<SidebarProps>(), {
  collapsible: "icon",
})

// This is sample data
const data = {
  user: {
    name: "shadcn",
    email: "m@example.com",
    avatar: "/avatars/shadcn.jpg",
  },
  navMain: [
    { title: "Inbox", url: "#", icon: Inbox, isActive: true },
    { title: "Drafts", url: "#", icon: File, isActive: false },
    { title: "Sent", url: "#", icon: Send, isActive: false },
    { title: "Junk", url: "#", icon: ArchiveX, isActive: false },
    { title: "Trash", url: "#", icon: Trash2, isActive: false },
  ],
  mails: [
    {
      name: "William Smith",
      email: "williamsmith@example.com",
      subject: "Meeting Tomorrow",
      date: "09:34 AM",
      teaser:
        "Hi team, just a reminder about our meeting tomorrow at 10 AM.\nPlease come prepared with your project updates.",
    },
    {
      name: "Alice Smith",
      email: "alicesmith@example.com",
      subject: "Re: Project Update",
      date: "Yesterday",
      teaser:
        "Thanks for the update. The progress looks great so far.\nLet's schedule a call to discuss the next steps.",
    },
    {
      name: "Bob Johnson",
      email: "bobjohnson@example.com",
      subject: "Weekend Plans",
      date: "2 days ago",
      teaser:
        "Hey everyone! I'm thinking of organizing a team outing this weekend.\nWould you be interested in a hiking trip or a beach day?",
    },
    {
      name: "Emily Davis",
      email: "emilydavis@example.com",
      subject: "Re: Question about Budget",
      date: "2 days ago",
      teaser:
        "I've reviewed the budget numbers you sent over.\nCan we set up a quick call to discuss some potential adjustments?",
    },
    {
      name: "Michael Wilson",
      email: "michaelwilson@example.com",
      subject: "Important Announcement",
      date: "1 week ago",
      teaser:
        "Please join us for an all-hands meeting this Friday at 3 PM.\nWe have some exciting news to share about the company's future.",
    },
    {
      name: "Sarah Brown",
      email: "sarahbrown@example.com",
      subject: "Re: Feedback on Proposal",
      date: "1 week ago",
      teaser:
        "Thank you for sending over the proposal. I've reviewed it and have some thoughts.\nCould we schedule a meeting to discuss my feedback in detail?",
    },
    {
      name: "David Lee",
      email: "davidlee@example.com",
      subject: "New Project Idea",
      date: "1 week ago",
      teaser:
        "I've been brainstorming and came up with an interesting project concept.\nDo you have time this week to discuss its potential impact and feasibility?",
    },
    {
      name: "Olivia Wilson",
      email: "oliviawilson@example.com",
      subject: "Vacation Plans",
      date: "1 week ago",
      teaser:
        "Just a heads up that I'll be taking a two-week vacation next month.\nI'll make sure all my projects are up to date before I leave.",
    },
    {
      name: "James Martin",
      email: "jamesmartin@example.com",
      subject: "Re: Conference Registration",
      date: "1 week ago",
      teaser:
        "I've completed the registration for the upcoming tech conference.\nLet me know if you need any additional information from my end.",
    },
    {
      name: "Sophia White",
      email: "sophiawhite@example.com",
      subject: "Team Dinner",
      date: "1 week ago",
      teaser:
        "To celebrate our recent project success, I'd like to organize a team dinner.\nAre you available next Friday evening? Please let me know your preferences.",
    },
  ],
}

const activeItem = ref(data.navMain[0]!)
const mails = ref(data.mails)
const { setOpen } = useSidebar()
</script>

<template>
  <Sidebar
    class="overflow-hidden *:data-[sidebar=sidebar]:flex-row"
    v-bind="props"
  >
    <!-- This is the first sidebar -->
    <!-- We disable collapsible and adjust width to icon. -->
    <!-- This will make the sidebar appear as icons. -->
    <Sidebar
      collapsible="none"
      class="w-[calc(var(--sidebar-width-icon)+1px)]! border-r"
    >
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton size="lg" as-child class="md:h-8 md:p-0">
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
        <SidebarGroup>
          <SidebarGroupContent class="px-1.5 md:px-0">
            <SidebarMenu>
              <SidebarMenuItem v-for="item in data.navMain" :key="item.title">
                <SidebarMenuButton
                  :tooltip="h('div', { hidden: false }, item.title)"
                  :is-active="activeItem.title === item.title"
                  class="px-2.5 md:px-2"
                  @click="() => {
                    activeItem = item

                    const mail = data.mails.sort(() => Math.random() - 0.5)
                    mails = mail.slice(0, Math.max(5, Math.floor(Math.random() * 10) + 1))
                    setOpen(true)
                  }"
                >
                  <component :is="item.icon" />
                  <span>{{ item.title }}</span>
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter>
        <NavUser :user="data.user" />
      </SidebarFooter>
    </Sidebar>

    <!--  This is the second sidebar -->
    <!--  We disable collapsible and let it fill remaining space -->
    <Sidebar collapsible="none" class="hidden flex-1 md:flex">
      <SidebarHeader class="gap-3.5 border-b p-4">
        <div class="flex w-full items-center justify-between">
          <div class="text-base font-medium text-foreground">
            {{ activeItem.title }}
          </div>
          <Label class="flex items-center gap-2 text-sm">
            <span>Unreads</span>
            <Switch class="shadow-none" />
          </Label>
        </div>
        <SidebarInput placeholder="Type to search..." />
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup class="px-0">
          <SidebarGroupContent>
            <a
              v-for="mail in mails"
              :key="mail.email"
              href="#"
              class="hover:bg-sidebar-accent hover:text-sidebar-accent-foreground flex flex-col items-start gap-2 border-b p-4 text-sm leading-tight whitespace-nowrap last:border-b-0"
            >
              <div class="flex w-full items-center gap-2">
                <span>{{ mail.name }}</span>
                <span class="ml-auto text-xs">{{ mail.date }}</span>
              </div>
              <span class="font-medium">{{ mail.subject }}</span>
              <span class="line-clamp-2 w-[260px] whitespace-break-spaces text-xs">
                {{ mail.teaser }}
              </span>
            </a>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  </Sidebar>
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
            class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground md:h-8 md:p-0"
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
          align="end"
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

---

## Block: sidebar-10

**Description:** Sidebar with popover actions panel, favorites, workspaces, and team switcher

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-10
```

**File tree:**
```
sidebar-10/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── NavActions.vue
    ├── NavFavorites.vue
    ├── NavMain.vue
    ├── NavSecondary.vue
    ├── NavWorkspaces.vue
    └── TeamSwitcher.vue
```

### page.vue
```vue
<script lang="ts">
export const description = "A sidebar in a popover."
export const iframeHeight = "800px"
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-10/components/AppSidebar.vue"
import NavActions from "@/registry/new-york-v4/blocks/sidebar-10/components/NavActions.vue"
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
    <AppSidebar />
    <SidebarInset>
      <header class="flex h-14 shrink-0 items-center gap-2">
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
        <div class="ml-auto px-3">
          <NavActions />
        </div>
      </header>
      <div class="flex flex-1 flex-col gap-4 px-4 py-10">
        <div class="bg-muted/50 mx-auto h-24 w-full max-w-3xl rounded-xl" />
        <div class="bg-muted/50 mx-auto h-full w-full max-w-3xl rounded-xl" />
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
```

### components/AppSidebar.vue
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

import NavFavorites from "@/registry/new-york-v4/blocks/sidebar-10/components/NavFavorites.vue"
import NavMain from "@/registry/new-york-v4/blocks/sidebar-10/components/NavMain.vue"
import NavSecondary from "@/registry/new-york-v4/blocks/sidebar-10/components/NavSecondary.vue"
import NavWorkspaces from "@/registry/new-york-v4/blocks/sidebar-10/components/NavWorkspaces.vue"
import TeamSwitcher from "@/registry/new-york-v4/blocks/sidebar-10/components/TeamSwitcher.vue"
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

### components/NavActions.vue
```vue
<script setup lang="ts">
import {
  ArrowDown,
  ArrowUp,
  Bell,
  Copy,
  CornerUpLeft,
  CornerUpRight,
  FileText,
  GalleryVerticalEnd,
  LineChart,
  Link,
  MoreHorizontal,
  Settings2,
  Star,
  Trash,
  Trash2,
} from "@lucide/vue"

import { ref } from "vue"
import { Button } from "@/registry/new-york-v4/ui/button"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/registry/new-york-v4/ui/popover"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

const data = [
  [
    { label: "Customize Page", icon: Settings2 },
    { label: "Turn into wiki", icon: FileText },
  ],
  [
    { label: "Copy Link", icon: Link },
    { label: "Duplicate", icon: Copy },
    { label: "Move to", icon: CornerUpRight },
    { label: "Move to Trash", icon: Trash2 },
  ],
  [
    { label: "Undo", icon: CornerUpLeft },
    { label: "View analytics", icon: LineChart },
    { label: "Version History", icon: GalleryVerticalEnd },
    { label: "Show delete pages", icon: Trash },
    { label: "Notifications", icon: Bell },
  ],
  [
    { label: "Import", icon: ArrowUp },
    { label: "Export", icon: ArrowDown },
  ],
]

const isOpen = ref(false)
</script>

<template>
  <div class="flex items-center gap-2 text-sm">
    <div class="hidden font-medium text-muted-foreground md:inline-block">
      Edit Oct 08
    </div>
    <Button variant="ghost" size="icon" class="h-7 w-7">
      <Star />
    </Button>
    <Popover v-model:open="isOpen">
      <PopoverTrigger as-child>
        <Button
          variant="ghost"
          size="icon"
          class="h-7 w-7 data-[state=open]:bg-accent"
        >
          <MoreHorizontal />
        </Button>
      </PopoverTrigger>
      <PopoverContent
        class="w-56 overflow-hidden rounded-lg p-0"
        align="end"
      >
        <Sidebar collapsible="none" class="bg-transparent">
          <SidebarContent>
            <SidebarGroup v-for="(group, index) in data" :key="index" class="border-b last:border-none">
              <SidebarGroupContent class="gap-0">
                <SidebarMenu>
                  <SidebarMenuItem v-for="(item, index) in group" :key="index">
                    <SidebarMenuButton>
                      <component :is="item.icon" /> <span>{{ item.label }}</span>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                </SidebarMenu>
              </SidebarGroupContent>
            </SidebarGroup>
          </SidebarContent>
        </Sidebar>
      </PopoverContent>
    </Popover>
  </div>
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

## Block: sidebar-11

**Description:** Sidebar with collapsible file tree and change tracking

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-11
```

**File tree:**
```
sidebar-11/
├── page.vue
└── components/
    ├── AppSidebar.vue
    └── Tree.vue
```

### page.vue
```vue
<script lang="ts">
export const description = "A sidebar with a collapsible file tree."
export const iframeHeight = "800px"
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-11/components/AppSidebar.vue"
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
                components
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem class="hidden md:block">
              <BreadcrumbLink href="#">
                ui
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem>
              <BreadcrumbPage>button.tsx</BreadcrumbPage>
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

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"
import { File } from "@lucide/vue"
import Tree from "@/registry/new-york-v4/blocks/sidebar-11/components/Tree.vue"
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<SidebarProps>()

// This is sample data.
const data = {
  changes: [
    { file: "README.md", state: "M" },
    { file: "api/hello/route.ts", state: "U" },
    { file: "app/layout.tsx", state: "M" },
  ],
  tree: [
    [
      "app",
      [
        "api",
        ["hello", ["route.ts"]],
        "page.tsx",
        "layout.tsx",
        ["blog", ["page.tsx"]],
      ],
    ],
    [
      "components",
      ["ui", "button.tsx", "card.tsx"],
      "header.tsx",
      "footer.tsx",
    ],
    ["lib", ["util.ts"]],
    ["public", "favicon.ico", "vercel.svg"],
    ".eslintrc.json",
    ".gitignore",
    "next.config.js",
    "tailwind.config.js",
    "package.json",
    "README.md",
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarContent>
      <SidebarGroup>
        <SidebarGroupLabel>Changes</SidebarGroupLabel>
        <SidebarGroupContent>
          <SidebarMenu>
            <SidebarMenuItem v-for="(item, index) in data.changes" :key="index">
              <SidebarMenuButton>
                <File />
                {{ item.file }}
              </SidebarMenuButton>
              <SidebarMenuBadge>{{ item.state }}</SidebarMenuBadge>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
      <SidebarGroup>
        <SidebarGroupLabel>Files</SidebarGroupLabel>
        <SidebarGroupContent>
          <SidebarMenu>
            <Tree v-for="(item, index) in data.tree" :key="index" :item="item" />
          </SidebarMenu>
        </SidebarGroupContent>
      </SidebarGroup>
    </SidebarContent>
    <SidebarRail />
  </Sidebar>
</template>
```

### components/Tree.vue
```vue
<script setup lang="ts">
import { ChevronRight, File, Folder } from "@lucide/vue"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/registry/new-york-v4/ui/collapsible"

import {
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<{
  item: string | any[]
}>()

const [name, ...items] = Array.isArray(props.item) ? props.item : [props.item]
</script>

<template>
  <SidebarMenuButton
    v-if="!items.length"
    :is-active="name === 'button.tsx'"
    class="data-[active=true]:bg-transparent"
  >
    <File />
    {{ name }}
  </SidebarMenuButton>

  <SidebarMenuItem v-else>
    <Collapsible
      class="group/collapsible [&[data-state=open]>button>svg:first-child]:rotate-90"
      :default-open="name === 'components' || name === 'ui'"
    >
      <CollapsibleTrigger as-child>
        <SidebarMenuButton>
          <ChevronRight class="transition-transform" />
          <Folder />
          {{ name }}
        </SidebarMenuButton>
      </CollapsibleTrigger>
      <CollapsibleContent>
        <SidebarMenuSub>
          <Tree v-for="(subItem, index) in items" :key="index" :item="subItem" />
        </SidebarMenuSub>
      </CollapsibleContent>
    </Collapsible>
  </SidebarMenuItem>
</template>
```

---

## Block: sidebar-12

**Description:** Sidebar with calendar date picker and collapsible calendar groups

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-12
```

**File tree:**
```
sidebar-12/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── Calendars.vue
    ├── DatePicker.vue
    └── NavUser.vue
```

### page.vue
```vue
<script lang="ts">
export const description = "A sidebar with a calendar."
export const iframeHeight = "800px"
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/sidebar-12/components/AppSidebar.vue"
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
    <AppSidebar />
    <SidebarInset>
      <header class="bg-background sticky top-0 flex h-16 shrink-0 items-center gap-2 border-b px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator
          orientation="vertical"
          class="mr-2 data-[orientation=vertical]:h-4"
        />
        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbPage>October 2024</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>
      <div class="flex flex-1 flex-col gap-4 p-4">
        <div class="grid auto-rows-min gap-4 md:grid-cols-5">
          <div v-for="i in 20" :key="i" class="aspect-square rounded-xl bg-muted/50" />
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
```

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import type { SidebarProps } from "@/registry/new-york-v4/ui/sidebar"

import { Plus } from "@lucide/vue"
import Calendars from "@/registry/new-york-v4/blocks/sidebar-12/components/Calendars.vue"
import DatePicker from "@/registry/new-york-v4/blocks/sidebar-12/components/DatePicker.vue"
import NavUser from "@/registry/new-york-v4/blocks/sidebar-12/components/NavUser.vue"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
  SidebarSeparator,
} from "@/registry/new-york-v4/ui/sidebar"

const props = defineProps<SidebarProps>()
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
  <Sidebar v-bind="props">
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
    <SidebarRail />
  </Sidebar>
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
                    class="group/calendar-item border-sidebar-border text-sidebar-primary-foreground data-[active=true]:border-sidebar-primary data-[active=true]:bg-sidebar-primary flex aspect-square size-4 shrink-0 items-center justify-center rounded-sm border"
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
