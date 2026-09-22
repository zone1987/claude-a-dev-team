# Playwright end-to-end testing

**Location:** `tests/E2E/` inside the plugin.

**Whatever the plugin ships gets an end-to-end test.** Administration work gets
administration tests; storefront work gets storefront tests. This is the only level that
uses a real browser against a running shop with real clicks, the only one that answers
"does the shopper see the right thing", and the only one that covers Twig at all.

Built on `@shopware-ag/acceptance-test-suite`, which supplies the shop customer, the API
clients and the test data service. Do not reimplement those.

## The governing principle: an end-to-end test does what a person does

It clicks, types, pages and reads what is on the screen. **It does not call an API to
check a result.**

**The one exception is establishing the starting position.** From the comment on the real
fixture:

```
Scaffolding, not testing.

A merchant checking their listing already has a catalogue; clicking 200 products in by
hand would test the product form rather than this plugin. Building that catalogue may
therefore go through the admin api, and everything the tests then *check* goes through
the interface a person uses.
```

**The dividing line:** creating test data may go through the Admin API. Everything that is
afterwards *checked* goes through the interface.

Recorded as an ADR: *"An end-to-end test does what a person does."*

## Where the files go

```
tests/E2E/
├── .env                          optional, git-ignored; a developer's own overrides
├── package.json
├── tsconfig.json                 path aliases
├── playwright.config.ts
├── README.md
├── fixtures/
│   ├── administration.ts         login, navigation, form handling
│   ├── plugin-data.ts            creating the plugin's own records
│   ├── listing-page.ts           storefront listing: counting, paging, reading off
│   └── shop-data.ts              categories, products, media
├── page-objects/
│   ├── administration/
│   └── storefront/
├── services/YourTestDataService.ts
└── tests/*.spec.ts
```

**The pattern is page object.** Each file encapsulates one area, so the spec files read
like a description of the procedure rather than a sequence of selectors.

## `playwright.config.ts`, complete

