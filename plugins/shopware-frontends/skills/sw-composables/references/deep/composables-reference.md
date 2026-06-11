# @shopware/composables — Vollständige API-Referenz

Version: **1.11.1**

Alle Composables setzen einen via `createShopwareContext()` bereitgestellten `apiClient` voraus.

---

## Setup & Kontext-Bereitstellung

### `createShopwareContext(app, options)`

Installiert das Shopware Vue-Plugin in der App-Instanz.

```ts
import { createShopwareContext } from '@shopware/composables'

createShopwareContext(app, {
  apiClient,              // createAPIClient<operations>(...) Instanz — Pflicht
  devStorefrontUrl?: string,  // URL des Twig-Storefronts für Dev-Links
  enableDevtools?: boolean,   // Vue-Devtools-Integration
  browserLocale?: string,     // z.B. "de-DE" für Preisformatierung
  cacheableReads?: boolean,   // GET-Anfragen cachen (default: false)
})
```

### `useShopwareContext(): ShopwareContext`

```ts
const { apiClient, devStorefrontUrl, browserLocale, cacheableReads } = useShopwareContext()
```

### `useContext<T>(injectionName, params?)`

Interner shared-State-Helper. Erstellt (mit `params.context`) oder liest ein shared reactive `Ref<T>`.

---

## Cart & Warenkorb

### `useCart` — Shared Composable

`useCart` ist ein `createSharedComposable` — alle Komponenten teilen denselben State.

```ts
const {
  cart,
  cartItems,
  count,
  isEmpty,
  isVirtualCart,
  totalPrice,
  subtotal,
  shippingCosts,
  shippingTotal,         // DEPRECATED → shippingCosts verwenden
  appliedPromotionCodes,
  refreshCart,
  addProduct,
  addProducts,
  addPromotionCode,
  removeItem,
  removeItemById,
  changeProductQuantity,
  consumeCartErrors,
} = useCart()
```

| Member | Typ | Beschreibung |
|---|---|---|
| `cart` | `ComputedRef<Schemas["Cart"] \| undefined>` | Warenkorb-Objekt |
| `cartItems` | `ComputedRef<Schemas["LineItem"][]>` | Alle Positionen |
| `count` | `ComputedRef<number>` | Gesamtanzahl (ohne Promotions) |
| `isEmpty` | `ComputedRef<boolean>` | `count <= 0` |
| `isVirtualCart` | `ComputedRef<boolean>` | Alle nicht-Promotion-Items sind Downloads |
| `totalPrice` | `ComputedRef<number>` | Gesamtpreis inkl. Versand |
| `subtotal` | `ComputedRef<number>` | Positionspreise ohne Versand |
| `shippingCosts` | `ComputedRef<Schemas["CartDelivery"][]>` | Lieferungen mit Versandkosten |
| `appliedPromotionCodes` | `ComputedRef<Schemas["LineItem"][]>` | Aktive Gutscheine |
| `refreshCart(newCart?)` | `Promise<Schemas["Cart"]>` | Cart laden oder direkt setzen |
| `addProduct({ id, quantity? })` | `Promise<Schemas["Cart"]>` | Produkt hinzufügen |
| `addProducts(items)` | `Promise<Schemas["Cart"]>` | Mehrere Produkte auf einmal |
| `addPromotionCode(code)` | `Promise<Schemas["Cart"]>` | Promotion-Code einlösen |
| `removeItem(lineItem)` | `Promise<Schemas["Cart"]>` | Position entfernen |
| `removeItemById(id)` | `Promise<Schemas["Cart"]>` | Per ID entfernen |
| `changeProductQuantity({ id, quantity })` | `Promise<Schemas["Cart"]>` | Menge ändern |
| `consumeCartErrors()` | `Schemas["Cart"]["errors"]` | Fehler lesen & löschen |

**Beispiel:**
```ts
const { addProduct, count, totalPrice } = useCart()
await addProduct({ id: '550e8400-...', quantity: 2 })
console.log(count.value, totalPrice.value)
```

---

