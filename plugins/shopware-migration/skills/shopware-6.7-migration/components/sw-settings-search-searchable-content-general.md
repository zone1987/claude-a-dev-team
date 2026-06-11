# sw-settings-search-searchable-content-general

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isEmpty | `any` | — | yes |  |
| columns | `any` | — | yes |  |
| repository | `any` | — | yes |  |
| searchConfigs | `any` | — | no |  |
| fieldConfigs | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| data-load | — | |
| config-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `getMatchingFields` | |
| `onSelectField` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onInlineEditItem` | |
| `onResetRanking` | |
| `getConfigRankingDefault` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

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
