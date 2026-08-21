## Block: dashboard-01

**Installation:**
```bash
npx shadcn-vue@latest add dashboard-01
```

**File tree:**
```
dashboard-01/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── ChartAreaInteractive.vue
    ├── DataTable.vue
    ├── DraggableRow.vue
    ├── DragHandle.vue
    ├── NavDocuments.vue
    ├── NavMain.vue
    ├── NavSecondary.vue
    ├── NavUser.vue
    ├── SectionCards.vue
    └── SiteHeader.vue
```

---

### page.vue
```vue
<script lang="ts">
export const iframeHeight = "800px"
export const description = "A dashboard with sidebar, data table, and analytics cards."
</script>

<script setup lang="ts">
import AppSidebar from "@/registry/new-york-v4/blocks/dashboard-01/components/AppSidebar.vue"
import ChartAreaInteractive from "@/registry/new-york-v4/blocks/dashboard-01/components/ChartAreaInteractive.vue"
import DataTable from "@/registry/new-york-v4/blocks/dashboard-01/components/DataTable.vue"
import SectionCards from "@/registry/new-york-v4/blocks/dashboard-01/components/SectionCards.vue"
import SiteHeader from "@/registry/new-york-v4/blocks/dashboard-01/components/SiteHeader.vue"
import {
  SidebarInset,
  SidebarProvider,
} from "@/registry/new-york-v4/ui/sidebar"

const data = [
  {
    id: 1,
    header: "Cover page",
    type: "Cover page",
    status: "In Process",
    target: "18",
    limit: "5",
    reviewer: "Eddie Lake",
  },
  {
    id: 2,
    header: "Table of contents",
    type: "Table of contents",
    status: "Done",
    target: "29",
    limit: "24",
    reviewer: "Eddie Lake",
  },
  {
    id: 3,
    header: "Executive summary",
    type: "Narrative",
    status: "Done",
    target: "10",
    limit: "13",
    reviewer: "Eddie Lake",
  },
  {
    id: 4,
    header: "Technical approach",
    type: "Narrative",
    status: "Done",
    target: "27",
    limit: "23",
    reviewer: "Jamik Tashpulatov",
  },
  {
    id: 5,
    header: "Design",
    type: "Narrative",
    status: "In Process",
    target: "2",
    limit: "16",
    reviewer: "Jamik Tashpulatov",
  },
  {
    id: 6,
    header: "Capabilities",
    type: "Narrative",
    status: "In Process",
    target: "20",
    limit: "8",
    reviewer: "Jamik Tashpulatov",
  },
  {
    id: 7,
    header: "Integration with existing systems",
    type: "Narrative",
    status: "In Process",
    target: "19",
    limit: "21",
    reviewer: "Jamik Tashpulatov",
  },
  {
    id: 8,
    header: "Innovation and Advantages",
    type: "Narrative",
    status: "Done",
    target: "25",
    limit: "26",
    reviewer: "Assign reviewer",
  },
  {
    id: 9,
    header: "Overview of EMR's Innovative Solutions",
    type: "Technical content",
    status: "Done",
    target: "7",
    limit: "23",
    reviewer: "Assign reviewer",
  },
  {
    id: 10,
    header: "Advanced Algorithms and Machine Learning",
    type: "Narrative",
    status: "Done",
    target: "30",
    limit: "28",
    reviewer: "Assign reviewer",
  },
  {
    id: 11,
    header: "Adaptive Communication Protocols",
    type: "Narrative",
    status: "Done",
    target: "9",
    limit: "31",
    reviewer: "Assign reviewer",
  },
  {
    id: 12,
    header: "Advantages Over Current Technologies",
    type: "Narrative",
    status: "Done",
    target: "12",
    limit: "0",
    reviewer: "Assign reviewer",
  },
  {
    id: 13,
    header: "Past Performance",
    type: "Narrative",
    status: "Done",
    target: "22",
    limit: "33",
    reviewer: "Assign reviewer",
  },
  {
    id: 14,
    header: "Customer Feedback and Satisfaction Levels",
    type: "Narrative",
    status: "Done",
    target: "15",
    limit: "34",
    reviewer: "Assign reviewer",
  },
  {
    id: 15,
    header: "Implementation Challenges and Solutions",
    type: "Narrative",
    status: "Done",
    target: "3",
    limit: "35",
    reviewer: "Assign reviewer",
  },
  {
    id: 16,
    header: "Security Measures and Data Protection Policies",
    type: "Narrative",
    status: "In Process",
    target: "6",
    limit: "36",
    reviewer: "Assign reviewer",
  },
  {
    id: 17,
    header: "Scalability and Future Proofing",
    type: "Narrative",
    status: "Done",
    target: "4",
    limit: "37",
    reviewer: "Assign reviewer",
  },
  {
    id: 18,
    header: "Cost-Benefit Analysis",
    type: "Plain language",
    status: "Done",
    target: "14",
    limit: "38",
    reviewer: "Assign reviewer",
  },
  {
    id: 19,
    header: "User Training and Onboarding Experience",
    type: "Narrative",
    status: "Done",
    target: "17",
    limit: "39",
    reviewer: "Assign reviewer",
  },
  {
    id: 20,
    header: "Future Development Roadmap",
    type: "Narrative",
    status: "Done",
    target: "11",
    limit: "40",
    reviewer: "Assign reviewer",
  },
  {
    id: 21,
    header: "System Architecture Overview",
    type: "Technical content",
    status: "In Process",
    target: "24",
    limit: "18",
    reviewer: "Maya Johnson",
  },
  {
    id: 22,
    header: "Risk Management Plan",
    type: "Narrative",
    status: "Done",
    target: "15",
    limit: "22",
    reviewer: "Carlos Rodriguez",
  },
  {
    id: 23,
    header: "Compliance Documentation",
    type: "Legal",
    status: "In Process",
    target: "31",
    limit: "27",
    reviewer: "Sarah Chen",
  },
  {
    id: 24,
    header: "API Documentation",
    type: "Technical content",
    status: "Done",
    target: "8",
    limit: "12",
    reviewer: "Raj Patel",
  },
  {
    id: 25,
    header: "User Interface Mockups",
    type: "Visual",
    status: "In Process",
    target: "19",
    limit: "25",
    reviewer: "Leila Ahmadi",
  },
  {
    id: 26,
    header: "Database Schema",
    type: "Technical content",
    status: "Done",
    target: "22",
    limit: "20",
    reviewer: "Thomas Wilson",
  },
  {
    id: 27,
    header: "Testing Methodology",
    type: "Technical content",
    status: "In Process",
    target: "17",
    limit: "14",
    reviewer: "Assign reviewer",
  },
  {
    id: 28,
    header: "Deployment Strategy",
    type: "Narrative",
    status: "Done",
    target: "26",
    limit: "30",
    reviewer: "Eddie Lake",
  },
  {
    id: 29,
    header: "Budget Breakdown",
    type: "Financial",
    status: "In Process",
    target: "13",
    limit: "16",
    reviewer: "Jamik Tashpulatov",
  },
  {
    id: 30,
    header: "Market Analysis",
    type: "Research",
    status: "Done",
    target: "29",
    limit: "32",
    reviewer: "Sophia Martinez",
  },
]
</script>

<template>
  <SidebarProvider
    :style=" {
      '--sidebar-width': 'calc(var(--spacing) * 72)',
      '--header-height': 'calc(var(--spacing) * 12)',
    }"
  >
    <AppSidebar variant="inset" />
    <SidebarInset>
      <SiteHeader />
      <div class="flex flex-1 flex-col">
        <div class="@container/main flex flex-1 flex-col gap-2">
          <div class="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
            <SectionCards />
            <div class="px-4 lg:px-6">
              <ChartAreaInteractive />
            </div>
            <DataTable :data="data" />
          </div>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
```

