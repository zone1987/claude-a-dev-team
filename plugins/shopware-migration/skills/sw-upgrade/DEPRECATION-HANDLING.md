# Shopware 6 — deprecation handling

Shopware announces breaking changes via `@deprecated tag:v6.x` notices and major feature flags (consistent
deprecation notices, ADR).

- **Finding them**: `@deprecated` hints in the core (against the APIs you use), deprecation log at runtime, `UPGRADE-*.md`.
- **Resolving them**: use the recommended successor API; where offered, apply the Rector rule (`shopware-quality` → `sw-rector`).
- **Major flags**: activate the new behavior for testing via `Feature::isActive('v6.x.0.0')`/flag (`shopware-core` → `sw-feature-flags`).
- **Tests**: deprecation handling in PHPUnit (ADR "deprecation handling during phpunit") — do not pin tests to deprecated paths.

Do not rely on `@internal`/deprecated APIs. Version-specific list: `sw-upgrade-overview` + `UPGRADE-6.x.md`.
