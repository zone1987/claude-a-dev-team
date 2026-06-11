---
title: Webhook Registration and Events
impact: HIGH
impactDescription: Webhooks are the primary mechanism for apps to react to shop events
tags: webhook, events, entity-written
---

## Webhook Registration and Events

Webhooks allow apps to receive HTTP notifications when events occur in the Shopware shop. They are registered in the `<webhooks>` section of the manifest.xml and must point to endpoints on your app server.

### Webhook XML Registration

```xml
<webhooks>
    <webhook name="orderCompleted" url="https://my-app.example.com/webhooks/order-completed" event="checkout.order.placed"/>
    <webhook name="productUpdated" url="https://my-app.example.com/webhooks/product-updated" event="product.written"/>
    <webhook name="customerRegistered" url="https://my-app.example.com/webhooks/customer-registered" event="checkout.customer.register"/>
</webhooks>
```

### Important Rules

- Webhook `name` attributes **must be unique** across the entire manifest.
- The `url` must be an HTTPS endpoint (except in development).
- The `event` must be a valid Shopware event name.

**Incorrect (duplicate webhook names):**

```xml
<webhooks>
    <webhook name="myHook" url="https://example.com/hook1" event="product.written"/>
    <webhook name="myHook" url="https://example.com/hook2" event="order.written"/>
</webhooks>
```

**Correct (unique webhook names):**

```xml
<webhooks>
    <webhook name="productWritten" url="https://example.com/hook1" event="product.written"/>
    <webhook name="orderWritten" url="https://example.com/hook2" event="order.written"/>
</webhooks>
```

### onlyLiveVersion Attribute (since 6.5.7.0)

For entity-written events, you can filter to only receive webhooks for the live version of entities (ignoring draft/version changes):

```xml
<webhook name="productChanged" url="https://example.com/product" event="product.written" onlyLiveVersion="true"/>
```

This is especially useful to avoid duplicate notifications during order processes where entities are written in versioned contexts first.

### Payload Structure

Every webhook POST request contains a JSON body with this structure:

```json
{
    "source": {
        "url": "https://my-shop.example.com",
        "appVersion": "1.0.0",
        "shopId": "dgrH7nLDnh3..."
    },
    "data": {
        "payload": [
            {
                "entity": "product",
                "operation": "update",
                "primaryKey": "7b04ebe416db4bebb4a4a3e93ebbf58e",
                "updatedFields": ["price", "stock"]
            }
        ],
        "event": "product.written"
    },
    "timestamp": 1694000000
}
```

### Entity Events Contain Only IDs

Entity-written events (`*.written`, `*.deleted`) contain **only entity IDs and updated field names**, not the full entity data. To get the full data, you must make a follow-up API call using the Admin API with the entity ID.

### Key Events Reference

| Event | Trigger |
|-------|---------|
| `product.written` | Product created or updated |
| `product.deleted` | Product deleted |
| `order.written` | Order created or updated |
| `checkout.order.placed` | New order placed via checkout |
| `checkout.customer.register` | New customer registration |
| `customer.written` | Customer created or updated |
| `category.written` | Category created or updated |
| `state_enter.order.state.cancelled` | Order enters cancelled state |
| `state_enter.order.state.completed` | Order enters completed state |
| `state_enter.order_delivery.state.shipped` | Delivery enters shipped state |
| `state_enter.order_transaction.state.paid` | Payment enters paid state |
| `state_enter.order_transaction.state.refunded` | Payment enters refunded state |

### State Machine Events

State machine events follow the pattern `state_enter.{entity}.state.{stateName}` and `state_leave.{entity}.state.{stateName}`. They are triggered when orders, deliveries, or transactions transition between states:

```xml
<webhooks>
    <webhook name="orderPaid" url="https://example.com/order-paid" event="state_enter.order_transaction.state.paid"/>
    <webhook name="orderShipped" url="https://example.com/order-shipped" event="state_enter.order_delivery.state.shipped"/>
    <webhook name="orderCancelled" url="https://example.com/order-cancelled" event="state_enter.order.state.cancelled"/>
</webhooks>
```
