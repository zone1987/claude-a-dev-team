# Calendar — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add calendar
```

This installs the `Calendar` component and all sub-components into your `components/ui/calendar/` directory.

## Manual Installation

### 1. Install dependencies

```bash
npm install reka-ui @internationalized/date @vueuse/core
```

`reka-ui` provides the headless calendar primitives.
`@internationalized/date` provides `DateValue`, `today()`, `getLocalTimeZone()`, calendar system helpers, and date arithmetic.

> **Note on tree-shaking calendar systems:** `@internationalized/date` ships support for 13 calendar systems. Only the calendar systems you import will be bundled — e.g. importing `PersianCalendar` adds only the Persian system to your bundle. The default Gregorian calendar is always included.

### 2. Copy component files

Create `components/ui/calendar/` and add the following files:

- `index.ts` — re-exports all sub-components and `LayoutTypes`
- `Calendar.vue` — root orchestrator component
- `CalendarCell.vue`
- `CalendarCellTrigger.vue`
- `CalendarGrid.vue`
- `CalendarGridBody.vue`
- `CalendarGridHead.vue`
- `CalendarGridRow.vue`
- `CalendarHeadCell.vue`
- `CalendarHeader.vue`
- `CalendarHeading.vue`
- `CalendarNextButton.vue`
- `CalendarPrevButton.vue`

### 3. Required peer components

The `Calendar.vue` component also imports `NativeSelect` and `NativeSelectOption` from `@/registry/new-york-v4/ui/native-select` for the month/year dropdown layouts. Ensure that component is installed:

```bash
npx shadcn-vue@latest add native-select
```

### 4. Required utility

Ensure `cn()` is available at `@/lib/utils`:

```ts
import { clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### 5. Icons

`CalendarNextButton` and `CalendarPrevButton` use `ChevronRight` / `ChevronLeft` from `lucide-vue-next`:

```bash
npm install lucide-vue-next
```
