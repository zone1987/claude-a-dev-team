# shadcn-vue Registry — Overview & Getting Started

Build, host and use your own component registry.

## Contents

- [What is a registry?](#what-is-a-registry)
- [Step 1: create registry.json](#step-1-create-registryjson)
- [Step 2: create a component](#step-2-create-a-component)
- [Step 3: add the item to registry.json](#step-3-add-the-item-to-registryjson)
- [Step 4: install the CLI and add a build script](#step-4-install-the-cli-and-add-a-build-script)
- [Step 5: serve the registry](#step-5-serve-the-registry)
- [Step 6: publish](#step-6-publish)
- [Add auth](#add-auth)
- [Install an item via the CLI](#install-an-item-via-the-cli)
- [Guidelines](#guidelines)

## What is a registry?

With the `shadcn-vue` CLI you can run and distribute your own component registries.
Registry items are automatically compatible with the `shadcn-vue` CLI.

**Requirement:** registry items must be valid JSON files that conform to the
[registry-item schema](/docs/registry/registry-item-json).

---

## Step 1: create registry.json

```json
{
  "$schema": "https://shadcn-vue.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": []
}
```

Must conform to the [registry.json schema](/docs/registry/registry-json).

---

## Step 2: create a component

```vue
<!-- registry/new-york/HelloWorld/HelloWorld.vue -->
<script setup lang="ts">
import { Button } from "@/components/ui/button"
</script>

<template>
  <Button>Hello World</Button>
</template>
```

Directory structure (required):
```
registry/
└── new-york/
    └── HelloWorld/
        └── HelloWorld.vue
```

Tailwind configuration (when in a custom directory):
```ts
// tailwind.config.ts
export default {
  content: ["./registry/**/*.{js,ts,jsx,tsx,vue}"],
}
```

---

## Step 3: add the item to registry.json

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

## Step 4: install the CLI and add a build script

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

Output: `public/r/hello-world.json` (default path).

Custom output: `shadcn-vue build --output dist/r`

---

## Step 5: serve the registry

```bash
npm run dev
```

Available at: `http://localhost:3000/r/hello-world.json`

---

## Step 6: publish

Deploy the registry to a public URL (e.g. Vercel, Netlify).

---

## Add auth

The CLI has no built-in auth support. Recommendation: pass a token as a query parameter.

```
http://localhost:3000/r/hello-world.json?token=SECURE_TOKEN
```

The CLI handles `401 Unauthorized` responses and shows the user a message.
Encrypt tokens and give them an expiry time.

---

## Install an item via the CLI

```bash
npx shadcn-vue@latest add http://localhost:3000/r/hello-world.json
```

---

## Guidelines

- Place registry items under `registry/[STYLE]/[NAME]`
- Required fields: `name`, `description`, `type`, `files`
- List all registry dependencies in `registryDependencies`
  (a name such as `button`, `card`, or a URL `http://...`)
- List all npm packages in `dependencies` (format: `name@version`)
- **Always import via the `@/registry` path:** `import { HelloWorld } from "@/registry/new-york/hello-world/hello-world"`
- Ideally nest files into `components/`, `hooks/`, `lib/` subfolders
