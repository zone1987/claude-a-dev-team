# Shopware 6 — Feature Flags

Flags let you ship new code behind a switch (major preparation, experiments).

```php
if (Feature::isActive('FEATURE_FF_NEXT_1')) {
    // new path
}
```

Register them via `config/packages/feature.yaml` or `Feature::registerFeature()`. Activate code selectively in tests
with `Feature::skipTestIfActive`/`Feature::skipTestIfInActive`. Major flags gate BC-breaking changes until the
next major (see the ADRs "feature flags for major versions", "toggle feature flag on demand", "experimental features").

Use plugin-owned flags sparingly and remove them once stabilized, so no dead path remains.
