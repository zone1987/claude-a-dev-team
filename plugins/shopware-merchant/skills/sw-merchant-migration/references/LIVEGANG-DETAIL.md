# Going live after the migration

**Source**: https://docs.shopware.com/de/migration-de/Livegang

---

## Contents

- [Overview](#overview)
- [1. Changes in the Shopware 6 target shop](#1-changes-in-the-shopware-6-target-shop)
- [2. Changes in the source shop](#2-changes-in-the-source-shop)
- [3. Changes at the hoster (DNS routing)](#3-changes-at-the-hoster-dns-routing)
- [4. Cleaning up the migration data](#4-cleaning-up-the-migration-data)
- [Magento-specific note: do not uninstall the extension](#magento-specific-note-do-not-uninstall-the-extension)
- [Go-live checklist](#go-live-checklist)

## Overview

The go-live takes place in three areas:
1. Changes in the **Shopware 6 target shop**
2. Changes in the **source shop** (SW5 / SW6 / Magento)
3. Changes at the **hoster** (DNS routing)

After that: clean up the migration data.

---

## 1. Changes in the Shopware 6 target shop

### 1.1 Transferring the licensing host

**Path:** **Einstellungen** (Settings) **> System > Shopware Account**

- Enter the main domain under which the new shop should be reachable
- Purpose: assign the Shopware licence to the domain correctly

### 1.2 Transferring the domain in the sales channels

**Path:** Administration **> Verkaufskanäle** (Sales channels)

- Every sales channel has a URL field
- Enter the new main domain
- Field: **"URL"**

> ⚠️ This step must be carried out **separately for every subshop / sales channel**!

---

## 2. Changes in the source shop

### Shopware 5
- Move the shop into a subfolder
- Enter the subfolder under Einstellungen > Shopeinstellungen > Shops (Settings > Shop settings > Shops)
- Goal: the main domain is freed up for SW6

### Shopware 6
- Transfer the domain in the sales channel to a new (fallback) domain
- The main domain is freed up for the target shop

### Magento
- Configure Magento so that it is **no longer reachable under the main domain**
- Set a new/different domain for Magento instead

---

## 3. Changes at the hoster (DNS routing)

The **shop domain must route to the subdirectory `/public/`** in the Shopware 6 installation directory.

### Apache configuration (example)

```apache
<VirtualHost *:80>
    ServerName "_HOST_NAME_"
    DocumentRoot _SHOPWARE_DIR_/public

    <Directory _SHOPWARE_DIR_>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Order allow,deny
        allow from all
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/shopware-platform.error.log
    CustomLog ${APACHE_LOG_DIR}/shopware-platform.access.log combined
    LogLevel debug
</VirtualHost>
```

**Replace the placeholders:**
- `_HOST_NAME_` → your own domain (e.g. `www.meinshop.de`)
- `_SHOPWARE_DIR_` → absolute path to the SW6 installation (e.g. `/var/www/shopware6`)

> **Important:** `DocumentRoot` points to `/public/` — not to the main directory!

---

## 4. Cleaning up the migration data

After a successful go-live the migration data should be removed from the database.

**Path:** **Einstellungen > Erweiterungen** (Extensions) **> Migrations-Assistent**

**Action:** context menu > **"Migrationsdaten aufräumen"** (Clean up migration data)

**Effect:** deletes all records cached for the migration from the database.

> ⚠️ **After the cleanup** no further data updates can be transferred from the source shop
> via the Migrationsassistent!

### Important note for SW5 with the plugin migration assistant
If the **plugin migration assistant** was used during the migration to book test licences:
→ finalise the **migration there first**, before clicking "Migration abschließen" (Complete migration) in the Migrationsassistent!

---

## Magento-specific note: do not uninstall the extension

> ⚠️ For a Magento migration: do **NOT uninstall the migration extension!**
>
> Reason: the **password algorithms** used by Magento are contained in the
> extension. Without the extension migrated customers **can no longer log in**.

---

## Go-live checklist

- [ ] Licensing host in SW6 transferred to the new domain (Einstellungen > System > Shopware Account)
- [ ] Domain transferred in **all** sales channels
- [ ] Source shop switched to a subfolder / alternative domain
- [ ] Apache/Nginx: DocumentRoot points to `/public/`
- [ ] DNS propagation awaited (can take some time)
- [ ] Shop reachable and functional under the new domain
- [ ] Migration data cleaned up (context menu > "Migrationsdaten aufräumen")
- [ ] For Magento: migration extension NOT uninstalled

---

*Source: https://docs.shopware.com/de/migration-de/Livegang*
