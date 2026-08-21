# Social Shopping – Facebook, Instagram, Google Shopping, Pinterest

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/social-shopping  
**Plan**: Shopware Rise (or higher)

## Contents

- [Overview](#overview)
- [Supported platforms](#supported-platforms)
- [Installation](#installation)
- [Setup per platform](#setup-per-platform)
- [Tracking & statistics](#tracking-statistics)
- [Product validation](#product-validation)
- [Feed management](#feed-management)
- [Performance tips](#performance-tips)

## Overview

The **Social Shopping Extension** integrates Shopware 6 with major social commerce platforms.
Products are exported as a feed and conversions are tracked via referral codes.

---

## Supported platforms

| Platform | Mechanism | Feed format |
|---|---|---|
| **Facebook** | XML feed export | RSS/Atom XML |
| **Instagram** | XML feed export | RSS/Atom XML |
| **Google Shopping** | XML feed export | Google Merchant XML |
| **Pinterest** | Metadata (Rich Pins) | No feed upload required |

---

## Installation

1. **Erweiterungen** (Extensions) **> Meine Erweiterungen** (My extensions)
2. Install and activate Social Shopping
3. New channel types appear in the **Verkaufskanäle** (Sales channels) area

---

## Setup per platform

### Facebook & Instagram

**Steps**:
1. **Verkaufskanäle** > add new channel → choose "Facebook" or "Instagram"
2. Name the channel
3. Assign **Storefront und Domain** (Storefront and domain)
4. Choose the **Währung** (Currency)
5. Select **Produktgruppen** (Product groups) – which products get exported
6. Set the **Generierungsintervall** (Generation interval): live or scheduled (daily/hourly)
7. Copy the feed URL from Shopware
8. Enter it in Facebook Business Manager / Catalog Manager

### Google Shopping

**Steps**:
1. New channel → choose "Google Shopping"
2. Perform **domain verification** via Google Merchant Center
3. Assign Google product category IDs (numeric)
4. Enter the feed URL in Google Merchant Center

**Important**: Google product category IDs must be **numeric**
(from the Google taxonomy: https://www.google.com/basepages/producttype/taxonomy-with-ids.de-DE.txt)

### Pinterest

**Mechanism**: No feed upload required – Pinterest reads metadata directly from the storefront.

**Steps**:
1. **Rich Pins validation** via the Pinterest developer tools:
   https://developers.pinterest.com/tools/url-debugger/
2. Verify the shop URL for Pinterest
3. Shopware pulls product data automatically from the storefront HTML

---

## Tracking & statistics

### Referral code in templates
For conversion tracking, every product link must contain the sales channel parameter:

```
{{ socialShoppingSalesChannel.salesChannelId }}
```

Without this parameter: no attribution in the order details.

### Tracking evaluation
- **Customer overview**: the "Einstiegspunkt" (Entry point) column shows which social channel the customer came from
- **Order overview**: the "Einstiegspunkt" column for each order

---

## Product validation

Before the export, Shopware automatically checks data completeness:

| Mandatory field | Description |
|---|---|
| Product name | Present and not empty |
| Description | Present |
| Main image | At least one image |
| Price | Valid price |
| GTIN/EAN | (Recommended for Google Shopping) |

Products with missing data are excluded from the feed.

---

## Feed management

### Generation intervals
| Option | Description |
|---|---|
| Live | The feed is regenerated on every request |
| Hourly | Hourly pre-generation (cache) |
| Daily | Once per day |

### Important notes

- **Deleting a sales channel**: always delete it **before** deactivating the extension!
  (Otherwise orphaned channel configurations remain)
- The feed URL is publicly accessible (no auth needed for the platform import)

---

## Performance tips

- For large catalogues: use scheduled generation (not live)
- Define product groups so that only relevant products are exported
- Enter the feed URL directly in the platform dashboard (do not download/upload manually)
