# sw-snippet-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| snippet | `any` | — | yes |  |
| fieldType | `any` | `'text'` | no | Valid: `text`, `textarea` |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updatePlaceholderValueToSnippetTranslation` | |
| `getTranslationByLocale` | |
| `getSystemDefaultLocale` | |
| `openEditModal` | |
| `closeEditModal` | |
| `onSave` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `snippetSetRepository` | |
| `languageRepository` | |
| `languageCriteria` | |
| `textField` | |
| `textareaField` | |

## Examples

### Basic Usage
```twig
<sw-snippet-field
    snippet="..."
>
    <!-- content -->
</sw-snippet-field>
```
