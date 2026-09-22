# Changelog

> **Entries below describe the state at their release.** The E2E setup has since moved
> from `tests/Acceptance/` with `zone1987/ddev-playwright` to `tests/E2E/` with
> `avhulst/ddev-browserless`; see `STANDARD-PLAYWRIGHT.md` for what holds now.

## [3.0.0] - 2026-09-11

### Added

- **`sw-testing-standard`** — the binding testing standard every Shopware plugin is built
  to. Not advice: what must exist, configured how, and when the work is finished. Where a
  required file does not exist yet, it is created.
  - `STANDARD-GATE.md` — `composer gate` and every file behind it: composer scripts with
    pinned versions, `phpstan.neon` at level max, `.php-cs-fixer.dist.php`, `rector.php`,
    five phpunit configs, `infection.json5`, both bootstraps, and the pcov requirement in
    `.ddev/config.yaml`.
  - `STANDARD-COVERAGE.md` — 100 % as the floor, what it does not tell you, `#[CoversClass]`,
    and why a tautological assertion inflates the figure without making the code safer.
  - `STANDARD-MUTATION.md` — Infection's configuration, how to judge a survivor, and why
    baselines are committed while coverage reports are not.
  - `STANDARD-JEST-ADMIN.md` — the complete administration setup: config, babel, the Twig
    and style transformers, and the global `Shopware` stub with its mixin stand-ins.
  - `STANDARD-JEST-STOREFRONT.md` — the storefront setup, which differs in ways that cost
    hours: the `moduleNameMapper` ordering trap, the `plugin.class` double, and the
    `clearMocks` interaction with `matchMedia`.
  - `STANDARD-PLAYWRIGHT.md` — the `zone1987/ddev-playwright` add-on, the required
    `.env.test` variables and how to create the integration, and four traps the Shopware
    documentation does not mention.
  - `STANDARD-CLEANUP.md` — **a test run leaves the shop as it found it**: three levels of
    clean-up, the one that fails silently, how to prove it by counting, and the single
    documented exception.
  - `STANDARD-ARCHITECTURE.md` — phpat through PHPStan, what to assert, why not Deptrac.
  - `STANDARD-WORKFLOW.md` — test-first, the order the levels are built in, and what done
    means.
  - `STANDARD-ANNOTATIONS.md` — the nineteen fixer and Rector rules that must stay disabled
    or the gate deletes the project's own DocBlocks on every run.
  - `STANDARD-SOURCE-OF-TRUTH.md` — read Shopware's source at the installed version tag.
  - `STANDARD-DIAGNOSIS.md` — how to find out why a test fails: naming which of the three
    causes it is before touching anything, the throwaway console command that runs inside
    the real container, reading `clover.xml` for uncovered lines, computing the value that
    kills a rounding mutant, the three Playwright artifacts, asking the server before the
    browser, and counting rather than reading when checking clean-up.
  - `STANDARD-DECISION-RECORDS.md` — ADRs and `CONTEXT.md`: the shape of each, what
    belongs in them, why an accepted ADR is never edited but superseded, and why writing
    down the mistakes is the highest-value part of a context file.
  - `STANDARD-DECISIONS.md` — every decision with its reasoning: Pest rejected twice,
    PHPUnit belonging to the project, what is committed and what is not.

### Verified

- **`STANDARD-JEST-STOREFRONT.md` is no longer a specification.** The setup was built in
  `FfFreeShippingProgress` and run: six specs, 100 % on statements, branches, functions and
  lines. Building it surfaced exactly what the standard predicts — a dead branch reporting
  as covered while being unreachable — which was removed rather than tested around.
- Every other configuration in the standard was already running in one of the two
  reference plugins.

### Changed

- `shopware-tester` loads `sw-testing-standard` first and is accountable to it; its scope
  is now writing individual tests, with the infrastructure belonging to the orchestrator.
- `sw-phpunit`, `sw-javascript` and `sw-e2e` open by pointing at the standard, and their
  reference files were brought in line with it: the PHPUnit path (`../../../vendor/bin/phpunit`),
  `static::` over `$this->`, `#[CoversClass]`, test names that state rules, `createStub`
  where no call is asserted, and the plugin's own Jest scripts rather than the platform's.
- `PLAYWRIGHT-E2E.md` no longer advises using end-to-end tests sparingly — it now says the
  opposite, and explains why the older advice does not apply.
- `sw-phpunit` reference files renamed from the `SHOPWARE-PHPUNIT-*` migration scheme to
  what they are about (`MOCK-REPOSITORY.md`, `ASSERT-SAME.md`, …).

### Added

- **`shopware-test-lead`** — orchestrator and entry point. Decides what must exist, audits
  a plugin against the standard, routes to the right skill or specialist.

### Removed

- `SETUP-TESTING.md` and `SHOPWARE-PHPUNIT-SETUP-KERNEL-BOOTSTRAP.md`, which carried a
  competing setup: one `phpunit.xml.dist` instead of five, a PHPUnit 10.5 schema, and a
  prohibition on exactly the autoloader-only bootstrap the standard requires.
- Five stub reference files that consisted of a teaser plus a broken link to their own
  longer counterpart, and three index files from a category scheme abandoned in v2.0.0.

### Fixed

- `marketplace.json` listed three skills and version 2.0.0, so the standard would not have
  shipped at all.
- The PHPUnit path had grown to six `../` levels in three files.
- Five links pointing at a `../shopware-phpunit/` directory that does not exist, with
  literal backticks inside the path.
- The administration Jest stub is documented as it actually is: notifications through
  `global.__shopwareNotifications`, a `beforeEach` the stub registers itself, and `Store`
  with `get()` only.
- The `@codeCoverageIgnore` contradiction between `STANDARD-COVERAGE.md` (never) and
  `STANDARD-SOURCE-OF-TRUTH.md` (on collections, because the core does) — resolved in
  favour of the core, scoped to collections alone.
- `tests/Acceptance/tsconfig.json` is now documented; without its `paths` block the
  `@fixtures/*` imports do not resolve.

## 2.0.0 — 2026-08-20

Restructured from 14 skills into 3 domain skills. **Breaking:** every skill ID changed.

### Why

14 skills cost 5,369 characters of the skill listing budget — 67 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating.

### Changed

- **14 skills → 3**, grouped by domain. Listing cost 5,369 → 826 characters
  (67 % → 10 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file; all reference
  files and bundled assets carried over, verified by content against a backup of the old layout
  (`scripts/verify-bundle.py`). 28 reference files remain.
- **References are flat siblings**, one level deep, with a table of contents in every file over
  100 lines that has more than two sections.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on vocabulary specific to this domain rather than generic nouns.
- **`license` MIT**; author reduced to a GitHub handle.

Each former skill is now a file named after its topic inside the domain directory. The domain
`SKILL.md` maps them.

## 1.0.0

Initial release — 14 skills, one per documentation topic.
