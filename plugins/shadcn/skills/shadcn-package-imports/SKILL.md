---
name: shadcn-package-imports
description: >
  shadcn/ui with package.json imports (#imports) — private import aliases,
  #components/*, #lib/*, moduleResolution bundler, resolvePackageJsonImports,
  single app and monorepo setup, file extension handling. Use when asked about
  package imports, #components alias, package.json imports shadcn,
  tsconfig bundler, resolvePackageJsonImports.
---

# shadcn/ui — Package Imports

The shadcn CLI supports `package.json#imports` for installing components,
rewriting imports, and resolving registries.

Package imports let you use private `#...` import aliases instead of
`compilerOptions.paths` in `tsconfig.json`.

## Requirements

- Specifiers must start with `#`
- TypeScript 5+ with `moduleResolution: "bundler"` and
  `resolvePackageJsonImports: true`

## Single app setup

### 1. Configure package.json
```json
{
  "imports": {
    "#components/*": "./src/components/*.tsx",
    "#lib/*": "./src/lib/*.ts",
    "#hooks/*": "./src/hooks/*.ts"
  }
}
```

Without src/ directory:
```json
{
  "imports": {
    "#components/*": "./components/*.tsx",
    "#lib/*": "./lib/*.ts",
    "#hooks/*": "./hooks/*.ts"
  }
}
```

### 2. Configure TypeScript
```json
{
  "compilerOptions": {
    "moduleResolution": "bundler",
    "resolvePackageJsonImports": true
  }
}
```
No `compilerOptions.paths` needed.

### 3. Configure components.json
```json
{
  "aliases": {
    "components": "#components",
    "ui": "#components/ui",
    "lib": "#lib",
    "hooks": "#hooks",
    "utils": "#lib/utils"
  }
}
```

### Usage
```tsx
import { Button } from "#components/ui/button"
import { cn } from "#lib/utils"
```

## File extension behaviour

With extension in target pattern (generates imports WITHOUT extension):
```json
{ "#components/*": "./src/components/*.tsx" }
// → import { Button } from "#components/ui/button"
```

Without extension in target (generates imports WITH extension):
```json
{ "#components/*": "./src/components/*" }
// → import { Button } from "#components/ui/button.tsx"
```

Use the extension in the target for most apps.

## Troubleshooting

If TypeScript cannot resolve `#...` imports:
- Specifier must start with `#`
- `imports` entry must be in the nearest `package.json`
- `moduleResolution` must be `bundler`
- `resolvePackageJsonImports` must be enabled
- The matching target must exist after components are added
- If imports still point to `@/...`, check that `components.json` uses
  the same `#...` aliases

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/package-imports.mdx`
