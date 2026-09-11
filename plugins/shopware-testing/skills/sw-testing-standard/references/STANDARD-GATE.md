# The gate

One command decides whether work is finished:

```bash
composer gate
```

It fixes what can be fixed, then checks everything. Green means mergeable. Red means the
work is not done — never "green apart from".

## What it runs

```json
"gate":       ["@gate:fix", "@gate:check"],
"gate:fix":   ["@rector:fix", "@cs-fix"],
"gate:check": ["@phpstan", "@cs", "@rector", "@test:unit"],
```

Fix first, then check: a run that reformats and then verifies the result cannot leave the
tree in a state the next run would change again.

## Where every file goes

All of these live in the plugin root, beside `composer.json`.

| File | Purpose |
|---|---|
| `phpstan.neon` | static analysis at level `max`, and where the phpat rules are registered |
| `.php-cs-fixer.dist.php` | style |
| `rector.php` | automated refactoring |
| `infection.json5` | mutation testing |
| `phpunit.unit.xml.dist` | fast tests, no kernel |
| `phpunit.xml.dist` | unit **and** integration, kernel booted |
| `phpunit.coverage.unit.xml.dist` | unit coverage into `var/coverage/unit/` |
| `phpunit.coverage.integration.xml.dist` | integration coverage into `var/coverage/integration/` |
| `phpunit.coverage.all.xml.dist` | both, into `var/coverage/all/` |
| `build/infection/phpunit.xml.dist` | Infection's own, isolated — see below |
| `docs/mutation/<date>/` | the mutation baselines, which **are** committed |
| `tests/UnitBootstrap.php` | autoloader only |
| `tests/TestBootstrap.php` | Shopware's `TestBootstrapper` |

**Five phpunit configs is not excess.** A filtered run must never overwrite a full
coverage report, and Infection needs one of its own because it passes `--configuration`
itself and looks only for a file literally named `phpunit.*` in the directory it is
pointed at.

## composer.json

```json
"require": {
    "php": ">=8.3"
},
"require-dev": {
    "friendsofphp/php-cs-fixer": "3.95.15",
    "infection/infection": "0.35.4",
    "phpat/phpat": "0.12.4",
    "phpstan/extension-installer": "^1.4",
    "phpstan/phpstan": "2.2.8",
    "phpstan/phpstan-deprecation-rules": "2.0.5",
    "phpstan/phpstan-phpunit": "2.0.18",
    "phpstan/phpstan-strict-rules": "2.0.12",
    "phpstan/phpstan-symfony": "2.0.20",
    "rector/rector": "^2.0",
    "rector/type-perfect": "2.1.4",
    "shopware/core": "~6.7.0",
    "shopware/storefront": "~6.7.0"
},
"conflict": {
    "shopware/core": "<6.7 || >=6.8",
    "shopware/storefront": "<6.7 || >=6.8",
    "shopware/administration": "<6.7 || >=6.8"
},
"config": {
    "sort-packages": true,
    "allow-plugins": {
        "infection/extension-installer": true,
        "phpstan/extension-installer": true,
        "symfony/runtime": true
    }
}
```

**Versions are pinned exactly**, not ranged. A gate that passes today and fails tomorrow
because a patch release changed a rule is a gate nobody trusts.

**`phpunit/phpunit` is deliberately absent.** It belongs to the project. Every script
calls `../../../vendor/bin/phpunit`, which is the version the shop actually runs.

**`shopware/storefront` is needed** whenever the plugin extends the storefront, or PHPStan
cannot resolve the page and event classes.

**`rector/type-perfect` is marked abandoned** by its author. It is kept because the
replacement (`tomasvotruba/type-coverage`) checks something else; revisit when a rule
actually breaks.

### The scripts, in full

