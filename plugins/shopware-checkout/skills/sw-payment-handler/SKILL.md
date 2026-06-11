---
name: sw-payment-handler
description: >
  Eigener Payment-Handler in Shopware 6 (6.7 AbstractPaymentHandler): pay()/finalize(), synchron/asynchron/vorbereitet,
  refund, payment_method-Entity, PaymentException. Trigger: "Payment Handler", "AbstractPaymentHandler", "Zahlungsart plugin",
  "pay finalize", "payment method anlegen", "redirect payment", "refund handler", "PaymentException". Shopware 6.7.
  Scaffolder: /sw-payment-handler.
---

# Shopware 6 — Payment-Handler

Seit 6.7 ein vereinheitlichter `AbstractPaymentHandler` (löst die alten Sync/Async-Interfaces ab). `pay()` startet die
Zahlung (optional Redirect), `finalize()` schließt nach Rückkehr ab.

```php
class FfPaymentHandler extends AbstractPaymentHandler
{
    public function supports(PaymentHandlerType $type, string $paymentMethodId, Context $context): bool
    { return $type === PaymentHandlerType::REFUND; }

    public function pay(Request $request, PaymentTransactionStruct $transaction, Context $context, ?Struct $validateStruct): ?RedirectResponse
    { /* Zahlung initiieren; bei Redirect RedirectResponse zurückgeben, sonst null */ }

    public function finalize(Request $request, PaymentTransactionStruct $transaction, Context $context): void
    { /* Rückkehr verarbeiten; bei Abbruch PaymentException::customerCanceled(...) */ }
}
```

`payment_method`-Entity per Migration/Lifecycle anlegen und dem Handler zuordnen; Transaktions-Status über die
StateMachine setzen (`sw-order-state-machine`). Fehler über `PaymentException`. App-basierte Zahlung: `sw-payment-app`.
PayPal-Beispiel-SDK: `sw-paypal-sdk`.

→ Payment-Details: [references/payment.md](references/payment.md) · Beispiel: [examples/PaymentHandler.php](examples/PaymentHandler.php)
