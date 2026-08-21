# Migration process: Shopware 5 → Shopware 6 (step by step)

**Source**: https://docs.shopware.com/de/migration-de/Migrationsprozess

---

## Contents

- [Step 1: install the extensions](#step-1-install-the-extensions)
- [Step 2: create an integration in the source shop (API access)](#step-2-create-an-integration-in-the-source-shop-api-access)
- [Step 3: establish the migration connection](#step-3-establish-the-migration-connection)
- [Step 4: check the migration data](#step-4-check-the-migration-data)
- [Step 5: start the migration](#step-5-start-the-migration)
- [Running the migration again](#running-the-migration-again)
- [Shopware 5: metadata adjustment before the migration](#shopware-5-metadata-adjustment-before-the-migration)

## Step 1: install the extensions

### In the target shop (Shopware 6)
- Extension: **SwagMigrationAssistent** (from the Community Store)
- The documentation applies from version **16.0.0** of the assistant

### In the source shop (Shopware 5)
- Extension: **SwagMigrationConnector**

> **Recommendation:** complete the data migration entirely **before** starting on design/styling.
> The process is iterative and may require system resets.

---

## Step 2: create an integration in the source shop (API access)

**Path in the source shop (SW6):** **Einstellungen** (Settings) **> System > Integrationen** (Integrations) **> Integration anlegen** (Create integration)

| Field | Description | Note |
|---|---|---|
| **Name (1)** | Unique name (e.g. "Migration") | To distinguish several integrations |
| **Administrator (2)** | Enable the checkbox | Grants full access to the source shop resources |
| **Zugangs-ID (3)** (Access ID) | Generated automatically | **Write it down!** — needed in step 3 |
| **Sicherheitsschlüssel (4)** (Secret access key) | Generated automatically | **Write it down!** — needed in step 3 |

To finish: click the **"Integration speichern"** (Save integration) button.

---

## Step 3: establish the migration connection

**Path in the target shop:** **Einstellungen > Erweiterungen** (Extensions) **> Migrations-Assistent**

### 3.1 Initial connection
1. Click the **"Initiale Verbindung anlegen"** (Create initial connection) button
2. Choose the profile:
   - `Shopware 5.5` for an SW5 migration
   - `Shopware 6` for an SW6-to-SW6 migration
3. Click **"Fortfahren"** (Continue)

### 3.2 Configure the connection

**Connection fields (all source systems):**

| Field | Content |
|---|---|
| **Name** | Unique connection name (important with several source shops) |
| **Profil** (Profile) | Source system type (e.g. Shopware 5.5) |
| **Schnittstelle** (Interface) | Connection type (see below) |

> ⚠️ **Warning:** do not use hyphens in the connection name!

### 3.3 Connection types (Shopware 5)

#### API method
| Field | Description |
|---|---|
| **API-Schlüssel** (API key) | From the SW5 user administration |
| **Benutzername** (User name) | Admin user (group: local_admins) |
| **Shopdomain** (Shop domain) | With SSL status |

#### Local method (direct access to the DB)
| Field | Description |
|---|---|
| **DB-Host** | `localhost` or a URL |
| **DB-Port** | Default: `3306` |
| **DB-Benutzer** (DB user) | User with admin rights |
| **DB-Passwort** (DB password) | The corresponding password |
| **DB-Name** | Name of the SW5 database |
| **Root Verzeichnis** (Root directory) | Absolute installation path |

#### Shopware 6 profile (API is the only option)
Enter the access ID and secret access key from step 2.

---

## Step 4: check the migration data

### Overview page
After the connection has been configured the migration overview appears with:
- (1) Shop system / current connection
- System profile and interface type
- Time of the last connection check
- Time of the last migration

**Actions:**
- Button **"Verbindung bearbeiten"** (Edit connection) (2) — make changes
- Context menu (3) with options:
  - Create a new connection
  - Delete the credentials
  - Switch to another connection
  - **"Prüfsumme zurücksetzen"** (Reset checksum) (forces a complete retransfer of all data)

### Data selection
Set the checkboxes for the desired data. What is shown:
- Data type (**Shopdaten** – shop data – vs. **Plugindaten**/extension data)
- Number of records to be migrated
- Information about third-party extensions

> Third-party data appears with the type **"Plugindaten"** in the list.

### Data check
Automatic check for mappability:
- **Successful mapping:** the migration can start immediately
- **Manual mapping required:** make corrections, then click **"Fortfahren"**
- Example of follow-up work: assign a default payment method
- Automatic mappings can be reviewed and readjusted

### History
- All previous migration attempts can be viewed
- Context menu: **"Details anzeigen"** (Show details) or **"Protokoll herunterladen"** (Download log) (.txt file)

---

## Step 5: start the migration

Click the **"Migration starten"** (Start migration) button.

### The 6 migration phases

#### Phase 1: reading the data
- All records from the source shop are captured
- A **checksum** is generated for every record
- Data that has already been transferred and is unchanged is **not migrated again**
- Reset checksums: context menu > "Prüfsumme zurücksetzen" (forces a full transfer)

#### Phase 2: troubleshooting (intelligent pause)
- Problematic records are identified
- Corrections are possible directly in the admin interface
- No restart is required after corrections

#### Phase 3: writing the data
Automatically created if not yet present in the target shop:
- Customer groups
- Categories
- Languages
- Currencies
- Sales channels

#### Phase 4: download
- Media files are downloaded from the source shop
- Stored in the media management of the target shop

#### Phase 5: cleanup
- Cached data is deleted from the `swag_migration_data` table

#### Phase 6: indexing
- All Shopware indexers are triggered again
- Ensures Shopware-internal data integrity

### Log book
- Errors, warnings, information after the migration
- Download link: **"Protokoll herunterladen"**
- Also retrievable later via **Historie > Details** (History > Details)

---

## Running the migration again

The migration can be repeated **as often as you like**.

**Default behaviour (with checksums):**
- Changed data is migrated again
- Unchanged data is skipped

**Forcing a complete retransfer:**
1. Open the migration overview
2. Shop system area > context menu (1)
3. Choose **"Prüfsumme zurücksetzen"**
4. All data is **overwritten** in the target system

---

## Shopware 5: metadata adjustment before the migration

Some metadata is truncated to **varchar(255)**:

| Table | Columns |
|---|---|
| s_articles | description |
| s_categories | metadescription, metakeywords |

> **Note:** texts over 255 characters are cut off. Check before the migration!

---

*Source: https://docs.shopware.com/de/migration-de/Migrationsprozess | https://docs.shopware.com/de/migration-de/shopware6-Migrationsprozess*
