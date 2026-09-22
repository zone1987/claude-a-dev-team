# Mutation testing

Coverage says every line ran. Mutation testing says a test would have failed if the line
were wrong. **It is the only figure that measures the assertions rather than the reach.**

## The target

**As close to 100 % as honest tests reach.** Not 100 % as a hard gate, and the distinction
matters:

- Every surviving mutant is examined and either **killed by a test that states a rule**, or
  **documented with the reason it cannot be killed**.
- A mutant is never hidden with an ignore rule.
- A test is never written for the sole purpose of killing a mutant.
- Production logic is never changed to make a mutant die.

A score of 96 % with two documented survivors is better than 100 % reached by any of those
four routes, and a plugin is judged on the documentation of the survivors, not on the
number.

## infection.json5

```json5
{
    $schema: 'vendor/infection/infection/resources/schema.json',
    source: {
        directories: ['src'],
        excludes: [
            // Container configuration, executed at boot and never by a test — the same
            // files the phpunit configs exclude from coverage.
            'Resources/config',
            // DDL only. A mutant in a CREATE TABLE string either breaks every test at
            // once or none of them, and says nothing about the tests.
            'Migration',
            // Both npm trees ship a stray php file of their own: flatted carries a php
            // port beside its javascript, and it is nobody's code but its author's.
            'Resources/app/administration/node_modules',
            'Resources/app/storefront/node_modules',
        ],
    },
    mutators: {
        '@default': true,
    },
    // The integration suite shares one database, so parallel runs corrupt each other.
    threads: 1,
    // Measured: the suite runs in 1 second and the Shopware kernel takes 16 to boot, so
    // Infection's default of 10 seconds turns every mutant into a timeout - 201 of 273
    // on the first attempt, which is a number that says nothing about the tests.
    timeout: 60,
    // Every class extends a Shopware one, and the plugin's own autoloader does not know
    // the core. Without this Infection dies on the plugin base class.
    bootstrap: '../../../vendor/autoload.php',
    testFramework: 'phpunit',
    phpUnit: {
        // PHPUnit belongs to the project, so Infection cannot find it beside its own
        // vendor/bin.
        customPath: '../../../vendor/bin/phpunit',
        // Infection passes --configuration itself and only ever looks for a file
        // literally named phpunit.* in this directory. Giving it one of its own leaves
        // the plugin's five configs untouched.
        configDir: 'build/infection',
    },
    logs: {
        text: 'var/infection/infection.log',
        html: 'var/infection/infection.html',
        json: 'var/infection/infection.json',
        summaryJson: 'var/infection/summary.json',
    },
    tmpDir: 'var/infection/tmp',
}
```

`build/infection/phpunit.xml.dist` is the unit config with every path prefixed `../../`
**and a cache directory of its own**, so a mutation run does not fight the regular suite
for the cache:

```xml
bootstrap="../../tests/UnitBootstrap.php"
cacheDirectory="../../var/phpunit-infection"
…
<testsuite name="unit">
    <directory>../../tests/Unit</directory>
</testsuite>
<source>
    <include><directory suffix=".php">../../src</directory></include>
    <exclude><directory suffix=".php">../../src/Resources/config</directory></exclude>
</source>
```

Put a `README.md` beside it explaining why the directory exists, or the next person deletes
it as a duplicate of the plugin's own config.

**`timeout: 60` is not optional.** Infection's default is 10 seconds. Measured: the unit
suite runs in 1 second and the Shopware kernel takes 16 to boot — which turned **201 of
273 mutants** into timeouts on the first attempt. A timeout is neither a kill nor a
survivor; it is a number that says nothing.

**The exclude list appears in four places and has to match everywhere:** here, in every
phpunit config's `<source>` block, and in `phpstan.neon`'s `excludePaths`. Where one
diverges it measures something the others do not, and two figures contradict each other
with no way to tell which is right.

## Running it, and what the switches do

```bash
composer infection
# infection --show-mutations --no-interaction --threads=1 --only-covering-test-cases
```

| Switch | Effect |
|---|---|
| `--show-mutations` | prints every survivor as a diff — without it you have to open the report |
| `--no-interaction` | no prompts |
| `--threads=1` | see above: one shared database |
| `--only-covering-test-cases` | runs only the tests that cover the mutated line. The single largest saving there is |

## A measured result

From a real run's `docs/mutation/<date>/infection-summary.json`:

```json
{
    "stats": {
        "totalMutantsCount": 273,
        "killedCount": 264,
        "notCoveredCount": 0,
        "escapedCount": 8,
        "errorCount": 0,
        "timeOutCount": 1,
        "msi": 97.07,
        "mutationCodeCoverage": 100,
        "coveredCodeMsi": 97.07
    }
}
```

