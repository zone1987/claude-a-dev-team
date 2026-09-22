# Shopware 6 — php-cs-fixer

**Plugins use php-cs-fixer, not ECS.** Shopware's own core uses ECS internally; a plugin
follows the core's `.php-cs-fixer.dist.php` instead, because that is the file the core
publishes its rule choices in and the one a plugin can adopt directly.

## The skeleton

`.php-cs-fixer.dist.php` in the plugin root:

```php
<?php declare(strict_types=1);

use PhpCsFixer\Config;
use PhpCsFixer\Finder;
use Shopware\Core\Framework\Log\Package;

$finder = Finder::create()
    ->in([__DIR__ . '/src', __DIR__ . '/tests'])
    ->exclude(['node_modules'])
    ->append([__FILE__, __DIR__ . '/rector.php']);

return (new Config())
    ->setRiskyAllowed(true)
    ->setFinder($finder)
    ->setCacheFile('var/php-cs-fixer/.php-cs-fixer.cache')
    ->setRules([ /* below */ ]);
```

`->append([...])` pulls the configuration files themselves into the formatting.

`setRiskyAllowed(true)` enables rules that can change behaviour — `strict_comparison`
(`==` becomes `===`) and `native_function_invocation`. That is deliberate and carried by
the test coverage: a behaviour-changing rule is noticed by a test when coverage is 100 %.
**Without that coverage, leave `setRiskyAllowed` at `false`.**

## The base sets

```php
'@PSR12'         => true,
'@Symfony'       => true,
'@Symfony:risky' => true,
```

## The rules that must stay OFF

This is the part forgotten in every new plugin, and it costs hours.

### Group 1 — `<?php declare(strict_types=1);` on one line

```php
'declare_strict_types'         => true,
'blank_line_after_opening_tag' => false,
'linebreak_after_opening_tag'  => false,
```

Without the two `false` entries php-cs-fixer spreads it over three lines. The core writes
it on one in **294 of 300 sampled files**.

### Group 2 — the seven rules that would destroy DocBlocks

```php
'no_superfluous_phpdoc_tags'                    => false,
'phpdoc_no_package'                             => false,
'phpdoc_no_empty_return'                        => false,
'phpdoc_separation'                             => false,
'phpdoc_trim_consecutive_blank_line_separation' => false,
'phpdoc_summary'                                => false,
'phpdoc_align'                                  => ['align' => 'left'],
```

The decision behind them: **complete DocBlock tags on every class, property and method**,
even where the native type carries the same information.

`no_superfluous_phpdoc_tags` removes exactly those — it considers `@param string $x`
redundant next to `string $x`. For the machine it is; for `@throws`, `@template` and
generic types (`array<int, Foo>`, which PHP has no native form for) it is not, and there is
no rule that removes the one kind and keeps the other.

**These seven are the counterpart to the eleven Rector skip rules**
([RECTOR.md](RECTOR.md)). Disable them in only one tool and the gate oscillates.

### Group 3 — global classes are not imported

```php
'global_namespace_import' => [
    'import_classes'   => false,
    'import_constants' => false,
    'import_functions' => false,
],
```

`\Throwable`, never `use Throwable;`. The leading backslash shows at the point of use that
the class is global, without scrolling to the file header.

### Group 4 — no Yoda

```php
'yoda_style' => [
    'equal'            => false,
    'identical'        => false,
    'less_and_greater' => false,
],
```

`if ($page > 0)`, never `if (0 < $page)`. Subject first, the way the sentence is read.

> Some plugins hold the **opposite** convention in their JavaScript, because the existing
> code was written that way. The rule is: **consistent within a plugin.** Which of the two
> applies is the plugin's decision, recorded once in an ADR.

### Group 5 — the Package attribute comes first

```php
'ordered_attributes' => ['order' => [Package::class], 'sort_algorithm' => 'custom'],
```

## Taken from the core

The remaining rules come from the core's own `.php-cs-fixer.dist.php`. Some fire daily,
others report nothing today — the latter are there to keep it that way:

```php
'attribute_empty_parentheses'   => ['use_parentheses' => false],
'class_attributes_separation'   => ['elements' => ['property' => 'one', 'method' => 'one']],
'concat_space'                  => ['spacing' => 'one'],
'general_phpdoc_annotation_remove' => ['annotations' => ['copyright', 'category']],
'method_argument_space'         => ['on_multiline' => 'ensure_fully_multiline'],
'native_function_invocation'    => ['scope' => 'namespaced', 'strict' => false, 'exclude' => ['ini_get']],
'no_useless_else'               => true,
'no_useless_return'             => true,
'ordered_class_elements'        => true,
'ordered_imports'               => ['sort_algorithm' => 'alpha'],
'phpdoc_annotation_without_dot' => false,
'phpdoc_line_span'              => true,
'phpdoc_order'                  => ['order' => ['param', 'throws', 'return']],
'phpdoc_to_comment'             => false,
'php_unit_dedicate_assert'      => ['target' => 'newest'],
'php_unit_dedicate_assert_internal_type' => true,
'php_unit_mock'                 => true,
'php_unit_test_case_static_method_calls' => ['methods' => [
    'any' => 'this', 'never' => 'this', 'atLeast' => 'this', 'atLeastOnce' => 'this',
    'once' => 'this', 'exactly' => 'this', 'atMost' => 'this',
]],
'self_accessor'                 => false,
'single_line_throw'             => false,
'static_lambda'                 => false,
'strict_comparison'             => true,
'strict_param'                  => true,
'void_return'                   => true,
```

**`general_phpdoc_annotation_remove` with `copyright` and `category`** enforces the rule
that class files carry no copyright header: write one and the next `gate:fix` removes it.
The licence belongs in `LICENSE` and `composer.json`, where it is maintained — a copy in
a hundred files is one that nobody updates and that eventually states something false with
authority.

**`native_function_invocation` with `scope: namespaced`** writes `\count()` instead of
`count()`. Inside a namespace PHP looks for a function locally first, then globally; the
leading backslash skips that lookup. `ini_get` is excluded because the core excludes it.

## Running it

```bash
composer cs       # php-cs-fixer fix --dry-run --diff
composer cs-fix   # php-cs-fixer fix
```

`cs-fix` runs in `gate:fix` **after** Rector; `cs --dry-run` runs in `gate:check` to prove
the fix pass was complete.

## Exact version pinning

```json
{
    "require-dev": {
        "friendsofphp/php-cs-fixer": "3.95.15"
    }
}
```

**Pinned exactly.** A new minor adds rules to existing sets, and the next run reformats a
thousand lines nobody touched.
