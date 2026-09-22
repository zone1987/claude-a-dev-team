# Shopware 6 — extendability principles

## Contents

- [Short version](#short-version)
- [@internal / @final rules](#internal-final-rules)
- [Mandatory decoration pattern rules](#mandatory-decoration-pattern-rules)
- [Shopware 6 — extendability: complete reference](#shopware-6-extendability-complete-reference)

## Short version

- **Events (mediator)** — first choice for extendability; listeners via `EventSubscriberInterface`; pass primary keys only, never entities
- **Decorator (decoration pattern)** — when events are not enough; an abstract class is mandatory; `getDecorated()` plus `DecorationPatternException` in the core
- **Factory** — for new user input types; registry pattern with tagged services
- **Visitor** — for objects that are visited or extended during processing
- **Adapter** — for the functional exchange market (complete technology swap)
- **Hooks** — app script entry points (the equivalent of events for apps)

## @internal / @final rules

- `@final`: the class is public API (consumable) but not extendable; changes to public methods are forbidden
- `@internal`: private API; may change or be removed without deprecation; do not use in third-party plugins
- All DTOs and event subscribers → `final`
- All decoratable services → abstract class (NO `@internal`, NO `@final`)

## Mandatory decoration pattern rules

1. Define an abstract class with `getDecorated(): self`
2. Core implementation: `getDecorated()` throws `DecorationPatternException`
3. The abstract class must NOT be `@internal` or `@final`
4. Implementations must NOT add extra public methods
5. Implementations must NOT act as event subscribers

Boundary to `sw-coding-guidelines`: this skill focuses on the architecture concepts; the coding guidelines cover coding style, migrations and static analysis.

## Shopware 6 — extendability: complete reference

Sources: `guides/development/extensions/architecture/{extendability,final-and-internal,internal,index}.md` plus
`resources/guidelines/code/core/{extendability,final-and-internal,internal,decorator-pattern}.md`

---

### Contents

- [Overview: why extendability?](#overview-why-extendability)
- [Technical requirements](#technical-requirements)
- [Extension patterns](#extension-patterns)
- [Public API and @internal/@final](#public-api-and-internalfinal)
- [Decision tree: which pattern?](#decision-tree-which-pattern)
- [Architecture subsystems](#architecture-subsystems)
- [References](#references)

### Overview: why extendability?

Shopware must be adaptable by third parties and internally without every change breaking core stability. That is why there is a clear extension model with defined patterns and API boundaries.

Extension types: **plugins** (full server access, self-hosted only), **apps** (API-based, cloud-compatible), **project bundles** (project-specific).

---

### Technical requirements

| Category | Description | Example |
|-----------|-------------|---------|
| Functional extensibility | Extend a feature with additional features | Add a suggestion feature to enterprise search |
| Functional modifiability | Override parts of a feature | Tax calculation for the USA via a tax provider |
| Functional differentiation | Make parts paid | Feature behind a version flag |
| Functional exchange market | Replace a feature entirely | Connect an external newsletter system |

---

### Extension patterns

#### 1. Decoration (decorator pattern)

**Use for:** completely replacing or extending services; store API routes; the functional exchange market.

**Mandatory rules:**

1. Define an abstract class (not an interface!) with `getDecorated(): static`.
2. Core class: `getDecorated()` throws `DecorationPatternException(self::class)`.
3. The abstract class must NOT be `@internal` or `@final`.
4. Implementations must NOT add public methods beyond those of the abstract class.
5. Implementations must NOT act as an `EventSubscriberInterface` (Symfony event system limitation).
6. The PHPStan rule `DecorationPatternRule` enforces these rules automatically.

```php
abstract class AbstractRuleLoader
{
    abstract public function getDecorated(): AbstractRuleLoader;
    abstract public function load(Context $context): RuleCollection;

    // New methods: add them as non-abstract with delegation (BC-safe):
    public function create(Context $context): RuleCollection
    {
        return $this->getDecorated()->create($context);
    }
}

class CoreRuleLoader extends AbstractRuleLoader
{
    public function getDecorated(): AbstractRuleLoader
    {
        throw new DecorationPatternException(self::class);
    }
    public function load(Context $context): RuleCollection { /* ... */ }
}

class PluginRuleLoader extends AbstractRuleLoader
{
    public function __construct(private AbstractRuleLoader $inner) {}

    public function getDecorated(): AbstractRuleLoader { return $this->inner; }

    public function load(Context $context): RuleCollection
    {
        $rules = $this->inner->load($context);
        // extension / modification
        return $rules;
    }
}
```

**Internal decoration (without external extendability):** if decoration is only needed internally (for example a cache or log layer), use an abstract class but mark all classes as `@internal` or `@final`.

```php
/**
 * @final
 */
class CachedLoader extends AbstractRuleLoader
{
    public function __construct(
        private readonly AbstractRuleLoader $decorated,
        private readonly CacheInterface $cache
    ) {}

    public function load(Context $context): RuleCollection
    {
        return $this->cache->get(self::CACHE_KEY, fn () => $this->decorated->load($context));
    }
}
```

ADR: [2020-11-25-decoration-pattern](https://github.com/shopware/shopware/blob/trunk/adr/2020-11-25-decoration-pattern.md)

---

#### 2. Factory pattern

**Use for:** interpreting and validating user input; functional extensibility; adding new types.

**Example:** `LineItemFactoryRegistry` — a registry with tagged services; third parties can register their own handlers.

```php
// src/Resources/config/services/cart.php — PHP, not XML
// (`XmlFileLoader` is `@deprecated tag:v6.8.0`), explicitly and without autowiring.
$services->set(CustomLineItemFactory::class)
    // Without autoconfigure this tag is not inferred.
    ->tag('shopware.cart.line_item_factory_handler');
```

→ `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`

---

#### 3. Visitor pattern

**Use for:** processing sets of objects; functional extensibility plus modifiability.

**Example:** the cart `Processor` calls all `LineItemProcessor` implementations; third-party visitors run before or after the core visitor.

---

#### 4. Mediator pattern — events

**Use for:** entry points for listeners; asynchronous processing.

**Best practices:**
- Pass only primary keys in the event, no entities or objects — this enables asynchronous processing.
- Register listeners via `EventSubscriberInterface`.

```php
// Good: pass the ID only
class CheckoutOrderPlacedEvent
{
    public function __construct(private readonly string $orderId) {}
    public function getOrderId(): string { return $this->orderId; }
}

// Bad: pass the whole entity
class CheckoutOrderPlacedEvent
{
    public function __construct(private readonly OrderEntity $order) {}
}
```

##### Hooks (for apps)

Hooks are app script entry points — the equivalent of events for plugins. Since apps have no direct server access, hooks allow more complex business logic without an HTTP round trip to the app server.

Example: `ProductPageLoadedHook` — dispatched in the controller; every registered app script runs.

---

#### 5. Adapter pattern

**Use for:** the functional exchange market; swapping technology (for example changing the captcha type).

**Implementation:** registry plus tagged services; the user selects the adapter through configuration.

---

### Public API and @internal/@final

#### What is public API?

All `public` and `protected` methods, properties and constants count as public API for third parties by default.

The Shopware public API must stay compatible across minor releases for:
- Service usage (calling methods)
- Service decoration (extending)
- DTO usage (reading and passing data)

#### @final annotation

The class is public API (consumable) but **not extendable**.

**Permitted changes to `@final` classes:**
- Add new public methods, properties or constants
- Add new optional parameters to public methods
- Change protected/private methods without restriction
- Widen the types of public method parameters

**Forbidden changes:**
- Remove public methods, properties or constants
- Remove public method parameters
- Narrow the types of public methods, properties or constants

**Why `final`?**
- DI container services: `final`, so no direct inheritance takes place — decoratable services have an abstract class
- DTO classes: `final` plus struct extensions for additional data
- Event subscribers: `final`

Note: because these are doc annotations, inheritance is technically possible — but without guarantees.

#### @internal annotation

The class is **private API** — do not use it in plugins or apps.

- Can be changed or removed without restriction and without deprecation
- Use for internal implementation details, refactoring candidates, and classes that exist only to split up a "master class"
- `@internal` interfaces: when several implementations are needed internally but no external interference is wanted (for example DAL Field/FieldSerializer)

---

### Decision tree: which pattern?

```
Do I need external extendability?
├─ Yes, listener-based (before/after an action) → events / hooks
├─ Yes, service fully replaceable/extendable → decoration pattern (abstract class)
├─ Yes, new types/handlers can be added → factory / registry + tagged services
├─ Yes, visit objects during processing → visitor pattern
├─ Yes, technology fully swappable → adapter pattern
└─ No, internal only → @internal or @final, no abstract class needed
```

---

### Architecture subsystems

Shopware draws a clear line between **Core**, **Storefront** and **Administration**.

Extensions must respect these boundaries:
- Do not introduce non-deterministic behavior
- Do not break background jobs or CLI commands
- No performance regressions
- Ensure upgrade compatibility

---

### References

- `guides/development/extensions/architecture/extendability.md`
- `guides/development/extensions/architecture/final-and-internal.md`
- `guides/development/extensions/architecture/internal.md`
- `guides/development/extensions/architecture/index.md`
- `resources/guidelines/code/core/extendability.md`
- `resources/guidelines/code/core/final-and-internal.md`
- `resources/guidelines/code/core/internal.md`
- `resources/guidelines/code/core/decorator-pattern.md`
- ADR: https://github.com/shopware/shopware/blob/trunk/adr/2020-11-25-decoration-pattern.md
