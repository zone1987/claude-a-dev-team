# Shopware 6 — Webhooks

Shopware can send business events to external URLs — primarily the **app system** (manifest `<webhooks>`), but also
programmatically through the `webhook` entity.

```xml
<!-- App manifest -->
<webhooks>
    <webhook name="order-placed" url="https://app.example.com/hook/order" event="checkout.order.placed"/>
</webhooks>
```

- The payload is **HMAC-signed** with the app secret (header `shopware-shop-signature`) — verify it on the receiving side.
- Delivery is asynchronous with retry; status in the webhook event log. Which events: `shopware-core` → `sw-event-catalog`.
- For purely plugin-internal reactions use subscribers (`sw-events-subscriber`), webhooks for **external** receivers.

App development (manifest, signature handling, SDKs): plugin `shopware-apps` (`sw-app-php-sdk`/`sw-app-sdk-js`).