```ts
import { defineConfig, devices } from '@playwright/test';
import { existsSync } from 'node:fs';
import path from 'node:path';

// Node >= 20.12 brings process.loadEnvFile, so no dotenv dependency is needed.
// A developer who has just checked the plugin out has no .env of their own, so the
// shop's own is read as well: everything these tests need is already in there.
[
    path.join(__dirname, '.env'),
    path.join(__dirname, '../../../../../.env.local'),
    path.join(__dirname, '../../../../../.env'),
].forEach((file) => {
    if (existsSync(file)) {
        process.loadEnvFile(file);
    }
});

const token = process.env.BROWSERLESS_TOKEN;
if (!token) {
    throw new Error(
        'BROWSERLESS_TOKEN is not set. These tests run inside the DDEV web container against a\n' +
            'Chromium in its own container, which has to be started on the host first:\n' +
            '  ddev browserless on\n' +
            '  ddev exec -d /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME>/tests/E2E \\\n' +
            '      npx playwright test',
    );
}

// The acceptance test suite concatenates "api/..." onto APP_URL without a separator, so a
// missing trailing slash turns into https://<host>api/oauth/token.
const appUrl = (process.env.APP_URL ?? process.env.DDEV_PRIMARY_URL ?? '').replace(/\/*$/, '/');
process.env.APP_URL = appUrl;

export default defineConfig({
    testDir: './tests',
    outputDir: './test-results',
    // Every test builds its own category and its own records through the
    // administration, and two of them running at once would each see the other's rows in
    // the listing they are counting. Correctness beats wall-clock here.
    fullyParallel: false,
    workers: 1,
    forbidOnly: !!process.env.CI,
    retries: 0,
    // A page that shows 200 products over nine pages is walked click by click, and the
    // administration is not fast. The default 30 seconds is not enough for one of these.
    timeout: 300_000,
    expect: { timeout: 15_000 },
    reporter: [
        ['list'],
        ['html', { outputFolder: './playwright-report', open: 'never' }],
    ],
    use: {
        baseURL: appUrl,
        // The browserless container does not trust DDEV's mkcert CA, and plain http is no
        // way out: the router sends HSTS, so Chromium upgrades back to https on its own.
        ignoreHTTPSErrors: true,
        trace: 'retain-on-failure',
        screenshot: 'only-on-failure',
        video: 'off',
        actionTimeout: 30_000,
        navigationTimeout: 60_000,
        // Pin the clock to the server timezone: a test reading a rendered date must not
        // drift with the runner's zone.
        timezoneId: 'UTC',
        // The dedicated Playwright endpoint, not the CDP one at /chromium.
        connectOptions: {
            wsEndpoint: `ws://browserless:3000/chromium/playwright?token=${token}`,
            timeout: 60_000,
        },
    },
    projects: [
        {
            name: 'chromium',
            use: { ...devices['Desktop Chrome'], viewport: { width: 1600, height: 1000 } },
        },
    ],
});
```

## The decisions in it

### Three `.env` files, in this order

```
tests/E2E/.env          # the developer's own values, if any
shopware/.env.local     # the shop's credentials
shopware/.env           # the defaults
```

`process.loadEnvFile` has existed since Node 20.12 — **no `dotenv` dependency is needed**.
Whoever has just checked the plugin out owns no `.env` of their own; everything required
is already in the shop's.

**The credentials belong in `shopware/.env.local`**, which is where every other tool in
this working method reads them from. They are not committed: the secret grants full admin
API access to the shop.

| Variable | Required | What it is |
|---|---|---|
| `BROWSERLESS_TOKEN` | **yes** | written by the browserless add-on; the config aborts without it |
| `APP_URL` | no | falls back to `DDEV_PRIMARY_URL` |
| `SHOPWARE_ACCESS_KEY_ID` | for admin API scaffolding | admin integration access key, `SWIA…` |
| `SHOPWARE_SECRET_ACCESS_KEY` | for admin API scaffolding | its secret; shown once, at creation |
| `SHOPWARE_ADMIN_USERNAME` | for administration tests | an administrator's login |
| `SHOPWARE_ADMIN_PASSWORD` | for administration tests | that administrator's password |

### A hard abort when the token is missing

The `throw` carries the full instructions deliberately. The alternative is a connection
error deep inside Playwright that says nothing about a container needing to be started.

### The missing slash in `APP_URL`

```ts
const appUrl = (process.env.APP_URL ?? process.env.DDEV_PRIMARY_URL ?? '').replace(/\/*$/, '/');
```

`@shopware-ag/acceptance-test-suite` appends `"api/..."` to `APP_URL` **without a
separator**. Without the trailing slash the result is `https://<host>api/oauth/token` — an
address that does not exist, and the failure looks like an authentication problem.

### `workers: 1` and `fullyParallel: false`

Every test builds its own category and its own records. Two running at once would see each
other's rows in the listing they are counting. Correctness beats runtime.

### `retries: 0`

A test that only passes on the second attempt is not passing. Retries hide exactly the
timing defects this level exists to find.

### `timeout: 300_000`

Five minutes per test. A test that clicks through 200 products over nine pages needs it.
The default of 30 seconds is enough for none of them.

### `ignoreHTTPSErrors: true`

The browserless container does not know DDEV's mkcert CA. Plain `http` is no way out: the
router sends HSTS, and Chromium upgrades back to `https` by itself.

### `timezoneId: 'UTC'`

A test that reads a rendered date must not drift with the runner's zone. Pinning the clock
to the server timezone is what makes a date assertion mean the same thing on every
machine.

### `trace: 'retain-on-failure'`

The recording is kept only for a failure. It contains every step, every DOM state and
every network call, and is by a distance the most useful debugging tool available:

```bash
npx playwright show-trace tests/E2E/test-results/<test>/trace.zip
```

## `package.json` of the E2E suite

```json
{
    "name": "<NPM-NAME>-e2e",
    "version": "4.1.0",
    "private": true,
    "description": "End-to-end tests of the <PLUGIN-NAME> plugin, driven through browserless",
    "scripts": {
        "test": "playwright test",
        "test:headed": "playwright test --headed",
        "report": "playwright show-report playwright-report",
        "typecheck": "tsc --noEmit"
    },
    "devDependencies": {
        "@playwright/test": "1.62.1",
        "@shopware-ag/acceptance-test-suite": "12.19.0",
        "@types/node": "24.13.3",
        "playwright-core": "1.62.1",
        "typescript": "5.9.3"
    }
}
```

**`@shopware-ag/acceptance-test-suite`** brings the login, the API context and helpers for
Shopware test data. **`typecheck` belongs in the list** because the specs are TypeScript
and a type error would otherwise only surface at runtime.

## `tsconfig.json` — without it the imports do not resolve

The specs import through aliases (`@fixtures/…`, `@page-objects/…`), which only exist
because of the `paths` block. Leave it out and nothing compiles:

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
ddev exec -d /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME>/tests/E2E \
    npm run typecheck
```

**`strict: true` has a consequence:** `process.env.APP_URL` is `string | undefined`, which
is why the config pins the value into a local constant before normalising the trailing
slash rather than operating on `process.env` directly.

## Running it

```bash
ddev browserless on
ddev exec -d /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME>/tests/E2E \
    npx playwright test
```

`-d` sets the working directory **inside the container**. The report afterwards:

```bash
npx playwright show-report tests/E2E/playwright-report
```

Install dependencies the same way — inside the container, not on the host:

```bash
ddev exec -d /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME>/tests/E2E npm install
```

**Never `docker exec`.** `ddev exec` reaches the same container through DDEV, and a restart
is `ddev restart` — other projects share the Docker daemon.

## Test data: a prefix, and quantities that are argued for

**Everything the suite writes carries a prefix**, so the clean-up can find it again:

```ts
/** Everything this suite writes carries it, so the clean-up can find it again. */
export const TEST_PREFIX = 'Test-FFLI';
```

**The quantities are argued for, not guessed.** A number in a fixture is a claim about
what the test proves, and it is written down as such:

```ts
/**
 * The listing shows 24 products per page by default, and the pagination defect lived in
 * the arithmetic across many pages. 200 products is nine pages: enough to place
 * records early, in the middle and late, and to prove the cumulative offset over
 * eight page turns.
 */
export const PRODUCT_COUNT = 200;
```

A count picked at random proves nothing in particular; a count derived from the page size
and the defect under test proves exactly the thing it was chosen for.

## Clean-up and counting

**There is no transaction.** Unlike an integration test, everything an E2E test writes
stays behind. So it is cleaned up by hand — through the Sync API, in one go:

```ts
[`delete-${entity}`]: { entity: entity.replace(/-/g, '_'), action: 'delete', payload: ids },
```

**The proof is a count, not an assertion of good intent.** Before and after the run:

```bash
ddev mysql -uroot -proot db -e "SELECT
  (SELECT COUNT(*) FROM product_translation  WHERE name LIKE 'Test-%') AS products,
  (SELECT COUNT(*) FROM category_translation WHERE name LIKE 'Test-%') AS categories,
  (SELECT COUNT(*) FROM <TABLE-PREFIX>badge)                           AS own_rows;" -N
```

**Two consecutive runs must produce the same numbers.** If they do not, the suite is
leaving data behind — and the next run measures in a shop that is no longer the one the
expectations were written for.

The full mechanism, including the three levels of clean-up and the way the suite's own
delete fails silently, is in → **[STANDARD-CLEANUP.md](STANDARD-CLEANUP.md)**. A suite that
leaves data behind is not finished, however green it is.

## What an E2E suite has to cover

Not "the important cases", but **every function, every procedure, every switch**:

| Area | What is checked |
|---|---|
| Regression protection | every existing setting, in its effect |
| Every configuration combination | image/no image, full height on/off, link on/off, new tab, all pages vs. a single page, recursive on/off |
| Pagination | exactly the configured number of cards per page, at every record count |
| Completeness | summed across all pages, exactly the expected product count — none twice, none missing |
| Edge cases | empty category, filter with no hits, search with no result |
| Extreme cases | many records spread over all pages, adjacent positions |
| Interplay with third-party plugins | the plugin's own markup does not carry anything a foreign plugin would wrongly evaluate |
| After AJAX | filters and sorting reload — the numbers must still be right |
| Administration | create, edit, save, delete, validation, language switch |

## The traps in the browser

### The URL of a listing changes before its content does

Wait for the first product name, never for the URL. The address bar updates on the
navigation, not on the render.

### `networkidle` never happens in the administration

The administration keeps connections open. Wait for the spinner to disappear, for the row
to appear, for the page to have turned — never for network silence.

### Saving a record shows no success message

What proves it worked is the transition from the create page to the detail page. Asserting
on a notification that is never shown is an assertion that will always time out.

### `page.goto` to a different `#/route` of a loaded administration renders nothing

The router sees a hash change in an already-booted SPA and does not rebuild the view.
Reload after navigating.

### `mt-number-field` renders `<input type="text">`

For `getByRole` it is therefore a **textbox**, never a spinbutton. The Meteor component
handles the numeric behaviour itself.

### The acceptance test suite creates an English-language admin user

Selectors written against a German administration find nothing. Write them against the
English interface, or against a `data-*` attribute that does not change with the language.

### A fresh sales channel has no compiled theme

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

### The suite's channel is not on the shop's default currency

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

### The shop decides what a cart is worth

A product created at `40` arrives as a gross cart value of `35.66`, because the suite
treats the number as net. **Read the figure back and assert the plugin's arithmetic against
it**, rather than hard-coding a total that depends on a tax rate:

```typescript
const goods = await Display.goodsValue();          // dd.summary-value.summary-total
const expected = (100 / THRESHOLD) * goods;

expect(await Display.reportedProgress()).toBeCloseTo(expected, 1);
```

### Assigning a shipping method does not change the running session

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
    await this.page.locator('.offcanvas-cart-header').waitFor();
}
```

Wait for something visible, not for `networkidle` — see the trap above.

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

They need a running shop with the plugin installed, its storefront built, and the
browserless container started. Run them before a release, after any change to a template,
and after any change to an administration page.

---

# browserless: the browser these tests drive

Playwright needs a browser. There is none installed in the DDEV web container, and one
there would be in the wrong place anyway — it would drag hundreds of megabytes of
dependencies into a container whose job is running PHP.

**The solution is a container of its own carrying Chromium, addressed over WebSocket.**

## The DDEV add-on

Set up through **[ddev-browserless](https://github.com/avhulst/ddev-browserless)**:

```bash
ddev add-on get avhulst/ddev-browserless
ddev restart
```

Afterwards:

```bash
ddev browserless on     # start the container
ddev browserless off    # stop it
```

The add-on creates a service named `browserless`, reachable under exactly that name on the
DDEV network — so from inside the web container it is `ws://browserless:3000`.