---

### components/AppSidebar.vue
```vue
<script setup lang="ts">
import {
  IconCamera,
  IconChartBar,
  IconDashboard,
  IconDatabase,
  IconFileAi,
  IconFileDescription,
  IconFolder,
  IconHelp,
  IconInnerShadowTop,
  IconListDetails,
  IconReport,
  IconSearch,
  IconSettings,
  IconUsers,
} from "@tabler/icons-vue"

import NavDocuments from "@/registry/new-york-v4/blocks/dashboard-01/components/NavDocuments.vue"
import NavMain from "@/registry/new-york-v4/blocks/dashboard-01/components/NavMain.vue"
import NavSecondary from "@/registry/new-york-v4/blocks/dashboard-01/components/NavSecondary.vue"
import NavUser from "@/registry/new-york-v4/blocks/dashboard-01/components/NavUser.vue"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

const data = {
  user: {
    name: "shadcn",
    email: "m@example.com",
    avatar: "/avatars/shadcn.jpg",
  },
  navMain: [
    {
      title: "Dashboard",
      url: "#",
      icon: IconDashboard,
    },
    {
      title: "Lifecycle",
      url: "#",
      icon: IconListDetails,
    },
    {
      title: "Analytics",
      url: "#",
      icon: IconChartBar,
    },
    {
      title: "Projects",
      url: "#",
      icon: IconFolder,
    },
    {
      title: "Team",
      url: "#",
      icon: IconUsers,
    },
  ],
  navClouds: [
    {
      title: "Capture",
      icon: IconCamera,
      isActive: true,
      url: "#",
      items: [
        {
          title: "Active Proposals",
          url: "#",
        },
        {
          title: "Archived",
          url: "#",
        },
      ],
    },
    {
      title: "Proposal",
      icon: IconFileDescription,
      url: "#",
      items: [
        {
          title: "Active Proposals",
          url: "#",
        },
        {
          title: "Archived",
          url: "#",
        },
      ],
    },
    {
      title: "Prompts",
      icon: IconFileAi,
      url: "#",
      items: [
        {
          title: "Active Proposals",
          url: "#",
        },
        {
          title: "Archived",
          url: "#",
        },
      ],
    },
  ],
  navSecondary: [
    {
      title: "Settings",
      url: "#",
      icon: IconSettings,
    },
    {
      title: "Get Help",
      url: "#",
      icon: IconHelp,
    },
    {
      title: "Search",
      url: "#",
      icon: IconSearch,
    },
  ],
  documents: [
    {
      name: "Data Library",
      url: "#",
      icon: IconDatabase,
    },
    {
      name: "Reports",
      url: "#",
      icon: IconReport,
    },
    {
      name: "Word Assistant",
      url: "#",
      icon: IconFileDescription,
    },
  ],
}
</script>

<template>
  <Sidebar collapsible="offcanvas">
    <SidebarHeader>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton
            as-child
            class="data-[slot=sidebar-menu-button]:!p-1.5"
          >
            <a href="#">
              <IconInnerShadowTop class="!size-5" />
              <span class="text-base font-semibold">Acme Inc.</span>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="data.navMain" />
      <NavDocuments :items="data.documents" />
      <NavSecondary :items="data.navSecondary" class="mt-auto" />
    </SidebarContent>
    <SidebarFooter>
      <NavUser :user="data.user" />
    </SidebarFooter>
  </Sidebar>
</template>
```

---

