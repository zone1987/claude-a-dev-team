# sw-self-maintained-extension-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `changeExtensionStatus` | |
| `installAndActivateExtension` | |
| `installExtension` | |
| `activateExtension` | |
| `deactivateExtension` | |
| `removeExtension` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `extensionCardClasses` | |
| `permissions` | |
| `isInstalled` | |

## Examples

### Basic Usage
```twig
<sw-self-maintained-extension-card
    extension="..."
>
    <!-- content -->
</sw-self-maintained-extension-card>
```
