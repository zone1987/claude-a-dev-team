# shadcn-vue Registry — Examples

Ready-made examples for all registry item types.

---

## Contents

- [registry:style — style extending shadcn-vue](#registrystyle-style-extending-shadcn-vue)
- [registry:style — style from scratch (extends: none)](#registrystyle-style-from-scratch-extends-none)
- [registry:theme — custom theme](#registrytheme-custom-theme)
- [registry:theme — custom color](#registrytheme-custom-color)
- [registry:block — simple block](#registryblock-simple-block)
- [registry:block — block with override primitives](#registryblock-block-with-override-primitives)
- [CSS Variables — theme variables](#css-variables-theme-variables)
- [CSS Variables — overriding Tailwind CSS variables](#css-variables-overriding-tailwind-css-variables)
- [CSS — base styles](#css-base-styles)
- [CSS — component styles](#css-component-styles)
- [CSS — simple utility](#css-simple-utility)
- [CSS — complex utility with nested selector](#css-complex-utility-with-nested-selector)
- [CSS — functional utility](#css-functional-utility)
- [CSS — animation (keyframes + cssVars)](#css-animation-keyframes-cssvars)

## registry:style — style extending shadcn-vue

Installed by `npx shadcn-vue init`:
- `@iconify/vue` as a dependency
- `Login01` block + `calendar` component
- `editor` from a remote registry
- sets the `font-sans` variable
- `brand` color in light and dark mode

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "example-style",
  "type": "registry:style",
  "dependencies": ["@iconify/vue"],
  "registryDependencies": [
    "Login01",
    "calendar",
    "https://example.com/r/editor.json"
  ],
  "cssVars": {
    "theme": {
      "font-sans": "Inter, sans-serif"
    },
    "light": {
      "brand": "20 14.3% 4.1%"
    },
    "dark": {
      "brand": "20 14.3% 4.1%"
    }
  }
}
```

---

## registry:style — style from scratch (extends: none)

Installed by `npx shadcn-vue add`:
- `tailwind-merge` and `clsx` as dependencies
- `utils` from the shadcn-vue registry
- `button`, `input`, `label`, `select` from a remote registry
- New CSS vars: `main`, `bg`, `border`, `text`, `ring`

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "extends": "none",
  "name": "new-style",
  "type": "registry:style",
  "dependencies": ["tailwind-merge", "clsx"],
  "registryDependencies": [
    "utils",
    "https://example.com/r/button.json",
    "https://example.com/r/input.json",
    "https://example.com/r/label.json",
    "https://example.com/r/select.json"
  ],
  "cssVars": {
    "theme": {
      "font-sans": "Inter, sans-serif"
    },
    "light": {
      "main": "#88aaee",
      "bg": "#dfe5f2",
      "border": "#000",
      "text": "#000",
      "ring": "#000"
    },
    "dark": {
      "main": "#88aaee",
      "bg": "#272933",
      "border": "#000",
      "text": "#e6e6e6",
      "ring": "#fff"
    }
  }
}
```

---

## registry:theme — custom theme

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "light": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.546 0.245 262.881)",
      "primary-foreground": "oklch(0.97 0.014 254.604)",
      "ring": "oklch(0.746 0.16 232.661)",
      "sidebar-primary": "oklch(0.546 0.245 262.881)",
      "sidebar-primary-foreground": "oklch(0.97 0.014 254.604)",
      "sidebar-ring": "oklch(0.746 0.16 232.661)"
    },
    "dark": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.707 0.165 254.624)",
      "primary-foreground": "oklch(0.97 0.014 254.604)",
      "ring": "oklch(0.707 0.165 254.624)",
      "sidebar-primary": "oklch(0.707 0.165 254.624)",
      "sidebar-primary-foreground": "oklch(0.97 0.014 254.604)",
      "sidebar-ring": "oklch(0.707 0.165 254.624)"
    }
  }
}
```

---

## registry:theme — custom color

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "custom-style",
  "type": "registry:style",
  "cssVars": {
    "light": { "brand": "oklch(0.99 0.00 0)" },
    "dark": { "brand": "oklch(0.14 0.00 286)" }
  }
}
```

---

## registry:block — simple block

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "Login01",
  "type": "registry:block",
  "description": "A simple login form.",
  "registryDependencies": ["button", "card", "input", "label"],
  "files": [
    {
      "path": "blocks/Login01/page.vue",
      "content": "import { LoginForm } ...",
      "type": "registry:page",
      "target": "pages/login/index.vue"
    },
    {
      "path": "blocks/login-01/components/LoginForm.vue",
      "content": "...",
      "type": "registry:component"
    }
  ]
}
```

---

## registry:block — block with override primitives

Installs `Login01` and overrides `button`, `input`, `label` with your own.

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "custom-login",
  "type": "registry:block",
  "registryDependencies": [
    "Login01",
    "https://example.com/r/button.json",
    "https://example.com/r/input.json",
    "https://example.com/r/label.json"
  ]
}
```

---

## CSS Variables — theme variables

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "theme": {
      "font-heading": "Inter, sans-serif",
      "shadow-card": "0 0 0 1px rgba(0, 0, 0, 0.1)"
    }
  }
}
```

---

## CSS Variables — overriding Tailwind CSS variables

```json
{
  "cssVars": {
    "theme": {
      "spacing": "0.2rem",
      "breakpoint-sm": "640px",
      "breakpoint-md": "768px",
      "breakpoint-lg": "1024px",
      "breakpoint-xl": "1280px",
      "breakpoint-2xl": "1536px"
    }
  }
}
```

---

## CSS — base styles

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "custom-style",
  "type": "registry:style",
  "css": {
    "@layer base": {
      "h1": { "font-size": "var(--text-2xl)" },
      "h2": { "font-size": "var(--text-xl)" }
    }
  }
}
```

---

## CSS — component styles

```json
{
  "css": {
    "@layer components": {
      "card": {
        "background-color": "var(--color-white)",
        "border-radius": "var(--rounded-lg)",
        "padding": "var(--spacing-6)",
        "box-shadow": "var(--shadow-xl)"
      }
    }
  }
}
```

---

## CSS — simple utility

```json
{
  "css": {
    "@utility content-auto": {
      "content-visibility": "auto"
    }
  }
}
```

---

## CSS — complex utility with nested selector

```json
{
  "css": {
    "@utility scrollbar-hidden": {
      "scrollbar-hidden": {
        "&::-webkit-scrollbar": {
          "display": "none"
        }
      }
    }
  }
}
```

---

## CSS — functional utility

```json
{
  "css": {
    "@utility tab-*": {
      "tab-size": "var(--tab-size-*)"
    }
  }
}
```

---

## CSS — Animation (keyframes + cssVars)

Both are needed together: `@keyframes` in `css` AND the theme variable in `cssVars`.

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "cssVars": {
    "theme": {
      "--animate-wiggle": "wiggle 1s ease-in-out infinite"
    }
  },
  "css": {
    "@keyframes wiggle": {
      "0%, 100%": { "transform": "rotate(-3deg)" },
      "50%": { "transform": "rotate(3deg)" }
    }
  }
}
```
