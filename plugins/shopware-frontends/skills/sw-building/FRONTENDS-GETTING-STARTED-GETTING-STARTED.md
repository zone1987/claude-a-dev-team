# Shopware Frontends – Getting Started

Source: official documentation `apps/docs/src/getting-started/` + `src/installation.md` + `src/framework/requirements.md`

---

## Contents

- [Requirements](#requirements)
- [Templates overview](#templates-overview)
- [Try It Out](#try-it-out)
- [Next steps after setup](#next-steps-after-setup)

## Requirements

### Node.js
- **v22.x** LTS (recommended)
- v20.x – maintenance
- v18.x – maintenance

Tip: use `nvm` (Node Version Manager).

### Package manager
- **pnpm** – recommended
- npm (out of the box with Node)
- yarn

### Shopware API
Both cloud instances and self-managed Shopware 6 are supported.
All templates are preconfigured with a public demo API.

### IDE
- VSCode with:
  - `Vue.volar` (Vue Language Features)
  - `biomejs.biome` (code formatter)
  - `vscode.typescript-language-features`
  - `antfu.unocss` (for the Demo Store template)

---

## Templates overview

### 1. Vue Starter Template (RECOMMENDED)

Production-ready Nuxt 4.x foundation without demo boilerplate.

**Contains:**
- Nuxt 4.x with SSR
- `@shopware/api-client`, `@shopware/composables`, `@shopware/helpers`
- `@shopware/cms-base-layer`, `@shopware/unocss-design-tokens-layer`
- `@shopware/nuxt-module`
- UnoCSS (Tailwind-compatible)
- i18n support
- TypeScript + type generation

**Setup:**
```bash
npx tiged shopware/frontends/templates/vue-starter-template my-store && cd my-store
npm i && npm run dev
```

**Live demo:** https://frontends-starter-template.vercel.app/

**Directory structure (Nuxt 4.x with the app/ directory):**
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
│  │  ├─ [...all].vue  # catch-all for CMS pages
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

**Configuration (nuxt.config.ts):**
```ts
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      shopware: {
        endpoint: "https://your-shop.shopware.store/store-api",
        accessToken: "your-access-token",
        // Optional: for customer registration in local dev:
        // devStorefrontUrl: "https://your-shop.shopware.store",
      },
    },
  },
});
```

**Via a .env file:**
```bash
NUXT_PUBLIC_SHOPWARE_ENDPOINT=https://your-shop.shopware.store/store-api
NUXT_PUBLIC_SHOPWARE_ACCESS_TOKEN=your-access-token
```

**Type generation:**
```bash
npm run generate-types
```

**Overriding CMS components:**
```
app/components/SwProductCard.vue  # overrides the base layer component
```

**Local UnoCSS customisation (uno.config.ts):**
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

### 2. Vue Starter Template Extended (Nuxt layers – multi-brand)

Demonstrates the **Nuxt layer pattern** for brand-specific storefronts.
Example: "Lumora" – a fictional home fragrance brand.

**Setup:**
```bash
npx tiged shopware/frontends/templates/vue-starter-template vue-starter-template
npx tiged shopware/frontends/templates/vue-starter-template-extended lumora-store
cd lumora-store
# adjust package.json: workspace:* → file:../vue-starter-template
npm i && npm run dev
```

**nuxt.config.ts of the extended template:**
```ts
export default defineNuxtConfig({
  extends: ["../vue-starter-template"],  // base template
  // Lumora-specific config
})
```

**What is inherited:**
- All pages (navigation, product, checkout, ...)
- All layout components
- Composables and business logic
- CMS integration, i18n, type generation

**What is customised (minimal):**
```
lumora-store/
├─ app/
│  └─ app.config.ts        # brand colors, settings
├─ public/                  # logo, favicon
├─ nuxt.config.ts
├─ uno.config.ts
└─ package.json
```

**Brand color via app.config.ts:**
```ts
export default defineAppConfig({
  imagePlaceholder: {
    color: "#B38A65",  // Lumora brand-primary
  },
});
```

**Advantages:**
- Minimal code duplication
- Automatic updates from the base template
- Multiple brands from a single base
- Clean separation of custom vs. framework

**Update the base template:**
```bash
npm update vue-starter-template
```

**Multi-brand monorepo:**
```
my-monorepo/
├─ vue-starter-template/      # base
├─ lumora-store/              # brand A
├─ another-brand/             # brand B
└─ premium-brand/             # brand C
```

**Live demo:** https://frontends-extended-starter-template.vercel.app/

---

### 3. Blank Template

An empty Nuxt 3 project with the packages preinstalled, no UI/CSS.

```bash
npx tiged shopware/frontends/templates/vue-blank vue-blank && cd vue-blank
npm i && npm run dev
```

Ideal when: you bring your own CSS framework, or build a completely new frontend.

---

### 4. Demo Store Template (DEPRECATED)

**No longer recommended.** Only as a reference implementation. Uses the old patterns without Nuxt layers.

Recommendation: use the Vue Starter Template.

---

### 5. Custom Vue.js project (existing app)

```bash
pnpm add @shopware/composables @shopware/api-client js-cookie
```

**Create the plugin:**
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

**Register the plugin (main.ts):**
```ts
import ShopwareFrontends from "./plugins/vue-shopware-frontends";
app.use(ShopwareFrontends, {
  endpoint: "https://demo-frontends.swstage.store",
  accessToken: "SWSCBHFSNTVMAWNZDNFKSHLAYW",
});
```

**SSR vs. CSR endpoints:**
```
NUXT_SHOPWARE_ENDPOINT=http://shopware        # internal/SSR
NUXT_PUBLIC_SHOPWARE_ENDPOINT=https://...     # external/CSR
```

---

### 6. Custom React project

Prototype based on the Vercel Commerce template:
- React + Next.js (App Router)
- `@shopware/api-client`
- No headless checkout (in development)
- Pages are pre-generated at build time

---

### 7. Astro Template

Blank Astro with Shopware compatibility for Vue components.

```bash
npx tiged shopware/frontends/templates/astro astro-blank && cd astro-blank
npm i && npm run dev
```

**Configuration:**
```bash
# .env.development
API_URL="https://demo-frontends.shopware.store"
API_ACCESS_TOKEN="SWSCBHFSNTVMAWNZDNFKSHLAYW"
```

---

## Try It Out

Templates can be launched directly in the browser:
- StackBlitz (all templates)
- GitHub Codespaces

The dev server runs on port `3000` by default.

---

## Next steps after setup

1. Explore CMS components (Shopping Experiences)
2. Build the routing (SeoUrl resolution)
3. Implement page elements (navigation, product listing)
4. E-commerce features (cart, checkout)
