# @shopware/helpers — Complete Function Reference

Version: **1.7.1**

Pure utility functions without state, without Vue dependencies. All functions are tree-shakeable.

---

## Contents

- [Installation & import](#installation-import)
- [Translations](#translations)
- [Product functions](#product-functions)
- [Category functions](#category-functions)
- [CMS functions](#cms-functions)
- [Media functions](#media-functions)
- [Price functions](#price-functions)
- [Listing functions](#listing-functions)
- [Routing functions](#routing-functions)
- [URL utilities](#url-utilities)
- [Checkout helper functions](#checkout-helper-functions)
- [Language functions](#language-functions)
- [B2B helper functions](#b2b-helper-functions)
- [UI interface types](#ui-interface-types)
- [Complete export list](#complete-export-list)

## Installation & import

```ts
import { getTranslatedProperty, getProductRoute, getFormattedPrice } from '@shopware/helpers'
```

---

## Translations

### `getTranslatedProperty(element, property)`

```ts
function getTranslatedProperty<T extends { translated?: Record<string, unknown> }>(
  element: T | null | undefined,
  property: keyof T
): string
```

Returns `element.translated[property]`, falling back to `element[property]`, falling back to `""`.

```ts
const name = getTranslatedProperty(product, 'name')
const description = getTranslatedProperty(product, 'description')
const metaTitle = getTranslatedProperty(category, 'metaTitle')
```

---

## Product functions

### `getProductName(product)`

```ts
function getProductName(product: Partial<Schemas["Product"]> | undefined): string
```

Shorthand for `getTranslatedProperty(product, 'name')`.

---

### `getProductUrl(product)`

```ts
function getProductUrl(product: Partial<Schemas["Product"]>): string
```

Returns `/{seoPathInfo}` when present, otherwise `/detail/{id}`.

---

### `getProductRoute(product)`

```ts
function getProductRoute(product: Partial<Schemas["Product"]>): RouteLocationRaw
```

Returns a Vue Router route object:
```ts
{
  path: '/',
  state: {
    routeName: 'frontend.detail.page',
    foreignKey: product.id
  }
}
```

---

### `getMainImageUrl(product)`

```ts
function getMainImageUrl(product: Partial<Schemas["Product"]>): string
```

Checks in order: `cover.media.url` → `cover.url` → `media[0].media.url` → `""`.

---

### `getProductRealPrice(product)`

```ts
function getProductRealPrice(product: Partial<Schemas["Product"]>): Schemas["CalculatedPrice"] | undefined
```

Returns the last entry of `calculatedPrices[]` when several are present (tier prices), otherwise `calculatedPrice`.

---

### `getProductFromPrice(product)`

```ts
function getProductFromPrice(product: Partial<Schemas["Product"]>): number | undefined
```

Returns the `unitPrice`, but only when `calculatedPrices.length > 0` (that is, when tier prices exist — for a "from X €" display).

---

### `getProductCalculatedListingPrice(product)`

```ts
function getProductCalculatedListingPrice(product: Partial<Schemas["Product"]>): number | undefined
```

Returns `listPrice.price ?? unitPrice` of the `calculatedPrice`.

---

### `getProductRatingAverage(product)`

```ts
function getProductRatingAverage(product: Partial<Schemas["Product"]>): number | null | undefined
```

---

### `getProductReviews(product)`

```ts
function getProductReviews(product: Partial<Schemas["Product"]>): UiProductReview[]
```

Converts `productReviews[]` into `UiProductReview[]`:

```ts
type UiProductReview = {
  id: string
  author: string
  date: string
  message: string | null
  points: number | null | undefined
}
```

---

### `getProductManufacturerName(product)`

```ts
function getProductManufacturerName(product: Partial<Schemas["Product"]>): string
```

→ `manufacturer.translated.name ?? ""`

---

### `getProductTierPrices(product)`

```ts
function getProductTierPrices(product: Partial<Schemas["Product"]>): TierPrice[]

type TierPrice = {
  label: string   // "to N" or "from N"
  quantity: number
  unitPrice: number
  totalPrice: number
  regulationPrice: number | null
}
```

Maps `calculatedPrices[]` onto `TierPrice[]`. The last entry gets `"from N"`, all others `"to N"`.

---

### `getProductFreeShipping(product)`

```ts
function getProductFreeShipping(product: Partial<Schemas["Product"]>): boolean
```

→ `product.shippingFree ?? false`

---

### `isProductOnSale(product)`

```ts
function isProductOnSale(product: Partial<Schemas["Product"]>): boolean
```

→ `calculatedPrice.listPrice.percentage > 0`

---

### `isProductTopSeller(product)`

```ts
function isProductTopSeller(product: Partial<Schemas["Product"]>): boolean
```

→ `!!product.markAsTopseller`

---

## Category functions

### `getCategoryBreadcrumbs(category, options?)`

```ts
function getCategoryBreadcrumbs(
  category: Partial<Schemas["Category"]>,
  options?: { startIndex?: number }
): Array<{ name: string }>
```

Returns `category.translated.breadcrumb.slice(startIndex)` (default: from index 0).

---

### `getCategoryImageUrl(category)`

```ts
function getCategoryImageUrl(category: Partial<Schemas["Category"]>): string
```

Returns `media.url` when the type is `page`, `link` or `folder`, otherwise `""`.

---

### `getCategoryRoute(category)`

```ts
function getCategoryRoute(category: Partial<Schemas["Category"]>): RouteLocationRaw
```

Type-dependent logic:
- Type `link` → `{ path: category.externalLink }` (external) or `{ path: category.internalLink }` (internal)
- Type `page`/`folder` → `{ path: '/', state: { routeName: 'frontend.navigation.page', foreignKey: id } }`

---

### `getCategoryUrl(category)`

```ts
function getCategoryUrl(category: Partial<Schemas["Category"]>): string
```

- Type `link` → external URL
- SEO URL present → `/{seoPathInfo}`
- Otherwise → `/navigation/{id}`

---

## CMS functions

### `getCmsEntityObject(page)`

```ts
function getCmsEntityObject(
  page: Schemas["CmsPage"]
): Schemas["Category"] | Schemas["Product"] | Schemas["LandingPage"] | undefined
```

Extracts the entity object from the CMS page.

---

### `getCmsLayoutConfiguration(element)`

```ts
function getCmsLayoutConfiguration(
  element: Schemas["CmsSection"] | Schemas["CmsBlock"] | Schemas["CmsSlot"]
): {
  cssClasses: Record<string, boolean>
  layoutStyles: {
    backgroundColor?: string | null
    backgroundImage?: string | null
    backgroundSize?: string | null
    sizingMode?: string | null
  }
}
```

Parses visibility flags and style configurations out of the CMS element. The CSS classes correspond to Tailwind classes (e.g. `max-md:hidden`, `md:max-lg:hidden`, `lg:hidden`).

---

### `getCmsBreadcrumbs(page)`

```ts
function getCmsBreadcrumbs(page: Schemas["CmsPage"]): Array<{ name: string }>
```

→ `[{ name: page.translated.name }]`

---

### `getCmsTranslate(content, key, params?)`

```ts
function getCmsTranslate(
  content: Record<string, unknown>,
  key: string,
  params?: Record<string, string>
): string
```

Looks up `content[key]` and replaces `{placeholder}` with the `params` values.

---

### `getProductListingFromCmsPage(page)`

```ts
function getProductListingFromCmsPage<T = Schemas["ProductListingResult"]>(
  page: Schemas["CmsPage"]
): T | null
```

Searches `page.sections[].blocks[].slots[]` for the first slot with `type === 'product-listing'` and returns `slot.data.listing`.

---

### `buildUrlPrefix(url, prefix)`

```ts
type UrlRouteOutput = {
  path: string
  state?: { routeName: string; foreignKey: string }
}

function buildUrlPrefix(
  url: UrlRouteOutput | string,
  prefix: string
): UrlRouteOutput
```

Prepends the language prefix to a relative path. Absolute URLs are returned unchanged.

---

### `getBackgroundImageUrl(media, element?, options?)`

```ts
type BackgroundImageOptions = {
  width?: number
  height?: number
  format?: string
  quality?: number
}

function getBackgroundImageUrl(
  media: string | Schemas["Media"] | null | undefined,
  element?: object,
  options?: BackgroundImageOptions
): string
```

Extracts the URL from a CSS `url()` string or a media object. Adds the CDN parameters `?width=N&fit=crop,smart`.

---

### `isProduct(entity)` / `isCategory(entity)` / `isLandingPage(entity)`

```ts
function isProduct(entity: unknown): entity is Schemas["Product"]
function isCategory(entity: unknown): entity is Schemas["Category"]
function isLandingPage(entity: unknown): entity is Schemas["LandingPage"]
```

Type guards that check `apiAlias`.

---

### `isMaintenanceMode(errors)`

```ts
function isMaintenanceMode(errors: unknown): boolean
```

Checks for the error code `FRAMEWORK__API_SALES_CHANNEL_MAINTENANCE_MODE`.

---

### `helpersCssClasses` + `HelpersCssClasses`

```ts
const helpersCssClasses: readonly string[]
type HelpersCssClasses = typeof helpersCssClasses[number]
```

All CSS classes that `getCmsLayoutConfiguration` can return (Tailwind responsive classes).

---

## Media functions

### `getBiggestThumbnailUrl(media)`

```ts
function getBiggestThumbnailUrl(media: Schemas["Media"] | null | undefined): string
```

Finds the thumbnail with the largest `width`. Falls back to `""`.

---

### `getSmallestThumbnailUrl(media)`

```ts
function getSmallestThumbnailUrl(media: Schemas["Media"] | null | undefined): string
```

Finds the thumbnail with the smallest `width`. Falls back to `media.url` → `""`.

---

### `getMedia(media)`

```ts
function getMedia(
  media: Schemas["LineItem"]["downloads"]
): Array<{ id: string; fileName: string; accessGranted: boolean }>
```

Maps `lineItem.downloads[]` onto a simplified array.

---

### `getSrcSetForMedia(media)`

```ts
function getSrcSetForMedia(media: Schemas["Media"] | null | undefined): string
```

Builds a `srcset` string from `thumbnails[]`. Example:
```
"https://cdn.example.com/img-320.jpg 320w, https://cdn.example.com/img-640.jpg 640w"
```

---

### `encodeUrlPath(url)`

```ts
function encodeUrlPath(url: string): string
```

Normalizes URL path encoding: decodes and cleanly re-encodes every path segment.

---

### `generateCdnSrcSet(src, widths, options?)`

```ts
function generateCdnSrcSet(
  src: string,
  widths: number[],
  options?: { format?: string; quality?: number }
): string
```

Generates a `srcset` string with CDN parameters:
```ts
generateCdnSrcSet('https://cdn.example.com/img.jpg', [320, 640, 1280])
// → "https://cdn.example.com/img.jpg?width=320&fit=crop,smart 320w, ..."
```

---

### `buildCdnImageUrl(src, dimensions, options?)`

```ts
function buildCdnImageUrl(
  src: string,
  dimensions: { width?: number; height?: number },
  options?: { format?: string; quality?: number }
): string
```

Picks the larger of the two dimensions, rounds up to the next multiple of 100, adds `?width=N&fit=crop,smart`.

---

### `downloadFile(file, name)`

```ts
function downloadFile(file: Blob, name: string): void
```

Creates a temporary `<a>` tag with `URL.createObjectURL`, triggers the download and removes the link afterwards.

---

## Price functions

### `getFormattedPrice(value, currency?, options?)`

```ts
function getFormattedPrice(
  value: number | string | undefined,
  currency?: string,   // ISO currency code, e.g. "EUR", "USD"
  options?: {
    localeCode?: string  // e.g. "de-DE", "en-US"
    decimals?: number
    rtl?: boolean        // right-to-left for Arabic currencies
    removeCurrency?: boolean
  }
): string
```

Formats a price with `Intl.NumberFormat`. Without `currency`, the currency symbol from the `usePrice()` composable is used.

```ts
getFormattedPrice(19.99, 'EUR', { localeCode: 'de-DE' })
// → "19,99 €"

getFormattedPrice(19.99, 'USD', { localeCode: 'en-US' })
// → "$19.99"
```

---

## Listing functions

### `getListingFilters(aggregations)`

```ts
function getListingFilters(
  aggregations: Schemas["ProductListingResult"]["aggregations"]
): ListingFilter[]

type ListingFilter = {
  code: string
  label?: string
  entities?: unknown[]   // for "properties" aggregations
  options?: unknown[]    // for other aggregations
}
```

Transforms the aggregations object into a structured filter list. Skips `"options"` aggregations.

---

## Routing functions

### `getRouteFromPathInfo(path)`

```ts
type RouteNameFromPathInfo = 'frontend.navigation.page' | 'frontend.detail.page' | 'frontend.landing.page'

type RouteInfoFromPathInfo = {
  routeName: RouteNameFromPathInfo
  foreignKey: string
}

function getRouteFromPathInfo(
  path: Schemas["SeoUrl"] | { pathInfo: string }
): RouteInfoFromPathInfo | null
```

Converts Shopware path info strings into Vue-Router-friendly objects:
- `/navigation/{id}` → `{ routeName: 'frontend.navigation.page', foreignKey: id }`
- `/detail/{id}` → `{ routeName: 'frontend.detail.page', foreignKey: id }`
- `/landingPage/{id}` → `{ routeName: 'frontend.landing.page', foreignKey: id }`

---

### `normalizePath(path)`

```ts
function normalizePath(path: string): string
```

Normalizes URL paths (removes duplicate slashes, etc.).

---

### `isTechnicalPath(path)`

```ts
function isTechnicalPath(path: string): boolean
```

Checks whether the path is a technical Shopware path (starts with `/navigation/`, `/detail/`, etc.).

---

## URL utilities

### `relativeUrlSlash(url, slash?)`

```ts
function relativeUrlSlash(url: string, slash?: boolean): string
```

`slash = true` (default): add a leading `/`.
`slash = false`: remove a leading `/`.

---

### `urlIsAbsolute(url)`

```ts
function urlIsAbsolute(url: string): boolean
```

→ `true` when the URL starts with `//` or `https://`.

---

## Checkout helper functions

### `getPaymentMethodIcon(paymentMethod)`

```ts
function getPaymentMethodIcon(paymentMethod: Partial<Schemas["PaymentMethod"]>): string
```

→ `paymentMethod.media?.url ?? ""`

---

### `getShippingMethodIcon(shippingMethod)`

```ts
function getShippingMethodIcon(shippingMethod: Partial<Schemas["ShippingMethod"]>): string
```

→ `shippingMethod.media?.url ?? ""`

---

### `getShippingMethodDeliveryTime(shippingMethod)`

```ts
function getShippingMethodDeliveryTime(shippingMethod: Partial<Schemas["ShippingMethod"]>): string
```

→ `shippingMethod.deliveryTime?.translated?.name ?? ""`

---

## Language functions

### `getLanguageName(language)`

```ts
function getLanguageName(language: Partial<Schemas["Language"]>): string
```

→ `language.translationCode?.translated?.name ?? ""`

---

## B2B helper functions

### `canUseQuoteActions(quote)`

```ts
function canUseQuoteActions(quote: Schemas["Quote"]): boolean
```

→ `true` when `quote.stateMachineState.technicalName === "replied"`.

---

## UI interface types

```ts
type UiMediaGalleryItemUrl = {
  src: string
  width?: number
  height?: number
}

type UiMediaGalleryItem = {
  thumbnailUrl: string
  thumbnailUrls: UiMediaGalleryItemUrl[]
  mediaUrl: string
  alt?: string
  title?: string
}

type UiProductOption = {
  id: string
  code: string
  name: string
  color?: string
  label?: string
  description?: string
  colorHexCode?: string
  media?: Schemas["Media"]
  position?: number
}

type UiProductProperty = {
  name: string
  values: string[]
}

type UiProductReview = {
  id: string
  author: string
  date: string
  message: string | null
  points: number | null | undefined
}
```

---

## Complete export list

```ts
// product
export { getProductName, getProductUrl, getProductRoute, getMainImageUrl }
export { getProductRealPrice, getProductFromPrice, getProductCalculatedListingPrice }
export { getProductRatingAverage, getProductReviews, getProductManufacturerName }
export { getProductTierPrices, getProductFreeShipping, isProductOnSale, isProductTopSeller }

// category
export { getCategoryBreadcrumbs, getCategoryImageUrl, getCategoryRoute, getCategoryUrl }

// CMS
export { getCmsEntityObject, getCmsLayoutConfiguration, getCmsBreadcrumbs }
export { getCmsTranslate, getProductListingFromCmsPage }
export { buildUrlPrefix, getBackgroundImageUrl }
export { isProduct, isCategory, isLandingPage, isMaintenanceMode }
export { helpersCssClasses }
export type { HelpersCssClasses }

// media
export { getBiggestThumbnailUrl, getSmallestThumbnailUrl, getMedia }
export { getSrcSetForMedia, encodeUrlPath, generateCdnSrcSet, buildCdnImageUrl }
export { downloadFile }

// price
export { getFormattedPrice }

// listing
export { getListingFilters }

// routing
export { getRouteFromPathInfo, normalizePath, isTechnicalPath }
export type { RouteNameFromPathInfo, RouteInfoFromPathInfo, UrlRouteOutput }

// URL
export { relativeUrlSlash, urlIsAbsolute }

// checkout
export { getPaymentMethodIcon, getShippingMethodIcon, getShippingMethodDeliveryTime }

// language
export { getLanguageName }

// translation
export { getTranslatedProperty }

// B2B
export { canUseQuoteActions }

// UI types
export type { UiMediaGalleryItemUrl, UiMediaGalleryItem }
export type { UiProductOption, UiProductProperty, UiProductReview, TierPrice }
```
