# shadcn-vue: Typography Reference

shadcn-vue Typography provides Tailwind CSS utility class conventions applied directly
to semantic HTML elements. There are no component files to install — these are pure
CSS class combinations.

## Contents

- [h1](#h1)
- [h2](#h2)
- [h3](#h3)
- [h4](#h4)
- [p (paragraph)](#p-paragraph)
- [blockquote](#blockquote)
- [table](#table)
- [list](#list)
- [Inline Code](#inline-code)
- [Lead](#lead)
- [Large](#large)
- [Small](#small)
- [Muted](#muted)
- [Summary Table](#summary-table)

## h1

Demo component: `TypographyH1`

```html
<h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
  Taxing Laughter: The Joke Tax Chronicles
</h1>
```

## h2

Demo component: `TypographyH2`

```html
<h2 class="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0">
  The People of the Kingdom
</h2>
```

## h3

Demo component: `TypographyH3`

```html
<h3 class="scroll-m-20 text-2xl font-semibold tracking-tight">
  The Joke Tax
</h3>
```

## h4

Demo component: `TypographyH4`

```html
<h4 class="scroll-m-20 text-xl font-semibold tracking-tight">
  People stopped telling jokes
</h4>
```

## p (paragraph)

Demo component: `TypographyP`

```html
<p class="leading-7 [&:not(:first-child)]:mt-6">
  The king, seeing how much happiness...
</p>
```

## blockquote

Demo component: `TypographyBlockquote`

```html
<blockquote class="mt-6 border-l-2 pl-6 italic">
  "After all," he said, "everyone enjoys a good joke..."
</blockquote>
```

## table

Demo component: `TypographyTable`

```html
<div class="my-6 w-full overflow-y-auto">
  <table class="w-full">
    <thead>
      <tr class="m-0 border-t p-0 even:bg-muted">
        <th class="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
          King's Treasury
        </th>
        <th class="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
          People's Happiness
        </th>
      </tr>
    </thead>
    <tbody>
      <tr class="m-0 border-t p-0 even:bg-muted">
        <td class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
          Empty
        </td>
        <td class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
          Overflowing
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## list

Demo component: `TypographyList`

```html
<ul class="my-6 ml-6 list-disc [&>li]:mt-2">
  <li>1st level of puns: 5 gold coins</li>
  <li>2nd level of jokes: 10 gold coins</li>
  <li>3rd level of one-liners: 20 gold coins</li>
</ul>
```

## Inline Code

Demo component: `TypographyInlineCode`

```html
<code class="relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold">
  @radix-ui/react-alert-dialog
</code>
```

## Lead

Demo component: `TypographyLead`

```html
<p class="text-xl text-muted-foreground">
  A modal dialog that interrupts the user with important content and expects a response.
</p>
```

## Large

Demo component: `TypographyLarge`

```html
<div class="text-lg font-semibold">
  Are you absolutely sure?
</div>
```

## Small

Demo component: `TypographySmall`

```html
<small class="text-sm font-medium leading-none">
  Email address
</small>
```

## Muted

Demo component: `TypographyMuted`

```html
<p class="text-sm text-muted-foreground">
  Enter your email address.
</p>
```

## Summary Table

| Element | Key Classes |
|---|---|
| h1 | `scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl` |
| h2 | `scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight` |
| h3 | `scroll-m-20 text-2xl font-semibold tracking-tight` |
| h4 | `scroll-m-20 text-xl font-semibold tracking-tight` |
| p | `leading-7 [&:not(:first-child)]:mt-6` |
| blockquote | `mt-6 border-l-2 pl-6 italic` |
| ul | `my-6 ml-6 list-disc [&>li]:mt-2` |
| inline code | `relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold` |
| lead | `text-xl text-muted-foreground` |
| large | `text-lg font-semibold` |
| small | `text-sm font-medium leading-none` |
| muted | `text-sm text-muted-foreground` |

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/.typography.md`
and `components/typography.md`
