---
name: sw-feature-flags
description: >
  Feature-Flags in Shopware 6: Features registrieren und abfragen (Feature::isActive), Major-Feature-Flags,
  experimentelle Features, Flag bei Bedarf umschalten. Trigger: "Feature Flag", "Feature::isActive",
  "experimental feature", "major flag", "feature toggle", "FEATURE_NEXT", "feature.flags". Shopware 6.7.
---

# Shopware 6 — Feature-Flags

Flags erlauben es, neuen Code hinter einem Schalter auszuliefern (Major-Vorbereitung, Experimente).

```php
if (Feature::isActive('FEATURE_FF_NEXT_1')) {
    // neuer Pfad
}
```

Registrierung über `config/packages/feature.yaml` bzw. `Feature::registerFeature()`. Code in Tests gezielt aktivieren
mit `Feature::skipTestIfActive`/`Feature::skipTestIfInActive`. Major-Flags steuern BC-brechende Änderungen bis zum
nächsten Major (vgl. ADRs „feature flags for major versions", „toggle feature flag on demand", „experimental features").

Plugin-eigene Flags sparsam einsetzen und nach Stabilisierung entfernen, damit kein toter Pfad bleibt.