### components/ChartAreaInteractive.vue
```vue
<script setup lang="ts">
import type { ChartConfig } from "@/registry/new-york-v4/ui/chart"

// import { Area, AreaChart, CartesianGrid, XAxis, YAxis } from "recharts"
import { VisArea, VisAxis, VisLine, VisXYContainer } from "@unovis/vue"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/registry/new-york-v4/ui/card"
import {
  ChartContainer,
  ChartCrosshair,
  ChartLegendContent,
  ChartTooltip,
  ChartTooltipContent,
  componentToString,
} from "@/registry/new-york-v4/ui/chart"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/registry/new-york-v4/ui/select"

const description = "An interactive area chart"

const chartData = [
  { date: new Date("2024-04-01"), desktop: 222, mobile: 150 },
  { date: new Date("2024-04-02"), desktop: 97, mobile: 180 },
  { date: new Date("2024-04-03"), desktop: 167, mobile: 120 },
  { date: new Date("2024-04-04"), desktop: 242, mobile: 260 },
  { date: new Date("2024-04-05"), desktop: 373, mobile: 290 },
  { date: new Date("2024-04-06"), desktop: 301, mobile: 340 },
  { date: new Date("2024-04-07"), desktop: 245, mobile: 180 },
  { date: new Date("2024-04-08"), desktop: 409, mobile: 320 },
  { date: new Date("2024-04-09"), desktop: 59, mobile: 110 },
  { date: new Date("2024-04-10"), desktop: 261, mobile: 190 },
  { date: new Date("2024-04-11"), desktop: 327, mobile: 350 },
  { date: new Date("2024-04-12"), desktop: 292, mobile: 210 },
  { date: new Date("2024-04-13"), desktop: 342, mobile: 380 },
  { date: new Date("2024-04-14"), desktop: 137, mobile: 220 },
  { date: new Date("2024-04-15"), desktop: 120, mobile: 170 },
  { date: new Date("2024-04-16"), desktop: 138, mobile: 190 },
  { date: new Date("2024-04-17"), desktop: 446, mobile: 360 },
  { date: new Date("2024-04-18"), desktop: 364, mobile: 410 },
  { date: new Date("2024-04-19"), desktop: 243, mobile: 180 },
  { date: new Date("2024-04-20"), desktop: 89, mobile: 150 },
  { date: new Date("2024-04-21"), desktop: 137, mobile: 200 },
  { date: new Date("2024-04-22"), desktop: 224, mobile: 170 },
  { date: new Date("2024-04-23"), desktop: 138, mobile: 230 },
  { date: new Date("2024-04-24"), desktop: 387, mobile: 290 },
  { date: new Date("2024-04-25"), desktop: 215, mobile: 250 },
  { date: new Date("2024-04-26"), desktop: 75, mobile: 130 },
  { date: new Date("2024-04-27"), desktop: 383, mobile: 420 },
  { date: new Date("2024-04-28"), desktop: 122, mobile: 180 },
  { date: new Date("2024-04-29"), desktop: 315, mobile: 240 },
  { date: new Date("2024-04-30"), desktop: 454, mobile: 380 },
  { date: new Date("2024-05-01"), desktop: 165, mobile: 220 },
  { date: new Date("2024-05-02"), desktop: 293, mobile: 310 },
  { date: new Date("2024-05-03"), desktop: 247, mobile: 190 },
  { date: new Date("2024-05-04"), desktop: 385, mobile: 420 },
  { date: new Date("2024-05-05"), desktop: 481, mobile: 390 },
  { date: new Date("2024-05-06"), desktop: 498, mobile: 520 },
  { date: new Date("2024-05-07"), desktop: 388, mobile: 300 },
  { date: new Date("2024-05-08"), desktop: 149, mobile: 210 },
  { date: new Date("2024-05-09"), desktop: 227, mobile: 180 },
  { date: new Date("2024-05-10"), desktop: 293, mobile: 330 },
  { date: new Date("2024-05-11"), desktop: 335, mobile: 270 },
  { date: new Date("2024-05-12"), desktop: 197, mobile: 240 },
  { date: new Date("2024-05-13"), desktop: 197, mobile: 160 },
  { date: new Date("2024-05-14"), desktop: 448, mobile: 490 },
  { date: new Date("2024-05-15"), desktop: 473, mobile: 380 },
  { date: new Date("2024-05-16"), desktop: 338, mobile: 400 },
  { date: new Date("2024-05-17"), desktop: 499, mobile: 420 },
  { date: new Date("2024-05-18"), desktop: 315, mobile: 350 },
  { date: new Date("2024-05-19"), desktop: 235, mobile: 180 },
  { date: new Date("2024-05-20"), desktop: 177, mobile: 230 },
  { date: new Date("2024-05-21"), desktop: 82, mobile: 140 },
  { date: new Date("2024-05-22"), desktop: 81, mobile: 120 },
  { date: new Date("2024-05-23"), desktop: 252, mobile: 290 },
  { date: new Date("2024-05-24"), desktop: 294, mobile: 220 },
  { date: new Date("2024-05-25"), desktop: 201, mobile: 250 },
  { date: new Date("2024-05-26"), desktop: 213, mobile: 170 },
  { date: new Date("2024-05-27"), desktop: 420, mobile: 460 },
  { date: new Date("2024-05-28"), desktop: 233, mobile: 190 },
  { date: new Date("2024-05-29"), desktop: 78, mobile: 130 },
  { date: new Date("2024-05-30"), desktop: 340, mobile: 280 },
  { date: new Date("2024-05-31"), desktop: 178, mobile: 230 },
  { date: new Date("2024-06-01"), desktop: 178, mobile: 200 },
  { date: new Date("2024-06-02"), desktop: 470, mobile: 410 },
  { date: new Date("2024-06-03"), desktop: 103, mobile: 160 },
  { date: new Date("2024-06-04"), desktop: 439, mobile: 380 },
  { date: new Date("2024-06-05"), desktop: 88, mobile: 140 },
  { date: new Date("2024-06-06"), desktop: 294, mobile: 250 },
  { date: new Date("2024-06-07"), desktop: 323, mobile: 370 },
  { date: new Date("2024-06-08"), desktop: 385, mobile: 320 },
  { date: new Date("2024-06-09"), desktop: 438, mobile: 480 },
  { date: new Date("2024-06-10"), desktop: 155, mobile: 200 },
  { date: new Date("2024-06-11"), desktop: 92, mobile: 150 },
  { date: new Date("2024-06-12"), desktop: 492, mobile: 420 },
  { date: new Date("2024-06-13"), desktop: 81, mobile: 130 },
  { date: new Date("2024-06-14"), desktop: 426, mobile: 380 },
  { date: new Date("2024-06-15"), desktop: 307, mobile: 350 },
  { date: new Date("2024-06-16"), desktop: 371, mobile: 310 },
  { date: new Date("2024-06-17"), desktop: 475, mobile: 520 },
  { date: new Date("2024-06-18"), desktop: 107, mobile: 170 },
  { date: new Date("2024-06-19"), desktop: 341, mobile: 290 },
  { date: new Date("2024-06-20"), desktop: 408, mobile: 450 },
  { date: new Date("2024-06-21"), desktop: 169, mobile: 210 },
  { date: new Date("2024-06-22"), desktop: 317, mobile: 270 },
  { date: new Date("2024-06-23"), desktop: 480, mobile: 530 },
  { date: new Date("2024-06-24"), desktop: 132, mobile: 180 },
  { date: new Date("2024-06-25"), desktop: 141, mobile: 190 },
  { date: new Date("2024-06-26"), desktop: 434, mobile: 380 },
  { date: new Date("2024-06-27"), desktop: 448, mobile: 490 },
  { date: new Date("2024-06-28"), desktop: 149, mobile: 200 },
  { date: new Date("2024-06-29"), desktop: 103, mobile: 160 },
  { date: new Date("2024-06-30"), desktop: 446, mobile: 400 },
]
type Data = typeof chartData[number]

const chartConfig = {
  // visitors: {
  //   label: 'Visitors',
  // },
  mobile: {
    label: "Mobile",
    color: "var(--primary)",
  },
  desktop: {
    label: "Desktop",
    color: "var(--primary)",
  },
} satisfies ChartConfig

const svgDefs = `
  <linearGradient id="fillDesktop" x1="0" y1="0" x2="0" y2="1">
    <stop
      offset="5%"
      stop-color="var(--color-desktop)"
      stop-opacity="0.8"
    />
    <stop
      offset="95%"
      stop-color="var(--color-desktop)"
      stop-opacity="0.1"
    />
  </linearGradient>
  <linearGradient id="fillMobile" x1="0" y1="0" x2="0" y2="1">
    <stop
      offset="5%"
      stop-color="var(--color-mobile)"
      stop-opacity="0.8"
    />
    <stop
      offset="95%"
      stop-color="var(--color-mobile)"
      stop-opacity="0.1"
    />
  </linearGradient>
