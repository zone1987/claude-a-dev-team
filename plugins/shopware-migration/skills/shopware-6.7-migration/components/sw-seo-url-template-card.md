# sw-seo-url-template-card

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchSeoUrlTemplates` | |
| `createSeoUrlTemplatesFromDefaultRoutes` | |
| `createVariableOptions` | |
| `getVariableOptions` | |
| `getLabel` | |
| `getPlaceholder` | |
| `onClickSave` | |
| `createSaveErrorNotification` | |
| `createSaveSuccessNotification` | |
| `onSelectInput` | |
| `onInput` | |
| `debouncedPreviewSeoUrlTemplate` | |
| `setErrorMessagesForEntity` | |
| `fetchSeoUrlPreview` | |
| `fetchSalesChannels` | |
| `onSalesChannelChanged` | |
| `getTemplatesForSalesChannel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `seoUrlTemplatesTemplateError` | |
| `salesChannelRepository` | |
| `salesChannelIsHeadless` | |

## Examples

### Example 1
Source: `sw-settings-seo/page/sw-settings-seo/sw-settings-seo.html.twig`
```twig
<sw-seo-url-template-card ref="seoUrlTemplateCard" />
```
