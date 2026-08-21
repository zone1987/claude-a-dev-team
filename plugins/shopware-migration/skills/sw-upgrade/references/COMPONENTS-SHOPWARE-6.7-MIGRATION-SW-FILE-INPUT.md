# sw-file-input

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| maxFileSize | `any` | `null` | no |  |
| allowedMimeTypes | `any` | `null` | no |  |
| label | `any` | `null` | no |  |
| value | `any` | — | no |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| caption-label | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `beforeUnmountComponent` | |
| `onChooseButtonClick` | |
| `onRemoveIconClick` | |
| `onFileInputChange` | |
| `setSelectedFile` | |
| `checkFileSize` | |
| `checkFileType` | |
| `onDragEnter` | |
| `onDragLeave` | |
| `stopEventPropagation` | |
| `onDrop` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `id` | |
| `isDragActiveClass` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-csv-page/sw-import-export-new-profile-wizard-csv-page.html.twig`
```twig
<sw-file-input
    v-model:value="csvFile"
    :allowed-mime-types="['text/csv']"
    :label="$tc('sw-import-export.profile.csvUploadText')"
    class="sw-import-export-new-profile-wizard-csv-page__file-upload"
    @update:value="onFileChange"
>
    <template #caption-label>
        {{ $tc('sw-import-export.importer.labelUploadCaption') }}
    </template>
</sw-file-input>
```

### Example 2
Source: `sw-import-export/component/sw-import-export-importer/sw-import-export-importer.html.twig`
```twig
<sw-file-input
    :key="isLoading"
    v-model:value="importFile"
>
    <template #caption-label>
        {{ $tc('sw-import-export.importer.labelUploadCaption') }}
    </template>
</sw-file-input>
```
