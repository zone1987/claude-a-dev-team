# shadcn-vue Registry — Beispiele

Fertige Beispiele fuer alle Registry-Item-Typen.

---

## Contents

- [registry:style — Style der shadcn-vue erweitert](#registrystyle-style-der-shadcn-vue-erweitert)
- [registry:style — Style von Grund auf (extends: none)](#registrystyle-style-von-grund-auf-extends-none)
- [registry:theme — Eigenes Theme](#registrytheme-eigenes-theme)
- [registry:theme — Benutzerdefinierte Farbe](#registrytheme-benutzerdefinierte-farbe)
- [registry:block — Einfacher Block](#registryblock-einfacher-block)
- [registry:block — Block mit Override-Primitives](#registryblock-block-mit-override-primitives)
- [CSS Variables — Theme-Variablen](#css-variables-theme-variablen)
- [CSS Variables — Tailwind CSS-Variablen ueberschreiben](#css-variables-tailwind-css-variablen-ueberschreiben)
- [CSS — Base-Styles](#css-base-styles)
- [CSS — Component Styles](#css-component-styles)
- [CSS — Einfaches Utility](#css-einfaches-utility)
- [CSS — Komplexes Utility mit Nested Selector](#css-komplexes-utility-mit-nested-selector)
- [CSS — Funktionales Utility](#css-funktionales-utility)
- [CSS — Animation (keyframes + cssVars)](#css-animation-keyframes-cssvars)

## registry:style — Style der shadcn-vue erweitert

Installiert bei `npx shadcn-vue init`:
- `@iconify/vue` als Abhaengigkeit
- `Login01` Block + `calendar` Komponente
- `editor` aus Remote-Registry
- `font-sans` Variable setzen
- `brand` Farbe in Light und Dark Mode

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

## registry:style — Style von Grund auf (extends: none)

Installiert bei `npx shadcn-vue add`:
- `tailwind-merge` und `clsx` als Abhaengigkeiten
- `utils` aus shadcn-vue Registry
- `button`, `input`, `label`, `select` aus Remote-Registry
- Neue CSS-Vars: `main`, `bg`, `border`, `text`, `ring`

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

## registry:theme — Eigenes Theme

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

## registry:theme — Benutzerdefinierte Farbe

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

## registry:block — Einfacher Block

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

## registry:block — Block mit Override-Primitives

Installiert `Login01` und ueberschreibt `button`, `input`, `label` mit eigenen.

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

## CSS Variables — Theme-Variablen

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

## CSS Variables — Tailwind CSS-Variablen ueberschreiben

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

## CSS — Base-Styles

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

## CSS — Component Styles

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

## CSS — Einfaches Utility

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

## CSS — Komplexes Utility mit Nested Selector

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

## CSS — Funktionales Utility

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

Beides zusammen noetig: `@keyframes` in `css` UND Theme-Variable in `cssVars`.

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
