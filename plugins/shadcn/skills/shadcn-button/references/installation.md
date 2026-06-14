# Button — Installation

## CLI

```bash
npx shadcn@latest add button
```

## Manual — Radix UI

```bash
npm install radix-ui
```

Copy `components/ui/button.tsx` (Radix variant, see `source.md`).

## Manual — Base UI

```bash
npm install @base-ui/react
```

Copy `components/ui/button.tsx` (Base UI variant, see `source.md`).

Update import paths to match your project.

### Optional: cursor pointer

Tailwind v4 uses `cursor: default` for buttons. Add to `globals.css` to restore pointer:

```css
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

Or use `npx shadcn@latest init --pointer` during project setup.

---
Sources:
- `/tmp/shadcn-repo/apps/v4/content/docs/components/base/button.mdx`
- `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/button.mdx`
