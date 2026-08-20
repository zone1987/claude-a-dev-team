# Shopware Frontends – Best Practices

Source: `apps/docs/src/best-practices/`

---

## Contents

- [Performance](#performance)
- [Images](#images)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Deployment](#deployment)

## Performance

### Lighthouse checklist (only check against a production build!)

**Performance:**
- Images have an appropriate resolution
- Images in WebP format
- Third-party code is loaded asynchronously
- Images are lazy-loaded
- All custom event listeners are destroyed on unmount

**Accessibility:**
- All images have an `alt` attribute
- Contrast is correct
- `aria-label` on HTML tags

**Best Practices:**
- `https` connection
- Semantic HTML structure

**SEO:**
- `robots.txt` present
- All pages have metadata (title, description)

---

## Images

### Format & compression

**WebP** as the first choice for raster images (full browser support).
Tools: [Squoosh](https://squoosh.app/), [Thumbor](http://thumborize.globo.com/)

**Open-source image processors:**
- [thumbor](https://www.thumbor.org/)
- [lovell/sharp](https://github.com/lovell/sharp)
- [imgproxy](https://github.com/imgproxy/imgproxy)

### CDN + image processor

```html
<img
  src="https://images.swfrontends.com/frontends-unsplash.png?width=400px"
  srcset="
    https://images.swfrontends.com/frontends-unsplash.png?width=400px 320w,
    https://images.swfrontends.com/frontends-unsplash.png?width=800px 720w
  "
/>
```

### Responsive images with srcset

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

### Picture element (multi-format fallback)

```html
<picture>
  <source type="image/avif" srcset="image-320.avif 320w, image-720.avif 720w" />
  <source type="image/webp" srcset="image-320.webp 320w, image-720.webp 720w" />
  <img src="image.png" alt="Logo" />
</picture>
```

### Avoiding Cumulative Layout Shift (CLS)

- Always set `width` and `height` on `<img>`
- CSS override:
  ```css
  img { max-width: 100%; height: auto; }
  ```
- Use a low-quality placeholder (e.g. SVG)

### Optimising Largest Contentful Paint (LCP)

- **NEVER** use `loading="lazy"` on above-the-fold images
- Set `fetchpriority="high"` for the LCP image

---

## Error Handling

Note: The older error-handling documentation is based on the old API client.
Current: use the new `@shopware/api-client` (typesafe, via `invoke`).

---

## Testing

### E2E testing with Playwright

**Page object pattern (best practices):**
- Use `data-testid` selectors
- Unambiguous class names for page objects
- Classes contain only methods for UI interaction
- No assertions at the page-object level
- Page objects can also be small components

**Directory structure:**
```
e2e-tests/
├─ page-objects/   # Page classes
├─ tests/          # Test files
└─ utils/          # Helpers and factories
```

**No hard waits:**
```js
// WRONG
await page.waitFor(1000);

// RIGHT
await page.waitForNavigation();
await page.waitForLoadState();
await page.waitForSelector();
```

**data-testid convention:**
```
data-testid="{scope}-{name}-{type}"
data-testid="header-search-input"
data-testid="login-email-input"
data-testid="login-submit-button"
```

**Example LoginForm page object:**
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

**E2E test example:**
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

**Providers:**
- [AB Tasty](https://www.abtasty.com/)
- [Optimizely](https://www.optimizely.com/)
- [VWO](https://vwo.com/)
- [Split.io](https://www.split.io/)
- [Kameleoon](https://www.kameleoon.com/)
- [PostHog](https://posthog.com/) (free tier available at no cost)

**Best Practices:**

1. Start with a clear hypothesis

2. Dynamic splitting (bundle size):
```ts
const myExperimentFlag = useABTesting("myExperimentFlag");
const MyComponent = myExperimentFlag
  ? import("./MyComponentVariantA")
  : import("./MyComponentVariantB");
```

3. Small components: inline variants
```ts
<button :class="{
  'bg-color-red': myExperimentFlag,
  'bg-color-blue': !myExperimentFlag
}">Click me</button>
```

4. After the test: **clean up the code!** – Remove unused variants.

---

### Accessibility testing with axe-core

**Integration with Playwright:**
```bash
npm install @axe-core/playwright
```

**Full-page scan:**
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

**Partial scan (navigation menu):**
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

Tip: axe-core is also available as a Chrome/Firefox extension.

---

## Deployment

Source: `apps/docs/src/best-practices/deployment.md`

### Hosting options

#### Static hosting (SPA / SSG)

| Mode | Description | Advantages | Disadvantages |
|-------|-------------|----------|-----------|
| **SPA** | Server delivers HTML+JS, browser renders | No Node server required | Slower initial load, API-dependent |
| **SSG** | Pages are generated once at build time | Maximum performance, independent of the API | Every product change requires a rebuild |

**Popular static hosting services:**
- [Vercel](https://vercel.com/)
- [Netlify](https://www.netlify.com/)
- [Amazon S3](https://aws.amazon.com/s3/)

#### Dynamic hosting (SSR)

SSR (server-side rendering) renders pages on the server on every request.
- Better SEO (immediately visible content)
- No cache-invalidation problem
- Requires a Node.js server
- Additional round trip: browser → Node → API → Node → browser

**Popular SSR hosting services:**
- [Vercel](https://vercel.com/)
- [Heroku](https://www.heroku.com/)

### Nitro (Nuxt server engine)

[Nitro](https://github.com/unjs/nitro) is the default server engine of Nuxt 3.
Ready-made deployment presets (almost zero-config):

```
azure          – Azure Static Web Apps / Functions
cloudflare_pages – Cloudflare Pages
netlify        – Netlify Functions
stormkit       – Stormkit
vercel         – Vercel
```

Full list: https://nitro.unjs.io/deploy

### Deployment best practices

1. **Automation:** automate build, tests and releases → fewer human errors
2. **Use CI/CD:** tests, build verification and static analysis before every deployment
3. **Multiple environments:** test different Node versions and dependency states
4. **Deployment checklist:** a clear procedure before every roll-out

### Troubleshooting

#### CORS problems

The Shopware Store API allows cross-origin requests by default. Configuration:

| Header | Default | Description |
|--------|---------|-------------|
| `Access-Control-Allow-Origin` | `*` | Allowed origins |
| `Access-Control-Allow-Methods` | `GET,POST,PUT,PATCH,DELETE` | Allowed HTTP methods |
| `Access-Control-Allow-Headers` | `Content-Type,sw-context-token,...` | Allowed headers |

**Solution options for CORS problems:**

| Solution | CORS-free | Performance | Setup |
|--------|-----------|-------------|-------|
| Reverse proxy (NGINX) | Yes | Fast | Medium |
| Nuxt SSR mode | Yes | Fast | Easy |
| Adjust Shopware API CORS | No | Fast | Easy |
| Custom API middleware | Yes | Slower | Laborious |

**Vite proxy for local development:**
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

#### devStorefrontUrl (customer registration locally)

Shopware's registration endpoint requires a `storefrontUrl` that matches a configured sales channel domain. In local dev this fails.

```ts
// nuxt.config.ts
shopware: {
  endpoint: "https://your-shop.shopware.store/store-api",
  accessToken: "your-access-token",
  devStorefrontUrl: "https://your-shop.shopware.store",  // must be configured in the sales channel domains
},
```

Or via an environment variable:
```bash
NUXT_PUBLIC_SHOPWARE_DEV_STOREFRONT_URL=https://your-shop.shopware.store
```

#### HTTPS for localhost

**Option A: mkcert**
```bash
mkcert localhost
# package.json:
NODE_TLS_REJECT_UNAUTHORIZED=0 nuxt dev --https --ssl-cert localhost.pem --ssl-key localhost-key.pem
```

**Option B: Vite plugin**
```bash
pnpm add -D @vitejs/plugin-basic-ssl
```
```ts
// nuxt.config.ts
devServer: { https: true },
vite: { plugins: [basicSsl()] },
```
