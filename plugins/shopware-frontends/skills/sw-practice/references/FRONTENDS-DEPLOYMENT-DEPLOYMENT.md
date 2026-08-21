# Shopware Frontends – Deployment

Source: `apps/docs/src/best-practices/deployment.md`, `src/resources/troubleshooting.md`, `src/resources/troubleshooting/CORS.md`

---

## Contents

- [Deployment strategies](#deployment-strategies)
- [Nitro Presets (Zero-Config Deployment)](#nitro-presets-zero-config-deployment)
- [Deployment checklist (best practices)](#deployment-checklist-best-practices)
- [Local development: HTTPS](#local-development-https)
- [Troubleshooting](#troubleshooting)
- [CORS (Cross-Origin Resource Sharing)](#cors-cross-origin-resource-sharing)
- [SSR endpoint separation (SSR vs. CSR)](#ssr-endpoint-separation-ssr-vs-csr)

## Deployment strategies

### 1. Static Hosting (SPA / SSG)

#### SPA (Single Page Application)
- Server delivers static HTML + JavaScript
- Browser parses JS → page becomes interactive
- API required at runtime for products/categories
- **Disadvantages:** slow first page load, worse for SEO

#### SSG (Server-Side Generation)
- Pages are generated once at build time
- The entire site is delivered as static HTML + JS
- Dynamic operations (cart, account) still call the API
- **Advantages:** best performance, no server required
- **Disadvantages:** pages must be regenerated when products change

**Popular providers:**
- Vercel
- Netlify
- Amazon S3

### 2. Dynamic Hosting (SSR)

- A Node.js server renders every page on demand (SSR)
- The page is delivered as HTML + JS → browser hydrates (SPA)
- **Advantages:** always up-to-date data, best SEO, no rebuild on changes
- **Disadvantages:** additional round trip Node→API→Node

**Network optimisation:** the Node server should be hosted close to the Shopware API.

**Popular providers:**
- Vercel (SSR + Node)
- Heroku

---

## Nitro Presets (Zero-Config Deployment)

Nuxt 3 uses [Nitro](https://nitro.unjs.io/) as its server engine.

**Built-in presets:**
- `azure`
- `cloudflare_pages`
- `netlify`
- `stormkit`
- `vercel`

**All presets:** https://nitro.unjs.io/deploy

---

## Deployment checklist (best practices)

1. **Automate processes** – use CI/CD (GitHub Actions, GitLab CI)
2. **Continuous integration** – run tests, builds and static analysis automatically
3. **Multiple environments** – staging, production, possibly different Node versions
4. **Deployment checklist** – document a clear roll-out flow

---

## Local development: HTTPS

### Option 1: mkcert
```bash
mkcert localhost
# package.json:
"dev": "NODE_TLS_REJECT_UNAUTHORIZED=0 nuxt dev --https --ssl-cert localhost.pem --ssl-key localhost-key.pem"
```

### Option 2: Vite plugin
```bash
pnpm add -D @vitejs/plugin-basic-ssl
```
```ts
// nuxt.config.ts
import basicSsl from '@vitejs/plugin-basic-ssl'
export default defineNuxtConfig({
  devServer: { https: true },
  vite: { plugins: [basicSsl()] },
})
```

---

## Troubleshooting

### 412 Precondition Failed

**Cause:** the `accessToken` is wrong or does not match the `endpoint`.

```ts
// check nuxt.config.ts:
shopware: {
  accessToken: "SWSCBHFSNTVMAWNZDNFKSHLAYW",
  endpoint: "https://demo-frontends.shopware.store/store-api/",
  devStorefrontUrl: "https://demo-frontends.shopware.store",
},
```

---

### devStorefrontUrl – when and why?

**Purpose:** for customer registration in a local environment.

**Problem:** `window.location.origin` (e.g. `http://localhost:3000`) does not match the configured sales channel domain.

**Solution:**
```ts
// nuxt.config.ts
shopware: {
  endpoint: "https://your-shop.shopware.store/store-api",
  accessToken: "your-access-token",
  devStorefrontUrl: "https://your-shop.shopware.store",  // sales channel domain
}
```

Or via `.env`:
```bash
NUXT_PUBLIC_SHOPWARE_DEV_STOREFRONT_URL=https://your-shop.shopware.store
```

---

### SSR + DDEV + 500 errors

**Problem:** 500 errors with DDEV + SSR=true  
**Solution:** SSL certificate problem – set in `.env`:
```
NODE_TLS_REJECT_UNAUTHORIZED=0
```

---

### SalesChannel type for Composable Frontends

**Correct:** **Storefront SalesChannel** (not Headless)  
Reason: SEO URLs are only generated for storefront sales channels.

---

### Securing the access token in production

Default: the public token is visible in the frontend.
Options:
1. Use proxy requests (community module `store-api-proxy`)
2. Configure Nuxt server middleware as a proxy

---

### `[unimport] failed to find "createShopwareContext"`

**Problem:** `@shopware/composables/nuxt-layer` is missing from `extends`.

**Solution:**
```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: [
    "@shopware/composables/nuxt-layer",  // MANDATORY
    "@shopware/cms-base-layer",
    "@shopware/unocss-design-tokens-layer"
  ],
  modules: ["@shopware/nuxt-module"],
})
```

---

## CORS (Cross-Origin Resource Sharing)

### Shopware 6 default CORS configuration

| Header | Default | Description |
|---|---|---|
| `Access-Control-Allow-Origin` | `*` | All origins allowed |
| `Access-Control-Allow-Methods` | `GET,POST,PUT,PATCH,DELETE` | |
| `Access-Control-Allow-Headers` | `Content-Type,Authorization,sw-context-token,sw-access-key,...` | |

Shopware 6 allows cross-origin requests by default.

### Solving CORS problems

| Solution | CORS-free? | Performance | Effort | When? |
|---|---|---|---|---|
| **Reverse proxy (NGINX)** | Yes | Very fast | Medium | Self-hosted, best performance |
| **Nuxt SSR mode** | Yes | Fast | Easy | APIs without CORS settings |
| **Modify Shopware CORS** | No | Fast | Easy | When you control the API |
| **Custom API middleware** | Yes | Slower | Hard | When CORS cannot be changed |

### Nuxt proxy configuration

```ts
// nuxt.config.ts
vite: {
  server: {
    proxy: {
      "/store-api": {
        target: "<backend-url>",
        changeOrigin: true,
        secure: false,
      },
    },
  },
},
```

Then point the Shopware endpoint at the local frontend:
```ts
shopware: {
  endpoint: "<frontends-url>/store-api/",
}
```

### Broadcasting & BFCache incompatibility

Broadcasting and BFCache (back-forward cache) are incompatible.
Default: broadcasting **disabled**.

```ts
// nuxt.config.ts
runtimeConfig: {
  broadcasting: true,  // BFCache is then no longer active!
}
```

---

## SSR endpoint separation (SSR vs. CSR)

When the frontend uses a different endpoint internally (SSR) than externally (CSR):

```bash
NUXT_SHOPWARE_ENDPOINT=http://shopware              # internal/SSR
NUXT_PUBLIC_SHOPWARE_ENDPOINT=https://demo.shop.com # external/CSR
```
