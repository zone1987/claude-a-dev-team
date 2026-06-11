# sw-image-slider

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| images | `any` | — | yes |  |
| canvasWidth | `any` | `0` | no |  |
| canvasHeight | `any` | `0` | no |  |
| gap | `any` | `20` | no |  |
| elementPadding | `any` | `0` | no |  |
| navigationType | `any` | `'arrow'` | no |  |
| enableDescriptions | `any` | `false` | no |  |
| overflow | `any` | `'hidden'` | no |  |
| rewind | `any` | `false` | no |  |
| bordered | `any` | `true` | no |  |
| rounded | `any` | `true` | no |  |
| autoWidth | `any` | `false` | no |  |
| itemPerPage | `any` | `1` | no |  |
| initialIndex | `any` | `0` | no |  |
| arrowStyle | `any` | `'inside'` | no |  |
| buttonStyle | `any` | `'outside'` | no |  |
| displayMode | `any` | `'cover'` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| image-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `setCurrentPageNumber` | |
| `isImageObject` | |
| `hasValidDescription` | |
| `getImage` | |
| `imageAlt` | |
| `goToPreviousImage` | |
| `goToNextImage` | |
| `elementClasses` | |
| `elementStyles` | |
| `imageClasses` | |
| `borderStyles` | |
| `onSetCurrentItem` | |
| `isHiddenItem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `totalPage` | |
| `remainder` | |
| `buttonList` | |
| `wrapperStyles` | |
| `componentStyles` | |
| `containerStyles` | |
| `scrollableContainerStyles` | |
| `imageStyles` | |
| `buttonClasses` | |
| `showButtons` | |
| `showArrows` | |

## Examples

### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-modal-detail/sw-sales-channel-modal-detail.html.twig`
```twig
        <sw-image-slider
            class="sw-sales-channel-modal-detail__screenshot"
            :images="detailType.screenshotUrls || []"
            :canvas-width="580"
            :canvas-height="272"
            overflow="visible"
            navigation-type="arrow"
            enable-descriptions
        />
    </div>
    {% endblock %}
</div>
{% endblock %}

```
