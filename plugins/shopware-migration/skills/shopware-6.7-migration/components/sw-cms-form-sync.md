# sw-cms-form-sync

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| element | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createFieldWatcher` | |
| `createWatcher` | |
| `fieldChangeHandler` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `cmsElements` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-page-form/sw-cms-page-form.html.twig`
```twig
<sw-cms-form-sync :element="element">
    <component
        :is="cmsElements[element.type].configComponent"
        :element="element"
        :element-data="cmsElements[element.type]"
        @element-update="elementUpdate"
    />
</sw-cms-form-sync>
```
