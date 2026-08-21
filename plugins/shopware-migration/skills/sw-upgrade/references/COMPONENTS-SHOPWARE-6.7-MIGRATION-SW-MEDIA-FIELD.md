# sw-media-field

> Media selection field for picking images/files from the media library.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| label | `any` | `null` | no |  |
| defaultFolder | `any` | `null` | no |  |
| fileAccept | `any` | `'*/*'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchTermChange` | |
| `fetchItem` | |
| `fetchSuggestions` | |
| `onTogglePicker` | |
| `mediaItemChanged` | |
| `removeLink` | |
| `computePickerPositionAndStyle` | |
| `toggleUploadField` | |
| `exposeNewId` | |
| `showLabel` | |
| `onPageChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaId` | |
| `mediaRepository` | |
| `popoverConfig` | |
| `mediaFieldClasses` | |
| `toggleButtonLabel` | |
| `suggestionCriteria` | |

## Examples

### Example 1
Source: `sw-settings-document/page/sw-settings-document-detail/sw-settings-document-detail.html.twig`
```twig
    <sw-media-field
        :value="documentConfig.logoId"
        @update:value="(v) => documentConfig.logoId = v"
        name="sw-field--documentConfig-logoId"
        :disabled="!acl.can('document.editor')"
        :label="$tc('sw-settings-document.detail.labelOptionMedia')"
    />
</div>
{% endblock %}

{% block sw_settings_document_detail_content_field_file_name_prefix %}
<div class="sw-settings-document-detail__field_file_name_prefix">

    <mt-text-field
        v-model="documentConfig.filenamePrefix"
```
