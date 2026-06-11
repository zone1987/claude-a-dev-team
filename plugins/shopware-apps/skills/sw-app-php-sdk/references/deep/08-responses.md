# PHP SDK — Response Factories & Gateway Commands

## ActionButtonResponse

`Shopware\App\SDK\Response\ActionButtonResponse` — all methods static, return 200 JSON `ResponseInterface`.

```php
ActionButtonResponse::openNewTab(string $url): ResponseInterface
ActionButtonResponse::reload(): ResponseInterface
ActionButtonResponse::modal(string $url, string $size = 'medium', bool $expand = false): ResponseInterface
// size: 'small' | 'medium' | 'large' | 'fullscreen'
ActionButtonResponse::notification(string $type, string $message): ResponseInterface
// type: 'success' | 'error' | 'info' | 'warning'
```

## PaymentResponse

`Shopware\App\SDK\Response\PaymentResponse` — all static.

**Status constants:**
`ACTION_CANCEL`, `ACTION_FAIL`, `ACTION_PAID`, `ACTION_PAID_PARTIALLY`, `ACTION_PROCESS`, `ACTION_PROCESS_UNCONFIRMED`, `ACTION_REFUND`, `ACTION_REMIND`, `ACTION_REOPEN`, `ACTION_AUTHORIZE`, `ACTION_CHARGEBACK`

| Method | Purpose |
|--------|---------|
| `paid()` | Mark transaction paid |
| `paidPartially()` | Partially paid |
| `cancelled(string $msg = '')` | Cancel |
| `failed(string $msg = '')` | Fail |
| `authorize()` | Authorize (prepared payment) |
| `unconfirmed()` | Process unconfirmed |
| `inProgress()` | In progress |
| `refunded()` | Refunded |
| `reminded()` | Reminded |
| `chargeback()` | Chargeback |
| `reopen()` | Reopen |
| `validateSuccess(array $data)` | Returns `{preOrderPayment: $data}` — for validate endpoint |
| `validationError(string $msg)` | Validation failed |
| `redirectUrl(string $status, string $url)` | Redirect with status |
| `createStatusResponse(string $status, string $msg = '')` | Generic helper |
| `redirect(string $url)` | **@deprecated tag:v5.0.0** |

```php
// Async payment — step 1 (pay endpoint):
return PaymentResponse::redirect('https://payment-provider.example.com/pay?token=xyz');

// Step 2 (finalize endpoint):
if ($wasSuccessful) {
    return PaymentResponse::paid();
} else {
    return PaymentResponse::failed('Payment declined by provider');
}
```

## RefundResponse

`Shopware\App\SDK\Response\RefundResponse`

Constants: `ACTION_CANCEL`, `ACTION_COMPLETE`, `ACTION_FAIL`, `ACTION_PROCESS`, `ACTION_REOPEN`

Static methods: `open()`, `inProgress()`, `cancelled()`, `failed()`, `completed()`

## GatewayResponse

`Shopware\App\SDK\Response\GatewayResponse`

```php
GatewayResponse::createCheckoutGatewayResponse(Collection $checkoutCommands): ResponseInterface
GatewayResponse::createContextGatewayResponse(Collection $contextCommands): ResponseInterface
```

Responses **must** be signed with `ResponseSigner::signResponse()`.

## InAppPurchasesResponse

`Shopware\App\SDK\Response\InAppPurchasesResponse`

```php
InAppPurchasesResponse::filter(Collection $purchases): ResponseInterface
// Returns JSON: {"purchases": ["key1", "key2"]}
```

## TaxProviderResponseBuilder

`Shopware\App\SDK\TaxProvider\TaxProviderResponseBuilder`

```php
$builder = new TaxProviderResponseBuilder();

// Per-line-item tax
$builder->addLineItemTax('unique-identifier', new CalculatedTax(19.0, 19.0, 100.0));

// Per-delivery tax
$builder->addDeliveryTax('delivery-id', new CalculatedTax(2.85, 19.0, 15.0));

// Cart-level tax (accumulated by rate)
$builder->addCartTax(new CalculatedTax(21.85, 19.0, 115.0));

$response = $builder->build();  // ResponseInterface, must be signed
$json     = $builder->buildPayload(); // string JSON
```

