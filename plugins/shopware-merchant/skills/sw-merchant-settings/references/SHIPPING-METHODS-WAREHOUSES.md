# Shopware 6 – Lagerhäuser (Warehouses) – complete reference

Source: https://docs.shopware.com/de/shopware6-de/einstellungen/lagerhaeuser

---

## Overview

**Path:** Einstellungen (Settings) > Handel (Commerce) > Lagerhäuser  
**Available from:** 6.4.19.0  
**Plan:** Commercial — Shopware Beyond

Allows warehouses to be created and grouped into warehouse groups.

---

## Warehouses

### Creation

| Field | Description |
|---|---|
| Lagerhaus-Name (Warehouse name) | Unique label |
| Interne Beschreibung (Internal description) | Additional information (address, product type) |
| Lagerhausgruppen-Zuweisung (Warehouse group assignment) | Dropdown for assigning a group |

### Editing & deletion
- `...` menu → "Bearbeiten" (Edit) or "Löschen" (Delete)
- Alternatively: in the edit form "Lagerhaus löschen" (Delete warehouse)

### Product assignment
In the product under "Lagerbestand & Lieferbarkeit" (Stock & deliverability) → select a warehouse group → detailed stock settings appear.

---

## Warehouse groups

### Creation

| Field | Description |
|---|---|
| Name | Mandatory field |
| Priorität (Priority) | Numeric prioritisation (determines the depletion order) |
| Interne Beschreibung | Additional information |
| Zugewiesene Regel (Assigned rule) | Rule-based activation for orders |

### Adding warehouses
1. Click "Lagerhäuser hinzufügen" (Add warehouses)
2. Select warehouses via checkbox
3. Confirm

### Prioritisation
Double-click the priority column → adjust the value → save with the check-mark button.

### Removing an assignment
- Via the `...` button in the group → "Löschen"
- Or: click the X in the warehouse's group entry

---

## Use cases

- **International delivery optimisation:** regional warehouse groups for local delivery
- **Rule-based availability:** Rule Builder for warehouse activation
- **Prioritised storage:** warehouse order controls stock withdrawal
