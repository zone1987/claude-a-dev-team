# Shopware 6 — extendability principles

Complete reference: `EXTENDABILITY-DETAIL.md`

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
