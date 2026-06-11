# sw-confirm-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| compact | `any` | `false` | no |  |
| preventEmptySubmit | `any` | `false` | no |  |
| required | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| error | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| remove-error | — | |
| blur | — | |
| submit-cancel | — | |
| input | — | |

## Methods

| Method | Description |
|--------|-------------|
| `removeActionButtons` | |
| `onStartEditing` | |
| `onBlurField` | |
| `cancelSubmit` | |
| `onCancelFromKey` | |
| `onCancelSubmit` | |
| `submitValue` | |
| `onSubmitFromKey` | |
| `onSubmitValue` | |
| `onInput` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `confirmFieldClasses` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
                <sw-confirm-field
                    v-if="editable"
                    ref="inlineEditFieldName"
                    :disabled="!acl.can('media.creator')"
                    compact
                    :value="mediaFolder.name"
                    :error="mediaFolderNameError"
                    @input="onChangeFolderName"
                />
                <template v-else>
                    {{ mediaFolder.name }}
                </template>
            </sw-media-quickinfo-metadata-item>

            <sw-media-quickinfo-metadata-item
```

### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldName"
        class="sw-media-quickinfo-metadata-name"
        :disabled="!acl.can('media.editor')"
        compact
        :value="item.fileName"
        :error="fileNameError"
        @input="onChangeFileName"
        @remove-error="onRemoveFileNameError"
    /><template v-else>
        {{ item.fileName }}
    </template>
</sw-media-quickinfo-metadata-item>

```

### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldTitle"
        :disabled="!acl.can('media.editor')"
        compact
        :placeholder="placeholder(item, 'title', $t('sw-media.sidebar.metadata.title'))"
        :value="item.title"
        @input="onSubmitTitle"
    />
    <template v-else>
        {{ placeholder(item, 'title') }}
    </template>
</sw-media-quickinfo-metadata-item>

<sw-media-quickinfo-metadata-item
```

### Example 4
Source: `sw-order/component/sw-order-inline-field/sw-order-inline-field.html.twig`
```twig
        <sw-confirm-field
            :value="value"
            :required="required"
            @input="onInput"
        />
    </slot>
    <span v-else>
        {{ displayValue }}
    </span>
</div>
{% endblock %}

```
