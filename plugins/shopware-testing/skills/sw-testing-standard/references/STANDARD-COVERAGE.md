# Coverage: 100 %, and what that does not mean

**100 % is the floor, not the goal.** It is mandatory, and reaching it proves less than it
sounds.

## The rule

100 % of classes, methods and lines, on every level:

| Where | Measured by | Enforced by |
|---|---|---|
| PHP | pcov via PHPUnit | reading the report; the figure is checked before handing over |
| Administration JS | Jest | `coverageThreshold` — the run **fails** below 100 % |
| Storefront JS | Jest | `coverageThreshold` — the run **fails** below 100 % |

The JavaScript side fails automatically. The PHP side does not, because PHPUnit's own
threshold options are coarse; the figure is read and acted on.

**Excluded from measurement: `src/Resources/config`.** Container configuration is executed
at boot and never by a test.

**Nothing else is excluded by choice** — no `@codeCoverageIgnore` for "trivial" getters, no
exemption for subscribers or structs. Every exception is a judgement call, and judgement
calls multiply.

**One exception, and it is not a judgement call:** a DAL `EntityCollection` subclass carries
`@codeCoverageIgnore`, because Shopware's own collections do and
[STANDARD-SOURCE-OF-TRUTH.md](STANDARD-SOURCE-OF-TRUTH.md) requires mirroring what the core
writes on a class of that kind. The generated collection methods belong to the framework,
not to the plugin, and testing them tests Shopware. This applies to collections only — not
to any other class you find tedious to test.

## What 100 % says, and what it does not

It says every line ran during the test suite.

It does **not** say a test would fail if the line were wrong. That is a different question,
and the only thing that answers it is mutation testing.

A worked example from this workspace. This class had 100 % coverage:

```php
private function costOf(Price $price, bool $taxStateIsGross): float
{
    return $taxStateIsGross ? $price->getGross() : $price->getNet();
}
```

Every line ran. Every test passed. And **swapping gross for net changed nothing**, because
every fixture priced both the same. A net shop would have read the wrong figure and nobody
would have known. → [STANDARD-MUTATION.md](STANDARD-MUTATION.md)

## Three rules without which the figure lies

**Every test names its subject with `#[CoversClass]`.**

```php
#[CoversClass(FreeShippingThresholdResolver::class)]
final class FreeShippingThresholdResolverTest extends TestCase
```

A test that drives a class without naming it makes the report call tested code untested —
and the figure then depends on the order the tests happened to run in.

**A tautological assertion is not a test.** PHPStan catches these, and it is right to:

```php
// Useless: the type is statically known, so this can never fail.
static::assertInstanceOf(Plugin::class, new MyPlugin(true, __DIR__));

// Useful: this can fail, and would if someone removed the parent.
static::assertTrue((new \ReflectionClass(MyPlugin::class))->isSubclassOf(Plugin::class));
```

The first form reaches the line and proves nothing. It is exactly how a coverage figure
gets inflated without the code getting safer.

**A coverage driver must be installed**, or the run is green and measures nothing:

```bash
ddev exec php -m | grep -E 'pcov|xdebug'
```

## Producing the figure

```bash
composer coverage        # all three suites, into var/coverage/{unit,integration,all}/
composer coverage:unit   # just the fast one, while working
```

Read the summary:

```bash
sed -e 's/\x1b\[[0-9;]*m//g' var/coverage/unit/coverage.txt | head -20
```

Find what is missing — the text report says how much, `clover.xml` says where:

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

An uncovered line is a question, not a chore: **why has no test gone there?** In this
workspace the answer was once "because every test builds a cart without a delivery, and
the delivery branch is the one real shops take" — the uncovered line was the normal path.

## Jest: the threshold does the enforcing

```javascript
coverageThreshold: {
    global: {
        statements: 100,
        branches: 100,
        functions: 100,
        lines: 100,
    },
},
```

All four metrics. `html-spa`, the reporter the core uses, defaults to showing only lines,
branches and functions — statements are measured and enforced but invisible unless named:

```javascript
coverageReporters: [
    'text',
    'text-summary',
    ['html-spa', { metricsToShow: ['statements', 'branches', 'functions', 'lines'] }],
    'json-summary',
],
```

## What "everything" means for the administration

Every component, every function, every statement, every method, every button, every page,
every dropdown, every flow, every mixin. If the plugin ships it, a test drives it. The
threshold is what makes this checkable rather than aspirational: the run fails, and the
gap cannot reach the branch quietly.

The same applies to the storefront. Whatever JavaScript the plugin adds is covered.

## Reports are not committed

They are reproducible in seconds, change wholesale on every run, and make every diff
unreadable. `var/` and `src/Resources/app/*/coverage/` are ignored.

Mutation baselines **are** committed, for a reason that does not apply here.
→ [STANDARD-MUTATION.md](STANDARD-MUTATION.md)
