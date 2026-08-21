# Shopware Subscriptions — developer reference

## Contents

- [Core concepts](#core-concepts)
- [Checkout processes](#checkout-processes)
- [Extending cart processors and collectors](#extending-cart-processors-and-collectors)
- [Template scoping](#template-scoping)
- [Extensibility pattern (recommendation)](#extensibility-pattern-recommendation)
- [Design decisions (background)](#design-decisions-background)

## Core concepts

### Subscription Plans
A set of rules (interval, product). Several intervals per plan are possible.
Managed in the Shopware Administration.

### Subscription Intervals
The time span between delivery cycles:

| Type       | Description                                    | Implementation   |
|------------|------------------------------------------------|------------------|
| Relative   | Based on the previous interval (e.g. +1M)      | PHP `DateInterval`|
| Absolute   | Fixed date (e.g. the 1st of every month)       | Cron expression  |

Absolute intervals can have a relative portion (e.g. every 12 weeks, but only on Fridays).

### Subscription Cart
Contains only subscription products of one plan+interval combination.
Calculated with the subscription cart calculator (a subset of cart processors/collectors).
Link between main cart ↔ subscription cart via the `subscription_cart` table.

### Subscription Context
Sales channel context with the `subscription` extension:
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

## Checkout processes

### Separate subscription checkout

Every subscription product is checked out individually (express-checkout style):
- A new subscription cart with ONLY the subscription product
- A new subscription context (derived from the main context)
- The main cart stays unchanged

**Headless request scoping:**
```
Header: sw-subscription-plan: <plan-id>
Header: sw-subscription-interval: <interval-id>
```

**Storefront URL parameter:** `/subscription/checkout/cart/{subscriptionToken}`

**Adding a subscription product (Store API):**
```sh
POST /store-api/subscription/checkout/cart/line-item
{
  "lineItems": [{"id": "<product-id>"}],
  "subscription-plan-option": "<plan-id>",
  "subscription-plan-option-<plan-id>-interval": "<interval-id>"
}
```

**Events:** all events in the subscription checkout carry the `subscription.` prefix:
```php
// Normal:
'subscription.' . CheckoutOrderPlacedCriteriaEvent::class => 'handler'
```
Full list: `Subscription/Framework/Event/SubscriptionEventRegistry.php`

### Mixed cart checkout (from Shopware 6.7.4.0)

Subscription products and one-off purchase products in the same cart:
- Subscription products are normal line items with a subscription payload
- Per plan+interval combination: its own managed subscription cart (derived)
- Managed carts: `subscriptionManagedCarts` extension on the main cart

**Subscription metadata in the line item payload:**
```json
{"subscriptionPlan": "<plan-id>", "subscriptionInterval": "<interval-id>"}
```

**Adding a product as a subscription (Store API):**
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

**Reading managed carts from the cart:**
```twig
{% set managedCarts = page.cart.extensions.subscriptionManagedCarts %}
{# Key: "<plan-id>-<interval-id>" #}
```

## Extending cart processors and collectors

For the separate checkout: `subscription.cart.processor` / `subscription.cart.collector`
For the mixed cart: the same tags + `shopware.cart.processor` / `shopware.cart.collector`

Differentiating in code:
```php
// Is it a subscription cart?
$isSubscription = $salesChannelContext->hasExtension('subscription');
// Is it a managed (mixed) cart?
$isManaged = $salesChannelContext->getExtension('subscription')?->isManaged();
```

**Important with the mixed cart:** do NOT add line items only to the subscription cart.
Always add them to the main cart as well. For subscription-only items:
subscribe to `SubscriptionOrderLineItemRestoredEvent`.

### Creating a subscription line item in PHP (processor/collector)

```php
$planId = $salesChannelContext->getExtension('subscription')->getPlan()->getId();
$intervalId = $salesChannelContext->getExtension('subscription')->getInterval()->getId();

// The composite ID prevents merging with existing line items
$lineItemId = sprintf('%s-%s-%s', $productId, $planId, $intervalId);
$lineItem = new LineItem($lineItemId, LineItem::PRODUCT_LINE_ITEM_TYPE, $productId);
$lineItem->setPayloadValue('subscriptionPlan', $planId);
$lineItem->setPayloadValue('subscriptionInterval', $intervalId);
$cart->add($lineItem);
```

## Template scoping

Prevents standard storefront customizations from being visible in the subscription checkout
(e.g. express checkout buttons that do not support subscriptions).

**Scopes:**
- `subscription` — separate subscription checkout
- `mixed-subscription` — mixed cart checkout

**Template with a scope declaration:**
```twig
{% sw_extends {
    template: '@Storefront/storefront/base.html.twig',
    scopes: ['default', 'subscription']
} %}
```

**Affected storefront pages (both scopes):**
- `frontend.checkout.cart.page`
- `frontend.checkout.confirm.page`
- `frontend.checkout.register.page`
- `frontend.account.edit-order.page`
- `frontend.account.login.page`
- `frontend.account.register.page`
- `frontend.cart.offcanvas` (mixed-subscription only)

Customizable route list via the parameter: `subscription.routes.mixed-storefront-scope`

## Extensibility pattern (recommendation)

The decorator pattern for subscription services:

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

## Design decisions (background)

Subscriptions are deliberately designed in isolation so as not to affect existing extensions:
- Promotions are excluded from subscription carts (complexity with follow-up orders)
- Template scopes prevent incompatible UI elements
- Scoped events enable a targeted opt-in

B2B employee integration: see `sw-b2b-components-employee-management` (subscription integration).
