# Shopware 6 – CMS-Erweiterungen (CMS extensions): full documentation

**Source:** https://docs.shopware.com/de/shopware-6-de/erweiterungen/cms-erweiterungen  
**Version:** from 1.0.1; current version 2.2.0+

---

## Contents

- [Screenshots](#screenshots)
- [Overview](#overview)
- [Installation](#installation)
- [Feature 1: Quickview](#feature-1-quickview)
- [Feature 2: Suchergebnisse-Quickview](#feature-2-suchergebnisse-quickview)
- [Feature 3: Scroll-Navigation](#feature-3-scroll-navigation)
- [Feature 4: Block-Sichtbarkeit via the Rule Builder](#feature-4-block-sichtbarkeit-via-the-rule-builder)
- [Feature 5: Custom Forms (Benutzerdefinierte Formulare)](#feature-5-custom-forms-benutzerdefinierte-formulare)
- [Changelog (version history)](#changelog-version-history)
- [Related documentation](#related-documentation)

## Screenshots

| File | Content |
|---|---|
| `../../assets/quickview.png` | Quickview in the listing |
| `../../assets/scroll-navigation-sektion.png` | Scroll-Navigation section setting |
| `../../assets/scroll-navigation-frontend.png` | Scroll-Navigation in the storefront |
| `../../assets/block-sichtbarkeit.png` | Block-Sichtbarkeit via the Rule Builder |
| `../../assets/custom-form-erstellen.png` | Creating a custom form |
| `../../assets/custom-form-optionen.png` | Custom form options |
| `../../assets/custom-form-felder.png` | Custom form fields and groups |

---

## Overview

The **CMS-Erweiterungen** are an official Shopware extension available as part
of **Shopware Evolve** (and higher plans).

They extend the Erlebniswelten (Shopping Experiences) with the following core functions:
1. Quickview (product preview in the listing)
2. Suchergebnisse-Quickview (search results quickview)
3. Scroll-Navigation (anchor points)
4. Block-Sichtbarkeit (block visibility) via the Rule Builder
5. Custom Forms (Benutzerdefinierte Formulare — custom forms)

---

## Installation

### Prerequisites
- Shopware Evolve plan or higher on the shop domain
- Shopware account stored in the admin

### Steps
1. Admin > **Erweiterungen** (Extensions) > **Meine Erweiterungen** (My extensions)
2. Search for the "CMS-Erweiterungen" extension
3. "Installieren" (Install) → "Aktivieren" (Activate)
4. Adjust the shop configuration if needed

---

## Feature 1: Quickview

### Function
Allows a product preview directly in the listing, without leaving the category page.
Users click a product and immediately get a modal preview dialogue.

### Available blocks
Quickview works with the following Erlebniswelten blocks:
- **Drei Spalten Produkte-Boxen** (Three-column product boxes)
- **Produkt-Slider** (Product slider)
- **Cross-Selling**

### Activation
After installing the extension, Quickview is automatically active for supported blocks.

### Configuration
- Open the extension settings (under Erweiterungen > CMS-Erweiterungen > Konfiguration (Configuration))
- Enable/disable Quickview

---

## Feature 2: Suchergebnisse-Quickview

### Function
Extends the Quickview functionality to the **search results page**.

Users can view product details directly in the search without having to navigate to
the product detail page.

### Activation
In the extension configuration under:
- CMS-Erweiterungen > Konfiguration > "Quickview auf Suchergebnisseite aktivieren" (Enable quickview on the search results page)

---

## Feature 3: Scroll-Navigation

### Function
Creates an **anchor-point navigation** within an Erlebniswelten page.
Especially useful for long landing pages with several sections.

### Presentation in the storefront

**Desktop:**
- The navigation appears as a vertical menu on the **left-hand side**
- It scrolls along with the user (sticky)
- The active section is highlighted

**Mobile:**
- The navigation appears as buttons at the bottom right
- Expandable menu

### URL parameters
Sections can be jumped to directly via URL anchors:
```
https://meinshop.de/landingpage/#sektionsname
```
Example: `/#lorem%20ipsum`

### Setup
1. Open the Erlebniswelten layout
2. Click the section → section settings
3. Assign a section name (used as the anchor)
4. Scroll-Navigation is active automatically once the extension is installed

---

## Feature 4: Block-Sichtbarkeit via the Rule Builder

### Function
Individual CMS blocks can be shown or hidden conditionally based on
**Rule Builder rules**.

### Use cases
- Show blocks only to logged-in customers
- Blocks only for certain Kundengruppen (customer groups)
- Blocks only during certain periods (e.g. a promotion period)
- Control blocks by order history / turnover
- Geographic control (country/region)

### Usage
1. Open the Erlebniswelten layout
2. Click the block → block settings in the right-hand sidebar
3. "Sichtbarkeit" (Visibility) area → assign a rule
4. Select from existing rules or create new ones
5. **Speichern** (Save)

### Rule Builder
Rules are defined in **Einstellungen** (Settings) **> Rule Builder** (or Marketing > Rule Builder).
Complex conditions with AND/OR combinations can be created here.

---

## Feature 5: Custom Forms (Benutzerdefinierte Formulare)

### Function
Allows the creation of **individual forms** with your own fields,
field groups and email templates – going far beyond the standard contact form.

### Areas of use
- Application forms
- Product enquiries with specific fields
- Event registrations
- Callback requests
- Customer surveys

### Available field types
- Text field (single line)
- Textarea (multi-line)
- Email field
- Phone number
- Number
- Date/time
- Selection list (dropdown)
- Checkbox
- Radio buttons
- File upload

### Creating a form

1. Erweiterungen > CMS-Erweiterungen > "Formulare" (Forms) tab
2. "Neues Formular erstellen" (Create new form)
3. **General settings:**
   - Form name
   - Recipient email address(es)
   - Email template for the confirmation email
   - Email template for the notification
4. **Adding fields:**
   - Choose the field type
   - Enter the label/designation
   - Mandatory field (yes/no)
   - Set validation rules
5. **Field groups** (optional): group fields logically
6. **Speichern** (Save)

### Embedding a form in an Erlebniswelt

1. Open the Erlebniswelten layout
2. Open the "Formulare" block category in the sidebar
3. Insert the "Custom Form" block by drag and drop
4. Click the block → select the form from the list
5. **Speichern** (Save)

### Email templates for Custom Forms

Separate templates for:
- **Customer confirmation**: email to the sender after the form is submitted
- **Shop notification**: email to the shop operator with the form content

Templates can be adjusted under Einstellungen > E-Mail-Vorlagen (Mail templates).

---

## Changelog (version history)

| Version | Changes |
|---|---|
| 2.2.0+ | Current version |
| 2.0.0 | Custom Forms feature |
| 1.5.0 | Block-Sichtbarkeit via the Rule Builder |
| 1.3.0 | Suchergebnisse-Quickview |
| 1.1.0 | Scroll-Navigation |
| 1.0.1 | Initial version (Quickview) |

---

## Related documentation

- Erlebniswelten: `sw-merchant-content-shopping-experiences`
- Rule Builder: `sw-merchant-marketing` (Marketing area)
- Standard contact form: Erlebniswelten > "Formular" (Form) block
- Shopware Evolve: https://www.shopware.com/de/preise/
