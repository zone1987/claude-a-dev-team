# sw-cms-detail

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyedComponent` | |
| `setPageContext` | |
| `resetCmsPageState` | |
| `getDefaultFolderId` | |
| `loadPage` | |
| `hydratePage` | |
| `restoreActiveBlock` | |
| `updateDataMapping` | |
| `onDeviceViewChange` | |
| `setSelectedBlock` | |
| `onChangeLanguage` | |
| `abortOnLanguageChange` | |
| `hasUnsavedChanges` | |
| `saveOnLanguageChange` | |
| `loadDemoProduct` | |
| `loadDemoCategory` | |
| `loadDemoCategoryProducts` | |
| `onDemoEntityChange` | |
| `onAddSection` | |
| `onCloseBlockConfig` | |
| `pageConfigOpen` | |
| `saveFinish` | |
| `onPageSave` | |
| `debouncedPageSave` | |
| `onSave` | |
| `onSaveEntity` | |
| `addError` | |
| `getError` | |
| `getSlotValidations` | |
| `pageIsValid` | |
| `missingFieldsValidation` | |
| `listingPageValidation` | |
| `pageSectionCountValidation` | |
| `slotValidation` | |
| `deleteEntityAndRequiredConfigKey` | |
| `checkRequiredSlotConfigField` | |
| `updateSectionAndBlockPositions` | |
| `updateBlockPositions` | |
| `onPageUpdate` | |
| `onBlockDuplicate` | |
| `onSectionDuplicate` | |
| `onPageTypeChange` | |
| `processProductListingType` | |
| `processProductDetailType` | |
| `processBlock` | |
| `processElements` | |
| `checkSlotMappings` | |
| `isProductPageElement` | |
| `onOpenLayoutAssignment` | |
| `openLayoutAssignmentModal` | |
| `closeLayoutAssignmentModal` | |
| `onOpenLayoutSetAsDefault` | |
| `onCloseLayoutSetAsDefault` | |
| `onConfirmLayoutSetAsDefault` | |
| `setDefaultLayout` | |
| `onCloseMissingElementModal` | |
| `onSaveMissingElementModal` | |
| `onChangeDontRemindCheckbox` | |
| `onClickBack` | |
| `resetRelatedStores` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `pageRepository` | |
| `sectionRepository` | |
| `blockRepository` | |
| `slotRepository` | |
| `defaultFolderRepository` | |
| `cmsBlocks` | |
| `productRepository` | |
| `cmsStageClasses` | |
| `cmsPageTypeSettings` | |
| `blockConfigDefaults` | |
| `tooltipSave` | |
| `addBlockTitle` | |
| `pageHasSections` | |
| `loadPageCriteria` | |
| `demoProductCriteria` | |
| `currentDeviceView` | |
| `isProductPage` | |
| `requiredFieldErrors` | |
| `pageErrors` | |
| `hasPageErrors` | |
| `pageType` | |
| `layoutVersionContext` | |
| `pageNameError` | |
| `pageSectionsError` | |
| `pageBlocksError` | |
| `pageSlotsError` | |
| `pageSlotConfigError` | |

## Examples

### Basic Usage
```twig
<sw-cms-detail>
    <!-- content -->
</sw-cms-detail>
```
