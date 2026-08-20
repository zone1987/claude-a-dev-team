# Typography — Examples

All examples show the HTML element with the recommended Tailwind utility classes as documented in shadcn-vue.

## Contents

- [h1](#h1)
- [h2](#h2)
- [h3](#h3)
- [h4](#h4)
- [Paragraph](#paragraph)
- [Blockquote](#blockquote)
- [Table](#table)
- [Unordered List](#unordered-list)
- [Inline Code](#inline-code)
- [Lead (intro paragraph)](#lead-intro-paragraph)
- [Large](#large)
- [Small](#small)
- [Muted](#muted)
- [Full typography specimen](#full-typography-specimen)

## h1

```vue
<template>
  <h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
    Taxing Laughter: The Joke Tax Chronicles
  </h1>
</template>
```

---

## h2

```vue
<template>
  <h2 class="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0">
    The People of the Kingdom
  </h2>
</template>
```

---

## h3

```vue
<template>
  <h3 class="scroll-m-20 text-2xl font-semibold tracking-tight">
    The Joke Tax
  </h3>
</template>
```

---

## h4

```vue
<template>
  <h4 class="scroll-m-20 text-xl font-semibold tracking-tight">
    People stopped telling jokes
  </h4>
</template>
```

---

## Paragraph

```vue
<template>
  <p class="leading-7 [&:not(:first-child)]:mt-6">
    The king, seeing how much happier his subjects were, realized the error
    of his ways and repealed the joke tax.
  </p>
</template>
```

---

## Blockquote

```vue
<template>
  <blockquote class="mt-6 border-l-2 pl-6 italic">
    "After all," he said, "everyone enjoys a good joke, so it's only fair
    that they should pay for the privilege."
  </blockquote>
</template>
```

---

## Table

```vue
<template>
  <div class="my-6 w-full overflow-y-auto">
    <table class="w-full">
      <thead>
        <tr class="m-0 border-t p-0 even:bg-muted">
          <th class="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
            King's Treasury
          </th>
          <th class="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
            People's happiness
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
        <tr class="m-0 border-t p-0 even:bg-muted">
          <td class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
            Modest
          </td>
          <td class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
            Satisfied
          </td>
        </tr>
        <tr class="m-0 border-t p-0 even:bg-muted">
          <td class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
            Full
          </td>
          <td class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
            Ecstatic
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
```

---

## Unordered List

```vue
<template>
  <ul class="my-6 ml-6 list-disc [&>li]:mt-2">
    <li>1st level of puns: 5 gold coins</li>
    <li>2nd level of jokes: 10 gold coins</li>
    <li>3rd level of one-liners: 20 gold coins</li>
  </ul>
</template>
```

---

## Inline Code

```vue
<template>
  <code class="relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold">
    @radix-ui/react-alert-dialog
  </code>
</template>
```

---

## Lead (intro paragraph)

```vue
<template>
  <p class="text-xl text-muted-foreground">
    A modal dialog that interrupts the user with important content and
    expects a response.
  </p>
</template>
```

---

## Large

```vue
<template>
  <div class="text-lg font-semibold">
    Are you absolutely sure?
  </div>
</template>
```

---

## Small

```vue
<template>
  <small class="text-sm font-medium leading-none">
    Email address
  </small>
</template>
```

---

## Muted

```vue
<template>
  <p class="text-sm text-muted-foreground">
    Enter your email address.
  </p>
</template>
```

---

## Full typography specimen

All elements combined showing h1, h2, h3, paragraphs, blockquote, table, list, and inline code.

```vue
<template>
  <div class="space-y-4">
    <h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
      Taxing Laughter: The Joke Tax Chronicles
    </h1>
    <p class="text-xl text-muted-foreground">
      A king's misguided attempt to tax the funniest jokes in the kingdom.
    </p>
    <h2 class="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0">
      The People of the Kingdom
    </h2>
    <p class="leading-7 [&:not(:first-child)]:mt-6">
      Once upon a time, in a far-off land, there was a very lazy king who
      spent all day lounging on his throne.
    </p>
    <h3 class="scroll-m-20 text-2xl font-semibold tracking-tight">
      The Joke Tax
    </h3>
    <p class="leading-7 [&:not(:first-child)]:mt-6">
      The king's subjects were not amused. They grumbled and complained, but
      the king was firm:
    </p>
    <blockquote class="mt-6 border-l-2 pl-6 italic">
      "After all, everyone enjoys a good joke, so it's only fair that they
      should pay for the privilege."
    </blockquote>
    <ul class="my-6 ml-6 list-disc [&>li]:mt-2">
      <li>1st level of puns: 5 gold coins</li>
      <li>2nd level of jokes: 10 gold coins</li>
      <li>3rd level of one-liners: 20 gold coins</li>
    </ul>
    <p class="leading-7 [&:not(:first-child)]:mt-6">
      Use the
      <code class="relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold">
        joke-tax
      </code>
      utility to calculate your dues.
    </p>
  </div>
</template>
```

Source: shadcn-vue typography documentation page
