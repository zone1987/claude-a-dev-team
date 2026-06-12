# shopware-checkout

**Wofür:** Checkout: Cart-Pipeline (Collector/Processor/Validator), LineItems, Preise/Rabatte/Tax, Payment-Handler (6.7) & App-Payment, Shipping, Order-StateMachine, Dokumente (inkl. ZUGFeRD), Promotions, Kunden.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install shopware-checkout@claude-a-dev-team
```

## Skills (20)

`sw-cart-collector`, `sw-cart-discount`, `sw-cart-facade-script`, `sw-cart-line-item`, `sw-cart-price`, `sw-cart-processor`, `sw-cart-validator`, `sw-customer`, `sw-delivery`, `sw-document`, `sw-document-type`, `sw-nested-line-items`, `sw-order-events`, `sw-order-state-machine`, `sw-payment-app`, `sw-payment-handler`, `sw-paypal-sdk`, `sw-promotion`, `sw-shipping-method`, `sw-tax-provider`

## Agents (1)

- **`shopware-checkout`** — Spezialist für den Shopware-6.7-Checkout: Warenkorb (Collector/Processor/Validator, LineItems, Preise/Rabatte), Tax-Provider, Lieferung/Versandarten, Payment-Handler (6.7 AbstractPaymentHandler) & App

## Commands (3)

- **`/sw-cart-processor`** — Scaffold eines Shopware-6 Cart-Collectors + Cart-Processors (Warenkorb-Berechnung) inkl.
- **`/sw-document-type`** — Scaffold eines eigenen Shopware-6 Dokumenttyps (Renderer + Twig-Template + document_type-Migration) inkl.
- **`/sw-payment-handler`** — Scaffold eines Shopware-6.7 Payment-Handlers (AbstractPaymentHandler) inkl.
