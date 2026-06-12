# Shopware Frontends – Best Practices

Quelle: `apps/docs/src/best-practices/`

---

## Performance

### Lighthouse-Checkliste (nur auf Production Build prüfen!)

**Performance:**
- Bilder haben angemessene Auflösung
- Bilder im WebP-Format
- Third-Party-Code wird asynchron geladen
- Bilder werden lazy geladen
- Alle Custom-Event-Listener werden beim Unmount zerstört

**Accessibility:**
- Alle Bilder haben `alt`-Attribut
- Kontrast stimmt
- `aria-label` bei HTML-Tags

**Best Practices:**
- `https`-Verbindung
- Semantische HTML-Struktur

**SEO:**
- `robots.txt` vorhanden
- Alle Seiten haben Metadata (title, description)

---

## Bilder (Images)

### Format & Kompression

**WebP** als erste Wahl für Rasterbilder (vollständige Browser-Unterstützung).
Tools: [Squoosh](https://squoosh.app/), [Thumbor](http://thumborize.globo.com/)

**Open-Source Image Processors:**
- [thumbor](https://www.thumbor.org/)
- [lovell/sharp](https://github.com/lovell/sharp)
- [imgproxy](https://github.com/imgproxy/imgproxy)

### CDN + Image Processor

```html
<img
  src="https://images.swfrontends.com/frontends-unsplash.png?width=400px"
  srcset="
    https://images.swfrontends.com/frontends-unsplash.png?width=400px 320w,
    https://images.swfrontends.com/frontends-unsplash.png?width=800px 720w
  "
/>
```

### Responsive Images mit srcset

```html
<img
  sizes="50vw"
  srcset="
    frontends-header-xs.webp  600w,
    frontends-header-md.webp  1200w,
    frontends-header-xl.webp  2000w
  "
  src="frontends-header-xs.webp"
  alt="..."
/>
```

### Picture-Element (Multi-Format-Fallback)

```html
<picture>
  <source type="image/avif" srcset="image-320.avif 320w, image-720.avif 720w" />
  <source type="image/webp" srcset="image-320.webp 320w, image-720.webp 720w" />
  <img src="image.png" alt="Logo" />
</picture>
```

### Cumulative Layout Shift (CLS) vermeiden

- Immer `width` und `height` auf `<img>` setzen
- CSS-Override:
  ```css
  img { max-width: 100%; height: auto; }
  ```
- Low-Quality Placeholder (z.B. SVG) verwenden

### Largest Contentful Paint (LCP) optimieren

- **NIE** `loading="lazy"` auf Above-the-Fold-Bilder
- `fetchpriority="high"` für LCP-Bild setzen

---

## Error Handling

Hinweis: Die ältere Error-Handling-Dokumentation basiert auf dem alten API-Client.
Aktuell: Neuen `@shopware/api-client` verwenden (typesafe, via `invoke`).

---

## Testing

### E2E Testing mit Playwright

**Page Object Pattern (Best Practices):**
- `data-testid`-Selektoren verwenden
- Unzweideutige Klassen-Namen für Page Objects
- Klassen enthalten nur Methoden für UI-Interaktion
- Keine Assertions auf Page-Object-Ebene
- Page Objects können auch kleine Komponenten sein

**Verzeichnisstruktur:**
```
e2e-tests/
├─ page-objects/   # Page-Klassen
├─ tests/          # Testdateien
└─ utils/          # Helpers und Factories
```

**Keine Hard Waits:**
```js
// FALSCH
await page.waitFor(1000);

// RICHTIG
await page.waitForNavigation();
await page.waitForLoadState();
await page.waitForSelector();
```

**data-testid Konvention:**
```
data-testid="{scope}-{name}-{type}"
data-testid="header-search-input"
data-testid="login-email-input"
data-testid="login-submit-button"
```

**Beispiel LoginForm Page Object:**
```js
import { expect, Locator, Page } from "@playwright/test";

export class LoginForm {
  readonly page: Page;
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.locator("[data-testid='login-email-input']");
    this.passwordInput = page.locator("[data-testid='login-password-input']");
    this.submitButton = page.locator("[data-testid='login-submit-button']");
  }

  async login(username: string, password: string) {
    await this.usernameInput.type(username);
    await this.passwordInput.type(password);
    await this.submitButton.click();
  }
}
```

**E2E-Test Beispiel:**
```js
import { test, expect } from "@playwright/test";

test("failed login", async ({ page }) => {
  await page.goto("/");

  await Promise.all([
    page.waitForNavigation(),
    page.click("[data-testid='header-sign-in-link']"),
  ]);

  await page.locator("[data-testid='login-email-input']").fill("test@shopware.com");
  await page.locator("[data-testid='login-password-input']").fill("Password123!@#");

  await Promise.all([await page.click("[data-testid='login-submit-button']")]);

  await expect(
    page.locator("[data-testid='login-errors-container']")
  ).toBeVisible();
});
```

---

### A/B Testing

**Anbieter:**
- [AB Tasty](https://www.abtasty.com/)
- [Optimizely](https://www.optimizely.com/)
- [VWO](https://vwo.com/)
- [Split.io](https://www.split.io/)
- [Kameleoon](https://www.kameleoon.com/)
- [PostHog](https://posthog.com/) (kostenloses Free-Tier)

**Best Practices:**

1. Mit klarer Hypothese beginnen

2. Dynamisches Splitting (Bundle-Size):
```ts
const myExperimentFlag = useABTesting("myExperimentFlag");
const MyComponent = myExperimentFlag
  ? import("./MyComponentVariantA")
  : import("./MyComponentVariantB");
```

3. Kleine Komponenten: Inline-Varianten
```ts
<button :class="{
  'bg-color-red': myExperimentFlag,
  'bg-color-blue': !myExperimentFlag
}">Click me</button>
```

4. Nach dem Test: **Code aufräumen!** – Ungenutzte Varianten entfernen.

---

### Accessibility Testing mit axe-core

**Integration mit Playwright:**
```bash
npm install @axe-core/playwright
```

**Ganzseitiger Scan:**
```js
import { test, expect } from '@playwright/test';
import AxeBuilder from "@axe-core/playwright";

test('Check accessibility violations', async ({ page }) => {
  await page.goto('https://example.com');

  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();

  expect(accessibilityScanResults.violations).toEqual([]);
});
```

**Partieller Scan (Navigation Menu):**
```js
test('navigation menu accessibility', async ({ page }) => {
  await page.goto('https://your-site.com/');
  await page.getByRole('button', { name: 'Navigation Menu' }).click();
  await page.locator('#navigation-menu-flyout').waitFor();

  const accessibilityScanResults = await new AxeBuilder({ page })
    .include('#navigation-menu-flyout')
    .analyze();

  expect(accessibilityScanResults.violations).toEqual([]);
});
```

Tipp: axe-core ist auch als Chrome/Firefox-Extension verfügbar.

---

## Deployment

Quelle: `apps/docs/src/best-practices/deployment.md`

### Hosting-Optionen

#### Static Hosting (SPA / SSG)

| Modus | Beschreibung | Vorteile | Nachteile |
|-------|-------------|----------|-----------|
| **SPA** | Server liefert HTML+JS, Browser rendert | Kein Node-Server nötig | Langsamer Initial-Load, API-abhängig |
| **SSG** | Seiten werden einmalig beim Build generiert | Maximale Performance, API unabhängig | Jede Produktänderung erfordert Rebuild |

**Populäre Static-Hosting-Dienste:**
- [Vercel](https://vercel.com/)
- [Netlify](https://www.netlify.com/)
- [Amazon S3](https://aws.amazon.com/s3/)

#### Dynamic Hosting (SSR)

SSR (Server-Side Rendering) rendert Seiten bei jedem Request auf dem Server.
- Besseres SEO (sofort sichtbarer Inhalt)
- Kein Cache-Invalidierungsproblem
- Erfordert Node.js-Server
- Zusätzlicher Round-Trip: Browser → Node → API → Node → Browser

**Populäre SSR-Hosting-Dienste:**
- [Vercel](https://vercel.com/)
- [Heroku](https://www.heroku.com/)

### Nitro (Nuxt Server-Engine)

[Nitro](https://github.com/unjs/nitro) ist die Standard-Server-Engine von Nuxt 3.
Fertige Deployment-Presets (fast zero-config):

```
azure          – Azure Static Web Apps / Functions
cloudflare_pages – Cloudflare Pages
netlify        – Netlify Functions
stormkit       – Stormkit
vercel         – Vercel
```

Vollständige Liste: https://nitro.unjs.io/deploy

### Deployment Best Practices

1. **Automatisierung:** Build, Tests, Releases automatisieren → weniger menschliche Fehler
2. **CI/CD einsetzen:** Tests, Build-Prüfung und Static-Analysis vor jedem Deployment
3. **Multiple Environments:** Verschiedene Node-Versionen und Dependency-Stände testen
4. **Deployment-Checklist:** Klarer Ablauf vor jedem Roll-out

### Troubleshooting

#### CORS-Probleme

Shopware Store-API erlaubt standardmäßig Cross-Origin-Requests. Konfiguration:

| Header | Default | Beschreibung |
|--------|---------|-------------|
| `Access-Control-Allow-Origin` | `*` | Erlaubte Origins |
| `Access-Control-Allow-Methods` | `GET,POST,PUT,PATCH,DELETE` | Erlaubte HTTP-Methoden |
| `Access-Control-Allow-Headers` | `Content-Type,sw-context-token,...` | Erlaubte Header |

**Lösungsoptionen bei CORS-Problemen:**

| Lösung | CORS-frei | Performance | Setup |
|--------|-----------|-------------|-------|
| Reverse Proxy (NGINX) | Ja | Schnell | Mittel |
| Nuxt SSR Mode | Ja | Schnell | Einfach |
| Shopware API-CORS anpassen | Nein | Schnell | Einfach |
| Custom API Middleware | Ja | Langsamer | Aufwendig |

**Vite-Proxy für lokale Entwicklung:**
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

#### devStorefrontUrl (Kundenregistrierung lokal)

Shopwares Registrierungsendpunkt benötigt eine `storefrontUrl`, die mit einer konfigurierten Sales-Channel-Domain übereinstimmt. Bei lokalem Dev schlägt das fehl.

```ts
// nuxt.config.ts
shopware: {
  endpoint: "https://your-shop.shopware.store/store-api",
  accessToken: "your-access-token",
  devStorefrontUrl: "https://your-shop.shopware.store",  // muss in Sales-Channel-Domains konfiguriert sein
},
```

Oder per Environment-Variable:
```bash
NUXT_PUBLIC_SHOPWARE_DEV_STOREFRONT_URL=https://your-shop.shopware.store
```

#### HTTPS für localhost

**Option A: mkcert**
```bash
mkcert localhost
# package.json:
NODE_TLS_REJECT_UNAUTHORIZED=0 nuxt dev --https --ssl-cert localhost.pem --ssl-key localhost-key.pem
```

**Option B: Vite Plugin**
```bash
pnpm add -D @vitejs/plugin-basic-ssl
```
```ts
// nuxt.config.ts
devServer: { https: true },
vite: { plugins: [basicSsl()] },
```
