# Shopware 6 — Rector

Rector is the only tool in the gate that does not merely format code but **rewrites** it.

## The configuration, complete

`rector.php` in the plugin root:

```php
<?php declare(strict_types=1);

use Frosh\Rector\Set\ShopwareSetList;
use Rector\CodeQuality\Rector\Class_\ConvertStaticToSelfRector;
use Rector\Config\RectorConfig;
use Rector\DeadCode\Rector\ClassMethod\RemoveDuplicatedReturnSelfDocblockRector;
use Rector\DeadCode\Rector\ClassMethod\RemoveMixedDocblockOverruledByNativeTypeRector;
use Rector\DeadCode\Rector\ClassMethod\RemoveNullTagValueNodeRector;
use Rector\DeadCode\Rector\ClassMethod\RemoveReturnTagIncompatibleWithNativeTypeRector;
use Rector\DeadCode\Rector\ClassMethod\RemoveUselessParamTagRector;
use Rector\DeadCode\Rector\ClassMethod\RemoveUselessReturnTagRector;
use Rector\DeadCode\Rector\ClassMethod\RemoveUselessUnionReturnDocblockRector;
use Rector\DeadCode\Rector\ClassMethod\RemoveVoidDocblockFromMagicMethodRector;
use Rector\DeadCode\Rector\Node\RemoveNonExistingVarAnnotationRector;
use Rector\DeadCode\Rector\Property\RemoveUselessReadOnlyTagRector;
use Rector\DeadCode\Rector\Property\RemoveUselessVarTagRector;
use Rector\Php83\Rector\ClassMethod\AddOverrideAttributeToOverriddenMethodsRector;

return RectorConfig::configure()
    ->withPaths([
        __DIR__ . '/src',
        __DIR__ . '/tests',
    ])
    // reflection on Shopware parent classes needs the project autoloader
    ->withBootstrapFiles([
        __DIR__ . '/../../../vendor/autoload.php',
    ])
    ->withRootFiles()
    ->withPhpSets(php83: true)
    ->withPreparedSets(
        deadCode:         true,
        codeQuality:      true,
        typeDeclarations: true,
        privatization:    true,
        earlyReturn:      true,
    )
    // The released version only. The next major's set is deliberately absent: the plugin
    // declares a conflict with it, so applying its rules would write code the shop
    // cannot run.
    ->withSets([
        ShopwareSetList::SHOPWARE_6_7_0,
    ])
    ->withRules([
        AddOverrideAttributeToOverriddenMethodsRector::class,
    ])
    ->withSkip([
        // Complete DocBlock tags are mandatory. Every rule below removes tags this
        // project requires. Verified by running the gate twice against a reference
        // class and comparing the tag count.
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
        // the core writes static:: in assertions 22562 times against 48 self::
        ConvertStaticToSelfRector::class,
    ])
    ->withImportNames(importShortClasses: false, removeUnusedImports: true)
    ->withParallel();
```

## The three settings that are not optional

**`withBootstrapFiles` on the PROJECT vendor.** Rector uses reflection to inspect parent
classes. Without the project's autoloader it does not know
`Shopware\Core\Framework\Plugin` and cannot decide whether a method overrides anything.

**`withRootFiles()`** includes `rector.php` and `.php-cs-fixer.dist.php` themselves. They
are PHP and obey the same rules.

**`withImportNames(importShortClasses: false, …)`** keeps global classes written out
(`\Throwable`, never `use Throwable;`), matching php-cs-fixer's
`global_namespace_import`.

## The one rule worth adding by hand

```php
->withRules([AddOverrideAttributeToOverriddenMethodsRector::class])
```

It puts `#[Override]` on every method that overrides or implements something. **In a
plugin this is the single most useful rule there is:** when Shopware renames a method in a
minor version, a silent stops-overriding turns into a hard error — visible at once instead
of weeks later in production.

## Never the next major's set

The Rector set matches the version the plugin is released for — **never the one after**.
This follows directly from the `conflict` block in `composer.json`: applying the next
major's rules writes code the shop is not allowed to run.

> **A real finding:** an earlier configuration named `ShopwareSetList::SHOPWARE_6_8_0` —
> a class constant that **does not exist** in the installed version of
> `frosh/shopware-rector`. Rector ran anyway, because PHP only complains about an unknown
> class constant when it is accessed, and that path was never reached.
>
> A configuration that "runs" is not the same as one that takes effect.

## The twelve skip rules

Eleven of them remove DocBlock tags the annotation standard requires. They are the
counterpart to the seven php-cs-fixer rules in
[ECS-CS-FIXER.md](ECS-CS-FIXER.md) — **both tools have to be switched off.** Disable only
one and the other deletes the tags, and the gate oscillates: one tool writes them, the
next removes them, and two runs never leave the same tree.

The twelfth has a different reason: `ConvertStaticToSelfRector` would rewrite
`static::assertSame()` to `self::assertSame()`. The core writes `static::` — 22 562 times
against 48 — so following the core here keeps a test copied out of it from being
reformatted.

## How it is used

```bash
composer rector      # rector process --dry-run --no-progress-bar
composer rector:fix  # rector process --no-progress-bar
```

**The dry run comes first, and its suggestions are read.** Rector is not an oracle: it
occasionally proposes something that is correct code but obscures the intent — an early
return that tears apart a deliberately symmetric case distinction, say. Then the rule goes
into `withSkip()` **with a one-line comment naming the reason**. Not silently.

In the gate, `rector:fix` runs in `gate:fix` **before** php-cs-fixer (Rector's output is
correct but unformatted), and `rector --dry-run` runs in `gate:check` to prove the fix
pass was complete.

→ Major upgrades and Shopware's own deprecation rules: the `shopware-migration` plugin.
