---
name: sw-e2e
description: Shopware end-to-end testing with Playwright: setup, fixtures and the shop-specific helpers. Use when writing a Playwright end-to-end test against a Shopware shop.
---

# Shopware end-to-end testing

Full-stack tests against a running shop.

## Read the standard first

**[`sw-testing-standard`](../sw-testing-standard/SKILL.md) decides what must exist**; this
skill covers how to write it. Three of its rules bind every acceptance suite:

- **`STANDARD-PLAYWRIGHT.md`** — the location `tests/E2E/`, the
  [`avhulst/ddev-browserless`](https://github.com/avhulst/ddev-browserless) add-on and the
  browser in its own container, the complete `playwright.config.ts` including the
  `connectOptions.wsEndpoint`, the three `.env` files read with `process.loadEnvFile`, the
  pinned versions, `BROWSERLESS_TIMEOUT`, plus the traps: an uncompiled theme on a fresh
  sales channel, the suite's currency, the shop deciding what a cart is worth, and a
  session keeping its shipping method.
- **`STANDARD-CLEANUP.md`** — **a test run leaves the shop as it found it.** A suite that
  leaves entities behind is not finished, however green it is.
- **Whatever the plugin ships gets a Playwright test.** Administration work gets
  administration tests; storefront work gets storefront tests. If no suite exists yet, it
  is created.

## Running

The browser is not in the web container; it runs in its own, started from the host first:

```bash
ddev browserless on
ddev exec -d /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME>/tests/E2E \
    npx playwright test
```

## Reference map

- **[PLAYWRIGHT-E2E.md](references/PLAYWRIGHT-E2E.md)**: writing a spec once the suite in `tests/E2E/` exists — the acceptance test suite, page objects, administration flows, and what the examples encode.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