### `useCartItem(cartItem: Ref<Schemas["LineItem"]>)`

Composable für eine einzelne Warenkorb-Position.

| Member | Typ |
|---|---|
| `itemRegularPrice` | `ComputedRef<number \| undefined>` |
| `itemSpecialPrice` | `ComputedRef<number \| undefined>` |
| `itemTotalPrice` | `ComputedRef<number \| undefined>` |
| `itemImageThumbnailUrl` | `ComputedRef<string>` |
| `itemOptions` | `ComputedRef<...>` |
| `itemType` | `ComputedRef<LineItem["type"] \| undefined>` |
| `itemQuantity` | `ComputedRef<number \| undefined>` |
| `itemStock` | `ComputedRef<number \| undefined>` |
| `isProduct` | `ComputedRef<boolean>` |
| `isPromotion` | `ComputedRef<boolean>` |
| `isRemovable` | `ComputedRef<boolean>` |
| `isStackable` | `ComputedRef<boolean>` |
| `isDigital` | `ComputedRef<boolean>` |
| `changeItemQuantity(quantity)` | `Promise<Schemas["Cart"]>` |
| `removeItem()` | `Promise<Schemas["Cart"]>` |

---

### `useAddToCart(product: Ref<Schemas["Product"] | undefined>)`

UI-State für einen "In den Warenkorb"-Button.

| Member | Typ |
|---|---|
| `quantity` | `Ref<number>` |
| `getStock` | `ComputedRef<number \| undefined>` |
| `getAvailableStock` | `ComputedRef<number \| undefined>` |
| `isInCart` | `ComputedRef<boolean>` |
| `count` | `ComputedRef<number>` |
| `addToCart()` | `Promise<Schemas["Cart"]>` |

---

### `useCartNotification()`

| Member | Typ |
|---|---|
| `codeErrorsNotification()` | `void` — pusht Notifications für Cart-Fehler |
| `getErrorsCodes()` | `Schemas["CartError"][]` |

---

### `useCartErrorParamsResolver()`

| Member | Typ |
|---|---|
| `resolveCartError(error)` | `{ params, messageKey }` |

---

## Checkout

### `useCheckout()`

```ts
const {
  shippingMethods,
  paymentMethods,
  shippingAddress,
  billingAddress,
  selectedShippingMethod,
  selectedPaymentMethod,
  getShippingMethods,
  getPaymentMethods,
  createOrder,
  setShippingMethod,
  setPaymentMethod,
} = useCheckout()
```

| Member | Typ |
|---|---|
| `shippingMethods` | `ComputedRef<Schemas["ShippingMethod"][]>` |
| `paymentMethods` | `ComputedRef<Schemas["PaymentMethod"][]>` |
| `shippingAddress` | `ComputedRef<Schemas["CustomerAddress"] \| undefined>` |
| `billingAddress` | `ComputedRef<Schemas["CustomerAddress"] \| undefined>` |
| `selectedShippingMethod` | `ComputedRef<Schemas["ShippingMethod"] \| null>` |
| `selectedPaymentMethod` | `ComputedRef<Schemas["PaymentMethod"] \| null>` |
| `getShippingMethods({ forceReload? })` | `Promise<ComputedRef<ShippingMethod[]>>` |
| `getPaymentMethods({ forceReload? })` | `Promise<ComputedRef<PaymentMethod[]>>` |
| `createOrder(params?)` | `Promise<Schemas["Order"]>` |
| `setShippingMethod({ id })` | `Promise<void>` |
| `setPaymentMethod({ id })` | `Promise<void>` |

---

## Session & Kontext

### `useSessionContext(newContext?)`

Liest und schreibt den `SalesChannelContext`.

```ts
const {
  sessionContext,
  userFromContext,
  selectedShippingMethod,
  selectedPaymentMethod,
  currency,
  activeShippingAddress,
  activeBillingAddress,
  taxState,
  countryId,
  salesChannelCountryId,
  salesChannelLanguageId,
  currentLanguageId,
  refreshSessionContext,
  setShippingMethod,
  setPaymentMethod,
  setCurrency,
  setLanguage,
  setCountry,
  setActiveShippingAddress,
  setActiveBillingAddress,
  setContext,
  // deprecated:
  languageId,
  languageIdChain,
} = useSessionContext()
```

