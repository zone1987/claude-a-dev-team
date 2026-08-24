# Payment Handlers

## Contents

- [Overview](#overview)
- [AbstractPaymentHandler](#abstractpaymenthandler)
- [Synchronous Payment Handler](#synchronous-payment-handler)
- [Asynchronous Payment Handler (with Redirect)](#asynchronous-payment-handler-with-redirect)
- [Service Registration](#service-registration)
- [Payment Handler Types & Tags](#payment-handler-types-tags)
- [Registering Payment Method (Plugin Lifecycle)](#registering-payment-method-plugin-lifecycle)

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

## Service registration

**One tag, since 6.7:** `shopware.payment.method`. Without it Shopware does not recognise the class
as a payment handler at all.

```php
// <plugin root>/src/Resources/config/services.php
$services->set(MyCustomPaymentHandler::class)
    ->tag('shopware.payment.method');
```

### The five tags that no longer exist

Before 6.7 a handler declared its capabilities through separate tags. All five were removed with the
unified handler — **remove every one of them when migrating**, or the handler is registered twice
over and its capabilities are read from the wrong place:

| Removed tag | Removed interface | Replaced by |
|---|---|---|
| `shopware.payment.method.sync` | `SynchronousPaymentHandlerInterface` | `pay()`, always called during checkout |
| `shopware.payment.method.async` | `AsynchronousPaymentHandlerInterface` | `finalize()`, called only when `pay()` returns a `RedirectResponse` |
| `shopware.payment.method.prepared` | `PreparedPaymentHandlerInterface` | `validate()`, always called; use it to validate the cart during checkout |
| `shopware.payment.method.recurring` | `RecurringPaymentHandlerInterface` | `recurring()`, gated by `supports(PaymentHandlerType::RECURRING, …)` |
| `shopware.payment.method.refund` | `RefundPaymentHandlerInterface` | `refund()`, gated by `supports(PaymentHandlerType::REFUND, …)` |

Those interfaces lived under `Shopware\Core\Checkout\Payment\Cart\PaymentHandler\`. Instead of
implementing several of them, extend `AbstractPaymentHandler` and implement the methods you
need. **Prepared payments** lost their `capture()` method — implement `validate()` and let the
streamlined `pay()` do the capture.

## Registering the payment method (plugin lifecycle)

The handler alone does nothing: a `payment_method` entity has to point at it. Create it on install,
in the plugin base class — `SwagBasicExample.php` in the guide's own example, i.e. the class named
after your plugin.

```php
// <plugin root>/src/SwagBasicExample.php — your plugin's base class
private function addPaymentMethod(Context $context): void
{
    $paymentMethodExists = $this->getPaymentMethodId();

    // payment method exists already, no need to continue here
    if ($paymentMethodExists) {
        return;
    }

    $pluginIdProvider = $this->container->get(PluginIdProvider::class);
    $pluginId = $pluginIdProvider->getPluginIdByBaseClass(get_class($this), $context);

    $examplePaymentData = [
        // the handler is selected by this identifier
        'handlerIdentifier' => MyCustomPaymentHandler::class,
        'name' => 'Example payment',
        'description' => 'Example payment description',
        'pluginId' => $pluginId,
        // keeps the method available after the order exists, e.g. to retry a failed payment
        'afterOrderEnabled' => true,
        // REQUIRED from 6.7; use a plugin-specific prefix
        'technicalName' => 'swag_example-example_payment',
    ];

    $this->container->get('payment_method.repository')->create([$examplePaymentData], $context);
}
```

**`technicalName` is required for plugin-provided payment methods from 6.7 on.** It must be unique,
and a plugin-specific prefix is what keeps it so. Omitting it can prevent the plugin from being
installed or activated, depending on where the validation runs — so when migrating a payment plugin
to 6.7, check whether it sets one at all.

### Uninstall deactivates, never deletes

```php
public function uninstall(UninstallContext $context): void
{
    // Only deactivate. Removing the payment method breaks data consistency,
    // because past orders reference it.
    $this->setPaymentMethodIsActive(false, $context->getContext());
}

public function activate(ActivateContext $context): void
{
    $this->setPaymentMethodIsActive(true, $context->getContext());
    parent::activate($context);
}

public function deactivate(DeactivateContext $context): void
{
    $this->setPaymentMethodIsActive(false, $context->getContext());
    parent::deactivate($context);
}
```

`setPaymentMethodIsActive()` returns early when no method exists — there is nothing to
(de)activate — and `getPaymentMethodId()` finds it by handler identifier:

```php
$paymentCriteria = (new Criteria())->addFilter(new EqualsFilter('handlerIdentifier', ExamplePayment::class));
return $paymentRepository->searchIds($paymentCriteria, Context::createDefaultContext())->firstId();
```

### Identifying your payment method

Two ways, and the second is the one to prefer:

- **`formattedHandlerIdentifier`** shortens the PHP class reference: `Custom/Payment/SEPAPayment`
  becomes `handler_custom_sepapayment`. The exact shortening lives in
  `Shopware\Core\Checkout\Payment\DataAbstractionLayer\PaymentHandlerIdentifierSubscriber`.
- **`technicalName`**, which you chose yourself and which is unique by construction.

## Customising an existing payment provider

To change how a core payment handler behaves, **decorate it** rather than replacing the method. The
example customises `Shopware\Core\Checkout\Payment\Cart\PaymentHandler\DebitPayment`; the same
procedure applies to an asynchronous handler.

The constructor takes what the original service takes — an `OrderTransactionStateHandler` — plus the
instance being decorated:

```php
// <plugin root>/src/Checkout/Payment/ExampleDebitPayment.php
public function getDecorated(): DebitPayment
{
    return $this->decorated;
}

public function pay(Request $request, PaymentTransactionStruct $transaction,
                    Context $context, ?Struct $validateStruct): ?RedirectResponse
{
    // your own behaviour here

    $this->transactionStateHandler->process(
        $transaction->getOrderTransaction()->getId(),
        $salesChannelContext->getContext()
    );
}
```

```php
// <plugin root>/src/Resources/config/services.php
$services->set(ExampleDebitPayment::class)
    ->decorate(DebitPayment::class)
    ->args([
        service(OrderTransactionStateHandler::class),
        service('.inner'),
    ]);
```

The order of `args` matches the constructor: the state handler first, then `.inner` — the service
being decorated.

## Source

- [add-payment-plugin.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/payment/add-payment-plugin.html) — the handler, its registration and the plugin lifecycle
- [customize-payment-provider.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/payment/customize-payment-provider.html) — decorating a core handler

Shopware 6.7, retrieved 2026-08-21.