`

const timeRange = ref("90d")
const filterRange = computed(() => {
  return chartData.filter((item) => {
    const date = new Date(item.date)
    const referenceDate = new Date("2024-06-30")
    let daysToSubtract = 90
    if (timeRange.value === "30d") {
      daysToSubtract = 30
    }
    else if (timeRange.value === "7d") {
      daysToSubtract = 7
    }
    const startDate = new Date(referenceDate)
    startDate.setDate(startDate.getDate() - daysToSubtract)
    return date >= startDate
  })
})
</script>

<template>
  <Card class="pt-0">
    <CardHeader class="flex items-center gap-2 space-y-0 border-b py-5 sm:flex-row">
      <div class="grid flex-1 gap-1">
        <CardTitle>Area Chart - Interactive</CardTitle>
        <CardDescription>
          Showing total visitors for the last 3 months
        </CardDescription>
      </div>
      <Select v-model="timeRange">
        <SelectTrigger
          class="hidden w-[160px] rounded-lg sm:ml-auto sm:flex"
          aria-label="Select a value"
        >
          <SelectValue placeholder="Last 3 months" />
        </SelectTrigger>
        <SelectContent class="rounded-xl">
          <SelectItem value="90d" class="rounded-lg">
            Last 3 months
          </SelectItem>
          <SelectItem value="30d" class="rounded-lg">
            Last 30 days
          </SelectItem>
          <SelectItem value="7d" class="rounded-lg">
            Last 7 days
          </SelectItem>
        </SelectContent>
      </Select>
    </CardHeader>
    <CardContent class="px-2 pt-4 sm:px-6 sm:pt-6 pb-4">
      <ChartContainer :config="chartConfig" class="aspect-auto h-[250px] w-full" :cursor="false">
        <VisXYContainer
          :data="filterRange"
          :svg-defs="svgDefs"
          :margin="{ left: -40 }"
          :y-domain="[0, 1200]"
        >
          <VisArea
            :x="(d: Data) => d.date"
            :y="[(d: Data) => d.mobile, (d: Data) => d.desktop]"
            :color="(d: Data, i: number) => ['url(#fillMobile)', 'url(#fillDesktop)'][i]"
            :opacity="0.6"
          />
          <VisLine
            :x="(d: Data) => d.date"
            :y="[(d: Data) => d.mobile, (d: Data) => d.mobile + d.desktop]"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i]"
            :line-width="1"
          />
          <VisAxis
            type="x"
            :x="(d: Data) => d.date"
            :tick-line="false"
            :domain-line="false"
            :grid-line="false"
            :num-ticks="6"
            :tick-format="(d: number, index: number) => {
              const date = new Date(d)
              return date.toLocaleDateString('en-US', {
                month: 'short',
                day: 'numeric',
              })
            }"
          />
          <VisAxis
            type="y"
            :num-ticks="3"
            :tick-line="false"
            :domain-line="false"
          />
          <ChartTooltip />
          <ChartCrosshair
            :template="componentToString(chartConfig, ChartTooltipContent, {
              labelFormatter: (d) => {
                return new Date(d).toLocaleDateString('en-US', {
                  month: 'short',
                  day: 'numeric',
                })
              },
            })"
            :color="(d: Data, i: number) => [chartConfig.mobile.color, chartConfig.desktop.color][i % 2]"
          />
        </VisXYContainer>

        <ChartLegendContent />
      </ChartContainer>
    </CardContent>
  </Card>
</template>
```

---

