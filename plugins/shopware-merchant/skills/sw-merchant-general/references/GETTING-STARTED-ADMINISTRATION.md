# Administration at a glance

**Source**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/administration-ueberblick

## Overview

The Shopware 6 administration is the central backend for managing the online shop.
It uses a single display format (no separate window management) and can be opened in
**several browser tabs in parallel**.

---

## Access

- **URL scheme**: `https://www.meinshop.de/admin`
- **Login**: email/username + password
- **Forgotten password**: via the login screen, confirmation email to the stored address

---

## Main areas of the interface

### 1. Left-hand navigation bar

The primary navigation runs down the left and contains:

| Area | Description |
|---|---|
| **Dashboard** | Start page after login, statistics overview |
| **Bestellungen** (Orders) | Order management, returns |
| **Kunden** (Customers) | Customer master data, groups |
| **Katalog** (Catalogue) | Products, categories, properties, media |
| **Content** | Erlebniswelten (Shopping Experiences / CMS) |
| **Marketing** | Promotions, vouchers, newsletter |
| **Verkaufskanäle** (Sales channels) | Storefront, headless, social, POS |
| **Erweiterungen** (Extensions) | Store, Meine Erweiterungen (My extensions) |
| **Einstellungen** (Settings) | System, payments, shipping, taxes, users |

- At the top of the bar: the **Shopware version number** is visible
- At the bottom of the bar: **Profil-Einstellungen** (Profile settings) (name, language, password)
- **Minimise the navigation**: click the arrow icon → only icons are shown (more room)

---

### 2. Top bar

| Element | Function |
|---|---|
| **Search bar (centre)** | Searches across products, categories, customers, orders, media |
| **Bell icon** | Notifications: system updates, plugin updates, hints |

---

### 3. Content area

- Shows the content of the currently selected menu entry
- **Multiple tabs**: browser tabs can show different admin pages independently of each other
- No desktop window metaphor – all actions happen in the same tab

---

## Keyboard shortcuts

| Shortcut | Function |
|---|---|
| `Ctrl/Cmd + F` | Open the quick search |
| Typing `#` in the search | Open the module filter selection |

Full overview: **Profil** (Profile) **> Tastenkürzel** (Keyboard shortcuts)

---

## Multi-language support in the administration

- Switch the language: Profil (bottom left) > select the language
- Available languages: depending on the installed language pack
- Default: German and English

---

## Interactive learning path

The **Community Hub** (https://hub.shopware.com) offers an interactive learning path
for getting hands-on with the administration:
- Step-by-step instructions
- Sandbox exercises
- Networking with other Shopware users

---

## Note: permissions

Not all menu entries are visible to every user. This depends on the
**user role** (configurable under Einstellungen > System > Benutzer & Rechte (Users & permissions)).

- Administrator: full access
- Custom roles: restricted visibility/editing