`TaxProvider\CalculatedTax` constructor:
```php
__construct(
    readonly float $tax,       // absolute tax amount
    readonly float $taxRate,   // e.g. 19.0
    readonly float $price,     // gross price
    readonly ?string $label = null
)
```
`add(CalculatedTax $tax): self` — returns new instance with summed values (same rate, combined amounts).

## Checkout Gateway Commands

All extend `Shopware\App\SDK\Gateway\Checkout\CheckoutGatewayCommand`.
`jsonSerialize()` produces `{command: KEY, payload: {...}}`.

| Class | KEY | Constructor |
|-------|-----|-------------|
| `AddCartErrorCommand` | `add-cart-error` | `string $message, bool $blocking = false, int $level = Error::LEVEL_WARNING` |
| `AddPaymentMethodCommand` | `add-payment-method` | `string $paymentMethodTechnicalName` — **@experimental** |
| `AddPaymentMethodExtensionCommand` | `add-payment-method-extension` | `string $technicalName, string $extensionKey, array $extensionsPayload` |
| `AddShippingMethodCommand` | `add-shipping-method` | `string $shippingMethodTechnicalName` — **@experimental** |
| `AddShippingMethodExtensionCommand` | `add-shipping-method-extension` | `string $technicalName, string $extensionKey, array $extensionsPayload` |
| `RemovePaymentMethodCommand` | `remove-payment-method` | `string $paymentMethodTechnicalName` |
| `RemoveShippingMethodCommand` | `remove-shipping-method` | `string $shippingMethodTechnicalName` |

## Context Gateway Commands

All extend `Shopware\App\SDK\Gateway\Context\ContextGatewayCommand`.

| Class | KEY | Constructor |
|-------|-----|-------------|
| `AddCustomerMessageCommand` | `context_add-customer-message` | `string $message` — FlashBag |
| `ChangeBillingAddressCommand` | `context_change-billing-address` | `string $addressId` |
| `ChangeCurrencyCommand` | `context_change-currency` | `string $iso` — ISO 4217 e.g. `EUR` |
| `ChangeLanguageCommand` | `context_change-language` | `string $iso` — BCP 47 e.g. `en-US` |
| `ChangePaymentMethodCommand` | `context_change-payment-method` | `string $technicalName` |
| `ChangeShippingAddressCommand` | `context_change-shipping-address` | `string $addressId` |
| `ChangeShippingLocationCommand` | `context_change-shipping-location` | `?string $countryIso = null, ?string $countryStateIso = null` — overridden by customer address on login |
| `ChangeShippingMethodCommand` | `context_change-shipping-method` | `string $technicalName` |
| `LoginCustomerCommand` | `context_login-customer` | `string $customerEmail` |
| `RegisterCustomerCommand` | `context_register-customer` | `CustomerResponseStruct $data` — registers + logs in |

## CustomerResponseStruct / AddressResponseStruct

`Shopware\App\SDK\Context\Response\Customer\CustomerResponseStruct` (extends `ResponseStruct`)

Public mutable properties: `?string $title`, `?string $accountType` (`'private'|'business'`), `string $firstName`, `string $lastName`, `string $email`, `?string $salutationId`, `bool $guest = true`, `string $storefrontUrl`, `?string $requestedGroupId`, `?string $affiliateCode`, `?string $campaignCode`, `?int $birthdayDay`, `?int $birthdayMonth`, `?int $birthdayYear`, `?string $password`, `AddressResponseStruct $billingAddress`, `?AddressResponseStruct $shippingAddress`, `array<string> $vatIds`, `bool $acceptedDataProtection = false`, `array<string, mixed> $customFields`

`AddressResponseStruct`: `?string $title`, `string $firstName`, `string $lastName`, `?string $salutationId`, `string $street`, `string $zipcode`, `string $city`, `?string $company`, `?string $department`, `?string $countryStateId`, `string $countryId`, `?string $additionalAddressLine1`, `?string $additionalAddressLine2`, `?string $phoneNumber`