### components/DataTable.vue
```vue
<script lang="ts">
import { z } from "zod"
import DraggableRow from "./DraggableRow.vue"
import DragHandle from "./DragHandle.vue"

export const schema = z.object({
  id: z.number(),
  header: z.string(),
  type: z.string(),
  status: z.string(),
  target: z.string(),
  limit: z.string(),
  reviewer: z.string(),
})
</script>

<script setup lang="ts">
import type {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
} from "@tanstack/vue-table"
import { RestrictToVerticalAxis } from "@dnd-kit/abstract/modifiers"
import {
  IconChevronDown,
  IconChevronLeft,
  IconChevronRight,
  IconChevronsLeft,
  IconChevronsRight,
  IconCircleCheckFilled,
  IconDotsVertical,
  IconLayoutColumns,
  IconLoader,
  IconPlus,
} from "@tabler/icons-vue"
import {
  FlexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useVueTable,
} from "@tanstack/vue-table"
import { DragDropProvider } from "dnd-kit-vue"
import { Badge } from "@/registry/new-york-v4/ui/badge"

import { Button } from "@/registry/new-york-v4/ui/button"
import { Checkbox } from "@/registry/new-york-v4/ui/checkbox"
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"

import { Label } from "@/registry/new-york-v4/ui/label"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/registry/new-york-v4/ui/select"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/registry/new-york-v4/ui/table"

import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/registry/new-york-v4/ui/tabs"

const props = defineProps<{
  data: TableData[]
}>()

interface TableData {
  id: number
  header: string
  type: string
  status: string
  target: string
  limit: string
  reviewer: string
}

const sorting = ref<SortingState>([])
const columnFilters = ref<ColumnFiltersState>([])
const columnVisibility = ref<VisibilityState>({})
const rowSelection = ref({})

const columns: ColumnDef<TableData>[] = [
  {
    id: "drag",
    header: () => null,
    cell: ({ row }) => h(DragHandle),
  },
  {
    id: "select",
    header: ({ table }) => h(Checkbox, {
      "modelValue": table.getIsAllPageRowsSelected() || (table.getIsSomePageRowsSelected() && "indeterminate"),
      "onUpdate:modelValue": value => table.toggleAllPageRowsSelected(!!value),
      "aria-label": "Select all",
    }),
    cell: ({ row }) => h(Checkbox, {
      "modelValue": row.getIsSelected(),
      "onUpdate:modelValue": value => row.toggleSelected(!!value),
      "aria-label": "Select row",
    }),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: "header",
    header: "Header",
    cell: ({ row }) => h("div", String(row.getValue("header"))),
    enableHiding: false,
  },
  {
    accessorKey: "type",
    header: "Section Type",
    cell: ({ row }) => h(Badge, {
      variant: "outline",
    }, () => String(row.getValue("type"))),
  },
  {
    accessorKey: "status",
    header: "Status",
    cell: ({ row }) => {
      const status = row.getValue("status") as string
      return h("div", { class: "flex items-center gap-2" }, [
        status === "Done"
          ? h(IconCircleCheckFilled, { class: "h-4 w-4 text-emerald-500" })
          : h(IconLoader, { class: "h-4 w-4 animate-spin text-muted-foreground" }),
        h("span", {}, status),
      ])
    },
  },
  {
    accessorKey: "target",
    header: () => h("div", { class: "flex items-center gap-1" }, [
      "Target",
    ]),
    cell: ({ row }) => h(Button, {
      variant: "ghost",
      size: "sm",
      class: "h-auto p-1 text-xs font-mono",
    }, () => [
      h("span", { class: "ml-1 font-semibold" }, String(row.getValue("target"))),
    ]),
  },
  {
    accessorKey: "limit",
    header: () => h("div", { class: "flex items-center gap-1" }, [
      "Limit",
    ]),
    cell: ({ row }) => h(Button, {
      variant: "ghost",
      size: "sm",
      class: "h-auto p-1 text-xs font-mono",
    }, () => [
      h("span", { class: "ml-1 font-semibold" }, String(row.getValue("limit"))),
    ]),
  },
  {
    accessorKey: "reviewer",
    header: "Reviewer",
    cell: ({ row }) => {
      const reviewer = row.getValue("reviewer") as string
      const isAssigned = reviewer !== "Assign reviewer"

      if (isAssigned) {
        return h("span", {}, reviewer)
      }

      return h(Select, {}, {
        default: () => [
          h(SelectTrigger, { class: "w-full" }, {
            default: () => h(SelectValue, { placeholder: "Assign reviewer" }),
          }),
          h(SelectContent, {}, {
            default: () => [
              h(SelectItem, { value: "eddie" }, () => "Eddie Lake"),
              h(SelectItem, { value: "jamik" }, () => "Jamik Tashpulatov"),
            ],
          }),
        ],
      })
    },
  },
  {
    id: "actions",
    cell: () => h(DropdownMenu, {}, {
      default: () => [
        h(DropdownMenuTrigger, { asChild: true }, {
          default: () => h(Button, {
            variant: "ghost",
            class: "h-8 w-8 p-0",
          }, {
            default: () => [
              h("span", { class: "sr-only" }, "Open menu"),
              h(IconDotsVertical, { class: "h-4 w-4" }),
            ],
          }),
        }),
        h(DropdownMenuContent, { align: "end" }, {
          default: () => [
            h(DropdownMenuItem, {}, () => "Edit"),
            h(DropdownMenuItem, {}, () => "Make a copy"),
            h(DropdownMenuItem, {}, () => "Favorite"),
            h(DropdownMenuSeparator, {}),
            h(DropdownMenuItem, {}, () => "Delete"),
          ],
        }),
      ],
    }),
  },
]

const table = useVueTable({
  get data() {
    return props.data
  },
  columns,
  getCoreRowModel: getCoreRowModel(),
  getPaginationRowModel: getPaginationRowModel(),
  getSortedRowModel: getSortedRowModel(),
  getFilteredRowModel: getFilteredRowModel(),
  onSortingChange: (updaterOrValue) => {
    sorting.value = typeof updaterOrValue === "function"
      ? updaterOrValue(sorting.value)
      : updaterOrValue
  },
  onColumnFiltersChange: (updaterOrValue) => {
    columnFilters.value = typeof updaterOrValue === "function"
      ? updaterOrValue(columnFilters.value)
      : updaterOrValue
  },
  onColumnVisibilityChange: (updaterOrValue) => {
    columnVisibility.value = typeof updaterOrValue === "function"
      ? updaterOrValue(columnVisibility.value)
      : updaterOrValue
  },
  onRowSelectionChange: (updaterOrValue) => {
    rowSelection.value = typeof updaterOrValue === "function"
      ? updaterOrValue(rowSelection.value)
      : updaterOrValue
  },
  state: {
    get sorting() { return sorting.value },
    get columnFilters() { return columnFilters.value },
    get columnVisibility() { return columnVisibility.value },
    get rowSelection() { return rowSelection.value },
  },
})
</script>

<template>
  <Tabs
    default-value="outline"
    class="w-full flex-col justify-start gap-6"
  >
    <div class="flex items-center justify-between px-4 lg:px-6">
      <Label for="view-selector" class="sr-only">
        View
      </Label>
      <Select default-value="outline">
        <SelectTrigger
          id="view-selector"
          class="flex w-fit @4xl/main:hidden"
          size="sm"
        >
          <SelectValue placeholder="Select a view" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="outline">
            Outline
          </SelectItem>
          <SelectItem value="past-performance">
            Past Performance
          </SelectItem>
          <SelectItem value="key-personnel">
            Key Personnel
          </SelectItem>
          <SelectItem value="focus-documents">
            Focus Documents
          </SelectItem>
        </SelectContent>
      </Select>
      <TabsList class="**:data-[slot=badge]:bg-muted-foreground/30 hidden **:data-[slot=badge]:size-5 **:data-[slot=badge]:rounded-full **:data-[slot=badge]:px-1 @4xl/main:flex">
        <TabsTrigger value="outline">
          Outline
        </TabsTrigger>
        <TabsTrigger value="past-performance">
          Past Performance <Badge variant="secondary">
            3
          </Badge>
        </TabsTrigger>
        <TabsTrigger value="key-personnel">
          Key Personnel <Badge variant="secondary">
            2
          </Badge>
        </TabsTrigger>
        <TabsTrigger value="focus-documents">
          Focus Documents
        </TabsTrigger>
      </TabsList>
      <div class="flex items-center gap-2">
        <DropdownMenu>
          <DropdownMenuTrigger as-child>
            <Button variant="outline" size="sm">
              <IconLayoutColumns />
              <span class="hidden lg:inline">Customize Columns</span>
              <span class="lg:hidden">Columns</span>
              <IconChevronDown />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end" class="w-56">
            <template v-for="column in table.getAllColumns().filter((column) => typeof column.accessorFn !== 'undefined' && column.getCanHide())" :key="column.id">
              <DropdownMenuCheckboxItem
                class="capitalize"
                :model-value="column.getIsVisible()"
                @update:model-value="(value) => {

                  column.toggleVisibility(!!value)
                }"
              >
                {{ column.id }}
              </DropdownMenuCheckboxItem>
            </template>
          </DropdownMenuContent>
        </DropdownMenu>
        <Button variant="outline" size="sm">
          <IconPlus />
          <span class="hidden lg:inline">Add Section</span>
        </Button>
      </div>
    </div>
    <TabsContent
      value="outline"
      class="relative flex flex-col gap-4 overflow-auto px-4 lg:px-6"
    >
      <div class="overflow-hidden rounded-lg border">
        <DragDropProvider :modifiers="[RestrictToVerticalAxis]">
          <Table>
            <TableHeader class="bg-muted sticky top-0 z-10">
              <TableRow v-for="headerGroup in table.getHeaderGroups()" :key="headerGroup.id">
                <TableHead v-for="header in headerGroup.headers" :key="header.id" :col-span="header.colSpan">
                  <FlexRender v-if="!header.isPlaceholder" :render="header.column.columnDef.header" :props="header.getContext()" />
                </TableHead>
              </TableRow>
            </TableHeader>
            <TableBody class="**:data-[slot=table-cell]:first:w-8">
              <template v-if="table.getRowModel().rows.length">
                <DraggableRow v-for="row in table.getRowModel().rows" :key="row.id" :row="row" :index="row.index" />
              </template>
              <TableRow v-else>
                <TableCell
                  :col-span="columns.length"
                  class="h-24 text-center"
                >
                  No results.
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </DragDropProvider>
      </div>
      <div class="flex items-center justify-between px-4">
        <div class="text-muted-foreground hidden flex-1 text-sm lg:flex">
          {{ table.getFilteredSelectedRowModel().rows.length }} of
          {{ table.getFilteredRowModel().rows.length }} row(s) selected.
        </div>
        <div class="flex w-full items-center gap-8 lg:w-fit">
          <div class="hidden items-center gap-2 lg:flex">
            <Label for="rows-per-page" class="text-sm font-medium">
              Rows per page
            </Label>
            <Select
              :model-value="table.getState().pagination.pageSize"
              @update:model-value="(value) => {
                table.setPageSize(Number(value))
              }"
            >
              <SelectTrigger id="rows-per-page" size="sm" class="w-20">
                <SelectValue :placeholder="`${table.getState().pagination.pageSize}`" />
              </SelectTrigger>
              <SelectContent side="top">
                <SelectItem v-for="pageSize in [10, 20, 30, 40, 50]" :key="pageSize" :value="`${pageSize}`">
                  {{ pageSize }}
                </SelectItem>
              </SelectContent>
            </Select>
          </div>
          <div class="flex w-fit items-center justify-center text-sm font-medium">
            Page {{ table.getState().pagination.pageIndex + 1 }} of
            {{ table.getPageCount() }}
          </div>
          <div class="ml-auto flex items-center gap-2 lg:ml-0">
            <Button
              variant="outline"
              class="hidden h-8 w-8 p-0 lg:flex"
              :disabled="!table.getCanPreviousPage()"
              @click="table.setPageIndex(0)"
            >
              <span class="sr-only">Go to first page</span>
              <IconChevronsLeft />
            </Button>
            <Button
              variant="outline"
              class="size-8"
              size="icon"
              :disabled="!table.getCanPreviousPage()"
              @click="table.previousPage()"
            >
              <span class="sr-only">Go to previous page</span>
              <IconChevronLeft />
            </Button>
            <Button
              variant="outline"
              class="size-8"
              size="icon"
              :disabled="!table.getCanNextPage()"
              @click="table.nextPage()"
            >
              <span class="sr-only">Go to next page</span>
              <IconChevronRight />
            </Button>
            <Button
              variant="outline"
              class="hidden size-8 lg:flex"
              size="icon"
              :disabled="!table.getCanNextPage()"
              @click="table.setPageIndex(table.getPageCount() - 1)"
            >
              <span class="sr-only">Go to last page</span>
              <IconChevronsRight />
            </Button>
          </div>
        </div>
      </div>
    </TabsContent>
    <TabsContent
      value="past-performance"
      class="flex flex-col px-4 lg:px-6"
    >
      <div class="aspect-video w-full flex-1 rounded-lg border border-dashed" />
    </TabsContent>
    <TabsContent value="key-personnel" class="flex flex-col px-4 lg:px-6">
      <div class="aspect-video w-full flex-1 rounded-lg border border-dashed" />
    </TabsContent>
    <TabsContent
      value="focus-documents"
      class="flex flex-col px-4 lg:px-6"
    >
      <div class="aspect-video w-full flex-1 rounded-lg border border-dashed" />
    </TabsContent>
  </Tabs>
</template>
```

