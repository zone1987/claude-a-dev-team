# Dashboard

**Source**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/dashboard  
**Applies from**: Shopware 6.4.8.0 (for older versions there is separate documentation under 6.0.0–6.4.7.0)

## Overview

The dashboard is the **start page after logging in** to the Shopware 6 administration.
It provides a first overview of current shop topics and key figures.

---

## Components of the dashboard

### Statistics widgets

By default the dashboard shows **two statistics panels**:

#### 1. Bestellungen (Orders) – count trend
- Shows the number of incoming orders in the selected period
- Trend comparison: current period vs. previous period

#### 2. Umsatz (Revenue) – development
- Shows the revenue (gross) in the selected period
- Trend comparison: current period vs. previous period

### Period selection

Both widgets have a **dropdown menu** for selecting the period:

| Option | Description |
|---|---|
| Seit gestern (Since yesterday) | All orders from midnight of the previous day |
| Letzte 7 Tage (Last 7 days) | Rolling 7-day window |
| Letzte 30 Tage (Last 30 days) | Rolling 30-day window |
| Diesen Monat (This month) | Current calendar month |
| Letzten Monat (Last month) | The entire previous month |

> "Seit gestern" covers all orders from midnight (00:00) of the previous day.

---

### Help & feedback area

- **Help links**: direct access to the Shopware documentation
- **Feedback button**: forwards you to the issue tracker for direct feedback to Shopware

---

## Shopware Analytics vs. the standard dashboard

The standard dashboard shows simple core figures. For extended reports:
- Install the **Shopware Analytics Extension** (from Dashboard > Analytics)
- Provides: revenue, conversion rate, page views, customer segments, payment methods and much more
- Available for all plans (Rise, Evolve, Beyond)

→ See `../../../sw-merchant-extensions/references/deep/shopware-analytics.md`

---

## Tips

- The dashboard cannot be customised individually (no widget drag and drop in the standard version)
- For deeper analyses: the Shopware Analytics Extension or external BI tools via the API
- Quick access to the dashboard: always via the Shopware logo at the top left of the navigation
