# sw-media-quickinfo-metadata-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| labelName | `any` | — | yes |  |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-name"
    :class="nameItemClasses"
    :label-name="$tc('sw-media.sidebar.metadata.name')"
    :truncated="false"
>
    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldName"
        :disabled="!acl.can('media.creator')"
        compact
        :value="mediaFolder.name"
        :error="mediaFolderNameError"
        @input="onChangeFolderName"
    />
```

### Example 2
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-createdAt"
    :label-name="$tc('sw-media.sidebar.metadata.createdAt')"
>
    {{ createdAt }}
</sw-media-quickinfo-metadata-item>
```

### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-name"
    :class="fileNameClasses"
    :label-name="$t('sw-media.sidebar.metadata.name')"
    :truncated="false"
>

    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldName"
        class="sw-media-quickinfo-metadata-name"
        :disabled="!acl.can('media.editor')"
        compact
        :value="item.fileName"
        :error="fileNameError"
```

### Example 4
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-file-type"
    :label-name="$t('sw-media.sidebar.metadata.fileType')"
>
    {{ item.fileExtension.toUpperCase() }}
</sw-media-quickinfo-metadata-item>
```
