# sw-product-restriction-selection

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| groupsWithOptions | `any` | — | yes |  |
| restriction | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| contentAfter | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| restriction-delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `deleteRestriction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `availableGroups` | |
| `availableGroupsOptions` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-variants-configurator/sw-product-variants-configurator-restrictions/sw-product-variants-configurator-restrictions.html.twig`
```twig
<sw-product-restriction-selection
    v-for="(restriction, index) in actualRestriction.values"
    :key="restriction.id"
    :groups-with-options="groupsWithOptions"
    :restriction="restriction"
    @restriction-delete="deleteRestriction"
>

    <template #contentAfter>
        <p
            v-if="index < actualRestrictionValueLength - 1"
            class="sw-product-variants-configurator-restrictions__seperator"
        >
            {{ $tc('sw-product.variations.configuratorModal.singleRestrictionSeperation') }}
        </p>
```
