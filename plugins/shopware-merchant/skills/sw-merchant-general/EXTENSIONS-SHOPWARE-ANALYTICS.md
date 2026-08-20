# Shopware Analytics – extended reporting

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/shopware-analytics  
**Path in the admin**: Dashboard > Analytics  
**Available for**: All plans (Rise, Evolve, Beyond)

## Contents

- [Overview](#overview)
- [Versions](#versions)
- [Installation & activation](#installation-activation)
- [Configuration options](#configuration-options)
- [Backend metrics](#backend-metrics)
- [Storefront metrics (requires event tracking)](#storefront-metrics-requires-event-tracking)
- [Data protection & performance note](#data-protection-performance-note)
- [Troubleshooting](#troubleshooting)

## Overview

**Shopware Analytics** extends the standard dashboard statistics with detailed reporting.
The data processing happens on your own system – no third-party tracking.

---

## Versions

| Shopware version | Analytics version |
|---|---|
| Shopware 6.5 | App version 1.4.x |
| Shopware 6.6+ | App version 2.4.x |

---

## Installation & activation

1. **Erweiterungen** (Extensions) **> Meine Erweiterungen** (My extensions) or **Erweiterungen > Store**
2. Search for "Shopware Analytics" → install + activate
3. Access: **Dashboard > Analytics**

---

## Configuration options

### Period filter
- Predefined periods: today, yesterday, the last 7/30 days, this/last month, this/last year
- **Custom period**: choose the start and end date freely

### Filter dimensions
| Filter | Possible values |
|---|---|
| Verkaufskanal (Sales channel) | All channels or a specific channel |
| Country | The customer country of the order |
| Kundengruppe (Customer group) | For example B2C, B2B |
| Order status | Offen (Open), In Bearbeitung (In progress), Abgeschlossen (Completed), Storniert (Cancelled) |
| Payment status | Offen (Open), Bezahlt (Paid), Teilweise bezahlt (Partially paid) |

---

## Backend metrics

### Revenue & orders
| Key figure | Description |
|---|---|
| Total revenue | Gross revenue in the selected period |
| Number of orders | The total number of orders |
| Average order value | Revenue / number of orders |

### Payment methods
- Which payment methods are used, and how often?
- The revenue share per payment method

### Customer acquisition
- New vs. returning customers
- Customer development over time

### Discounts & vouchers
- The total discount volume
- Frequently used voucher codes

### Revenue by dimension
- By manufacturer
- By country / region
- By product (top sellers)
- By shipping method

---

## Storefront metrics (requires event tracking)

> **Prerequisite**: Tracking has to be active and customers have to consent (GDPR-compliant)

| Key figure | Description |
|---|---|
| Page impressions | Total page views |
| Unique visitors | Distinct visitors |
| Conversion rate | Visitors → buyers (%) |
| Customer journey | The path from the first visit to the order |

---

## Data protection & performance note

- Data processing: **on your own server** (no third parties)
- Users have to consent to the data processing
- **Important**: "Large data volumes can affect the system performance" – on large shops
  run the analysis outside the peak times

---

## Troubleshooting

| Problem | Solution |
|---|---|
| No data after a URL change | Run `bin/console app:url-change:resolve` |
| The tracking activation fails | Check whether external communication is blocked (firewall) |
| The data is out of date | Check the message queue (`php bin/console messenger:consume`) |
| The reports load slowly | Restrict the period or run the analysis off-peak |
