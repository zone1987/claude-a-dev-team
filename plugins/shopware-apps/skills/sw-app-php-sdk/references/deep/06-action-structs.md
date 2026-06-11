# PHP SDK — Action Structs

All structs are `readonly` value objects. All have `shop: ShopInterface`.

## WebhookAction

`Shopware\App\SDK\Context\Webhook\WebhookAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly string $eventName;       // e.g. "order.placed"
public readonly array $payload;           // raw decoded event payload
public readonly \DateTimeInterface $timestamp;
```

## ActionButtonAction

`Shopware\App\SDK\Context\ActionButton\ActionButtonAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly array $ids;     // selected entity IDs in the Admin
public readonly string $entity; // entity type e.g. "order"
public readonly string $action; // action name from manifest
```

## ModuleAction

`Shopware\App\SDK\Context\Module\ModuleAction`

```php
public readonly ShopInterface $shop;
public readonly string $shopwareVersion;
public readonly string $contentLanguage;  // UUID
public readonly string $userLanguage;     // BCP-47, e.g. "en-GB"
public readonly Collection $inAppPurchases; // Collection<InAppPurchase>
```

## StorefrontAction

`Shopware\App\SDK\Context\Storefront\StorefrontAction`

```php
public readonly ShopInterface $shop;
public readonly StorefrontClaims $claims;
public readonly Collection $inAppPurchases;
```

## PaymentPayAction

`Shopware\App\SDK\Context\Payment\PaymentPayAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly Order $order;
public readonly OrderTransaction $orderTransaction;
public readonly ?string $returnUrl;     // only for async payments
public readonly ?RecurringData $recurring;
public readonly array $requestData;
```

## PaymentFinalizeAction

`Shopware\App\SDK\Context\Payment\PaymentFinalizeAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly OrderTransaction $orderTransaction;
public readonly ?RecurringData $recurring;
public readonly array $queryParameters; // @deprecated tag:v5.0.0 — use $requestData in 6.7+
```

## PaymentCaptureAction

`Shopware\App\SDK\Context\Payment\PaymentCaptureAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly Order $order;
public readonly OrderTransaction $orderTransaction;
public readonly ?RecurringData $recurring;
public readonly array $requestData;     // result of PaymentResponse::validateSuccess()
```

## PaymentRecurringAction

`Shopware\App\SDK\Context\Payment\PaymentRecurringAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly Order $order;
public readonly OrderTransaction $orderTransaction;
public readonly ?RecurringData $recurring;
```

## PaymentValidateAction

`Shopware\App\SDK\Context\Payment\PaymentValidateAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly Cart $cart;
public readonly SalesChannelContext $salesChannelContext;
public readonly array $requestData;
```

## RefundAction

`Shopware\App\SDK\Context\Payment\RefundAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly Order $order;
public readonly Refund $refund;
```

## TaxProviderAction

`Shopware\App\SDK\Context\TaxProvider\TaxProviderAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly SalesChannelContext $context;
public readonly Cart $cart;
```

## CheckoutGatewayAction

`Shopware\App\SDK\Context\Gateway\Checkout\CheckoutGatewayAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly Cart $cart;
public readonly SalesChannelContext $context;
public readonly Collection $paymentMethods;   // Collection<string>, keys = technical names
public readonly Collection $shippingMethods;  // Collection<string>, keys = technical names
```

## ContextGatewayAction

`Shopware\App\SDK\Context\Gateway\Context\ContextGatewayAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly Cart $cart;
public readonly SalesChannelContext $context;
public readonly array $data;  // additional context data
```

## FilterAction (InAppFeatures)

`Shopware\App\SDK\Context\Gateway\InAppFeatures\FilterAction`

```php
public readonly ShopInterface $shop;
public readonly ActionSource $source;
public readonly Collection $purchases;  // Collection<string> — identifiers to filter
```

## ActionSource

`Shopware\App\SDK\Context\ActionSource`

```php
public readonly string $url;          // shop URL
public readonly string $appVersion;   // installed app version
public readonly Collection $inAppPurchases;  // Collection<InAppPurchase>
```

## ArrayStruct

`Shopware\App\SDK\Context\ArrayStruct` (abstract base for domain objects)

```php
__construct(protected readonly array $data)
```

Methods: `toArray(): array`, `jsonSerialize(): array`, `isset(string $property): bool`, `isNull(string $property): bool`

## CustomFieldsAware (trait)

Applied to: `Address`, `Country`, `CountryState`, `Currency`, `Customer`, `Order`, `OrderCustomer`, `OrderDelivery`, `OrderTransaction`, `Refund`, `RefundTransactionCapture`, `SalesChannelDomain`.

```php
public function getCustomFields(): array  // returns [] if null
```
