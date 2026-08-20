# Shopware 6 — Upgrade-Überblick (Code/Plugin)

Code-/Plugin-Migration zwischen Major-Versionen (Entwicklersicht; Betreiber-Update siehe `shopware-merchant` →
`sw-merchant-update-guides`).

- **Quellen**: `UPGRADE-6.x.md` (Breaking Changes je Version), `CHANGELOG.md`, `RELEASE_INFO-*`, Deprecation-Notices im Code.
- **Reihenfolge**: schrittweise je Minor/Major (z.B. 6.6 → 6.7 → 6.8), nicht überspringen; `composer.json`-`conflict` anpassen.
- **Werkzeuge**: Rector-Sets für deprecierte APIs (`shopware-quality` → `sw-rector`); PHPStan/ECS nach jedem Schritt.
- **Schwerpunkte 6.6→6.7**: Admin `sw-*`→Meteor `mt-*` (`sw-meteor-component-map`), Webpack→Vite (`sw-vite-migration`),
  Vuex→Pinia (`sw-vuex-to-pinia`), PHP-Features/Signaturen (`sw-php-migration-patterns`), neuer Payment-Handler.

Versionsspezifische Schritte: dedizierte Skills + die References des Skills `shopware-6.7-migration`.
Deprecations sauflösen: `sw-deprecation-handling`.
