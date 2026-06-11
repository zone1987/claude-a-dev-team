# sw-category-entry-point-overwrite-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannels | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| cancel | — | |
| confirm | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onConfirm` | |

## Examples

### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-category-entry-point-overwrite-modal
    v-if="showEntryPointOverwriteModal"
    :sales-channels="entryPointOverwriteSalesChannels"
    @cancel="cancelEntryPointOverwrite"
    @confirm="confirmEntryPointOverwrite"
/>
{% endblock %}

{% block sw_landing_page_content_view %}
<sw-landing-page-view
    v-if="landingPage"
    ref="landingPageView"
    :is-loading="isLoading"
/>
{% endblock %}
```
