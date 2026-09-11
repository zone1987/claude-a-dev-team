# Architecture tests

**Every plugin has them.** They are the cheapest tests in the suite — they run inside
PHPStan, cost no extra execution, and catch the class of mistake that unit tests never see:
a dependency pointing the wrong way.

## phpat, through PHPStan — not Deptrac

`phpat` runs as a PHPStan extension, which means it shares PHPStan's type resolution. It
sees what PHPStan sees: inferred types, generics, the lot.

Deptrac parses independently and knows less. It also needs its own run, its own config and
its own place in the gate. The reference plugin migrated away from it; `.deptrac.cache`
lingering in a repository is the fossil of that decision.

## Setup

In `composer.json`:

```json
"phpat/phpat": "0.12.4"
```

`phpstan/extension-installer` registers it. In `phpstan.neon`:

```neon
parameters:
    phpat:
        show_rule_names: true

services:
    -
        class: YourPlugin\Tests\Architecture\LayerTest
        tags:
            - phpat.test
```

`show_rule_names: true` puts the method name in the failure, so a violation says which
rule broke rather than only which class.

## tests/Architecture/LayerTest.php

```php
<?php declare(strict_types=1);

namespace YourPlugin\Tests\Architecture;

use PHPat\Selector\Selector;
use PHPat\Test\Builder\Rule;
use PHPat\Test\PHPat;

/**
 * @class LayerTest
 * @package YourPlugin.Architecture
 */
final class LayerTest
{
    /**
     * @return Rule
     */
    public function testStructsCarryDataAndNotBehaviour(): Rule
    {
        return PHPat::rule()
            ->classes(Selector::inNamespace('YourPlugin\Struct'))
            ->shouldNot()
            ->dependOn()
            ->classes(
                Selector::inNamespace('YourPlugin\Service'),
                Selector::inNamespace('YourPlugin\Subscriber'),
            )
            ->because('what the template is handed must not reach back into the services that built it');
    }

    /**
     * @return Rule
     */
    public function testEnumsAreLeavesOfTheDependencyGraph(): Rule
    {
        return PHPat::rule()
            ->classes(Selector::inNamespace('YourPlugin\Enum'))
            ->shouldNot()
            ->dependOn()
            ->classes(
                Selector::inNamespace('YourPlugin\Service'),
                Selector::inNamespace('YourPlugin\Struct'),
                Selector::inNamespace('YourPlugin\Subscriber'),
            )
            ->because('enums are leaves of the dependency graph');
    }

    /**
     * @return Rule
     */
    public function testServicesDoNotDependOnSubscribers(): Rule
    {
        return PHPat::rule()
            ->classes(Selector::inNamespace('YourPlugin\Service'))
            ->shouldNot()
            ->dependOn()
            ->classes(Selector::inNamespace('YourPlugin\Subscriber'))
            ->because('a subscriber calls a service, never the other way round');
    }
}
```

**Note there is no `extends TestCase`.** phpat discovers the class through the service tag
and calls each `test*` method for the `Rule` it returns. It never runs under PHPUnit.

## What is worth asserting

The rules that encode decisions someone could unknowingly undo:

| Rule | What it protects |
|---|---|
| Structs do not depend on services | the struct handed to Twig stays a value, not a service locator |
| Enums depend on nothing of ours | they stay leaves, so they can be used anywhere |
| Services do not depend on subscribers | the direction of the wiring |
| Nothing depends on `Shopware\Storefront\Controller` | a display plugin attaches data to a page; it does not route |
| Interfaces depend only on structs and enums | a contract other plugins implement stays free of internals |
| Nothing outside `Core\Content` depends on a `Definition` | the DAL layer stays behind its repositories |

**`->because(...)` is mandatory and is not decoration.** It is the sentence a developer
reads when the rule fires, and it has to explain the decision, not restate the rule.

## Beyond layering

Two more architecture tests worth having, both plain PHPUnit rather than phpat, because
they inspect files rather than dependencies:

**Annotation signatures.** Reads every PHP file and compares its `@param` tags with the
real signature; fails when a tag names a parameter that does not exist or a non-void method
has no `@return`. A wrong tag is worse than none, and PHPStan does not check the tag set
this standard requires. → [STANDARD-ANNOTATIONS.md](STANDARD-ANNOTATIONS.md)

**Readonly classes.** Asserts that every class under `Struct` is `final readonly`. A struct
that becomes mutable does so quietly.

Both use `#[DataProvider]` over a generator yielding one case per file, so a failure names
the file rather than the whole suite.

## When a rule fails

Fix the code, not the rule. A rule that is relaxed to make a violation pass was never a
rule. If the design genuinely changed, the rule changes with a written reason — in the
ADR that the `->because(...)` line points at.
