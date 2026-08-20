# shadcn-vue Registry — Uebersicht & Getting Started

Eigene Komponenten-Registry aufbauen, hosten und nutzen.

## Contents

- [Was ist eine Registry?](#was-ist-eine-registry)
- [Schritt 1: registry.json anlegen](#schritt-1-registryjson-anlegen)
- [Schritt 2: Komponente erstellen](#schritt-2-komponente-erstellen)
- [Schritt 3: Item zur registry.json hinzufuegen](#schritt-3-item-zur-registryjson-hinzufuegen)
- [Schritt 4: CLI installieren und Build-Script anlegen](#schritt-4-cli-installieren-und-build-script-anlegen)
- [Schritt 5: Registry bereitstellen](#schritt-5-registry-bereitstellen)
- [Schritt 6: Veroeffentlichen](#schritt-6-veroeffentlichen)
- [Auth hinzufuegen](#auth-hinzufuegen)
- [Item per CLI installieren](#item-per-cli-installieren)
- [Richtlinien (Guidelines)](#richtlinien-guidelines)

## Was ist eine Registry?

Mit der `shadcn-vue` CLI kann man eigene Komponenten-Registries betreiben und verteilen.
Registry-Items sind automatisch kompatibel mit der `shadcn-vue` CLI.

**Anforderung:** Registry-Items muessen valide JSON-Dateien sein, die dem
[registry-item Schema](/docs/registry/registry-item-json) entsprechen.

---

## Schritt 1: registry.json anlegen

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": []
}
```

Muss dem [registry.json Schema](/docs/registry/registry-json) entsprechen.

---

## Schritt 2: Komponente erstellen

```vue
<!-- registry/new-york/HelloWorld/HelloWorld.vue -->
<script setup lang="ts">
import { Button } from "@/components/ui/button"
</script>

<template>
  <Button>Hello World</Button>
</template>
```

Verzeichnisstruktur (Pflicht):
```
registry/
└── new-york/
    └── HelloWorld/
        └── HelloWorld.vue
```

Tailwind-Konfiguration (wenn in custom directory):
```ts
// tailwind.config.ts
export default {
  content: ["./registry/**/*.{js,ts,jsx,tsx,vue}"],
}
```

---

## Schritt 3: Item zur registry.json hinzufuegen

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "files": [
        {
          "path": "registry/new-york/HelloWorld/HelloWorld.vue",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

---

## Schritt 4: CLI installieren und Build-Script anlegen

```bash
npm install shadcn-vue@latest
```

```json
{
  "scripts": {
    "registry:build": "shadcn-vue build"
  }
}
```

```bash
npm run registry:build
```

Output: `public/r/hello-world.json` (Standard-Pfad).

Custom output: `shadcn-vue build --output dist/r`

---

## Schritt 5: Registry bereitstellen

```bash
npm run dev
```

Verfuegbar unter: `http://localhost:3000/r/hello-world.json`

---

## Schritt 6: Veroeffentlichen

Registry auf einer oeffentlichen URL deployen (z.B. Vercel, Netlify).

---

## Auth hinzufuegen

Die CLI unterstuetzt kein eingebautes Auth. Empfehlung: Token als Query-Parameter.

```
http://localhost:3000/r/hello-world.json?token=SECURE_TOKEN
```

Die CLI behandelt `401 Unauthorized` Antworten und zeigt dem Benutzer eine Meldung.
Token verschluesseln und mit Ablaufzeit versehen.

---

## Item per CLI installieren

```bash
npx shadcn-vue@latest add http://localhost:3000/r/hello-world.json
```

---

## Richtlinien (Guidelines)

- Registry-Items unter `registry/[STYLE]/[NAME]` ablegen
- Pflichtfelder: `name`, `description`, `type`, `files`
- Alle Registry-Abhaengigkeiten in `registryDependencies` auflisten
  (Name z.B. `button`, `card` oder URL `http://...`)
- Alle npm-Pakete in `dependencies` auflisten (Format: `name@version`)
- **Imports immer mit `@/registry`-Pfad:** `import { HelloWorld } from "@/registry/new-york/hello-world/hello-world"`
- Dateien idealerweise in `components/`, `hooks/`, `lib/` unterordnern
