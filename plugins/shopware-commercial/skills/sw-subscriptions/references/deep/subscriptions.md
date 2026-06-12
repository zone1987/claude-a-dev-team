# Shopware Subscriptions — Entwickler-Referenz

## Kernkonzepte

### Subscription Plans
Set von Regeln (Interval, Produkt). Mehrere Intervals pro Plan moeglich.
Verwaltung in der Shopware Administration.

### Subscription Intervals
Zeitabstand zwischen Lieferzyklen:

| Typ        | Beschreibung                                   | Implementierung  |
|------------|------------------------------------------------|------------------|
| Relativ    | Basierend auf vorherigem Interval (z.B. +1M)   | PHP `DateInterval`|
| Absolut    | Fester Termin (z.B. jeder 1. des Monats)       | Cron-Ausdruck    |

Absolut-Intervals koennen relativen Anteil haben (z.B. alle 12 Wochen, aber nur freitags).

### Subscription Cart
Enthaelt nur Subscription-Produkte eines Plan+Interval-Kombination.
Wird mit Subscription-Cart-Calculator berechnet (Subset von Cart-Processors/Collectors).
Verknuepfung Main-Cart ↔ Subscription-Cart via `subscription_cart` Tabelle.

### Subscription Context
Sales-Channel-Context mit Extension `subscription`:
```json
{
  "token": "<subscription-context-token>",
  "extensions": {
    "subscription": {
      "mainToken": "<main-context-token>",
      "subscriptionToken": "<subscription-context-token>",
      "managed": true,
      "plan": {},
      "interval": {}
    }
  }
}
```

## Checkout-Prozesse

### Separate Subscription Checkout

Jedes Subscription-Produkt wird einzeln ausgecheckt (Express-Checkout-artig):
- Neuer Subscription-Cart mit NUR dem Subscription-Produkt
- Neuer Subscription-Context (abgeleitet vom Main-Context)
- Main-Cart bleibt unveraendert

**Headless Request Scoping:**
```
Header: sw-subscription-plan: <plan-id>
Header: sw-subscription-interval: <interval-id>
```

**Storefront URL-Parameter:** `/subscription/checkout/cart/{subscriptionToken}`

**Subscription-Produkt hinzufuegen (Store API):**
```sh
POST /store-api/subscription/checkout/cart/line-item
{
  "lineItems": [{"id": "<product-id>"}],
  "subscription-plan-option": "<plan-id>",
  "subscription-plan-option-<plan-id>-interval": "<interval-id>"
}
```

**Events:** Alle Events im Subscription-Checkout haben `subscription.`-Prefix:
```php
// Normal:
'subscription.' . CheckoutOrderPlacedCriteriaEvent::class => 'handler'
```
Vollstaendige Liste: `Subscription/Framework/Event/SubscriptionEventRegistry.php`

### Mixed Cart Checkout (ab Shopware 6.7.4.0)

Subscription-Produkte und Einmalkauf-Produkte im gleichen Warenkorb:
- Subscription-Produkte sind normale Line-Items mit Subscription-Payload
- Pro Plan+Interval-Kombination: eigener verwalteter Subscription-Cart (abgeleitet)
- Verwaltete Carts: `subscriptionManagedCarts` Extension am Main-Cart

**Subscription-Metadaten in Line-Item-Payload:**
```json
{"subscriptionPlan": "<plan-id>", "subscriptionInterval": "<interval-id>"}
```

**Produkt als Subscription hinzufuegen (Store API):**
```sh
POST /store-api/checkout/cart/line-item
{
  "lineItems": [{
    "id": "<product-id>",
    "subscriptionPlan": "<plan-id>",
    "subscriptionInterval": "<interval-id>"
  }]
}
```

**Managed Carts aus dem Cart lesen:**
```twig
{% set managedCarts = page.cart.extensions.subscriptionManagedCarts %}
{# Key: "<plan-id>-<interval-id>" #}
```

## Cart Processors und Collectors erweitern

Fuer Separate Checkout: `subscription.cart.processor` / `subscription.cart.collector`
Fuer Mixed Cart: Gleiche Tags + `shopware.cart.processor` / `shopware.cart.collector`

Differenzierung im Code:
```php
// Ist es ein Subscription-Cart?
$isSubscription = $salesChannelContext->hasExtension('subscription');
// Ist es ein managed (mixed) Cart?
$isManaged = $salesChannelContext->getExtension('subscription')?->isManaged();
```

**Wichtig beim Mixed Cart:** Line-Items NICHT nur zum Subscription-Cart hinzufuegen.
Immer auch zum Main-Cart hinzufuegen. Fuer Subscription-only-Items:
`SubscriptionOrderLineItemRestoredEvent` subscriben.

### Subscription Line-Item im PHP erstellen (Processor/Collector)

```php
$planId = $salesChannelContext->getExtension('subscription')->getPlan()->getId();
$intervalId = $salesChannelContext->getExtension('subscription')->getInterval()->getId();

// Composite ID verhindert Merging mit existierenden Line-Items
$lineItemId = sprintf('%s-%s-%s', $productId, $planId, $intervalId);
$lineItem = new LineItem($lineItemId, LineItem::PRODUCT_LINE_ITEM_TYPE, $productId);
$lineItem->setPayloadValue('subscriptionPlan', $planId);
$lineItem->setPayloadValue('subscriptionInterval', $intervalId);
$cart->add($lineItem);
```

## Template Scoping

Verhindert, dass Standard-Storefront-Anpassungen im Subscription-Checkout sichtbar sind
(z.B. Express-Checkout-Buttons, die keine Abonnements unterstuetzen).

**Scopes:**
- `subscription` — Separater Subscription-Checkout
- `mixed-subscription` — Mixed Cart Checkout

**Template mit Scope-Deklaration:**
```twig
{% sw_extends {
    template: '@Storefront/storefront/base.html.twig',
    scopes: ['default', 'subscription']
} %}
```

**Betroffene Storefront-Seiten (beide Scopes):**
- `frontend.checkout.cart.page`
- `frontend.checkout.confirm.page`
- `frontend.checkout.register.page`
- `frontend.account.edit-order.page`
- `frontend.account.login.page`
- `frontend.account.register.page`
- `frontend.cart.offcanvas` (nur mixed-subscription)

Anpassbare Route-Liste via Parameter: `subscription.routes.mixed-storefront-scope`

## Extensibility-Pattern (Empfehlung)

Decorator-Pattern fuer Subscription-Services:

```php
class CustomSubscriptionServiceDecorator extends AbstractSubscriptionService
{
    public function __construct(
        private readonly AbstractSubscriptionService $decorated,
        private readonly CustomLogicService $customService
    ) {}

    public function getDecorated(): AbstractService { return $this->decorated; }

    public function someMethod(SalesChannelContext $context): void
    {
        $this->customService->doSomething($context);
        $this->decorated->someMethod($context);
    }
}
```

## Design-Entscheidungen (Hintergrund)

Subscriptions sind bewusst isoliert konzipiert, um bestehende Extensions nicht zu beeinflussen:
- Promotions werden aus Subscription-Carts ausgeschlossen (Komplexitaet bei Folge-Orders)
- Template Scopes verhindern inkompatible UI-Elemente
- Scoped Events ermöglichen gezieltes Opt-in

B2B Employee Integration: siehe `sw-b2b-components-employee-management` (Subscription-Integration).
