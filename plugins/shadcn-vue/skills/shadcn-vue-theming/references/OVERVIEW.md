# shadcn-vue: Theming

shadcn-vue recommends CSS variables for theming. Semantic token names
(`background`, `foreground`, `primary` etc.) are mapped to Tailwind utilities:
`bg-background`, `text-foreground`, `border-border`, `ring-ring`.

Dark mode works with the same tokens, overridden in the `.dark` selector.

## Reference Files

- `OVERVIEW-DETAIL.md` — Token convention (background/foreground pairs),
  complete token table with intended use, radius scale (sm/md/lg/xl/2xl/3xl/4xl),
  adding new tokens (@theme inline), base colors (Neutral/Gray/Zinc/Stone/Slate),
  complete neutral theme CSS, variant without CSS variables (--no-css-variables)
