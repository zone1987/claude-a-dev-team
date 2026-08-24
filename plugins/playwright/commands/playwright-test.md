---
name: playwright-test
description: Scaffolds a Playwright test from a description — picks role-based locators, web-first assertions, the fitting fixtures and optionally page-object methods; covers UI flows, API tests and auth setup.
argument-hint: <description> e.g. "test the login flow" | "check POST /api/cart" [--pom] [--api] [--auth-setup]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /playwright-test

Produce a runnable Playwright test. Skills: `playwright-writing`; with `--api` also
`playwright-library`; with `--pom` also `playwright-runner`.

## Steps
1. Read the scenario from `$ARGUMENTS` (UI flow / API / auth setup).
2. **UI:** `test('...', async ({ page }) => {...})` with role- and label-based locators, actions
   (auto-waiting, no sleeps) and web-first `expect(locator)` assertions.
3. **`--api`:** `test('...', async ({ request }) => {...})` with `APIRequestContext` (get/post/…),
   `expect(response).toBeOK()`, body and header checks (`playwright-library`).
4. **`--auth-setup`:** a setup project that logs in once and saves `storageState`; the tests then
   use it (`playwright-writing`).
5. **`--pom`:** wrap locators and actions in a page-object class, exposed through a fixture
   (`playwright-runner`).

Use documented API and matchers only (source: `playwright-writing`, `playwright-library`) — never
guess. Pick stable, role-first selectors.
