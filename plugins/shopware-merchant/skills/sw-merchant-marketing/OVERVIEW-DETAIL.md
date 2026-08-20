# Marketing – overview

**Path:** Admin > Marketing

## Description

The Marketing area in the Shopware 6 administration offers all the tools for running discount promotions and for managing newsletter subscribers.

> **Note:** the Marketing area is part of the Shopware administration and is available from version 6.0.0.

## Included areas

### 1. Rabatte & Aktionen (Discounts & promotions)

Path: Admin > Marketing > **Rabatte & Aktionen**

Allows discount promotions (promotions) to be created for sales channels. Supports:

- **Aktionscodes** (Promotion codes — none, fixed or individual codes)
- Conditions via the Rule Builder
- Various discount types (absolute, percentage, fixed price)
- Time limits
- Usage limits (in total and per customer)

**Details:** see `sw-merchant-marketing-promotions` and `sw-merchant-marketing-codes`

### 2. Newsletter Empfänger (Newsletter recipients)

Path: Admin > Marketing > **Newsletter Empfänger**

Management of all customers who have signed up for the newsletter. Supports:

- Status management (**Warten auf Aktivierung** – waiting for activation, **Sofort Aktiv** – directly active, **Aktiv** – active, **Warten auf Löschung** – waiting for deletion)
- Filtering by status, language and sales channel
- Editing recipient data (address, language, email, tags)

**Details:** see `sw-merchant-marketing-newsletter`

## Related areas

| Area | Path | Relevance |
|---------|------|----------|
| Rule Builder | **Einstellungen > Automatisierung** (Settings > Automation) **> Rule Builder** | Conditions for promotions |
| **Verkaufskanäle** (Sales channels) | Verkaufskanäle | Assign promotions per channel |
| Flow Builder | Einstellungen > Automatisierung > Flow Builder | Automation based on promotions |

## Sub-skills

| Skill | Topic |
|-------|-------|
| `sw-merchant-marketing-promotions` | Creating and configuring Rabatte & Aktionen |
| `sw-merchant-marketing-codes` | Aktionscodes: fixed, individual, examples |
| `sw-merchant-marketing-newsletter` | Managing newsletter recipients |
| `sw-merchant-marketing-rule-builder` | Rule Builder for conditions |
