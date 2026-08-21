# sw-media-display-options

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| presentation | `any` | `'medium-preview'` | no | Valid: `small-preview`, `medium-preview`, `large-preview`, `list-preview` |
| sorting | `any` | — | no |  |
| hidePresentation | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-sorting-change | — | |
| media-presentation-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSortingChanged` | |
| `onPresentationChanged` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sortingConCat` | |
| `sortOptions` | |
| `previewOptions` | |
| `presentationOptions` | |
| `sortOptionsSelect` | |

## Examples

### Example 1
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
<sw-media-display-options
    class="sw-media-library__display-options"
    :presentation="presentation"
    :sorting="sorting"
    :hide-presentation="compact"
    :disabled="disabled"
    @media-presentation-change="presentation = $event"
    @media-sorting-change="sorting = $event"
/>

<sw-extension-teaser-popover
    position-identifier="sw-media-generate-image-button"
/>

{% block sw_media_index_create_folder %}
```
