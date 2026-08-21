# sw-category-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| categoryId | `any` | `null` | no |  |
| landingPageId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `categoryCheckedElementsCount` | |
| `landingPageCheckedElementsCount` | |
| `registerListener` | |
| `onSearch` | |
| `checkViewport` | |
| `getAssignedCmsPage` | |
| `updateCmsPageDataMapping` | |
| `getAssignedCmsPageForLandingPage` | |
| `updateCmsPageDataMappingForLandingPage` | |
| `setLandingPage` | |
| `setCategory` | |
| `loadCustomFieldSet` | |
| `loadLandingPageCustomFieldSet` | |
| `onSaveCategories` | |
| `openChangeModal` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `cancelEdit` | |
| `resetCategory` | |
| `onChangeLanguage` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `saveFinish` | |
| `onSave` | |
| `checkForEntryPointOverwrite` | |
| `cancelEntryPointOverwrite` | |
| `confirmEntryPointOverwrite` | |
| `onSaveLandingPage` | |
| `addLandingPageSalesChannelError` | |
| `extractSlotOverrides` | |
| `getCmsPageOverrides` | |
| `deleteSpecifcKeys` | |
| `updateSeoUrls` | |
| `onLandingPageDelete` | |
| `onCategoryDelete` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `changesetGenerator` | |
| `showEmptyState` | |
| `identifier` | |
| `landingPageRepository` | |
| `categoryRepository` | |
| `cmsPageRepository` | |
| `landingPage` | |
| `category` | |
| `showEntryPointOverwriteModal` | |
| `cmsPage` | |
| `cmsPageState` | |
| `cmsPageId` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `customFieldSetLandingPageCriteria` | |
| `mediaRepository` | |
| `pageClasses` | |
| `tooltipSave` | |
| `landingPageTooltipSave` | |
| `tooltipCancel` | |
| `categoryCriteria` | |
| `landingPageCriteria` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
<sw-category-detail-menu v-bind="{ category, isLoading }" />
```
