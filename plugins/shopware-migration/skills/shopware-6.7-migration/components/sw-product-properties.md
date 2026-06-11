# sw-product-properties

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| isAssociation | `any` | `true` | no |  |
| showInheritanceSwitcher | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getGroupIds` | |
| `getProperties` | |
| `onDeletePropertyValue` | |
| `onDeleteProperty` | |
| `onDeleteProperties` | |
| `onChangeSearchTerm` | |
| `turnOnAddPropertiesModal` | |
| `turnOffAddPropertiesModal` | |
| `updateNewProperties` | |
| `onCancelAddPropertiesModal` | |
| `onSaveAddPropertiesModal` | |
| `checkIfPropertiesExists` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `propertyGroupRepository` | |
| `propertyOptionRepository` | |
| `propertyGroupCriteria` | |
| `propertyExistsCriteria` | |
| `propertyColumns` | |
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `isChild` | |
| `productProperties` | |
| `assetFilter` | |
| `productHasProperties` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-specifications/sw-product-detail-specifications.html.twig`
```twig
<sw-product-properties
    v-show="showProductCard('properties')"
/>
{% endblock %}

{% block sw_product_detail_specifications_essential_characteristics %}
<mt-card
    v-show="showProductCard('essential_characteristics')"
    class="sw-product-detail-specification__essential-characteristics"
    position-identifier="sw-product-detail-specifications-essential-characteristics"
    :title="$tc('sw-product.specifications.cardTitleEssentialCharacteristics')"
>
    {% block sw_product_detail_specifications_essential_characteristics_content %}
    <sw-product-feature-set-form :allow-edit="acl.can('product.editor')" />
    {% endblock %}
```
