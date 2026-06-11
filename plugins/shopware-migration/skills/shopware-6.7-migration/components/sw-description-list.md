# sw-description-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| grid | `any` | `'1fr'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `descriptionListStyles` | |

## Examples

### Example 1
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
<sw-description-list>
    {% block sw_customer_base_metadata_created_at_label %}
    <dt class="sw-review-base-info__label">
        {{ $tc('sw-review.detail.labelCreatedAt') }}
    </dt>
    {% endblock %}

    {% block sw_customer_base_metadata_created_at_content %}
    <dd>
        <sw-time-ago
            :date="review.createdAt"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </dd>
    {% endblock %}
```

### Example 2
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
<sw-description-list>
    {% block sw_customer_base_metadata_sales_channel_label %}
    <dt class="sw-review-base-info__label">
        {{ $tc('sw-review.detail.labelSalesChannel') }}
    </dt>
    {% endblock %}

    {% block sw_customer_base_metadata_sales_channel_content %}
    <dd>
        {{ review.salesChannel.name }}
    </dd>
    {% endblock %}
</sw-description-list>
```

### Example 3
Source: `sw-customer/component/sw-customer-base-info/sw-customer-base-info.html.twig`
```twig
<sw-description-list>
    <dt class="sw-customer-base-info__label">
        {{ $tc('sw-customer.baseInfo.labelCompany') }}
    </dt>

    <dd>
        {{ customer.company }}
    </dd>
</sw-description-list>
```

### Example 4
Source: `sw-customer/component/sw-customer-base-info/sw-customer-base-info.html.twig`
```twig
<sw-description-list>
    <dt class="sw-customer-base-info__label">
        {{ $tc('sw-customer.baseInfo.labelVatId') }}
    </dt>

    <dd>
        {{ customer.vatIds[0] || '-' }}
    </dd>
</sw-description-list>
```

### Example 5
Source: `sw-order/component/sw-order-send-document-modal/sw-order-send-document-modal.html.twig`
```twig
<sw-description-list>
    <dt>{{ $tc('sw-order.documentSendModal.labelNumber') }}</dt>
    <dd>{{ document.config.documentNumber }}</dd>
</sw-description-list>
```