**`notCoveredCount: 0` is the figure that confirms the coverage claim**: there is no mutant
in code no test executes.

## "No source code was executed by the test framework"

Infection reports this and exits non-zero while a plugin still has no executable source —
an empty plugin class has nothing to mutate. It is the correct answer to that state, not a
misconfiguration: the wiring is proven by the run reaching that point at all. Say so in the
`build/infection/README.md` so it is not later misread as a fault.

## Reading a run

```bash
composer infection
```

Two numbers come out. **Covered code MSI** is the one to watch — plain MSI is diluted by
code no test reaches, and with 100 % coverage they are equal anyway.

List the survivors:

```bash
python3 -c "
import json
d = json.load(open('var/infection/infection.json'))
for m in d.get('escaped', []):
    mu = m.get('mutator', {})
    plus = [l for l in m.get('diff','').splitlines() if l.startswith('+') and not l.startswith('+++')]
    print(f\"{mu.get('mutatorName'):<18} {mu.get('originalFilePath','').split('/')[-1]}:{mu.get('originalStartLine')}\")
    if plus: print('   ' + plus[0][1:].strip()[:100])
"
```

## Judging a survivor

Ask one question: **would a shop behave differently with this mutant in place?**

Yes → a test is missing, and the test states the rule that the mutant breaks.
No → document it and move on.

Four real examples, all genuine gaps:

**Gross and net were never distinguished.** Every fixture priced both the same, so swapping
them survived. A net shop would have read the wrong figure. → a test with `0.0` net and
`4.9` gross, asserting both directions.

**Rounding was never exercised on a value that needs it.** `3.33 × 3` is exactly `9.99` in
floating point, so `round`, `floor` and `ceil` agree and the test proved nothing. `1.15` is
held as `1.1499999999999999` and `4.35` as `4.3499999999999996` — truncating either costs
the shopper a cent. → tests using those.

**Rounding up was never exercised either.** `0.07` is held just above its cent value, so
`ceil` credits a cent nobody spent.

**A delivery without a price matrix.** The loop skipping it was covered but not asserted.

And two genuine false positives, documented and left:

**`?? 1.0` instead of `?? 0.0`** where the coalescing only fires for a missing lower bound.
Both mean "every cart qualifies"; the domain makes no distinction, so a test asserting one
would be asserting nothing.

**Rounding a percentage to three decimals instead of two.** The value renders into an aria
attribute and a JSON attribute; a third decimal is invisible in both.

**Finding the value that kills a rounding mutant is arithmetic, not guesswork:**

```php
foreach ([1.15, 4.35, 0.07, 0.10] as $v) {
    $x = $v * 100;
    printf("%.2f -> %.20f round=%d floor=%d ceil=%d\n",
        $v, $x, (int)round($x), (int)floor($x), (int)ceil($x));
}
```

## Stryker — the same thing for JavaScript

Infection covers PHP. **JavaScript needs Stryker**, for the administration and for the
storefront as soon as it has JavaScript of its own.

### `stryker.config.json`

Lives beside `jest.config.js` in `src/Resources/app/administration/`:

```json
{
    "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
    "packageManager": "npm",
    "testRunner": "jest",
    "jest": {
        "projectType": "custom",
        "configFile": "jest.config.js",
        "enableFindRelatedTests": true
    },
    "mutate": [
        "src/**/*.js",
        "!src/**/*.spec.js",
        "!src/**/snippet/*.json"
    ],
    "coverageAnalysis": "perTest",
    "reporters": [
        "html",
        "json",
        "clear-text",
        "progress"
    ],
    "htmlReporter": {
        "fileName": "mutation/index.html"
    },
    "jsonReporter": {
        "fileName": "mutation/report.json"
    },
    "clearTextReporter": {
        "allowColor": false,
        "maxTestsToLog": 3
    },
    "thresholds": {
        "high": 90,
        "low": 80,
        "break": null
    },
    "timeoutMS": 30000,
    "timeoutFactor": 2,
    "concurrency": 4,
    "tempDirName": ".stryker-tmp",
    "cleanTempDir": true,
    "disableTypeChecks": false,
    "ignoreStatic": false
}
```

| Setting | Why |
|---|---|
| `projectType: "custom"` | tells Stryker **not** to guess the Jest setup. The default assumes a `create-react-app` project and ignores the plugin's own `jest.config.js` |
| `enableFindRelatedTests: true` | the counterpart to Infection's `--only-covering-test-cases`: per mutant only the specs that touch the file run |
| `coverageAnalysis: "perTest"` | the most precise level — Stryker measures per **test** which lines it executes. The alternative `"all"` runs the whole suite for every mutant |
| `"!src/**/snippet/*.json"` | snippets are translations. A mutant in a German string teaches nothing |
| `concurrency: 4` | unlike Infection, Stryker may run in parallel: Jest tests share no database |
| `timeoutMS: 30000` | generous, because a jsdom test with a mounted component is noticeably slower than a plain function |
| `"break": null` | **the run does not fail on a minimum score.** A breaking threshold leads to tests written to reach a number — exactly what the four forbidden routes above rule out |

