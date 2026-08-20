# sw-settings-listing-option-general-info

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sortingOption | `any` | — | yes |  |
| isDefaultSorting | `any` | — | yes |  |
| technicalNameError | `any` | `{}` | no |  |
| labelError | `any` | `{}` | no |  |

## Examples

### Example 1
Source: `sw-settings-listing/page/sw-settings-listing-option-base/sw-settings-listing-option-base.html.twig`
```twig
    <sw-settings-listing-option-general-info
        v-if="productSortingEntity"
        :sorting-option="productSortingEntity"
        :is-default-sorting="isDefaultSorting"
        :label-error="sortingOptionLabelError"
        :technical-name-error="sortingOptionTechnicalNameError"
    />
    {% endblock %}

    {% block sw_settings_listing_option_base_smart_bar_actions_grid %}
    <sw-settings-listing-option-criteria-grid
        v-if="productSortingEntity"
        :product-sorting-entity="productSortingEntity"
        @criteria-delete="onDeleteCriteria"
        @criteria-add="onAddCriteria"
```
