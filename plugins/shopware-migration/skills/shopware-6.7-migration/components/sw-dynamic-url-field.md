# sw-dynamic-url-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getEmptyCategoryCollection` | |
| `getCategoryCollection` | |
| `parseLink` | |
| `replaceCategorySelection` | |
| `removeCategorySelection` | |
| `prepareLink` | |
| `removeLink` | |
| `onSelectFieldChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `seoUrlReplacePrefix` | |
| `entityFilter` | |
| `categoryRepository` | |
| `linkCategoryOptions` | |

## Examples

### Example 1
Source: `sw-cms/elements/image/config/sw-cms-el-config-image.html.twig`
```twig
        <sw-dynamic-url-field
            v-model:value="element.config.url.value"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>

<sw-cms-inherit-wrapper
    field="ariaLabel"
    :element="element"
    :label="$t('sw-cms.elements.image.config.label.ariaLabel')"
>
    <template #default="{ isInherited }">
        <mt-text-field
            v-model="element.config.ariaLabel.value"
```
