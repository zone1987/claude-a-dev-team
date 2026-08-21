# What is carried over during the migration?

**Source**: https://docs.shopware.com/de/migration-de/Systemvoraussetzungen  
(the detail page was reachable via the category parameter at the time of crawling)

## Basic principle

The **Migrationsassistent** (Migration Assistant, SwagMigrationAssistent) transfers data from the source system
to Shopware 6. What exactly is migrated depends on the source system.

---

## Shopware 5 → Shopware 6

### Shop data (standard, selectable via checkbox)

| Data type | Notes |
|---|---|
| Products | Incl. variants, properties, prices |
| Categories | Category hierarchy and assignments |
| Manufacturers | Manufacturer data |
| Customers | Accounts and personal data |
| Customer addresses | Shipping and billing addresses |
| Orders | Orders and line items |
| Media | Images and media files (downloaded from the source shop) |
| Tax rules | Tax classes |
| Currencies | Currency configuration |
| Languages | Language configuration |

### Plugin data (third party)
Some third-party extensions provide their own migration profiles.
These appear in the data selection with the type **"Plugindaten"** (plugin data).

### Not migrated (typically)
- Shop design / theme (has to be rebuilt)
- Custom plugin configurations (only if the plugin offers a migration profile)
- SEO URLs (are regenerated)
- CMS pages / **Erlebniswelten** (Shopping Experiences) (have to be recreated)

---

## Shopware 6 → Shopware 6

The scope is analogous to SW5→SW6, since the same Migrationsassistent is used.
Limitation: the source and target systems must be on an **identical Shopware version**.

---

## Magento → Shopware 6

See the Magento dictionary (term mapping Magento ↔ Shopware):
`docs.shopware.com/de/migration-de/magento`

Typical data: products, categories, customers, orders, media.

---

## Metadata restriction (Shopware 5)

When migrating from Shopware 5, some metadata is **truncated to 255 characters**:

| Table | Columns |
|---|---|
| s_articles | description |
| s_categories | metadescription, metakeywords |

**Note:** longer texts are cut off after 255 characters. Check the content beforehand.

---

## Checking the system requirements (Shopware 5)

Install the **SwagMigrationAssistent** plugin in the SW5 backend:
1. Reload the backend after installation and activation
2. Click the question mark icon in the menu bar
3. Open "Shopware 6 Update-Check"
4. **Tab "Voraussetzungen"** (Requirements): shows fulfilled/unfulfilled server requirements
5. **Tab "Plugins"**: shows which plugins are available/configurable for SW6

---

*Source: https://docs.shopware.com/de/migration-de/Systemvoraussetzungen*
