# Shopware 6 — Checklist for a New Plugin

Replace every placeholder (`{PluginName}`, `{plugin-vendor}`, `{shopwareNext}`, …) with the
plugin's own values. A file that still contains `{PluginName}` has been copied, not adopted.

## Skeleton

- [ ] `composer.json`: `{plugin-vendor}/{plugin-kebab-case}`, `license: proprietary`,
      `conflict` block, `autoload` + `autoload-dev`, `extra.shopware-plugin-class`
- [ ] `LICENSE` proprietary, end year = current year
- [ ] `src/{PluginName}.php` with a `build()` override for `packages/`
- [ ] `src/Framework/Log/Package.php` — the plugin's own attribute
- [ ] `src/Resources/config/services.php` + `services/*.php`, explicit, without autowiring
- [ ] `src/Resources/config/packages/monolog.yaml` with its own channel

## Tooling

- [ ] `.php-cs-fixer.dist.php` — including the rules that stay OFF
- [ ] `phpstan.neon` — `level: max`, no `ignoreErrors`
- [ ] `rector.php` — the set of the plugin's own Shopware version, 12 skip rules
- [ ] `infection.json5` — `timeout: 60`, `threads: 1`, `configDir`
- [ ] `build/infection/phpunit.xml.dist`
- [ ] The five PHPUnit configurations
- [ ] `tests/UnitBootstrap.php` and `tests/TestBootstrap.php`
- [ ] `cliff.toml`
- [ ] `.gitignore` — `/sbom.json`, `CONTEXT.md`, mutation and coverage reports

## Tests

- [ ] `tests/Unit/`, mirroring `src/`
- [ ] `tests/Integration/` for everything a stub cannot do
- [ ] `tests/Architecture/LayerTest.php` — at least direction, migration, delimitation
- [ ] Convention tests next to the definitions
- [ ] `tests/Helper/` — `RecordingLogger`, `TestDefinitionRegistry` with `freshlyCompiled()`
- [ ] `tests/E2E/` with `playwright.config.ts` and fixtures

## Administration (if present)

- [ ] `jest.config.js` with the `vue.cjs.js` mapping and the 100 % threshold
- [ ] `test/_setup/shopware.js` — the stub
- [ ] `test/_transformer/twig.js` and `style.js`
- [ ] `eslint.config.js` with `eslint-plugin-vue`
- [ ] `.prettierrc.json`, `.prettierignore` (with `*.html.twig`)
- [ ] `.stylelintrc.json`
- [ ] `stryker.config.json` — 9.6.1, `qs` override
- [ ] Convention spec for the component sizes

## Storefront

- [ ] `.stylelintrc.json` and `package.json` with `lint:scss` — **always**
- [ ] Jest, ESLint, Prettier — **only if there is JavaScript**

## Documentation

- [ ] `CLAUDE.md` — under 200 lines, with an ADR table and `Traps`
- [ ] `adr/` with the generally applicable ADRs
- [ ] `adr/_superseded/` created
- [ ] `README.md` — German, for the shop operator
- [ ] `SECURITY.md` — CRA article 13 paragraph 8
- [ ] `UPGRADE-{shopwareNext}.md`
- [ ] `CHANGELOG.md` — via `composer changelog`
- [ ] `CONTEXT.md` — during the work, gitignored

## Completion

- [ ] `composer gate` green, twice, same checksum
- [ ] `composer coverage:all` — 100 %, measured
- [ ] `composer test:admin` — 100 %
- [ ] E2E green, shop unchanged afterwards (counted)
- [ ] `composer mutation` — every survivor justified, baseline committed
- [ ] Looked at in the browser
- [ ] Committed, **nothing pushed**

→ Tree and `.gitignore`: [PLUGIN-STRUCTURE.md](PLUGIN-STRUCTURE.md)
→ `composer.json` in full: [PLUGIN-COMPOSER.md](PLUGIN-COMPOSER.md)
→ The `Package` attribute: [PLUGIN-PACKAGE-ATTRIBUTE.md](PLUGIN-PACKAGE-ATTRIBUTE.md)
