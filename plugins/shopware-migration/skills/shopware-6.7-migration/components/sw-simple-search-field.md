# sw-simple-search-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'default'` | no | Valid: `default`, `inverted`, `form` |
| value | `any` | `null` | no |  |
| size | `any` | `'default'` | no |  |
| delay | `any` | `400` | no |  |
| icon | `any` | `'regular-search-s'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-simple-search-field-icon | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| search-term-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onInput` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `fieldClasses` | |
| `placeholder` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
<sw-simple-search-field
    v-model:value="term"
    size="small"
    variant="form"
    @search-term-change="onSearchCountryState"
/>
{% endblock %}

{% block sw_settings_country_state_list_toolbar_delete %}
<mt-button
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('country.editor'),
        showOnDisabledElements: true
    }"
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-simple-search-field
    v-model:value="liveSearchTerm"
    class="sw-settings-search-live-search__search_box"
    variant="form"
    :delay="1000"
    :disabled="!isSearchEnable || undefined"
    @search-term-change="searchOnStorefront"
>

    {% block sw_settings_search_view_live_search_search_icon_wrapper %}
    <template #sw-simple-search-field-icon>
        {% block sw_settings_search_view_live_search_search_icon %}
        <mt-icon
            class="sw-settings-search-live-search__search-icon"
            name="regular-search-s"
```

### Example 3
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-modal/sw-settings-product-feature-sets-modal.html.twig`
```twig
    <sw-simple-search-field
        v-model:value="term"
        size="small"
        variant="form"
        @search-term-change="onSearchCustomFields"
    />
    {% endblock %}

</div>
{% endblock %}

<sw-data-grid
    ref="customFieldGrid"
    :data-source="customFields"
    :columns="customFieldColumns"
```

### Example 4
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-modal/sw-settings-product-feature-sets-modal.html.twig`
```twig
    <sw-simple-search-field
        v-model:value="term"
        size="small"
        variant="form"
        @search-term-change="onSearchPropertyGroups"
    />
    {% endblock %}

</div>
{% endblock %}

<sw-data-grid
    ref="propertyGroupGrid"
    :data-source="propertyGroups"
    :columns="propertyGroupColumns"
```

### Example 5
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-values-card/sw-settings-product-feature-sets-values-card.html.twig`
```twig
<sw-simple-search-field
    v-model:value="term"
    size="small"
    variant="form"
    :disabled="!allowEdit || undefined"
    @search-term-change="onSearch"
/>
{% endblock %}

{% block sw_product_feature_set_toolbar_delete %}
<mt-button
    :disabled="deleteButtonDisabled || !allowEdit || undefined"
    square
    size="small"
    class="sw-product-feature-set__delete-button"
```
