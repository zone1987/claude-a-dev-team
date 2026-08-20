# Shopware 6 — App-Payment

Apps stellen Zahlungsarten über das Manifest bereit (kein PHP-Handler im Shop). Shopware ruft die App-URLs auf
(signiert), die App antwortet mit Status/Redirect.

```xml
<payments>
    <payment-method>
        <identifier>ffPay</identifier>
        <name>FF Pay</name>
        <pay-url>https://app.example.com/payment/pay</pay-url>
        <finalize-url>https://app.example.com/payment/finalize</finalize-url>
        <refund-url>https://app.example.com/payment/refund</refund-url>
    </payment-method>
</payments>
```

Varianten: synchron, asynchron (Redirect via `pay-url` → Rückkehr → `finalize-url`), vorbereitet, recurring, refund.
Requests sind HMAC-signiert (App-Secret verifizieren). App-Server/SDK: `shopware-apps` (`sw-app-php-sdk`/`sw-app-sdk-js`).
Plugin-Variante (PHP): `sw-payment-handler`.
