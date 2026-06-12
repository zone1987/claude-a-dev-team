# Shopware Frontends – Getting Started

Quelle: offizielle Dokumentation `apps/docs/src/getting-started/` + `src/installation.md` + `src/framework/requirements.md`

---

## Anforderungen (Requirements)

### Node.js
- **v22.x** LTS (empfohlen)
- v20.x – maintenance
- v18.x – maintenance

Tipp: `nvm` (Node Version Manager) verwenden.

### Package Manager
- **pnpm** – empfohlen
- npm (out of the box mit Node)
- yarn

### Shopware API
Sowohl Cloud-Instanzen als auch self-managed Shopware 6 werden unterstützt.
Alle Templates sind mit einer öffentlichen Demo-API vorkonfiguriert.

### IDE
- VSCode mit:
  - `Vue.volar` (Vue Language Features)
  - `biomejs.biome` (Code Formatter)
  - `vscode.typescript-language-features`
  - `antfu.unocss` (für Demo Store Template)

---

## Templates-Übersicht

### 1. Vue Starter Template (EMPFOHLEN)

Produktionsreifes Nuxt-4.x-Fundament ohne Demo-Boilerplate.

**Enthält:**
- Nuxt 4.x mit SSR
- `@shopware/api-client`, `@shopware/composables`, `@shopware/helpers`
- `@shopware/cms-base-layer`, `@shopware/unocss-design-tokens-layer`
- `@shopware/nuxt-module`
- UnoCSS (Tailwind-kompatibel)
- i18n-Support
- TypeScript + Type-Generation

**Setup:**
```bash
npx tiged shopware/frontends/templates/vue-starter-template my-store && cd my-store
npm i && npm run dev
```

**Live Demo:** https://frontends-starter-template.vercel.app/

**Verzeichnisstruktur (Nuxt 4.x mit app/ Directory):**
```
my-store/
├─ app/
│  ├─ components/
│  │  ├─ layout/       # header, footer, account menu
│  │  ├─ checkout/     # cart items, cart overview
│  │  ├─ account/      # order history, account settings
│  │  ├─ product/      # product components
│  │  ├─ form/         # form components
│  │  ├─ shared/       # modals, notifications
│  ├─ composables/     # auto-imported composables
│  ├─ layouts/
│  │  ├─ checkout.vue  # minimal layout
│  │  ├─ default.vue   # default layout
│  ├─ pages/
│  │  ├─ checkout/
│  │  ├─ account/
│  │  ├─ [...all].vue  # catch-all für CMS-Seiten
│  ├─ utils/
│  ├─ app.config.ts
│  ├─ app.vue
├─ i18n/
├─ public/
├─ server/
├─ nuxt.config.ts
├─ package.json
├─ tsconfig.json
```

**Konfiguration (nuxt.config.ts):**
```ts
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      shopware: {
        endpoint: "https://your-shop.shopware.store/store-api",
        accessToken: "your-access-token",
        // Optional: für customer registration in local dev:
        // devStorefrontUrl: "https://your-shop.shopware.store",
      },
    },
  },
});
```

**Per .env-Datei:**
```bash
NUXT_PUBLIC_SHOPWARE_ENDPOINT=https://your-shop.shopware.store/store-api
NUXT_PUBLIC_SHOPWARE_ACCESS_TOKEN=your-access-token
```

**Type Generation:**
```bash
npm run generate-types
```

**CMS-Komponenten überschreiben:**
```
app/components/SwProductCard.vue  # überschreibt Base-Layer-Komponente
```

**UnoCSS lokale Anpassung (uno.config.ts):**
```ts
import { mergeConfigs } from '@unocss/core'
import baseConfig from './.nuxt/uno.config.mjs'

export default mergeConfigs([baseConfig, {
  theme: {
    colors: {
      'brand-primary': '#your-brand-color',
    },
  },
}])
```

---

### 2. Vue Starter Template Extended (Nuxt Layers – Multi-Brand)

Demonstriert das **Nuxt-Layer-Pattern** für markenspezifische Storefronts.
Beispiel: "Lumora" – fiktive Heimdüfte-Marke.

**Setup:**
```bash
npx tiged shopware/frontends/templates/vue-starter-template vue-starter-template
npx tiged shopware/frontends/templates/vue-starter-template-extended lumora-store
cd lumora-store
# package.json anpassen: workspace:* → file:../vue-starter-template
npm i && npm run dev
```

**nuxt.config.ts des Extended-Templates:**
```ts
export default defineNuxtConfig({
  extends: ["../vue-starter-template"],  // Base-Template
  // Lumora-spezifische Config
})
```

**Was geerbt wird:**
- Alle Seiten (Navigation, Produkt, Checkout, ...)
- Alle Layout-Komponenten
- Composables und Business Logic
- CMS-Integration, i18n, Type-Generation