---

### components/DraggableRow.vue
```vue
<script setup lang="ts">
import type { Row } from "@tanstack/vue-table"
import type { z } from "zod"
import type { schema } from "./DataTable.vue"
import { FlexRender } from "@tanstack/vue-table"
import { useSortable } from "dnd-kit-vue"
import {
  TableCell,
  TableRow,
} from "@/registry/new-york-v4/ui/table"

const props = defineProps<{ row: Row<z.infer<typeof schema>>, index: number }>()

const { elementRef, isDragging } = useSortable({
  id: props.row.original.id,
  index: props.index,
})
</script>

<template>
  <TableRow
    :ref="elementRef"
    :data-state="row.getIsSelected() && 'selected'"
    :data-dragging="isDragging"
    class="relative z-0 data-[dragging=true]:z-10 data-[dragging=true]:opacity-80"
  >
    <TableCell v-for="cell in row.getVisibleCells()" :key="cell.id">
      <FlexRender :render="cell.column.columnDef.cell" :props="cell.getContext()" />
    </TableCell>
  </TableRow>
</template>
```

---

### components/DragHandle.vue
```vue
<script setup lang="ts">
import { IconGripVertical } from "@tabler/icons-vue"
import { useSortableContext } from "dnd-kit-vue"
import { Button } from "@/registry/new-york-v4/ui/button"

const { handleRef, sortable } = useSortableContext()
</script>

<template>
  <Button
    :ref="handleRef"
    variant="ghost"
    size="icon"
    class="text-muted-foreground size-7 hover:bg-transparent"
  >
    <IconGripVertical class="text-muted-foreground size-3" />
    <span class="sr-only">Drag to reorder</span>
  </Button>
</template>
```

