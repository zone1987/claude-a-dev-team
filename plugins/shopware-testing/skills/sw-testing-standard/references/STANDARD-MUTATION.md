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
        ],
    },
    mutators: {
        '@default': true,
    },
    // The integration suite shares one database, so parallel runs corrupt each other.
    threads: 1,
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

## Baselines are committed — coverage reports are not

This is the one generated artifact that belongs in the repository.

A mutation run costs hours. The figure's **history** answers a question nothing else can:
"we were at 96 %, why are we at 71 %?" is unanswerable without the old run. A coverage
report answers nothing that a two-second rerun would not.

So: `docs/mutation/<YYYY-MM-DD>/` holds `summary.json` and `infection.log` (the survivors),
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
tests/Acceptance/.env
tests/Acceptance/test-results/
tests/Acceptance/playwright-report/
tests/Acceptance/report.xml
tests/Acceptance/blob-report/
tests/Acceptance/.cache/

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
