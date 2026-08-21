# Shopware 6 – Währungen (Currencies), Sprachen (Languages) & Länder (Countries) – complete reference

Sources:
- https://docs.shopware.com/de/shopware-6-de/einstellungen/waehrungen
- https://docs.shopware.com/de/shopware-6-de/einstellungen/sprachen
- https://docs.shopware.com/de/shopware-6-de/einstellungen/laender

---

## Contents

- [Währungen](#währungen)
- [Sprachen](#sprachen)
- [Länder](#länder)

## Währungen

**Path:** Einstellungen (Settings) > Shop > Währungen

### Overview
- Shows all configured currencies
- Context menu: edit or remove
- The factor is based on the topmost system currency (which should remain unchanged)

### Creating a new currency

#### 1. Settings
| Field | Description |
|---|---|
| Name | Label (e.g. "Euro") |
| ISO-Code | Valid ISO currency code |
| Kurzname (Short name) | Three-letter abbreviation (e.g. "EUR") |
| Symbol | Currency symbol (e.g. "€") |
| Faktor (Factor) | Conversion factor relative to the system currency |

#### 2. Price rounding
| Field | Description |
|---|---|
| Nachkommastellen (Decimal places) | Decimal places in cart calculations |
| Rundungsintervall (Rounding interval) | Defines the rounding logic |
| Nettokunden (Net customers) | Apply rounding to net customers |
| Summen (Totals) | Separate settings for grand totals |

#### 3. Countries
Country-specific price rounding settings can be configured differently.

### Editing & removing
- Existing currencies can be edited
- Language variants can be added
- Removal is only possible if the currency is not assigned to any object

### Presentation
The formatting of the currency symbol depends on the selected language:
- German: "499,99 $"
- English: "US$499.99"

---

## Sprachen

**Path:** Einstellungen > Allgemein (General) > Sprachen  
**Available from:** 6.7.3.0

> **Critical:** The system default language is chosen during installation and **cannot be changed afterwards**.

### Overview
All configured languages with name, locale, ISO code, active status.

### Filter options
| Filter | Description |
|---|---|
| Nur Root-Sprachen (Root languages only) | Main languages without inheritance |
| Nur abgeleitete Sprachen (Derived languages only) | Languages that inherit from a parent language |

> Derived languages inherit core components from the parent but allow specific adjustments.

### Fields (create / edit)
| Field | Description |
|---|---|
| Name | Language label |
| Aktiv (Active) | Activate/deactivate in the shop |
| Lokalisierung (Locale) | Country/region assignment |
| ISO-Code | Official code (e.g. `de-DE`, `en-GB`) |
| Erben von (Inherit from) | Parent language (at most one possible) |

### Creating a language
1. Click "Sprache anlegen" (Create language)
2. Fill in the fields
3. Save → the language is available in the sales channels

---

## Länder

**Path:** Einstellungen > Regional > Länder  
**Available from:** 6.7.0.0

### Overview
Table with: country name, positioning, ISO-2 code, ISO-3 code, active status

### Allgemein (General) area (when creating)
| Field | Description |
|---|---|
| Name | Country label (in the system default language) |
| Position | Sort order in the storefront |
| ISO2 | Two-letter ISO code (e.g. DE) |
| ISO3 | Three-letter ISO code (e.g. DEU) |

### Optionen (Options) area (8 switches)
| Option | Description |
|---|---|
| Aktiv | Availability in the shop |
| Versand (Shipping) | Activate/deactivate shipping options |
| Steuerfrei (B2C) (Tax-free, B2C) | Tax exemption for private customers |
| Steuerfrei ab (Tax-free from) | Value threshold for the B2C tax exemption |
| Währungsabhängige Werte (Currency-dependent values) | Multi-currency support |
| Steuerfrei (B2B) (Tax-free, B2B) | Company tax exemption (requires a valid VAT ID) |
| USt-ID-Format überprüfen (Check VAT ID format) | EU validation of the VAT ID |
| USt-ID Pflichtfeld (VAT ID mandatory) | Mandatory entry of the VAT ID |
| EU-Mitgliedstaat (EU member state) | Automatic for EU countries; adds "intra-community delivery" |

### Länder/Regionen (Countries/regions) (tab)
- Manage federal states/regions
- Add new regions: name, ISO code, position
- Inline editing via double-click

### Address management (validation)
| Option | Description |
|---|---|
| Land/Region Pflichtfeld (Country/region mandatory) | Mandatory entry in the address form |
| Postleitzahl Pflichtfeld (Postcode mandatory) | Mandatory entry |
| Postleitzahl validieren (Validate postcode) | Activate format validation |
| Erweiterte Validierungsregeln (Advanced validation rules) | RegEx format (e.g. `^\d{5}$` for 5 digits) |

**Examples:**
- `^\d{5}$` → exactly 5 digits (Germany)
- `^(\d{4})\s*([A-Z]{2})$` → format "1234 AB" (Netherlands)

### Address format
- Country-specific address formatting is configurable (e.g. USA: house number before street)
- A live preview is available for validation
