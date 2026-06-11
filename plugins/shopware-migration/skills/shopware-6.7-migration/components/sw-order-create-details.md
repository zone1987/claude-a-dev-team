# sw-order-create-details

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateContext` | |
| `loadCart` | |
| `onRemoveExistingCode` | |
| `onRemoveItems` | |
| `updatePromotionList` | |
| `toggleAutomaticPromotions` | |
| `onClosePromotionModal` | |
| `onSavePromotionModal` | |
| `modifyShippingCosts` | |
| `handlePromotionCodeTags` | |
| `onSubmitCode` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelId` | |
| `customer` | |
| `cart` | |
| `currency` | |
| `salesChannelContext` | |
| `email` | |
| `phoneNumber` | |
| `cartDelivery` | |
| `shippingCosts` | |
| `deliveryDate` | |
| `shippingMethodCriteria` | |
| `paymentMethodCriteria` | |
| `languageCriteria` | |
| `currencyCriteria` | |
| `currencyRepository` | |
| `isCartTokenAvailable` | |
| `hasLineItem` | |
| `promotionCodeLineItems` | |
| `disabledAutoPromotion` | |
| `promotionCodeTags` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
    <sw-order-create-details-header
        :customer="customer"
        :order-date="orderDate"
        :cart-price="cartPrice"
        :currency="currency"
        @on-select-existing-customer="onSelectExistingCustomer"
    />
    {% endblock %}
    {% block sw_order_create_details_body %}
    <sw-order-create-details-body
        :customer="customer"
        :is-customer-active="isCustomerActive"
        @on-edit-billing-address="onEditBillingAddress"
        @on-edit-shipping-address="onEditShippingAddress"
    />
```