---

### components/NavDocuments.vue
```vue
<script setup lang="ts">
import type { Component } from "vue"

import {
  IconDots,
  IconFolder,
  IconShare3,
  IconTrash,
} from "@tabler/icons-vue"

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

interface Document {
  name: string
  url: string
  icon?: Component
}

defineProps<{
  items: Document[]
}>()

const { isMobile } = useSidebar()
</script>

<template>
  <SidebarGroup class="group-data-[collapsible=icon]:hidden">
    <SidebarGroupLabel>Documents</SidebarGroupLabel>
    <SidebarMenu>
      <SidebarMenuItem v-for="item in items" :key="item.name">
        <SidebarMenuButton as-child>
          <a :href="item.url">
            <component :is="item.icon" />
            <span>{{ item.name }}</span>
          </a>
        </SidebarMenuButton>
        <DropdownMenu>
          <DropdownMenuTrigger as-child>
            <SidebarMenuAction
              show-on-hover
              class="data-[state=open]:bg-accent rounded-sm"
            >
              <IconDots />
              <span class="sr-only">More</span>
            </SidebarMenuAction>
          </DropdownMenuTrigger>
          <DropdownMenuContent
            class="w-24 rounded-lg"
            :side="isMobile ? 'bottom' : 'right'"
            :align="isMobile ? 'end' : 'start'"
          >
            <DropdownMenuItem>
              <IconFolder />
              <span>Open</span>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <IconShare3 />
              <span>Share</span>
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem variant="destructive">
              <IconTrash />
              <span>Delete</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
      <SidebarMenuItem>
        <SidebarMenuButton class="text-sidebar-foreground/70">
          <IconDots class="text-sidebar-foreground/70" />
          <span>More</span>
        </SidebarMenuButton>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarGroup>
</template>
```

---

