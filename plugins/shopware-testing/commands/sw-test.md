---
name: sw-test
description: Scaffolds a fitting test for a Shopware 6 class or file, to the binding testing standard — unit, integration, architecture, Jest or Playwright, with the right bootstrap, mocks and naming.
argument-hint: <ClassOrPath> [--plugin <PluginName>] [--type unit|integration|architecture|jest|e2e]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /sw-test

Produce a test for the given class or file, **to the standard in `sw-testing-standard`**.
Delegate the writing to `shopware-tester`.

## Before anything

Load **`sw-testing-standard`**. It settles what must exist and how it is configured; this
command only decides which file to write next. If the plugin's test setup does not exist
yet, **create it first** — the standard specifies every file.

## Steps

1. **Analyse the target**: dependencies, whether it needs a kernel, whether it is PHP, admin
   JavaScript, storefront JavaScript, or something a user sees.
2. **Pick the level** (or take `--type`), and write into the directory the standard names:

   | Level | Where | Bootstrap |
   |---|---|---|
   | Unit | `tests/Unit/` | `tests/UnitBootstrap.php`, no kernel |
   | Integration | `tests/Integration/` | `tests/TestBootstrap.php` + `IntegrationTestBehaviour` |
   | Architecture | `tests/Architecture/` | none — phpat, registered in `phpstan.neon` |
   | Jest admin | `src/Resources/app/administration/src/**/*.spec.js` | beside the code |
   | Jest storefront | `src/Resources/app/storefront/src/**/*.spec.js` | beside the code |
   | Playwright | `tests/E2E/tests/*.spec.ts` | the acceptance fixture |

3. **Write it to the standard's rules**, which are not stylistic preferences:
   - `#[CoversClass(…)]` on the class. **Never `#[CoversNothing]`** — a test that covers
     nothing is deleted, not written.
   - **Test names state the rule**: `testACartAtExactlyTheThresholdEarnsTheTier`, never
     `testCalculate`. In Jest: `it('asks for the offers of the product it was given')`.
   - `static::assertSame(…)`, not `$this->assertSame(…)`.
   - `createStub` when no call is asserted; `createMock` only with expectations. PHPUnit 12
     reports the difference, and `failOnRisky` turns it into a failure.
   - Arrange, act, assert — in that order, with a blank line between.
   - A one-line comment only where the case is not obvious from the name, and it says *why
     the case exists*, not what the code does.

4. **Run it and watch it fail first.** A test that passes the moment it is written has not
   been shown to test anything.

   ```bash
   composer test:unit
   composer test:integration
   npm --prefix src/Resources/app/administration run unit
   ddev browserless on
   ddev exec -d /var/www/html/shopware/custom/static-plugins/<PluginName>/tests/E2E \
       npx playwright test
   ```

   The Playwright specs drive a Chromium in its own container; `ddev browserless on` starts
   it, and it has to be running before the specs are. The details are in the
   `sw-testing-standard` skill, `STANDARD-PLAYWRIGHT.md`.

5. **Report the coverage consequence.** If the new test does not bring its subject to
   100 %, say what is still uncovered and why.

## Never

- **Never overwrite an existing test.** Add to it.
- **Never weaken an assertion to make a test pass.** The failure is the finding.
- **Never write a tautological assertion** — `assertInstanceOf` on a statically known type
  reaches the line and proves nothing. PHPStan rejects it, correctly.
- **Git: commit on a feature branch, never push, and ask first** — a "no" at the start of
  a project holds throughout.
