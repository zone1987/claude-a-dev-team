# Anpassbare Popups & Benachrichtigungen (Customisable popups & notifications)

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/anpassbare-popups-und-benachrichtigungen  
**Availability**: Free of charge in the Shopware Store  
**Minimum version**: Shopware 6.4.0.0

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [Configuration path](#configuration-path)
- [Popup types](#popup-types)
- [Multi-channel configuration](#multi-channel-configuration)
- [GDPR notes](#gdpr-notes)

## Overview

The **Anpassbare Popups & Benachrichtigungen** extension enables various
popup and banner types for the storefront – for customer communication on a shop visit.

---

## Installation

1. **Erweiterungen** (Extensions) **> Store** → search for "Custom Popups & Notifications"
2. Download it free of charge
3. **Erweiterungen > Meine Erweiterungen** (My extensions) → install + activate

---

## Configuration path

**Erweiterungen > Meine Erweiterungen > Anpassbare Popups & Benachrichtigungen > Konfigurieren** (Configure)

Or directly: **Einstellungen** (Settings) **> Erweiterungen > Anpassbare Popups & Benachrichtigungen**

The configuration is possible **per sales channel** (different popups for different shops).

---

## Popup types

### 1. Consent popup
**Description**: The popup appears immediately on the shop visit and has to be **actively confirmed**.

**Use cases**:
- Age verification ("Are you 18 years or older?")
- A general consent/notice for certain shops (for example pharmacies, alcohol shops)

**Configurable**:
- Title
- Description text
- Button text (confirm / decline)
- Redirect on a decline

---

### 2. Banner
**Description**: A configurable bar at the **top edge of the page**.

**Configurable options**:
| Property | Options |
|---|---|
| Background colour | Freely selectable (colour picker) |
| Text colour | Freely selectable |
| Text | Free text |
| Scrolling animation | The text scrolls through (marquee effect) |
| Closable | Yes/no (X button for customers) |
| Permanent | Always visible, even after scrolling |

**Typical use cases**:
- "Kostenloser Versand ab 50 €" (Free shipping from 50 €)
- "SALE: 20% auf alles" (20% off everything) (time-limited)
- "Neue Kollektion jetzt verfügbar" (New collection available now)

---

### 3. Info popup
**Description**: A popup on entering the shop with general information or promotion announcements.

**Configurable**:
- Title
- Description text
- Image upload (a banner image for the visual impression)

**Typical use cases**:
- Seasonal announcements ("Winter Sale beginnt!" – Winter sale starts!)
- Shop news ("Neue Funktionen verfügbar" – New features available)
- Maintenance announcements

---

### 4. Newsletter registration popup
**Description**: A popup right on the shop visit for the **newsletter sign-up**.

**Configurable**:
- Title and description
- Optional fields: first name, last name (on/off)
- Mandatory fields for the sign-up

**Integration**: Linked to the Shopware newsletter system
→ Subscribers appear in **Marketing > Newsletter-Empfänger** (Newsletter recipients)

---

## Multi-channel configuration

A popup can be activated for **several sales channels** or only for **specific channels**.
Each channel can have different popup settings.

---

## GDPR notes

- Consent popup: suitable for mandatory consents
- Newsletter popup: the double opt-in has to be configured in the Shopware settings
  → **Einstellungen > E-Mail-Templates > Newsletter-Bestätigung** (Newsletter confirmation)
