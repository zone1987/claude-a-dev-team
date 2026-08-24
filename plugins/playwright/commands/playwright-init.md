---
name: playwright-init
description: Scaffolds a Playwright project — installation (@playwright/test plus browsers), a playwright.config.ts with sensible defaults (projects and browser matrix, reporter, use options, webServer, trace), a first example test and optionally a page-object structure.
argument-hint: [--ts|--js] [--browsers chromium,firefox,webkit] [--ui] [--webserver "npm run dev"] [--pom]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /playwright-init

Produce a ready-to-use Playwright setup. Skills: `playwright-writing`, `playwright-runner`.

## Steps
1. Language, browsers and options from `$ARGUMENTS` (default TS, browser matrix chromium+firefox+webkit).
2. **Installation**: propose `npm init playwright@latest` or `npm i -D @playwright/test` plus
   `npx playwright install` (with `--with-deps` on Linux and CI).
3. **`playwright.config.ts`** — documented options only (`playwright-runner`): `testDir`,
   `fullyParallel`, `forbidOnly`/`retries`/`workers` (depending on CI), `reporter: 'html'`, `use`
   (`baseURL`, `trace: 'on-first-retry'`, `screenshot`/`video` on failure), `projects` (the browser
   matrix), optionally `webServer`.
4. **A first test** (`tests/example.spec.ts`) with a `getByRole` locator and a web-first `expect`.
5. `--pom` adds a page-object class plus a fixture (`playwright-runner`).

Use documented config fields and options only (source: `playwright-runner`). Web-first assertions
rather than sleeps. No secrets in the config.
