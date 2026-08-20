# @shopware/composables — Complete API reference

Version: **1.11.1**

All composables require an `apiClient` provided via `createShopwareContext()`.

---

## Contents

- [Setup & context provisioning](#setup-context-provisioning)
- [Cart & shopping cart](#cart-shopping-cart)
- [Checkout](#checkout)
- [Session & context](#session-context)
- [User & account](#user-account)
- [Products](#products)
- [Listing & search](#listing-search)
- [Navigation & routing](#navigation-routing)
- [Wishlist](#wishlist)
- [Notifications](#notifications)
- [Newsletter](#newsletter)
- [CMS composables](#cms-composables)
- [B2B](#b2b)
- [CMS associations](#cms-associations)
- [Complete export list](#complete-export-list)

## Setup & context provisioning

### `createShopwareContext(app, options)`

Installs the Shopware Vue plugin into the app instance.

```ts
import { createShopwareContext } from '@shopware/composables'

createShopwareContext(app, {
  apiClient,              // createAPIClient<operations>(...) instance — mandatory
  devStorefrontUrl?: string,  // URL of the Twig storefront for dev links
  enableDevtools?: boolean,   // Vue devtools integration
  browserLocale?: string,     // e.g. "de-DE" for price formatting
  cacheableReads?: boolean,   // cache GET requests (default: false)
})
```

### `useShopwareContext(): ShopwareContext`

```ts
const { apiClient, devStorefrontUrl, browserLocale, cacheableReads } = useShopwareContext()
```

### `useContext<T>(injectionName, params?)`

Internal shared-state helper. Creates (with `params.context`) or reads a shared reactive `Ref<T>`.

---

## Cart & shopping cart

### `useCart` — shared composable

`useCart` is a `createSharedComposable` — all components share the same state.

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
  shippingTotal,         // DEPRECATED → use shippingCosts
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

| Member | Type | Description |
|---|---|---|
| `cart` | `ComputedRef<Schemas["Cart"] \| undefined>` | Cart object |
| `cartItems` | `ComputedRef<Schemas["LineItem"][]>` | All line items |
| `count` | `ComputedRef<number>` | Total quantity (excluding promotions) |
| `isEmpty` | `ComputedRef<boolean>` | `count <= 0` |
| `isVirtualCart` | `ComputedRef<boolean>` | All non-promotion items are downloads |
| `totalPrice` | `ComputedRef<number>` | Total price including shipping |
| `subtotal` | `ComputedRef<number>` | Line item prices without shipping |
| `shippingCosts` | `ComputedRef<Schemas["CartDelivery"][]>` | Deliveries with shipping costs |
| `appliedPromotionCodes` | `ComputedRef<Schemas["LineItem"][]>` | Active vouchers |
| `refreshCart(newCart?)` | `Promise<Schemas["Cart"]>` | Load the cart or set it directly |
| `addProduct({ id, quantity? })` | `Promise<Schemas["Cart"]>` | Add a product |
| `addProducts(items)` | `Promise<Schemas["Cart"]>` | Several products at once |
| `addPromotionCode(code)` | `Promise<Schemas["Cart"]>` | Redeem a promotion code |
| `removeItem(lineItem)` | `Promise<Schemas["Cart"]>` | Remove a line item |
| `removeItemById(id)` | `Promise<Schemas["Cart"]>` | Remove by ID |
| `changeProductQuantity({ id, quantity })` | `Promise<Schemas["Cart"]>` | Change the quantity |
| `consumeCartErrors()` | `Schemas["Cart"]["errors"]` | Read & clear the errors |

**Example:**
```ts
const { addProduct, count, totalPrice } = useCart()
await addProduct({ id: '550e8400-...', quantity: 2 })
console.log(count.value, totalPrice.value)
```

---

### `useCartItem(cartItem: Ref<Schemas["LineItem"]>)`

Composable for a single cart line item.

| Member | Type |
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

UI state for an "add to cart" button.

| Member | Type |
|---|---|
| `quantity` | `Ref<number>` |
| `getStock` | `ComputedRef<number \| undefined>` |
| `getAvailableStock` | `ComputedRef<number \| undefined>` |
| `isInCart` | `ComputedRef<boolean>` |
| `count` | `ComputedRef<number>` |
| `addToCart()` | `Promise<Schemas["Cart"]>` |

---

### `useCartNotification()`

| Member | Type |
|---|---|
| `codeErrorsNotification()` | `void` — pushes notifications for cart errors |
| `getErrorsCodes()` | `Schemas["CartError"][]` |

---

### `useCartErrorParamsResolver()`

| Member | Type |
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

| Member | Type |
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

## Session & context

### `useSessionContext(newContext?)`

Reads and writes the `SalesChannelContext`.

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

| Member | Type | Note |
|---|---|---|
| `sessionContext` | `ComputedRef<Schemas["SalesChannelContext"] \| undefined>` | |
| `userFromContext` | `ComputedRef<Schemas["Customer"] \| undefined \| null>` | |
| `currency` | `ComputedRef<Schemas["Currency"] \| null>` | |
| `taxState` | `ComputedRef<string \| undefined>` | `"gross"` or `"net"` |
| `countryId` | `ComputedRef<string \| undefined>` | Country of the customer |
| `salesChannelCountryId` | `ComputedRef<string \| undefined>` | Default country of the sales channel |
| `salesChannelLanguageId` | `ComputedRef<string \| undefined>` | Current language |
| `currentLanguageId` | `ComputedRef<string \| undefined>` | Alias for `salesChannelLanguageId` |
| `languageId` | `ComputedRef<string \| undefined>` | **DEPRECATED** |
| `languageIdChain` | `ComputedRef<string>` | **DEPRECATED** |
| `refreshSessionContext()` | `Promise<void>` | Reload the context |
| `setCurrency(currency)` | `Promise<void>` | Switch the currency |
| `setLanguage(language)` | `Promise<void>` | Switch the language |
| `setCountry(countryId)` | `Promise<void>` | |
| `setShippingMethod(method)` | `Promise<void>` | |
| `setPaymentMethod(method)` | `Promise<void>` | |
| `setActiveShippingAddress(address)` | `Promise<void>` | |
| `setActiveBillingAddress(address)` | `Promise<void>` | |
| `setContext(context)` | `void` | Local state update without an API call |

---

## User & account

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

| Member | Type |
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

| Member | Type |
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

| Member | Type |
|---|---|
| `orders` | `Ref<Schemas["Order"][]>` |
| `currentPage` | `ComputedRef<number>` |
| `totalPages` | `ComputedRef<number>` |
| `limit` | `Ref<number>` |
| `loadOrders(parameters?)` | `Promise<void>` |
| `changeCurrentPage(page)` | `Promise<void>` |

---

### `useCustomerPassword()`

| Member | Type |
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

| Member | Type |
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

| Member | Type |
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

Returns a default associations object for order queries:

```ts
// Contains: stateMachineState, lineItems.cover, lineItems.downloads,
//           addresses, deliveries, transactions.paymentMethod
const associations = useDefaultOrderAssociations()
```

---

### `useSalutations()`

| Member | Type |
|---|---|
| `getSalutations` | `ComputedRef<Schemas["Salutation"][]>` |
| `fetchSalutations()` | `Promise<response>` |

---

### `useCountries()`

| Member | Type |
|---|---|
| `getCountries` | `ComputedRef<Schemas["Country"][]>` |
| `getCountriesOptions` | `ComputedRef<{ label: string; value: string }[]>` |
| `mountedCallback()` | `Promise<void>` |
| `fetchCountries()` | `Promise<response>` |
| `getStatesForCountry(countryId)` | `Schemas["CountryState"][] \| null` |

---

## Products

### `useProduct(product?, configurator?)`

Throws `ContextError` when there is no product in the context.

| Member | Type |
|---|---|
| `product` | `ComputedRef<Schemas["Product"]>` |
| `configurator` | `ComputedRef<Schemas["PropertyGroup"][]>` |
| `changeVariant(variant?)` | `void` |

---

### `useProductSearch()`

```ts
const { search } = useProductSearch()

const result = await search(productId, {
  withCmsAssociations: true,     // also loads the CMS associations
  criteria: { includes: { product: ['id', 'name'] } },
  associations: { manufacturer: {} }
})
// result: Schemas["ProductDetailResponse"]
```

---

### `useProductPrice(product: Ref<Schemas["Product"] | undefined>)`

| Member | Type |
|---|---|
| `price` | `ComputedRef<Schemas["CalculatedPrice"] \| undefined>` |
| `totalPrice` | `ComputedRef<number \| undefined>` |
| `unitPrice` | `ComputedRef<number \| undefined>` |
| `referencePrice` | `ComputedRef<CalculatedPrice["referencePrice"] \| undefined>` |
| `displayFrom` | `ComputedRef<boolean>` — true when there are several tier prices |
| `displayFromVariants` | `ComputedRef<number \| false \| undefined>` |
| `tierPrices` | `ComputedRef<TierPrice[]>` |
| `hasListPrice` | `ComputedRef<boolean>` |
| `isListPrice` | `ComputedRef<boolean>` — **DEPRECATED**, use `hasListPrice` |
| `regulationPrice` | `ComputedRef<number \| undefined>` |

---

### `usePrice` — shared composable

```ts
const { currencyCode, currencyLocale, getFormattedPrice, update } = usePrice()

// Format a price:
const formatted = getFormattedPrice(19.99)  // → "19,99 €" (depending on the locale)

// Update the currency/locale:
update({ currencyCode: 'USD', localeCode: 'en-US' })
```

---

### `useProductConfigurator()`

| Member | Type |
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
  associationContext: 'cross-selling',  // or 'reviews'
  includeSeoUrls: true
})
await loadAssociations({ params: { limit: 5 } })
```

---

### `useProductReviews(product: Ref<Schemas["Product"]>)`

| Member | Type |
|---|---|
| `productReviews` | `ComputedRef<Schemas["ProductReview"][]>` |
| `loadProductReviews(parameters?)` | `Promise<response>` |
| `addReview({ title, content, points })` | `Promise<void>` |

---

### `useProductSearchSuggest()`

| Member | Type |
|---|---|
| `searchTerm` | `Ref<string>` |
| `loading` | `ComputedRef<boolean>` |
| `getProducts` | `ComputedRef<ProductListingResult["elements"]>` |
| `getTotal` | `ComputedRef<number>` |
| `search(additionalCriteria?)` | `Promise<void>` |
| `loadMore(criteria)` | `Promise<void>` |

---

## Listing & search

### `useListing(params?)`

```ts
const listing = useListing({
  listingType: 'categoryListing',   // or 'productSearchListing'
  categoryId: 'uuid...',
  initialListing: serverSideFetchedListing,
})
```

| Member | Type |
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
// In the parent (e.g. CmsPage.vue — called there internally):
import { createCategoryListingContext } from '@shopware/composables'
createCategoryListingContext(initialListing)

// In the child composable:
const listing = useCategoryListing()
```

### `useProductSearchListing` — shared

```ts
// Shared state for the search result listing
const listing = useProductSearchListing()
```

### `createListingComposable(options)` — factory

```ts
const myListing = createListingComposable({
  searchMethod: async (criteria) => apiClient.invoke('...', criteria),
  searchDefaults: { limit: 24 },
  listingKey: 'myCustomListing',
  initialListing: null,
})
```

---

## Navigation & routing

### `useNavigation(params?)`

```ts
const { navigationElements, loadNavigationElements } = useNavigation({
  type: 'main-navigation'   // default; also: 'footer-navigation', 'service-navigation'
})

const elements = await loadNavigationElements({ depth: 2 })
```

---

### `useNavigationContext(context?)`

| Member | Type |
|---|---|
| `navigationContext` | `ComputedRef<Schemas["SeoUrl"] \| null>` |
| `routeName` | `ComputedRef<SeoUrl["routeName"] \| undefined>` |
| `foreignKey` | `ComputedRef<string>` |

---

### `useNavigationSearch()`

```ts
const { resolvePath } = useNavigationSearch()
const seoUrl = await resolvePath('/my-category/product-slug')
// → Schemas["SeoUrl"] | null
```

---

### `useCategorySearch()`

```ts
const { search, advancedSearch } = useCategorySearch()

// Load a single category:
const category = await search(categoryId, { withCmsAssociations: true })

// Load several categories:
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

| Member | Type |
|---|---|
| `category` | `ComputedRef<Schemas["Category"]>` |

Throws `ContextError` when there is no product in the context.

---

### `useBreadcrumbs(newBreadcrumbs?)`

| Member | Type |
|---|---|
| `breadcrumbs` | `ComputedRef<Breadcrumb[]>` |
| `clearBreadcrumbs()` | `void` |
| `pushBreadcrumb(breadcrumb)` | `void` |
| `buildDynamicBreadcrumbs(breadcrumbs)` | `Promise<void>` |

---

### `useUrlResolver()`

| Member | Type |
|---|---|
| `getUrlPrefix()` | `string` — current language prefix |
| `resolveUrl(url)` | `string` — URL with the language prefix |

---

### `useInternationalization(pathResolver?)`

| Member | Type |
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

Combines the local wishlist and the API wishlist (when logged in).

| Member | Type |
|---|---|
| `items` | `ComputedRef<string[]>` — product IDs |
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

| Member | Type |
|---|---|
| `isInWishlist` | `ComputedRef<boolean>` |
| `addToWishlist()` | `Promise<void>` |
| `removeFromWishlist()` | `Promise<void>` |

---

### `useLocalWishlist()`

| Member | Type |
|---|---|
| `items` | `ComputedRef<string[]>` |
| `count` | `ComputedRef<number>` |
| `getWishlistProducts()` | `void` — from localStorage |
| `addToWishlist(id)` | `Promise<void>` |
| `removeFromWishlist(id)` | `Promise<void>` |
| `clearWishlist()` | `Promise<void>` |

---

### `useSyncWishlist()`

| Member | Type |
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

pushError('Error while loading', { timeout: 3000 })
pushSuccess('Product added!')
```

```ts
type Notification = {
  type: 'info' | 'warning' | 'success' | 'danger'
  message: string
  id: number
}

type NotificationOptions = {
  type?: Notification['type']
  timeout?: number       // ms after which the notification disappears automatically
  persistent?: boolean   // do not auto-remove
}
```

---

## Newsletter

### `useNewsletter()`

| Member | Type |
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

## CMS composables

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
// title: "Category name | Shop"
// meta: [{ name: 'description', content: '...' }]
```

---

### `useCmsTranslations()`

Returns the injected `cmsTranslations` object (default: `{}`).

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
// → componentName e.g. "CmsElementText"
// → resolvedComponent: the resolved Vue component, or a string when not found
```

---

## B2B

### `useB2bQuoteManagement()`

| Member | Type |
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

## CMS associations

The `cmsAssociations` object (from `@shopware/composables`) contains deep association definitions for the CMS page query:

```ts
import { cmsAssociations } from '@shopware/composables'

// Usage with useProductSearch:
await search(productId, { withCmsAssociations: true })
// Internally: criteria.associations = cmsAssociations
```

---

## Complete export list

All public exports of `@shopware/composables`:

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

// Types (re-exports from @shopware/api-client)
export type { Schemas, operations }
// + all CmsElement*, CmsBlock*, CmsSection* types
```
