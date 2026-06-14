# registry-item.json: font and Advanced Fields

## font

Required for `registry:font` items. Configures font family, provider, import
name, CSS variable, and optional npm package.

```json
{
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

| Property     | Type       | Required | Description                                                      |
|--------------|------------|----------|------------------------------------------------------------------|
| `family`     | `string`   | Yes      | CSS font-family value                                            |
| `provider`   | `string`   | Yes      | Font provider. Only `google` is currently supported              |
| `import`     | `string`   | Yes      | Import name for `next/font/google`                               |
| `variable`   | `string`   | Yes      | CSS variable name (e.g. `--font-sans`, `--font-mono`)            |
| `weight`     | `string[]` | No       | Array of font weights to include                                 |
| `subsets`    | `string[]` | No       | Array of font subsets (e.g. `["latin"]`)                         |
| `selector`   | `string`   | No       | CSS selector to apply the font to. Defaults to `html`            |
| `dependency` | `string`   | No       | npm package for non-Next.js projects (fontsource)                |

## Complete registry-item.json example

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "type": "registry:block",
  "title": "Hello World",
  "description": "A simple hello world component.",
  "author": "Jane Doe <jane@example.com>",
  "registryDependencies": [
    "button",
    "@acme/input-form",
    "https://example.com/r/foo"
  ],
  "dependencies": ["is-even@3.0.0", "motion"],
  "devDependencies": ["tw-animate-css"],
  "files": [
    {
      "path": "registry/new-york/hello-world/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/use-hello-world.ts",
      "type": "registry:hook"
    }
  ],
  "cssVars": {
    "theme": {
      "font-heading": "Poppins, sans-serif"
    },
    "light": {
      "brand": "oklch(0.205 0.015 18)"
    },
    "dark": {
      "brand": "oklch(0.205 0.015 18)"
    }
  },
  "css": {
    "@keyframes wiggle": {
      "0%, 100%": { "transform": "rotate(-3deg)" },
      "50%": { "transform": "rotate(3deg)" }
    }
  },
  "envVars": {
    "OPENAI_API_KEY": ""
  },
  "docs": "Get an API key at https://platform.openai.com.",
  "categories": ["ai", "chat"],
  "meta": { "featured": true }
}
```

Source: registry/registry-item-json.mdx
