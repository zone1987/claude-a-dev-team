# @shopware/helpers — Vollständige Funktionsreferenz

Version: **1.7.1**

Reine Utility-Funktionen ohne State, ohne Vue-Abhängigkeiten. Alle Funktionen sind tree-shakeable.

---

## Installation & Import

```ts
import { getTranslatedProperty, getProductRoute, getFormattedPrice } from '@shopware/helpers'
```

---

## Übersetzungen

### `getTranslatedProperty(element, property)`

```ts
function getTranslatedProperty<T extends { translated?: Record<string, unknown> }>(
  element: T | null | undefined,
  property: keyof T
): string
```

Gibt `element.translated[property]` zurück, Fallback auf `element[property]`, Fallback auf `""`.

```ts
const name = getTranslatedProperty(product, 'name')
const description = getTranslatedProperty(product, 'description')
const metaTitle = getTranslatedProperty(category, 'metaTitle')
```

---

## Produkt-Funktionen

### `getProductName(product)`

```ts
function getProductName(product: Partial<Schemas["Product"]> | undefined): string
```

Kurz für `getTranslatedProperty(product, 'name')`.

---

### `getProductUrl(product)`

```ts
function getProductUrl(product: Partial<Schemas["Product"]>): string
```

Gibt `/{seoPathInfo}` zurück wenn vorhanden, sonst `/detail/{id}`.

---

### `getProductRoute(product)`

```ts
function getProductRoute(product: Partial<Schemas["Product"]>): RouteLocationRaw
```

Gibt ein Vue-Router-Route-Objekt zurück:
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

Prüft der Reihe nach: `cover.media.url` → `cover.url` → `media[0].media.url` → `""`.

---

### `getProductRealPrice(product)`

```ts
function getProductRealPrice(product: Partial<Schemas["Product"]>): Schemas["CalculatedPrice"] | undefined
```

Gibt den letzten Eintrag aus `calculatedPrices[]` zurück wenn mehrere vorhanden (Tier-Preise), sonst `calculatedPrice`.

---

### `getProductFromPrice(product)`

```ts
function getProductFromPrice(product: Partial<Schemas["Product"]>): number | undefined
```

Gibt den `unitPrice` zurück, aber nur wenn `calculatedPrices.length > 0` (also wenn es Tier-Preise gibt — für "ab X €"-Anzeige).

---

### `getProductCalculatedListingPrice(product)`

```ts
function getProductCalculatedListingPrice(product: Partial<Schemas["Product"]>): number | undefined
```

Gibt `listPrice.price ?? unitPrice` des `calculatedPrice`.

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

