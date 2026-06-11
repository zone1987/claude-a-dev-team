# sw-media-folder-content

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| startFolderId | `any` | `null` | no |  |
| selectedId | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selected | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getSubFolders` | |
| `getChildCount` | |
| `fetchParentFolder` | |
| `updateParentFolder` | |
| `emitInput` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `assetFilter` | |

## Examples

### Basic Usage
```twig
<sw-media-folder-content>
    <!-- content -->
</sw-media-folder-content>
```
