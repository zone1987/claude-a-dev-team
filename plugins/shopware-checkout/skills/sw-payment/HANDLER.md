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

→ Payment-Details: [HANDLER-OVERVIEW.md](HANDLER-OVERVIEW.md) · Beispiel: [examples/PaymentHandler.php](examples/PaymentHandler.php)
