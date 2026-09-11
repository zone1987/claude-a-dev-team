---
name: sw-e2e
description: Shopware end-to-end testing with Playwright: setup, fixtures and the shop-specific helpers. Use when writing a Playwright end-to-end test against a Shopware shop.
---

# Shopware end-to-end testing

Full-stack tests against a running shop.

## Read the standard first

**[`sw-testing-standard`](../sw-testing-standard/SKILL.md) decides what must exist**; this
skill covers how to write it. Three of its rules bind every acceptance suite:

- **`STANDARD-PLAYWRIGHT.md`** — the `zone1987/ddev-playwright` add-on, the complete
  `playwright.config.ts`, the `.env.test` variables and how to create the admin
  integration, plus four traps: an uncompiled theme on a fresh sales channel, the suite's
  currency, the shop deciding what a cart is worth, and a session keeping its shipping
  method.
- **`STANDARD-CLEANUP.md`** — **a test run leaves the shop as it found it.** A suite that
  leaves entities behind is not finished, however green it is.
- **Whatever the plugin ships gets a Playwright test.** Administration work gets
  administration tests; storefront work gets storefront tests. If no suite exists yet, it
  is created.

## Reference map

- **[PLAYWRIGHT-E2E.md](references/PLAYWRIGHT-E2E.md)**: Shopware uses **Playwright** for E2E/acceptance tests — against a running shop instance, the smallest tie….

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
