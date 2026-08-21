# sw-settings-product-feature-sets-values-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productFeatureSet | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| allowEdit | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onAddField` | |
| `onGridSelectionChanged` | |
| `onSearch` | |
| `doSearch` | |
| `getList` | |
| `onModalClose` | |
| `onShowFeatureModal` | |
| `onDeleteFields` | |
| `onPositionChange` | |
| `resetPositions` | |
| `getColumns` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productFeatureSetRepository` | |
| `propertyGroupRepository` | |
| `customFieldRepository` | |
| `valuesEmpty` | |
| `valuesCardClasses` | |
| `productFeatureSetCriteria` | |
| `featureGridTranslationService` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-settings-product-feature-sets/page/sw-settings-product-feature-sets-detail/sw-settings-product-feature-sets-detail.html.twig`
```twig
                <sw-settings-product-feature-sets-values-card
                    v-if="productFeatureSet.id"
                    :disabled="!productFeatureSetId || undefined"
                    :allow-edit="acl.can('product_feature_sets.editor') || undefined"
                    class="sw-settings-product-feature-sets-detail__tax-rule-grid"
                    :product-feature-set="productFeatureSet"
                    :is-loading="isLoading"
                    @product-feature-set-rule-save="onSave"
                />
                {% endblock %}
            </template>
        </sw-card-view>
    </template>
    {% endblock %}

```