| Member | Typ | Hinweis |
|---|---|---|
| `sessionContext` | `ComputedRef<Schemas["SalesChannelContext"] \| undefined>` | |
| `userFromContext` | `ComputedRef<Schemas["Customer"] \| undefined \| null>` | |
| `currency` | `ComputedRef<Schemas["Currency"] \| null>` | |
| `taxState` | `ComputedRef<string \| undefined>` | `"gross"` oder `"net"` |
| `countryId` | `ComputedRef<string \| undefined>` | Land des Kunden |
| `salesChannelCountryId` | `ComputedRef<string \| undefined>` | Standard-Land des Sales-Channel |
| `salesChannelLanguageId` | `ComputedRef<string \| undefined>` | Aktuelle Sprache |
| `currentLanguageId` | `ComputedRef<string \| undefined>` | Alias für `salesChannelLanguageId` |
| `languageId` | `ComputedRef<string \| undefined>` | **DEPRECATED** |
| `languageIdChain` | `ComputedRef<string>` | **DEPRECATED** |
| `refreshSessionContext()` | `Promise<void>` | Context neu laden |
| `setCurrency(currency)` | `Promise<void>` | Währung wechseln |
| `setLanguage(language)` | `Promise<void>` | Sprache wechseln |
| `setCountry(countryId)` | `Promise<void>` | |
| `setShippingMethod(method)` | `Promise<void>` | |
| `setPaymentMethod(method)` | `Promise<void>` | |
| `setActiveShippingAddress(address)` | `Promise<void>` | |
| `setActiveBillingAddress(address)` | `Promise<void>` | |
| `setContext(context)` | `void` | Lokaler State-Update ohne API-Call |

---

## Nutzer & Account

### `useUser()`

```ts
const {
  user,
  isLoggedIn,
  isCustomerSession,
  isGuestSession,
  country,
  salutation,
  defaultBillingAddressId,
  defaultShippingAddressId,
  userDefaultPaymentMethod,
  userDefaultBillingAddress,
  userDefaultShippingAddress,
  login,
  register,
  logout,
  refreshUser,
  loadCountry,
  loadSalutation,
  updatePersonalInfo,
  updateEmail,
  setDefaultPaymentMethod, // DEPRECATED in SW 6.7
} = useUser()
```

| Member | Typ |
|---|---|
| `user` | `ComputedRef<Schemas["Customer"] \| undefined>` |
| `isLoggedIn` | `ComputedRef<boolean>` |
| `isCustomerSession` | `ComputedRef<boolean>` |
| `isGuestSession` | `ComputedRef<boolean>` |
| `login({ username, password })` | `Promise<void>` |
| `register(params)` | `Promise<Schemas["Customer"]>` |
| `logout()` | `Promise<response>` |
| `refreshUser(params?)` | `Promise<Schemas["Customer"]>` |
| `updatePersonalInfo(personals)` | `Promise<void>` |
| `updateEmail(data)` | `Promise<void>` |

---

### `useAddress()`

| Member | Typ |
|---|---|
| `customerAddresses` | `ComputedRef<Schemas["CustomerAddress"][]>` |
| `loadCustomerAddresses()` | `Promise<Schemas["CustomerAddress"][]>` |
| `createCustomerAddress(address)` | `Promise<Schemas["CustomerAddress"]>` |
| `updateCustomerAddress(address)` | `Promise<Schemas["CustomerAddress"]>` |
| `deleteCustomerAddress(addressId)` | `Promise<void>` |
| `setDefaultCustomerBillingAddress(id)` | `Promise<string>` |
| `setDefaultCustomerShippingAddress(id)` | `Promise<string>` |
| `errorMessageBuilder(error)` | `string \| null` |

---

### `useCustomerOrders()`

