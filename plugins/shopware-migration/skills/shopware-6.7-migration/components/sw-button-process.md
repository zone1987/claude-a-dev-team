# sw-button-process

> Button with integrated progress/loading state visualization.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| processSuccess | `any` | — | yes |  |
| animationTimeout | `any` | `1250` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:processSuccess | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `contentVisibilityClass` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-button-process
    v-tooltip.bottom="tooltipSave"
    class="sw-settings-country-detail__save-action"
    :is-loading="isLoading"
    :process-success="isSaveSuccessful"
    :disabled="!country || !allowSave || undefined"
    variant="primary"
    @update:process-success="saveFinish"
    @click.prevent="onSave"
>
    {{ $tc('sw-settings-country.detail.buttonSave') }}
</sw-button-process>
```

### Example 2
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-button-process
    v-tooltip.bottom="tooltipSave"
    class="sw-settings-search__button-save"
    variant="primary"
    :disabled="!allowSave"
    :is-loading="isLoading"
    :process-success="isSaveSuccessful"
    @update:process-success="saveFinish"
    @click.prevent="onSaveSearchSettings"
>
    {{ $tc('global.default.save') }}
</sw-button-process>
```

### Example 3
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
<sw-button-process
    variant="primary"
    ghost
    class="sw-settings-search__search-index-rebuild-button"
    :is-loading="isRebuildInProgress"
    :disabled="isRebuildInProgress || !acl.can('product_search_config.editor')"
    :process-success="isRebuildSuccess"
    @update:process-success="buildFinish"
    @click="rebuildSearchIndex"
>
    {{ $tc('sw-settings-search.generalTab.buttonRebuildSearchIndex') }}
</sw-button-process>
```

### Example 4
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-button-process
    v-tooltip.bottom="tooltipSave"
    class="sw-settings-salutation-detail__save"
    :is-loading="isLoading"
    :process-success="isSaveSuccessful"
    :disabled="invalidKey || isKeyChecking || !allowSave || undefined"
    variant="primary"
    @update:process-success="saveFinish"
    @click="onSave"
>
    {{ $tc('sw-settings-salutation.general.buttonSave') }}
</sw-button-process>
```

### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-button-process
    class="sw-bulk-edit-product__save-action"
    variant="primary"
    :is-loading="isLoading"
    :process-success="isSaveSuccessful"
    :disabled="isLoading || !hasSelectedChanges || undefined"
    @click="openModal"
>
    {{ $tc('sw-bulk-edit.applyChanges') }}
</sw-button-process>
```
