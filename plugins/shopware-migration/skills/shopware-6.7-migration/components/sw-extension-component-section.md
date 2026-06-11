# sw-extension-component-section

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| positionIdentifier | `any` | — | yes |  |
| deprecated | `any` | `false` | no |  |
| deprecationMessage | `any` | `''` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `setActiveTab` | |
| `getActiveTab` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `componentSections` | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
<sw-extension-component-section
    v-if="isThemeRoute"
    position-identifier="sw-extension-my-extensions-listing__before-content"
/>

<sw-meteor-card
    v-if="!extensionListPaginated.length && filterByActiveState"
    class="sw-extension-my-extensions-listing__empty-state"
>
    <img
        :src="assetFilter('administration/administration/static/img/empty-states/extensions-empty-state.svg')"
        alt=""
    >

    <h3 v-if="isThemeRoute">
```

### Example 2
Source: `sw-settings-tax/page/sw-settings-tax-provider-detail/sw-settings-tax-provider-detail.html.twig`
```twig
                <sw-extension-component-section
                    v-if="hasIdentifier"
                    :position-identifier="positionIdentifier"
                />
            </template>
        </sw-card-view>
    </template>
</sw-page>
{% endblock %}

```

### Example 3
Source: `sw-settings/page/sw-settings-index/sw-settings-index.html.twig`
```twig
<sw-extension-component-section
    position-identifier="sw-settings-index"
/>

{% block sw_settings_content_card_view_header %}
<div class="sw-settings__content-header">
    <h1 class="sw-settings__content-header-title">
        {{ $tc('sw-settings.index.title') }}
    </h1>

    <mt-search
        v-model="searchQuery"
        class="sw-settings__content-header-search"
        :placeholder="$t('sw-settings.index.search.placeholder')"
        size="small"
```

### Example 4
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
<sw-extension-component-section
    position-identifier="sw-product-detail__before-content"
/>

{% block sw_product_detail_content_view %}
<router-view
    v-slot="{ Component }"
>
    <component
        :is="Component"
        @cover-change="onCoverChange"
    />
</router-view>
{% endblock %}

```

### Example 5
Source: `sw-customer/page/sw-customer-detail/sw-customer-detail.html.twig`
```twig
            <sw-extension-component-section
                position-identifier="sw-customer-detail__before-content"
            />

            {% block sw_customer_detail_content_view %}
            <template v-if="isLoading">
                <sw-skeleton variant="detail-bold" />
                <sw-skeleton />
            </template>

            <router-view
                v-if="customer"
                v-slot="{ Component }"
            >
                {# v-show is used here as underlying components influence the loading state and v-if would destroy this behaviour #}
```
