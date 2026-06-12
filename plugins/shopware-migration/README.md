# shopware-migration

> Versions-Upgrades bestehender Plugins (6.6 → 6.7 → 6.8).

`shopware-migration` begleitet das **Upgrade bestehender Plugins** zwischen Shopware-Major-Versionen aus
**Entwickler-Sicht** (das Aktualisieren eines Shops als Betreiber liegt in `shopware-merchant`).

Enthalten: ein **Upgrade-Überblick** (Strategie, `UPGRADE-*.md`/`RELEASE_INFO` nutzen, schrittweise je Minor/Major)
und die konkreten Migrationspfade für **6.6 → 6.7 (→ 6.8)**: Admin-Komponenten **`sw-*` → Meteor `mt-*`** (Mapping
von Props/Events/Slots), **Webpack → Vite**, **Vuex → Pinia**, **PHP-Migrationsmuster** (geänderte Signaturen/
Interfaces wie der neue Payment-Handler, moderne PHP-Features) sowie systematisches **Deprecation-Handling**
(Notices finden, Rector-Codemods, Major-Feature-Flags). Zusätzlich die Admin-spezifischen Upgrade-Themen (Vue-3-
Umstellung, Migration-Build, Native-Vue-Roadmap) und Übersetzungs-/Sprachpaket-Migration.

Spezialist: **`shopware-migrator`** (opus); Scaffolder/Helfer **`/sw-migrate-component`**. **Wann nutzen:** beim
Hochziehen eines Plugins auf eine neue Shopware-Version.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-migration@claude-a-dev-team
```

## Skills (8)

`sw-upgrade-overview`, `shopware-6.7-migration`, `sw-deprecation-handling`, `sw-meteor-component-map`, `sw-php-migration-patterns`, `sw-release-notes`, `sw-vite-migration`, `sw-vuex-to-pinia`

## Agents (1)

- **`shopware-migrator`** — Spezialist für Shopware-6 Versions-Upgrades von Plugins (Code-Migration): 6.6→6.7→6.8, Admin sw-*→Meteor mt-*, Webpack→Vite, Vuex→Pinia, PHP-Signatur-/API-Änderungen, Deprecations, Rector.

## Commands (1)

- **`/sw-migrate-component`** — Migriert eine Admin-Komponente/ein Template von Legacy sw-* auf Meteor mt-* (Shopware 6.7) inkl.
