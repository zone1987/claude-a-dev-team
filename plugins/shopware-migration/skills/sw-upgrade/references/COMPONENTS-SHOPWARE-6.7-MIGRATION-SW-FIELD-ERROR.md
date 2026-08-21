# sw-field-error

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| error | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `formatParameters` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `errorMessage` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-download-form/sw-product-download-form.html.twig`
```twig
<sw-field-error :error="error" />
```

### Example 2
Source: `sw-product-stream/component/sw-product-stream-filter/sw-product-stream-filter.html.twig`
```twig
<sw-field-error :error="currentError" />
```
