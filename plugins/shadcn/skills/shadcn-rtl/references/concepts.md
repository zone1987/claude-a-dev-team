# RTL Concepts and Migration

## How it works

When `rtl: true` is set in `components.json` and you install a component, the
CLI automatically:

- Converts physical classes (`left-*`, `right-*`) to logical equivalents
  (`start-*`, `end-*`)
- Updates directional props to logical values
- Adjusts text alignment and spacing classes
- Flips supported icons with `rtl:rotate-180`
- Converts directional animation classes (e.g. `slide-in-from-right` →
  `slide-in-from-end`)

## Supported styles

Automatic CLI transformation is only available for projects using `shadcn create`
with the new styles: `base-nova`, `radix-nova`, etc. (not legacy styles).

## Enable RTL in new project

```bash
npx shadcn@latest create --template next --rtl
# or --template vite / --template start
```

Creates `components.json` with:

```json
{ "rtl": true }
```

## Migrate existing components

```bash
npx shadcn@latest migrate rtl [path]
```

`[path]` accepts a path or glob. Without a path, migrates all files in the
`ui` directory.

### Components that need manual migration

The CLI does NOT automatically migrate:
- Calendar
- Pagination
- Sidebar

See each component's individual RTL support section.

### Migrate icons

```tsx
<ArrowRightIcon className="rtl:rotate-180" />
```

### Install DirectionProvider component

```bash
npx shadcn@latest add direction
```

## Animation workaround (tw-animate-css issue)

Known issue: logical slide utilities in `tw-animate-css` don't work correctly.
Workaround — pass `dir="rtl"` directly to portal elements:

```tsx
<PopoverContent dir="rtl">...</PopoverContent>
<TooltipContent dir="rtl">...</TooltipContent>
```

## Font recommendation

Use Google Noto fonts for best RTL support. Pairs well with Inter and Geist.

- Arabic: `Noto_Sans_Arabic` / `@fontsource-variable/noto-sans-arabic`
- Hebrew: `Noto_Sans_Hebrew` / `@fontsource-variable/noto-sans-hebrew`

Source: rtl/index.mdx
