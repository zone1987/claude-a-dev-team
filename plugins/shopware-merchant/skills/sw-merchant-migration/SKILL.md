---
name: sw-merchant-migration
description: >
  Migration zu Shopware 6 — Betreibersicht: Shopware 5 nach 6 migrieren, Magento nach Shopware 6 migrieren,
  Shopware 6 auf 6 umziehen (Cloud/Server-Wechsel). Migrationsassistent, Profile, Verbindung herstellen,
  Datenübernahme, Livegang. Trigger: "Shopware 5 auf 6 migrieren", "Migration Shopware", "Migrationsprozess
  Shopware", "Daten aus Shopware 5 übernehmen", "Magento zu Shopware migrieren", "Migrationsassistent
  installieren", "Verbindung für Migration einrichten", "was wird bei Migration übernommen", "Migration
  Shopware Voraussetzungen". Shopware 6.7.
---

# Shopware 6 — Migration (Betreiber-Überblick)

Destilliert aus `docs.shopware.com/de/migration-de`. Drei Quellsysteme unterstützt:

## Unterstützte Migrationsquellen

| Quelle | Ziel |
|---|---|
| Shopware 5 | Shopware 6 (self-hosted) |
| Shopware 6 (alt) | Shopware 6 (Cloud oder neuer Server) |
| Magento | Shopware 6 |

> **Wichtig (SW6→SW6):** Quell- und Zielsystem müssen dieselbe Shopware-Version haben.

## Drei Migrationsphasen

1. **Vorbereitungsphase** — Systemcheck, Lizenz, SW6-Installation
2. **Migrationsphase** — Migrationsassistent + Datentransfer
3. **Abschlussphase** — Livegang, DNS, Shopware Account

## Detailwissen je Thema

| Thema | Skill |
|---|---|
| Migrationsprozess (Assistent, Verbindung, Daten) | `sw-merchant-migration-prozess` |
| Livegang (Domain, Hosting, Abschluss) | `sw-merchant-migration-livegang` |

Tiefes Referenzwissen: `references/deep/`

---

*Quelle: https://docs.shopware.com/de/migration-de*
