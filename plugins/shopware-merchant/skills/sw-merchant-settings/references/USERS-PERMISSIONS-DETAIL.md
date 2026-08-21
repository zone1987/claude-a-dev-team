# Shopware 6 – Benutzer & Rechte (Users & permissions) – complete reference

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/System/benutzer

---

## Contents

- [Overview](#overview)
- [1. User management](#1-user-management)
- [2. Role management](#2-role-management)
- [3. Permission system](#3-permission-system)
- [4. Additional permissions (Allgemein)](#4-additional-permissions-allgemein)
- [5. Detailed privileges](#5-detailed-privileges)
- [6. Configuring the admin search](#6-configuring-the-admin-search)

## Overview

**Path:** Einstellungen (Settings) > System > Benutzer & Rechte  
**Available from:** 6.4.5.0

Management of administrators and their access rights in Shopware 6.

---

## 1. User management

### User overview
- All created administrators with names, roles, email addresses
- Editing and deletion via the context menu
- "Neuer Benutzer" (New user) button

### Fields when creating a user

| Field | Description |
|---|---|
| Vorname / Nachname (First name / Last name) | Identification |
| E-Mail-Adresse (Email address) | Required for password reset |
| Benutzername (Username) | Login credentials |
| Passwort (Password) | Admin access (changeable in the profile) |
| Sprache der Benutzeroberfläche (Interface language) | Selectable language (changeable in the profile) |
| Jobtitel (Job title) | Internal job designation |
| Profilbild (Profile picture) | To distinguish users in user lists |
| Administrator-Status | Full rights (cannot be assigned to yourself) |
| Zeitzone (Time zone) | For consistent time information |
| Rollen (Roles) | Assignment of predefined roles (only if not an admin) |

---

## 2. Role management

### Role overview
- All roles with name and description
- Editing/deletion via the context menu
- "Neue Rolle" (New role) button

### Fields
- **Name:** meaningful label
- **Beschreibung** (Description): short characterisation of the role

---

## 3. Permission system

### Hierarchy of the main permissions

| Permission | Description |
|---|---|
| **Ansehen** (View) | Visibility only, no changes |
| **Bearbeiten** (Edit) | Change existing configurations |
| **Erstellen** (Create) | Add new entities |
| **Löschen** (Delete) | Remove entities (automatically with the view right) |
| **Alle** (All) | Full access to the area |

**Inheritance hierarchy:** Löschen → Ansehen; Erstellen → Bearbeiten → Ansehen

---

## 4. Additional permissions (Allgemein)

| Permission | Scope |
|---|---|
| Grundlegende Einstellungen (Basic settings) | Einstellungen > Shop (addresses, login/registration, products, SEO, sitemap, Stammdaten (Master data), cart) + System (mailer, Shopware account) |
| Update starten (Start update) | Search for and install Shopware updates |
| Erweiterungen verwalten (Manage extensions) | Installation, uninstallation, activation, deactivation |
| Erweiterung hochladen (Upload extension) | ZIP file upload in Meine Erweiterungen (My extensions) |
| Ereignis-Logs (Event logs) | Access to Shopware and system logs |
| Cache leeren (Clear cache) | Manage Caches & Indizes (Caches & indexes) |
| Import/Export | Data import/export, profile management |
| Shopware Store | Store access |
| Eigenes Profil ändern (Change own profile) | Personal profile settings |
| Gutschriften erstellen (Create credit notes) | Voucher line items in the orders module |
| Apps | The entire extensions area |

---

## 5. Detailed privileges

For exceptional cases (e.g. extensions without correct ACL):
- Technical names of all permissions
- Granular read/write/create/delete rights per function
- Greyed-out checkboxes = already granted in the "Allgemein" (General) tab

### Error handling
Error messages show the missing permissions (e.g. `order`, `order_customer`, `order_delivery` — edit right) for manual reconfiguration.

---

## 6. Configuring the admin search

Configurable per user:
- Selective release of areas for search results
- Example: promotions area enabled → searching for discount codes becomes possible
