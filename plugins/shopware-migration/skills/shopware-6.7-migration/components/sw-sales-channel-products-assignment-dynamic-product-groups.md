# sw-sales-channel-products-assignment-dynamic-product-groups

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
| `createdComponent` | |
| `getProductStreams` | |
| `onSearch` | |
| `onPaginate` | |
| `onOpen` | |
| `onSelect` | |
| `getProductsFromProductStreams` | |
| `getProductStreamFilter` | |
| `getProducts` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productStreamRepository` | |
| `productCriteria` | |
| `productStreamCriteria` | |
| `productStreamColumns` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-products-assignment-modal/sw-sales-channel-products-assignment-modal.html.twig`
```twig
                <sw-sales-channel-products-assignment-dynamic-product-groups
                    ref="productGroup"
                    v-hide="active === 'dynamicProductGroups'"
                    :sales-channel="salesChannel"
                    :container-style="productGroupContainerStyle"
                    @selection-change="onChangeSelection"
                    @product-loading="setProductLoading"
                />
                {% endblock %}
            </div>
        </template>
    </sw-tabs>
    {% endblock %}
</template>

```
