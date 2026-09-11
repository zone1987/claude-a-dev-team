# Playwright end-to-end testing

**Whatever the plugin ships gets an end-to-end test.** Administration work gets
administration tests; storefront work gets storefront tests. This is the only level that
answers "does the shopper see the right thing", and the only one that covers Twig at all.

Built on `@shopware-ag/acceptance-test-suite`, which supplies the shop customer, the API
clients and the test data service. Do not reimplement those.

## The environment: ddev-playwright

The browsers run in a container of their own, provided by the DDEV add-on
**[`zone1987/ddev-playwright`](https://github.com/zone1987/ddev-playwright)**:

```bash
ddev add-on get zone1987/ddev-playwright
ddev restart
```

It adds `.ddev/docker-compose.playwright.yaml` (marked `#ddev-generated`, so do not edit
it by hand) and a `ddev playwright` host command.

What it gives you:

- `mcr.microsoft.com/playwright:v1.60.0-noble` with **the browsers preinstalled** —
  nothing is ever downloaded into the project. Override the tag with
  `ddev dotenv set .ddev/.env --playwright-image-tag v1.57.0-noble`.
- `PLAYWRIGHT_BROWSERS_PATH=/ms-playwright`, which is why `npx playwright install` is
  never needed.
- The project root mounted at `/var/www/html`, so the app is reachable at `http://web`
  and your tests live where you put them.
- UI mode at `https://<site>.ddev.site:8078` and the HTML report at `:9324`, both through
  the DDEV router.

**Pin the Playwright version in `package.json` to the image tag.** A client newer than the
browsers in the image fails in ways that look like test bugs.

### Running it

```bash
ddev playwright test                        # from the directory holding playwright.config.ts
ddev playwright test tests/Foo.spec.ts      # a single spec
ddev playwright --ui                        # UI mode in the browser
ddev playwright codegen https://…           # any CLI subcommand
```

`HostWorkingDir: true` maps the directory you are standing in into the container, so the
command finds the config and `node_modules` wherever the suite lives.

**One caveat:** arguments are forwarded through a shell without re-quoting, so a `--grep`
pattern containing spaces is split. Use a pattern without spaces, or fall back to the
explicit form:

```bash
ddev exec -s playwright bash -c "cd /var/www/html/path/to/Acceptance && npx playwright test --grep 'two words'"
```

**Never `docker exec`.** `ddev exec -s playwright` reaches the same container through DDEV,
and a restart is `ddev restart` — other projects share the Docker daemon.

## Where the files go

```
tests/Acceptance/
├── .env.dist                    template; .env is git-ignored
├── package.json
├── tsconfig.json                path aliases
├── playwright.config.ts
├── global-teardown.ts           → STANDARD-CLEANUP.md
├── README.md
├── fixtures/AcceptanceTest.ts   wires the data service and page objects
├── page-objects/
│   ├── administration/
│   └── storefront/
├── services/YourTestDataService.ts
└── tests/*.spec.ts
```

## package.json

```json
{
    "name": "your-plugin-acceptance",
    "version": "0.1.0",
    "private": true,
    "description": "Acceptance tests of the YourPlugin plugin",
    "type": "module",
    "scripts": {
        "test": "playwright test",
        "test:ui": "playwright test --ui"
    },
    "dependencies": {
        "@shopware-ag/acceptance-test-suite": "12.17.0"
    },
    "devDependencies": {
        "@playwright/test": "1.60.0",
        "@types/node": "20.6.5",
        "dotenv": "16.6.1",
        "typescript": "5.9.3"
    }
}
```

Install inside the container, not on the host:

```bash
ddev exec -s playwright bash -c "cd /var/www/html/<path>/tests/Acceptance && npm install"
```

## tsconfig.json — without it the imports do not resolve

The specs import through aliases (`@fixtures/AcceptanceTest`, `@page-objects/…`), which
only exist because of the `paths` block. Leave it out and nothing compiles:

```json
{
    "compilerOptions": {
        "target": "ES2022",
        "module": "ESNext",
        "moduleResolution": "bundler",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "types": ["node"],
        "baseUrl": ".",
        "paths": {
            "@page-objects/*": ["./page-objects/*"],
            "@fixtures/*": ["./fixtures/*"],
            "@services/*": ["./services/*"]
        }
    },
    "include": ["**/*.ts"]
}
```

Check it before running the suite — a type error here surfaces as a confusing runtime
failure:

```bash
ddev exec -s playwright bash -c "cd /var/www/html/<path>/tests/Acceptance && npx tsc --noEmit"
```

**`strict: true` has a consequence in `playwright.config.ts`:** `process.env['APP_URL']` is
`string | undefined`, so the line that normalises the trailing slash needs the value pinned
first:

```typescript
const appUrl = process.env['APP_URL'] ?? 'https://your-shop.ddev.site';
process.env['APP_URL'] = appUrl.replace(/\/+$/, '') + '/';
```

## playwright.config.ts

```typescript
import { defineConfig, devices } from '@playwright/test';
import path from 'path';
import dotenv from 'dotenv';

// The shop's own .env.test already carries the integration credentials; reading it here
// keeps the secret in one place. A local .env may override it.
const SHOP_ENV = path.resolve('../../../../../.env.test');
const LOCAL_ENV = path.resolve('.env');

dotenv.config({ path: LOCAL_ENV });
dotenv.config({ path: SHOP_ENV });

process.env['APP_URL'] = process.env['APP_URL'] ?? 'https://your-shop.ddev.site';

const missing = ['SHOPWARE_ACCESS_KEY_ID', 'SHOPWARE_SECRET_ACCESS_KEY'].filter(
    (name) => process.env[name] === undefined || process.env[name] === '',
);

if (missing.length > 0) {
    process.stdout.write(`Missing env vars (looked in ${LOCAL_ENV} and ${SHOP_ENV}):\n`);
    process.stdout.write('- ' + missing.join('\n- ') + '\n');
    process.exit(1);
}

process.env['APP_URL'] = process.env['APP_URL'].replace(/\/+$/, '') + '/';
process.env['ADMIN_URL'] = process.env['ADMIN_URL']
    ? process.env['ADMIN_URL'].replace(/\/+$/, '') + '/'
    : process.env['APP_URL'] + 'admin/';

// DDEV and OrbStack serve a self-signed certificate.
const ignoreHTTPSErrors =
    process.env['SHOPWARE_PLAYWRIGHT_IGNORE_HTTPS_ERRORS'] === 'true' ||
    process.env['SHOPWARE_PLAYWRIGHT_IGNORE_HTTPS_ERRORS'] === '1';

export default defineConfig({
    testDir: './tests',
    globalTeardown: './global-teardown.ts',
    fullyParallel: false,
    forbidOnly: Boolean(process.env['CI']),
    retries: process.env['CI'] ? 2 : 0,
    workers: 1,
    reporter: process.env['CI'] ? [['list'], ['junit', { outputFile: 'report.xml' }]] : 'list',
    timeout: 60_000,

    use: {
        baseURL: process.env['APP_URL'],
        trace: 'retain-on-failure',
        screenshot: 'only-on-failure',
        video: 'off',
        ignoreHTTPSErrors,
        // Pin the clock to the server timezone: a test reading a rendered date must not
        // drift with the runner's zone.
        timezoneId: 'UTC',
    },

    projects: [{ name: 'YourPlugin', use: { ...devices['Desktop Chrome'] } }],
});
```

**`workers: 1` and `fullyParallel: false`** are deliberate: the tests share one shop, and
parallel runs corrupt each other's data.

## Credentials — required, and they go in `.env.test`

**Without these the suite exits before the first test.** The config checks for them on
purpose and prints where it looked, rather than failing later with an authentication error
that looks like a test bug.

### Where they belong: `shopware/.env.test`

Not `.env`, not `.env.local`. Tests run in the `test` environment, and that is the file
Symfony reads there. `.env.local` belongs to the development environment and may hold
entirely different values — having the keys in both is how a suite ends up authenticating
as something other than what you configured.

```dotenv
# shopware/.env.test

KERNEL_CLASS='App\Kernel'
DATABASE_URL="mysql://db:db@db:3306/db"

# The admin integration the acceptance suite authenticates with.
SHOPWARE_ACCESS_KEY_ID="SWIA…"
SHOPWARE_SECRET_ACCESS_KEY="…"

# DDEV and OrbStack serve a self-signed certificate; the suite's own README names
# exactly this variable for that case.
SHOPWARE_PLAYWRIGHT_IGNORE_HTTPS_ERRORS=1
```

Optional, and needed as soon as a test drives the administration UI rather than the API:

```dotenv
SHOPWARE_ADMIN_USERNAME="admin"
SHOPWARE_ADMIN_PASSWORD="…"
```

| Variable | Required | What it is |
|---|---|---|
| `SHOPWARE_ACCESS_KEY_ID` | **yes** | admin integration access key, `SWIA…` |
| `SHOPWARE_SECRET_ACCESS_KEY` | **yes** | its secret; shown once, at creation |
| `SHOPWARE_PLAYWRIGHT_IGNORE_HTTPS_ERRORS` | yes, on DDEV | `1` — accepts the self-signed certificate |
| `APP_URL` | no | defaults to the value in `playwright.config.ts` |
| `ADMIN_URL` | no | derived from `APP_URL` + `admin/` |
| `SHOPWARE_ADMIN_USERNAME` | for admin UI tests | an administrator's login |
| `SHOPWARE_ADMIN_PASSWORD` | for admin UI tests | that administrator's password |

**`.env.test` is not committed.** The secret grants full admin API access to the shop.

### Creating the integration

Two ways. The command is faster and prints the secret, which the administration shows only
once:

```bash
ddev exec bin/console integration:create AcceptanceTest --admin
```

```
Integration created:
access key: SWIAQJE0CJAZ…
secret access key: …
```

`--admin` is required: the suite creates and deletes products, shipping methods and sales
channels, which a non-admin integration cannot do.

Check what already exists before making another:

```bash
ddev mysql -uroot -proot db -e \
  "SELECT label, LEFT(access_key, 12) AS key_prefix, admin FROM integration;"
```

**Through the administration instead:** Settings → System → Integrations → *Add
integration*, name it, switch on *Administrator*, save. The secret is displayed once at
that moment — copy it then, because it cannot be read back afterwards. Regenerating it
invalidates the old one.

### The suite reads two files, in this order

```typescript
const SHOP_ENV = path.resolve('../../../../../.env.test');  // the shop's
const LOCAL_ENV = path.resolve('.env');                      // the suite's own

dotenv.config({ path: LOCAL_ENV });
dotenv.config({ path: SHOP_ENV });
```

`dotenv` does not overwrite variables already set, so **the local `.env` wins**. It exists
for overriding a single value while debugging; the shop's `.env.test` is where the keys
live. `.env.dist` beside it documents the shape, and `.env` is git-ignored.

### When it fails

```
Missing env vars (looked in /…/tests/Acceptance/.env and /…/shopware/.env.test):
- SHOPWARE_ACCESS_KEY_ID
- SHOPWARE_SECRET_ACCESS_KEY
```

The config prints both paths deliberately — the usual cause is the keys sitting in `.env`
or `.env.local` instead of `.env.test`.

## Four traps that cost hours

### 1. A fresh sales channel has no compiled theme

The suite creates its own sales channel. A new one has assets but **no `css` or `js`
directory at all**, so there is no storefront JavaScript, the off-canvas cart never opens,
and every test fails in a way that looks like a selector problem.

Compile it in `beforeEach`, through the admin API — no console needed:

```typescript
async compileThemeForSalesChannel(): Promise<void> {
    const salesChannelId = this.defaultSalesChannel.id;

    const assigned = await this.AdminApiClient.get(
        `theme?filter[theme.salesChannels.id]=${salesChannelId}&limit=1`,
    );
    const { data: assignedThemes } = await assigned.json();
    let themeId = assignedThemes?.[0]?.id as string | undefined;

    // A channel the suite has just created may carry no theme at all.
    if (themeId === undefined) {
        const defaults = await this.AdminApiClient.get(
            'theme?filter[theme.technicalName]=Storefront&limit=1',
        );
        const { data: defaultThemes } = await defaults.json();
        themeId = defaultThemes?.[0]?.id as string | undefined;
    }

    expect(themeId, 'the installation has a Storefront theme').toBeTruthy();

    // Assigning compiles it, which is what produces css and js.
    const response = await this.AdminApiClient.post(
        `_action/theme/${themeId}/assign/${salesChannelId}`,
        { data: {} },
    );
    expect(response.ok()).toBeTruthy();
}
```

### 2. The suite's channel is not on the shop's default currency

It has been GBP against a EUR shop. Every asserted amount is then a conversion, and a test
comparing rendered figures is testing an exchange rate. Set it per test and restore it in
`cleanUp()`:

```typescript
async useDefaultCurrency(): Promise<void> {
    if (this.originalCurrencyId === null) {
        this.originalCurrencyId = this.defaultSalesChannel.currencyId ?? null;
    }

    const currencyId = this.defaultCurrencyId;
    const response = await this.AdminApiClient.patch(
        `sales-channel/${this.defaultSalesChannel.id}`,
        { data: { currencyId, currencies: [{ id: currencyId }] } },
    );
    expect(response.ok()).toBeTruthy();
}
```

### 3. The shop decides what a cart is worth

A product created at `40` arrives as a gross cart value of `35.66`, because the suite
treats the number as net. **Read the figure back and assert the plugin's arithmetic against
it**, rather than hard-coding a total that depends on a tax rate:

```typescript
const goods = await Display.goodsValue();          // dd.summary-value.summary-total
const expected = (100 / THRESHOLD) * goods;

expect(await Display.reportedProgress()).toBeCloseTo(expected, 1);
```

### 4. Assigning a shipping method does not change the running session

A session keeps the method it was created with. Post to the route the cart page uses:

```typescript
async useShippingMethod(shippingMethodId: string): Promise<void> {
    await this.page.goto('checkout/cart');

    await this.page.evaluate(async (id: string) => {
        const body = new URLSearchParams();
        body.set('shippingMethodId', id);

        await fetch(window.router['frontend.checkout.configure'], {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: body.toString(),
        });
    }, shippingMethodId);
}
```

**`window.router` only carries the routes the current page needs.** Look the name up on a
page that uses it, or build the URL from the channel base path.

## Filling the cart

Through the storefront's own buy button. A hand-built form post to
`checkout/line-item/add` from `page.evaluate` returns 404 or silently adds nothing:

```typescript
async putInCart(productUrl: string): Promise<void> {
    await this.page.goto(productUrl);
    await this.page.locator('button.btn-buy').first().click();
    await this.page.waitForLoadState('networkidle');
}
```

## Reaching the off-canvas cart

Through its own route, not by clicking it open:

```typescript
url(): string {
    return 'checkout/offcanvas';
}
```

That route is what the storefront's JavaScript calls itself. Driving it directly keeps the
test about the plugin's output rather than about a dialog animation, and removes a
dependency on the off-canvas opening at all.

## Page objects pin the markup

Every selector a theme might rely on belongs in a page object, named so that a change to it
is visible as a change to the contract:

```typescript
export class FreeShippingProgressDisplay implements PageObject {
    public readonly container: Locator;
    public readonly text: Locator;
    public readonly progress: Locator;

    constructor(public readonly page: Page) {
        this.container = page.locator('.up-to-free-shipping');
        this.text = page.locator('#up-to-free-shipping-text');
        this.progress = page.locator('.up-to-free-shipping-progress');
    }

    // PageObject requires it even when the object has no page of its own.
    url(): string {
        return 'checkout/offcanvas';
    }
}
```

## Not part of the gate

They need a running shop with the plugin installed and its storefront built. Run them
before a release, after any change to a template, and after any change to an administration
page.

## Clean-up is mandatory

→ **[STANDARD-CLEANUP.md](STANDARD-CLEANUP.md)**. A suite that leaves data behind is not
finished, however green it is.
