# shadcn-vue Installation: Nuxt

## Contents

- [Step 1: Create project](#step-1-create-project)
- [Step 2: Add Tailwind CSS](#step-2-add-tailwind-css)
- [Step 3: Add Nuxt module (shadcn-nuxt)](#step-3-add-nuxt-module-shadcn-nuxt)
- [Step 4: Configure nuxt.config.ts](#step-4-configure-nuxtconfigts)
- [Step 5: Add ssrWidth plugin (optional)](#step-5-add-ssrwidth-plugin-optional)
- [Step 6: Run Nuxt Prepare](#step-6-run-nuxt-prepare)
- [Step 7: Run the CLI](#step-7-run-the-cli)
- [Step 8: Add Components](#step-8-add-components)

## Step 1: Create project

```bash
npm create nuxt@latest
```

If you encounter `ERROR: Cannot read properties of undefined (reading 'sys') (x4)`:

```bash
npm install -D typescript
```

## Step 2: Add Tailwind CSS

### Option A: @tailwindcss/vite

```bash
npm install tailwindcss @tailwindcss/vite -D
```

Create `app/assets/css/tailwind.css`:

```css
@import "tailwindcss";
```

Update `nuxt.config.ts`:

```ts
import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  css: ['~/assets/css/tailwind.css'],
  vite: {
    plugins: [tailwindcss()],
  },
})
```

### Option B: @nuxtjs/tailwindcss

```bash
npm install tailwindcss @nuxtjs/tailwindcss@7.0.0-beta.1 -D
```

`app/assets/css/tailwind.css`:

```css
@import "tailwindcss";
```

```ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],
})
```

## Step 3: Add Nuxt module (shadcn-nuxt)

Skipping this causes numerous console warnings due to Nuxt's auto-import feature.

### Option A: nuxi module add (recommended)

```bash
npx nuxi@latest module add shadcn-nuxt
```

### Option B: Manual — modules/shadcn.ts

```bash
npm install -D @types/node
```

Create `modules/shadcn.ts`:

```ts
import { readdirSync } from 'node:fs'
import { join } from 'node:path'
import {
  addComponentExports,
  addComponentsDir,
  createResolver,
  defineNuxtModule,
} from 'nuxt/kit'

export interface ShadcnVueOptions {
  /** Prefix for all the imported component. @default "Ui" */
  prefix: string
  /** Directory that the component lives in. @default "@/components/ui" */
  componentDir: string
}

export default defineNuxtModule<ShadcnVueOptions>({
  defaults: {
    prefix: 'Ui',
    componentDir: '@/components/ui',
  },
  meta: {
    name: 'ShadcnVue',
    configKey: 'shadcn',
    version: '0.0.1',
    compatibility: { nuxt: '>=3.17.0' },
  },
  async setup({ componentDir, prefix }, nuxt) {
    const COMPONENT_DIR_PATH = componentDir!
    const ROOT_DIR_PATH = nuxt.options.rootDir
    const { resolve, resolvePath } = createResolver(ROOT_DIR_PATH)
    const componentsPath = await resolvePath(COMPONENT_DIR_PATH)

    addComponentsDir({
      path: componentsPath,
      extensions: [],
      ignore: ['**/*'],
    }, { prepend: true })

    try {
      await Promise.all(readdirSync(componentsPath).map(async (dir) => {
        try {
          const filePath = await resolvePath(
            join(COMPONENT_DIR_PATH, dir, 'index'),
            { extensions: ['.ts', '.js'] }
          )
          addComponentExports({ prefix, filePath: resolve(filePath), priority: 1 })
        }
        catch (err) {
          if (err instanceof Error) console.warn('Module error: ', err.message)
        }
      }))
    }
    catch (err) {
      if (err instanceof Error) console.warn(err.message)
    }
  },
})
```

## Step 4: Configure nuxt.config.ts

```ts
export default defineNuxtConfig({
  modules: ['shadcn-nuxt'],
  shadcn: {
    /**
     * Prefix for all the imported component.
     * @default "Ui"
     */
    prefix: '',
    /**
     * Directory that the component lives in.
     * Will respect the Nuxt aliases.
     * @link https://nuxt.com/docs/api/nuxt-config#alias
     * @default "@/components/ui"
     */
    componentDir: '@/components/ui'
  }
})
```

## Step 5: Add ssrWidth plugin (optional)

Some components require ssrWidth via VueUse to avoid hydration errors on mobile.

Create `app/plugins/ssr-width.ts`:

```ts
import { provideSSRWidth } from '@vueuse/core'

export default defineNuxtPlugin((nuxtApp) => {
  provideSSRWidth(1024, nuxtApp.vueApp)
})
```

Read more: https://vueuse.org/core/useSSRWidth/

## Step 6: Run Nuxt Prepare

```bash
npx nuxi prepare
```

## Step 7: Run the CLI

```bash
npx shadcn-vue@latest init
# Which color would you like to use as base color? › Neutral
```

## Step 8: Add Components

```bash
npx shadcn-vue@latest add button
```

Usage (Nuxt auto-import, no explicit import needed):

```vue
<template>
  <div>
    <Button>Click me</Button>
  </div>
</template>
```

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/installation/02.nuxt.md`
