# Migration process: Shopware 6 → Shopware 6

**Source**: https://docs.shopware.com/de/migration-de/shopware6-Migrationsprozess

---

## Use cases

- Moving to the Shopware Cloud (SaaS)
- Server change / hosting change
- Transferring a staging instance → live instance

---

## Critical prerequisite

> ⚠️ **The source and target systems must use the same Shopware version.**
> A migration between different versions is **not possible**.

---

## Differences from SW5→SW6

- **No SwagMigrationConnector** needed in the source shop (no separate connector)
- The **SwagMigrationAssistent** must also be installed and active in the source shop
- The connection type is **API only** (no local mode)
- Profile: choose **"Shopware 6"** in the assistant

---

## Step 1: install the extensions

### In the source shop (SW6)
- Install and activate **SwagMigrationAssistent**

### In the target shop (SW6)
- Install and activate **SwagMigrationAssistent**
- From version **16.0.0** of the assistant

---

## Step 2: create an integration in the source shop

**Path:** **Einstellungen** (Settings) **> System > Integrationen** (Integrations) **> Integration anlegen** (Create integration)

| Field | Description |
|---|---|
| **Name** | e.g. "Migration" |
| **Administrator** | Enable the checkbox (mandatory!) |
| **Zugangs-ID** (Access ID) | Generated automatically — store it temporarily! |
| **Sicherheitsschlüssel** (Secret access key) | Generated automatically — store it temporarily! |

Save with: **"Integration speichern"** (Save integration)

---

## Step 3: establish the connection in the target shop

**Path:** **Einstellungen > Erweiterungen** (Extensions) **> Migrations-Assistent**

1. Click **"Initiale Verbindung anlegen"** (Create initial connection)
2. Profile: choose **"Shopware 6"**
3. **"Fortfahren"** (Continue)
4. Configure the connection:

| Field | Content |
|---|---|
| **Name** | Unique connection name |
| **Profil** (Profile) | Shopware 6 |
| **Schnittstelle** (Interface) | API (the only option) |
| **Zugangs-ID** | From step 2 |
| **Sicherheitsschlüssel** | From step 2 |
| **Shopdomain** (Shop domain) | URL of the source shop |

> ⚠️ No hyphens in the connection name!

---

## Steps 4–6: check the data, start the migration, go live

The remaining sequence corresponds to the SW5→SW6 migration:
→ detailed docs: `references/deep/migrationsprozess-sw5-sw6.md`

---

*Source: https://docs.shopware.com/de/migration-de/shopware6 | https://docs.shopware.com/de/migration-de/shopware6-Migrationsprozess*
