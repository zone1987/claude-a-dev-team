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

| Skill | Beschreibung |
|---|---|
| `sw-cart-collector` | Eigener Cart-Collector in Shopware 6: CartDataCollectorInterface, Daten für die Warenkorb-Berechnung vorab laden (collect) und in die CartDataCollection legen |
| `sw-cart-discount` | Rabatte/Zu- und Abschläge im Shopware-6-Warenkorb: Discount-LineItem (type promotion/discount), PercentagePriceCalculator, negative Preise, Verhältnis zu Promotions |
| `sw-cart-facade-script` | Warenkorb per App-Script manipulieren in Shopware 6: Cart-Facade (services.cart) im cart-Hook, Items/Preise/Rabatte hinzufügen ohne PHP-Processor |
| `sw-cart-line-item` | LineItems im Shopware-6-Warenkorb: LineItem erzeugen/hinzufügen (LineItemFactory/CartService), Typen (product/promotion/ custom), Payload, Label/Quantity/Preis, eigener LineItem-Typ |
| `sw-cart-price` | Preisberechnung im Shopware-6-Warenkorb: QuantityPriceCalculator/PercentagePriceCalculator/AbsolutePriceCalculator, QuantityPriceDefinition, CalculatedPrice, Steuer-/Rundungslogik |
| `sw-cart-processor` | Eigener Cart-Processor in Shopware 6: CartProcessorInterface, in die Warenkorb-Berechnungspipeline einklinken (process), Preise/LineItems berechnen, Verhältnis zu Collector |
| `sw-cart-validator` | Eigener Cart-Validator in Shopware 6: CartValidatorInterface, Warenkorb vor Checkout prüfen und Fehler/Blocker (CartError) hinzufügen |
| `sw-customer` | Kunden im Shopware-6-Checkout-Kontext (technisch): customer-Entity, Registrierung/Login (Store-API/AccountService), Kundengruppen, Adressen, SalesChannelContext-Kunde, Events |
| `sw-delivery` | Lieferungen/Versandkosten im Shopware-6-Warenkorb: Delivery/DeliveryCollection, DeliveryProcessor, Versandkosten-Berechnung, DeliveryTime, mehrere Lieferungen |
| `sw-document` | Dokumente in Shopware 6 erzeugen (Rechnung, Lieferschein, Storno, Gutschrift): DocumentGenerator.generate, DocumentGenerateOperation, Rendering, Speicherung, ZUGFeRD/E-Rechnung |
| `sw-document-type` | Eigener Dokumenttyp in Shopware 6: DocumentType-Entity, AbstractDocumentRenderer, Twig-Template + Config, Registrierung |
| `sw-nested-line-items` | Verschachtelte LineItems in Shopware 6 (Bundles/Sets): children-Collection, Preisaggregation über Kinder, Anzeige/Berechnung |
| `sw-order-events` | Auf Bestell-Lebenszyklus in Shopware 6 reagieren: CheckoutOrderPlacedEvent, StateMachineStateChangeEvent, OrderStateMachineStateChangeEvent, order.written; Daten anreichern/Folgeaktionen |
| `sw-order-state-machine` | Order-/Transaction-/Delivery-StateMachine in Shopware 6: Zustände & Übergänge, StateMachineRegistry.transition, eigene States/Transitions, mail/flow bei Statuswechsel |
| `sw-payment-app` | App-basierte Zahlungsart in Shopware 6 (App Payment): Manifest <payment>, pay/finalize/validate/refund/recurring URLs, Signatur, ohne PHP-Handler |
| `sw-payment-handler` | Eigener Payment-Handler in Shopware 6 (6.7 AbstractPaymentHandler): pay()/finalize(), synchron/asynchron/vorbereitet, refund, payment_method-Entity, PaymentException |
| `sw-paypal-sdk` | PHP-SDK für die PayPal REST APIs (shopware/paypal-sdk). Gateways, OAuth-Kontexte, Structs |
| `sw-promotion` | Promotions/Aktionen in Shopware 6 technisch: promotion-Entity (Rabattarten, Codes, Bedingungen/Rules, discount scopes), PromotionProcessor, eigene Rabatt-Logik |
| `sw-shipping-method` | Eigene Versandart in Shopware 6 programmatisch bereitstellen: shipping_method-Entity (Migration), Verfügbarkeitsregel, Preismatrix, Tracking-URL, Aktivierung je SalesChannel |
| `sw-tax-provider` | Eigener Tax-Provider in Shopware 6 (externe Steuerberechnung): AbstractTaxProvider, provide(), TaxProviderResult, Registrierung, App-Mode |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-checkout` | Spezialist für den Shopware-6.7-Checkout: Warenkorb (Collector/Processor/Validator, LineItems, Preise/Rabatte), Tax-Provider, Lieferung/Versandarten, Payment-Handler (6.7 AbstractPaymentHandler) & App-Payment, Order-StateMachine & -Events,  |

## Commands (3)

| Command | Beschreibung |
|---|---|
| `/sw-cart-processor` | Scaffold eines Shopware-6 Cart-Collectors + Cart-Processors (Warenkorb-Berechnung) inkl |
| `/sw-document-type` | Scaffold eines eigenen Shopware-6 Dokumenttyps (Renderer + Twig-Template + document_type-Migration) inkl |
| `/sw-payment-handler` | Scaffold eines Shopware-6.7 Payment-Handlers (AbstractPaymentHandler) inkl |
