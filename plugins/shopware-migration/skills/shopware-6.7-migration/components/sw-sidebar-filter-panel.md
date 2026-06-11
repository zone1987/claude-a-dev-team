# sw-sidebar-filter-panel

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| activeFilterNumber | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `resetAll` | |

## Examples

### Example 1
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="product_review"
                :store-key="storeKey"
                :filters="listFilters"
                :defaults="defaultFilters"
                :active-filter-number="activeFilterNumber"
                @criteria-changed="updateCriteria"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 2
Source: `sw-settings-rule/page/sw-settings-rule-list/sw-settings-rule-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="rule"
                :store-key="storeKey"
                :active-filter-number="activeFilterNumber"
                :filters="listFilters"
                :defaults="defaultFilters"
                @criteria-changed="updateCriteria"
            />
        {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
    {% endblock %}
</sw-page>
    {% endblock %}
```

### Example 3
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="product"
                :store-key="storeKey"
                :active-filter-number="activeFilterNumber"
                :filters="listFilters"
                :defaults="defaultFilters"
                @criteria-changed="updateCriteria"
            />
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 4
Source: `sw-customer/page/sw-customer-list/sw-customer-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="customer"
                :store-key="storeKey"
                :filters="listFilters"
                :defaults="defaultFilters"
                :active-filter-number="activeFilterNumber"
                @criteria-changed="updateCriteria"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 5
Source: `sw-order/page/sw-order-list/sw-order-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="order"
                :store-key="storeKey"
                :filters="listFilters"
                :defaults="defaultFilters"
                :active-filter-number="activeFilterNumber"
                @criteria-changed="updateCriteria"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
    {% endblock %}
</sw-page>
{% endblock %}
```
