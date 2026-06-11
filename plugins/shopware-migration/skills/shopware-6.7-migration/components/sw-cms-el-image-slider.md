# sw-cms-el-image-slider

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| activeMedia | `null \| null` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| active-image-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setSliderItem` | |
| `activeButtonClass` | |
| `setSliderArrowItem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `gridAutoRows` | |
| `uploadTag` | |
| `sliderItems` | |
| `displayModeClass` | |
| `styles` | |
| `outsideNavArrows` | |
| `navDotsClass` | |
| `navArrowsClass` | |
| `verticalAlignStyle` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-cms/elements/image-gallery/component/sw-cms-el-image-gallery.html.twig`
```twig
    <sw-cms-el-image-slider
        :element="element"
        :active-media="activeMedia"
        @active-image-change="onChangeGalleryImage"
    />
    {% endblock %}
</div>
{% endblock %}

```
