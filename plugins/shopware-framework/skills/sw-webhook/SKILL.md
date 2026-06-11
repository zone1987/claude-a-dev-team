---
name: sw-webhook
description: >
  Webhooks in Shopware 6: Events an externe URLs senden (Webhook-Entity/Manifest), HMAC-Signatur, App-/Plugin-Kontext,
  Webhook-EventLog. Trigger: "Webhook shopware", "Event an externe URL", "webhook HMAC", "sw-shopware-shop-signature",
  "webhook registrieren", "webhook event log". Shopware 6.7.
---

# Shopware 6 — Webhooks

Shopware kann Business-Events an externe URLs senden — primär das **App-System** (Manifest `<webhooks>`), aber auch
programmatisch über die `webhook`-Entity.

```xml
<!-- App-Manifest -->
<webhooks>
    <webhook name="order-placed" url="https://app.example.com/hook/order" event="checkout.order.placed"/>
</webhooks>
```

- Payload wird mit dem App-Secret **HMAC-signiert** (Header `shopware-shop-signature`) — empfängerseitig verifizieren.
- Zustellung asynchron mit Retry; Status im Webhook-Event-Log. Welche Events: `shopware-core` → `sw-event-catalog`.
- Für reine Plugin-interne Reaktionen Subscriber nutzen (`sw-events-subscriber`), Webhooks für **externe** Empfänger.

App-Entwicklung (Manifest, Signatur-Handling, SDKs): Plugin `shopware-apps` (`sw-app-php-sdk`/`sw-app-sdk-js`).
