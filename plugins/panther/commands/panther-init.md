---
name: panther-init
description: Scaffold eines Symfony-Panther-Setups — composer require, Web-Driver-Installation (ChromeDriver/GeckoDriver via bdi), PHPUnit-Extension in phpunit.xml.dist, sinnvolle PANTHER_*-Env-Vars und eine Basis-PantherTestCase samt erstem Test.
argument-hint: [--browser chrome|firefox] [--bdi] [--ci github|gitlab] [--docker]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /panther-init

Erzeuge ein einsatzfertiges Panther-Setup. Skills: `panther-installation`, `panther-testcase`, `panther-config-env`,
bei `--ci`/`--docker` zusätzlich `panther-docker-ci`.

## Ablauf
1. Optionen aus `$ARGUMENTS` (Default Chrome, headless).
2. **Installation** vorschlagen: `composer require --dev symfony/panther dbrekelmans/bdi` + `vendor/bin/bdi detect drivers`.
3. **`phpunit.xml.dist`**: Panther-Extension registrieren (PHPUnit 10+: `<extensions><bootstrap class="Symfony\\Component\\Panther\\ServerExtension"/>`; PHPUnit 9: Listener) + sinnvolle `PANTHER_*`-`<env>`-Einträge (`panther-config-env`).
4. **Basis-Test** (`tests/E2ETest.php`) mit `PantherTestCase`, `createPantherClient()`, `filter()` + `assertSelectorTextContains()`, `waitForVisibility()` für JS.
5. `--ci`/`--docker` → CI-Workflow bzw. Dockerfile (headless + no-sandbox + `--disable-dev-shm-usage`) aus `panther-docker-ci`; Vorlagen in `utils/`.

Nur dokumentierte Env-Vars/Optionen (Quelle: `panther-config-env`/`panther-installation`). Keine echten Credentials — als CI-Secrets/`.env.test`.