Konvertiert `productReviews[]` in `UiProductReview[]`:

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
  label: string   // "to N" oder "from N"
  quantity: number
  unitPrice: number
  totalPrice: number
  regulationPrice: number | null
}
```

Mappt `calculatedPrices[]` auf `TierPrice[]`. Letzter Eintrag bekommt `"from N"`, alle anderen `"to N"`.

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

## Kategorie-Funktionen

### `getCategoryBreadcrumbs(category, options?)`

```ts
function getCategoryBreadcrumbs(
  category: Partial<Schemas["Category"]>,
  options?: { startIndex?: number }
): Array<{ name: string }>
```

Gibt `category.translated.breadcrumb.slice(startIndex)` zurück (Standard: ab Index 0).

---

### `getCategoryImageUrl(category)`

```ts
function getCategoryImageUrl(category: Partial<Schemas["Category"]>): string
```

Gibt `media.url` zurück wenn Typ `page`, `link` oder `folder`, sonst `""`.

---

### `getCategoryRoute(category)`

```ts
function getCategoryRoute(category: Partial<Schemas["Category"]>): RouteLocationRaw
```

Typenabhängige Logik:
- Typ `link` → `{ path: category.externalLink }` (external) oder `{ path: category.internalLink }` (internal)
- Typ `page`/`folder` → `{ path: '/', state: { routeName: 'frontend.navigation.page', foreignKey: id } }`

---

### `getCategoryUrl(category)`

```ts
function getCategoryUrl(category: Partial<Schemas["Category"]>): string
```

- Typ `link` → externe URL
- SEO-URL vorhanden → `/{seoPathInfo}`
- Sonst → `/navigation/{id}`

---

## CMS-Funktionen

### `getCmsEntityObject(page)`

```ts
function getCmsEntityObject(
  page: Schemas["CmsPage"]
): Schemas["Category"] | Schemas["Product"] | Schemas["LandingPage"] | undefined
```

Extrahiert das Entity-Objekt aus der CMS-Page.

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

Parst Sichtbarkeits-Flags und Style-Konfigurationen aus dem CMS-Element. Die CSS-Klassen entsprechen Tailwind-Klassen (z.B. `max-md:hidden`, `md:max-lg:hidden`, `lg:hidden`).

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

Sucht `content[key]` und ersetzt `{placeholder}` mit `params`-Werten.

---

### `getProductListingFromCmsPage(page)`

```ts
function getProductListingFromCmsPage<T = Schemas["ProductListingResult"]>(
  page: Schemas["CmsPage"]
): T | null
```

Durchsucht `page.sections[].blocks[].slots[]` nach dem ersten Slot mit `type === 'product-listing'` und gibt `slot.data.listing` zurück.

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

Stellt einem relativen Pfad das Sprachpräfix voran. Absolute URLs werden unverändert zurückgegeben.

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

Extrahiert die URL aus einem CSS-`url()`-String oder Media-Objekt. Fügt CDN-Parameter `?width=N&fit=crop,smart` hinzu.

---

### `isProduct(entity)` / `isCategory(entity)` / `isLandingPage(entity)`

```ts
function isProduct(entity: unknown): entity is Schemas["Product"]
function isCategory(entity: unknown): entity is Schemas["Category"]
function isLandingPage(entity: unknown): entity is Schemas["LandingPage"]
```

Type-Guards die auf `apiAlias` prüfen.

---

### `isMaintenanceMode(errors)`

```ts
function isMaintenanceMode(errors: unknown): boolean
```

Prüft auf Error-Code `FRAMEWORK__API_SALES_CHANNEL_MAINTENANCE_MODE`.

---

### `helpersCssClasses` + `HelpersCssClasses`

```ts
const helpersCssClasses: readonly string[]
type HelpersCssClasses = typeof helpersCssClasses[number]
```

Alle CSS-Klassen die von `getCmsLayoutConfiguration` zurückgegeben werden können (Tailwind-Responsiv-Klassen).

---

## Media-Funktionen

### `getBiggestThumbnailUrl(media)`

```ts
function getBiggestThumbnailUrl(media: Schemas["Media"] | null | undefined): string
```

Findet das Thumbnail mit der größten `width`. Fallback auf `""`.

---

### `getSmallestThumbnailUrl(media)`

```ts
function getSmallestThumbnailUrl(media: Schemas["Media"] | null | undefined): string
```

Findet das Thumbnail mit der kleinsten `width`. Fallback auf `media.url` → `""`.

---

### `getMedia(media)`

```ts
function getMedia(
  media: Schemas["LineItem"]["downloads"]
): Array<{ id: string; fileName: string; accessGranted: boolean }>
```

Mappt `lineItem.downloads[]` auf ein vereinfachtes Array.

---

### `getSrcSetForMedia(media)`

```ts
function getSrcSetForMedia(media: Schemas["Media"] | null | undefined): string
```

Baut einen `srcset`-String aus `thumbnails[]`. Beispiel:
```
"https://cdn.example.com/img-320.jpg 320w, https://cdn.example.com/img-640.jpg 640w"
```

---

### `encodeUrlPath(url)`

```ts
function encodeUrlPath(url: string): string
```

Normalisiert URL-Pfad-Encoding: dekodiert und re-encodiert jeden Pfad-Segment sauber.

---

### `generateCdnSrcSet(src, widths, options?)`

```ts
function generateCdnSrcSet(
  src: string,
  widths: number[],
  options?: { format?: string; quality?: number }
): string
```

Generiert einen `srcset`-String mit CDN-Parametern:
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

Wählt die größere der beiden Dimensionen, rundet auf die nächste 100er-Grenze, fügt `?width=N&fit=crop,smart` hinzu.

---

### `downloadFile(file, name)`

```ts
function downloadFile(file: Blob, name: string): void
```

Erstellt einen temporären `<a>`-Tag mit `URL.createObjectURL`, triggert den Download und entfernt den Link danach.

---

## Preis-Funktionen

### `getFormattedPrice(value, currency?, options?)`

```ts
function getFormattedPrice(
  value: number | string | undefined,
  currency?: string,   // ISO-Währungscode, z.B. "EUR", "USD"
  options?: {
    localeCode?: string  // z.B. "de-DE", "en-US"
    decimals?: number
    rtl?: boolean        // Right-to-left für arabische Währungen
    removeCurrency?: boolean
  }
): string
```

Formatiert einen Preis mit `Intl.NumberFormat`. Ohne `currency` wird das Währungssymbol aus dem `usePrice()`-Composable verwendet.

```ts
getFormattedPrice(19.99, 'EUR', { localeCode: 'de-DE' })
// → "19,99 €"

