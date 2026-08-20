# Shopware Frontends — Nuxt / Vue-Starter

Produktionsreife Templates basieren auf **Nuxt 4 / Vue 3 / Vite / Tailwind**. Setup-Kern:

1. **api-client bereitstellen** (Nuxt-Plugin): `createAPIClient` mit `baseURL` (Store-API) + `accessToken`
   (`sw-access-key`) instanziieren und via `provide` für Composables verfügbar machen.
2. **Context-Token SSR-sicher** pro Request aus Cookie laden/setzen (kein geteilter State zwischen Nutzern,
   `sw-frontends-session-context`).
3. **Typen** generieren (`@shopware/api-gen`, `sw-api-gen-types`), als `#shopware` einbinden.
4. **CMS** über `@shopware/cms-base` rendern (`sw-frontends-cms`); Seiten/Routen via `useNavigation`/`useCms`.

```bash
npx degit shopware/frontends/templates/vue-demo-store my-shop   # bzw. offizielles Starter-Template
```

Composables (`sw-composables`) und Helpers (`sw-frontends-helpers`) bauen darauf auf. Env: `SHOPWARE_ENDPOINT`
(Store-API-URL) + `SHOPWARE_ACCESS_TOKEN`. Deployment headless: Plugin `shopware-devops`.

→ Vollständige Referenz: [FRONTENDS-NUXT-NUXT-MODULE-REFERENCE.md](FRONTENDS-NUXT-NUXT-MODULE-REFERENCE.md)
