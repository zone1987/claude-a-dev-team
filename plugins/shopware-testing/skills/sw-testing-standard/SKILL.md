---
name: sw-testing-standard
description: The binding testing standard for every Shopware 6 plugin — which tools, which configuration, which thresholds, and the clean-up rule. Use before setting up a plugin's test suite, when adding a test level to an existing plugin, or when deciding whether something is finished.
---

# The Shopware plugin testing standard

**This is law, not advice.**

Every Shopware plugin in this workspace is built to it — existing ones are brought up to
it, new ones start from it. A plugin that does not meet this standard is not finished,
whatever else is true of it.

**Where a required file does not exist yet, it is created.** "This plugin has no Jest
setup" is not a reason to skip the administration tests; it is the first task. The same
holds for the gate, the architecture rules, the acceptance suite and the clean-up.

The other skills in this plugin explain **how** to write a given test.
This one settles **what must exist, configured how, and when you are done.**

## The short version

| Level | Tool | Threshold |
|---|---|---|
| Unit | PHPUnit (the project's, never the plugin's) | 100 % coverage |
| Integration | PHPUnit + `TestBootstrapper` | part of the same 100 % |
| Architecture | phpat, run by PHPStan | every rule green |
| Administration JS | Jest + `@vue/test-utils` | 100 %, enforced by threshold |
| Storefront JS | Jest | 100 %, enforced by threshold |
| End-to-end | Playwright + Acceptance Test Suite | every flow the plugin touches |
| Static analysis | PHPStan level `max` | zero errors |
| Style | php-cs-fixer | zero deviations |
| Refactoring | Rector | dry run clean |
| Mutation | Infection | as close to 100 % as honest tests reach |

**All of them. Every plugin. No level is optional.**

Two arguments that are not accepted:

- *"This plugin is too small for that."* A small plugin reaches the thresholds in an
  afternoon, and a small plugin with no tests is where the next defect lives.
- *"The setup does not exist yet."* Then it is created. Every file needed is specified in
  these references, taken from plugins where it is running today.

**Applies to whatever the plugin ships.** Administration code means Jest specs for every
component and a Playwright suite for every page. Storefront code means Jest specs for
every JavaScript plugin and a Playwright suite for what the shopper sees. PHP means unit,
integration, architecture and acceptance tests. If the plugin adds it, tests cover it.

## Reference map

- **[STANDARD-GATE.md](references/STANDARD-GATE.md)**: the one command that must be green, and every file that makes it work — `composer.json` scripts, `phpstan.neon`, `.php-cs-fixer.dist.php`, `rector.php`, the five phpunit configs, `infection.json5`.
- **[STANDARD-COVERAGE.md](references/STANDARD-COVERAGE.md)**: why 100 % is the floor and not the goal, what it does not tell you, and how the figure is produced and read.
- **[STANDARD-MUTATION.md](references/STANDARD-MUTATION.md)**: Infection's configuration, how to judge a surviving mutant, and why baselines are committed while coverage reports are not.
- **[STANDARD-JEST-ADMIN.md](references/STANDARD-JEST-ADMIN.md)**: complete Jest setup for a plugin's administration, including the Shopware global stub, the Twig transformer and the mixin stand-ins.
- **[STANDARD-JEST-STOREFRONT.md](references/STANDARD-JEST-STOREFRONT.md)**: complete Jest setup for storefront JavaScript, which differs from the administration in ways that cost hours if you assume otherwise.
- **[STANDARD-PLAYWRIGHT.md](references/STANDARD-PLAYWRIGHT.md)**: the Acceptance Test Suite setup, and the traps the Shopware documentation does not mention.
- **[STANDARD-CLEANUP.md](references/STANDARD-CLEANUP.md)**: **a test run leaves the shop as it found it.** Three levels of clean-up, the one that silently fails, and the single documented exception.
- **[STANDARD-ARCHITECTURE.md](references/STANDARD-ARCHITECTURE.md)**: phpat rules through PHPStan — what to assert, and why not Deptrac.
- **[STANDARD-WORKFLOW.md](references/STANDARD-WORKFLOW.md)**: test-first, the order the levels are built in, and what "done" means.
- **[STANDARD-ANNOTATIONS.md](references/STANDARD-ANNOTATIONS.md)**: the DocBlock rules, and the twelve Rector plus seven php-cs-fixer rules that must stay disabled or the gate deletes them on every run.
- **[STANDARD-DECISIONS.md](references/STANDARD-DECISIONS.md)**: every decision behind this standard with its reasoning — Pest, PHPUnit's location, what is committed, and the rest.
- **[STANDARD-DIAGNOSIS.md](references/STANDARD-DIAGNOSIS.md)**: how to find out why a test fails — naming the three causes, the throwaway console probe, reading coverage and mutation output, and counting rather than reading.
- **[STANDARD-DECISION-RECORDS.md](references/STANDARD-DECISION-RECORDS.md)**: ADRs and `CONTEXT.md` — the shape of each, what belongs in them, and why an accepted ADR is never edited.
- **[STANDARD-SOURCE-OF-TRUTH.md](references/STANDARD-SOURCE-OF-TRUTH.md)**: **read Shopware's own source at the exact installed version** before deciding how anything is done — `github.com/shopware/shopware/tree/v<VERSION>`, with the tag matched to the shop.

## The two rules that are argued about most

**PHPUnit belongs to the project, never to the plugin.** A plugin that pins its own
version pins a version that goes stale. Scripts call `../../../vendor/bin/phpunit`.

**A test run leaves the shop as it found it.** A suite that leaves entities behind fills
the administration with noise nobody can tell from real configuration, and it eventually
changes what the next run measures. → [STANDARD-CLEANUP.md](references/STANDARD-CLEANUP.md)

## Look it up before you decide

**`https://github.com/shopware/shopware/tree/v<VERSION>`, with the tag matched to the
installed version.** On 6.7.14.0 that is `v6.7.14.0`; on 6.7.19.2 it is `v6.7.19.2`. A
trunk link describes code the shop does not run.

Constructor argument order, default values of feature flags, whether a field is nullable in
this version, how the core tests this kind of class — all of it is in there, and all of it
has been got wrong by assuming. → [STANDARD-SOURCE-OF-TRUTH.md](references/STANDARD-SOURCE-OF-TRUTH.md)

## Where this came from

Measured against Shopware 6.7.14.0 and two plugins built to it: `AgDropshippersCompanion`
(administration, DAL entities, messaging) and `FfFreeShippingProgress` (storefront, cart
display).

**Every configuration here is running, not proposed**, and was verified against the code
it came from: the gate and its configurations, the five phpunit configs, both bootstraps,
`infection.json5`, the architecture rules, both Jest setups, `playwright.config.ts`, and
the clean-up — the last measured by counting rows before and after two consecutive runs.

The storefront Jest setup was the last to be proven: it was written here first, then built
in `FfFreeShippingProgress` and run. Six specs, 100 % on all four metrics. Building it
surfaced a defect the standard predicted — a dead branch in `_isMotionActive()` that
reported as covered while being unreachable — which is the argument for
[STANDARD-MUTATION.md](references/STANDARD-MUTATION.md) in one line.
