# Dynamic Access – rule-based content access control

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/dynamicaccess  
**Plan**: Shopware Evolve (or higher)  
**Available from**: Shopware 6.4.6.0 (Rule Builder integration)

## Contents

- [Overview](#overview)
- [Areas of application](#areas-of-application)
- [Creating rules (Rule Builder)](#creating-rules-rule-builder)
- [Important notes & pitfalls](#important-notes-pitfalls)
- [Bulk assignment via Import/Export](#bulk-assignment-via-importexport)
- [Distinction from other access mechanisms](#distinction-from-other-access-mechanisms)

## Overview

**Dynamic Access** makes it possible to **conditionally show or hide** shop content
(categories, products, variants) on the basis of Rule Builder rules. Content only appears in
the storefront if one of the defined rules applies.

---

## Areas of application

### 1. Hiding categories

**Configuration**:
1. **Katalog** (Catalogue) **> Kategorien** (Categories) → open the category
2. **Allgemein** (General) tab → "Sichtbarkeit" (Visibility) section
3. Under "Dynamic Access Rules" → add rules

**Behaviour**:
- The category is only shown in the storefront if **at least one** of the rules applies
- No rules set = the category is always visible (default)

> **Note**: Hidden categories do **not** automatically hide the products they contain.
> Products can still be found via the search – so set rules at product level as well.

### 2. Hiding products

**Configuration**:
1. **Katalog** (Catalogue) **> Produkte** (Products) → open the product
2. **Allgemein** (General) tab → "Sichtbarkeit" (Visibility) section
3. Under "Dynamic Access Rules" → add rules

**Behaviour**:
- The product is only shown if at least one rule applies
- Invisible products are also **not searchable**

### 3. Hiding variants

**Configuration**: At variant level (inside the product, Varianten (Variants) tab)

**Special feature**: Variants are not hidden directly. Instead:
- The variant is **not selectable** on the product detail page (greyed out)
- The product itself remains visible

---

## Creating rules (Rule Builder)

### Typical rules for Dynamic Access

| Rule | Use case |
|---|---|
| Kundengruppe (Customer group) = "B2B" | Visible only for B2B customers |
| The customer is logged in | Only for registered customers |
| Country = "DE" | Visible only in Germany |
| Date between [start] and [end] | Seasonal products |
| The cart contains product X | Cross-selling logic |

Creating rules: **Einstellungen** (Settings) **> Regeln** (Rules) **> Neue Regel** (New rule)

---

## Important notes & pitfalls

### Products in hidden categories
- If a category is hidden via Dynamic Access, the products it contains
  remain discoverable via the **search**
- **Solution**: Apply the same rules at product level as well (or a bulk assignment)

### Mutually exclusive rules
- Rules should not be configured in such a way that the content is **never** shown
- Example: rule A = "Country DE" AND rule B = "Country FR" with an AND link → never visible
- Use an OR link or check the rule logic

### A cart containing a hidden product
- If a product was added to the cart and is hidden via Dynamic Access afterwards,
  it **blocks the checkout**
- The customer has to remove the product from the cart

---

## Bulk assignment via Import/Export

For large catalogues: assign rules in bulk via the **Import/Export** area:
1. Open **Einstellungen** (Settings) **> Import/Export**
2. Run a product export (CSV)
3. Fill in the Dynamic Access columns in the CSV
4. Import it

---

## Distinction from other access mechanisms

| Mechanism | Description |
|---|---|
| Dynamic Access | Rule-based visibility (plan: Evolve+) |
| Customer group visibility | Standard: configure products/categories for customer groups |
| Shopware Login Required | Lock the entire shop behind a login (Einstellungen > Benutzer & Rechte (Users & permissions)) |
