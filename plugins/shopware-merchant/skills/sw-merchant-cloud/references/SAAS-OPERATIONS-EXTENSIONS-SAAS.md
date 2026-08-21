# Shopware SaaS — managing Erweiterungen (Extensions)

**Source**: https://docs.shopware.com/de/shopware-6-de/saas/erweiterungen

> This documentation applies exclusively to users of a **Shopware 6 SaaS environment** (not to self-hosted).

---

## Contents

- [Store — finding extensions](#store--finding-extensions)
- [Adding an extension](#adding-an-extension)
- [Managing my extensions](#managing-my-extensions)
- [Installing an extension](#installing-an-extension)
- [Cancelling and removing a paid extension](#cancelling-and-removing-a-paid-extension)
- [Incompatible apps](#incompatible-apps)
- [SaaS updates and extensions](#saas-updates-and-extensions)
- [Prerequisites for extensions](#prerequisites-for-extensions)
- [Uploading extensions from macOS](#uploading-extensions-from-macos)

## Store — finding extensions

Browse and purchase free and paid extensions.

**Available filters:**
- Sorting
- Categories
- Ratings
- Payment model
- Additional options (support, trial versions)

---

## Adding an extension

Process via modal:
1. Accept the terms and conditions (mandatory)
2. Confirm permissions (depending on the app's feature scope)
3. Open the link **Berechtigungen anzeigen** (Show permissions) for details (optional)
4. A success message appears once finished

---

## Managing my extensions

### Apps area
- Overview of all apps with basic information
- Toggle for hiding inactive apps
- Sorting options
- Aktiv (Active)/Inaktiv (Inactive) toggle per app
- Context menu:
  - Show **Berechtigungen** (Permissions)
  - **Aktualisieren** (Update)
  - **Deinstallieren** (Uninstall)
- Upload function for manual installation (ZIP)

### Themes area
- Management functions similar to those for apps
- Additional options: "Datenschutz & Datensicherheit" (Data protection & data security), "Datenschutz-Erweiterungen" (Data protection extensions)
- **Note:** active themes must additionally be assigned to the Verkaufskanal (Sales channel)

---

## Installing an extension

Button **App installieren** (Install app) → start the installation → afterwards "App öffnen" (Open app) is available.

---

## Cancelling and removing a paid extension

Complete removal is required (deactivating alone is not enough to cancel).

**Procedure:**
1. "..." button next to the extension
2. Choose **Kündigen und entfernen** (Cancel and remove)

> ⚠️ **Warning:** all settings of the extension are lost!

---

## Incompatible apps

**Marking:** shown when apps are not compatible with the upcoming Shopware major version.

**Automatic behaviour:** apps are deactivated automatically on the version update if they have not been updated by then.

**Action:** update and reactivate the app manually.

---

## SaaS updates and extensions

- Shopware updates the SaaS shop **automatically**
- Incompatible extensions can be **deactivated automatically** in the process
- The operator must **update and reactivate** extensions **manually**
- Status information: `https://status.shopware.com/`

---

## Prerequisites for extensions

Required even for **free** extensions:

1. **Company information** (Einstellungen (Settings) > Account > Firma (Company))
2. **Payment method for billing** (Einstellungen > Account > Abrechnungen (Billing) > Zahlungsart (Payment method))

---

## Uploading extensions from macOS

> ⚠️ When compressing, macOS automatically creates a subfolder inside the ZIP file.

Solution: compress the extension via terminal (without macOS metadata):
```bash
cd /Pfad/zum/Plugin-Ordner
zip -r plugin-name.zip . -x "*.DS_Store" -x "__MACOSX/*"
```

---

*Source: https://docs.shopware.com/de/shopware-6-de/saas/erweiterungen*
