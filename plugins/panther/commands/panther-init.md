---
name: panther-init
description: Scaffold a Symfony Panther setup — composer require, web driver installation (ChromeDriver/GeckoDriver via bdi), PHPUnit extension in phpunit.xml.dist, sensible PANTHER_* env vars and a base PantherTestCase along with a first test.
argument-hint: [--browser chrome|firefox] [--bdi] [--ci github|gitlab] [--docker]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /panther-init

Produce a ready-to-run Panther setup. Skills: `panther-installation`, `panther-testcase`, `panther-config-env`,
plus `panther-docker-ci` with `--ci`/`--docker`.

## Procedure
1. Options from `$ARGUMENTS` (default Chrome, headless).
2. **Suggest the installation**: `composer require --dev symfony/panther dbrekelmans/bdi` + `vendor/bin/bdi detect drivers`.
3. **`phpunit.xml.dist`**: register the Panther extension (PHPUnit 10+: `<extensions><bootstrap class="Symfony\\Component\\Panther\\ServerExtension"/>`; PHPUnit 9: listener) + sensible `PANTHER_*` `<env>` entries (`panther-config-env`).
4. **Base test** (`tests/E2ETest.php`) with `PantherTestCase`, `createPantherClient()`, `filter()` + `assertSelectorTextContains()`, `waitForVisibility()` for JS.
5. `--ci`/`--docker` → CI workflow or Dockerfile (headless + no-sandbox + `--disable-dev-shm-usage`) from `panther-docker-ci`; templates in `utils/`.

Only documented env vars/options (source: `panther-config-env`/`panther-installation`). No real credentials — use CI secrets/`.env.test`.
