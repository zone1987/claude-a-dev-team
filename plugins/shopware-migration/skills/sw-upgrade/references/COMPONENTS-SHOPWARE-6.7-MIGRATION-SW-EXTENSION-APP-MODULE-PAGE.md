# sw-extension-app-module-page

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| appName | `any` | — | yes |  |
| moduleName | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `translate` | |
| `onContentLoaded` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentLocale` | |
| `fallbackLocale` | |
| `appDefinition` | |
| `moduleDefinition` | |
| `showSmartBar` | |
| `suspend` | |
| `heading` | |
| `entryPoint` | |
| `origin` | |
| `loadedMessage` | |

## Examples

### Basic Usage
```twig
<sw-extension-app-module-page
    appName="..."
>
    <!-- content -->
</sw-extension-app-module-page>
```