| Member | Typ |
|---|---|
| `orders` | `Ref<Schemas["Order"][]>` |
| `currentPage` | `ComputedRef<number>` |
| `totalPages` | `ComputedRef<number>` |
| `limit` | `Ref<number>` |
| `loadOrders(parameters?)` | `Promise<void>` |
| `changeCurrentPage(page)` | `Promise<void>` |

---

### `useCustomerPassword()`

| Member | Typ |
|---|---|
| `updatePassword(data)` | `Promise<response>` |
| `resetPassword(data)` | `Promise<response>` |

---

### `useOrderDetails(orderId, associations?)`

```ts
const {
  order, status, statusTechnicalName,
  total, subtotal, shippingCosts,
  shippingAddress, billingAddress,
  personalDetails, paymentUrl,
  shippingMethod, paymentMethod,
  hasDocuments, documents,
  paymentChangeable,
  loadOrderDetails,
  handlePayment,
  cancel,
  changePaymentMethod,
  getMediaFile,
  getDocumentFile,
  getPaymentMethods,
} = useOrderDetails(orderId)
```

| Member | Typ |
|---|---|
| `order` | `ComputedRef<Schemas["Order"] \| undefined \| null>` |
| `status` | `ComputedRef<string \| undefined>` |
| `loadOrderDetails()` | `Promise<Schemas["OrderRouteResponse"]>` |
| `handlePayment(successUrl?, errorUrl?, paymentDetails?)` | `void` |
| `cancel()` | `Promise<Schemas["StateMachineState"]>` |
| `changePaymentMethod(id)` | `Promise<Schemas["SuccessResponse"]>` |
| `getMediaFile(downloadId)` | `Promise<Blob>` |
| `getDocumentFile(documentId, deepLinkCode)` | `Promise<Blob \| string>` |

---

### `useOrderPayment(order: ComputedRef<...>)`

| Member | Typ |
|---|---|
| `isAsynchronous` | `ComputedRef<boolean \| undefined>` |
| `activeTransaction` | `ComputedRef<Schemas["OrderTransaction"] \| undefined>` |
| `state` | `ComputedRef<Schemas["StateMachineState"] \| null \| undefined>` |
| `paymentUrl` | `Ref<null \| string>` |
| `paymentMethod` | `ComputedRef<Schemas["PaymentMethod"] \| undefined \| null>` |
| `handlePayment(successUrl?, errorUrl?, paymentDetails?)` | `Promise<unknown>` |
| `changePaymentMethod(id)` | `Promise<Schemas["SuccessResponse"] \| undefined>` |

---

### `useDefaultOrderAssociations()`

Gibt ein Standard-Associations-Objekt für Order-Abfragen zurück:

```ts
// Enthält: stateMachineState, lineItems.cover, lineItems.downloads,
//           addresses, deliveries, transactions.paymentMethod
const associations = useDefaultOrderAssociations()
```

---

### `useSalutations()`

| Member | Typ |
|---|---|
| `getSalutations` | `ComputedRef<Schemas["Salutation"][]>` |
| `fetchSalutations()` | `Promise<response>` |

---

### `useCountries()`

| Member | Typ |
|---|---|
| `getCountries` | `ComputedRef<Schemas["Country"][]>` |
| `getCountriesOptions` | `ComputedRef<{ label: string; value: string }[]>` |
| `mountedCallback()` | `Promise<void>` |
| `fetchCountries()` | `Promise<response>` |
| `getStatesForCountry(countryId)` | `Schemas["CountryState"][] \| null` |

---

## Produkte

### `useProduct(product?, configurator?)`

Wirft `ContextError` wenn kein Produkt im Context.

| Member | Typ |
|---|---|
| `product` | `ComputedRef<Schemas["Product"]>` |
| `configurator` | `ComputedRef<Schemas["PropertyGroup"][]>` |
| `changeVariant(variant?)` | `void` |

---

### `useProductSearch()`

```ts
const { search } = useProductSearch()

const result = await search(productId, {
  withCmsAssociations: true,     // lädt CMS-Assoziationen mit
  criteria: { includes: { product: ['id', 'name'] } },
  associations: { manufacturer: {} }
})
// result: Schemas["ProductDetailResponse"]
```

