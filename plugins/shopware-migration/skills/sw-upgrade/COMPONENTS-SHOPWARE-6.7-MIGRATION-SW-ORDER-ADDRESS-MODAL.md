# sw-order-address-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| address | `any` | — | yes |  |
| countries | `any` | — | yes |  |
| order | `any` | — | yes |  |
| versionContext | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| reset | — | |
| address-select | — | |
| save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getCustomerInfo` | |
| `onNewActiveItem` | |
| `addressButtonClasses` | |
| `onExistingAddressSelected` | |
| `onClose` | |
| `onSave` | |
| `getCustomFieldSetData` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customerCriteria` | |
| `customFieldSetCriteria` | |
| `customerRepository` | |
| `orderRepository` | |
| `orderCustomer` | |
| `customFieldSetRepository` | |
| `salutationFilter` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
<sw-order-address-modal
    v-if="addressBeingEdited"
    :countries="countries"
    :address="addressBeingEdited"
    :order="currentOrder"
    :version-context="versionContext"
    @address-select="onAddressModalAddressSelected"
    @reset="onResetOrder"
    @save="onAddressModalSave"
    @error="$emit('error')"
/>
{% endblock %}

<template #grid>
    <sw-container rows="auto auto">
```
