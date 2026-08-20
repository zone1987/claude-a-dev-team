# sw-property-option-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| propertyGroup | `any` | — | yes |  |
| optionRepository | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `onSearch` | |
| `onGridSelectionChanged` | |
| `onOptionDelete` | |
| `onSingleOptionDelete` | |
| `onDeleteOptions` | |
| `onAddOption` | |
| `onCancelOption` | |
| `onSaveOption` | |
| `saveGroupLocal` | |
| `saveGroupRemote` | |
| `refreshOptionList` | |
| `onOptionEdit` | |
| `getGroupColumns` | |
| `checkEmptyState` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isSystemLanguage` | |
| `currentLanguage` | |
| `allowInlineEdit` | |
| `tooltipAdd` | |
| `disableAddButton` | |
| `useNaturalNameSorting` | |
| `dataSource` | |

## Examples

### Example 1
Source: `sw-property/page/sw-property-detail/sw-property-detail.html.twig`
```twig
                <sw-property-option-list
                    v-if="propertyGroup"
                    ref="optionListing"
                    :is-loading="isLoading || undefined"
                    :option-repository="optionRepository"
                    :property-group="propertyGroup"
                />
                {% endblock %}

                {% block sw_property_detail_custom_field_sets %}
                <mt-card
                    v-if="showCustomFields"
                    position-identifier="sw-property-detail"
                    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                >
```
