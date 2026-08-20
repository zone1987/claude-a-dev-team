# Date Picker — Installation

The Date Picker is built using a composition of `<Popover />` and
`<Calendar />`. Install those two components first.

## Step 1: Install Popover and Calendar

```bash
npx shadcn-vue@latest add popover
npx shadcn-vue@latest add calendar
```

For range pickers, also add RangeCalendar:

```bash
npx shadcn-vue@latest add range-calendar
```

## Step 2: Install @internationalized/date

```bash
npm install @internationalized/date
```

## Dependencies overview

| Package                   | Purpose                                     |
| :------------------------ | :------------------------------------------ |
| `@internationalized/date` | `CalendarDate`, `DateRange`, `DateFormatter`,|
|                           | `getLocalTimeZone`, `today`                 |
| `reka-ui`                 | `PopoverRoot`, `CalendarRoot`,              |
|                           | `RangeCalendarRoot`, `DateRange` type       |

## Manual installation

See the individual installation guides:
- [Popover](/docs/components/popover)
- [Calendar](/docs/components/calendar)

## Source location

Documentation: `apps/v4/content/docs/components/date-picker.md`
Examples: `apps/v4/registry/bases/reka/examples/calendar/`
(date-picker has no `ui/` directory — it is a guide-only composite)
