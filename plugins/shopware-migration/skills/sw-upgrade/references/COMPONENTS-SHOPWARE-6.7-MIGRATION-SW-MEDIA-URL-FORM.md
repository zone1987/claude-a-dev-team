# sw-media-url-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'inline'` | yes | Valid: `modal`, `inline` |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-url-form-submit | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `emitUrl` | |
| `onModalChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `urlObject` | |
| `hasInvalidInput` | |
| `invalidUrlError` | |
| `missingFileExtension` | |
| `fileExtension` | |
| `isValid` | |

## Examples

### Basic Usage
```twig
<sw-media-url-form
    variant="..."
>
    <!-- content -->
</sw-media-url-form>
```
