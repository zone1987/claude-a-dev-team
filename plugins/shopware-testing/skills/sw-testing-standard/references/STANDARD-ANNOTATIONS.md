# Annotations, and the rules that must stay disabled

This is a testing standard, so why annotations? Because **the gate deletes them on every
run unless nineteen rules are switched off**, and a gate that quietly removes what the
project requires is worse than no gate.

## The rule

Every class, property and method carries the conventional DocBlock tags — `@class`,
`@package`, `@param`, `@return`, `@throws`, `@var`. Tags only, never prose.

```php
/**
 * @class FreeShippingThresholdResolver
 * @package YourPlugin
 */
#[Package('YourPlugin')]
final class FreeShippingThresholdResolver
{
    /**
     * @param ShippingMethodPriceCollection $prices
     * @param string $currencyId
     * @param bool $taxStateIsGross
     * @throws \InvalidArgumentException
     * @return int|null
     */
    public function resolve(…): ?int
    {
    }
}
```

**This deliberately deviates from Shopware core**, which documents only what native types
cannot express. Measured against `vendor/shopware/core`: `@class` appears zero times,
`@package` once as a DocBlock. The core uses the `#[Package]` attribute instead.

Generic and shape types (`list<>`, `array<k,v>`, `Collection<>`) are mandatory wherever
they apply. Adding tags never removes type information.

`#[Package('YourPlugin')]` is used **in addition**, as the core does, because Shopware
reads the attribute at runtime while `@package` is inert. It needs an ignore rule in
`phpstan.neon` — the attribute declares a whitelist of core domain names.

## The nineteen rules that must be off

### php-cs-fixer — seven

```php
'no_superfluous_phpdoc_tags' => false,
'phpdoc_no_package' => false,
'phpdoc_no_empty_return' => false,
'phpdoc_separation' => false,
'phpdoc_trim_consecutive_blank_line_separation' => false,
'phpdoc_summary' => false,
'phpdoc_align' => ['align' => 'left'],
```

### Rector — twelve

```php
->withSkip([
    RemoveUselessParamTagRector::class,
    RemoveUselessReturnTagRector::class,
    RemoveUselessVarTagRector::class,
    RemoveDuplicatedReturnSelfDocblockRector::class,
    RemoveMixedDocblockOverruledByNativeTypeRector::class,
    RemoveNullTagValueNodeRector::class,
    RemoveReturnTagIncompatibleWithNativeTypeRector::class,
    RemoveUselessUnionReturnDocblockRector::class,
    RemoveVoidDocblockFromMagicMethodRector::class,
    RemoveUselessReadOnlyTagRector::class,
    RemoveNonExistingVarAnnotationRector::class,
    // The core writes static:: in assertions 22562 times against 48 self::.
    ConvertStaticToSelfRector::class,
])
```

**Leave any of them on and the gate removes on every run exactly what the project
requires.** The removal is silent: the run reports success, and the tags are gone.

## The check that proves it

One run proves nothing. A fixer that strips one tag per pass looks stable until the second:

```bash
composer gate
find src tests -name "*.php" -not -path "*/Acceptance/*" | sort | xargs shasum | shasum
composer gate
find src tests -name "*.php" -not -path "*/Acceptance/*" | sort | xargs shasum | shasum
```

Identical checksums, or a rule is still active. Counting tags works too:

```bash
grep -rhoE "@(class|package|param|return|throws|var)\b" src tests --include="*.php" | wc -l
```

**This check belongs in the acceptance of the gate**, not in a note somewhere.

## Two style rules that also matter

**`<?php declare(strict_types=1);` on one line.** The core writes it that way in 294 of 300
sampled files:

```php
'blank_line_after_opening_tag' => false,
'linebreak_after_opening_tag' => false,
```

**No Yoda notation.** A comparison reads subject first:

```php
'yoda_style' => ['equal' => false, 'identical' => false, 'less_and_greater' => false],
```

`if ($amount >= $threshold)`, never `if ($threshold <= $amount)`.

## No prose comments

No multi-line explanations, reasoning, trade-offs or decision history in code.

**Permitted:** a single line on a non-obvious constraint, a short DocBlock on public API,
`TODO`/`FIXME` with a concrete reference, tool directives.

**Reasoning goes to** an ADR, `CONTEXT.md`, or a test name that states the rule.

The reason is not brevity. A paragraph explaining *why* sits next to code that changes; the
code moves, the paragraph stays, and within a few releases the file carries a confident
explanation of something no longer true. A test called
`rejects_a_free_shipping_row_that_has_an_upper_bound` states the rule **and fails when the
rule stops holding**. A comment does neither.

**Copyright headers come out.** Author, licence and copyright live in `LICENSE` and
`composer.json`, where they are maintained. In a class they are a copy nobody updates: the
year goes stale, a licence change is corrected in one place and missed in a hundred, and
the company name survives a change of owner. A statement repeated in a hundred files and
maintained in one asserts something false with authority.

```php
'general_phpdoc_annotation_remove' => ['annotations' => ['copyright', 'category']],
```

## An architecture test can check the tags

PHPStan verifies that a `@param` matches the type; it does not verify that the tag exists.
A file-walking test closes that gap:

```php
#[DataProvider('phpFiles')]
public function testEveryMethodDocumentsItsSignature(string $file): void
```

Yield one case per file so a failure names the file. It catches the `@param` that was left
behind when a parameter was renamed — a wrong tag being worse than no tag.
