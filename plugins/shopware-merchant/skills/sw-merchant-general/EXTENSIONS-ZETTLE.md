# Zettle by PayPal – point-of-sale integration

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/zettle

## Overview

**Zettle by PayPal** enables card payments at the physical point of sale (POS) via a
chip card reader device for smartphones and tablets. The integration with Shopware 6 runs
as its **own sales channel type** and synchronises product data between the online shop and POS.

**Important**: Zettle is a **component of PayPal** – not a standalone extension.
No separate installation needed (it comes with PayPal).

---

## Setup

### Prerequisites
- PayPal extension installed and active
- Zettle account: https://zettle.com (a separate account is required)
- Zettle hardware (card reader)

### Setup wizard
1. **Verkaufskanäle** (Sales channels) → add new channel → choose "Zettle"
2. The setup wizard guides you through all configuration steps

---

## Configuration in detail

### Step 1: link the account
1. Generate an API key in the **Zettle admin panel**:
   - Zettle portal: https://my.zettle.com/integrations
   - "Add integration" → copy the API key
2. In the Shopware admin: Zettle channel → enter the API key

### Step 2: channel settings
| Field | Description |
|---|---|
| Channel name | Internal name (e.g. "Market stall Berlin") |
| Shop domain | Domain from which product media are loaded |

### Step 3: product synchronisation
Three options for the initial synchronisation:

| Option | Description |
|---|---|
| **Use Shopware products only** | The Zettle catalogue is replaced by the Shopware products |
| **Replace existing Zettle catalogue** | All Zettle products are replaced by Shopware products |
| **Add Shopware products** | Shopware products are added to the existing Zettle catalogue |

### Step 4: price synchronisation
| Option | Description |
|---|---|
| Synchronise prices incl. VAT | Transmit gross prices to Zettle |
| Synchronise prices excl. VAT | Transmit net prices (configure VAT in Zettle) |
| Manage prices separately in Zettle | No price synchronisation |

---

## Ongoing management

In the Zettle sales channel dashboard:

| Area | Content |
|---|---|
| **Account status** | Connection status to Zettle |
| **Synchronisation history** | Log of all sync operations |
| **Synchronised products** | List of the transferred products |
| **Detailed logs** | Technical sync details and errors |

### Manual synchronisation
Can be triggered manually at any time:
- Synchronise inventory
- Synchronise product images
- Synchronise product details

---

## Limitations

| Limitation | Details |
|---|---|
| Custom Products | Configurable products are synchronised as standard products without options |
| Product descriptions | Maximum **1,024 characters** (longer texts are truncated) |
| Variants | Are created as separate products in Zettle |
| Digital products | Not suitable for POS |

---

## Use cases

- **Merchants with an online shop + market stall**: the same product catalogue for both channels
- **Pop-up store**: temporary bricks-and-mortar sales with online shop products
- **Event sales**: merchandise at events
- **Store + online**: unified inventory management
