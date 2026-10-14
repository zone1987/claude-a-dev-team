# Plugin rules: Code and PHP conventions

## Contents

- [no-prose-comments: Prose comments are not written in any file type](#no-prose-comments-prose-comments-are-not-written-in-any-file-type)
- [complete-docblock-tags: DocBlocks carry complete tags and nothing but tags, and no tool strips them](#complete-docblock-tags-docblocks-carry-complete-tags-and-nothing-but-tags-and-no-tool-strips-them)
- [throws-where-known: @throws names every exception PhpStorm reports and is never guessed](#throws-where-known-throws-names-every-exception-phpstorm-reports-and-is-never-guessed)
- [classes-and-functions-are-imported: Classes and functions are imported, test classes use self::, and readonly is declared where possible](#classes-and-functions-are-imported-classes-and-functions-are-imported-test-classes-use-self-and-readonly-is-declared-where-possible)
- [every-phpstorm-inspection-is-resolved: Every PhpStorm inspection is resolved](#every-phpstorm-inspection-is-resolved-every-phpstorm-inspection-is-resolved)
- [php-conventions: PHP and Shopware code conventions](#php-conventions-php-and-shopware-code-conventions)
- [technical-folder-structure: Classes live where their kind belongs, names are derived, and the structure is technical, not DDD](#technical-folder-structure-classes-live-where-their-kind-belongs-names-are-derived-and-the-structure-is-technical-not-ddd)
- [services-registered-explicitly-in-php: Services, routes and bundle configuration are registered explicitly in PHP](#services-registered-explicitly-in-php-services-routes-and-bundle-configuration-are-registered-explicitly-in-php)
- [layers-enforced-by-architecture-rules: Layers are enforced by architecture rules, and transport, format and meaning are separate layers](#layers-enforced-by-architecture-rules-layers-are-enforced-by-architecture-rules-and-transport-format-and-meaning-are-separate-layers)
- [extension-through-tagged-registries: Extension goes through tagged registries and narrow interfaces](#extension-through-tagged-registries-extension-goes-through-tagged-registries-and-narrow-interfaces)
- [events-let-project-code-change-data: Events let project code change data](#events-let-project-code-change-data-events-let-project-code-change-data)
- [typed-readers-hold-each-field-path-once: Typed readers hold each field path exactly once](#typed-readers-hold-each-field-path-once-typed-readers-hold-each-field-path-exactly-once)
- [money-handling: Money is integer minor units, and net prices are stored unrounded like the core](#money-handling-money-is-integer-minor-units-and-net-prices-are-stored-unrounded-like-the-core)

## no-prose-comments: Prose comments are not written in any file type

**Area:** core **Status:** accepted

### Context

Long explanatory comments drift away from the code, repeat what names already say, and put the reasoning behind a decision in a place nobody checks. The same reasoning can be found and versioned as a decision record.

### Decision

- Prose comments are not written in PHP, JavaScript, Twig, SCSS, XML or configuration files. Multi-line blocks that tell background, trade-offs, history or comparisons are forbidden, even when they are correct.
- Allowed: a short single-line note for a restriction the code cannot show, DocBlock tags, `TODO` or `FIXME` with a concrete reference, and directives a tool requires, with a justification wherever the tool allows one (`@phpstan-ignore` with a reason, `eslint-disable-next-line`).
- Existing prose comments in a file that is touched are removed in the same change.
- Reasoning belongs in an ADR, state and pitfalls belong in `CONTEXT.md` and the commit message, and intent belongs in the name of a test (for example a test that rejects a path containing `..`).
- No copyright, author or license headers in source files. Every PHP file starts on line one with `<?php declare(strict_types=1);`, followed by the namespace.
- `CodingStyleTest` fails on a block comment that is not a DocBlock and on two consecutive `//` comment lines in `src/` and `tests/`.

### Consequences

The code stays short. A reader finds the reasoning in `adr/`, and tests name the rule they protect. The gate checks both, which it cannot do for a comment.

## complete-docblock-tags: DocBlocks carry complete tags and nothing but tags, and no tool strips them

**Area:** core **Status:** accepted

### Context

Free text in DocBlocks duplicates names and drifts apart. Types that PHP cannot express (generics, array shapes, thrown exceptions) have no other place, and tools such as PHPStan read them. Fixer rules that remove seemingly redundant tags silently delete this information.

Shopware core documents only what native types cannot express. Measured against `vendor/shopware/core` (6,385 PHP files):

| Tag | Occurrences | Observation |
|---|---|---|
| `@class` | 0 | not used at all |
| `@package` | 39 | only 1 in PHP, the rest in CSS. Core uses the attribute `#[Package]` |
| `@param` | 4,300 | 2,823 (66 %) carry generics or shapes |
| `@param` with prose | 160 | 3.7 % of all `@param` tags |
| `@return` | 3,082 | predominantly generics |

`Shopware\Core\Checkout\Cart\SalesChannel\CartService` is representative: eleven promoted constructor parameters, not one `@param`.

The plugins deviate from the core on purpose. The reason is not that the tags carry more type information, because mostly they do not. The reason is that a missing tag is invisible while a wrong one is loud. A DocBlock that lists every parameter fails visibly when a parameter is renamed and the tag is not, and a DocBlock that lists none never fails at all. A rule that demands tags only where they add information sounds right but cannot be decided in daily work, because every file becomes a case-by-case judgment. The trade-off was put to the plugin owner explicitly, with the numbers above, and the decision was to require complete tags regardless.

The cost is real. Eleven or twelve Rector rules (depending on the version) and seven php-cs-fixer rules remove exactly these tags as redundant, eighteen rules in total. With any of them active, the gate deletes on every run what the project requires, and it reports success while doing so. Modern PHP types also make many tags technically superfluous: a `@param string $code` above a method with `string $code` in the signature only repeats what the interpreter enforces. The two things native types cannot do are describing the content of an array and naming the exception a method throws, and PHPStan at level `max` needs exactly that.

Version 2.0.0 of one plugin already required DocBlocks with pure type information. The rule and the tool settings that protect it are recorded here.

### Decision

- A DocBlock contains only tags: `@class`, `@package`, `@param`, `@return`, `@var`, `@throws`, `@extends`, `@implements`, `@template`. No summary line, no description after a type, no `@example`. One tag per line, and a long tag may continue on indented follow-up lines.
- Every class, property and method carries the applicable tags completely. Every class, interface, enum and trait has `@class` and `@package`. Every class and method carries `@class`, `@param` and `@return` with one tag per line. Every parameter and the return type are tagged with full generic or shape types. Properties carry `@var`.
- `@package` names the namespace the class lives in, not the area. It is a PhpDocumentor tag and takes a namespace.
- `#[Package('<Plugin>.<Area>')]` names the area as an attribute, in addition. The two say different things and are not copies of one another. The attribute is read by Shopware at runtime while `@package` is not. It comes from the plugin's own `Framework\Log\Package` class, and every class carries it.
- `@return void` is always written.
- Constructors carry `@param` and `@throws`, never `@return`. Promoted properties are documented through the constructor `@param`.
- Generic and shape types (`list<>`, `array<k,v>`, `Collection<>`) are mandatory wherever they apply. This decision adds tags and never removes type information.
- Closures, anonymous classes and generated code carry no DocBlock.
- Free-text blocks are not allowed. The only comments besides tags are short single-line notes for a non-obvious restriction.
- Example of the required form:

```php
/**
 * @class SourcingOptimizer
 * @package <Plugin>.Sourcing
 */
final class SourcingOptimizer
{
    /**
     * @param list<SourcingCandidate> $candidates
     * @param SourcingContext $context
     * @return SourcingPlan
     * @throws NoEligibleOfferException
     */
    public function optimize(array $candidates, SourcingContext $context): SourcingPlan
    {
    }
}
```

- The rules that would strip these tags are disabled in `rector.php`, `.php-cs-fixer.dist.php` and, for projects using ECS, `ecs.php`. The list is not negotiable and is not trimmed. At minimum:

```text
PhpCsFixer\Fixer\Phpdoc\NoSuperfluousPhpdocTagsFixer
PhpCsFixer\Fixer\Phpdoc\PhpdocNoUselessInheritdocFixer
Rector\...\RemoveUselessParamTagRector
Rector\...\RemoveUselessReturnTagRector
```

- A Rector or php-cs-fixer rule that removes a tag is a configuration error.
- A verification step confirms that two consecutive gate runs leave the tree byte-identical. A fixer that strips one tag per pass looks stable after a single run.
- `CodingStyleTest` checks `@class` and `@package` on every class in `src/` and that no DocBlock line is a descriptive sentence.
- The rules for `@throws` are in the decision `throws-where-known`.

> Earlier variant: one older decision wrapped nothing and demanded one line per tag, never wrapped. Another listed only `@class`, `@param`, `@return` and `@throws` without `@package`.

### Consequences

The gate leaves DocBlocks untouched in both passes. A new exception means adding the tag in the same change. Reasoning lives in ADRs and types live in tags.

Files become longer and part of the tags repeats the signature. That is the price for a rule that can be applied without weighing. A DocBlock has to be maintained together with the signature it describes, and a stale tag is worse than none. PHPStan reports the contradiction, so the gap is noticed. The setup deviates from core, so contributors familiar with Shopware will find it unusual. The disabled fixers also stop cleaning up genuinely stale tags elsewhere, so code review carries that burden. A wrong `@param` is worse than none, so PHPStan at level max must verify them.

PHPStan with level max requires complete type information. A class without `@class`, a parameter without `@param` or a return without `@return` annoys PHPStan and can make static analysis fail. IDE tools find the code immediately, and maintenance gets easier because types are documented without reading prose.

`php-cs-fixer` removes the variable name from `@var` tags (`phpdoc_var_without_name`, part of `@Symfony`). This is accepted rather than fought, as in the reference plugins. `@param` and `@return` keep their names.

Rector writes `#[\Override]` when it adds the attribute. php-cs-fixer runs afterwards in `composer gate:fix` and turns it into an import, so committed code never shows the qualified form.

## throws-where-known: @throws names every exception PhpStorm reports and is never guessed

**Area:** core **Status:** accepted

### Context

`@throws` is the most useful and at the same time the most easily misused tag. It tells the caller what to expect, and nobody checks whether it is true. Two failure modes follow. A missing tag hides an exception the caller should handle. A guessed tag claims an exception that never occurs and makes the caller write code for a case that does not exist.

The common case is a method that throws nothing itself and calls Shopware code that declares nothing either. That covers most of the DAL, and `EntityRepository::search()` carries no `@throws` in the core. In one measured plugin, `src/` contained no `throw` statement at all, and every exception that could leave it came from something it called.

PhpStorm flags such methods as incomplete. An earlier position held that "this might throw something somewhere" is not a fact a DocBlock can state without inventing it. A method that writes `throw new X()` itself knows exactly which X it is, while a method that calls another method might pass its error on but does not know what all callers throw.

PhpStorm reports missing `@throws` as an inspection hint, and the decision `every-phpstorm-inspection-is-resolved` requires every hint to be fixed.

### Decision

- `@throws` is declared everywhere PhpStorm reports an exception, including `Exception`, `ExceptionInterface`, `RandomException` and `ReflectionException`.
- Where the exception can be avoided through the code, the code is changed instead. Example: `DateTimeImmutable::setTimestamp` instead of `modify`, so that no `DateMalformedStringException` can arise.
- `@throws` lists every exception a method raises itself and every exception a callee declares and that is not caught here. Nothing is added on suspicion. A `@throws Throwable` on a method that cannot throw one is a defect. Checking means reading: when it is unclear whether a core call throws, the source in the installed version is looked up.
- An exception that is caught in the method is not declared. Example: a registry of price calculators throws `RuntimeException` for an unknown price type, a payload builder catches it and skips the position, so the payload builder's `build()` declares nothing. A decorator that deliberately catches `Throwable` lets nothing escape, so a `@throws` there would be false.
- Domain errors are the plugin's own domain exception with factory methods, and the API client throws its own API exception. A bare `RuntimeException` is not thrown. Where the plugin grows exceptions of its own, every one of them is declared.
- The reverse check is cheap: `grep -rn "throw new" src/` against `grep -rn "@throws" src/`. Anything thrown and not declared is a fault, and anything declared and not thrown is stale.

> Earlier variant: `@throws` was declared only in three cases. The method throws the exception itself, something it calls declares it and it is not caught here, or the standard library throws it and the signature makes that plain (for example `ReflectionException` from a `ReflectionClass` on a class that may not exist, or `LoaderLoadException` from a delegating loader). Elsewhere nothing was written, a generic `Exception` was never declared, `@throws RuntimeException` was preferred over `@throws Exception`, an unclear case got no tag, a DAL call without its own `@throws` got none invented, and PhpStorm flags on such methods were left standing. A still earlier variant named the cases as the method throws it, it calls something that provably throws it and does not catch it, or static analysis requires it, and forbade a tag added only to quiet a tool whose warning was not understood.

### Consequences

The static analysis runs without errors and PhpStorm reports nothing. The DocBlock names every exception a caller can see, and a next developer cannot overlook a real error because a false one hides it. Where the code can be changed to remove an exception, it is changed, which keeps the tag list short.

## classes-and-functions-are-imported: Classes and functions are imported, test classes use self::, and readonly is declared where possible

**Area:** core **Status:** accepted

### Context

PHP allows `new \Throwable()` and `\count()` without an import. The code becomes longer, and the `\` reveals that an import is missing.

Two spellings side by side make every review a taste discussion. A file header should list everything the file uses, so that someone who wants to know which exceptions a class knows can read its imports instead of the whole class. The qualified form has an argument in its favor, namely that the origin of a class is visible at every place and the header stays short. Against it stands that two spellings coexist: everything from a namespace is imported except the global names. The core itself never imports global classes (in one measurement `\Throwable` appears 255 times and `use Throwable;` zero times), but a project rule that is written down and enforced beats following that habit.

### Decision

- Global classes and functions are imported with `use` and `use function`, never written as `\Foo` or `\count()` inline.
- Imports are fully qualified and without alias. Example: `use Exception;`, `use ReflectionClass;`, `use Throwable;`, then `catch (Throwable $exception)`, and `use function count;`.
- The rule holds in DocBlocks too. `@throws Exception` presumes the import and does not spell it out.
- A `use function` keeps the compile-time optimization.
- Two classes with the same name from different namespaces force an alias. That is rare.
- php-cs-fixer enforces this: `global_namespace_import` with `import_classes` and `import_functions` set to `true`, `native_function_invocation` off, and `ordered_imports` in the order class, function, constant. `tests/Unit/CodingStyleTest.php` checks every PHP file of the plugin, and Rector runs with `importDocBlockNames` off.
- In tests, `self::` is written instead of `static::`, because the test classes are `final`. `php_unit_test_case_static_method_calls` with `call_type` set to `self` ensures it. Static kernel helpers in integration tests use `self::` as well.
- Classes that can be `readonly` are declared `readonly class`. IDE hints are followed.

> Earlier variant: functions were excluded from the import rule and kept their leading backslash where php-cs-fixer's `native_function_invocation` demanded it. Another older variant wrote global classes qualified (`\Throwable`, `\ReflectionClass`) with `global_namespace_import` off, so that the fixer did not rewrite them.

### Consequences

The file header is complete. What a file uses in classes and functions is in its imports, without exception, and a missing import is noticed immediately. The header grows by a few lines, and the source text is shorter and reads faster. The static analysis runs without errors and PhpStorm reports nothing. New classes follow the same pattern.

## every-phpstorm-inspection-is-resolved: Every PhpStorm inspection is resolved

**Area:** core **Status:** accepted

### Context

The user decided bindingly: "this should please always and everywhere be thought of". This covers all PhpStorm inspection hints from level `WEAK_WARNING` upward, in production code and in tests, missing `@throws` included. PHPStan at level max and PhpStorm do not see the same things, so a green gate alone is not enough.

### Decision

- Every PhpStorm hint from `WEAK_WARNING` upward is fixed, in `src` and in `tests`, always and everywhere.
- Checking is done per file with the PhpStorm MCP tool `get_inspections`. A file counts as finished only when the check reports nothing.
- Missing `@throws` are added, or the code is changed so that no exception can arise.
- Types must agree for PhpStorm and for PHPStan at level max. A log context is `array<array-key, mixed>`, and the real `MonologExtension` is used instead of a custom stub type.
- Functions are imported with `use function`, tests use `self::`, and tests do not touch `@internal` classes. The details are in the decisions `classes-and-functions-are-imported` and `no-internal-shopware-code` (no internal Shopware code, not even in tests).
- The allowed exceptions are exactly these, and only as a tool directive directly above the statement:
  - `/** @noinspection PhpUnhandledExceptionInspection */` in top-level scripts where no `@throws` can be written: `tests/TestBootstrap.php` and `rector.php`.
  - `/** @noinspection DuplicatedCode */` in `rector.php`, because this file deliberately is the shared default configuration of the plugins.
- Every further exception needs a new ADR that names it.

### Consequences

PhpStorm reports nothing in the plugin. The gate stays green, shown in one plugin by 87 unit tests, 9 integration tests and 100 percent coverage (classes 9/9, methods 40/40, lines 198/198). New code costs slightly more effort because the IDE check is part of finishing. In return, a gap between PHPStan and the IDE is not found only by the next person who opens the file.

## php-conventions: PHP and Shopware code conventions

**Area:** core **Status:** accepted

### Context

Two spellings of the same thing side by side make every review a taste discussion. A plugin that mirrors the core's conventions can be read by anyone who reads the core, while a plugin that invents its own has to be learned separately. So the reference is `vendor/shopware`, the core itself, not other plugins, however popular. Plugins copy each other's mistakes, and the core is what Shopware actually maintains. Where the core does something consistently, the plugin does it the same way.

Several rules were checked against Shopware v6.7.14.0 rather than recalled. The core writes `<?php declare(strict_types=1);` on one line in 294 of 300 sampled files. It marks internal code `@internal` 4162 times and writes `@api` zero times, because public API is what carries no marker at all. It never imports global classes in its own code (`\Throwable` appears 255 times, `use Throwable;` zero times, see `classes-and-functions-are-imported`). It ships nine `services.php` files and zero `services.xml`, and XML service definitions are deprecated as of 6.8.

The conventions are decided before the first class exists, because retrofitting them across a grown codebase is what nobody gets round to.

A file header should list every class the file uses, and every constant should name its type for PHPStan and for the reader. A plugin targeting PHP 8.2 knows neither typed class constants nor the `#[Override]` attribute. An earlier version of the PHP 8.2 convention left out how constants name their type, the exception for functions and the rule about magic strings, and no check enforced the imports.

The `final` question needs a decision rather than a habit, because its two halves point in opposite directions. A service, handler, command, subscriber or value object that is subclassable is a service whose contract is whatever any subclass makes of it, and decoration through the container is the supported extension point, not inheritance. But a definition, entity, collection or entity extension that is `final` is a dead end: extension is the entire mechanism by which another plugin adds a field to the data model, and a middleware plugin exists to be extended by provider plugins.

The directory layout needs a decision for the same reason. Layer-first (`src/Service/Sourcing/`) and domain-first (`src/Sourcing/Service/`) are both defensible in the abstract, and both are unbearable when half the tree uses each. Layer-first matches where the core puts things and gives one answer to the question where a service is, always under `src/Service/`. The one exception are DAL entities. They follow the core's own `Core/Content/<Entity>/` shape, because that is the layout every Shopware developer already navigates and because the DAL's own conventions assume it.

Logging is where a middleware becomes a compliance surface. Requests and responses to a supplier API carry credentials, customer addresses and purchase prices. The default has to be that they are not written down, and the exception has to route through one redactor rather than through the judgment of whoever wrote the call site.

For a plugin that is small at first (one plugin class, one Twig template carrying all the logic, one JavaScript file, no service, no struct, no dependency injection), nothing exists yet that a convention could apply to. When threshold resolution, tier selection and cart processing become PHP, the conventions are already in place.

Money is the one value where the plugins decide who gets a discount, so rounding accidents matter. A threshold of 250.00 compared against a float cart total is a rounding accident waiting to happen.

### Decision

The reference is `vendor/shopware`, the core itself, not other plugins.

| ID | Sev | Rule |
|---|---|---|
| R-201 | MUST | `declare(strict_types=1);` at the top of every file, on the same line as `<?php`. |
| R-202 | MUST | `#[Package('<Plugin>.<Area>')]` on every class. |
| R-203 | MUST | `#[Override]` on every method that overrides a parent or implements an interface, for plugins whose minimum PHP is 8.3 or newer (see the PHP 8.2 rule below). |
| R-204 | MUST | `final` on services, handlers, commands, subscribers, cart processors, value objects. |
| R-205 | MUST | Never `final` on definitions, entities, collections, entity extensions and on structs meant to be extended. They must stay extensible. |
| R-206 | MUST | Constructor property promotion with `readonly` for dependencies. |
| R-207 | MUST | Enums instead of magic strings, for every closed list of values. |
| R-208 | SHOULD | No `service_container` injection, no `debug_backtrace` in production code. |
| R-209 | MUST | No DDD overhead: clear modules, value objects, DTO contracts, state machines, testable services, not aggregates and repositories for everything. |
| R-210 | MUST | Layer-first directory structure: `src/Service/`, `src/Controller/`, `src/Subscriber/`, `src/Struct/`, `src/Interface/`, `src/Enum/`, `src/Fixture/`, `src/Twig/`, `src/Command/`, `src/Migration/`, `src/Resources/`. Domain grouping happens in subdirectories below, for example `src/Service/Sourcing/`. |
| R-211 | MUST | DAL entities live in `src/Core/Content/<Entity>/` with `<Entity>Definition`, `<Entity>Entity`, `<Entity>Collection`, aggregates under `Aggregate/`, as in the core. |
| R-212 | MUST | `src/Interface/` depends only on `Struct` and `Enum`. phpat enforces the layer boundaries in `tests/Architecture/LayerTest.php`. |
| R-213 | MUST | Public API carries no marker, internal code carries `@internal`. Never `@api`. The core uses `@internal` 4162 times and `@api` zero times. The provider interfaces are public by absence of a marker. |
| R-214 | MUST | Service definitions live in `src/Resources/config/services.php`. Shopware's `Bundle::registerContainerFile()` loads `Resources/config/services.*` automatically, so never override `build()` to load it, that loads it twice. |
| R-215 | MUST | PHP format only, never `services.xml`. Shopware 6.7 ships nine `services.php` and zero XML, and XML is deprecated as of 6.8. Split by type under `Resources/config/services/` and import the files from `services.php`. |
| R-216 | MUST | Monolog channels are configured in `Resources/config/packages/monolog.yaml`. That directory is NOT loaded automatically, so the plugin class overrides `build()` for it, which is the one legitimate reason to do so. |
| R-217 | MUST | Every log channel writes to its own directory under `%kernel.logs_dir%/<plugin_logs>/` and rotates. Retention follows purpose: audit 365 files, order 90, sourcing and shipment 30, the rest 14, api-payload 48 hourly files. |
| R-218 | MUST | Provider request and response payloads are logged only when explicitly enabled, and always through `PayloadRedactor`. Credentials never reach a log. |

**On R-201.** "On the same line" means the core's own shape: `<?php declare(strict_types=1);` as one line, not a bare `<?php` followed by a separate `declare`. This is what 294 of 300 sampled core files do, and php-cs-fixer's `declare_strict_types` rule produces it. It stands in the first line with nothing in between.

**On R-202 and R-213.** The `#[Package]` attribute is the core's mechanism and is required on every class. The DocBlock tag set that accompanies it is decided in `complete-docblock-tags`. R-213 is a separate axis, visibility. Absence of a marker is the public declaration, which is why the provider interfaces of `extension-through-tagged-registries` carry none, since they are the plugin's contract with provider plugins. Everything else gets `@internal`. `@api` is never written, because the core never writes it and a marker no tool reads is a marker that will drift.

**On R-204 and R-205.** The split is not stylistic. Services are extended by decoration through the container, and `final` makes that the only route and keeps the contract honest. Definitions, entities, collections and entity extensions are extended by inheritance because the DAL requires it. `final` there would break the mechanism this middleware depends on to let provider plugins and shop projects add fields.

**On R-208.** `service_container` injection turns a class's dependencies into whatever it happens to pull at runtime, and `debug_backtrace` makes behavior depend on the call site. Both are SHOULD rather than MUST because a test double or a debugging session can justify either, but neither belongs in production code.

**On R-209.** The middleware has real domain complexity (sourcing, landed cost, state machines) and no need for the full DDD apparatus around it. Value objects, DTO contracts and testable services, yes. An aggregate root and a repository interface for every noun, no. Persistence choices are decided in a separate persistence layer decision.

**On R-212.** `src/Interface/` is the surface a provider plugin compiles against. If it could reach into `Service` or `Core`, every provider plugin would transitively depend on the middleware's internals, and the thin-provider promise of `extension-through-tagged-registries` would be gone. phpat enforces the boundary in `tests/Architecture/LayerTest.php`, so the rule fails the gate rather than a review.

**On R-214 and R-216.** These two look contradictory and are not. `Bundle::registerContainerFile()` already loads `Resources/config/services.*`, so overriding `build()` for services loads them twice. `Resources/config/packages/` is not loaded automatically, so the Monolog configuration does require a `build()` override, and that is the single legitimate reason the plugin overrides it.

**On R-218.** Payload logging is off unless explicitly enabled, and even then every payload passes through `PayloadRedactor`. There is no direct path from a provider response to a log line. Credentials never appear in a log under any configuration.

**Language, types and file shape.**

- `<?php declare(strict_types=1);` stands in the first line, nothing in between.
- Every class is imported, also those from the global namespace, see `classes-and-functions-are-imported`.
- Every class constant names its type in a DocBlock directly above it: `@var string`, `@var int`, `@var list<string>`, `@var array<string, string>`. This replaces the typed constants that PHP 8.2 does not have. The tag stays even when the type seems obvious.
- Comparisons are written with the subject first: `if ($count > 0)`, never Yoda.
- Subscribers live in `src/Subscriber/`. Constraints are named `<Name>Constraint` in `src/Constraint/` with `<Name>Validator` in `src/Validator/`.
- Twig never reads a boolean configuration with `??`. It uses `config('<Plugin>.config.y') is not same as(false)`.
- Enforcement: php-cs-fixer (`global_namespace_import` with `import_classes`, sorted imports, `yoda_style` off), Rector with `importDocBlockNames` off, PHPStan at level max, and `tests/Unit/CodingStyleTest.php`, which fails on a qualified global class, on a class constant without a `@var` tag and on a typed class constant in `src/` and `tests/`.

**PHP 8.2 minimum and banned features (for plugins supporting Shopware 6.6).**

- The plugin supports Shopware 6.6, whose supported PHP range begins at 8.2. A plugin that needs a newer PHP cannot be installed in the shops it is meant for. The local PHP can be newer than the target, so code that exists only in a later version runs locally and breaks in a shop.
- `composer.json` requires `php >=8.2` and sets the platform to `8.2.0`. PHPStan runs with `phpVersion: 80200`, Rector with the set `php82`.
- Development tools that require a newer PHP are pinned to the newest version that supports 8.2 (for example Infection).
- No `#[Override]`, no typed class constants, no `json_validate`, nothing that needs a PHP newer than 8.2. Banned because they need PHP 8.3 or newer: `json_validate`, `mb_str_pad`, typed class constants, `#[Override]`, dynamic class constant fetch (`Foo::{$name}`), `array_find`, `array_find_key`, `array_any`, `array_all`, `mb_trim`, `mb_ltrim`, `mb_rtrim`, `mb_ucfirst`, `mb_lcfirst`, the `#[Deprecated]` attribute, property hooks, asymmetric visibility, `new` without parentheses in a chain, `Randomizer::getBytesFromString`, `ini_parse_quantity`.
- `CodingStyleTest` fails on these in `src/` and `tests/`. Constants name their type in a `@var` tag instead.
- Source and tests are checked with `php -l` under PHP 8.2, either in a `php:8.2-cli` container or in the development container when it runs PHP 8.2, which counts as the same check.
- Raising the minimum needs a new ADR.

**Structure and dependency injection (small storefront plugins).**

- `src/Service/` for the calculating classes, `src/Struct/` for the value objects handed to Twig, `src/Subscriber/` for the page listener, `src/Core/Checkout/Cart/` for the cart processor, mirroring where Shopware puts its own.
- Dependency injection with explicit arguments, no autowiring by convention. A plugin that is read by someone else benefits from the wiring being visible.

> Earlier variant: one older decision wired the services through `services.xml` with explicit arguments. This is replaced by PHP service files (R-214, R-215 and `services-registered-explicitly-in-php`).

**Money is integer minor units.** Every threshold, every cart total, every discount amount. Floats appear only where Shopware's own cart API hands them over, and are converted at that boundary. See `money-handling`.

**The storefront template renders, it does not compute.** Every `{% set %}` that performs arithmetic is a defect by this convention. The subscriber puts a struct on the page and the template reads its properties.

**Twig extension points.** Templates extend with `sw_extends` and override named blocks only, never replace a whole file. A shop with another plugin on the same block must keep working.

> Earlier variant: R-203 required `#[Override]` on every plugin without exception. A plugin supporting Shopware 6.6 and PHP 8.2 bans it by name, so the rule now depends on the PHP target.

### Consequences

A developer who knows the Shopware core can navigate the plugin without a tour, because almost every convention is the core's convention with the reasoning attached. Reviews cite R-numbers instead of relitigating taste, and the extension points are predictable: services are decorated, entities are inherited, and which one applies is determined by R-204 and R-205 rather than by inspection.

A large part is enforced by tooling rather than attention. php-cs-fixer produces R-201. PHPStan with the strict rules catches a missing `#[Override]` (R-203) and much of what R-206 and R-207 ask for. phpat enforces R-212 and the rest of the layer boundaries in `tests/Architecture/LayerTest.php`, so a dependency violation is a red gate, not a comment. Rector's type-perfect rules push in the same direction. The versions of all of these are pinned by a rule in the git workflow decision (R-106).

The rest needs review attention. R-202's coverage of every class, R-204 and R-205's split, R-209's judgment about how much structure is enough, R-210's placement of a new directory and R-213's marker discipline are all things a reviewer checks. R-213 in particular has no failing tool behind it: writing `@api` produces no error, it just quietly creates a public contract nobody agreed to.

The costs are concrete. Layer-first (R-210) means a single feature's files are spread across several top-level directories, the trade accepted in exchange for one unambiguous answer to where a service lives. R-205 means definitions and entities stay open to subclassing that the project cannot audit, which is the price of being extensible at all. Splitting service definitions under `Resources/config/services/` (R-215) means more files than a single `services.xml`, and the import list in `services.php` has to be maintained. The per-channel log directories and retention windows of R-217 need the filesystem to actually hold them. 365 audit files is a real number, and it has to be provisioned, not assumed.

File headers grow by some lines and answer completely which classes a file uses. Every constant carries a three-line DocBlock, because php-cs-fixer writes DocBlocks across several lines. Two classes with the same name need an alias. If the plugin moves to PHP 8.3, the tags are turned into native constant types in one pass. Every Shopware 6.6 shop can run the plugin, and newer language features wait until the support range shifts.

Moving the arithmetic out of Twig is a visible rewrite of a file that is live in customer shops. The rendered output must stay byte-identical for a shop with no tiers configured, and the Playwright suite proves it. Explicit service wiring is more lines than autowiring, and it is also the file a maintainer reads first to understand what depends on what. Integer minor units mean conversion at every boundary with Shopware's float cart API, and each conversion is a place to get it wrong. The alternative of floats throughout is worse, because it gets it wrong silently.

## technical-folder-structure: Classes live where their kind belongs, names are derived, and the structure is technical, not DDD

**Area:** core **Status:** accepted

### Context

A predictable folder per class kind makes every class findable through its role, and architecture rules can be written against folders. Invented entity names that appear in no table make a class hard to find from its table, and loose translation classes in a shared folder hide which entity they belong to.

An early layout created domain folders (for example `Consent/`, `Translation/`, `Blocking/`, `ConnectionTest/`), each with its own `Dto/`, `Subscriber/`, `Message/` and `ScheduledTask/`. That is a DDD cut. The user wants no DDD and no domain folders and requires the convention of the other plugins of the same developer, which is documented in several plugins and secured by a PHPat structure check.

A layout that a second developer can follow without being told needs tests that keep it that way, without naming classes explicitly and without having to change the tests every time. A convention nobody can check decays: in one plugin 45 wired services had accumulated under `Core/Framework/`, which is where a class goes when nobody decided where it goes.

The plugin's own events are extension points for third parties. The folder convention had no place for own, dispatchable events. An event is neither a DTO (`Struct/`) nor business logic (`Service/`).

### Decision

Where a class lives is decided by what it is, not by the feature it belongs to or its business domain.

| Folder | Content |
|---|---|
| `Core/Content/<Entity>/` | only `<Entity>Definition`, `<Entity>Entity`, `<Entity>Collection`, `<Entity>Events` (DAL definition, entity, collection, translation) |
| `Core/Content/<Entity>/Aggregate/<Entity><Part>/` | one folder per aggregate (translation, mapping), same set of files |
| `Core/Content/Cms/` | CMS element resolvers |
| `Core/Extension/<CoreEntity>/` | one folder per extended core entity, entity extensions |
| `Core/Framework/<Topic>/` | exceptions and framework-level classes (not services), value objects, including `Core/Framework/Log/Package.php` |
| `Framework/Log/` | the plugin's own `Package` attribute (in plugins without `Core/Framework`) |
| `Enum/` | enums, flat |
| `Struct/<Topic>/` | DTOs, value objects, results |
| `Constraint/` | Symfony constraints, flat, suffix `Constraint` |
| `Validator/` | their validators, flat, `<Name>Validator`, returned by `validatedBy()` |
| `Interface/<Topic>/` | interfaces |
| `Provider/<Topic>/` | concrete implementations of an interface (providers, patterns, testers) |
| `Service/<Domain>/` | business logic, with domains such as Api, Registry, Mapping, Sync, Engine, Log, Legacy, Installer, Document, Payment, Config |
| `Controller/Administration/`, `Controller/Storefront/` | controllers, the folder matches the route scope |
| `Subscriber/` | every event subscriber and event listener, flat |
| `Command/` | console commands, flat |
| `Message/`, `MessageHandler/` | queue messages and handlers, flat |
| `Task/` | scheduled task and its handler together |
| `Event/` | own dispatchable events for third parties, flat |
| `Twig/` | Twig extensions, token parsers, nodes, if any are used |
| `Migration/` | migrations |
| `Resources/config/` | `config.xml`, `services.php`, `services/`, `routes.php`, `packages/` |

- Helper classes of a single provider live under `Service/<Topic>/<Provider>/` (for example `Service/Translation/<Provider>/`). The lifecycle helper for the default groups lives under `Service/Installer/`.
- There are no folders for entities, migrations, controllers or storefront where the plugin does not need them. A new role gets a technical folder following the same convention.
- Where Shopware has a convention, it wins. A Store API route stays under `Content/.../SalesChannel/`, a cart processor under `Checkout/Cart/`, a definition under `Core/Content/`. A developer opening the plugin looks where the core taught them to look, and a tidier layout nobody expects is worse than an untidy one everybody knows.
- Names are derived. The base name of the class is the entity name without the plugin prefix in PascalCase, and the folder carries the same name. The entity name of an aggregate is the name of its parent plus a suffix, and its folder is the parent name plus the same suffix.
- `<Entity>Events` is an abstract class holding the event names as class constants with `@var` tags, so that no subscriber writes an event name as a string.
- Own events live flat under `src/Event/`, just as subscribers live under `src/Subscriber/`: the folder says what the class is. Every event implements `ShopwareSalesChannelEvent`. The folder table in the ADR and in `CLAUDE.md` includes `Event/`.
- Write validation is split the Symfony way. A rule is a constraint in `Constraint/` and its validator is in `Validator/`. The write validation subscriber only collects the payload and passes it on. Value lists are checked with the `Choice` constraint over the enum cases.
- The folder of a class and its `#[Package]` area agree.
- The rules live in two places, for a reason. `tests/Architecture/` holds PHPat rules (16 of them in one plugin) that select by what a class is (the interface it implements, the base class it extends) and assert the namespace it must be named in. PHPat reads the dependency graph and is good at exactly that. `tests/Structure/` holds the PHPUnit rules PHPat cannot express: a queue job carrying both its halves, a controller's `_routeScope` matching its folder, every class that does something being named by some test.
- Not one rule names a class or a file. That is what makes them survive: a class written tomorrow is governed without anybody editing a test.
- A PHPat rule checks the folder structure. If no row fits a class, this ADR is superseded and not bent.

> Earlier variant: queue work lived in `Queue/<Job>/` with message and handler together, registries in `Registry/`, scheduled tasks in a flat `ScheduledTask/` folder. Later decisions moved registries to `Service/Registry/` and use `Message/` and `MessageHandler/`, while the newest keeps scheduled task and handler together in `Task/`.

### Consequences

Feature logic is spread across technical folders, and meaningful class names compensate. New code has an obvious place, and architecture tests can forbid dependencies between folders. Whoever knows one of the other plugins finds every class at the same place, and for a small plugin the split by roles is no problem. Existing classes are moved once.

- Moving a class out of a namespace breaks every unqualified reference to a class that stayed. They were neighbors, so neither had an import. 26 files needed one added, and the failure mode was a fatal error at load time rather than a red test.
- Two routing imports in `routes.xml` still pointed at old paths, which no unit test could see. The integration suite found it as four controller tests failing to resolve a URL.
- The first version of the rule "every class has a test" demanded a test file of the same name and flagged 34 classes. Most are proved in shared specs (every enum of one subject in one file), which is a better test than five files asserting one line each. The rule asks whether a test names the class at all, which found the three real gaps and none of the false ones.
- The same reasoning governs structured data: a rule that reads the templates off disk covers an element written tomorrow.
- Third parties find all extension events in one place, and the PHPat structure check includes `Event/`.

## services-registered-explicitly-in-php: Services, routes and bundle configuration are registered explicitly in PHP

**Area:** core **Status:** accepted

### Context

Services can be registered through XML, YAML or PHP, with autowiring or explicitly. Autowiring and autoconfiguration hide which class is a service, which tags it carries and what it receives, and turn a changed constructor into an invisible runtime error. That is dangerous for services with several loggers or path parameters. The plugin extends itself through tagged registries, so tags must be visible. PHP service files can be checked by PHPStan and refactored by the IDE.

### Decision

- Services are registered in `src/Resources/config/services/<area>.php`, one file per area. `services.php` only imports `services/*.php` (in one small plugin four files: `config.php`, `log.php`, `logging.php`, `task.php`).
- Every service is defined explicitly with its arguments and tags written out. No autowiring, no autoconfiguration, no resource scanning.
- There is no `services.xml`.
- Routes live in `src/Resources/config/routes.php`, which imports the controllers from `src/Controller` by attribute.
- Bundle configuration such as the Monolog channel lives in `src/Resources/config/packages/*.yaml` and is loaded by `build()` of the plugin class.
- The plugin configuration stays `config.xml`, the format Shopware requires.
- Registries receive their members through a tag iterator. A new member is a new class plus a tagged definition. Public services are programmed against interfaces.
- An integration test for the container start catches a wrong argument or a missing definition (test phase). `src/Resources/config` is the only coverage exclusion and the only folder excluded from mutation tests, because the directory only runs at boot.

### Consequences

The container is readable from the service files alone, a misspelled argument fails in a test, and every area owns its file, which keeps parallel work free of conflicts. The wiring is readable in one place and checkable by the IDE. A new service needs one more line. Missing arguments show up when the container is built, not only at runtime.

## layers-enforced-by-architecture-rules: Layers are enforced by architecture rules, and transport, format and meaning are separate layers

**Area:** core **Status:** accepted

### Context

Layer rules that exist only in documents erode under time pressure. PHPStan already runs in every gate, and phpat turns dependency rules into PHPStan errors.

A legacy connector mixed HTTP calls, array access on responses and write logic for Shopware in the same classes. A changed response field or a new endpoint version touched all layers at once.

### Decision

`tests/Architecture/LayerTest.php` is registered in `phpstan.neon` with the tag `phpat.test` and contains these rules:

- The Doctrine `Connection` is used only in `Migration`, `Service\Legacy`, `Service\Installer` and the plugin class (uninstall).
- Controllers never use the `Connection`.
- `Struct`, `Enum` and `Event` depend on no `Service` namespace, except the interfaces in `Service\Registry\Contract`.
- `Service\Registry` depends on no implementation namespace (API client, engine, installer, legacy import, log, mapping, sync, controller, commands).
- Nothing depends on `Service\Legacy`, except the legacy import command and the service wiring of the legacy area.

The layers are:

- Transport: the API client in `src/Service/Api/` knows HTTP, authentication, rate limits and pagination. It delivers raw entries.
- Format: typed readers in `src/Struct/<ExternalSystem>/` wrap a raw entry and know where each field lies.
- Meaning: mappers in `src/Service/Mapping/` turn reader values into Shopware payloads. They never call the client and never read raw arrays.
- The sync page type carries raw entries and pagination data and does not refer to the client, so that sync types, the engine and tests do not depend on HTTP classes.
- Writing goes through the DAL in the sync type or in a writer service, and logging goes through log entry values collected in a page result.

### Consequences

- A violation makes `composer phpstan` fail with the name of the rule.
- The legacy import stays a removable island. The administration triggers it through a message or a contract interface, not by importing legacy classes.
- A changed field path is a change in one reader method. A new endpoint is a change in the client and in the sync type, and mappers stay untouched.
- Mappers can be tested with recorded responses alone.

## extension-through-tagged-registries: Extension goes through tagged registries and narrow interfaces

**Area:** core **Status:** accepted

### Context

Shopware ships new fields, the external system changes its data, and every shop wants a slightly different mapping. A connector that branches on types in central classes has to be edited on every change, and every edit endangers the other sync types. Merchants also wish for new kinds of fields and new ways of pricing them. Each such wish used to be an opportunity to grow a `switch` in several places: in the validator, in the payload builder, in the price calculation, in the storefront template.

The central promise of a middleware plugin is that a provider plugin stays thin: authentication, API communication, mapping, capability declaration. No Shopware business logic, no repository writes, no sourcing engine of its own. The provider contract is split into nine narrow interfaces rather than one large one, and a capability system exists because no supplier supports everything. A single fat interface would force every provider to implement methods it cannot serve, filling plugins with `throw new UnsupportedException()` stubs, and the capability flags would then duplicate in data what the type system could have expressed by absence.

### Decision

- Every extension point is a registry in `src/Service/Registry/` that receives its members through `tagged_iterator` in `src/Resources/config/services/registry.php`. The tag name is the public constant `TAG` of the registry. Example registrations:

```php
$services->set(ComputedOptionType::class)->tag('<plugin>.option_type');
$services->set(PerUnitPriceCalculator::class)->tag('<plugin>.price_calculator');
```

- Option types and price calculators are found through Symfony tags and never enumerated by hand. The registries receive every tagged service. A new option type implements `OptionTypeInterface`, a new price kind implements `PriceCalculatorInterface`, and neither touches an existing file.
- Registries: sync types, product, category, manufacturer, customer and property mappers, order export mappers, order status handlers, payment reference providers, legacy sources and mapping types.
- A member implements a contract from `src/Service/Registry/Contract/` and is registered with a tagged definition in the service file of its area. The order follows the tag attribute `priority`, higher runs first.
- Registries never branch on a member type. They index members by key, reject duplicate keys, filter by `supports()` and by the disabled mapper keys of the context, and merge what members declare (relations of the external system, Shopware associations).
- Mapper keys are global and follow `<area>.<aspect>`, for example `product.custom_label`, so that a single disable list in the configuration can switch off any mapper.
- Names of sync types are strings returned by the sync type class. A new sync type needs no enum change.
- Every public service is programmed against an interface, so that a project can decorate it instead of patching it. Every storefront partial is divided into Twig blocks, and the storefront plugin publishes JavaScript events on its element.
- Services are registered explicitly in `src/Resources/config/services/*.php`: no autowiring, the service ID is the class name, the arguments are named.
- Provider plugins register through a Symfony DI tag, and a compiler pass collects them into the registry. A provider plugin never calls middleware classes to register itself.
- The provider contract is split into narrow interfaces:

```text
ProductProviderInterface
CatalogProviderInterface
PriceProviderInterface
AvailabilityProviderInterface
ShippingProviderInterface
OrderProviderInterface
CancellationProviderInterface
ShipmentProviderInterface
ReturnProviderInterface
```

- A provider implements only what it supports. `ProviderCapabilities` remains, carrying the quantitative facts a type cannot express: `maxBatchSize`, `maxRequestsPerSecond`, `supportsIdempotencyKey`, `supportsStockReservation` and so on.
- The middleware checks capability before use and falls back: webhook where supported, polling otherwise, live shipping quotes where supported, configured rules otherwise.

### Consequences

- New behavior is a new class plus a tagged service definition. Project code can add, replace or decorate members without touching the plugin.
- The administration lists sync types, mappers and mapping types from the registries, so new members appear without a frontend change.
- A duplicate key fails loudly on the first read of the registry with an error code ending in `__DUPLICATE_REGISTRY_KEY`.
- A type that needs data the registries do not pass (the values of other options, the base price) receives it through the arguments of the calculator, so the interface passes on the whole value set and the base price.
- The storefront rule JSON must also describe a new type, and the JavaScript must understand it. The shared fixtures make a forgotten half visible.
- Provider plugins stay minimal and declare their surface through types. The registry needs no knowledge of concrete providers, and new capabilities can be added as new interfaces without touching existing plugins.
- Nine interfaces plus a capability object is more surface to document. The definition of done for a provider becomes the checklist that keeps it honest.
- Interface changes are breaking changes for every provider plugin. They require the same deprecation discipline as public API.

## events-let-project-code-change-data: Events let project code change data

**Area:** core **Status:** accepted

### Context

Some changes are too small or too shop-specific for a new mapper, for example discarding an entry before mapping or adding a field to an order. Project code needs an entry point that does not presuppose knowledge of registry internals.

### Decision

- Events live in `src/Event/`, extend the Symfony Contracts `Event` and implement the core interfaces `ShopwareEvent` and `GenericEvent`. Each has a constant `NAME` and is dispatched under that name.
- The data-fetched event (`<vendor>.data.fetched`): after a page was fetched and before it is processed, the entries can be replaced.
- The payload-mapped event (`<vendor>.payload.mapped`): after all mappers have run and before the payload is written, the payload can be changed.
- The order-payload-built event (`<vendor>.order_payload.built`): after all order export mappers have run and before the order is sent.
- The sync-page-processed event (`<vendor>.sync_page.processed`): after a page was processed, read-only.
- Events carry structs and payload builders, never services.

### Consequences

- Shops adjust data with a subscriber without forking the plugin.
- Everything that should be reusable or configurable is still built as a registry member.

## typed-readers-hold-each-field-path-once: Typed readers hold each field path exactly once

**Area:** core **Status:** accepted

### Context

Responses of the external system are nested arrays in which IDs are sometimes numbers and sometimes strings, dates appear in several spellings and translated texts sit in lists. Reading them inline spreads paths and casts across the code and hides type errors until production.

### Decision

- Every structure of the external system has a `final readonly` reader that extends an abstract reader base class.
- The base class offers only protected typed accessors: dot-path lookup, string, nullable string, int, float, bool with default, list of objects, list of ints, nested reader, list of readers, dates, and translated text by language.
- Concrete readers provide one public method per field. The path string of a field exists in exactly one method.
- Dates are parsed in and returned as `Europe/Berlin`. Unix timestamps are accepted. Empty dates of the external system (negative or zero years) become null.
- A value of the wrong type raises an error with a code ending in `__READER_TYPE_MISMATCH`, and a missing required value raises one ending in `__READER_PATH_MISSING`. Both carry the reader class and the path, never the value.
- Readers start small. The agent that owns an area adds the fields it needs to the reader of that area.

### Consequences

- A wrong assumption about a field shows up as a typed exception with the exact path.
- `toArray()` returns the raw entry for the raw-data snapshot of the sync log.

## money-handling: Money is integer minor units, and net prices are stored unrounded like the core

**Area:** data **Status:** accepted

### Context

Floating point must be avoided for money, and supplier currency conversion must never happen implicitly. Purchase prices may arrive net, gross or with unknown tax treatment, and no implicit assumption is allowed.

The middleware's core arithmetic is a sum of many small amounts: purchase price times quantity, plus supplier shipping, plus surcharges, across several suppliers, compared against alternative combinations whose totals may differ by cents. This is the landed cost, and the optimizer compares those totals to pick a winner. Floating point error in that comparison does not merely round a display value. It can select the wrong supplier, and it does so non-deterministically, which collides directly with the sourcing determinism decision.

Shopware's own price fields are `float`. That is a constraint at the boundary, not a reason to carry floats through the domain.

The external system delivers gross sales prices, and Shopware stores gross and net per currency. An audit finding asked whether the net price should be rounded. A product created in the admin (gross 49.99) has the net price 42.00840336134454 in Shopware, so the core stores net prices unrounded as well. A rounded net price would no longer match the gross price.

### Decision

A readonly value object:

```php
final readonly class Money
{
    public function __construct(
        public int $amountMinor,
        public string $currency,
    ) {
    }
}
```

Rules:

- All domain arithmetic goes through `Money`. No float arithmetic on monetary values.
- Operations between different currencies throw. Conversion is always explicit.
- Conversion records the exchange rate used and is snapshotted with the order (see the purchase price storage decision).
- Tax treatment travels alongside the amount as an explicit enum (`NET`, `GROSS`, `UNKNOWN`) and is never assumed.
- Conversion to and from `float` happens only at the DAL and API boundary, in one place per direction.
- No external money library is introduced. The required surface is small, and the dependency budget of the plugin is better spent elsewhere.
- The connector computes the net price as gross divided by (1 + tax rate / 100) in `src/Service/Mapping/Product/PriceCalculator.php`.
- The result is not rounded. There is no code change.

### Consequences

- Exact arithmetic, deterministic optimizer comparisons, currency mistakes become type errors instead of silent wrong numbers, and tax treatment cannot be forgotten.
- Explicit conversion at every boundary to Shopware core. Developers must resist reaching for plain floats. PHPStan and code review enforce this.
- Minor-unit assumptions differ per currency (JPY has none, some currencies have three). The value object stores the exponent alongside the currency where it matters.
- Net and gross agree for every tax rate. As in the core, rounding is done by the price calculation when it computes with quantities and taxes.
- The long decimal places in the database are intended and not a defect.
