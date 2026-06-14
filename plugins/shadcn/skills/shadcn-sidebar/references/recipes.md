# Sidebar — Recipes & Cookbook Patterns

## Pattern 1: Workspace switcher in SidebarHeader

```tsx
<Sidebar>
  <SidebarHeader>
    <SidebarMenu>
      <SidebarMenuItem>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <SidebarMenuButton>
              Select Workspace
              <ChevronDown className="ml-auto" />
            </SidebarMenuButton>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-[--radix-popper-anchor-width]">
            <DropdownMenuItem>
              <span>Acme Inc</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarHeader>
</Sidebar>
```

## Pattern 2: User menu in SidebarFooter

```tsx
<Sidebar>
  <SidebarFooter>
    <SidebarMenu>
      <SidebarMenuItem>
        <SidebarMenuButton>
          <User2 /> Username
        </SidebarMenuButton>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarFooter>
</Sidebar>
```

## Pattern 3: Navigation links with icons

```tsx
const navItems = [
  { title: "Home", url: "/", icon: HomeIcon },
  { title: "Settings", url: "/settings", icon: SettingsIcon },
]

<SidebarGroup>
  <SidebarGroupLabel>Navigation</SidebarGroupLabel>
  <SidebarGroupContent>
    <SidebarMenu>
      {navItems.map((item) => (
        <SidebarMenuItem key={item.title}>
          <SidebarMenuButton asChild isActive={pathname === item.url} tooltip={item.title}>
            <a href={item.url}>
              <item.icon />
              <span>{item.title}</span>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      ))}
    </SidebarMenu>
  </SidebarGroupContent>
</SidebarGroup>
```

## Pattern 4: Menu item with action button

```tsx
<SidebarMenuItem>
  <SidebarMenuButton asChild>
    <a href="#">
      <Home />
      <span>Home</span>
    </a>
  </SidebarMenuButton>
  <SidebarMenuAction showOnHover>
    <Plus />
    <span className="sr-only">Add Project</span>
  </SidebarMenuAction>
</SidebarMenuItem>
```

## Pattern 5: Menu item with badge

```tsx
<SidebarMenuItem>
  <SidebarMenuButton>
    <Bell />
    <span>Notifications</span>
  </SidebarMenuButton>
  <SidebarMenuBadge>24</SidebarMenuBadge>
</SidebarMenuItem>
```

## Pattern 6: Nested submenu

```tsx
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuSub>
    <SidebarMenuSubItem>
      <SidebarMenuSubButton asChild isActive>
        <a href="/sub-page">Sub Page</a>
      </SidebarMenuSubButton>
    </SidebarMenuSubItem>
  </SidebarMenuSub>
</SidebarMenuItem>
```

## Pattern 7: Loading skeleton

```tsx
<SidebarMenu>
  {Array.from({ length: 5 }).map((_, index) => (
    <SidebarMenuItem key={index}>
      <SidebarMenuSkeleton showIcon />
    </SidebarMenuItem>
  ))}
</SidebarMenu>
```

## Pattern 8: Collapsible group (accordion)

```tsx
<Collapsible defaultOpen className="group/collapsible">
  <SidebarGroup>
    <SidebarGroupLabel asChild>
      <CollapsibleTrigger>
        Projects
        <ChevronDown className="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180" />
      </CollapsibleTrigger>
    </SidebarGroupLabel>
    <CollapsibleContent>
      <SidebarGroupContent>
        <SidebarMenu>
          {/* items */}
        </SidebarMenu>
      </SidebarGroupContent>
    </CollapsibleContent>
  </SidebarGroup>
</Collapsible>
```

## Pattern 9: Controlled sidebar

```tsx
export function AppLayout() {
  const [open, setOpen] = React.useState(false)

  return (
    <SidebarProvider open={open} onOpenChange={setOpen}>
      <Sidebar />
    </SidebarProvider>
  )
}
```

## Pattern 10: Custom trigger button

```tsx
import { useSidebar } from "@/components/ui/sidebar"

export function CustomTrigger() {
  const { toggleSidebar } = useSidebar()

  return <button onClick={toggleSidebar}>Toggle Sidebar</button>
}
```

## Pattern 11: SidebarRail (drag-to-resize handle)

```tsx
<Sidebar>
  <SidebarHeader />
  <SidebarContent>
    <SidebarGroup />
  </SidebarContent>
  <SidebarFooter />
  <SidebarRail />
</Sidebar>
```

## Pattern 12: Inset variant (floating main content)

```tsx
<SidebarProvider>
  <Sidebar variant="inset" />
  <SidebarInset>
    <main>{children}</main>
  </SidebarInset>
</SidebarProvider>
```

## Source files

- `content/docs/components/base/sidebar.mdx`
- `registry/new-york-v4/ui/sidebar.tsx`
