# shadcn-vue registry-item.json — Vollstaendiges Schema

JSON-Schema-URL: `https://shadcn-vue.com/schema/registry-item.json`

## Vollstaendiges Beispiel

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

## Felder

### $schema

```json
{ "$schema": "https://shadcn-vue.com/schema/registry-item.json" }
```

### name

Name des Registry-Items (kebab-case empfohlen).

```json
{ "name": "hello-world" }
```

### title

Menschenlesbarer Titel. Kurz und beschreibend.

```json
{ "title": "Hello World" }
```

### description

Beschreibung des Items (ausfuehrlicher als `title`).

```json
{ "description": "A simple hello world component." }
```

### type

Typ des Registry-Items.

```json
{ "type": "registry:block" }
```

| Typ                  | Beschreibung                                          |
|----------------------|-------------------------------------------------------|
| `registry:block`     | Komplexe Komponenten mit mehreren Dateien             |
| `registry:component` | Einfache Komponenten                                  |
| `registry:lib`       | Lib- und Utils-Dateien                                |
| `registry:hook`      | Composables (Hooks)                                   |
| `registry:ui`        | UI-Komponenten und Single-File-Primitives             |
| `registry:page`      | Seiten oder dateibasierte Routen                      |
| `registry:file`      | Sonstige Dateien                                      |
| `registry:style`     | Eigener Style der shadcn-vue erweitert oder ersetzt   |
| `registry:theme`     | Eigenes Theme mit CSS-Variablen                       |

### author

Autor des Items.

```json
{ "author": "John Doe <john@doe.com>" }
```

### dependencies

npm-Pakete als Abhaengigkeiten. Version mit `@` angeben.

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

Registry-Abhaengigkeiten (shadcn-Komponenten oder URLs).

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

Die CLI loest Remote-Registry-Abhaengigkeiten automatisch auf.

### files

Dateien des Items. Jede Datei hat `path`, `type` und optional `target`.

**`target` ist Pflicht fuer `registry:page` und `registry:file`.**

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

Pfad zur Datei relativ zum Projekt-Root. Wird vom Build-Script geparst und transformiert.

#### type

Typ der Datei (gleiche Typen wie Item-Typ).

#### target

Ziel-Pfad im Projekt. Optional, nur Pflicht bei `registry:page` und `registry:file`.
`~` referenziert das Projekt-Root (z.B. `~/foo.config.js`).

### tailwind

**VERALTET fuer Tailwind v4.** Fuer v4 `cssVars.theme` verwenden.

Fuer Tailwind-Konfiguration (theme, plugins, content):

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

CSS-Variablen fuer das Item.

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

| Schluessel | Beschreibung                                        |
|------------|-----------------------------------------------------|
| `theme`    | Tailwind v4 CSS-Variablen (`:root { @theme { } }`)  |
| `light`    | CSS-Variablen fuer den hellen Modus                 |
| `dark`     | CSS-Variablen fuer den dunklen Modus                |

### css

CSS-Regeln fuer das Projekt hinzufuegen (`@layer base`, `@layer components`,
`@utility`, `@keyframes` etc.).

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

Angepasste Dokumentation oder Hinweis bei CLI-Installation.

```json
{
  "docs": "Remember to add the FOO_BAR environment variable to your .env file."
}
```

### categories

Organisiere das Item in Kategorien.

```json
{
  "categories": ["sidebar", "dashboard"]
}
```

### meta

Beliebige Zusatz-Metadaten.

```json
{
  "meta": { "foo": "bar" }
}
```

### extends (nur fuer registry:style)

`"extends": "none"` erstellt einen Style von Grund auf ohne shadcn-vue zu erweitern.

```json
{
  "extends": "none"
}
```
