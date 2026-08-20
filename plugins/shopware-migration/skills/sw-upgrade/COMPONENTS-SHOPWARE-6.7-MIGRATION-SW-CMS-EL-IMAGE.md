# sw-cms-el-image

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateDemoValue` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `displayModeClass` | |
| `styles` | |
| `imgStyles` | |
| `horizontalAlign` | |
| `mediaUrl` | |
| `assetFilter` | |
| `mediaConfigValue` | |

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