getFormattedPrice(19.99, 'USD', { localeCode: 'en-US' })
// → "$19.99"
```

---

## Listing-Funktionen

### `getListingFilters(aggregations)`

```ts
function getListingFilters(
  aggregations: Schemas["ProductListingResult"]["aggregations"]
): ListingFilter[]

type ListingFilter = {
  code: string
  label?: string
  entities?: unknown[]   // für "properties"-Aggregationen
  options?: unknown[]    // für andere Aggregationen
}
```

Transformiert das Aggregations-Objekt in eine strukturierte Filter-Liste. Überspringt `"options"`-Aggregationen.

---

## Routing-Funktionen

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

Konvertiert Shopware-Pfadinfo-Strings in Vue-Router-freundliche Objekte:
- `/navigation/{id}` → `{ routeName: 'frontend.navigation.page', foreignKey: id }`
- `/detail/{id}` → `{ routeName: 'frontend.detail.page', foreignKey: id }`
- `/landingPage/{id}` → `{ routeName: 'frontend.landing.page', foreignKey: id }`

---

### `normalizePath(path)`

```ts
function normalizePath(path: string): string
```

Normalisiert URL-Pfade (entfernt doppelte Slashes, etc.).

---

### `isTechnicalPath(path)`

```ts
function isTechnicalPath(path: string): boolean
```

Prüft ob der Pfad ein technischer Shopware-Pfad ist (beginnt mit `/navigation/`, `/detail/`, etc.).

---

## URL-Utilities

### `relativeUrlSlash(url, slash?)`

```ts
function relativeUrlSlash(url: string, slash?: boolean): string
```

`slash = true` (Standard): führenden `/` hinzufügen.
`slash = false`: führenden `/` entfernen.

---

### `urlIsAbsolute(url)`

```ts
function urlIsAbsolute(url: string): boolean
```

→ `true` wenn URL mit `//` oder `https://` beginnt.

---

## Checkout-Hilfsfunktionen

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

## Sprach-Funktionen

### `getLanguageName(language)`

```ts
function getLanguageName(language: Partial<Schemas["Language"]>): string
```

→ `language.translationCode?.translated?.name ?? ""`

---

## B2B-Hilfsfunktionen

### `canUseQuoteActions(quote)`

```ts
function canUseQuoteActions(quote: Schemas["Quote"]): boolean
```

→ `true` wenn `quote.stateMachineState.technicalName === "replied"`.

---

## UI-Interface-Typen

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

## Vollständige Export-Liste

```ts
// Produkt
export { getProductName, getProductUrl, getProductRoute, getMainImageUrl }
export { getProductRealPrice, getProductFromPrice, getProductCalculatedListingPrice }
export { getProductRatingAverage, getProductReviews, getProductManufacturerName }
export { getProductTierPrices, getProductFreeShipping, isProductOnSale, isProductTopSeller }

// Kategorie
export { getCategoryBreadcrumbs, getCategoryImageUrl, getCategoryRoute, getCategoryUrl }

// CMS
export { getCmsEntityObject, getCmsLayoutConfiguration, getCmsBreadcrumbs }
export { getCmsTranslate, getProductListingFromCmsPage }
export { buildUrlPrefix, getBackgroundImageUrl }
export { isProduct, isCategory, isLandingPage, isMaintenanceMode }
export { helpersCssClasses }
export type { HelpersCssClasses }

// Media
export { getBiggestThumbnailUrl, getSmallestThumbnailUrl, getMedia }
export { getSrcSetForMedia, encodeUrlPath, generateCdnSrcSet, buildCdnImageUrl }
export { downloadFile }

// Preis
export { getFormattedPrice }

// Listing
export { getListingFilters }

// Routing
export { getRouteFromPathInfo, normalizePath, isTechnicalPath }
export type { RouteNameFromPathInfo, RouteInfoFromPathInfo, UrlRouteOutput }

// URL
export { relativeUrlSlash, urlIsAbsolute }

// Checkout
export { getPaymentMethodIcon, getShippingMethodIcon, getShippingMethodDeliveryTime }

// Sprache
export { getLanguageName }

// Übersetzung
export { getTranslatedProperty }

// B2B
export { canUseQuoteActions }

// UI-Typen
export type { UiMediaGalleryItemUrl, UiMediaGalleryItem }
export type { UiProductOption, UiProductProperty, UiProductReview, TierPrice }
```
