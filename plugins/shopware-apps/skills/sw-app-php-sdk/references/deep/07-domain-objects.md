# PHP SDK — Domain Objects (Cart, Order, SalesChannelContext)

All domain objects extend `ArrayStruct` unless noted. Access raw data via `toArray()`.

## Cart

`Shopware\App\SDK\Context\Cart\Cart`

| Method | Returns |
|--------|---------|
| `getToken()` | `string` |
| `getCustomerComment()` | `?string` |
| `getAffiliateCode()` | `?string` |
| `getCampaignCode()` | `?string` |
| `getLineItems()` | `Collection<LineItem>` |
| `getDeliveries()` | `Collection<Delivery>` |
| `getTransactions()` | `Collection<CartTransaction>` |
| `getPrice()` | `CartPrice` |

## CartPrice

| Method | Returns |
|--------|---------|
| `getNetPrice()` | `float` |
| `getTotalPrice()` | `float` |
| `getPositionPrice()` | `float` |
| `getRawTotal()` | `float` |
| `getTaxStatus()` | `string` (`'gross'`/`'net'`/`'tax-free'`) |
| `getCalculatedTaxes()` | `Collection<CalculatedTax>` |
| `getTaxRules()` | `Collection<TaxRule>` |

Constants: `TAX_STATE_GROSS = 'gross'`, `TAX_STATE_NET = 'net'`, `TAX_STATE_FREE = 'tax-free'`

## LineItem

| Method | Returns |
|--------|---------|
| `getId()` | `string` |
| `getUniqueIdentifier()` | `string` |
| `getType()` | `string` |
| `getReferencedId()` | `?string` |
| `getLabel()` | `string` |
| `getDescription()` | `?string` |
| `isGood()` | `bool` |
| `getQuantity()` | `int` |
| `getPayload()` | `array` |
| `getPrice()` | `CalculatedPrice` |
| `getStates()` | `array<string>` |
| `getChildren()` | `Collection<LineItem>` |

## CalculatedPrice

| Method | Returns | Notes |
|--------|---------|-------|
| `getUnitPrice()` | `float` | |
| `getTotalPrice()` | `float` | |
| `getQuantity()` | `int` | |
| `getCalculatedTaxes()` | `Collection<CalculatedTax>` | |
| `getTaxRules()` | `Collection<TaxRule>` | |
| `CalculatedPrice::sum(Collection $prices)` | `CalculatedPrice` | static: aggregate multiple prices |

## CalculatedTax

| Method | Returns |
|--------|---------|
| `getTaxRate()` | `float` |
| `getPrice()` | `float` |
| `getTax()` | `float` |
| `getLabel()` | `?string` |
| `CalculatedTax::sum(Collection $taxes)` | `Collection<CalculatedTax>` — merges by rate |

## Delivery / DeliveryPosition / DeliveryDate / CartTransaction / TaxRule

```
Delivery:         getPositions(), getLocation(): ShippingLocation, getShippingMethod(): ShippingMethod,
                  getDeliveryDate(): DeliveryDate, getShippingCosts(): CalculatedPrice
DeliveryDate:     getEarliest(): \DateTimeInterface, getLatest(): \DateTimeInterface
DeliveryPosition: getIdentifier(), getLineItem(): LineItem, getQuantity(): int,
                  getDeliveryDate(): DeliveryDate, getPrice(): CalculatedPrice
CartTransaction:  getPaymentMethodId(): string, getAmount(): CalculatedPrice
TaxRule:          getTaxRate(): float, getPercentage(): float
```

## Order

`Shopware\App\SDK\Context\Order\Order` (extends ArrayStruct, uses CustomFieldsAware)

| Method | Returns |
|--------|---------|
| `getId()` | `string` |
| `getOrderNumber()` | `string` |
| `getCurrencyFactor()` | `float` |
| `getOrderDate()` | `\DateTimeInterface` |
| `getPrice()` | `CartPrice` |
| `getAmountTotal()` | `float` |
| `getAmountNet()` | `float` |
| `getPositionPrice()` | `float` |
| `getTaxStatus()` | `string` |
| `getShippingTotal()` | `float` |
| `getShippingCosts()` | `CalculatedPrice` |
| `getOrderCustomer()` | `OrderCustomer` |
| `getCurrency()` | `Currency` |
| `getBillingAddress()` | `Address` |
| `getLineItems()` | `Collection<OrderLineItem>` |
| `getItemRounding()` | `RoundingConfig` |
| `getTotalRounding()` | `RoundingConfig` |
| `getDeepLinkCode()` | `string` |
| `getSalesChannelId()` | `string` |
| `getDeliveries()` | `Collection<OrderDelivery>` |
| `getTransactions()` | `Collection<OrderTransaction>` |
| `getLanguage()` | `?Language` |

## OrderTransaction (uses CustomFieldsAware)

`getId()`, `getAmount(): CalculatedPrice`, `getPaymentMethod(): PaymentMethod`, `getStateMachineState(): StateMachineState`, `getOrder(): Order`, `getValidationData(): array`

