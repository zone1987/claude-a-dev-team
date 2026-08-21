# sw-text-editor-toolbar-button-link

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| editor | `any` | — | yes |  |
| button | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `openLinkModal` | |
| `parseLink` | |
| `parseButtonClass` | |
| `applyLink` | |
| `removeLink` | |
| `isLink` | |
| `prepareLink` | |
| `prepareClass` | |
| `prepareTarget` | |
| `addProtocolToLink` | |
| `getCategoryCollection` | |
| `getEmptyCategoryCollection` | |
| `replaceCategorySelection` | |
| `removeCategorySelection` | |
| `onSelectFieldChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `linkOptions` | |
| `buttonVariantList` | |
| `seoUrlReplacePrefix` | |
| `categoryRepository` | |
| `showOpenInNewTabToggle` | |
| `productEntityFilter` | |
| `entityFilter` | |

## Examples

### Basic Usage
```twig
<sw-text-editor-toolbar-button-link
    editor="..."
    button="..."
>
    <!-- content -->
</sw-text-editor-toolbar-button-link>
```
