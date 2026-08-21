# Typography — Installation

There is no CLI installation step and no component to copy. Typography in shadcn-vue is pure Tailwind CSS utility classes applied on HTML elements.

## Prerequisites

Tailwind CSS v4 must be installed and configured in your project. See the shadcn-vue setup guide for details.

## CLI (no-op)

```bash
# There is no "npx shadcn-vue@latest add typography" command.
# Apply classes directly as documented in references/source.md
```

## Usage

Apply the documented utility classes directly on semantic HTML elements in your Vue templates:

```vue
<template>
  <article>
    <h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
      The Title
    </h1>
    <p class="leading-7 [&:not(:first-child)]:mt-6">
      Your paragraph text here.
    </p>
  </article>
</template>
```

## Custom utility approach

You can extract repeated class sets into custom Tailwind `@layer components` utilities or into reusable Vue wrapper components in your own project if preferred:

```css
/* In your CSS */
@layer components {
  .typography-h1 {
    @apply scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl;
  }
  .typography-p {
    @apply leading-7 [&:not(:first-child)]:mt-6;
  }
}
```