## The right endpoint

```ts
// The dedicated Playwright endpoint, not the CDP one at /chromium.
wsEndpoint: `ws://browserless:3000/chromium/playwright?token=${token}`
```

**This is a mistake that easily costs an hour.** browserless offers two endpoints:

| Path | Protocol | For whom |
|---|---|---|
| `/chromium` | Chrome DevTools Protocol | Puppeteer, `connectOverCDP` |
| `/chromium/playwright` | Playwright's own protocol | **Playwright** |

Playwright *does* connect to the CDP endpoint — but half its features (tracing, certain
locator operations) behave differently or are missing outright, and nothing says so.

## The token

```
BROWSERLESS_TOKEN=…
```

The add-on writes it. The Playwright configuration aborts without it, with the instructions
in the error message.

## `BROWSERLESS_TIMEOUT` — the most important setting

**The default is not enough.** browserless ends a session once `BROWSERLESS_TIMEOUT`
expires — and Playwright reports that as:

```
Target page, context or browser has been closed
```

That message says nothing about the cause. It looks like a defect in the test, and it is a
timeout in the container.

**A test of this plugin runs for up to five minutes** (200 products, nine pages, every page
turn a click). The value is therefore set to **900000** milliseconds, fifteen minutes:

```
# .ddev/.env.browserless
BROWSERLESS_TIMEOUT=900000
```

Then:

```bash
ddev restart
```

**Why `.ddev/.env.browserless` and not the add-on's own configuration:** this file survives
a `ddev add-on get` that updates the add-on. Changes made inside the files the add-on ships
would be gone afterwards.

## The debugger

browserless ships an interface for watching the browser work:

```
http://localhost:3000/?token=<BROWSERLESS_TOKEN>
```

Useful when a test fails and the trace file is not enough. For the normal case
`trace: 'retain-on-failure'` is the better tool, because it already has the recording by
the time the failure happens.

## The typical traps

| Symptom | Cause |
|---|---|
| `Target page, context or browser has been closed` | `BROWSERLESS_TIMEOUT` too small |
| `connect ECONNREFUSED browserless:3000` | the container is not running — `ddev browserless on` |
| certificate error | `ignoreHTTPSErrors: true` missing; the container does not know mkcert |
| `https://<host>api/oauth/token` | missing trailing slash in `APP_URL` |
| features behaving strangely | wrong endpoint — `/chromium` instead of `/chromium/playwright` |
