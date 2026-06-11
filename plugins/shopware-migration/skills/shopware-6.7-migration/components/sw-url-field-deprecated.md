# sw-url-field-deprecated

> **Deprecated in 6.7** — Use `mt-url-field` instead. Will be removed in 6.8.
> See [mt-url-field](mt-url-field.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-url-field>` | `<mt-url-field>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| error | `any` | `null` | no |  |
| omitUrlHash | `any` | `false` | no |  |
| omitUrlSearch | `any` | `false` | no |  |
| addTrailingSlash | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onBlur` | |
| `checkInput` | |
| `handleEmptyUrl` | |
| `validateCurrentValue` | |
| `changeMode` | |
| `getURLInstance` | |
| `getSSLMode` | |
| `setInvalidUrlError` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `prefixClass` | |
| `urlPrefix` | |
| `url` | |
| `combinedError` | |
| `unicodeUriFilter` | |

## Examples

### Basic Usage
```twig
<sw-url-field-deprecated>
    <!-- content -->
</sw-url-field-deprecated>
```