## OrderCustomer (uses CustomFieldsAware)

`getId()`, `getEmail()`, `getFirstName()`, `getLastName()`, `getTitle(): ?string`, `getVatIds(): array<string>`, `getCompany(): ?string`, `getCustomerNumber()`, `getCustomerId(): ?string`, `getSalutation(): ?Salutation`, `getRemoteAddress()`, `getCustomer(): Customer`

## OrderLineItem (extends LineItem)

Additional: `getParentId(): ?string`, `getPosition(): int`

## SalesChannelContext

`Shopware\App\SDK\Context\SalesChannelContext\SalesChannelContext` (extends ArrayStruct)

| Method | Returns |
|--------|---------|
| `getToken()` | `string` |
| `getCurrencyId()` | `string` |
| `getTaxState()` | `string` |
| `getRounding()` | `RoundingConfig` |
| `getCurrency()` | `Currency` |
| `getShippingMethod()` | `ShippingMethod` |
| `getPaymentMethod()` | `PaymentMethod` |
| `getSalesChannel()` | `SalesChannel` |
| `getCustomer()` | `?Customer` |
| `getLanguageInfo()` | `LanguageInfo` |
| `getShippingLocation()` | `ShippingLocation` |

## PaymentMethod

`getId()`, `getName()`, `getTechnicalName(): string` (since 6.7, returns `''` if null), `getDescription()`, `isActive(): bool`, `isAfterOrderEnabled(): bool`, `getAvailabilityRuleId(): ?string`, `isSynchronous(): bool`, `isAsynchronous(): bool`, `isPrepared(): bool`, `isRefundable(): bool`

## ShippingMethod

`getId()`, `getName()`, `getTechnicalName(): string` (since 6.7), `getTaxType()`

## Currency (uses CustomFieldsAware)

`getId()`, `getIsoCode()`, `getFactor(): float`, `getSymbol()`, `getShortName()`, `getName()`, `getItemRounding(): RoundingConfig`, `getTotalRounding(): RoundingConfig`, `getTaxFreeFrom(): float`

## Address (uses CustomFieldsAware)

`getId()`, `getSalutation(): ?Salutation`, `getFirstName()`, `getLastName()`, `getStreet()`, `getZipCode()`, `getCity()`, `getCompany(): ?string`, `getDepartment(): ?string`, `getTitle(): ?string`, `getCountry(): Country`, `getCountryState(): ?CountryState`, `getPhoneNumber(): ?string`, `getAdditionalAddressLine1(): ?string`, `getAdditionalAddressLine2(): ?string`

## Country / CountryState / TaxInfo

```
Country (CustomFieldsAware): getId(), getName(), getIso(), getIso3(),
                              getCustomerTax(): TaxInfo, getCompanyTax(): TaxInfo
CountryState (CustomFieldsAware): getId(), getName(), getShortCode(), getPosition(): int
TaxInfo: isEnabled(): bool, getCurrencyId(), getAmount(): float
```

## SalesChannel / SalesChannelDomain / LanguageInfo / RoundingConfig / ShippingLocation

```
SalesChannel: getId(), getName(), getAccessKey(), getTaxCalculationType(),
              getCurrency(): Currency, getDomains(): Collection<SalesChannelDomain>
SalesChannelDomain (CustomFieldsAware): getId(), getUrl(), getLanguageId(), getCurrencyId(), getSnippetSetId()
LanguageInfo: getName(), getLocaleCode()
RoundingConfig: getDecimals(): int, getInterval(): float, isRoundForNet(): bool
ShippingLocation: getCountry(): Country, getCountryState(): ?CountryState, getAddress(): Address
Salutation: getId(), getDisplayName(), getLetterName(), getSalutationKey()
```

## Customer (SalesChannelContext, uses CustomFieldsAware)

`getId()`, `getFirstName()`, `getLastName()`, `getEmail()`, `getCompany(): ?string`, `getCustomerNumber()`, `getTitle(): ?string`, `isActive(): bool`, `isGuest(): bool`, `getAccountType(): string`, `getVatIds(): array<string>`, `getRemoteAddress()`, `getSalutation(): ?Salutation`, `getDefaultPaymentMethod(): PaymentMethod`, `getDefaultBillingAddress(): Address`, `getDefaultShippingAddress(): Address`, `getActiveBillingAddress(): Address` (fallback to default), `getActiveShippingAddress(): Address` (fallback to default)

## Refund / RefundTransactionCapture (both use CustomFieldsAware)

```
Refund: getId(), getReason(): ?string, getAmount(): CalculatedPrice,
        getStateMachineState(): StateMachineState, getTransactionCapture(): RefundTransactionCapture
RefundTransactionCapture: getExternalReference(): ?string, getAmount(): CalculatedPrice,
                          getTransaction(): OrderTransaction
RecurringData (deprecated getters in v6): getSubscriptionId(): string @deprecated,
                                          getNextSchedule(): \DateTimeInterface @deprecated
                                          Use toArray() for raw data access.
```
