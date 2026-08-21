# Calendar — Installation

## CLI

```bash
npx shadcn@latest add calendar
```

## Manual

```bash
npm install react-day-picker date-fns
```

The `Calendar` component also requires the `Button` component to be
installed in your project.

Copy `components/ui/calendar.tsx` (see `source.md`).

Update import paths to match your project.

### Persian / Hijri calendar

Edit `calendar.tsx` and replace the DayPicker import:

```diff
- import { DayPicker } from "react-day-picker"
+ import { DayPicker } from "react-day-picker/persian"
```

---
Sources:
- `/tmp/shadcn-repo/apps/v4/content/docs/components/base/calendar.mdx`
- `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/calendar.mdx`
