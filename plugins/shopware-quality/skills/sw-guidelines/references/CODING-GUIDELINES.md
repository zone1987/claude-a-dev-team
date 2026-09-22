# Shopware 6 — coding guidelines

Binding guidelines from the core (`coding-guidelines/`). Key points:

- **Extendability**: extend primarily through **events** (`EventSubscriberInterface`); use decorators only when the
  event timing does not fit. Make your own classes `final` where possible.
- **final & internal**: `@internal`/`final` mark non-API; do NOT rely on it (it can change without a BC break).
- **Decorator pattern**: same interface, delegate to `.inner`, do not duplicate core logic.
- **Domain exceptions**: one exception factory per domain with stable `code`s (`sw-domain-exceptions`).
- **Deprecation**: put changes behind feature flags/major flags; consistent deprecation notices; Rector codemods.
- **DB migrations**: non-destructive `update()` plus a separate `updateDestructive()`; idempotent.
- **Static analysis**: write code so that PHPStan at `level: max` and the phpat architecture rules stay green; strict types.

Lint and analysis run as one command: **`composer gate`**. It covers php-cs-fixer, PHPStan `max`, Rector and
Stylelint; ESLint and Prettier join it where the plugin has JavaScript.
→ `sw-analysis` → `STATIC-ANALYSIS.md`
Architecture decisions: `sw-adr-knowledge`. Static analysis tools: `sw-static-analysis`.

**Complete code guidelines** (all rules from `resources/guidelines/code/core`): `CODING-GUIDELINES-CODE-GUIDELINES-FULL.md`
Extension patterns and @internal/@final in depth: `sw-extendability`. Plugin/bundle structure: `sw-code-structure`.
