# mt-text-editor

> Rich text editor with formatting toolbar (bold, italic, lists, links, etc.).

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | — | |
| update:codeMode | — | |

## Examples

### Example 1
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
    <mt-text-editor
        v-else
        :key="category.id + 'description-meteor'"
        v-model="category.description"
        class="sw-category-detail-base__description"
        type="textarea"
        :disabled="!acl.can('category.editor')"
        sanitize-input
        sanitize-field-name="category_translation.description"
        :label="$tc('sw-category.base.menu.descriptionLabel')"
        :placeholder="$tc('sw-category.base.menu.descriptionPlaceholder')"
    />
    {% endblock %}
</mt-card>
{% endblock %}
```

### Example 2
Source: `sw-cms/elements/text/config/sw-cms-el-config-text.html.twig`
```twig
                <mt-text-editor
                    v-else
                    :key="isInherited + '-meteor'"
                    :disabled="isInherited"
                    :model-value="element.config.content.value"
                    :custom-buttons="customTextEditorButtons"
                    @update:model-value="onInput"
                />

                <template #preview="{ demoValue }">
                    <div class="sw-cms-el-config-text__mapping-preview">
                        <div v-html="$sanitize(demoValue)"></div>
                    </div>
                </template>
            </sw-cms-mapping-field>
```

### Example 3
Source: `sw-cms/elements/text/component/sw-cms-el-text.html.twig`
```twig
    <mt-text-editor
        v-else
        :model-value="element.config.content.value"
        :custom-buttons="customTextEditorButtons"
        is-inline-edit
        @update:model-value="onInput"
    />
</div>
{% endblock %}

```

### Example 4
Source: `sw-product/component/sw-product-basic-form/sw-product-basic-form.html.twig`
```twig
        <mt-text-editor
            v-else
            :key="'meteor-' + isInherited"
            :placeholder="placeholder(product, 'description', $tc('sw-product.basicForm.placeholderDescriptionLong'))"
            :error="productDescriptionError"
            :disabled="isInherited || !allowEdit"
            :model-value="currentValue"
            sanitize-input
            sanitize-field-name="product_translation.description"
            @update:model-value="updateCurrentValue"
        />
    </template>
</sw-inherit-wrapper>
{% endblock %}

```

### Example 5
Source: `sw-manufacturer/page/sw-manufacturer-detail/sw-manufacturer-detail.html.twig`
```twig
    <mt-text-editor
        v-else
        v-model="manufacturer.description"
        :label="$tc('sw-manufacturer.detail.labelDescription')"
        :placeholder="placeholder(manufacturer, 'description', $tc('sw-manufacturer.detail.placeholderDescription'))"
        name="description"
        sanitize-input
        sanitize-field-name="product_manufacturer_translation.description"
        :error="manufacturerDescriptionError"
        :disabled="!acl.can('product_manufacturer.editor') || undefined"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```
