# sw-search-bar-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | no |  |
| type | `any` | — | yes |  |
| index | `any` | — | yes |  |
| column | `any` | — | yes |  |
| searchTerm | `any` | `null` | no |  |
| entityIconColor | `any` | — | yes |  |
| entityIconName | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `registerEvents` | |
| `removeEvents` | |
| `checkActiveState` | |
| `onEnter` | |
| `onMouseEnter` | |
| `onClickSearchResult` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `searchTypes` | |
| `moduleManifest` | |
| `detailRoute` | |
| `displayValue` | |
| `componentClasses` | |
| `moduleName` | |
| `routeName` | |
| `iconName` | |
| `iconColor` | |
| `shortcut` | |
| `productDisplayName` | |
| `currentUser` | |
| `mediaNameFilter` | |

## Examples

### Basic Usage
```twig
<sw-search-bar-item
    type="..."
    index="..."
>
    <!-- content -->
</sw-search-bar-item>
```
