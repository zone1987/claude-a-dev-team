---
name: playwright-test
description: Scaffold eines Playwright-Tests aus einer Beschreibung — wählt role-basierte Locators, Web-First-Assertions, passende Fixtures und optional Page-Object-Methoden; deckt UI-Flows, API-Tests und Auth-Setup ab.
argument-hint: <beschreibung> z.B. "Login-Flow testen" | "POST /api/cart prüfen" [--pom] [--api] [--auth-setup]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /playwright-test

Erzeuge einen lauffähigen Playwright-Test. Skills: `playwright-writing`, `playwright-writing`,
`playwright-writing`, `playwright-writing`; bei `--api` `playwright-library`; bei `--auth-setup` `playwright-writing`;
bei `--pom` `playwright-runner`.

## Ablauf
1. Szenario aus `$ARGUMENTS` interpretieren (UI-Flow / API / Auth-Setup).
2. **UI:** `test('...', async ({ page }) => {...})` mit role-/label-basierten Locators, Aktionen (Auto-Waiting,
   keine Sleeps) und Web-First-`expect(locator)`-Assertions.
3. **`--api`:** `test('...', async ({ request }) => {...})` mit `APIRequestContext` (get/post/…), `expect(response).toBeOK()`,
   Body-/Header-Prüfungen (`playwright-library`).
4. **`--auth-setup`:** Setup-Projekt, das einmalig einloggt und `storageState` speichert; Tests verwenden ihn (`playwright-writing`).
5. **`--pom`:** Locators/Aktionen in eine Page-Object-Klasse kapseln, per Fixture bereitstellen (`playwright-runner`).

Nur dokumentierte API/Matcher (Quelle: `playwright-api-*`/`playwright-writing`) — nichts raten. Selektoren stabil/role-first wählen.
