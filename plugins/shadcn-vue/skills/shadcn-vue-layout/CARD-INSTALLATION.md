# Card — Installation

## CLI

```bash
npx shadcn-vue@latest add card
```

## Manual

No extra dependencies required. The Card component uses only `@/lib/utils` for
the `cn` helper, which is already included in any shadcn-vue project.

Copy the source files from `references/source.md` into your project under
`components/ui/card/` and update the import paths to match your project
structure.

### File structure

```
components/ui/card/
├── Card.vue
├── CardAction.vue
├── CardContent.vue
├── CardDescription.vue
├── CardFooter.vue
├── CardHeader.vue
├── CardTitle.vue
└── index.ts
```

---
Source: `registry/new-york-v4/ui/card/`
