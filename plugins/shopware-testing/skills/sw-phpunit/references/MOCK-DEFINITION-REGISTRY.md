---
title: Compile DAL definitions without a kernel — and the static cache that silently breaks it
impact: HIGH
impactDescription: Makes definition assertions possible in unit tests, and prevents mutation testing from reporting a score built on stale fields
tags: mock, dal, definition, unit-test, mutation
---

## Compiling a definition without booting the kernel

A unit test that asserts on a DAL definition — its fields, their flags, their descriptions
— needs the definition **compiled**, which normally means a kernel. It does not have to.

`StaticDefinitionInstanceRegistry` compiles definitions on its own:

```php
<?php declare(strict_types=1);

namespace {PluginNamespace}\Tests\Helper;

use Shopware\Core\Content\Category\CategoryDefinition;
use Shopware\Core\Content\Media\MediaDefinition;
use Shopware\Core\Framework\DataAbstractionLayer\EntityDefinition;
use Shopware\Core\System\Language\LanguageDefinition;
use Shopware\Core\Test\Stub\DataAbstractionLayer\StaticDefinitionInstanceRegistry;
use Shopware\Core\Test\Stub\DataAbstractionLayer\StaticEntityWriterGateway;
use Symfony\Component\Validator\Validation;

final class TestDefinitionRegistry
{
    private static ?StaticDefinitionInstanceRegistry $registry = null;

    /**
     * @template TDefinition of EntityDefinition
     * @param class-string<TDefinition> $definitionClass
     * @return TDefinition
     */
    public static function get(string $definitionClass): EntityDefinition
    {
        $definition = self::registry()->get($definitionClass);

        \assert($definition instanceof $definitionClass);

        return $definition;
    }

    /**
     * A definition that has never been compiled, so defineFields() still runs on it.
     *
     * @template TDefinition of EntityDefinition
     * @param class-string<TDefinition> $definitionClass
     * @return TDefinition
     */
    public static function uncompiled(string $definitionClass): EntityDefinition
    {
        $definition = (new \ReflectionClass($definitionClass))->newInstanceWithoutConstructor();

        \assert($definition instanceof $definitionClass);

        return $definition;
    }

    /**
     * A definition compiled into a registry of its own, so `defineFields()` runs for
     * this call rather than being answered from the shared cache.
     *
     * @template TDefinition of EntityDefinition
     * @param class-string<TDefinition> $definitionClass
     * @return TDefinition
     */
    public static function freshlyCompiled(string $definitionClass): EntityDefinition
    {
        $definition = self::buildRegistry()->get($definitionClass);

        \assert($definition instanceof $definitionClass);

        return $definition;
    }

    private static function registry(): StaticDefinitionInstanceRegistry
    {
        return self::$registry ??= self::buildRegistry();
    }

    private static function buildRegistry(): StaticDefinitionInstanceRegistry
    {
        return new StaticDefinitionInstanceRegistry(
            [
                // Class names rather than instances: EntityDefinition::__construct()
                // is deprecated, and the registry builds them itself.
                MyEntityDefinition::class,
                MyEntityTranslationDefinition::class,
                // Every associated definition has to be listed, or compiling the
                // association fails.
                CategoryDefinition::class,
                MediaDefinition::class,
                LanguageDefinition::class,
            ],
            Validation::createValidator(),
            new StaticEntityWriterGateway(),
        );
    }
}
```

## The trap: `get()` caches statically

**`get()` answers from a registry built the first time any test asked for one.** A test
asserting on what `defineFields()` produces therefore reads fields that were built
**before its own arrangement took effect**.

In an ordinary test run this is invisible — the fields are the same either way. It becomes
visible under **mutation testing**, and there it is fatal:

> Every mutant inside the definitions survives **by construction**. The tests read fields
> compiled before the mutant was applied, so no mutation in `defineFields()` can ever be
> killed, and the score for that file is meaningless.

**Use `freshlyCompiled()` in any test that asserts on `defineFields()` output.** It builds
a registry of its own, so the compilation happens for that call.

| Method | When |
|---|---|
| `get()` | most tests — fast, shared cache, fine when the fields are only read |
| `freshlyCompiled()` | **any assertion on what `defineFields()` produced**, and anything that will be mutation-tested |
| `uncompiled()` | when the definition must not be compiled at all |

## What is asserted with it

Two convention tests belong on every DAL definition. They live **beside the definition's
own test**, not in a separate conventions directory: whoever changes the definition opens
that file.

**Every field explains itself:**

```php
public function testEveryFieldExplainsItselfToTheApi(): void
{
    $offenders = [];

    foreach ($this->definition()->getFields() as $field) {
        // createdAt, updatedAt and translated are added by the data abstraction
        // layer itself, so they are not ours to describe.
        if (\in_array($field->getPropertyName(), self::FIELDS_THE_DAL_ADDS, true)) {
            continue;
        }

        $description = $field->getDescription();

        if (mb_strlen($description) < 15 || !str_ends_with($description, '.')) {
            $offenders[] = $field->getPropertyName();
        }
    }

    static::assertSame([], $offenders, 'every field explains itself in a full sentence');
}
```

Three details make it usable: the DAL's own fields are skipped, a **minimum length**
catches a keyword where a regex on capitalisation would not, and violations are
**collected** so the failure names every field at once rather than the first.

**No association loads itself uninvited:**

```php
public function testNoAssociationLoadsItselfUninvited(): void
{
    $autoloading = [];

    $definition = TestDefinitionRegistry::freshlyCompiled(MyEntityDefinition::class);

    foreach ($definition->getFields() as $field) {
        if ($field instanceof AssociationField && $field->getAutoload()) {
            $autoloading[] = $field->getPropertyName();
        }
    }

    static::assertSame([], $autoloading, 'an association is loaded because it was asked for');
}
```

`autoload` on an association drags the other side along on **every** query — including
behind every search in the administration.

**The field list is complete**, as a provider:

```php
public static function expectedFieldProvider(): \Generator
{
    foreach (['id', 'active', 'position', 'name', 'mediaId', 'media', 'categories'] as $property) {
        yield $property => [$property];
    }
}
```

This is the counterpart to the two above: they check **every present** field for a
property, this one checks that the **expected fields are present**. A test iterating
`getFields()` passes when a field silently disappears — and against a schema running in
live shops, a vanished field is the most expensive defect there is.

→ Repository stubs and the callable trick: [MOCK-REPOSITORY.md](MOCK-REPOSITORY.md)
