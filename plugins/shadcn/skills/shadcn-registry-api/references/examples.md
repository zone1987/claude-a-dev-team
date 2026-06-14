# Registry Item Examples by Type

## registry:style (extending shadcn/ui)

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "example-style",
  "type": "registry:style",
  "dependencies": ["@tabler/icons-react"],
  "registryDependencies": [
    "login-01",
    "calendar",
    "https://example.com/r/editor.json"
  ],
  "cssVars": {
    "theme": { "font-sans": "Inter, sans-serif" },
    "light": { "brand": "20 14.3% 4.1%" },
    "dark": { "brand": "20 14.3% 4.1%" }
  }
}
```

## registry:style (from scratch, extends: none)

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "extends": "none",
  "name": "new-style",
  "type": "registry:style",
  "dependencies": ["tailwind-merge", "clsx"],
  "registryDependencies": ["utils", "https://example.com/r/button.json"],
  "cssVars": {
    "light": { "main": "#88aaee", "bg": "#dfe5f2" },
    "dark": { "main": "#88aaee", "bg": "#272933" }
  }
}
```

## registry:theme

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "light": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.546 0.245 262.881)",
      "primary-foreground": "oklch(0.97 0.014 254.604)"
    },
    "dark": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.707 0.165 254.624)",
      "primary-foreground": "oklch(0.97 0.014 254.604)"
    }
  }
}
```

## registry:block

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "login-01",
  "type": "registry:block",
  "description": "A simple login form.",
  "registryDependencies": ["button", "card", "input", "label"],
  "files": [
    {
      "path": "blocks/login-01/page.tsx",
      "content": "...",
      "type": "registry:page",
      "target": "app/login/page.tsx"
    },
    {
      "path": "blocks/login-01/components/login-form.tsx",
      "content": "...",
      "type": "registry:component"
    }
  ]
}
```

## registry:ui (with CSS vars)

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "sidebar",
  "type": "registry:ui",
  "dependencies": ["radix-ui"],
  "registryDependencies": ["button", "separator", "sheet", "tooltip"],
  "files": [{ "path": "ui/sidebar.tsx", "content": "...", "type": "registry:ui" }],
  "cssVars": {
    "light": {
      "sidebar-background": "oklch(0.985 0 0)",
      "sidebar-foreground": "oklch(0.141 0.005 285.823)"
    },
    "dark": {
      "sidebar-background": "oklch(0.141 0.005 285.823)",
      "sidebar-foreground": "oklch(0.985 0 0)"
    }
  }
}
```

## registry:lib

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "utils",
  "type": "registry:lib",
  "dependencies": ["clsx", "tailwind-merge"],
  "files": [
    {
      "path": "lib/utils.ts",
      "content": "import { clsx } from 'clsx'\nimport { twMerge } from 'tailwind-merge'\nexport function cn(...inputs) { return twMerge(clsx(inputs)) }",
      "type": "registry:lib"
    }
  ]
}
```

## registry:hook

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "use-mobile",
  "type": "registry:hook",
  "files": [{ "path": "hooks/use-mobile.ts", "content": "...", "type": "registry:hook" }]
}
```

## registry:font

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "font-inter",
  "type": "registry:font",
  "font": {
    "family": "'Inter Variable', sans-serif",
    "provider": "google",
    "import": "Inter",
    "variable": "--font-sans",
    "subsets": ["latin"],
    "dependency": "@fontsource-variable/inter"
  }
}
```

Font with custom selector (heading fonts):

```json
{
  "font": {
    "family": "'Playfair Display Variable', serif",
    "provider": "google",
    "import": "Playfair_Display",
    "variable": "--font-heading",
    "subsets": ["latin"],
    "selector": "h1, h2, h3, h4, h5, h6",
    "dependency": "@fontsource-variable/playfair-display"
  }
}
```

## registry:base

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-base",
  "type": "registry:base",
  "config": {
    "style": "custom-base",
    "iconLibrary": "lucide",
    "tailwind": { "baseColor": "neutral" }
  },
  "dependencies": ["class-variance-authority", "tw-animate-css", "lucide-react"],
  "registryDependencies": ["utils", "font-inter"],
  "cssVars": {
    "light": { "background": "oklch(1 0 0)", "foreground": "oklch(0.141 0.005 285.823)" },
    "dark": { "background": "oklch(0.141 0.005 285.823)", "foreground": "oklch(0.985 0 0)" }
  },
  "css": {
    "@import \"tw-animate-css\"": {},
    "@layer base": {
      "*": { "@apply border-border outline-ring/50": {} },
      "body": { "@apply bg-background text-foreground": {} }
    }
  }
}
```

`config` fields for `registry:base`:
`style`, `iconLibrary`, `rsc`, `tsx`, `rtl`, `menuColor`, `menuAccent`,
`tailwind.baseColor`, `tailwind.css`, `tailwind.prefix`,
`aliases.components`, `aliases.utils`, `aliases.ui`, `aliases.lib`,
`aliases.hooks`, `registries`

## registry:item (universal, no framework detection needed)

All files must have an explicit `target`:

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "python-rules",
  "type": "registry:item",
  "files": [
    {
      "path": "/path/to/custom-python.mdc",
      "type": "registry:file",
      "target": "~/.cursor/rules/custom-python.mdc",
      "content": "..."
    }
  ]
}
```

## CSS: animations (keyframes + cssVars.theme)

```json
{
  "cssVars": { "theme": { "--animate-wiggle": "wiggle 1s ease-in-out infinite" } },
  "css": {
    "@keyframes wiggle": {
      "0%, 100%": { "transform": "rotate(-3deg)" },
      "50%": { "transform": "rotate(3deg)" }
    }
  }
}
```

## CSS: Tailwind plugins

```json
{
  "dependencies": ["@tailwindcss/typography"],
  "css": {
    "@plugin \"@tailwindcss/typography\"": {},
    "@layer components": { ".prose": { "max-width": "65ch" } }
  }
}
```

Source: registry/examples.mdx
