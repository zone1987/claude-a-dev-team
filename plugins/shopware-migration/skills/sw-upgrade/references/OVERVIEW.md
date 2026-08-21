# Shopware 6 — upgrade overview (code/plugin)

Code/plugin migration between major versions (developer perspective; for the operator update see `shopware-merchant` →
`sw-merchant-update-guides`).

- **Sources**: `UPGRADE-6.x.md` (breaking changes per version), `CHANGELOG.md`, `RELEASE_INFO-*`, deprecation notices in the code.
- **Order**: step by step per minor/major (e.g. 6.6 → 6.7 → 6.8), do not skip; adjust the `conflict` in `composer.json`.
- **Tools**: Rector sets for deprecated APIs (`shopware-quality` → `sw-rector`); PHPStan/ECS after every step.
- **Focus areas 6.6→6.7**: admin `sw-*`→Meteor `mt-*` (`sw-meteor-component-map`), Webpack→Vite (`sw-vite-migration`),
  Vuex→Pinia (`sw-vuex-to-pinia`), PHP features/signatures (`sw-php-migration-patterns`), new payment handler.

Version-specific steps: dedicated skills + the references of the `shopware-6.7-migration` skill.
Resolving deprecations cleanly: `sw-deprecation-handling`.
