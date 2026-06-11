# sw-settings-search-searchable-content

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchConfigId | `any` | — | yes |  |
| productSearchConfigs | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| edit-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onShowExampleModal` | |
| `onCloseExampleModal` | |
| `onAddNewConfig` | |
| `createNewConfigItem` | |
| `getConfigFieldDefault` | |
| `onResetToDefault` | |
| `onChangeTab` | |
| `loadData` | |
| `getProductSearchFieldsList` | |
| `saveConfig` | |
| `deleteConfig` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productSearchFieldRepository` | |
| `productSearchFieldCriteria` | |
| `isListEmpty` | |
| `getProductSearchFieldColumns` | |
| `storefrontEsEnable` | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
            <sw-settings-search-searchable-content-general
                v-if="active === tabNames.generalTab"
                :is-empty="isListEmpty"
                :is-loading="isLoading"
                :columns="getProductSearchFieldColumns"
                :repository="productSearchFieldRepository"
                :search-configs="searchConfigFields"
                :field-configs="fieldConfigs"
                @data-load="loadData"
                @config-save="saveConfig"
            />
            {% endblock %}

            <sw-settings-search-searchable-content-customfields
                v-if="active === tabNames.customTab"
```

### Example 2
Source: `sw-settings-search/view/sw-settings-search-view-general/sw-settings-search-view-general.html.twig`
```twig
    <sw-settings-search-searchable-content
        :product-search-configs="productSearchConfigs"
        :search-config-id="searchConfigId"
    />
    {% endblock %}

    {% block sw_settings_search_excluded_search_terms_card %}
    <sw-settings-search-excluded-search-terms
        :search-configs="productSearchConfigs"
        :is-excluded-terms-loading="isLoading"
        @data-load="loadData"
    />
    {% endblock %}
</div>
{% endblock %}
```
