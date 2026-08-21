# Shopware Frontends – Code recipes & examples

Source: `apps/docs/src/getting-started/`

---

## Contents

- [1. Login form](#1-login-form)
- [2. Cart](#2-cart)
- [3. Checkout](#3-checkout)
- [4. Product listing](#4-product-listing)
- [5. Product detail page (PDP)](#5-product-detail-page-pdp)
- [6. Price display](#6-price-display)
- [7. Wishlist](#7-wishlist)
- [8. JSON-LD (SEO)](#8-json-ld-seo)
- [9. Payment flow (general)](#9-payment-flow-general)
- [10. B2B Quote Management](#10-b2b-quote-management)
- [11. Broadcasting (tab synchronisation)](#11-broadcasting-tab-synchronisation)
- [Navigation (breadcrumbs, navigation tree)](#navigation-breadcrumbs-navigation-tree)

## 1. Login form

```vue
<script setup lang="ts">
const { logout, login, errors, isLoggedIn, user } = useUser();
const loginCredentials = reactive({
  username: "",
  password: "",
});
const invokeLogin = () => login(loginCredentials);
</script>

<template>
  <div v-if="!isLoggedIn">
    <h1>Sign in to your account</h1>
    <input type="text" v-model="loginCredentials.username" />
    <input type="password" v-model="loginCredentials.password" />
    <button @click="invokeLogin">Sign in</button>
    <!-- error display -->
    <div v-if="errors.login.length">
      {{ errors.login[0].detail }}
    </div>
  </div>
  <div v-else>
    <h1>Hi, {{ user.firstName }}!</h1>
    <button @click="logout()">Sign out</button>
  </div>
</template>
```

**Composable `useUser` – important fields:**
- `login(credentials)` – login
- `logout()` – logout
- `errors.login` – array of API errors
- `isLoggedIn` – boolean (computed)
- `user` – customer object

StackBlitz demo: https://stackblitz.com/github/shopware/frontends/tree/main/examples/login-form

---

## 2. Cart

### Initialising the cart

```ts
const { refreshCart } = useCart();
await refreshCart();
// Automatically creates a new cart if none exists
// Internally: sw-context-token in the header
```

### Adding a product to the cart

```vue
<script setup lang="ts">
const product = { id: "7b5b97bd48454979b14f21c8ef38ce08" };
const { addProduct, quantity, getAvailableStock } = useAddToCart({ product });
</script>
<template>
  Only {{ getAvailableStock }} in stock<br />
  <input v-model="quantity" type="number" />
  <button @click="addToCart()">Add to cart</button>
</template>
```

### Adding a promotion code

```vue
<script setup lang="ts">
const promotionCode = ref<string>();
const { addPromotionCode, appliedPromotionCodes } = useCart();
</script>
<template>
  <input type="text" v-model="promotionCode" />
  <button @click="addPromotionCode(promotionCode)">Apply promotion code</button>
</template>
```

### Displaying the cart

```vue
<script setup lang="ts">
const { cartItems, totalPrice, count } = useCart();
</script>
<template>
  Items: {{ count }} | Total: {{ totalPrice }}
  <ul>
    <li v-for="item in cartItems" :id="item.id">
      {{ item.label }} – {{ item.price.totalPrice }}
    </li>
  </ul>
</template>
```

**CartItem properties:**

| Property | Description |
|---|---|
| `id` | Unique identifier |
| `referencedId` | Product ID or promotion code |
| `label` | Label |
| `price.totalPrice` | Total price (can be negative) |
| `price.unitPrice` | Unit price |
| `quantity` | Quantity |
| `type` | `"product"` or `"promotion"` |
| `cover` | Cover image |

### Changing the quantity

```ts
const { changeProductQuantity } = useCart();
changeProductQuantity({ id: "...", quantity: 2 });
```

### Removing an item

```ts
// Via useCart
const { removeItem } = useCart();
await removeItem({ id: "..." });

// Via useCartItem (the item is set in the composable)
const { cartItem } = toRefs(props);
const { removeItem } = useCartItem(cartItem);
await removeItem();
```

---

## 3. Checkout

### Loading and displaying shipping methods

```vue
<script setup lang="ts">
const {
  shippingMethods,
  setShippingMethod,
  selectedShippingMethod: shippingMethod,
  getShippingMethods,
} = useCheckout();

const selectedShippingMethod = computed({
  get(): string { return shippingMethod.value?.id || ""; },
  async set(shippingMethodId: string) {
    await setShippingMethod({ id: shippingMethodId });
  },
});
</script>
<template>
  <div v-for="method in shippingMethods" :key="method.id">
    <input
      :id="method.id"
      v-model="selectedShippingMethod"
      :value="method.id"
      name="shipping-method"
      type="radio"
    />
    <label :for="method.id">{{ method.name }}</label>
  </div>
</template>
```

### Loading and displaying payment methods

```vue
<script setup lang="ts">
const {
  paymentMethods,
  selectedPaymentMethod: paymentMethod,
  setPaymentMethod,
  getPaymentMethods,
} = useCheckout();

const selectedPaymentMethod = computed({
  get(): string { return paymentMethod.value?.id || ""; },
  async set(paymentMethodId: string) {
    await setPaymentMethod({ id: paymentMethodId });
  },
});
</script>
```

### Personal data (guest order)

```vue
<script setup lang="ts">
const state = reactive({
  salutationId: "",
  firstName: "",
  lastName: "",
  email: "",
  password: "",
  guest: false,
  billingAddress: {
    street: "",
    zipcode: "",
    city: "",
    countryId: "",
  },
});
const { register } = useUser();
const { getCountries } = useCountries();
const { getSalutations } = useSalutations();
const invokeSubmit = () => register(state);
</script>
```

### Order summary

```vue
<script setup lang="ts">
const { refreshCart, cartItems, subtotal, totalPrice, shippingTotal } = useCart();
const { getFormattedPrice } = usePrice();
await refreshCart();
</script>
<template>
  <div>
    <p>Subtotal: {{ getFormattedPrice(subtotal) }}</p>
    <p>Shipping: {{ getFormattedPrice(shippingTotal) }}</p>
    <p>Total: {{ getFormattedPrice(totalPrice) }}</p>
  </div>
</template>
```

**Important:** always calculate prices on the backend, never in the frontend!

### Placing the order

```ts
const { createOrder } = useCheckout();
const { refreshCart } = useCart();

const order = await createOrder();
refreshCart();

// load the order details
const { loadOrderDetails, personalDetails, billingAddress, order } =
  useOrderDetails({ order: { id: order.id } as any });
await loadOrderDetails();
```

---

## 4. Product listing

### Basic setup

```ts
const { search, getElements } = useListing({
  listingType: "categoryListing",  // or "productSearchListing"
  categoryId: "dfd52ab937f840fd87e9d24ebf6bd245",  // only for categoryListing
  defaultSearchCriteria: {
    limit: 3,
    p: 1,
  },
});

await search({
  includes: {
    product: ["id", "name", "cover", "calculatedPrice", "translated"],
    product_media: ["media"],
    media: ["url", "thumbnails"],
  },
});
```

### Displaying products

```vue
<template>
  <div v-for="product in getElements" :key="product.id">
    <img :src="getSmallestThumbnailUrl(product)" :alt="product.name" />
    <a :href="getProductUrl(product)">
      {{ getTranslatedProperty(product, "name") }}
    </a>
    <div>{{ product.calculatedPrice?.unitPrice }} €</div>
    <button @click="addProduct(product)">Add to cart</button>
  </div>
</template>
```

### Sorting

```ts
const { getCurrentSortingOrder, getSortingOrders, changeCurrentSortingOrder } = useListing(/**...*/);

const onOrderChange = (event: Event) => {
  changeCurrentSortingOrder(
    (event.target as HTMLSelectElement).value
  );
};
```

### Pagination

```ts
const { getCurrentPage, changeCurrentPage, getTotalPagesCount } = useListing(/**...*/);
```

```html
<button v-if="getCurrentPage > 1" @click="changeCurrentPage(getCurrentPage - 1)">Prev</button>
<span>{{ getCurrentPage }}</span>
<button v-if="getCurrentPage < getTotalPagesCount" @click="changeCurrentPage(getCurrentPage + 1)">Next</button>
```

### Filters

**Available filter codes:**
- `manufacturer` – manufacturer filter
- `price` – price range `{ min, max }`
- `rating` – rating filter (number)
- `shipping-free` – boolean
- `properties` – property IDs (array)

**Setting filters:**
```ts
const { setCurrentFilters, getCurrentFilters, getAvailableFilters } = useListing(/**...*/);

setCurrentFilters({ code: "manufacturer", value: "manufacturer-id" });
setCurrentFilters({ code: "rating", value: 5 });
setCurrentFilters({ code: "properties", value: "property-option-id" });
```

**Reading the active filters:**
```vue
<template>
  {{ getCurrentFilters.manufacturer }}        <!-- ["id1", "id2"] -->
  {{ getCurrentFilters.price }}               <!-- { min: 0, max: 299 } -->
  {{ getCurrentFilters.rating }}              <!-- null or number -->
  {{ getCurrentFilters["shipping-free"] }}    <!-- boolean -->
  {{ getCurrentFilters.properties }}          <!-- ["id1", "id2"] -->
</template>
```

**Displaying the manufacturer filter:**
```vue
<template>
  <h3>{{ manufacturerFilter.label }}</h3>
  <div v-for="manufacturer in manufacturerFilter.entities">
    <input
      type="checkbox"
      :name="manufacturerFilter.code"
      @click="selectManufacturerAndSearch(manufacturer.id)"
      :checked="getCurrentFilters['manufacturer']?.includes(manufacturer.id)"
    />
    <label>{{ manufacturer.name }}</label>
  </div>
</template>
```

### Variant presentation

In the admin: product → variants → storefront presentation → product listings:

| Configuration | API output |
|---|---|
| Single product (main) | 1 element, parent product data |
| Single product (variant) | 1 element, variant data, parentId set |
| Expand properties | Several elements (one per property) |

---

## 5. Product detail page (PDP)

```ts
import type { Schemas } from "#shopware";
import { useProductSearch } from "@shopware/composables";

const { search } = useProductSearch();

const productResponse = await search("some-product-id", {
  // withCmsAssociations: true  // for CMS pages
});

const product: Schemas["Product"] = productResponse.product;
const propertyGroups: Schemas["PropertyGroup"][] = productResponse.configurator;

const productName = computed(() => product.value?.translated.name);
const manufacturer = computed(() => product.value?.manufacturer?.name);
const description = computed(() => product.value?.translated.description);
```

### Loading cross-sells

```ts
const { loadAssociations, isLoading, productAssociations } =
  useProductAssociations(product, {
    associationContext: "cross-selling",
  });
```

Example repo: https://github.com/shopware/frontends/tree/main/examples/product-detail-page

---

## 6. Price display

### Price structure (`CalculatedPrice`)

| Field | Description |
|---|---|
| `unitPrice` | Unit price |
| `quantity` | Quantity |
| `totalPrice` | Total price |
| `calculatedTaxes` | Taxes |
| `referencePrice` | Price per unit (e.g. 1.99€/100g) |
| `listPrice` | Strike-through price (`price`, `discount`, `percentage`) |
| `regulationPrice` | Lowest price of the last 30 days |

### Displaying the standard price

```vue
<script setup>
const { getFormattedPrice } = usePrice();
const { search } = useProductSearch();
const { product } = await search("some-product-id");
const { unitPrice, price, tierPrices, hasListPrice } = useProductPrice(ref(product));
</script>
<template>
  <div>
    <b>{{ product.name }}</b>
    <div>
      {{ getFormattedPrice(unitPrice) }}
      <small>incl. {{ price.taxRules[0].taxRate }}% tax</small>
    </div>
    <div v-if="hasListPrice">
      <small>
        <del>{{ getFormattedPrice(price.listPrice.price) }}</del>
        (-{{ price.listPrice.percentage }}%)
      </small>
    </div>
  </div>
</template>
```

### Displaying tier prices

```vue
<template>
  <ul>
    <li v-for="(tierPrice, index) in product.calculatedPrices" :key="tierPrice.quantity">
      {{ index === product.calculatedPrices.length - 1 ? 'from' : 'to' }}
      {{ tierPrice.quantity }} –
      {{ getFormattedPrice(tierPrice.unitPrice) }}
    </li>
  </ul>
</template>
```

### Price decision logic

```vue
<script setup>
const defaultPrice = computed(() => {
  if (product.value?.calculatedPrices?.length === 1) {
    return product.value.calculatedPrices[0];
  }
  return product.value?.calculatedPrice;
});
</script>
<template>
  <ul v-if="product.calculatedPrices.length > 1">
    <!-- tier prices -->
  </ul>
  <div v-else>
    <!-- standard price -->
    {{ getFormattedPrice(defaultPrice.totalPrice) }}
  </div>
</template>
```

### useProductPrice – product listing

```vue
<script setup lang="ts">
const { totalPrice, displayFrom, displayVariantsFrom } = useProductPrice(product);
</script>
<template>
  <span v-if="displayFrom">from </span>{{ totalPrice }} €
  <span v-if="displayVariantsFrom">Variants from {{ displayVariantsFrom }} €</span>
</template>
```

---

## 7. Wishlist

### Composables overview

| Composable | Description |
|---|---|
| `useLocalWishlist` | Local (in-memory) wishlist |
| `useSyncWishlist` | Remote (server) wishlist |
| `useWishlist` | View helper for the wishlist page |
| `useProductWishlist` | View helper for a single product |

`useWishlist` and `useProductWishlist` automatically choose local/remote depending on the login state.

### Loading the wishlist

```vue
<script>
const { getWishlistProducts, items } = useWishlist();
const { apiClient } = useShopwareContext();
const products = ref([]);

const loadProductsByItemIds = async (itemIds: string[]) => {
  const result = await apiClient.invoke("readProduct post /product", {
    body: { ids: itemIds || items.value },
  });
  products.value = result.data.elements;
};

watch(items, (items, oldItems) => {
  if (items.length !== oldItems?.length) {
    products.value = products.value.filter(({ id }) => items.includes(id));
  }
  if (!items.length) return;
  loadProductsByItemIds(items);
}, { immediate: true });

onMounted(async () => {
  await getWishlistProducts();
});
</script>
```

### Adding/removing a product to/from the wishlist

```vue
<script setup lang="ts">
const product = { id: "7b5b97bd48454979b14f21c8ef38ce08" };
const { addToWishlist, removeFromWishlist, isInWishlist } = useProductWishlist(product);
</script>
<template>
  <button v-if="!isInWishlist" @click="addToWishlist">Add to wishlist</button>
  <button v-if="isInWishlist" @click="removeFromWishlist">Remove from wishlist</button>
</template>
```

### Merging wishlists (after login)

```ts
const { mergeWishlistProducts } = useSyncWishlist();

const invokeLogin = async () => {
  await login(formData.value);
  mergeWishlistProducts();  // local → remote wishlist
};
```

---

## 8. JSON-LD (SEO)

```ts
// product page
useProductJsonLD(productResponse.value.product);

// with extensions
useProductJsonLD(productResponse.value.product, {
  brand: {
    "@type": "Brand",
    name: "Test",
  },
});
```

JSON-LD improves rich snippets in search results (price, availability, ratings).

---

## 9. Payment flow (general)

### Synchronous payment

```js
const { createOrder } = useCheckout();
const order = await createOrder();
// the backend processes the payment directly
```

### Asynchronous payment (external gateway)

```js
// 1. create the order
const { createOrder } = useCheckout();
const order = await createOrder();

// 2. initialise the payment handler
const { paymentUrl, handlePayment, isAsynchronous } = useOrderPayment(ref(order));

// 3. process the payment
const SUCCESS_URL = `${window.location.origin}/checkout/success/${order.id}/paid`;
const FAILURE_URL = `${window.location.origin}/checkout/success/${order.id}/unpaid`;

const handlePaymentResponse = await handlePayment(SUCCESS_URL, FAILURE_URL, {
  /* payment-provider-specific data */
});

// 4. redirect
const redirectUrl = handlePaymentResponse?.redirectUrl;
```

### App server integration (payment apps)

```ts
const { apiClient } = useShopwareContext();

// fetch a JWT token for the app server (only for logged-in customers)
const tokenResponse = await apiClient.invoke(
  "generateJWTAppSystemAppServer post /app-system/{name}/generate-token",
  { pathParams: { name: "MyPaymentApp" } }
);
// { token, expires, shopId }

// use the token for requests to the app server
await fetch("https://payment-gateway.com/api/card", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${tokenResponse.data?.token}`,
  },
});
```

---

## 10. B2B Quote Management

```vue
<!-- request a quote -->
<script setup lang="ts">
import { useCart, useB2bQuoteManagement } from "@shopware/composables";
const { cartItems } = useCart();
const { requestQuote } = useB2bQuoteManagement();
const comment = ref("");
</script>
<template>
  <textarea v-model="comment"></textarea>
  <button :disabled="cartItems.length <= 0" @click="requestQuote(comment)">
    Request quote
  </button>
</template>
```

**Further methods:**
- `getQuoteList()` – load all quotes
- `declineQuote(id, comment)` – decline a quote
- `requestChangeQuote(id, changeRequest)` – request a change
- `changeShippingMethod(id, shippingId)` – change the shipping method
- `changePaymentMethod(id, paymentId)` – change the payment method
- `createOrderFromQuote(id, comment)` – create an order from a quote

---

## 11. Broadcasting (tab synchronisation)

```ts
// useBroadcastChannelSync – synchronises cart & session between tabs
import type { Schemas } from "#shopware";

export const useBroadcastChannelSync = createSharedComposable(() => {
  const { apiClient } = useShopwareContext();
  const { refreshCart } = useCart();
  const { setContext } = useSessionContext();

  const [cartData, notifyCartDataChanged] = useSyncChannel<Schemas["Cart"]>("shopware-cart");
  watch([cartData], () => { refreshCart(cartData.value); });

  const [sessionData, notifySessionDataChanged] = useSyncChannel<Schemas["SalesChannelContext"]>("shopware-session-data");
  watch([sessionData], () => { if (sessionData.value) setContext(sessionData.value); });

  apiClient.hook("onSuccessResponse", (response) => {
    if (response._data?.apiAlias === "cart") {
      notifyCartDataChanged(response._data);
    } else if (response._data?.apiAlias === "sales_channel_context") {
      notifySessionDataChanged(response._data);
    }
  });
});
```

**Enabling it in nuxt.config.ts:**
```ts
runtimeConfig: {
  broadcasting: true,  // default: false (BFCache conflict!)
}
```

---

## Navigation (breadcrumbs, navigation tree)

The navigation components use `useNavigation` and `useNavigationSearch`.
Details in the skill `sw-frontends-customization` (routing).
