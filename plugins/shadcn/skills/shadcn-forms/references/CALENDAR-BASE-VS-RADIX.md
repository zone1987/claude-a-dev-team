# Calendar — Base UI vs Radix UI

Both versions use `react-day-picker` v9 as the underlying library.

## Key differences

| | Radix UI | Base UI |
|---|---|---|
| `locale` prop | Not in default (add manually, see changelog) | Built-in `locale` prop |
| `CalendarDayButton` | No `locale` param | Accepts `locale` for `toLocaleDateString` |
| `dropdown_root` style | Inline border/shadow classes | `cn-calendar-dropdown-root` token |
| Range class names | `rounded-l-md` / `rounded-r-md` | `rounded-s-(--cell-radius)` / `rounded-e-(--cell-radius)` (logical props, RTL-friendly) |
| Cell radius | Hardcoded `rounded-md` | `(--cell-radius)` CSS variable |
| Style approach | Direct Tailwind | `cn-calendar-*` CSS tokens + CSS variables |

## RTL support

Base version uses CSS logical properties (`rounded-s-*`, `rounded-e-*`,
`after:start-0`, `after:end-0`) for better RTL support without class overrides.

Radix version requires extra RTL handling via `String.raw` rotate rules.

## Adding locale to Radix version

See the Changelog section in `installation.md` or the official docs for
the multi-step migration to add `locale` prop support to the Radix version.

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/calendar.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/calendar.tsx`
