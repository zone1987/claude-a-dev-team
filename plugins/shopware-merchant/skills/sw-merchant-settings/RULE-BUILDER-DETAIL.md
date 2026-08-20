# Shopware 6 – Rule Builder (complete reference)

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/regeln

---

## Contents

- [Überblick](#überblick)
- [Allgemeine Informationen einer Regel](#allgemeine-informationen-einer-regel)
- [Bedingungssystem](#bedingungssystem)
- [Operatoren](#operatoren)
- [Bedingungskategorien](#bedingungskategorien)
- [Bedingungen mit optionalem Filter](#bedingungen-mit-optionalem-filter)
- [Zuweisungen (Reiter)](#zuweisungen-reiter)
- [Vorschaumodus (ab Plan Rise)](#vorschaumodus-ab-plan-rise)
- [Regeln teilen (ab v6.7.1.0 + Rise Plan)](#regeln-teilen-ab-v6710-rise-plan)
- [Regeln löschen](#regeln-löschen)
- [Lernressourcen](#lernressourcen)

## Überblick (Overview)

**Path:** Einstellungen (Settings) > Automatisierung (Automation) > Rule Builder

Allows rules to be defined that customise various shop features without programming.

---

## Allgemeine Informationen (General information) of a rule

| Feld (Field) | Beschreibung (Description) |
|---|---|
| Name | Unique rule name |
| Beschreibung | Optional explanation of the function |
| Priorität (Priority) | Order of application (higher value = evaluated earlier) |
| Typ (Type) | Optional, to restrict assignment options |
| Tags | Organisational attributes for search and filtering |

---

## Condition system

### Core components
| Komponente (Component) | Beschreibung |
|---|---|
| Bedingung (Condition) | Parameter to be queried (e.g. delivery country) |
| Operator | Comparison method (e.g. Ist, Ist nicht) |
| Eingabewert (Input value) | Comparison criterion (e.g. Deutschland) |
| UND-Verknüpfung (AND link) | All conditions must be met |
| ODER-Verknüpfung (OR link) | At least one condition must be met |
| Unterbedingungen (Sub-conditions) | Created automatically when the link type changes |

### Creating rules
1. Einstellungen > Automatisierung > Rule Builder
2. "Regel erstellen" (Create rule)
3. Fill in the general information
4. Select at least one condition with an operator
5. Enter the input value
6. Speichern (Save)

---

## Operatoren (Operators)

| Operator | Funktion (Function) |
|---|---|
| Mind. eine (At least one) | At least one value applies |
| Alle (All) | All values apply |
| Gleich (Equal) | Exact match |
| Ungleich (Not equal) | No match |
| Ist eine von (Is one of) | Match with one of several options |
| Ist keine von (Is none of) | No match with any of the options |
| Größer (Greater) | Value greater than input |
| Größer gleich (Greater or equal) | Value ≥ input |
| Kleiner (Less) | Value less than input |
| Kleiner gleich (Less or equal) | Value ≤ input |

---

## Condition categories

### Allgemein (General)
- Triggered by the Admin API
- Date range, always applies
- Language, tax display, sales channel, currency
- Weekday, time period

### Bestellungen (Orders)
- Affiliate code, order status
- Order with document / with sent document
- Order with tag / custom field
- Campaign code, delivery status, payment status
- Created by the administrator

### Kunde (Customer)
- Affiliate code, logged-in customer
- Requested customer group
- Number of completed orders, total value
- Business customer, guest orderer
- Customer salutation, customer age, birthday
- Customer group, customer number
- Shipping address: state, country, postcode, city, street
- Billing address: state, country, postcode, city, street
- Time since first/last login
- Time since last order
- Is active, newsletter recipient
- With differing shipping address
- Default payment method, tag, custom field

### Positionen im Warenkorb (Line items in the cart)
- Number of different line items
- Line item marked as "neu" (new) / in clearance sale
- In dynamic product group / category
- Highlighted / free of shipping costs
- Average rating
- Width, purchase price, release date, weight, height
- Manufacturer, stock, length, tax rate
- Percentage price/list price ratio
- List price, tag, variant/property value
- Available stock, volume, custom field
- Line item count, unit price, subtotal
- Sum of all purchase prices

### Warenkorb (Cart)
- Total quantity of all products (with optional filter)
- Total number of different products (with optional filter)
- Total weight, total sum, total volume
- Sum, shipping costs
- Shipping method used, payment method

### Marketing & Rabattaktionen (Discount promotions)
- Number of discounts
- Discount promotion, discount promotions with promotion code type
- Subtotal of all discounts

---

## Conditions with an optional filter

| Bedingung | Filtermöglichkeit (Filter option) |
|---|---|
| Zwischensumme aller Positionen (Subtotal of all line items) | By category |
| Gesamtanzahl aller Produkte (Total quantity of all products) | By tags |
| Gesamtanzahl unterschiedlicher Produkte (Total number of different products) | By list price status |

---

## Zuweisungen (Assignments) tab

| Bereich (Area) | Verwendung (Usage) |
|---|---|
| Zahlungsmethoden (Payment methods) | Availability rule |
| Versandmethoden (Shipping methods) | Availability rule |
| Versandkosten (Shipping costs) | Calculation rule |
| Promotionen (Promotions) | Availability |
| Rabatte (Discounts) | Calculation rule |
| Erweiterte Preisgestaltung (Advanced pricing) | Price rules |
| Flow-Definition | Flow Builder |
| Sichtbarkeit (Visibility) | Dynamic Access |

---

## Vorschaumodus (Preview mode) (from plan Rise)

- Validates conditions in real time against selected orders
- Points in time can be simulated
- No effect on live data

---

## Sharing rules (from v6.7.1.0 + Rise plan)

### Download
Context menu → **Download** → JSON export with all conditions and operators

### Upload
Einstellungen > Automatisierung > Rule Builder → **Regel hochladen** (Upload rule) → choose file → upload

If references are missing (customers, customer groups, sales channels), they are reassigned automatically.

---

## Deleting rules

Via context menu → **Löschen** (Delete)

> **Limitation:** Assigned rules cannot be deleted.

---

## Learning resources

- Interactive learning path: https://hub.shopware.com/learn/unit/user-rule-builder
