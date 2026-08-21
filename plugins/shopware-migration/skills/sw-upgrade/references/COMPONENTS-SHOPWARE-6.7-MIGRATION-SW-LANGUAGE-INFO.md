# sw-language-info

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entityDescription | `any` | `''` | no |  |
| isNewEntity | `any` | `false` | no |  |
| changeLanguageOnParentClick | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `refreshParentLanguage` | |
| `onClickParentLanguage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `languageId` | |
| `systemLanguageId` | |
| `language` | |
| `languageRepository` | |
| `infoParent` | |
| `infoText` | |
| `isDefaultLanguage` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-language-info
    :entity-description="placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline'))"
/>
{% endblock %}

{% block sw_settings_country_tabs_header %}
<sw-tabs position-identifier="sw-settings-country-detail-header">
    {% block sw_setting_country_tabs_setting %}
    <sw-tabs-item
        v-bind="$props"
        class="sw-settings-country__setting-tab"
        :route="{ name: isNewCountry ? 'sw.settings.country.create.general' : 'sw.settings.country.detail.general' }"
    >
        {{ $tc('sw-settings-country.page.generalTab') }}
    </sw-tabs-item>
```

### Example 2
Source: `sw-settings-country/page/sw-settings-country-create/sw-settings-country-create.html.twig`
```twig
<sw-language-info
    :entity-description="placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline'))"
    is-new-entity
/>
{% endblock %}

```

### Example 3
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-language-info :entity-description="entityDescription" />
```

### Example 4
Source: `sw-settings-product-feature-sets/page/sw-settings-product-feature-sets-detail/sw-settings-product-feature-sets-detail.html.twig`
```twig
<sw-language-info
    :entity-description="placeholder(productFeatureSet, 'name', $tc('sw-settings-product-feature-sets.detail.textHeadline'))"
/>
{% endblock %}

{% block sw_settings_product_feature_set_detail_content_card %}
<mt-card
    :title="$tc('sw-settings-product-feature-sets.detail.titleCard')"
    position-identifier="sw-settings-product-feature-sets-detail"
>

    {% block sw_settings_product_feature_set_detail_content_field_name %}

    <mt-text-field
        v-model="productFeatureSet.name"
```

### Example 5
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
<sw-language-info :entity-description="identifier" />
```