---

### `useProductPrice(product: Ref<Schemas["Product"] | undefined>)`

| Member | Typ |
|---|---|
| `price` | `ComputedRef<Schemas["CalculatedPrice"] \| undefined>` |
| `totalPrice` | `ComputedRef<number \| undefined>` |
| `unitPrice` | `ComputedRef<number \| undefined>` |
| `referencePrice` | `ComputedRef<CalculatedPrice["referencePrice"] \| undefined>` |
| `displayFrom` | `ComputedRef<boolean>` — true wenn mehrere Tier-Preise |
| `displayFromVariants` | `ComputedRef<number \| false \| undefined>` |
| `tierPrices` | `ComputedRef<TierPrice[]>` |
| `hasListPrice` | `ComputedRef<boolean>` |
| `isListPrice` | `ComputedRef<boolean>` — **DEPRECATED**, `hasListPrice` nutzen |
| `regulationPrice` | `ComputedRef<number \| undefined>` |

---

### `usePrice` — Shared Composable

```ts
const { currencyCode, currencyLocale, getFormattedPrice, update } = usePrice()

// Preis formatieren:
const formatted = getFormattedPrice(19.99)  // → "19,99 €" (je nach Locale)

// Währung/Locale aktualisieren:
update({ currencyCode: 'USD', localeCode: 'en-US' })
```

---

### `useProductConfigurator()`

| Member | Typ |
|---|---|
| `isLoadingOptions` | `Ref<boolean>` |
| `getSelectedOptions` | `ComputedRef<{ [groupId: string]: string }>` |
| `getOptionGroups` | `ComputedRef<Schemas["PropertyGroup"][]>` |
| `handleChange(attribute, option, onChangeHandled?)` | `Promise<void>` |
| `findVariantForSelectedOptions(options?)` | `Promise<Schemas["Product"] \| undefined>` |

---

### `useProductAssociations(product, options)`

```ts
const { isLoading, productAssociations, loadAssociations } = useProductAssociations(product, {
  associationContext: 'cross-selling',  // oder 'reviews'
  includeSeoUrls: true
})
await loadAssociations({ params: { limit: 5 } })
```

---

### `useProductReviews(product: Ref<Schemas["Product"]>)`

| Member | Typ |
|---|---|
| `productReviews` | `ComputedRef<Schemas["ProductReview"][]>` |
| `loadProductReviews(parameters?)` | `Promise<response>` |
| `addReview({ title, content, points })` | `Promise<void>` |

---

### `useProductSearchSuggest()`

| Member | Typ |
|---|---|
| `searchTerm` | `Ref<string>` |
| `loading` | `ComputedRef<boolean>` |
| `getProducts` | `ComputedRef<ProductListingResult["elements"]>` |
| `getTotal` | `ComputedRef<number>` |
| `search(additionalCriteria?)` | `Promise<void>` |
| `loadMore(criteria)` | `Promise<void>` |

---

## Listing & Suche

### `useListing(params?)`

```ts
const listing = useListing({
  listingType: 'categoryListing',   // oder 'productSearchListing'
  categoryId: 'uuid...',
  initialListing: serverSideFetchedListing,
})
```

| Member | Typ |
|---|---|
| `getInitialListing` | `ComputedRef<ProductListingResult \| null>` |
| `getCurrentListing` | `ComputedRef<ProductListingResult \| null>` |
| `getElements` | `ComputedRef<ProductListingResult["elements"]>` |
| `getTotal` | `ComputedRef<number>` |
| `getTotalPagesCount` | `ComputedRef<number>` |
| `getLimit` | `ComputedRef<number>` |
| `getCurrentPage` | `ComputedRef<number>` |
| `getCurrentSortingOrder` | `ComputedRef<string \| undefined>` |
| `getSortingOrders` | `ComputedRef<ProductSorting[]>` |
| `getCurrentFilters` | `ComputedRef<...currentFilters>` |
| `getInitialFilters` | `ComputedRef<ListingFilter[]>` |
| `getAvailableFilters` | `ComputedRef<ListingFilter[]>` |
| `loading` | `ComputedRef<boolean>` |
| `loadingMore` | `ComputedRef<boolean>` |
| `setInitialListing(listing)` | `Promise<void>` |
| `search(criteria)` | `Promise<void>` |
| `initSearch(criteria)` | `Promise<ProductListingResult>` — **DEPRECATED** |
| `loadMore(criteria?)` | `Promise<void>` |
| `changeCurrentSortingOrder(order, query?)` | `Promise<void>` |
| `changeCurrentPage(page, query?)` | `Promise<void>` |
| `setCurrentFilters(filters)` | `Promise<void>` |
| `resetFilters()` | `Promise<void>` |
| `filtersToQuery(filters)` | `Record<string, unknown>` |

