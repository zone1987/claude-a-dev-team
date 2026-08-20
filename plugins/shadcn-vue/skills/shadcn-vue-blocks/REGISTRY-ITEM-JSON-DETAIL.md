# shadcn-vue registry-item.json — Complete Schema

JSON-Schema-URL: `https://shadcn-vue.com/schema/registry-item.json`

## Complete example

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "hello-world",
  "type": "registry:block",
  "title": "Hello World",
  "description": "A simple hello world component.",
  "files": [
    {
      "path": "registry/new-york/HelloWorld/HelloWorld.vue",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/HelloWorld/useHelloWorld.ts",
      "type": "registry:hook"
    }
  ]
}
```

---

## Fields

### $schema

```json
{ "$schema": "https://shadcn-vue.com/schema/registry-item.json" }
```

### name

Name of the registry item (kebab-case recommended).

```json
{ "name": "hello-world" }
```

### title

Human-readable title. Short and descriptive.

```json
{ "title": "Hello World" }
```

### description

Description of the item (more detailed than `title`).

```json
{ "description": "A simple hello world component." }
```

### type

Type of the registry item.

```json
{ "type": "registry:block" }
```

| Type                 | Description                                           |
|----------------------|-------------------------------------------------------|
| `registry:block`     | Complex components with multiple files                |
| `registry:component` | Simple components                                     |
| `registry:lib`       | Lib and utils files                                   |
| `registry:hook`      | Composables (hooks)                                   |
| `registry:ui`        | UI components and single-file primitives              |
| `registry:page`      | Pages or file-based routes                            |
| `registry:file`      | Miscellaneous files                                   |
| `registry:style`     | Custom style extending or replacing shadcn-vue        |
| `registry:theme`     | Custom theme with CSS variables                       |

### author

Author of the item.

```json
{ "author": "John Doe <john@doe.com>" }
```

### dependencies

npm packages as dependencies. Specify the version with `@`.

```json
{
  "dependencies": [
    "reka-ui",
    "zod",
    "@lucide/vue",
    "name@1.0.2"
  ]
}
```

### registryDependencies

Registry dependencies (shadcn components or URLs).

```json
{
  "registryDependencies": [
    "button",
    "input",
    "select",
    "https://example.com/r/editor.json"
  ]
}
```

The CLI resolves remote registry dependencies automatically.

### files

Files of the item. Every file has `path`, `type` and optionally `target`.

**`target` is required for `registry:page` and `registry:file`.**

```json
{
  "files": [
    {
      "path": "registry/new-york/HelloWorld/page.vue",
      "type": "registry:page",
      "target": "pages/hello/index.vue"
    },
    {
      "path": "registry/new-york/HelloWorld/HelloWorld.vue",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/HelloWorld/useHelloWorld.ts",
      "type": "registry:hook"
    },
    {
      "path": "registry/new-york/HelloWorld/.env",
      "type": "registry:file",
      "target": "~/.env"
    }
  ]
}
```

#### path

Path to the file relative to the project root. Parsed and transformed by the build script.

#### type

Type of the file (same types as the item type).

#### target

Target path in the project. Optional, required only for `registry:page` and `registry:file`.
`~` references the project root (e.g. `~/foo.config.js`).

### tailwind

**DEPRECATED for Tailwind v4.** For v4 use `cssVars.theme` instead.

For Tailwind configuration (theme, plugins, content):

```json
{
  "tailwind": {
    "config": {
      "theme": {
        "extend": {
          "colors": {
            "brand": "hsl(var(--brand))"
          },
          "keyframes": {
            "wiggle": {
              "0%, 100%": { "transform": "rotate(-3deg)" },
              "50%": { "transform": "rotate(3deg)" }
            }
          },
          "animation": {
            "wiggle": "wiggle 1s ease-in-out infinite"
          }
        }
      }
    }
  }
}
```

### cssVars

CSS variables for the item.

```json
{
  "cssVars": {
    "theme": {
      "font-sans": "Inter, sans-serif",
      "--animate-wiggle": "wiggle 1s ease-in-out infinite"
    },
    "light": {
      "brand": "20 14.3% 4.1%",
      "radius": "0.5rem"
    },
    "dark": {
      "brand": "20 14.3% 4.1%"
    }
  }
}
```

| Key        | Description                                         |
|------------|-----------------------------------------------------|
| `theme`    | Tailwind v4 CSS variables (`:root { @theme { } }`)  |
| `light`    | CSS variables for light mode                        |
| `dark`     | CSS variables for dark mode                         |

### css

Add CSS rules to the project (`@layer base`, `@layer components`,
`@utility`, `@keyframes`, etc.).

```json
{
  "css": {
    "@layer base": {
      "body": {
        "font-size": "var(--text-base)",
        "line-height": "1.5"
      }
    },
    "@layer components": {
      "button": {
        "background-color": "var(--color-primary)",
        "color": "var(--color-white)"
      }
    },
    "@utility text-magic": {
      "font-size": "var(--text-base)",
      "line-height": "1.5"
    },
    "@keyframes wiggle": {
      "0%, 100%": {
        "transform": "rotate(-3deg)"
      },
      "50%": {
        "transform": "rotate(3deg)"
      }
    }
  }
}
```

### docs

Custom documentation or a note shown on CLI installation.

```json
{
  "docs": "Remember to add the FOO_BAR environment variable to your .env file."
}
```

### categories

Organize the item into categories.

```json
{
  "categories": ["sidebar", "dashboard"]
}
```

### meta

Arbitrary additional metadata.

```json
{
  "meta": { "foo": "bar" }
}
```

### extends (registry:style only)

`"extends": "none"` creates a style from scratch without extending shadcn-vue.

```json
{
  "extends": "none"
}
```
