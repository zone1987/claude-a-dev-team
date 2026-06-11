# Payment Handlers

## Overview

Payment handlers process payments in Shopware. They extend `AbstractPaymentHandler` and implement methods based on the payment flow type (synchronous, asynchronous with redirect, refund, recurring).

## AbstractPaymentHandler

The base class (Shopware 6.7+):

```php
abstract class AbstractPaymentHandler
{
    // Required: Which payment handler types are supported
    abstract public function supports(PaymentHandlerType $type, string $paymentMethodId, Context $context): bool;

    // Required: Main payment logic
    abstract public function pay(Request $request, PaymentTransactionStruct $transaction, Context $context, ?Struct $validateStruct): ?RedirectResponse;

    // Optional: Validate before order is persisted
    public function validate(Cart $cart, RequestDataBag $dataBag, SalesChannelContext $context): ?Struct { return null; }

    // Optional: Called after redirect (if pay() returned RedirectResponse)
    public function finalize(Request $request, PaymentTransactionStruct $transaction, Context $context): void {}

    // Optional: Process refunds
    public function refund(RefundPaymentTransactionStruct $transaction, Context $context): void {}

    // Optional: Recurring payments (subscriptions)
    public function recurring(PaymentTransactionStruct $transaction, Context $context): void {}
}
```

## Synchronous Payment Handler

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Checkout\Payment;

use Shopware\Core\Checkout\Payment\Cart\PaymentHandler\AbstractPaymentHandler;
use Shopware\Core\Checkout\Payment\Cart\PaymentHandler\PaymentHandlerType;
use Shopware\Core\Checkout\Payment\Cart\PaymentTransactionStruct;
use Shopware\Core\Framework\Context;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\Struct\Struct;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\HttpFoundation\Request;

/**
 * @class InvoicePaymentHandler
 * @package FfContentPlus\Checkout\Payment
 */
#[Package('custom-plugins')]
class InvoicePaymentHandler extends AbstractPaymentHandler
{
    /**
     * @param PaymentHandlerType $type
     * @param string $paymentMethodId
     * @param Context $context
     * @return bool
     */
    public function supports(PaymentHandlerType $type, string $paymentMethodId, Context $context): bool
    {
        return $type === PaymentHandlerType::SYNC;
    }

    /**
     * @param Request $request
     * @param PaymentTransactionStruct $transaction
     * @param Context $context
     * @param Struct|null $validateStruct
     * @return RedirectResponse|null
     */
    public function pay(
        Request $request,
        PaymentTransactionStruct $transaction,
        Context $context,
        ?Struct $validateStruct,
    ): ?RedirectResponse {
        // Synchronous payment — no redirect needed
        // Mark order as paid, capture payment, etc.
        return null;
    }
}
```

## Asynchronous Payment Handler (with Redirect)

```php
class ExternalPaymentHandler extends AbstractPaymentHandler
{
    public function supports(PaymentHandlerType $type, string $paymentMethodId, Context $context): bool
    {
        return match ($type) {
            PaymentHandlerType::ASYNC => true,
            PaymentHandlerType::REFUND => true,
            default => false,
        };
    }

    public function pay(
        Request $request,
        PaymentTransactionStruct $transaction,
        Context $context,
        ?Struct $validateStruct,
    ): ?RedirectResponse {
        // Redirect to external payment provider
        $redirectUrl = $this->paymentProvider->createPayment(
            $transaction->getOrderTransaction()->getAmount()->getTotalPrice(),
            $transaction->getReturnUrl(),
        );

        return new RedirectResponse($redirectUrl);
    }

    public function finalize(
        Request $request,
        PaymentTransactionStruct $transaction,
        Context $context,
    ): void {
        // Called after redirect back from payment provider
        $paymentId = $request->query->get('payment_id');
        $status = $this->paymentProvider->verifyPayment($paymentId);

        if ($status !== 'success') {
            throw PaymentException::asyncFinalizeInterrupted(
                $transaction->getOrderTransaction()->getId(),
                'Payment verification failed'
            );
        }
    }

    public function refund(
        RefundPaymentTransactionStruct $transaction,
        Context $context,
    ): void {
        $this->paymentProvider->refund(
            $transaction->getRefund()->getAmount()->getTotalPrice()
        );
    }
}
```

## Service Registration

```xml
<service id="FfContentPlus\Checkout\Payment\InvoicePaymentHandler">
    <tag name="shopware.payment.method.sync"/>
</service>

<service id="FfContentPlus\Checkout\Payment\ExternalPaymentHandler">
    <tag name="shopware.payment.method.async"/>
    <tag name="shopware.payment.method.refund"/>
</service>
```

## Payment Handler Types & Tags

| Type | Tag | Description |
|------|-----|-------------|
| Sync | `shopware.payment.method.sync` | No redirect, instant capture |
| Async | `shopware.payment.method.async` | Redirect to provider, finalize on return |
| Prepared | `shopware.payment.method.prepared` | Pre-authorized payment |
| Refund | `shopware.payment.method.refund` | Supports refunds |
| Recurring | `shopware.payment.method.recurring` | Subscription payments |

## Registering Payment Method (Plugin Lifecycle)

```php
public function install(InstallContext $installContext): void
{
    $paymentMethodRepository = $this->container->get('payment_method.repository');

    $paymentMethodRepository->create([
        [
            'handlerIdentifier' => InvoicePaymentHandler::class,
            'name' => 'Invoice Payment',
            'translations' => [
                'de-DE' => ['name' => 'Rechnungskauf', 'description' => 'Zahlung per Rechnung'],
                'en-GB' => ['name' => 'Invoice Payment', 'description' => 'Pay by invoice'],
            ],
        ],
    ], $installContext->getContext());
}
```
