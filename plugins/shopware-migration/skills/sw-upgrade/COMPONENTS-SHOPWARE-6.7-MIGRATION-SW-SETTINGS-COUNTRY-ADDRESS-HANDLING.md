# sw-settings-country-address-handling

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| country | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onDragStart` | |
| `onDragEnter` | |
| `onDrop` | |
| `onDropEnd` | |
| `moveToNewPosition` | |
| `addNewLineAt` | |
| `swapPosition` | |
| `change` | |
| `customerLabel` | |
| `onChangeCustomer` | |
| `resetMarkup` | |
| `openSnippetModal` | |
| `onCloseModal` | |
| `getSnippets` | |
| `renderFormattingAddress` | |
| `getLabelProperty` | |
| `updateCountry` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customerCriteria` | |
| `dragConf` | |
| `addressFormat` | |
| `hasDefaultPostalCodePattern` | |
| `disabledAdvancedPostalCodePattern` | |

## Examples

### Basic Usage
```twig
<sw-settings-country-address-handling
    country="..."
    isLoading="..."
>
    <!-- content -->
</sw-settings-country-address-handling>
```