### `createCategoryListingContext` + `useCategoryListing()`

```ts
// Im Parent (z.B. CmsPage.vue — wird dort intern aufgerufen):
import { createCategoryListingContext } from '@shopware/composables'
createCategoryListingContext(initialListing)

// Im Kind-Composable:
const listing = useCategoryListing()
```

### `useProductSearchListing` — Shared

```ts
// Geteilter State für Suchergebnis-Listing
const listing = useProductSearchListing()
```

### `createListingComposable(options)` — Factory

```ts
const myListing = createListingComposable({
  searchMethod: async (criteria) => apiClient.invoke('...', criteria),
  searchDefaults: { limit: 24 },
  listingKey: 'myCustomListing',
  initialListing: null,
})
```

---

## Navigation & Routing

### `useNavigation(params?)`

```ts
const { navigationElements, loadNavigationElements } = useNavigation({
  type: 'main-navigation'   // Standard; auch: 'footer-navigation', 'service-navigation'
})

const elements = await loadNavigationElements({ depth: 2 })
```

---

### `useNavigationContext(context?)`

| Member | Typ |
|---|---|
| `navigationContext` | `ComputedRef<Schemas["SeoUrl"] \| null>` |
| `routeName` | `ComputedRef<SeoUrl["routeName"] \| undefined>` |
| `foreignKey` | `ComputedRef<string>` |

---

### `useNavigationSearch()`

```ts
const { resolvePath } = useNavigationSearch()
const seoUrl = await resolvePath('/meine-kategorie/produkt-slug')
// → Schemas["SeoUrl"] | null
```

---

### `useCategorySearch()`

```ts
const { search, advancedSearch } = useCategorySearch()

// Einzelne Kategorie laden:
const category = await search(categoryId, { withCmsAssociations: true })

// Mehrere Kategorien laden:
const categories = await advancedSearch({ criteria: { filter: [...] } })
```

---

### `useLandingSearch()`

```ts
const { search } = useLandingSearch()
const landing = await search(navigationId, { withCmsAssociations: true })
```

---

### `useCategory(category?)`

| Member | Typ |
|---|---|
| `category` | `ComputedRef<Schemas["Category"]>` |

Wirft `ContextError` wenn kein Produkt im Context.

---

### `useBreadcrumbs(newBreadcrumbs?)`

| Member | Typ |
|---|---|
| `breadcrumbs` | `ComputedRef<Breadcrumb[]>` |
| `clearBreadcrumbs()` | `void` |
| `pushBreadcrumb(breadcrumb)` | `void` |
| `buildDynamicBreadcrumbs(breadcrumbs)` | `Promise<void>` |

---

### `useUrlResolver()`

| Member | Typ |
|---|---|
| `getUrlPrefix()` | `string` — aktuelles Sprachpräfix |
| `resolveUrl(url)` | `string` — URL mit Sprachpräfix |

---

### `useInternationalization(pathResolver?)`

| Member | Typ |
|---|---|
| `languages` | `Ref<Schemas["Language"][]>` |
| `currentLanguage` | `Ref<string>` |
| `currentPrefix` | `Ref<string>` |
| `getStorefrontUrl()` | `string` |
| `getAvailableLanguages()` | `Promise<response>` |
| `changeLanguage(languageId)` | `Promise<response>` |
| `getLanguageCodeFromId(id)` | `string` |
| `getLanguageIdFromCode(code)` | `string` |
| `replaceToDevStorefront(url)` | `string` |
| `formatLink(link)` | `string \| RouteObject` |

