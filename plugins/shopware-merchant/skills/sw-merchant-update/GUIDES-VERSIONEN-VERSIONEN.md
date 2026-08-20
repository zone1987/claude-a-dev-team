# Shopware 6 — Version-specific update notes: complete reference

## Contents

- [Update guide: 6.4 → 6.5](#update-guide-64--65)
- [Update guide: 6.5 → 6.6](#update-guide-65--66)
- [Update guide: Shopware 6.6 — new features](#update-guide-shopware-66--new-features)
- [Update guide: Shopware 6.7 — new features](#update-guide-shopware-67--new-features)
- [Upgrade path: skipping several versions](#upgrade-path-skipping-several-versions)
- [Compatibility matrix for common requirements](#compatibility-matrix-for-common-requirements)

## Update guide: 6.4 → 6.5

**Source:** https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-64-zu-65

### Prerequisites (mandatory)

| Component | Requirement |
|---|---|
| Shopware source version | 6.4.20.2 or newer (NOT from 6.4.0–6.4.20.1!) |
| PHP | 8.1 or higher |
| Node.js | 18 |
| Git | Installed and configured |

> **IMPORTANT:** If an older 6.4 version is still in place, first update to 6.4.20.2, only then to 6.5.

### Extensions: deactivate all of them (mandatory)

For this major update, ALL extensions must be deactivated:

1. **Set the theme to the default** — deactivate the active custom theme, activate the storefront default
2. **Deactivate the theme extension under Erweiterungen** (Extensions)
3. **Deactivate all further extensions**
4. Only then: run the update to 6.5

After a successful update:
- Update the extensions in the Store/Composer to compatible versions
- Reactivate the extensions

### Running the update

Update as described in the general instructions:
→ https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten#update-per-administration

### New features in Shopware 6.5

- Vue 3 support in the admin (extensions must be adapted)
- Node.js 18 as the minimum requirement
- PHP 8.1 as the minimum requirement
- Reworked permission system

---

## Update guide: 6.5 → 6.6

**Source:** https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-65-zu-66

### Prerequisites (mandatory)

| Component | Requirement |
|---|---|
| Shopware source version | 6.5.0.0 or newer |
| PHP | 8.2 |
| Node.js | 20 |
| MySQL | 8.0 or higher |
| MariaDB | 10.11 or higher |
| Git | Installed and configured |

> **NOTE:** If Shopware 6.4 is still in place, first update from 6.4 to 6.5, then to 6.6.

### Extensions: deactivate all of them (mandatory)

Same procedure as for 6.4 → 6.5:

1. Set the theme to the default
2. Deactivate the theme extension
3. Deactivate all further extensions
4. Run the update
5. After the update: update and reactivate the extensions

### Running the update

Update as described in the general instructions, via the administration.

### New features in Shopware 6.6

Documented in detail in the 6.6 update guide (see the next section).

---

## Update guide: Shopware 6.6 — new features

**Source:** https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-shopware-66

**Applies to:** Shopware 6.6.0.0 and newer

### System requirements 6.6

| Component | Requirement |
|---|---|
| PHP | 8.2+ |
| Node.js | 20 |
| Redis | 7.0 (optional) |
| MariaDB | 10.11+ |
| MySQL | 8.0+ |

### Technical new features

#### Full Vue 3 support
- Vue 3 is fully enabled in the admin area
- Extension incompatibilities are possible → individual extension updates required
- Extension developers must switch to the Vue 3 API

#### Webpack 5 with SWC
- Webpack updated to version 5
- Babel replaced by SWC → **three times faster** admin builds
- Plugin extensions with their own Webpack configurations must be migrated to the Webpack 5 API

#### Faster storefront performance
- Improved page speed (an SEO advantage)
- Up to 6× faster indexing for multilingual shops
- Improved Elasticsearch/OpenSearch mapping: several languages in one index

#### Automatic logout (extendable)
- The login session can be extended to up to 14 days via a checkbox
- Configurable: Einstellungen (Settings) > Login-Einstellungen (Login settings)

#### Warehouse management (Lagerbestand — stock)
- Stock is now deducted when the order is placed (not only on completion)
- Adjustable: the stock calculation can be disabled

#### Media path storage
- File paths are now stored permanently in the database (previously calculated dynamically)
- Fixes performance problems and "file not found" errors of the previous versions

#### Language-dependent Elasticsearch indexes
- OpenSearch/Elasticsearch indexes now support language-specific configurations
- Improved performance for multilingual shops

---

## Update guide: Shopware 6.7 — new features

**Source:** https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-shopware-67

**Applies to:** Shopware 6.7.0.0 and newer

### System requirements 6.7

| Component | Requirement | Excluded versions |
|---|---|---|
| PHP | 8.2, 8.3 or 8.4 | — |
| Node.js | 20+ | — |
| MySQL | 8.0.17+ | 8.0.20, 8.0.21 (bugs!) |
| MariaDB | 10.11+ | 10.11.5, 11.0.3 (bugs!) |
| Redis | 7.0+ (optional) | — |
| OpenSearch | 1.0+ (optional) | — |
| Elasticsearch | 7.8+ (optional) | — |

### Technical new features

#### Webpack → Vite migration
- The frontend toolchain has been switched over to Vite entirely
- **Consequence for extension operators:** extensions with admin components require separate plugin versions for 6.6 and 6.7
- Storefront extensions must be migrated to the Vite build system

#### Vue 3 without compat mode
- Full Vue 3 compatibility: compatibility mode has been discontinued
- State management: Vuex → Pinia
- **Consequence:** extensions still using Vue 2 APIs are incompatible

#### Cache architecture rework
Substantial improvements:
- **Delayed cache invalidation:** the cache is cleared with a delay (prevents cache stampedes)
- **Store API caching layer removed:** simplified architecture, better performance
- **Expected results:** lower memory consumption, higher cache hit rate

#### Core library updates
| Library | Old version | New version |
|---|---|---|
| PHPUnit | 10 | 11 |
| League OAuth2 Server | old | current |
| DomPDF | old | current |
| DBAL | 3.x | 4.0 |

> **Note for extension developers (merchant perspective):** extensions that use these libraries directly must be checked for compatibility. In the Shopware Store this is indicated by the compatibility checker.

---

## Upgrade path: skipping several versions

### Is going directly from 6.4 to 6.7 possible?
**No.** Shopware does not support version jumps. Every major update must be carried out individually:

```
6.4.x → 6.4.20.2 → 6.5.x → 6.6.x → 6.7.x
```

### Recommended upgrade path

1. Update to the latest 6.4 patch version (6.4.20.2)
2. Deactivate all extensions
3. Update to 6.5 (latest patch version)
4. Update the extensions to 6.5-compatible versions
5. Deactivate all extensions
6. Update to 6.6 (latest patch version)
7. Update the extensions to 6.6-compatible versions
8. Deactivate all extensions
9. Update to 6.7

---

## Compatibility matrix for common requirements

| Shopware | PHP | Node.js | MariaDB | MySQL | Redis |
|---|---|---|---|---|---|
| 6.4.x | 7.4–8.1 | 14–16 | 10.3+ | 5.7.21+, 8.0+ | 6.0+ |
| 6.5.x | 8.1–8.2 | 18 | 10.11+ | 8.0+ | 7.0+ |
| 6.6.x | 8.2–8.3 | 20 | 10.11+ | 8.0.17+ | 7.0+ |
| 6.7.x | 8.2–8.4 | 20+ | 10.11+ | 8.0.17+ | 7.0+ |

---

*Sources:*
*- https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-64-zu-65*
*- https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-65-zu-66*
*- https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-shopware-66*
*- https://docs.shopware.com/de/shopware-6-de/update-guides/update-guide-shopware-67*
