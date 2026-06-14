# Typography — Style Classes Reference

This is the complete set of Tailwind utility class combinations used for each typographic element in shadcn-vue. No Vue component source exists; these classes are applied directly on HTML elements.

## Headings

### h1

```
scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl
```

### h2

```
scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0
```

### h3

```
scroll-m-20 text-2xl font-semibold tracking-tight
```

### h4

```
scroll-m-20 text-xl font-semibold tracking-tight
```

## Body text

### p (paragraph)

```
leading-7 [&:not(:first-child)]:mt-6
```

### Lead (intro paragraph)

```
text-xl text-muted-foreground
```

### Large

```
text-lg font-semibold
```

### Small

```
text-sm font-medium leading-none
```

### Muted

```
text-sm text-muted-foreground
```

## Inline elements

### Inline code

```
relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold
```

## Block elements

### Blockquote

```
mt-6 border-l-2 pl-6 italic
```

### List (ul)

```
my-6 ml-6 list-disc [&>li]:mt-2
```

### Table

Container: `my-6 w-full overflow-y-auto`

`table`: `w-full`

`tr`: `m-0 border-t p-0 even:bg-muted`

`th`: `border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right`

`td`: `border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right`
