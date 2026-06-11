# sw-sales-channel-product-assignment-categories

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| containerStyle | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |
| product-loading | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSearchTermChange` | |
| `createdComponent` | |
| `categoryCriteria` | |
| `categorySearchCriteria` | |
| `getTreeItems` | |
| `onChangeSearchTerm` | |
| `onCheckItem` | |
| `removeItem` | |
| `searchCategories` | |
| `isSearchItemChecked` | |
| `onCheckSearchItem` | |
| `getBreadcrumb` | |
| `productCriteria` | |
| `getProductFromCategories` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `categoryRepository` | |
| `productRepository` | |
| `selectedCategoriesItemsIds` | |
| `selectedCategoriesPathIds` | |

## Examples

### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-products-assignment-modal/sw-sales-channel-products-assignment-modal.html.twig`
```twig
                <sw-sales-channel-product-assignment-categories
                    ref="category"
                    v-hide="active === 'categories'"
                    :sales-channel="salesChannel"
                    :container-style="categoryContainerStyle"
                    @selection-change="onChangeSelection"
                    @product-loading="setProductLoading"
                />
                {% endblock %}

                {% block sw_sales_channel_products_assignment_modal_tab_content_dynamic_product_groups %}
                <sw-sales-channel-products-assignment-dynamic-product-groups
                    ref="productGroup"
                    v-hide="active === 'dynamicProductGroups'"
                    :sales-channel="salesChannel"
```
