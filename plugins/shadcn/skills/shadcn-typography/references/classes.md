# Typography — Utility Classes

shadcn/ui does not provide a Typography component. Instead, apply these Tailwind utility classes
directly to HTML elements.

## Headings

### h1

```tsx
<h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight text-balance">
  Heading 1
</h1>
```

Classes:
- `scroll-m-20` — margin-top for scroll offset (anchor links)
- `text-4xl` — 2.25rem font size
- `font-extrabold` — font-weight 800
- `tracking-tight` — tight letter spacing
- `text-balance` — CSS text-wrap: balance (even line lengths)

### h2

```tsx
<h2 className="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0">
  Heading 2
</h2>
```

Classes:
- `scroll-m-20` — scroll offset
- `border-b pb-2` — bottom border with padding
- `text-3xl` — 1.875rem font size
- `font-semibold` — font-weight 600
- `tracking-tight` — tight letter spacing
- `first:mt-0` — no top margin when first child

### h3

```tsx
<h3 className="scroll-m-20 text-2xl font-semibold tracking-tight">
  Heading 3
</h3>
```

### h4

```tsx
<h4 className="scroll-m-20 text-xl font-semibold tracking-tight">
  Heading 4
</h4>
```

## Body Text

### Paragraph

```tsx
<p className="leading-7 [&:not(:first-child)]:mt-6">
  Paragraph text.
</p>
```

Classes:
- `leading-7` — line-height 1.75rem
- `[&:not(:first-child)]:mt-6` — top margin when not the first child

### Lead

Larger introductory paragraph:

```tsx
<p className="text-xl text-muted-foreground">
  Lead paragraph text.
</p>
```

### Large

```tsx
<div className="text-lg font-semibold">Large text</div>
```

### Small

```tsx
<small className="text-sm leading-none font-medium">Small text</small>
```

### Muted

```tsx
<p className="text-sm text-muted-foreground">Muted text</p>
```

## Inline Elements

### Inline Code

```tsx
<code className="relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold">
  code
</code>
```

Classes:
- `relative rounded` — rounded background
- `bg-muted` — muted background color
- `px-[0.3rem] py-[0.2rem]` — tight horizontal/vertical padding
- `font-mono text-sm font-semibold` — monospace, small, semibold

### Link

```tsx
<a href="#" className="font-medium text-primary underline underline-offset-4">
  Link text
</a>
```

## Block Elements

### Blockquote

```tsx
<blockquote className="mt-6 border-l-2 pl-6 italic">
  "Quote text"
</blockquote>
```

### Unordered List

```tsx
<ul className="my-6 ml-6 list-disc [&>li]:mt-2">
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
```

### Table (Typography style)

```tsx
<div className="my-6 w-full overflow-y-auto">
  <table className="w-full">
    <thead>
      <tr className="m-0 border-t p-0 even:bg-muted">
        <th className="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
          Header
        </th>
      </tr>
    </thead>
    <tbody>
      <tr className="m-0 border-t p-0 even:bg-muted">
        <td className="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
          Cell
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

Note: For a full data table component, use the [Table component](/docs/components/table) instead.

Sources: content/docs/components/radix/typography.mdx, content/docs/components/base/typography.mdx