### components/NavMain.vue
```vue
<script setup lang="ts">
import type { Component } from "vue"
import { IconCirclePlusFilled, IconMail } from "@tabler/icons-vue"

import { Button } from "@/registry/new-york-v4/ui/button"
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

interface NavItem {
  title: string
  url: string
  icon?: Component
}

defineProps<{
  items: NavItem[]
}>()
</script>

<template>
  <SidebarGroup>
    <SidebarGroupContent class="flex flex-col gap-2">
      <SidebarMenu>
        <SidebarMenuItem class="flex items-center gap-2">
          <SidebarMenuButton
            tooltip="Quick Create"
            class="bg-primary text-primary-foreground hover:bg-primary/90 hover:text-primary-foreground active:bg-primary/90 active:text-primary-foreground min-w-8 duration-200 ease-linear"
          >
            <IconCirclePlusFilled />
            <span>Quick Create</span>
          </SidebarMenuButton>
          <Button
            size="icon"
            class="size-8 group-data-[collapsible=icon]:opacity-0"
            variant="outline"
          >
            <IconMail />
            <span class="sr-only">Inbox</span>
          </Button>
        </SidebarMenuItem>
      </SidebarMenu>
      <SidebarMenu>
        <SidebarMenuItem v-for="item in items" :key="item.title">
          <SidebarMenuButton :tooltip="item.title">
            <component :is="item.icon" v-if="item.icon" />
            <span>{{ item.title }}</span>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarGroupContent>
  </SidebarGroup>
</template>
```

---

### components/NavSecondary.vue
```vue
<script setup lang="ts">
import type { Component } from "vue"

import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/registry/new-york-v4/ui/sidebar"

interface NavItem {
  title: string
  url: string
  icon?: Component
}

defineProps<{
  items: NavItem[]
}>()
</script>

<template>
  <SidebarGroup>
    <SidebarGroupContent>
      <SidebarMenu>
        <SidebarMenuItem
          v-for="item in items"
          :key="item.title"
        >
          <SidebarMenuButton as-child>
            <a :href="item.url">
              <component :is="item.icon" v-if="item.icon" />
              {{ item.title }}
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarGroupContent>
  </SidebarGroup>
</template>
```

---

### components/NavUser.vue
```vue
<script setup lang="ts">
import {
  IconCreditCard,
  IconDotsVertical,
  IconLogout,
  IconNotification,
  IconUserCircle,
} from "@tabler/icons-vue"

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

interface User {
  name: string
  email: string
  avatar: string
}

defineProps<{
  user: User
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
            <Avatar class="h-8 w-8 rounded-lg grayscale">
              <AvatarImage :src="user.avatar" :alt="user.name" />
              <AvatarFallback class="rounded-lg">
                CN
              </AvatarFallback>
            </Avatar>
            <div class="grid flex-1 text-left text-sm leading-tight">
              <span class="truncate font-medium">{{ user.name }}</span>
              <span class="text-muted-foreground truncate text-xs">
                {{ user.email }}
              </span>
            </div>
            <IconDotsVertical class="ml-auto size-4" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent
          class="w-(--reka-dropdown-menu-trigger-width) min-w-56 rounded-lg"
          :side="isMobile ? 'bottom' : 'right'"
          :side-offset="4"
          align="end"
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
                <span class="text-muted-foreground truncate text-xs">
                  {{ user.email }}
                </span>
              </div>
            </div>
          </DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <IconUserCircle />
              Account
            </DropdownMenuItem>
            <DropdownMenuItem>
              <IconCreditCard />
              Billing
            </DropdownMenuItem>
            <DropdownMenuItem>
              <IconNotification />
              Notifications
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem>
            <IconLogout />
            Log out
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
```

---

### components/SectionCards.vue
```vue
<script setup lang="ts">
import { IconTrendingDown, IconTrendingUp } from "@tabler/icons-vue"

import { Badge } from "@/registry/new-york-v4/ui/badge"
import {
  Card,
  CardAction,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/registry/new-york-v4/ui/card"
</script>

<template>
  <div class="*:data-[slot=card]:from-primary/5 *:data-[slot=card]:to-card dark:*:data-[slot=card]:bg-card grid grid-cols-1 gap-4 px-4 *:data-[slot=card]:bg-gradient-to-t *:data-[slot=card]:shadow-xs lg:px-6 @xl/main:grid-cols-2 @5xl/main:grid-cols-4">
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>Total Revenue</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          $1,250.00
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            <IconTrendingUp />
            +12.5%
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Trending up this month <IconTrendingUp class="size-4" />
        </div>
        <div class="text-muted-foreground">
          Visitors for the last 6 months
        </div>
      </CardFooter>
    </Card>
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>New Customers</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          1,234
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            <IconTrendingDown />
            -20%
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Down 20% this period <IconTrendingDown class="size-4" />
        </div>
        <div class="text-muted-foreground">
          Acquisition needs attention
        </div>
      </CardFooter>
    </Card>
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>Active Accounts</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          45,678
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            <IconTrendingUp />
            +12.5%
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Strong user retention <IconTrendingUp class="size-4" />
        </div>
        <div class="text-muted-foreground">
          Engagement exceed targets
        </div>
      </CardFooter>
    </Card>
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>Growth Rate</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          4.5%
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            <IconTrendingUp />
            +4.5%
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Steady performance increase <IconTrendingUp class="size-4" />
        </div>
        <div class="text-muted-foreground">
          Meets growth projections
        </div>
      </CardFooter>
    </Card>
  </div>
</template>
```

---

### components/SiteHeader.vue
```vue
<script setup lang="ts">
import { Button } from "@/registry/new-york-v4/ui/button"
import { Separator } from "@/registry/new-york-v4/ui/separator"
import { SidebarTrigger } from "@/registry/new-york-v4/ui/sidebar"
</script>

<template>
  <header class="flex h-(--header-height) shrink-0 items-center gap-2 border-b transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-(--header-height)">
    <div class="flex w-full items-center gap-1 px-4 lg:gap-2 lg:px-6">
      <SidebarTrigger class="-ml-1" />
      <Separator
        orientation="vertical"
        class="mx-2 data-[orientation=vertical]:h-4"
      />
      <h1 class="text-base font-medium">
        Documents
      </h1>
      <div class="ml-auto flex items-center gap-2">
        <Button variant="ghost" as-child size="sm" class="hidden sm:flex">
          <a
            href="https://github.com/shadcn-ui/ui/tree/main/apps/v4/app/(examples)/dashboard"
            rel="noopener noreferrer"
            target="_blank"
            class="dark:text-foreground"
          >
            GitHub
          </a>
        </Button>
      </div>
    </div>
  </header>
</template>
```
