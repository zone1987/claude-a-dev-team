# Shopware 6 — App Payment

Apps provide payment methods through the manifest (no PHP handler in the shop). Shopware calls the app URLs
(signed), and the app responds with a status or a redirect.

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

Variants: synchronous, asynchronous (redirect via `pay-url` → return → `finalize-url`), prepared, recurring, refund.
Requests are HMAC-signed (verify the app secret). App server/SDK: `shopware-apps` (`sw-app-php-sdk`/`sw-app-sdk-js`).
Plugin variant (PHP): `sw-payment-handler`.