Two reports, deliberately: `html` under `mutation/index.html` to look at, `json` under
`mutation/report.json` for the baseline.

### Pin 9.6.1 — version 10 cannot run here

```
BABEL_VERSION_UNSUPPORTED
```

Stryker 10's instrumenter requires `@babel/core@~8.0.0`. Its JavaScript parser passes
**no** `configFile: false`, so it loads the plugin's own `babel.config.js` — which uses
`@babel/preset-env` 7 — into a Babel 8 context, and fails.

**9.6.1 uses Babel 7.29** and therefore shares the plugin's dependency tree. Pin it, and
put a line in `CLAUDE.md` saying why, so nobody bumps it casually.

### The `qs` override

```json
{
    "overrides": {
        "qs": "6.16.0"
    }
}
```

Stryker pulls in `typed-rest-client` transitively, which pins a version of `qs` carrying
**three DoS advisories**. `npm audit fix` can do nothing about a pinned version. The
override forces 6.16.0 across the tree, after which `npm audit` reports **zero** findings.

### Running it

```bash
composer mutation:admin
# npm --prefix src/Resources/app/administration run mutation   →   stryker run
```

**The reports do not belong in the repository.** The HTML report runs to several
megabytes:

```gitignore
/src/Resources/app/administration/.stryker-tmp/
/src/Resources/app/administration/mutation/
```

Only the **summary** is committed, under `docs/mutation/<date>/stryker-summary.json` —
the same rule as for Infection.

### An equivalent mutant, from a real report

```json
{
    "notKilled": [
        {
            "line": 19,
            "mutator": "OptionalChaining",
            "replacement": "this.$refs.swTree",
            "static": false
        }
    ]
}
```

Mutating `this.$refs.swTree?.foo` to `this.$refs.swTree.foo` changes nothing unless
`$refs.swTree` is absent — and in every state the component can reach it is set. The
mutant is equivalent: document it in the baseline with that sentence, and the next run's
diff shows only genuinely new survivors.

Measured on a plugin built to this standard: **609 killed, 1 survivor, 99.84 %.**

## Baselines are committed — coverage reports are not

This is the one generated artifact that belongs in the repository.

A mutation run costs hours. The figure's **history** answers a question nothing else can:
"we were at 96 %, why are we at 71 %?" is unanswerable without the old run. A coverage
report answers nothing that a two-second rerun would not.

So: `docs/mutation/<YYYY-MM-DD>/` holds `infection-summary.json`, `infection-not-killed.json` and `stryker-summary.json` (the survivors),
and `docs/mutation/README.md` holds the table and the judgement on each survivor. The
verbose `infection.html` is not kept.

```gitignore
### IDE
.idea
.vscode

### Composer
composer.lock
**/vendor

### Node
package-lock.json
**/node_modules

### Built storefront assets — a release archive carries them, git does not.
### Build with: shopware-cli project storefront-build --only-extensions YourPlugin
src/Resources/app/storefront/dist/

### Tool caches and generated reports.
### Reproducible in seconds, and they change wholesale on every run.
var/
.php-cs-fixer.cache
.phpunit.cache
.phpunit.result.cache

### Jest coverage, same reasoning
src/Resources/app/*/coverage/

### Playwright output
tests/E2E/.env
tests/E2E/test-results/
tests/E2E/playwright-report/
tests/E2E/report.xml
tests/E2E/blob-report/
tests/E2E/.cache/

### Logs, except the mutation baselines below
*.log
!docs/mutation/**/*.log

### Mutation baselines ARE committed — a score costs hours and its history answers a
### question nothing else can. The verbose HTML report is not kept.
!docs/mutation/
docs/mutation/**/infection.html
```

`docs/mutation/README.md`:

```markdown
| Run | MSI | Covered MSI | Mutants | Killed | Escaped |
|---|---:|---:|---:|---:|---:|
| 2026-09-11 — baseline | 96 % | 96 % | 65 | 63 | 2 |
```

…followed by each survivor and why it stays. A survivor without a written reason is an
unexamined survivor.

## When to run it

Not in the gate — it takes minutes on a small plugin and hours on a large one, and a gate
slow enough to skip protects nothing.

Run it when the test suite changes shape: after adding a level, after a refactoring, before
a release. The score moving down without the code changing means tests were weakened.
