# CMS extensions – Quick View, scroll navigation, block visibility

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/cms-erweiterungen  
**Plan**: Shopware Evolve (or higher)

## Overview

The **CMS extensions** extend the integrated Shopping Experiences (Erlebniswelten)
CMS editor with three essential functions: Quick View, scroll navigation and block visibility.

---

## Installation

1. The **Shopware Evolve plan** must be registered for the shop domain
2. Log in on the Shopware Account tab
3. **Erweiterungen** (Extensions) **> Meine Erweiterungen** (My extensions) → install + activate CMS Erweiterungen

---

## Function 1: Quick View

**What it is**: a quick view of a product straight from the category listing,
without leaving the category.

**Applicable to**:
- Product boxes in category listings
- Product sliders
- Cross-selling elements

**Activation**:
1. Open the Erlebniswelten (Shopping Experiences) editor (Content > Erlebniswelten)
2. Select a product listing element
3. In the element settings: switch on "Quick View aktivieren" (Enable Quick View)

**Storefront behaviour**: customers click a product → a modal window opens with product details,
variant selection and an "In den Warenkorb" (Add to cart) button.

---

## Function 2: Scroll navigation

**What it is**: navigation anchors within long Erlebniswelten pages.
Shows a navigation menu on the left (desktop) or at the bottom right (mobile).

**Usage**:
1. Open the shopping experience in the editor
2. Select the section/block that should appear as a navigation point
3. Block settings → "Navigationspunkt setzen" (Set navigation point) + assign a name

**Storefront behaviour**:
- Desktop: the navigation menu appears on the left of the page
- Mobile: navigation controls at the bottom right

**Typical use case**: long brand or category landing pages with several sections.

---

## Function 3: Block visibility

**What it is**: individual blocks in shopping experiences can be shown or hidden
via **Rule Builder rules**.

**Examples of rules**:
- Block visible only to logged-in customers
- Block only for certain customer groups
- Show the block only in certain countries
- Time-controlled visibility (start/end date)

**Configuration**:
1. Open the shopping experience in the editor
2. Select the block → open the block settings
3. Under "Sichtbarkeit" (Visibility) → select a Rule Builder rule
4. Choose a rule from the existing rules or create a new one (Einstellungen (Settings) > Regeln (Rules))

---

## Function 4: Custom Forms (user-defined forms)

**What it is**: an alternative to standard contact forms with a fully customisable layout.

**Field types**:
| Type | Description |
|---|---|
| Text | Single-line text field |
| E-Mail | Email address with validation |
| Zahl (Number) | Numeric input |
| Checkbox | Yes/no selection |
| Dropdown | Selection from a list (from entities or fixed values) |
| Textarea | Multi-line text field |

**Configuration per field**:
- Width (full width, half width, etc.)
- Mandatory field (required)
- Placeholder text
- Validation message

**Usage**: Erlebniswelten editor → add the CMS block "Formular" (Form) → choose the Custom Form element.
