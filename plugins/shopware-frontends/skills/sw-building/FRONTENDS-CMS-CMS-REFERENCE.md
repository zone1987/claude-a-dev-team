# @shopware/cms-base-layer — Complete CMS reference

Version: **3.0.0**

Nuxt layer with Vue 3 components for rendering all Shopware CMS types (sections, blocks, elements).

---

## Contents

- [Integration as a Nuxt layer](#integration-as-a-nuxt-layer)
- [Core rendering components](#core-rendering-components)
- [Component resolver: `resolveCmsComponent`](#component-resolver-resolvecmscomponent)
- [Registering custom CMS components](#registering-custom-cms-components)
- [Complete component list](#complete-component-list)
- [Listing filter components](#listing-filter-components)
- [Sw* components (reusable UI)](#sw-components-reusable-ui)
- [Base UI components](#base-ui-components)
- [CMS composables in components](#cms-composables-in-components)
- [HTML-to-Vue renderer (`CmsElementText`)](#html-to-vue-renderer-cmselementtext)
- [3D content (`CmsBlockSpatialViewer`)](#3d-content-cmsblockspatialviewer)
- [Layout configuration](#layout-configuration)

## Integration as a Nuxt layer

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: ['@shopware/cms-base-layer'],
  // Prerequisite: @shopware/nuxt-module is registered as a module
})
```

The layer:
- Registers all CMS components **globally** (auto-import from `app/components/public/`)
- Enables auto-import of the Nuxt composables in cms-base files (fix for Nitro import transformations)
- Uses `@nuxt/image` for optimized images, `@tresjs/nuxt` for 3D content

---

## Core rendering components

### `<CmsPage :content="cmsPage" />`

Entry point for rendering a complete CMS page. Renders all sections dynamically.

```vue
<script setup>
import type { Schemas } from '#shopware'
const { page } = useListing()
// or: via useProductSearch / useCategorySearch / useLandingSearch with withCmsAssociations: true
</script>
<template>
  <CmsPage v-if="page?.cmsPage" :content="page.cmsPage" />
</template>
```

**Props:**
```ts
defineProps<{ content: Schemas["CmsPage"] }>()
```

**Internals:** Iterates `content.sections[]`, resolves the component name per section (`CmsSection${pascalCase(section.type)}`), renders via `h()`. Applies `getCmsLayoutConfiguration` for styles and CSS classes. Calls `createCategoryListingContext` when `routeName === 'frontend.navigation.page'`.

---

### `<CmsGenericBlock :content="block" />`

Renders a CMS block dynamically based on `block.type`.

```vue
<template>
  <CmsGenericBlock :content="block" />
</template>
```

**Props:**
```ts
defineProps<{ content: Schemas["CmsBlock"] }>()
```

**Internals:**
1. `resolveCmsComponent(block)` → resolves `CmsBlock${pascalCase(block.type)}`
2. Applies background styles and CSS classes (`getCmsLayoutConfiguration`)
3. Provides `slotCount` and `imageSizes` via `provide`
4. In `import.meta.dev`: console warning with a docs link when the component is missing

---

### `<CmsGenericElement :content="slot" />`

Renders a CMS element (slot) dynamically based on `slot.type`.

**Props:**
```ts
defineProps<{ content: Schemas["CmsSlot"] }>()
```

**Internals:**
1. `resolveCmsComponent(slot)` → resolves `CmsElement${pascalCase(slot.type)}`
2. Applies CSS classes/styles
3. In `import.meta.dev`: console warning when the element is missing

---

### `<CmsNoComponent :content="..." />`

Fallback component shown in dev mode when a block/element type is not implemented. Displays the missing component name.

---

## Component resolver: `resolveCmsComponent`

```ts
import { resolveCmsComponent } from '@shopware/composables'

const { resolvedComponent, componentName, isResolved, componentNameToResolve } =
  resolveCmsComponent(content)
```

| Returns | Type | Description |
|---|---|---|
| `resolvedComponent` | `Component \| string` | Resolved Vue component, or a string when not found |
| `componentName` | `string` | e.g. `"CmsElementText"` |
| `isResolved` | `boolean` | `true` when resolved to a real component |
| `componentNameToResolve` | `string` | Expected component name |

**Naming convention:** Shopware CMS type string → `CmsElement` / `CmsBlock` / `CmsSection` + PascalCase of the type.

Examples:
- Slot `type: "text"` → `CmsElementText`
- Block `type: "image-text"` → `CmsBlockImageText`
- Section `type: "default"` → `CmsSectionDefault`
- Section `type: "sidebar"` → `CmsSectionSidebar`

---

## Registering custom CMS components

### Custom CMS element

For a CMS slot type that does not exist in `cms-base-layer` yet or that should be overridden:

```vue
<!-- components/CmsElementMyCustomType.vue -->
<script setup lang="ts">
import { useCmsElementConfig } from '@shopware/composables'
import type { CmsSlot } from '#shopware'

const props = defineProps<{ content: CmsSlot }>()
const { getConfigValue } = useCmsElementConfig(props.content)

const myOption = getConfigValue('myCustomOption')
</script>
<template>
  <div>{{ content.data?.text }}</div>
</template>
```

Nuxt auto-imports components from `components/` — since `CmsGenericElement` looks them up via `resolveComponent()`, the custom component is found automatically.

---

### Registering a custom CMS block

```vue
<!-- components/CmsBlockMyCustomBlock.vue -->
<script setup lang="ts">
import { useCmsBlock } from '@shopware/composables'
import type { CmsBlock } from '#shopware'

const props = defineProps<{ content: CmsBlock }>()
const { getSlotContent } = useCmsBlock(props.content)
const mainSlot = getSlotContent('main')
</script>
<template>
  <div class="my-custom-block">
    <CmsGenericElement v-if="mainSlot" :content="mainSlot" />
  </div>
</template>
```

---

### Overriding a default component

Your own `CmsElementText.vue` in `components/` overrides the one from the layer. Nuxt gives project components precedence over layer components.

---

## Complete component list

### Sections (2)

| Component name | Shopware type | Description |
|---|---|---|
| `CmsSectionDefault` | `default` | Default section (only the `main` position) |
| `CmsSectionSidebar` | `sidebar` | Two-column layout: `main` + `sidebar` |

---

### Blocks (44)

| Component name | Shopware type | Layout/content |
|---|---|---|
| `CmsBlockCategoryNavigation` | `category-navigation` | Category navigation |
| `CmsBlockCenterText` | `center-text` | Centered text |
| `CmsBlockCrossSelling` | `cross-selling` | Cross-selling products |
| `CmsBlockCustomForm` | `custom-form` | Custom form |
| `CmsBlockDefault` | (fallback) | Fallback block |
| `CmsBlockForm` | `form` | Default form |
| `CmsBlockGalleryBuybox` | `gallery-buybox` | Gallery + buy box |
| `CmsBlockHtml` | `html` | Raw HTML content |
| `CmsBlockImage` | `image` | Single image |
| `CmsBlockImageBubbleRow` | `image-bubble-row` | Images in bubble form |
| `CmsBlockImageCover` | `image-cover` | Full-width image |
| `CmsBlockImageFourColumn` | `image-four-column` | Four-column images |
| `CmsBlockImageGallery` | `image-gallery` | Image gallery |
| `CmsBlockImageGalleryBig` | `image-gallery-big` | Large image gallery |
| `CmsBlockImageHighlightRow` | `image-highlight-row` | Highlight image row |
| `CmsBlockImageSimpleGrid` | `image-simple-grid` | Simple image grid |
| `CmsBlockImageSlider` | `image-slider` | Image slider |
| `CmsBlockImageText` | `image-text` | Image + text |
| `CmsBlockImageTextBubble` | `image-text-bubble` | Image + text (bubble style) |
| `CmsBlockImageTextCover` | `image-text-cover` | Image cover + text |
| `CmsBlockImageTextGallery` | `image-text-gallery` | Gallery + text |
| `CmsBlockImageTextRow` | `image-text-row` | Image and text row |
| `CmsBlockImageThreeColumn` | `image-three-column` | Three-column images |
| `CmsBlockImageThreeCover` | `image-three-cover` | Three cover images |
| `CmsBlockImageTwoColumn` | `image-two-column` | Two-column images |
| `CmsBlockProductDescriptionReviews` | `product-description-reviews` | Description + reviews |
| `CmsBlockProductHeading` | `product-heading` | Product heading |
| `CmsBlockProductListing` | `product-listing` | Product listing |
| `CmsBlockProductSlider` | `product-slider` | Product slider |
| `CmsBlockProductThreeColumn` | `product-three-column` | Three-column products |
| `CmsBlockSidebarFilter` | `sidebar-filter` | Sidebar filter |
| `CmsBlockText` | `text` | Text block |
| `CmsBlockTextHero` | `text-hero` | Text hero |
| `CmsBlockTextOnImage` | `text-on-image` | Text on image |
| `CmsBlockTextTeaser` | `text-teaser` | Text teaser |
| `CmsBlockTextTeaserSection` | `text-teaser-section` | Text teaser section |
| `CmsBlockTextThreeColumn` | `text-three-column` | Three-column text |
| `CmsBlockTextTwoColumn` | `text-two-column` | Two-column text |
| `CmsBlockVimeoVideo` | `vimeo-video` | Vimeo video |
| `CmsBlockYoutubeVideo` | `youtube-video` | YouTube video |

---

### Elements (21)

| Component name | Shopware type | Description |
|---|---|---|
| `CmsElementBuyBox` | `buy-box` | Buy box (product + add to cart) |
| `CmsElementCategoryNavigation` | `category-navigation` | Category nav bar |
| `CmsElementCrossSelling` | `cross-selling` | Cross-selling products |
| `CmsElementCustomForm` | `custom-form` | Custom form |
| `CmsElementForm` | `form` | Default form |
| `CmsElementHtml` | `html` | XSS-sanitized HTML content |
| `CmsElementImage` | `image` | Image with link, display mode, thumbnails |
| `CmsElementImageGallery` | `image-gallery` | Image gallery with zoom |
| `CmsElementImageGallery3dPlaceholder` | (internal) | 3D placeholder in the gallery |
| `CmsElementImageSlider` | `image-slider` | Image slider |
| `CmsElementManufacturerLogo` | `manufacturer-logo` | Manufacturer logo |
| `CmsElementProductBox` | `product-box` | Product card |
| `CmsElementProductDescriptionReviews` | `product-description-reviews` | Tabs: description/reviews |
| `CmsElementProductListing` | `product-listing` | Complete product listing |
| `CmsElementProductName` | `product-name` | Product name as a heading |
| `CmsElementProductSlider` | `product-slider` | Horizontally scrollable product slider |
| `CmsElementSidebarFilter` | `sidebar-filter` | Filter sidebar |
| `CmsElementText` | `text` | Rich text (HTML via the html-to-vue renderer) |
| `CmsElementVimeoVideo` | `vimeo-video` | Embedded Vimeo video |
| `CmsElementYoutubeVideo` | `youtube-video` | Embedded YouTube video |
| `SwProductListingPagination` | (internal) | Pagination for product listings |

---

## Listing filter components

| Component name | Description |
|---|---|
| `SwFilterPrice` | Price slider with dual input |
| `SwFilterProperties` | Checkbox list for property groups/manufacturers |
| `SwFilterRating` | Five-star rating filter |
| `SwFilterShippingFree` | Free-shipping toggle |

---

## Sw* components (reusable UI)

In addition to the CMS components, the layer exports general storefront components:

| Component | Description |
|---|---|
| `SwCategoryNavigation` | Category navigation bar |
| `SwCategoryNavigationLink` | Single navigation link |
| `SwContactForm` | Contact form |
| `SwFilterChips` | Active filters as chips |
| `SwFilterDropdown` | Filter dropdown container |
| `SwListingProductPrice` | Price in the listing |
| `SwMedia3D` | 3D media (via @tresjs) |
| `SwNewsletterForm` | Newsletter sign-up form |
| `SwPagination` | General pagination |
| `SwProductAddToCart` | Add-to-cart button |
| `SwProductCard` | Product card (image + name + price) |
| `SwProductCardDetails` | Product card details |
| `SwProductCardImage` | Product card image |
| `SwProductCardSkeleton` | Skeleton loader for the product card |
| `SwProductGallery` | Product image gallery |
| `SwProductListingFilter` | Single listing filter |
| `SwProductListingFilters` | Listing filter panel (vertical) |
| `SwProductListingFiltersHorizontal` | Listing filter panel (horizontal) |
| `SwProductPrice` | Product price display |
| `SwProductRating` | Star rating display |
| `SwProductReviews` | Review list |
| `SwProductReviewsForm` | Review input form |
| `SwProductUnits` | Product units |
| `SwQuantitySelect` | Quantity selection |
| `SwSharedPrice` | Price formatting |
| `SwSlider` | General slider |
| `SwSortDropdown` | Sorting dropdown |
| `SwStockInfo` | Stock level display |
| `SwVariantConfigurator` | Variant selection |

---

## Base UI components

| Component | Description |
|---|---|
| `BaseButton` | Base button (various variants) |
| `BaseIcon` | Icon wrapper |
| `Checkbox` | Checkbox with custom styling |
| `CheckmarkIcon` | Checkmark icon |
| `ChevronIcon` | Arrow icon (chevron) |
| `ExclamationIcon` | Exclamation mark icon |
| `IconButton` | Icon button |
| `RadioButton` | Radio button (`defineModel<string\|null>`) |
| `StarIcon` | Star icon (`filled` prop) |
| `SwitchButton` | Toggle switch (`defineModel<boolean\|null>`) |
| `UserIcon` | User icon |
| `WishlistIcon` | Wishlist icon (filled/empty) |

---

## CMS composables in components

### `useCmsBlock` — in block components

```vue
<!-- CmsBlockImageText.vue -->
<script setup lang="ts">
import { useCmsBlock } from '@shopware/composables'
import type { CmsBlock } from '#shopware'

const props = defineProps<{ content: CmsBlock }>()
const { block, getSlotContent } = useCmsBlock(props.content)

const imageSlot = getSlotContent('left')    // slot by position/name
const textSlot = getSlotContent('right')
</script>
<template>
  <div class="flex">
    <CmsGenericElement v-if="imageSlot" :content="imageSlot" />
    <CmsGenericElement v-if="textSlot" :content="textSlot" />
  </div>
</template>
```

---

### `useCmsSection` — in section components

```vue
<!-- CmsSectionSidebar.vue -->
<script setup lang="ts">
import { useCmsSection } from '@shopware/composables'
import type { CmsSection } from '#shopware'

const props = defineProps<{ content: CmsSection }>()
const { section, getPositionContent } = useCmsSection(props.content)

const mainBlocks = getPositionContent('main')
const sidebarBlocks = getPositionContent('sidebar')
</script>
<template>
  <div class="flex">
    <aside class="w-1/4">
      <CmsGenericBlock v-for="block in sidebarBlocks" :key="block.id" :content="block" />
    </aside>
    <main class="w-3/4">
      <CmsGenericBlock v-for="block in mainBlocks" :key="block.id" :content="block" />
    </main>
  </div>
</template>
```

---

### `useCmsElementConfig` — reading the element configuration

```vue
<!-- CmsElementImage.vue -->
<script setup lang="ts">
import { useCmsElementConfig, useCmsElementImage } from '@shopware/composables'

const props = defineProps<{ content: CmsSlot }>()
const { getConfigValue } = useCmsElementConfig(props.content)
const { imageAttrs, anchorAttrs, displayMode, isVideoElement } = useCmsElementImage(props.content)

const minHeight = getConfigValue('minHeight')  // e.g. "200px"
const displayMode = getConfigValue('displayMode')  // "cover", "contain", "standard"
</script>
```

---

## HTML-to-Vue renderer (`CmsElementText`)

`CmsElementText` uses its own AST-based HTML renderer (from `helpers/html-to-vue/`):

1. **`generateAST(html)`**: parses the HTML string into an AST (via `html-to-ast`)
2. **`rectifyAST(ast)`**: renames tags to Vue component names
3. **`renderer(ast, config)`**: converts the AST into VNodes via `h()`; uses `extraComponentsMap` for custom tag handlers
4. **`renderToHtml(html, config)`**: entry point; configurable with:
   - `container.type` — wrapper element
   - `extraComponentsMap` — custom tag handlers
   - `textTransformer` — text transformation

**XSS protection**: HTML is sanitized via the `xss` library before it is rendered.

---

## 3D content (`CmsBlockSpatialViewer`)

Renders `.glb` 3D models via `@tresjs/cientos` (Three.js). Activated by `isSpatial(media)` (checks for the `.glb` extension).

---

## Layout configuration

`getCmsLayoutConfiguration(element)` extracts from every CMS element:

```ts
{
  cssClasses: {
    // Visibility classes (Tailwind):
    'max-md:hidden': boolean,      // desktop only
    'md:max-lg:hidden': boolean,   // mobile + desktop only (no tablet)
    'lg:hidden': boolean,          // mobile only
  },
  layoutStyles: {
    backgroundColor?: string,      // CSS background color
    backgroundImage?: string,      // CSS url(...)
    backgroundSize?: string,       // "cover", "contain", "auto"
    sizingMode?: string,           // "boxed" | "full_width"
  }
}
```

`CmsPage` converts `sizingMode` into Tailwind classes:
- `"boxed"` → `"max-w-screen-2xl w-full mx-auto"`
- `"full_width"` → `"w-full"`
