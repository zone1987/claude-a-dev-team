---
name: playwright-init
description: Scaffold eines Playwright-Projekts — Installation (@playwright/test + Browser), playwright.config.ts mit sinnvollen Defaults (Projects/Browser-Matrix, reporter, use-Options, webServer, trace), erster Beispiel-Test und optional Page-Object-Struktur.
argument-hint: [--ts|--js] [--browsers chromium,firefox,webkit] [--ui] [--webserver "npm run dev"] [--pom]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /playwright-init

Erzeuge ein einsatzfertiges Playwright-Setup. Skills: `playwright-intro`, `playwright-writing-tests`,
`playwright-test-config`, ggf. `playwright-pom`.

## Ablauf
1. Sprache/Browser/Optionen aus `$ARGUMENTS` (Default TS, Browser-Matrix chromium+firefox+webkit).
2. **Installation** vorschlagen: `npm init playwright@latest` bzw. `npm i -D @playwright/test` + `npx playwright install`
   (mit `--with-deps` für Linux/CI).
3. **`playwright.config.ts`** erzeugen — nur dokumentierte Optionen (`playwright-test-config`): `testDir`, `fullyParallel`,
   `forbidOnly`/`retries`/`workers` (CI-abhängig), `reporter: 'html'`, `use` (`baseURL`, `trace: 'on-first-retry'`,
   `screenshot`/`video` on failure), `projects` (Browser-Matrix), optional `webServer`.
4. **Erster Test** (`tests/example.spec.ts`) mit `getByRole`-Locator + Web-First-`expect`.
5. `--pom` → Page-Object-Klasse + Fixture (`playwright-pom`).

Nur dokumentierte Config-Felder/Options (Quelle: `playwright-test-config`). Web-First-Assertions statt Sleeps. Keine Secrets in die Config.