```json
"phpstan": "phpstan analyse --memory-limit=1G",
"cs": "php-cs-fixer fix --dry-run --diff",
"cs-fix": "php-cs-fixer fix",
"rector": "rector process --dry-run --no-progress-bar",
"rector:fix": "rector process --no-progress-bar",

"test": ["@test:unit", "@test:integration"],
"test:unit": "../../../vendor/bin/phpunit -c phpunit.unit.xml.dist",
"test:integration": "../../../vendor/bin/phpunit -c phpunit.xml.dist --testsuite=integration",
"test:admin": "npm --prefix src/Resources/app/administration run unit",
"test:storefront": "npm --prefix src/Resources/app/storefront run unit",

"coverage:unit": "../../../vendor/bin/phpunit -c phpunit.coverage.unit.xml.dist",
"coverage:integration": "../../../vendor/bin/phpunit -c phpunit.coverage.integration.xml.dist --testsuite=integration",
"coverage:all": "../../../vendor/bin/phpunit -c phpunit.coverage.all.xml.dist",
"coverage": ["@coverage:unit", "@coverage:integration", "@coverage:all"],

"infection": "infection --show-mutations --no-interaction --threads=1 --only-covering-test-cases"
```

Add `scripts-descriptions` for every one of them, in whole sentences. A script whose
purpose is not written down is a script someone will be afraid to run.

**Coverage and mutation are not in the gate.** They are slow, and a gate slow enough to
tempt anyone into skipping it protects nothing. They are run deliberately: coverage before
handing over, mutation when the test suite changed shape.

## phpstan.neon

```neon
parameters:
    level: max
    paths:
        - src
        - tests
    scanDirectories:
        - ../../../vendor
    excludePaths:
        analyseAndScan:
            # php-cs-fixer and Rector bundle prefixed Symfony copies; phpstan-symfony
            # resolves against them and fails on the prefixed namespace.
            - vendor/friendsofphp
            - vendor/rector
            # Acceptance tests are TypeScript with their own node_modules.
            - tests/Acceptance
    tmpDir: var/phpstan
    treatPhpDocTypesAsCertain: false
    reportUnmatchedIgnoredErrors: true

    phpat:
        show_rule_names: true

    type_perfect:
        no_mixed_property: true
        no_mixed_caller: true
        null_over_false: true

    ignoreErrors:
        # Shopware's Package attribute declares a whitelist of core domain names. It is
        # not binding for third-party plugins, which use their own.
        -
            identifier: argument.type
            message: '#Parameter \#1 \$package of attribute class Shopware\\Core\\Framework\\Log\\Package#'
            paths:
                - src/*

services:
    -
        class: YourPlugin\Tests\Architecture\LayerTest
        tags:
            - phpat.test
```

**`reportUnmatchedIgnoredErrors: true` is the point of the ignore block.** Scope the
`Package` exception to `src/*` only — adding `tests/*` makes the gate fail, correctly,
because no test class carries the attribute.

## The phpunit configs

All five share this shape; only bootstrap, cache directory, suites and coverage differ.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="https://schema.phpunit.de/12.5/phpunit.xsd"
         bootstrap="tests/UnitBootstrap.php"
         cacheDirectory="var/phpunit-unit"
         executionOrder="depends,defects"
         beStrictAboutOutputDuringTests="true"
         failOnRisky="true"
         failOnWarning="true"
         colors="true">
    <testsuites>
        <testsuite name="unit">
            <directory>tests/Unit</directory>
        </testsuite>
    </testsuites>

    <source>
        <include>
            <directory suffix=".php">src</directory>
        </include>
        <exclude>
            <!-- Container configuration, executed at boot and never by a test. -->
            <directory suffix=".php">src/Resources/config</directory>
        </exclude>
    </source>

    <php>
        <ini name="error_reporting" value="-1"/>
    </php>