---

## Wishlist

### `useWishlist()`

Kombiniert lokale Wishlist und API-Wishlist (wenn eingeloggt).

| Member | Typ |
|---|---|
| `items` | `ComputedRef<string[]>` — Produkt-IDs |
| `products` | `ComputedRef<Schemas["Product"][]>` |
| `count` | `ComputedRef<number>` |
| `currentPage` | `ComputedRef<number>` |
| `totalPagesCount` | `ComputedRef<number>` |
| `limit` | `ComputedRef<number>` |
| `canSyncWishlist` | `ComputedRef<boolean>` |
| `getWishlistProducts(query?)` | `Promise<void>` |
| `clearWishlist()` | `void` |
| `mergeWishlistProducts()` | `void` |

---

### `useProductWishlist(productId: string)`

| Member | Typ |
|---|---|
| `isInWishlist` | `ComputedRef<boolean>` |
| `addToWishlist()` | `Promise<void>` |
| `removeFromWishlist()` | `Promise<void>` |

---

### `useLocalWishlist()`

| Member | Typ |
|---|---|
| `items` | `ComputedRef<string[]>` |
| `count` | `ComputedRef<number>` |
| `getWishlistProducts()` | `void` — aus localStorage |
| `addToWishlist(id)` | `Promise<void>` |
| `removeFromWishlist(id)` | `Promise<void>` |
| `clearWishlist()` | `Promise<void>` |

---

### `useSyncWishlist()`

| Member | Typ |
|---|---|
| `items` | `ComputedRef<string[]>` |
| `products` | `ComputedRef<Schemas["Product"][]>` |
| `count` | `ComputedRef<number>` |
| `isLoading` | `Ref<boolean>` |
| `getWishlistProducts(criteria?)` | `Promise<void>` |
| `addToWishlistSync(id)` | `void` |
| `removeFromWishlistSync(id)` | `void` |
| `mergeWishlistProducts(items)` | `void` |

---

## Notifications

### `useNotifications()`

```ts
const { notifications, pushInfo, pushSuccess, pushWarning, pushError, removeOne, removeAll } = useNotifications()

pushError('Fehler beim Laden', { timeout: 3000 })
pushSuccess('Produkt hinzugefügt!')
```

```ts
type Notification = {
  type: 'info' | 'warning' | 'success' | 'danger'
  message: string
  id: number
}

type NotificationOptions = {
  type?: Notification['type']
  timeout?: number       // ms, nach denen die Notification automatisch verschwindet
  persistent?: boolean   // nicht auto-entfernen
}
```

---

## Newsletter

### `useNewsletter()`

| Member | Typ |
|---|---|
| `newsletterStatus` | `Ref<Schemas["AccountNewsletterRecipient"]["status"]>` |
| `isNewsletterSubscriber` | `ComputedRef<boolean>` |
| `confirmationNeeded` | `ComputedRef<boolean>` |
| `SUBSCRIBE_KEY` | `string` |
| `UNSUBSCRIBE_KEY` | `string` |
| `newsletterSubscribe(params)` | `Promise<response>` |
| `newsletterUnsubscribe(email)` | `Promise<void>` |
| `getNewsletterStatus()` | `Promise<Schemas["AccountNewsletterRecipient"]>` |

---

## CMS-Composables

### `useCmsBlock<BLOCK_TYPE>(content)`

```ts
const { block, getSlotContent } = useCmsBlock(props.content)
const mainSlot = getSlotContent('main')
```

---

### `useCmsSection<SECTION_TYPE>(content)`

```ts
const { section, getPositionContent } = useCmsSection(props.content)
const mainBlocks = getPositionContent('main')
const sidebarBlocks = getPositionContent('sidebar')
```

---

### `useCmsMeta(entity)`

