# shadcn/ui — Monorepo Details

## File structure

```
apps
└── web
    ├── app
    │   └── page.tsx
    ├── components
    │   └── login-form.tsx
    ├── components.json
    └── package.json
packages
└── ui
    ├── src
    │   ├── components
    │   │   └── button.tsx
    │   ├── hooks
    │   ├── lib
    │   │   └── utils.ts
    │   └── styles
    │       └── globals.css
    ├── components.json
    └── package.json
package.json
turbo.json
```

## Requirements

1. Every workspace must have a `components.json` file.
2. `components.json` must define aliases for that workspace.
3. `style`, `iconLibrary`, and `baseColor` must be identical in both files.
4. For Tailwind CSS v4, leave `tailwind.config` blank.

## apps/web/components.json

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "radix-nova",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "../../packages/ui/src/styles/globals.css",
    "baseColor": "neutral",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "hooks": "@/hooks",
    "lib": "@/lib",
    "utils": "@workspace/ui/lib/utils",
    "ui": "@workspace/ui/components"
  }
}
```

## packages/ui/components.json

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "radix-nova",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/styles/globals.css",
    "baseColor": "neutral",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@workspace/ui/components",
    "utils": "@workspace/ui/lib/utils",
    "hooks": "@workspace/ui/hooks",
    "lib": "@workspace/ui/lib",
    "ui": "@workspace/ui/components"
  }
}
```

## Using package.json#imports in a monorepo

### apps/web/package.json
```json
{
  "name": "web",
  "private": true,
  "type": "module",
  "imports": {
    "#components/*": "./src/components/*.tsx",
    "#lib/*": "./src/lib/*.ts",
    "#hooks/*": "./src/hooks/*.ts"
  },
  "dependencies": {
    "@workspace/ui": "workspace:*"
  }
}
```

### apps/web/components.json with package imports
```json
{
  "aliases": {
    "components": "#components",
    "ui": "@workspace/ui/components",
    "lib": "#lib",
    "hooks": "#hooks",
    "utils": "@workspace/ui/lib/utils"
  }
}
```

### packages/ui/package.json
```json
{
  "name": "@workspace/ui",
  "private": true,
  "type": "module",
  "imports": {
    "#components/*": "./src/components/*.tsx",
    "#lib/*": "./src/lib/*.ts",
    "#hooks/*": "./src/hooks/*.ts"
  },
  "exports": {
    "./globals.css": "./src/styles/globals.css",
    "./components/*": "./src/components/*.tsx",
    "./lib/*": "./src/lib/*.ts",
    "./hooks/*": "./src/hooks/*.ts"
  }
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/monorepo.mdx`
