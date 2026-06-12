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

| Skill | Beschreibung |
|---|---|
| `sw-upgrade-overview` | Überblick über Shopware-6-Versions-Upgrades (Plugin/Code): Major-Strategie, UPGRADE-*.md/CHANGELOG nutzen, Feature-Flags, Rector-Codemods, Reihenfolge (6.6→6.7→6.8) |
| `shopware-6.7-migration` | Use when migrating Shopware plugins from 6.6 to 6.7, upgrading admin components from sw-* to mt-* (Meteor), migrating from Webpack to Vite, converting Vuex to Pinia, adopting Vue 3 Composition API, or updating PHP code with constructor prop |
| `sw-deprecation-handling` | Deprecations in Shopware 6 erkennen und auflösen: Deprecation-Notices (@deprecated tag:v6.x), Feature-Flags für Major-Verhalten, Rector-Codemods, Test-Deprecation-Handling |
| `sw-meteor-component-map` | Migration der Shopware-Admin-Komponenten von sw-* zu Meteor mt-* (6.6→6.7): Komponenten-Mapping, geänderte Props/Events/ Slots, v-model:value, Ersetzungsstrategie |
| `sw-php-migration-patterns` | PHP-Migrationsmuster für Shopware-Plugins (6.6→6.7): geänderte Signaturen/Interfaces (z.B |
| `sw-release-notes` | Shopware-6-Release-Notes und Versions-Highlights (6.5–6.8) |
| `sw-vite-migration` | Migration des Admin-Builds von Webpack zu Vite (Shopware 6.7): Build-Konfiguration, Entry, Anpassungen, Watcher |
| `sw-vuex-to-pinia` | Migration des Admin-State von Vuex zu Pinia (Shopware 6.6→6.7): Shopware.State → Shopware.Store, Mutations→Actions, mapState/mapGetters ersetzen |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-migrator` | Spezialist für Shopware-6 Versions-Upgrades von Plugins (Code-Migration): 6.6→6.7→6.8, Admin sw-*→Meteor mt-*, Webpack→Vite, Vuex→Pinia, PHP-Signatur-/API-Änderungen, Deprecations, Rector |

## Commands (1)

| Command | Beschreibung |
|---|---|
| `/sw-migrate-component` | Migriert eine Admin-Komponente/ein Template von Legacy sw-* auf Meteor mt-* (Shopware 6.7) inkl |
