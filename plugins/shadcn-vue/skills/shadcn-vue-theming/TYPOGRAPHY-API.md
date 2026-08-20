# Typography — Class Reference

Since typography has no component, this documents each element type and its recommended utility classes.

## Element class table

| Element | Recommended Tailwind classes |
|---|---|
| `h1` | `scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl` |
| `h2` | `scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0` |
| `h3` | `scroll-m-20 text-2xl font-semibold tracking-tight` |
| `h4` | `scroll-m-20 text-xl font-semibold tracking-tight` |
| `p` | `leading-7 [&:not(:first-child)]:mt-6` |
| `blockquote` | `mt-6 border-l-2 pl-6 italic` |
| `ul` | `my-6 ml-6 list-disc [&>li]:mt-2` |
| `code` (inline) | `relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold` |
| Lead paragraph | `text-xl text-muted-foreground` |
| Large text | `text-lg font-semibold` |
| Small text | `text-sm font-medium leading-none` |
| Muted text | `text-sm text-muted-foreground` |

## Table element classes

| Element | Recommended Tailwind classes |
|---|---|
| Wrapper div | `my-6 w-full overflow-y-auto` |
| `table` | `w-full` |
| `tr` | `m-0 border-t p-0 even:bg-muted` |
| `th` | `border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right` |
| `td` | `border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right` |

## Design tokens used

| Token | Usage |
|---|---|
| `scroll-m-20` | Scroll margin top for anchor links (5rem) |
| `tracking-tight` | Letter spacing `-0.025em` |
| `text-muted-foreground` | Subdued text color from CSS variable |
| `bg-muted` | Muted background for inline code and alternating table rows |
| `border-b` / `border-l-2` | Separator lines on h2 and blockquote |
| `font-mono` | Monospace font for inline code |

## No props, slots, or emits

Typography has no component API — there are no props, slots, emits, or data attributes to document. All styling is achieved via utility classes.
