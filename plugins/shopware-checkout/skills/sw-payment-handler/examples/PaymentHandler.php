<?php declare(strict_types=1);

namespace FfContentPlus\Checkout\Payment;

use Shopware\Core\Checkout\Payment\Cart\AbstractPaymentHandler;
use Shopware\Core\Checkout\Payment\Cart\PaymentHandlerType;
use Shopware\Core\Checkout\Payment\Cart\PaymentTransactionStruct;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\Struct\Struct;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\HttpFoundation\Request;

/**
 * @class FfContentPlusPaymentHandler
 * @package FfContentPlus\Checkout\Payment
 */
#[Package('custom-plugins')]
class FfContentPlusPaymentHandler extends AbstractPaymentHandler
{
    /**
     * @return PaymentHandlerType
     */
    public static function type(): PaymentHandlerType
    {
        return PaymentHandlerType::SYNC;
    }

    /**
     * @param PaymentTransactionStruct $transaction
     * @param Request $request
     * @param Struct $validateStruct
     * @return void
     */
    public function pay(
        PaymentTransactionStruct $transaction,
        Request $request,
        Struct $validateStruct,
    ): void {
        // Process payment
    }
}
