# Shopware 6 — The Plugin's Own `#[Package]` Attribute

**Every plugin brings its own `#[Package]` attribute.** Shopware's own one is not used.

## Why not the core's

`Shopware\Core\Framework\Log\Package` is marked **`@internal`**, and its `PackageString`
type enumerates the core's domains only (`core`, `checkout`, `content`, …).

A plugin that uses it has two problems:

1. It reaches into API marked internal — a broken contract that is allowed to break on any
   minor version.
2. It has to be excused from static analysis, because its own domain name is not in the
   whitelist — that is, an `ignoreErrors` entry, which `level: max` without `ignoreErrors`
   rules out.

## The plugin's own version

`src/Framework/Log/Package.php`:

```php
<?php declare(strict_types=1);

namespace {PluginName}\Framework\Log;

/**
 * Names the area of this plugin a class belongs to.
 *
 * Shopware's own `Shopware\Core\Framework\Log\Package` is marked `@internal`, and its
 * `PackageString` type lists the core's own domains only, so a plugin using it both
 * reaches into internal api and has to be excused from static analysis. This one
 * carries the same meaning without either cost.
 *
 * Its behaviour mirrors the core class exactly, verified against
 * vendor/shopware/core/Framework/Log/Package.php at v6.7.14.0: the same constant, the
 * same signature, the same answers including the parent class lookup. Only the
 * `PackageString` restriction is dropped, which is the reason it exists.
 *
 * Nothing is lost by the substitution: the core reads its own attribute at runtime only
 * for controllers and exceptions, through PackageService, and this plugin ships neither.
 *
 * @class Package
 * @package
 */
#[Package('{PluginName}.Framework')]
#[\Attribute(\Attribute::TARGET_CLASS)]
final class Package
{
    public const string PACKAGE_TRACE_ATTRIBUTE_KEY = 'pTrace';

    public function __construct(public string $package)
    {
    }

    /**
     * @throws \ReflectionException
     */
    public static function getPackageName(string $class, bool $tryParentClass = false): ?string
    {
        if (!class_exists($class)) {
            return null;
        }

        $package = self::evaluateAttributes($class);

        if ($package !== null || !$tryParentClass) {
            return $package;
        }

        $parentClass = get_parent_class($class);

        if ($parentClass !== false && ($package = self::evaluateAttributes($parentClass)) !== null) {
            return $package;
        }

        return null;
    }

    /**
     * @param class-string $class
     * @throws \ReflectionException
     */
    private static function evaluateAttributes(string $class): ?string
    {
        $attributes = (new \ReflectionClass($class))->getAttributes(self::class);

        if ($attributes === []) {
            return null;
        }

        $arguments = $attributes[0]->getArguments();

        return isset($arguments[0]) && \is_string($arguments[0]) ? $arguments[0] : null;
    }
}
```

**The DocBlock is exceptionally verbose here** — it is the justification for a class that
at first glance looks like a redundant copy. Exactly this knowledge belongs on the class,
because the question "why not the one from the core?" arises immediately on reading. That
is the exception to the no-prose-comments rule, not its repeal.

**The attribute carries itself** (`#[Package('{PluginName}.Framework')]`). That is not
circular; it allows the convention test to run over *all* classes without exception.

## Usage

```php
#[Package('{PluginName}.{Area}')]
final class ProductBadgeLoader
{
}
```

**On every class**, on tests too, on the attribute itself too. The areas are decided per
plugin, for example:

```
{PluginName}.Core
{PluginName}.Storefront
{PluginName}.Administration
{PluginName}.Framework
{PluginName}.Tests
```

**It always comes first**, enforced by php-cs-fixer.

## What this removes

```neon
# No ignoreErrors block: this plugin carries its own Package attribute, so the core's
# whitelist of domain names never applies to it.
```

That is the tangible gain: no `ignoreErrors` in `phpstan.neon`.

→ Where the file lives in the tree: [PLUGIN-STRUCTURE.md](PLUGIN-STRUCTURE.md)
