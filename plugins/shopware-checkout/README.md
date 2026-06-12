# shopware-checkout

> Der gesamte Kauf-/Bestellprozess: Warenkorb, Zahlung, Versand, Bestellung, Dokumente.

`shopware-checkout` deckt den **kompletten Kauf- und Bestellprozess** ab — von der Warenkorbberechnung bis zum
fertigen Beleg.

**Warenkorb-Pipeline:** Collector (Daten gebündelt laden) → Processor (Preise/Struktur berechnen) → Validator
(prüfen/blockieren), dazu **LineItems** (inkl. verschachtelter Bundles), **Preisberechnung** über die
Calculator-Services, **Rabatte**, **Tax-Provider** und Cart-Manipulation per **App-Script-Facade**.
**Lieferung & Versand:** Delivery-Berechnung und eigene Versandarten. **Zahlung:** der vereinheitlichte
**`AbstractPaymentHandler`** (6.7) und **App-Payment**. **Bestellung:** die **State-Machines** (Order/Transaction/
Delivery) und die Order-Lifecycle-Events. **Belege:** **Dokumente** (Rechnung, Lieferschein, Storno, Gutschrift,
inkl. **ZUGFeRD**) und eigene Dokumenttypen. Plus **Promotions** und **Kunden**(-Kontext). Als konkretes Beispiel
liegt hier auch das **PayPal-PHP-SDK**.

Spezialist **`shopware-checkout`**; Scaffolder **`/sw-payment-handler`**, **`/sw-cart-processor`**,
**`/sw-document-type`**. **Wann nutzen:** für alles rund um Warenkorb, Zahlung, Versand, Bestellstatus und Belege.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-checkout@claude-a-dev-team
```

## Skills (20)

`sw-cart-collector`, `sw-cart-discount`, `sw-cart-facade-script`, `sw-cart-line-item`, `sw-cart-price`, `sw-cart-processor`, `sw-cart-validator`, `sw-customer`, `sw-delivery`, `sw-document`, `sw-document-type`, `sw-nested-line-items`, `sw-order-events`, `sw-order-state-machine`, `sw-payment-app`, `sw-payment-handler`, `sw-paypal-sdk`, `sw-promotion`, `sw-shipping-method`, `sw-tax-provider`

## Agents (1)

- **`shopware-checkout`** — Spezialist für den Shopware-6.7-Checkout: Warenkorb (Collector/Processor/Validator, LineItems, Preise/Rabatte), Tax-Provider, Lieferung/Versandarten, Payment-Handler (6.7 AbstractPaymentHandler) & App-Payment, Order-Stat

## Commands (3)

- **`/sw-cart-processor`** — Scaffold eines Shopware-6 Cart-Collectors + Cart-Processors (Warenkorb-Berechnung) inkl.
- **`/sw-document-type`** — Scaffold eines eigenen Shopware-6 Dokumenttyps (Renderer + Twig-Template + document_type-Migration) inkl.
- **`/sw-payment-handler`** — Scaffold eines Shopware-6.7 Payment-Handlers (AbstractPaymentHandler) inkl.
