# Shopware 6 — Update guides: complete reference (overview)

## Contents

- [Chapter structure of the official documentation](#chapter-structure-of-the-official-documentation)
- [System requirements per version](#system-requirements-per-version)
- [Update process: step by step (overview)](#update-process-step-by-step-overview)
- [Important warnings](#important-warnings)

## Chapter structure of the official documentation

The official update guides at `docs.shopware.com/de/shopware-6-de/update-guides` comprise:

| Page | Content |
|---|---|
| Shopware aktualisieren / updaten (Updating Shopware) | General instructions (all methods) |
| Update Guide 6.4 zu 6.5 (6.4 to 6.5) | Major update instructions |
| Update Guide Shopware 6.6 | New features & requirements for 6.6 |
| Update Guide 6.5 zu 6.6 (6.5 to 6.6) | Major update instructions |
| Update Guide Shopware 6.7 | New features & requirements for 6.7 |

---

## System requirements per version

### Shopware 6.7 (current)
| Component | Requirement |
|---|---|
| PHP | 8.2, 8.3 or 8.4 |
| Node.js | 20 or higher |
| MySQL | 8.0.17+ (not 8.0.20, 8.0.21) |
| MariaDB | 10.11+ (not 10.11.5 & 11.0.3) |
| Redis | 7.0+ (optional) |
| OpenSearch/Elasticsearch | 1.0+ / 7.8+ (optional) |

### Shopware 6.6
| Component | Requirement |
|---|---|
| PHP | 8.2+ |
| Node.js | 20 |
| MariaDB | 10.11+ |
| Redis | 7.0 (optional) |
| MySQL | 8.0+ |

### Shopware 6.5 (for an update from 6.4)
| Component | Requirement |
|---|---|
| PHP | 8.1+ |
| Node.js | 18 |
| Git | required |

### Hardware (recommendations)
| Component | Minimum | Recommendation |
|---|---|---|
| CPU | Dual core | Quad core or higher |
| RAM | 8 GB | 16 GB |
| Disk | 10 GB free | 20 GB free |

---

## Update process: step by step (overview)

### Phase 1: preparation

**1.1 Set up a test environment**
- Set up a separate server or subdomain
- Clone the production database (anonymised)
- Run the update on the test environment first

**1.2 Create a backup (MANDATORY)**
- Shopware does not create an automatic backup
- Database dump via `mysqldump` or the hosting panel
- Back up all files (var/, public/media/, config/)
- Backup storage location: external (another server/cloud)

**1.3 Check extensions**

Three compatibility statuses in the admin:
1. **Bereits kompatibel** (Already compatible) — the installed version runs with the new Shopware version
2. **Mit der neuen Shopware Version kompatibel** (Compatible with the new Shopware version) — the extension can be updated after the shop update
3. **Nicht kompatibel** (Not compatible) — no successor version; the extension must be deactivated/deleted before the update

Check compatibility via:
- Shopware Store (store.shopware.com)
- Admin panel: Einstellungen (Settings) > System > Shopware-Update (Shopware update)
- Shopware Account: the "Lizenzen" (Licences) area

### Phase 2: running the update

→ Choose a method: admin panel, browser installer or Composer+CLI

### Phase 3: follow-up
- Update the extensions (Store or Composer)
- Reactivate the extensions
- Recompile the theme (with CLI: `bin/console theme:compile`)
- Test the storefront
- Clear the cache: `bin/console cache:clear`

---

## Important warnings

> **CRITICAL:** For a major update (6.4→6.5 or 6.5→6.6), ALL extensions MUST be deactivated — including compatible ones. The theme must be set to the default theme.

> **IMPORTANT:** A Composer update is more stable than an admin update (no PHP timeouts on large shops).

> **NOTE:** Incompatible extensions can abort the update or block the shop.

---

*Source: https://docs.shopware.com/de/shopware-6-de/update-guides*
