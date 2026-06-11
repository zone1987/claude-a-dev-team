# sw-settings-document-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| documentConfigId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `loadAvailableSalesChannel` | |
| `showOption` | |
| `onChangeType` | |
| `onChangeSalesChannel` | |
| `saveFinish` | |
| `onSave` | |
| `onCancel` | |
| `createSalesChannelSelectOptions` | |
| `onRemoveDocumentType` | |
| `onAddDocumentType` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `countryRepository` | |
| `documentBaseConfigCriteria` | |
| `documentBaseConfigRepository` | |
| `documentTypeRepository` | |
| `salesChannelRepository` | |
| `documentBaseConfigSalesChannelRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `documentBaseConfig` | |
| `documentBaseConfigNameError` | |
| `documentBaseConfigDocumentTypeIdError` | |
| `showCustomFields` | |
| `fileTypesSelected` | |
| `documentCriteria` | |

## Examples

### Basic Usage
```twig
<sw-settings-document-detail>
    <!-- content -->
</sw-settings-document-detail>
```
