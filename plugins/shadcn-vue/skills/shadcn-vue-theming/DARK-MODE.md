# shadcn-vue: Dark Mode

Dark mode is based on the `.dark` CSS class on the `<html>` element. The theme tokens
in `:root` are overridden by their `.dark` variants.

## Reference Files

- `DARK-MODE-VITE.md` — Vite: @vueuse/core useColorMode, optional icons
  (@iconify/vue @iconify-json/radix-icons), complete ModeToggle.vue
  with DropdownMenu (Light / Dark / System)
- `DARK-MODE-NUXT.md` — Nuxt: @nuxtjs/color-mode module, nuxt.config.ts
  (classSuffix: ''), useColorMode composable, complete ModeToggle.vue
  with colorMode.preference
- `DARK-MODE-VITEPRESS.md` — Vitepress: @vueuse/core useToggle,
  useData isDark, complete ModeToggle.vue
- `DARK-MODE-ASTRO.md` — Astro: inline script for localStorage/matchMedia,
  useColorMode (@vueuse/core), complete ModeToggle.vue,
  client:load directive
