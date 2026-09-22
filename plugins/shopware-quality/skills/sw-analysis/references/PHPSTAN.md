# Shopware 6 — PHPStan

**`level: max`, from the start, with no `ignoreErrors` block.**

## The configuration, complete

`phpstan.neon` in the plugin root:

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
            # php-cs-fixer and Rector bundle their own prefixed Symfony copies.
            # phpstan-symfony resolves against them and fails on the prefixed namespace.
            - vendor/friendsofphp
            - vendor/rector
            # Both npm trees ship a stray PHP file of their own.
            - src/Resources/app/administration/node_modules
            - src/Resources/app/storefront/node_modules
    tmpDir: var/phpstan
    treatPhpDocTypesAsCertain: false
    reportUnmatchedIgnoredErrors: true

    phpat:
        show_rule_names: true

    type_perfect:
        no_mixed_property: true
        no_mixed_caller: true
        null_over_false: true

services:
    -
        class: {PluginNamespace}\Tests\Architecture\LayerTest
        tags:
            - phpat.test
```

## `level: max`, and why not a lower one

The level is set to `max` at the start, never raised gradually.

**A level you plan to raise later is one you never raise.** At level 6 it is twenty
errors, at level 8 two hundred, and from there raising it is a project of its own that
nobody starts. Starting at `max` means having the errors at the moment of writing —
one at a time, in code you still have in your head.

## No `ignoreErrors`, and no baseline

A suppressed error is an error that stays, plus a line that hides the fact. When PHPStan
reports something there are three acceptable answers:

1. The code is wrong → fix the code
2. The type is described imprecisely → sharpen the DocBlock (`@var`, `@param`, `@template`)
3. PHPStan cannot know → write an `assert()` that states the type for reader **and**
   machine, and checks it at runtime

A fourth — ignoring it — is not among them. `reportUnmatchedIgnoredErrors: true` makes an
ignore entry that no longer matches an error in itself.

**A baseline is the same thing at scale.** It is defensible exactly once: taking over a
legacy plugin, as a record of what was inherited, with a commitment to shrink it. It is
not a working state.

## The paths

**`scanDirectories: ../../../vendor` points at the PROJECT vendor**, not the plugin's.
Shopware lives there. Without it PHPStan does not know the parent classes and reports
every overridden method as unknown.

The four `excludePaths` have two distinct causes:

| Path | Cause |
|---|---|
| `vendor/friendsofphp`, `vendor/rector` | both bundle a **prefixed** copy of Symfony. `phpstan-symfony` tries to resolve against it and fails on the prefix |
| both `node_modules` | each npm tree ships one stray PHP file — `flatted` carries a PHP port beside its JavaScript. Somebody else's code |

## The five extensions

Registered by `phpstan/extension-installer`, not by hand:

| Extension | What it adds |
|---|---|
| `phpstan-strict-rules` | bans loose comparisons, implicit casts, `switch` without `default` |
| `phpstan-phpunit` | understands `assert*()` as a type narrowing and knows `MockObject` |
| `phpstan-symfony` | knows the container, catches wrong service ids |
| `phpstan-deprecation-rules` | reports every call to something `@deprecated` |
| `phpat` | architecture rules as PHPStan rules |

**`phpstan-deprecation-rules` is the one that matters most for maintenance.** Without it a
deprecation surfaces when the next major removed it and the plugin fatals in production.
With it the finding is in the gate, months earlier — and it is what
`UPGRADE-<next>.md` is written from.

## `rector/type-perfect`

Three rules PHPStan does not enforce even at `max`:

```neon
type_perfect:
    no_mixed_property: true   # no property without a precise type
    no_mixed_caller: true     # no method call on a mixed
    null_over_false: true     # "found nothing" is null, not false
```

**`null_over_false`** is the interesting one. A method returning `false` for "found
nothing" forces every caller into `=== false` — and once the return type is
`bool|Something`, the signature no longer says whether `false` is a result or an absence.
`null` is unambiguous, and `?->` and `??` work with it.

## `treatPhpDocTypesAsCertain: false`

By default PHPStan believes a DocBlock. Given `@param string $x` it treats `$x` as
guaranteed and reports `is_string($x)` as always true — dead code.

That is wrong at a **public API boundary**. A DocBlock is the author's claim, not a
contract the runtime enforces; an outside caller can pass anything. With `false`, defensive
checks at the edges survive instead of being reported as redundant.

## Exact version pinning

```json
{
    "require-dev": {
        "phpstan/phpstan": "2.2.8"
    }
}
```

**Pinned exactly, without `^`.** A new minor finds new errors in unchanged code, and the
gate turns red without anybody having done anything.

## Running it

```bash
composer phpstan     # phpstan analyse --memory-limit=1G
```

Part of `gate:check`, and the first check in it: it finds the most real defects and takes
the longest, so a failure surfaces early rather than after three faster checks passed.

## The trap

**A stale result cache reports errors that are not there.** When assertions suddenly fail
to resolve:

```bash
rm -rf var/phpstan
```

→ Shopware's own rules: [PHPSTAN-SHOPWARE.md](PHPSTAN-SHOPWARE.md)
→ Architecture rules through phpat, and why not Deptrac: the `sw-testing-standard` skill
  in the `shopware-testing` plugin.
