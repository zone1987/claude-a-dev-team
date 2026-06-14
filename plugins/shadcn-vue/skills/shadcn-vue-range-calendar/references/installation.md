# Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add range-calendar
```

This copies all 12 component files into your project's UI directory and updates the component index automatically.

## Manual Installation

### 1. Install dependencies

```bash
npm install reka-ui @internationalized/date @vueuse/core
```

`@internationalized/date` is required for the `CalendarDate`, `CalendarDateTime`, `ZonedDateTime`, and `DateValue` types used by all date props and the `DateRange` model.

### 2. Copy source files

Copy all `.vue` files and `index.ts` from `references/source.md` into your UI components directory, for example `src/components/ui/range-calendar/`.

### 3. Update imports

If your project uses a different alias than `@/registry/new-york-v4/ui/button`, update the import path in `RangeCalendarCellTrigger.vue` and `RangeCalendarNextButton.vue` / `RangeCalendarPrevButton.vue` to point to your local `button` component that exports `buttonVariants`.

Ensure `@/lib/utils` exports the `cn` helper (a `clsx` + `tailwind-merge` wrapper).

### 4. Lucide icons

`RangeCalendarNextButton` and `RangeCalendarPrevButton` import `ChevronRight` and `ChevronLeft` from `@lucide/vue`. Install if not already present:

```bash
npm install @lucide/vue
```
