# sw-product-variant-info

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variations | `any` | `null` | no |  |
| highlighted | `any` | `false` | no |  |
| searchTerm | `any` | `''` | no |  |
| titleTerm | `any` | `null` | no |  |
| showTooltip | `any` | `true` | no |  |
| ommitParenthesis | `any` | `false` | no |  |
| seperator | `any` | `'|'` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getFirstSlot` | |
| `setHelpText` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productName` | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-product-variant-info
    :variations="item.variation"
    :show-tooltip="false"
>
    <sw-settings-search-live-search-keyword
        :text="(item.name || item.translated.name)"
        :search-term="liveSearchTerm"
    />
</sw-product-variant-info>
```

### Example 2
Source: `sw-category/view/sw-category-detail-products/sw-category-detail-products.html.twig`
```twig
<sw-product-variant-info :variations="item.variation">
    {{ getItemName(item) }}
</sw-product-variant-info>
```

### Example 3
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
<sw-product-variant-info
    :variations="item.options"
    @click="onAbort"
>
    {{ item.translated.name }}
</sw-product-variant-info>
```

### Example 4
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-product-variant-info :variations="item.variation">
    {{ item.translated.name || item.name }}
</sw-product-variant-info>
```

### Example 5
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-product-variant-info :variations="item.variation">
    {{ item.translated.name || item.name }}
</sw-product-variant-info>
```
