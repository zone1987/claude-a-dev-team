# sw-tax-rule-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| tax | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `paginate` | |
| `onColumnSort` | |
| `onSearchTermChange` | |
| `onModalClose` | |
| `showRuleModal` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `hasTypeCellComponent` | |
| `getTypeCellComponent` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `taxRuleRepository` | |
| `taxRulesEmpty` | |
| `taxRuleCardClasses` | |
| `taxRuleCriteria` | |
| `getColumns` | |
| `assetFilter` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-settings-tax/page/sw-settings-tax-detail/sw-settings-tax-detail.html.twig`
```twig
                <sw-tax-rule-card
                    v-if="tax.id"
                    :disabled="!taxId"
                    class="sw-settings-tax-detail__tax-rule-grid"
                    :tax="tax"
                    :is-loading="isLoading"
                />
                {% endblock %}

                {% block sw_settings_tax_detail_custom_field_sets %}
                <mt-card
                    v-if="showCustomFields"
                    position-identifier="sw-settings-tax-detail-custom-field-sets"
                    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                    :is-loading="isLoading"
```