</phpunit>
```

`failOnRisky` and `failOnWarning` are not decoration. PHPUnit 12 reports a mock without
expectations as a notice; with these set it becomes a failure, which is what makes you
write `createStub` where you meant a stub.

The integration variants add:

```xml
<env name="KERNEL_CLASS" value="Shopware\Core\Kernel"/>
<env name="APP_ENV" value="test"/>
<env name="APP_DEBUG" value="0"/>
<env name="SYMFONY_DEPRECATIONS_HELPER" value="weak"/>
```

The coverage variants add six report formats, into a directory of their own per suite:

```xml
<coverage>
    <report>
        <html      outputDirectory="var/coverage/all/html"/>
        <text      outputFile="var/coverage/all/coverage.txt" showUncoveredFiles="true"/>
        <clover    outputFile="var/coverage/all/clover.xml"/>
        <cobertura outputFile="var/coverage/all/cobertura.xml"/>
        <crap4j    outputFile="var/coverage/all/crap4j.xml"/>
        <xml       outputDirectory="var/coverage/all/xml"/>
    </report>
</coverage>
```

`clover.xml` is the one to parse when you want the list of uncovered lines:

```bash
python3 -c "
import xml.etree.ElementTree as ET, pathlib
t = ET.parse('var/coverage/unit/clover.xml')
for f in t.iter('file'):
    src = pathlib.Path(f.get('name')).read_text().splitlines()
    for l in f.iter('line'):
        if l.get('count') == '0':
            n = int(l.get('num')); print(f'{f.get(\"name\")}:{n}: {src[n-1].strip()}')
"
```

## The bootstraps

`tests/UnitBootstrap.php` — no kernel, so unit tests stay fast:

```php
<?php declare(strict_types=1);

$pluginAutoload = __DIR__ . '/../vendor/autoload.php';

if (file_exists($pluginAutoload)) {
    require_once $pluginAutoload;
}

require_once __DIR__ . '/../../../../vendor/autoload.php';
```

`tests/TestBootstrap.php` — the kernel, for integration tests:

```php
<?php declare(strict_types=1);

use Shopware\Core\TestBootstrapper;

require_once __DIR__ . '/../../../../vendor/autoload.php';

$loader = (new TestBootstrapper())
    ->addCallingPlugin()
    ->addActivePlugins('YourPlugin')
    ->setForceInstallPlugins(true)
    ->bootstrap()
    ->getClassLoader();

$loader->addPsr4('YourPlugin\\Tests\\', __DIR__);
```

## tests/Integration must exist even while empty

Three configs name it as a suite, and PHPUnit aborts with `Test directory "…" not found`
when it is missing. An empty directory does not survive a clone, so put a `.gitkeep` there
saying why.

## A coverage driver has to be present — this is a DDEV setting

`composer coverage` runs green and measures **nothing** without one. A coverage figure
from a run with no driver is not a low figure, it is no figure.

**Required in `.ddev/config.yaml`:**

```yaml
# pcov measures coverage without attaching a debugger, so a coverage run does not bury
# PhpStorm in "Debug session was finished without being paused" notices.
webimage_extra_packages: [php8.3-pcov]
```

Match the PHP version of the web image. Then `ddev restart` — never `ddev start`/`stop`,
and never touch Docker directly; other projects share that daemon.

Verify:

```bash
ddev exec php -m | grep -E 'pcov|xdebug'
```

**pcov over Xdebug**, for two reasons: it is several times faster on a full suite, and it
does not attach a debugger, which keeps the IDE quiet during a coverage run. Xdebug is
needed only for branch coverage, which this standard does not require.

**Check this before writing the first test.** Discovering it after the suite exists means
re-reading every figure you believed.

## The acceptance check, once the gate is green

Run it twice and compare the tree:

```bash
composer gate
find src tests -name "*.php" -not -path "*/Acceptance/*" | sort | xargs shasum | shasum
composer gate
find src tests -name "*.php" -not -path "*/Acceptance/*" | sort | xargs shasum | shasum
```

The two checksums must be identical. A fixer that strips one DocBlock tag per pass looks
stable until the second pass — which is exactly what the disabled rules in
[STANDARD-ANNOTATIONS.md](STANDARD-ANNOTATIONS.md) prevent.