```ts
const { title, meta } = useCmsMeta(category)
// title: "Kategoriename | Shop"
// meta: [{ name: 'description', content: '...' }]
```

---

### `useCmsTranslations()`

Gibt das injizierte `cmsTranslations`-Objekt zurück (Standard: `{}`).

---

### `useCmsElementConfig<T>(element)`

```ts
const { getConfigValue } = useCmsElementConfig(element)
const displayMode = getConfigValue('displayMode')
```

---

### `useCmsElementImage(element)`

```ts
const {
  containerStyle,
  anchorAttrs,
  imageAttrs,
  imageContainerAttrs,
  imageLink,
  displayMode,
  isVideoElement,
  mimeType,
} = useCmsElementImage(element)
```

---

### `useCmsElementProductBox(element)`

```ts
const { product, boxLayout } = useCmsElementProductBox(element)
```

---

### `resolveCmsComponent(content)`

```ts
import { resolveCmsComponent } from '@shopware/composables'

const { resolvedComponent, componentName, isResolved, componentNameToResolve } =
  resolveCmsComponent(cmsSlot)
// → componentName z.B. "CmsElementText"
// → resolvedComponent: aufgelöste Vue-Komponente oder string wenn nicht gefunden
```

---

## B2B

### `useB2bQuoteManagement()`

| Member | Typ |
|---|---|
| `getQuoteList()` | `Promise<Schemas["Quote"][]>` |
| `getQuote(quoteId)` | `Promise<Schemas["Quote"]>` |
| `declineQuote(quoteId, comment)` | `Promise<void>` |
| `requestChangeQuote(quoteId, comment)` | `Promise<void>` |
| `requestQuote(comment)` | `Promise<Schemas["Quote"]>` |
| `createOrderFromQuote(quoteId, comment)` | `Promise<Schemas["Order"]>` |
| `changeShippingMethod(quoteId, shippingMethodId)` | `Promise<void>` |
| `changePaymentMethod(quoteId, paymentMethodId)` | `Promise<void>` |

---

## CMS-Assoziationen

Das Objekt `cmsAssociations` (aus `@shopware/composables`) enthält tiefe Assoziationsdefinitionen für die CMS-Page-Abfrage:

```ts
import { cmsAssociations } from '@shopware/composables'

// Verwendung mit useProductSearch:
await search(productId, { withCmsAssociations: true })
// Intern: criteria.associations = cmsAssociations
```

---

## Vollständige Export-Liste

Alle öffentlichen Exports von `@shopware/composables`:

```ts
// Context
export { createShopwareContext, useShopwareContext, useContext }

// Cart
export { useCart, useCartItem, useAddToCart, useCartNotification, useCartErrorParamsResolver }

// Checkout
export { useCheckout }

// Session
export { useSessionContext }

// User/Account
export { useUser, useAddress, useCustomerOrders, useCustomerPassword }
export { useSalutations, useCountries }
export { useOrderDetails, useOrderPayment, useDefaultOrderAssociations }

// Product
export { useProduct, useProductSearch, useProductPrice, useProductConfigurator }
export { useProductAssociations, useProductReviews, useProductSearchSuggest }
export { usePrice }

// Listing
export { useListing, useCategoryListing, useProductSearchListing }
export { createCategoryListingContext, createListingComposable }

// Navigation
export { useNavigation, useNavigationContext, useNavigationSearch }
export { useCategorySearch, useCategory, useLandingSearch }
export { useBreadcrumbs, useUrlResolver, useInternationalization }

// Wishlist
export { useWishlist, useProductWishlist, useLocalWishlist, useSyncWishlist }

// Misc
export { useNotifications, useNewsletter, useB2bQuoteManagement }

// CMS
export { useCmsBlock, useCmsSection, useCmsMeta, useCmsTranslations }
export { useCmsElementConfig, useCmsElementImage, useCmsElementProductBox }
export { resolveCmsComponent, cmsAssociations }

// Types (re-exports aus @shopware/api-client)
export type { Schemas, operations }
// + alle CmsElement*, CmsBlock*, CmsSection* Typen
```
