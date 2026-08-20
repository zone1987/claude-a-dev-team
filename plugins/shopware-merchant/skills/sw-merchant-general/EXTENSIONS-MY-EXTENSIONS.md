# Meine Erweiterungen (My extensions) – the management centre

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen  
**Path in the admin**: Erweiterungen (Extensions) > Meine Erweiterungen

## Contents

- [Overview](#overview)
- [Navigation structure](#navigation-structure)
- [Installing an extension](#installing-an-extension)
- [Activating / deactivating an extension](#activating-deactivating-an-extension)
- [Configuring an extension](#configuring-an-extension)
- [Updating an extension](#updating-an-extension)
- [Shopware Account tab](#shopware-account-tab)
- [Managing licences](#managing-licences)
- [Plans and extensions](#plans-and-extensions)
- [Common problems](#common-problems)

## Overview

The **Erweiterungen** area is the central management centre for all installed
and available extensions in Shopware 6. It makes it possible to extend the
standard feature set with apps, plugins and themes.

---

## Navigation structure

```
Erweiterungen
├── Store          → Shopware Erweiterungsmarktplatz (browsen & kaufen)
└── Meine Erweiterungen
    ├── Apps-Tab   → Installierte Apps
    ├── Plugins-Tab → Installierte Plugins
    └── Themes-Tab  → Installierte Themes
```

---

## Installing an extension

### From the Shopware Store (online)
1. Open **Erweiterungen** (Extensions) **> Store**
2. Search for the extension (for example "PayPal", "Klarna")
3. Click **Hinzufügen** (Add) or **Kaufen** (Buy)
4. The Shopware Account has to be linked (tab: Shopware Account)
5. After the purchase the extension appears under **Meine Erweiterungen**
6. Click **Installieren** (Install) → click **Aktivieren** (Activate)

### Manually (ZIP upload)
1. Open **Erweiterungen** (Extensions) **> Meine Erweiterungen**
2. **Erweiterung hochladen** (Upload extension) (ZIP file)
3. Install + activate

### Via Composer (the developer route)
```bash
composer require shopware/[extension-name]
php bin/console plugin:refresh
php bin/console plugin:install --activate [PluginName]
```

---

## Activating / deactivating an extension

| Action | Procedure | Effect |
|---|---|---|
| Aktivieren (Activate) | Toggle switch → ON | The extension runs; the shop cache is cleared |
| Deaktivieren (Deactivate) | Toggle switch → OFF | The extension stays installed but is inactive |
| Deinstallieren (Uninstall) | Three-dot menu > Deinstallieren | Removes the code; data can optionally be deleted |

> **Note**: On activation/deactivation the shop cache is cleared automatically.
> On large shops this can cause brief loading times.

---

## Configuring an extension

After the activation an extension can be configured:

1. **Three-dot menu** (⋮) next to the extension → **Konfigurieren** (Configure)
2. Or directly via: **Einstellungen** (Settings) **> Erweiterungen > [extension name]**

---

## Updating an extension

- In the **Meine Erweiterungen** area an **update badge** appears for new versions
- Bell icon (top right in the admin): notifies you about available updates
- Performing the update: click **Aktualisieren** (Update) → the compatibility check runs automatically

---

## Shopware Account tab

The **Meine Erweiterungen** area has a **Shopware Account tab**:
- Link the Shopware Account to the shop
- Check the licence information
- Troubleshoot licence problems

---

## Managing licences

| Licence type | Description |
|---|---|
| Free licence | No costs; installation after linking the account |
| Monthly rental | Monthly debit; can be cancelled at any time |
| Purchase (one-off) | One-off payment; all future updates included |
| Trial licence | Time-limited (usually 14–30 days) |

Managing licences: https://account.shopware.com > Lizenzen (Licences)

---

## Plans and extensions

Some extensions are **part of a plan** (Rise, Evolve, Beyond) and are unlocked via
the **Shopware Commercial Extension**:

- **Shopware Rise**: Custom Products, Social Shopping, Immersive Elements, AI Copilot
- **Shopware Evolve**: + Advanced Search, CMS extensions, Dynamic Access, B2B, Publisher
- **Shopware Beyond**: + Digital Sales Rooms, Kundenspezifische Preise, Multi-Inventory

→ Details: `shopware-commercial.md`

---

## Common problems

| Problem | Solution |
|---|---|
| "Keine Verbindung zum Store" (No connection to the store) | Link the Shopware Account; check the firewall |
| The extension becomes inactive after an update | Check the compatibility; if necessary wait for a newer version |
| Licence not found | Is the domain entered correctly in the Shopware Account? |
| Cache error after the activation | Run `php bin/console cache:clear` |
