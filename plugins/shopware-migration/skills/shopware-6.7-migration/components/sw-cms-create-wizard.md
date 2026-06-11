# sw-cms-create-wizard

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-section-select | — | |
| wizard-complete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `goToStep` | |
| `getStepName` | |
| `onPageTypeSelect` | |
| `onSectionSelect` | |
| `onCompletePageCreation` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `visiblePageTypes` | |
| `currentPageType` | |
| `isCustomEntityType` | |
| `isCompletable` | |
| `customEntities` | |
| `pagePreviewMedia` | |
| `pagePreviewStyle` | |
| `assetFilter` | |
| `cmsPageStore` | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-create/sw-cms-create.html.twig`
```twig
<sw-cms-create-wizard
    :page="page"
    @on-section-select="onAddSection($event, 0)"
    @wizard-complete="onWizardComplete"
/>
{% endblock %}

```
