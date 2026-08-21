# sw-settings-language-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| languageId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `checkTranslationCodeInheritance` | |
| `setParentTranslationCodeId` | |
| `onInputLanguage` | |
| `isLocaleAlreadyUsed` | |
| `onSave` | |
| `onCancel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `languageRepository` | |
| `isIsoCodeRequired` | |
| `languageHasName` | |
| `isNewLanguage` | |
| `usedLocaleCriteria` | |
| `allowSave` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `parentLanguageCriteria` | |
| `isSystemDefaultLanguageId` | |
| `inheritanceTooltipText` | |
| `showCustomFields` | |
| `languageLocaleIdError` | |
| `languageNameError` | |

## Examples

### Basic Usage
```twig
<sw-settings-language-detail>
    <!-- content -->
</sw-settings-language-detail>
```
