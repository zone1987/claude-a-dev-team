# shadcn-vue: Dark Mode

Dark Mode basiert auf der `.dark`-CSS-Klasse am `<html>`-Element. Die Theme-Tokens
in `:root` werden durch `.dark`-Varianten ueberschrieben.

## Reference Files

- `DARK-MODE-VITE.md` — Vite: @vueuse/core useColorMode, optionale Icons
  (@iconify/vue @iconify-json/radix-icons), vollstaendige ModeToggle.vue
  mit DropdownMenu (Light / Dark / System)
- `DARK-MODE-NUXT.md` — Nuxt: @nuxtjs/color-mode Modul, nuxt.config.ts
  (classSuffix: ''), useColorMode composable, vollstaendige ModeToggle.vue
  mit colorMode.preference
- `DARK-MODE-VITEPRESS.md` — Vitepress: @vueuse/core useToggle,
  useData isDark, vollstaendige ModeToggle.vue
- `DARK-MODE-ASTRO.md` — Astro: Inline-Script fuer localStorage/matchMedia,
  useColorMode (@vueuse/core), vollstaendige ModeToggle.vue,
  client:load Direktive
