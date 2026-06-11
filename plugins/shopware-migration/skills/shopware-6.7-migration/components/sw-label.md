# sw-label

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `''` | no | Valid: `info`, `danger`, `success`, `warning`, `neutral`, `neutral-reversed`, `primary` |
| size | `any` | `'default'` | no | Valid: `small`, `medium`, `default` |
| appearance | `any` | `'default'` | no | Valid: `default`, `pill`, `circle`, `badged` |
| ghost | `any` | `false` | no |  |
| caps | `any` | `false` | no |  |
| dismissable | `any` | `true` | no |  |
| light | `any` | `false` | no |  |
| onDismiss | `any` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| dismiss-icon | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selected | — | |
| dismiss | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `labelClasses` | |
| `showDismissable` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-label
    v-droppable="{ ...mergedDropConfig, data: { snippet, index, linePosition }}"
    v-draggable="{ ...mergedDragConfig, data: { snippet, index, linePosition }}"
    :dismissable="!isSelectionDisabled(snippet)"
    :size="size"
    @dismiss="onClickDismiss(index)"
>
    <span class="sw-select-selection-list__item">
        <slot
            name="label-property"
            v-bind="{ item: snippet, index, getLabelProperty }"
        >
            {{ getLabelProperty(snippet) }}
        </slot>
    </span>
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-label
    :dismissable="true"
    :size="size"
    @dismiss="onClickDismiss(index)"
>
    <span class="sw-select-selection-list__item">
        <slot
            name="label-property"
            v-bind="{ item: snippet, index }"
        >
            {{ getLabelProperty(snippet) }}
        </slot>
    </span>
</sw-label>
```

### Example 3
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-error/sw-bulk-edit-save-modal-error.html.twig`
```twig
<sw-label
    class="sw-bulk-edit-save-modal__icon"
    appearance="pill"
    variant="danger"
>
    <mt-icon
        name="regular-times-hexagon"
        size="30px"
    />
</sw-label>
```

### Example 4
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-success/sw-bulk-edit-save-modal-success.html.twig`
```twig
<sw-label
    class="sw-bulk-edit-save-modal__icon"
    appearance="pill"
    variant="success"
>
    <mt-icon
        name="regular-check-circle"
        size="30px"
    />
</sw-label>
```

### Example 5
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-process/sw-bulk-edit-save-modal-process.html.twig`
```twig
<sw-label
    class="sw-bulk-edit-save-modal__icon"
    appearance="pill"
    variant="info"
>
    <sw-loader
        class="sw-bulk-edit-save-modal__loading-icon"
        size="30px"
    />
</sw-label>
```
