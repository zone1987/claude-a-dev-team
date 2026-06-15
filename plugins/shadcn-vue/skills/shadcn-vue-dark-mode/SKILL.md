---
name: shadcn-vue-dark-mode
description: >
  Dark Mode in shadcn-vue fuer alle Frameworks: Vite (@vueuse/core useColorMode),
  Nuxt (@nuxtjs/color-mode, classSuffix), Vitepress (useToggle + useData isDark),
  Astro (inline script + useColorMode). Vollstaendige ModeToggle-Komponenten.
  Triggers: "shadcn vue dark mode", "dark mode vue", "dark mode nuxt shadcn",
  "dark mode vite shadcn", "useColorMode shadcn", "@nuxtjs/color-mode shadcn",
  "dark mode toggle vue", "light dark mode shadcn vue", "dark mode astro vue",
  "vitepress dark mode shadcn", "theme toggle shadcn vue"
---

# shadcn-vue: Dark Mode

Dark Mode basiert auf der `.dark`-CSS-Klasse am `<html>`-Element. Die Theme-Tokens
in `:root` werden durch `.dark`-Varianten ueberschrieben.

## Reference Files

- `references/vite.md` — Vite: @vueuse/core useColorMode, optionale Icons
  (@iconify/vue @iconify-json/radix-icons), vollstaendige ModeToggle.vue
  mit DropdownMenu (Light / Dark / System)
- `references/nuxt.md` — Nuxt: @nuxtjs/color-mode Modul, nuxt.config.ts
  (classSuffix: ''), useColorMode composable, vollstaendige ModeToggle.vue
  mit colorMode.preference
- `references/vitepress.md` — Vitepress: @vueuse/core useToggle,
  useData isDark, vollstaendige ModeToggle.vue
- `references/astro.md` — Astro: Inline-Script fuer localStorage/matchMedia,
  useColorMode (@vueuse/core), vollstaendige ModeToggle.vue,
  client:load Direktive
