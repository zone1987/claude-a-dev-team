# registry-item.json: cssVars, css, and envVars

## cssVars

Define CSS custom properties for your registry item.

```json
{
  "cssVars": {
    "theme": {
      "font-heading": "Poppins, sans-serif"
    },
    "light": {
      "brand": "20 14.3% 4.1%",
      "radius": "0.5rem"
    },
    "dark": {
      "brand": "oklch(0.205 0.015 18)"
    }
  }
}
```

| Sub-key  | Description                                          |
|----------|------------------------------------------------------|
| `theme`  | Global CSS variables (outside light/dark scope)      |
| `light`  | Variables scoped to light mode (`:root`)             |
| `dark`   | Variables scoped to dark mode (`.dark`, `@media`)    |

Use `cssVars.theme` for Tailwind v4 projects instead of the deprecated
`tailwind` field.

## css

Add at-rules and CSS blocks directly to the project's CSS file.

```json
{
  "css": {
    "@plugin @tailwindcss/typography": {},
    "@plugin foo": {},
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
      "0%, 100%": { "transform": "rotate(-3deg)" },
      "50%": { "transform": "rotate(3deg)" }
    }
  }
}
```

Supported at-rule prefixes: `@plugin`, `@layer base`, `@layer components`,
`@utility`, `@keyframes`.

## tailwind (DEPRECATED)

Do NOT use for new Tailwind v4 projects. Use `cssVars.theme` instead.

For Tailwind v3 registries only:

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

## envVars

Add environment variables to the consumer project's `.env.local` or `.env`.
Existing variables are NOT overwritten.

```json
{
  "envVars": {
    "NEXT_PUBLIC_APP_URL": "http://localhost:4000",
    "DATABASE_URL": "postgresql://postgres:postgres@localhost:5432/postgres",
    "OPENAI_API_KEY": ""
  }
}
```

IMPORTANT: Use only for development or example variables. Never use for
production secrets.

Source: registry/registry-item-json.mdx
