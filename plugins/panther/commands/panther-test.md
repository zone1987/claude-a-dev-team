---
name: panther-test
description: Scaffold a Symfony Panther test from a description — picks the right client (WebDriver for JS / KernelBrowser / HttpBrowser), builds navigation, form interaction, correct waitFor* calls and Panther/web assertions; optionally as a page object.
argument-hint: <description> e.g. "submit the login form and check the dashboard" [--browserkit] [--js] [--pom]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /panther-test

Produce a runnable Panther test. Skills: `panther-testing`, `panther-testing`, `panther-testing`,
`panther-testing`, `panther-testing`; with `--browserkit` also `panther-testing`.

## Procedure
1. Interpret the scenario from `$ARGUMENTS`; choose the client:
   - JS/AJAX/real-time → `createPantherClient()` (real browser)
   - pure server/HTML checks → `createClient()` (KernelBrowser) or `--browserkit` `createHttpBrowserClient()`
2. **Navigation/interaction:** `$client->request('GET', …)`, `$crawler->filter(...)`/`selectButton(...)`, `submitForm(...)`/`click(...)`.
3. **Waiting (WebDriver/JS only):** `waitForVisibility`/`waitForElementToContain`/`waitFor` with the correct signature instead of `sleep()`.
4. **Assertions:** `assertSelectorTextContains`/`assertPageTitleSame`/`assertSelectorIsVisible`/… (`panther-testing`).
5. `--pom` → encapsulate locators/actions in a page object class.

Check methods/signatures against the (source-verified) `panther-*` skills — Panther's crawler does NOT support all DomCrawler methods. No `sleep()` hacks.
