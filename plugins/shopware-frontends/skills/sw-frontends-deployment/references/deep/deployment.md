# Shopware Frontends – Deployment

Quelle: `apps/docs/src/best-practices/deployment.md`, `src/resources/troubleshooting.md`, `src/resources/troubleshooting/CORS.md`

---

## Deployment-Strategien

### 1. Static Hosting (SPA / SSG)

#### SPA (Single Page Application)
- Server liefert statisches HTML + JavaScript
- Browser parst JS → Seite wird interaktiv
- API zur Laufzeit für Produkte/Kategorien nötig
- **Nachteile:** Langsame erste Seitenladung, schlechter für SEO

#### SSG (Server-Side Generation)
- Seiten werden einmalig zur Build-Zeit generiert
- Gesamte Site als statisches HTML + JS ausgeliefert
- Dynamische Operationen (Cart, Account) rufen API weiterhin auf
- **Vorteile:** Beste Performance, kein Server nötig
- **Nachteile:** Seiten müssen bei Produktänderungen neu generiert werden

**Beliebte Anbieter:**
- Vercel
- Netlify
- Amazon S3

### 2. Dynamic Hosting (SSR)

- Node.js-Server rendert jede Seite on-demand (SSR)
- Seite wird als HTML + JS geliefert → Browser hydratisiert (SPA)
- **Vorteile:** Immer aktuelle Daten, bestes SEO, kein Re-Build bei Änderungen
- **Nachteile:** Zusätzlicher Round-Trip Node→API→Node

**Netzwerk-Optimierung:** Node-Server sollte nah an der Shopware-API gehostet werden.

**Beliebte Anbieter:**
- Vercel (SSR + Node)
- Heroku

---

## Nitro Presets (Zero-Config Deployment)

Nuxt 3 verwendet [Nitro](https://nitro.unjs.io/) als Server-Engine.

**Built-in Presets:**
- `azure`
- `cloudflare_pages`
- `netlify`
- `stormkit`
- `vercel`

**Alle Presets:** https://nitro.unjs.io/deploy

---

## Deployment-Checkliste (Best Practices)

1. **Prozesse automatisieren** – CI/CD nutzen (GitHub Actions, GitLab CI)
2. **Continuous Integration** – Tests, Builds, statische Analyse automatisch ausführen
3. **Mehrere Environments** – Staging, Production, ggf. verschiedene Node-Versionen
4. **Deployment-Checkliste** – Klarer Roll-out-Flow dokumentieren

---

## Lokale Entwicklung: HTTPS

### Option 1: mkcert
```bash
mkcert localhost
# package.json:
"dev": "NODE_TLS_REJECT_UNAUTHORIZED=0 nuxt dev --https --ssl-cert localhost.pem --ssl-key localhost-key.pem"
```

### Option 2: Vite Plugin
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

**Ursache:** `accessToken` ist falsch oder passt nicht zum `endpoint`.

```ts
// nuxt.config.ts prüfen:
shopware: {
  accessToken: "SWSCBHFSNTVMAWNZDNFKSHLAYW",
  endpoint: "https://demo-frontends.shopware.store/store-api/",
  devStorefrontUrl: "https://demo-frontends.shopware.store",
},
```

---

### devStorefrontUrl – Wann und warum?

**Zweck:** Für Kunden-Registrierung im lokalen Umfeld.

**Problem:** `window.location.origin` (z.B. `http://localhost:3000`) stimmt nicht mit der konfigurierten Sales-Channel-Domain überein.

**Lösung:**
```ts
// nuxt.config.ts
shopware: {
  endpoint: "https://your-shop.shopware.store/store-api",
  accessToken: "your-access-token",
  devStorefrontUrl: "https://your-shop.shopware.store",  // Sales-Channel-Domain
}
```

Oder per `.env`:
```bash
NUXT_PUBLIC_SHOPWARE_DEV_STOREFRONT_URL=https://your-shop.shopware.store
```

---

### SSR + DDEV + 500-Fehler

**Problem:** 500-Fehler mit DDEV + SSR=true  
**Lösung:** SSL-Zertifikats-Problem – `.env` setzen:
```
NODE_TLS_REJECT_UNAUTHORIZED=0
```

---

### SalesChannel-Typ für Composable Frontends

**Richtig:** **Storefront SalesChannel** (nicht Headless)  
Grund: SEO-URLs werden nur für Storefront-SalesChannels generiert.

---

### Access Token in Production sichern

Default: öffentliches Token im Frontend sichtbar.
Optionen:
1. Proxy-Requests nutzen (Community Module `store-api-proxy`)
2. Nuxt-Server-Middleware als Proxy konfigurieren

---

### `[unimport] failed to find "createShopwareContext"`

**Problem:** `@shopware/composables/nuxt-layer` fehlt in `extends`.

**Lösung:**
```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: [
    "@shopware/composables/nuxt-layer",  // PFLICHT
    "@shopware/cms-base-layer",
    "@shopware/unocss-design-tokens-layer"
  ],
  modules: ["@shopware/nuxt-module"],
})
```

---

## CORS (Cross-Origin Resource Sharing)

### Shopware 6 Standard-CORS-Konfiguration

| Header | Default | Beschreibung |
|---|---|---|
| `Access-Control-Allow-Origin` | `*` | Alle Origins erlaubt |
| `Access-Control-Allow-Methods` | `GET,POST,PUT,PATCH,DELETE` | |
| `Access-Control-Allow-Headers` | `Content-Type,Authorization,sw-context-token,sw-access-key,...` | |

Shopware 6 erlaubt standardmäßig Cross-Origin-Requests.

### CORS-Probleme lösen

| Lösung | CORS-frei? | Performance | Aufwand | Wann? |
|---|---|---|---|---|
| **Reverse Proxy (NGINX)** | Ja | Sehr schnell | Mittel | Self-hosted, beste Performance |
| **Nuxt SSR Mode** | Ja | Schnell | Einfach | APIs ohne CORS-Einstellungen |
| **Shopware CORS modifizieren** | Nein | Schnell | Einfach | Wenn API-Kontrolle vorhanden |
| **Custom API Middleware** | Ja | Langsamer | Schwer | Wenn CORS nicht geändert werden kann |

### Nuxt Proxy-Konfiguration

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

Dann Shopware-Endpoint auf lokales Frontend zeigen:
```ts
shopware: {
  endpoint: "<frontends-url>/store-api/",
}
```

### Broadcasting & BFCache-Inkompatibilität

Broadcasting und BFCache (Back-Forward Cache) sind inkompatibel.
Default: Broadcasting **deaktiviert**.

```ts
// nuxt.config.ts
runtimeConfig: {
  broadcasting: true,  // BFCache dann nicht mehr aktiv!
}
```

---

## SSR-Endpunkt-Trennung (SSR vs. CSR)

Wenn Frontend intern (SSR) einen anderen Endpoint nutzt als extern (CSR):

```bash
NUXT_SHOPWARE_ENDPOINT=http://shopware              # intern/SSR
NUXT_PUBLIC_SHOPWARE_ENDPOINT=https://demo.shop.com # extern/CSR
```
