# sw-text-editor

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| isInlineEdit | `any` | `false` | no |  |
| verticalAlign | `any` | `''` | no |  |
| label | `any` | `''` | no |  |
| placeholder | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |
| allowInlineDataMapping | `any` | `false` | no |  |
| sanitizeInput | `any` | `false` | no |  |
| sanitizeFieldName | `any` | `null` | no |  |
| sanitizeInfoWarn | `any` | `false` | no |  |
| enableTransparentBackground | `any` | `false` | no |  |
| buttonConfig | `any` | — | no |  |
| error | `any` | `null` | no |  |

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
| `mountedComponent` | |
| `destroyedComponent` | |
| `keyListener` | |
| `onSelectionChange` | |
| `getPath` | |
| `toggleCodeEditor` | |
| `handleInsertDataMapping` | |
| `resetForeColor` | |
| `onToolbarCreated` | |
| `onToolbarDestroyed` | |
| `onTextStyleChange` | |
| `expandSelectionToNearestEndBracket` | |
| `expandSelectionToNearestStartBracket` | |
| `setSelection` | |
| `containsStartBracket` | |
| `containsEndBracket` | |
| `isInsideInlineMapping` | |
| `handleInsertTable` | |
| `setTablesResizable` | |
| `setTableResizable` | |
| `setTableSelectorListeners` | |
| `setTableListeners` | |
| `onSetLink` | |
| `onRemoveLink` | |
| `onClick` | |
| `onFocus` | |
| `onEnter` | |
| `fixWrongNodes` | |
| `hasDirectMinorElements` | |
| `setFocus` | |
| `removeFocus` | |
| `onDocumentClick` | |
| `onInput` | |
| `onContentChange` | |
| `onCopy` | |
| `onPaste` | |
| `emitContent` | |
| `emitHtmlContent` | |
| `getContentValue` | |
| `emptyCheck` | |
| `setWordCount` | |
| `onTableEdit` | |
| `onTableModify` | |
| `onTableDelete` | |
| `showLabel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `contentClasses` | |
| `verticalAlignStyle` | |
| `availableDataMappings` | |

## Examples

### Example 1
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
    <sw-text-editor
        v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
        :key="category.id + 'description'"
        v-model:value="category.description"
        class="sw-category-detail-base__description"
        type="textarea"
        :disabled="!acl.can('category.editor')"
        sanitize-input
        sanitize-field-name="category_translation.description"
        :label="$tc('sw-category.base.menu.descriptionLabel')"
        :placeholder="$tc('sw-category.base.menu.descriptionPlaceholder')"
    />
    <mt-text-editor
        v-else
        :key="category.id + 'description-meteor'"
```

### Example 2
Source: `sw-cms/elements/text/config/sw-cms-el-config-text.html.twig`
```twig
                <sw-text-editor
                    v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
                    :key="isInherited"
                    :value="element.config.content.value"
                    :disabled="isInherited"
                    :allow-inline-data-mapping="true"
                    :sanitize-info-warn="true"
                    enable-transparent-background
                    @update:value="onInput"
                    @blur="onBlur"
                />

                <mt-text-editor
                    v-else
                    :key="isInherited + '-meteor'"
```

### Example 3
Source: `sw-cms/elements/text/component/sw-cms-el-text.html.twig`
```twig
    <sw-text-editor
        v-else-if="!feature.isActive('METEOR_TEXT_EDITOR')"
        v-model:value="element.config.content.value"
        :disabled="disabled"
        :vertical-align="element.config.verticalAlign.value"
        :allow-inline-data-mapping="true"
        :is-inline-edit="true"
        sanitize-input
        sanitize-field-name="app_cms_block.template"
        enable-transparent-background
        @blur="onBlur"
        @update:value="onInput"
    />
    <mt-text-editor
        v-else
```

### Example 4
Source: `sw-product/component/sw-product-basic-form/sw-product-basic-form.html.twig`
```twig
        <sw-text-editor
            v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
            :key="isInherited"
            :placeholder="placeholder(product, 'description', $tc('sw-product.basicForm.placeholderDescriptionLong'))"
            :error="productDescriptionError"
            :disabled="isInherited || !allowEdit"
            :value="currentValue"
            sanitize-input
            sanitize-field-name="product_translation.description"
            @update:value="updateCurrentValue"
        />
        <mt-text-editor
            v-else
            :key="'meteor-' + isInherited"
            :placeholder="placeholder(product, 'description', $tc('sw-product.basicForm.placeholderDescriptionLong'))"
```

### Example 5
Source: `sw-manufacturer/page/sw-manufacturer-detail/sw-manufacturer-detail.html.twig`
```twig
    <sw-text-editor
        v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
        v-model:value="manufacturer.description"
        :label="$tc('sw-manufacturer.detail.labelDescription')"
        :placeholder="placeholder(manufacturer, 'description', $tc('sw-manufacturer.detail.placeholderDescription'))"
        name="description"
        sanitize-input
        sanitize-field-name="product_manufacturer_translation.description"
        :error="manufacturerDescriptionError"
        :disabled="!acl.can('product_manufacturer.editor') || undefined"
    />
    <mt-text-editor
        v-else
        v-model="manufacturer.description"
        :label="$tc('sw-manufacturer.detail.labelDescription')"
```
