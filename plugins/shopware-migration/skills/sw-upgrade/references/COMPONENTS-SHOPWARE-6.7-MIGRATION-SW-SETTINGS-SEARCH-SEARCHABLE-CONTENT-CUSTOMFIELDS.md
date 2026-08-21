# sw-settings-search-searchable-content-customfields

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isEmpty | `any` | — | yes |  |
| columns | `any` | — | yes |  |
| repository | `any` | — | yes |  |
| searchConfigs | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| config-add | — | |
| data-load | — | |
| config-save | — | |
| config-delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `showCustomFieldWithSet` | |
| `getMatchingCustomFields` | |
| `onSelectCustomField` | |
| `onAddField` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onResetRanking` | |
| `onRemove` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customFieldRepository` | |
| `customFieldFilteredCriteria` | |
| `customFieldCriteria` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
            <sw-settings-search-searchable-content-customfields
                v-if="active === tabNames.customTab"
                :is-empty="isListEmpty"
                :is-loading="isLoading"
                :columns="getProductSearchFieldColumns"
                :repository="productSearchFieldRepository"
                :search-configs="searchConfigFields"
                @data-load="loadData"
                @config-add="onAddNewConfig"
                @config-save="saveConfig"
                @config-delete="deleteConfig"
            />
        </template>
    </sw-tabs>
    {% endblock %}
```
