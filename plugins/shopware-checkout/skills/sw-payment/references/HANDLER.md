# Shopware 6 — Payment Handler

Since 6.7 there is one unified `AbstractPaymentHandler` (replacing the old sync/async interfaces). `pay()` starts the
payment (optionally with a redirect), `finalize()` completes it after the return.

```php
class FfPaymentHandler extends AbstractPaymentHandler
{
    public function supports(PaymentHandlerType $type, string $paymentMethodId, Context $context): bool
    { return $type === PaymentHandlerType::REFUND; }

    public function pay(Request $request, PaymentTransactionStruct $transaction, Context $context, ?Struct $validateStruct): ?RedirectResponse
    { /* initiate payment; return a RedirectResponse for a redirect, otherwise null */ }

    public function finalize(Request $request, PaymentTransactionStruct $transaction, Context $context): void
    { /* handle the return; on cancellation PaymentException::customerCanceled(...) */ }
}
```

Create the `payment_method` entity via migration/lifecycle and assign it to the handler; set the transaction state through the
state machine — see `ORDER-STATE-MACHINE.md` in `sw-fulfilment`. Report errors via `PaymentException`.
App-based payment: `APP.md`. The PayPal SDK example: `PAYPAL-SDK.md`.

→ The full handler reference, the removed 6.6 tags and interfaces, and the plugin lifecycle:
[HANDLER-OVERVIEW.md](HANDLER-OVERVIEW.md)
