# Shopware Commercial plugin — developer reference

## Overview

The Shopware 6 Commercial plugin is a group of nested sub-bundles that provide extended
functionality for B2B and enterprise shop operators. Among other things it covers:

- Advanced Search (Elasticsearch/OpenSearch based)
- B2B Components (Employee Management, Quotes, Order Approval, Shopping Lists, Individual Pricing, Organization Unit)
- Subscriptions (subscription products)
- B2B Suite (legacy, supported up to SW 6.8)
- Migration Assistant (data migration from SW5, SW6, Magento)

## Plugin structure

The Commercial plugin is built as a group of sub-bundles (concept: Shopware plugins).
Every feature is a self-contained bundle. Merchant configuration enables/disables
features according to the license.

## Licensing

On installation the plugin tries to fetch the license key via the logged-in Shopware account.
Without a key the plugin stays installed, but all features are disabled.

```bash
# Update the license key
bin/console commercial:license:update

# Check the license status
bin/console commercial:license:info
```

## Enabling bundles selectively

Since Commercial 6.6.10.0 individual bundles can be controlled via the environment variable:

```env
SHOPWARE_COMMERCIAL_ENABLED_BUNDLES=CustomPricing,Subscription
```

Determine all available bundle names:

```bash
./bin/console debug:container --parameter kernel.bundles --format=json
```

## Plans

| Plan    | Features (excerpt)                         |
|---------|--------------------------------------------|
| Rise    | Base features                              |
| Evolve  | Advanced Search, B2B Components            |
| Beyond  | Full Commercial suite                      |

## Installation

No special handling required — identical to a standard plugin installation:
`bin/console plugin:install --activate SwagCommercial`

## Important for developers

- Every Commercial bundle can be an optional dependency in a plugin extension (conditional loading).
- When developing against Commercial features: always check whether the respective bundle is licensed and active.
- Merchant perspective (admin UI, merchant docs): see `shopware-merchant`.
