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
