# Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add spinner
```

## Manual

### Dependencies

```bash
npm install reka-ui
```

Copy the source from GitHub into `src/components/ui/spinner/`:
https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/spinner

Update import paths to match your project (e.g. `@/lib/utils`).

### Customization note

You can replace the default `Loader2Icon` with any other icon by editing
the `Spinner.vue` component. Use `size-*` Tailwind classes to resize and
`text-*` classes to change the color.
