# sw-order-create-initial

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCloseCreateModal` | |
| `onPreviewOrder` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customerRepository` | |
| `customerCriteria` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-initial/sw-order-create-initial.html.twig`
```twig
    <sw-order-create-initial-modal
        v-if="routeCustomerReady"
        @modal-close="onCloseCreateModal"
        @order-preview="onPreviewOrder"
    />
    <sw-loader v-else />
</div>
{% endblock %}

```
