# Icon Tile

Custom Shadcn Icon Tile for React and Tailwind CSS. Shadcn Icon Tile that wraps an icon in a
consistent square surface for list rows, feature cards, and empty states.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (17 total, titles enumerated upstream)](#examples-17-total-titles-enumerated-upstream)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/icon-tile
```

## Import

```tsx
import { FolderIcon } from "lucide-react"
import { IconTile } from "@/components/reui/icon-tile"
```

## Usage

```tsx
<IconTile aria-hidden="true">
  <FolderIcon />
</IconTile>
```

`IconTile` is a shadcn-compatible ReUI primitive that gives an icon a square surface with a
consistent size, radius, and border treatment. Use it for list row media, feature cards, settings
rows, empty states, and any place where a bare glyph needs a container to sit in.

The tile sizes its own child svgs, so you do not pass a size class to the icon in the common case.
Keep meaningful labels in the surrounding copy and mark purely decorative tiles with
`aria-hidden="true"`.

## Examples (17 total, titles enumerated upstream)

Elevated icon tile, Framed icon tile, All variants, Sizes, Circular tiles, Custom sizing, Color
tones, Text content, List row, Feature card, Empty state, Interactive tile, Status overlay, Soft
tones, Solid tones, Brand colors, plus the top-of-page usage preview.

Every prop, variant, size, and composition mechanism these 17 examples exercise is already
enumerated exhaustively below in the API Reference (`variant`, `size`, `radius`, `render`, the four
CSS variables, and the three ways to override size) — the page itself states the API section
"renders a single element... There are no sub-components. Everything the tile draws is derived from
CSS variables set on that root", so no example introduces a prop beyond what is catalogued there.
Representative code for the variant, size, radius, composition, and size-override mechanics is given
inline in the API Reference section below (each is a short, complete snippet as printed upstream);
the remaining examples (Text content, List row, Feature card, Empty state, Interactive tile, Status
overlay, Brand colors) combine those same mechanics with other shadcn/ui components (`Item`,
`Empty`, `Badge`, `Button`) and were not individually transcribed here since they add no new
`IconTile` prop or behaviour beyond composition.

## API Reference

`IconTile` renders a single element (a `span` by default) that centers its children on a sized,
rounded surface. There are no sub-components. Everything the tile draws is derived from CSS
variables set on that root, so a tile can be retuned from one `className` without extra wrappers.

Implementation dependencies: `@base-ui/react` and `class-variance-authority`.

### Variants

| Variant | Description |
|---|---|
| `outline` | The default. A plain bordered surface on the page background, quiet enough for list rows and toolbars. |
| `elevated` | A muted fill with a 2px background-colored ring and a soft shadow, the same recipe as the card-2 block. Reads as a physical chip lifted off the page. |
| `soft` | A tinted double container: an opacity-filled outer ring with no border around a bordered inner card, all from `currentColor`. Defaults to `text-primary`; set a text color class to retint the whole tile. |
| `solid` | A filled tone with a contrasting glyph. Defaults to `bg-primary`; override the fill with a `bg-*` class plus a readable text color to retint. |
| `frame` | A double container: a muted ring around an inset card, matching the `Frame` primitive. The inner card is painted with an `::after` pseudo element, so there is no wrapper node and `render` composition keeps working. |

```tsx
<IconTile variant="elevated">
  <PackageIcon />
</IconTile>
```

### Sizes

Each size sets the tile box, the glyph size, and the inset shared by the `soft` and `frame` variants
together, so the proportions hold at every step.

| Size | Tile | Glyph |
|---|---|---|
| `xs` | 24px | 14px |
| `sm` | 32px | 16px |
| `default` | 40px | 18px |
| `lg` | 48px | 22px |
| `xl` | 56px | 28px |

```tsx
<IconTile size="lg" variant="frame">
  <FolderIcon />
</IconTile>
```

### Radius

`radius="default"` follows the active style radius, so a tile matches the rest of the installed
style. `radius="full"` makes the tile circular.

```tsx
<IconTile radius="full">
  <FolderIcon />
</IconTile>
```

### Composition

The tile composes through the Base UI `render` prop, so it can become a link, a button, or any other
element while keeping its surface styles and data attributes.

```tsx
<IconTile render={<a href="/settings" aria-label="Open settings" />}>
  <Settings2Icon aria-hidden="true" />
</IconTile>
```

### Data attributes

The root carries data attributes for styling and for test selectors.

| Attribute | Value |
|---|---|
| `data-slot` | `"icon-tile"` |
| `data-variant` | `"outline" \| "elevated" \| "soft" \| "solid" \| "frame"` |
| `data-size` | `"xs" \| "sm" \| "default" \| "lg" \| "xl"` |

### CSS Variables

The root sets four variables, so a single `className` can retune the whole tile without touching the
icon.

| Variable | Default (at `size="default"`) | Description |
|---|---|---|
| `--icon-tile-size` | `--spacing(10)` | Tile width and height. |
| `--icon-tile-icon-size` | `--spacing(4.5)` | Glyph size applied to child svgs that carry no `size-*` class. |
| `--icon-tile-radius` | Active style radius | Corner radius. Also drives the inner card of the `soft` and `frame` variants. |
| `--icon-tile-inset` | `--spacing(0.75)` | Gap between the outer ring and the inner card of the `soft` and `frame` variants. |

### Overriding the size

There are three ways to step outside the size scale, and they can be combined.

1. **A plain utility on the tile.** A `size-*` class in `className` wins over the primitive's
   `size-(--icon-tile-size)` through tailwind-merge, so the tile box changes while the glyph keeps
   the size from the `size` prop.

   ```tsx
   <IconTile variant="elevated" className="size-14">
     <ImageIcon />
   </IconTile>
   ```

2. **A `size-*` class directly on the child icon.** Child svgs are auto-sized with
   `[&_svg:not([class*=size-])]:size-(--icon-tile-icon-size)`, so an icon that already carries a
   `size-*` class opts out of the tile's glyph sizing.

   ```tsx
   <IconTile className="size-14">
     <ImageIcon className="size-7" />
   </IconTile>
   ```

3. **The CSS variables.** Setting `--icon-tile-size` and `--icon-tile-icon-size` keeps the tile and
   glyph in step and needs no class on the icon. The `soft` and `frame` inset stays on the value
   from the `size` prop, so set `--icon-tile-inset` too when such a tile moves far from its scale
   step.

   ```tsx
   <IconTile className="[--icon-tile-icon-size:--spacing(7)] [--icon-tile-size:--spacing(14)]">
     <Settings2Icon />
   </IconTile>
   ```

For color, reach for the `soft` or `solid` variant and set a single text color class; both derive
their fills and borders from `currentColor`. Any variant can also be recolored directly through
`className`, as the brand-color example does by overriding the `elevated` fill with a Tailwind
color.

```tsx
<IconTile variant="soft" className="text-success">
  <CircleCheckIcon />
</IconTile>
```

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"outline" \| "elevated" \| "soft" \| "solid" \| "frame"` | `"outline"` | The surface treatment of the tile. |
| `size` | `"xs" \| "sm" \| "default" \| "lg" \| "xl"` | `"default"` | The tile size, which also sets the glyph size. |
| `radius` | `"default" \| "full"` | `"default"` | `"default"` uses the active style radius, `"full"` makes the tile circular. |
| `render` | `useRender.RenderProp` | `-` | Render a different element while keeping the tile styles (Base UI `useRender`). |
| `className` | `string` | `-` | Additional CSS classes, including overrides of the tile CSS variables. |
| `children` | `React.ReactNode` | `-` | The icon, initials, or short text rendered inside the tile. |

All native `span` props are supported.

## Base UI vs Radix UI

This is the component with the most substantive Base UI vs. Radix UI difference in this reference
set — real behavioural and dependency changes, not only marketing text or import paths:

1. **Implementation dependency differs**: Base UI states "Implementation dependencies: `@base-ui/react`
   and `class-variance-authority`"; Radix UI states "Implementation dependencies: `radix-ui` and
   `class-variance-authority`".

2. **Composition prop differs**, matching the pattern on Stepper, Kanban, and Badge:

   | Build | Prop | Type | Default | Description |
   |---|---|---|---|---|
   | Base UI | `render` | `useRender.RenderProp` | `-` | Render a different element while keeping the tile styles (Base UI `useRender`). |
   | Radix UI | `asChild` | `boolean` | `false` | Render the child element instead of a `span` (Radix `Slot`). |

   Base UI: `<IconTile render={<a href="/settings" aria-label="Open settings" />}><Settings2Icon aria-hidden="true" /></IconTile>`
   Radix UI: `<IconTile asChild className="hover:bg-accent"><a href="/settings" aria-label="Open settings"><Settings2Icon aria-hidden="true" /></a></IconTile>`

3. **The "Composition" prose section's wording differs** to match: Base UI says "The tile composes
   through the Base UI `render` prop, so it can become a link, a button, or any other element while
   keeping its surface styles and data attributes." Radix UI says "The tile composes through
   `asChild`, backed by the Radix `Slot`, so it can become a link, a button, or any other element
   while keeping its surface styles and data attributes."

4. **The `frame` variant's description differs by one clause**: Base UI ends "...so there is no
   wrapper node and `render` composition keeps working." Radix UI ends "...so there is no wrapper
   node and `asChild` composition keeps working." — purely the same prop-name substitution as above,
   not a behavioural difference in the `frame` variant itself.

Everything else — installation command (`@reui/icon-tile`), import path
(`@/components/reui/icon-tile`), the Variants table, Sizes table, Radius section, Data attributes,
CSS Variables, and the size-override mechanics — is identical between builds.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI
(`render` prop, `@base-ui/react` dependency), `style: "radix-nova"` means Radix UI (`asChild` prop,
`radix-ui` dependency).

## Source

- Base UI: `docs/components/base/icon-tile` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/icon-tile` — mirror captured 2026-09-04.
