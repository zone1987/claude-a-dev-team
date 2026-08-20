# shopware-checkout

> The entire purchase and order process: cart, payment, shipping, order, documents.

`shopware-checkout` covers the **complete purchase and order process** — from cart calculation to the finished
document.

**Cart pipeline:** collector (load data in bulk) → processor (calculate prices/structure) → validator
(check/block), plus **line items** (including nested bundles), **price calculation** through the calculator
services, **discounts**, **tax providers** and cart manipulation via the **app script facade**.
**Delivery and shipping:** delivery calculation and custom shipping methods. **Payment:** the unified
**`AbstractPaymentHandler`** (6.7) and **app payment**. **Order:** the **state machines**
(order/transaction/delivery) and the order lifecycle events. **Documents:** **documents** (invoice, delivery note,
cancellation, credit note, including **ZUGFeRD**) and custom document types. Plus **promotions** and
**customers** (context). As a concrete example, the **PayPal PHP SDK** also lives here.

Specialist **`shopware-checkout`**; scaffolders **`/sw-payment-handler`**, **`/sw-cart-processor`**,
**`/sw-document-type`**. **When to use:** for everything around cart, payment, shipping, order state and
documents.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official
sources and embedded; depth sits in flat reference files beside each SKILL.md, loaded on demand.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-checkout@claude-a-dev-team
```

## Skills (4)

| Skill | Description |
|---|---|
| `sw-cart` | Shopware cart: the processor pipeline, collectors, validators, price calculation, line items, discounts, the cart facade. Use when changing Shopware cart behaviour |
| `sw-document` | Shopware documents: document generation, custom document types, ZUGFeRD, and the customer entity in checkout. Use when the request names a Shopware document type or invoice |
| `sw-fulfilment` | Shopware fulfilment: deliveries, shipping methods, the order state machine and its transitions, order events. Use when the request names a Shopware shipping method or order state |
| `sw-payment` | Shopware payment: the 6.7 AbstractPaymentHandler, app payment, the PayPal SDK, tax providers. Use when the request names a Shopware payment handler or tax provider |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-checkout` | Specialist for the Shopware 6.7 checkout: cart (collector/processor/validator, line items, prices/discounts), tax providers, delivery/shipping methods, payment handlers (6.7 AbstractPaymentHandler) and app payment, order state machine and events,  |

## Commands (3)

| Command | Description |
|---|---|
| `/sw-cart-processor` | Scaffolds a Shopware 6 cart collector + cart processor (cart calculation) incl |
| `/sw-document-type` | Scaffolds a custom Shopware 6 document type (renderer + Twig template + document_type migration) incl |
| `/sw-payment-handler` | Scaffolds a Shopware 6.7 payment handler (AbstractPaymentHandler) incl |
