# sw-extension-teaser-popover

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| positionIdentifier | `any` | — | yes |  |
| component | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onMouseEnterTrigger` | |
| `onMouseEnterContent` | |
| `onMouseLeaveContent` | |
| `onMouseLeaveTrigger` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `popoverComponent` | |
| `isInsideComponent` | |

## Examples

### Example 1
Source: `sw-cms/blocks/app/app-renderer/preview/sw-cms-block-app-preview-renderer.html.twig`
```twig
    <sw-extension-teaser-popover
        v-else-if="appName === 'SwagRecommendations'"
        position-identifier="sw-cms-block-3d-object"
    />

    <section
        v-else
        class="sw-cms-block-app-preview-renderer__fallback-preview"
    >
        <h2>
            {{ $tc(appName) }}
        </h2>
    </section>
</div>
{% endblock %}
```

### Example 2
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
    <sw-extension-teaser-popover
        position-identifier="sw-media-generate-image-button"
    />

    {% block sw_media_index_create_folder %}
    <mt-button
        v-if="editable || allowCreateFolder"
        v-tooltip="{
            message: $tc('sw-privileges.tooltip.warning'),
            disabled: acl.can('media.creator'),
            showOnDisabledElements: true
        }"
        :disabled="!acl.can('media.creator') || disabled"
        class="sw-media-index__create-folder-action"
        ghost
```

### Example 3
Source: `sw-settings-rule/view/sw-settings-rule-detail-base/sw-settings-rule-detail-base.html.twig`
```twig
    <sw-extension-teaser-popover
        position-identifier="sw-settings-rule-preview-mode-switch"
    />
</template>

<div
    v-if="showProductStreamIndexingWarning"
    class="sw-settings-rule-detail-base__product-stream-warning"
>
    <mt-banner
        variant="attention"
        :title="$tc('sw-settings-rule.detail.productStreamIndexingWarning.title')"
    >
        <p>
            {{ $tc('sw-settings-rule.detail.productStreamIndexingWarning.message') }}
```

### Example 4
Source: `sw-product/component/sw-product-add-properties-modal/sw-product-add-properties-modal.html.twig`
```twig
                <sw-extension-teaser-popover
                    position-identifier="sw-product-add-properties-assistant-button"
                />
            </div>
            {% endblock %}
        </template>
    </sw-property-search>
    {% endblock %}
    {% endblock %}
</div>
{% endblock %}

<template #modal-footer>
    {% block sw_product_add_properties_modal_button_cancel %}
    <mt-button
```

### Example 5
Source: `sw-product/component/sw-product-basic-form/sw-product-basic-form.html.twig`
```twig
        <sw-extension-teaser-popover
            position-identifier="sw-product-generated-description-button"
        />
    </div>
</div>
{% endblock %}

```
