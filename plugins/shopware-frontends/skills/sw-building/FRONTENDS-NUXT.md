# Shopware Frontends — Nuxt / Vue starter

Production-ready templates are based on **Nuxt 4 / Vue 3 / Vite / Tailwind**. Core of the setup:

1. **Provide the api-client** (Nuxt plugin): instantiate `createAPIClient` with `baseURL` (Store API) + `accessToken`
   (`sw-access-key`) and make it available to composables via `provide`.
2. **Context token SSR-safe** — load/set it per request from the cookie (no shared state between users,
   `sw-frontends-session-context`).
3. **Generate types** (`@shopware/api-gen`, `sw-api-gen-types`), include them as `#shopware`.
4. **Render CMS** via `@shopware/cms-base` (`sw-frontends-cms`); pages/routes via `useNavigation`/`useCms`.

```bash
npx degit shopware/frontends/templates/vue-demo-store my-shop   # or the official starter template
```

Composables (`sw-composables`) and helpers (`sw-frontends-helpers`) build on top of that. Env: `SHOPWARE_ENDPOINT`
(Store API URL) + `SHOPWARE_ACCESS_TOKEN`. Headless deployment: plugin `shopware-devops`.

→ Complete reference: [FRONTENDS-NUXT-NUXT-MODULE-REFERENCE.md](FRONTENDS-NUXT-NUXT-MODULE-REFERENCE.md)
