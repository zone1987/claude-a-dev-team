# shadcn-vue Dark Mode: Astro

## Contents

- [Step 1: Create an inline theme script](#step-1-create-an-inline-theme-script)
- [Step 2: Install Dependencies](#step-2-install-dependencies)
- [Step 3: Add a mode toggle component](#step-3-add-a-mode-toggle-component)
- [Step 4: Display the mode toggle](#step-4-display-the-mode-toggle)

## Step 1: Create an inline theme script

Add an inline script to your Astro page to read and apply the theme from localStorage
before the page renders (avoids flash of wrong theme):

`src/pages/index.astro`:

```astro
---
import '../styles/globals.css'
---

<script is:inline>
  const getThemePreference = () => {
    if (typeof localStorage !== 'undefined' && localStorage.getItem('theme')) {
      return localStorage.getItem('theme');
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };
  const isDark = getThemePreference() === 'dark';
  document.documentElement.classList[isDark ? 'add' : 'remove']('dark');

  if (typeof localStorage !== 'undefined') {
    const observer = new MutationObserver(() => {
      const isDark = document.documentElement.classList.contains('dark');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
  }
</script>

<html lang="en">
  <body>
    <h1>Astro</h1>
  </body>
</html>
```

## Step 2: Install Dependencies

```bash
npm install @vueuse/core
```

Optional (icons):

```bash
npm install -D @iconify/vue @iconify-json/radix-icons
```

## Step 3: Add a mode toggle component

We use [`useColorMode`](https://vueuse.org/core/usecolormode/) from `@vueuse/core`.

`components/ModeToggle.vue`:

```vue
<script setup lang="ts">
import { Icon } from '@iconify/vue'
import { useColorMode } from '@vueuse/core'
import { Button } from '@/components/ui/button'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'

const mode = useColorMode()
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button variant="outline">
        <Icon
          icon="radix-icons:moon"
          class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
        />
        <Icon
          icon="radix-icons:sun"
          class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
        />
        <span class="sr-only">Toggle theme</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end">
      <DropdownMenuItem @click="mode = 'light'">
        Light
      </DropdownMenuItem>
      <DropdownMenuItem @click="mode = 'dark'">
        Dark
      </DropdownMenuItem>
      <DropdownMenuItem @click="mode = 'auto'">
        System
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
```

## Step 4: Display the mode toggle

Use `client:load` to hydrate the Vue component in Astro:

`src/pages/index.astro`:

```astro
---
import '../styles/globals.css'
import ModeToggle from '@/components/ModeToggle.vue';
---

<!-- Inline script from Step 1 here -->

<html lang="en">
  <body>
    <h1>Astro</h1>
    <ModeToggle client:load />
  </body>
</html>
```

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/dark-mode/04.astro.md`
