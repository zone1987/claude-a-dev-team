---
name: playwright-test
description: Scaffold eines Playwright-Tests aus einer Beschreibung — wählt role-basierte Locators, Web-First-Assertions, passende Fixtures und optional Page-Object-Methoden; deckt UI-Flows, API-Tests und Auth-Setup ab.
argument-hint: <beschreibung> z.B. "Login-Flow testen" | "POST /api/cart prüfen" [--pom] [--api] [--auth-setup]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /playwright-test

Erzeuge einen lauffähigen Playwright-Test. Skills: `playwright-writing-tests`, `playwright-locators`,
`playwright-actions`, `playwright-test-assertions`; bei `--api` `playwright-api-testing`; bei `--auth-setup` `playwright-auth`;
bei `--pom` `playwright-pom`.

## Ablauf
1. Szenario aus `$ARGUMENTS` interpretieren (UI-Flow / API / Auth-Setup).
2. **UI:** `test('...', async ({ page }) => {...})` mit role-/label-basierten Locators, Aktionen (Auto-Waiting,
   keine Sleeps) und Web-First-`expect(locator)`-Assertions.
3. **`--api`:** `test('...', async ({ request }) => {...})` mit `APIRequestContext` (get/post/…), `expect(response).toBeOK()`,
   Body-/Header-Prüfungen (`playwright-api-testing`).
4. **`--auth-setup`:** Setup-Projekt, das einmalig einloggt und `storageState` speichert; Tests verwenden ihn (`playwright-auth`).
5. **`--pom`:** Locators/Aktionen in eine Page-Object-Klasse kapseln, per Fixture bereitstellen (`playwright-pom`).

Nur dokumentierte API/Matcher (Quelle: `playwright-api-*`/`playwright-test-assertions`) — nichts raten. Selektoren stabil/role-first wählen.
