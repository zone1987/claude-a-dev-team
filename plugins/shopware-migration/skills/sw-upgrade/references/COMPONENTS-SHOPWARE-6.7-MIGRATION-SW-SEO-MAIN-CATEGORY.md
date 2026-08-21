# sw-seo-main-category

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentSalesChannelId | `any` | `null` | no |  |
| categories | `any` | — | yes |  |
| mainCategories | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| allowEdit | `any` | `true` | no |  |
| overwriteLabel | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| main-category-add | — | |
| main-category-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onMainCategorySelected` | |
| `refreshMainCategoryForSalesChannel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mainCategoryRepository` | |
| `isHeadlessSalesChannel` | |
| `selectedCategory` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-seo/sw-product-detail-seo.html.twig`
```twig
                    <sw-seo-main-category
                        :current-sales-channel-id="props.currentSalesChannelId"
                        :categories="categories"
                        :main-categories="isInherited ? parentProduct.mainCategories : product.mainCategories"
                        :overwrite-label="true"
                        :allow-edit="acl.can('product.editor') && !isInherited"
                        @main-category-add="onAddMainCategory"
                        @main-category-remove="onRemoveMainCategory"
                    />
                    {% endblock %}
                </template>

            </sw-inherit-wrapper>
            {% endblock %}
        </template>
```