**Was angepasst wird (minimal):**
```
lumora-store/
├─ app/
│  └─ app.config.ts        # Brand-Farben, Settings
├─ public/                  # Logo, Favicon
├─ nuxt.config.ts
├─ uno.config.ts
└─ package.json
```

**Brand-Farbe per app.config.ts:**
```ts
export default defineAppConfig({
  imagePlaceholder: {
    color: "#B38A65",  // Lumora brand-primary
  },
});
```

**Vorteile:**
- Minimale Code-Duplizierung
- Automatische Updates vom Base-Template
- Mehrere Marken aus einer Basis
- Saubere Trennung Custom vs. Framework

**Update Base-Template:**
```bash
npm update vue-starter-template
```

**Multi-Brand Monorepo:**
```
my-monorepo/
├─ vue-starter-template/      # Base
├─ lumora-store/              # Brand A
├─ another-brand/             # Brand B
└─ premium-brand/             # Brand C
```

**Live Demo:** https://frontends-extended-starter-template.vercel.app/

---

### 3. Blank Template

Leeres Nuxt-3-Projekt mit vorinstallierten Paketen, kein UI/CSS.

```bash
npx tiged shopware/frontends/templates/vue-blank vue-blank && cd vue-blank
npm i && npm run dev
```

Ideal wenn: eigenes CSS-Framework, komplett neues Frontend.

---

### 4. Demo Store Template (DEPRECATED)

**Nicht mehr empfohlen.** Nur als Referenzimplementierung. Verwendet die alten Patterns ohne Nuxt-Layers.

Empfehlung: Vue Starter Template verwenden.

---

### 5. Custom Vue.js Project (bestehende App)

```bash
pnpm add @shopware/composables @shopware/api-client js-cookie
```

**Plugin erstellen:**
```ts
// plugins/vue-shopware-frontends.ts
import { ref } from "vue";
import type { App } from "vue";
import { createAPIClient } from "@shopware/api-client";
import { createShopwareContext } from "@shopware/composables";
import Cookies from "js-cookie";

export type ShopwareFrontendsOptions = {
  endpoint: string;
  accessToken: string;
  shopwareApiClient?: { timeout: number };
  enableDevtools?: boolean;
};

export default {
  install: (app: App, options: ShopwareFrontendsOptions) => {
    const cookieContextToken = Cookies.get("sw-context-token");
    const cookieLanguageId = Cookies.get("sw-language-id");

    const contextToken = ref(cookieContextToken);
    const languageId = ref(cookieLanguageId);

    const apiClient = createAPIClient<operations>({
      baseURL: options.endpoint,
      accessToken: options.accessToken,
      contextToken: contextToken.value,
    });

    apiClient.onConfigChange(({ config }) => {
      Cookies.set("sw-context-token", config.contextToken || "", {
        expires: 365, sameSite: "Lax", path: "/",
      });
      Cookies.set("sw-language-id", config.languageId || "", {
        expires: 365, sameSite: "Lax", path: "/",
      });
      contextToken.value = config.contextToken;
      languageId.value = config.languageId;
    });

    const shopwareContext = createShopwareContext(app, {
      enableDevtools: !!options.enableDevtools,
    });

    app.provide("apiClient", apiClient);
    app.provide("shopware", shopwareContext);
    app.provide("swSessionContext", ref());
  },
};
```

**Plugin registrieren (main.ts):**
```ts
import ShopwareFrontends from "./plugins/vue-shopware-frontends";
app.use(ShopwareFrontends, {
  endpoint: "https://demo-frontends.swstage.store",
  accessToken: "SWSCBHFSNTVMAWNZDNFKSHLAYW",
});
```

**SSR vs. CSR Endpoints:**
```
NUXT_SHOPWARE_ENDPOINT=http://shopware        # intern/SSR
NUXT_PUBLIC_SHOPWARE_ENDPOINT=https://...     # extern/CSR
```

---

### 6. Custom React Project

Prototyp basierend auf Vercel Commerce Template:
- React + Next.js (App Router)
- `@shopware/api-client`
- Kein headless Checkout (in Entwicklung)
- Seiten werden zur Build-Zeit pre-generated

---

### 7. Astro Template

Blank Astro mit Shopware-Kompatibilität für Vue-Komponenten.

```bash
npx tiged shopware/frontends/templates/astro astro-blank && cd astro-blank
npm i && npm run dev
```

**Konfiguration:**
```bash
# .env.development
API_URL="https://demo-frontends.shopware.store"
API_ACCESS_TOKEN="SWSCBHFSNTVMAWNZDNFKSHLAYW"
```

---

## Try It Out

Templates können direkt im Browser gestartet werden:
- StackBlitz (alle Templates)
- GitHub Codespaces

Dev-Server läuft standardmäßig auf Port `3000`.

---

## Nächste Schritte nach Setup

1. CMS-Komponenten erkunden (Shopping Experiences)
2. Routing aufbauen (SeoUrl-Auflösung)
3. Page-Elements implementieren (Navigation, Produktlisting)
4. E-Commerce-Features (Cart, Checkout)
