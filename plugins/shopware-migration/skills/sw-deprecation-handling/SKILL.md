---
name: sw-deprecation-handling
description: >
  Deprecations in Shopware 6 erkennen und auflösen: Deprecation-Notices (@deprecated tag:v6.x), Feature-Flags für
  Major-Verhalten, Rector-Codemods, Test-Deprecation-Handling. Trigger: "Deprecation shopware", "@deprecated auflösen",
  "deprecated entfernen", "Feature flag major", "deprecation notice", "rector deprecation". Shopware 6.7.
---

# Shopware 6 — Deprecation-Handling

Shopware kündigt Breaking Changes über `@deprecated tag:v6.x`-Notices und Major-Feature-Flags an (konsistente
Deprecation-Notices, ADR).

- **Finden**: `@deprecated`-Hinweise im Core (gegen genutzte APIs), Deprecation-Log zur Laufzeit, `UPGRADE-*.md`.
- **Auflösen**: empfohlene Nachfolge-API nutzen; wo angeboten, Rector-Regel anwenden (`shopware-quality` → `sw-rector`).
- **Major-Flags**: neues Verhalten testweise via `Feature::isActive('v6.x.0.0')`/Flag aktivieren (`shopware-core` → `sw-feature-flags`).
- **Tests**: Deprecation-Handling in PHPUnit (ADR „deprecation handling during phpunit") — Tests nicht an deprecierten Pfaden festmachen.

Nicht auf `@internal`/deprecierte APIs verlassen. Versionsspezifische Liste: `sw-upgrade-overview` + `UPGRADE-6.x.md`.
