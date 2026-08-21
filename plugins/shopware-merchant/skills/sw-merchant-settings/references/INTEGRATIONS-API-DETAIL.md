# Shopware 6 – Integrationen (Integrations) & API access – complete reference

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/system/integrationen

---

## Overview

**Path:** Einstellungen (Settings) > System > Integrationen  
**Available from:** 6.3.3.0

Allows external applications and systems to be connected via the Shopware API.

---

## Creating an integration

1. Click "Integration anlegen" (Create integration)
2. Enter a **Name** (identifies the integration)
3. Choose **Berechtigungen** (Permissions): administrator or custom roles
4. **Zugangsdaten generieren** (Generate credentials): an access ID + secret key are created

> **Important:** The secret key is **shown only once**. Store it securely immediately!

---

## Managing integrations

The overview page shows:
- All created integrations with name and permissions
- Editing by clicking the name
- Context menu for editing or deletion

---

## Editing an integration

When editing later on:
- The secret key is not displayed for security reasons
- The function **"API-Zugangsschlüssel neu generieren"** (Regenerate API access key) renews both credentials (ID and key)

---

## API permissions

| Option | Description |
|---|---|
| Administrator | Full rights (all API endpoints) |
| Custom roles | Granular rights assignment as with user roles |

---

## Using the credentials

The generated credentials (Access Key + Secret Key) are used for:
- OAuth 2.0 client credentials flow
- API requests with bearer token authentication

Complete API documentation: https://developer.shopware.com

---

## API access for individual users

Alternatively, API access can be tied directly to users:
**Path:** Einstellungen > System > Benutzer & Rechte (Users & permissions) > [user] > Integrationen (tab)

- The "Neuer Zugangsschlüssel" (New access key) button generates an API ID + secret key
- Note the secret key immediately (visible only once)
- Editing/deletion via the context menu
