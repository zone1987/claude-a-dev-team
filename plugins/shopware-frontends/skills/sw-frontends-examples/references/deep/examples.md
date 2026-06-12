# Shopware Frontends – Code-Rezepte & Beispiele

Quelle: `apps/docs/src/getting-started/`

---

## 1. Login-Formular

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
    <!-- Fehleranzeige -->
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

**Composable `useUser` – wichtige Felder:**
- `login(credentials)` – Login
- `logout()` – Logout
- `errors.login` – Array mit API-Fehlern
- `isLoggedIn` – Boolean (computed)
- `user` – Customer-Objekt

StackBlitz-Demo: https://stackblitz.com/github/shopware/frontends/tree/main/examples/login-form

---

## 2. Warenkorb (Cart)

### Warenkorb initialisieren

```ts
const { refreshCart } = useCart();
await refreshCart();
// Erstellt automatisch neuen Cart, falls keiner existiert
// Intern: sw-context-token im Header
```

### Produkt zum Warenkorb hinzufügen

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

### Promotion-Code hinzufügen

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

### Warenkorb anzeigen

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

**CartItem-Eigenschaften:**

| Property | Beschreibung |
|---|---|
| `id` | Unique Identifier |
| `referencedId` | Produkt-ID oder Promotion-Code |
| `label` | Bezeichnung |
| `price.totalPrice` | Gesamtpreis (kann negativ sein) |
| `price.unitPrice` | Stückpreis |
| `quantity` | Menge |
| `type` | `"product"` oder `"promotion"` |
| `cover` | Cover-Bild |

### Menge ändern

```ts
const { changeProductQuantity } = useCart();
changeProductQuantity({ id: "...", quantity: 2 });
```

### Artikel entfernen

```ts
// Via useCart
const { removeItem } = useCart();
await removeItem({ id: "..." });

// Via useCartItem (item wird im Composable gesetzt)
const { cartItem } = toRefs(props);
const { removeItem } = useCartItem(cartItem);
await removeItem();
```

---

## 3. Checkout

### Versandmethoden laden und anzeigen

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

### Zahlungsmethoden laden und anzeigen

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

### Persönliche Daten (Gastbestellung)

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

### Bestellzusammenfassung

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

**Wichtig:** Preisberechnungen immer Backend-seitig, nie im Frontend!

### Bestellung aufgeben

```ts
const { createOrder } = useCheckout();
const { refreshCart } = useCart();

const order = await createOrder();
refreshCart();

// Orderdetails laden
const { loadOrderDetails, personalDetails, billingAddress, order } =
  useOrderDetails({ order: { id: order.id } as any });
await loadOrderDetails();
```

---

## 4. Produktlisting

### Grundsetup

```ts
const { search, getElements } = useListing({
  listingType: "categoryListing",  // oder "productSearchListing"
  categoryId: "dfd52ab937f840fd87e9d24ebf6bd245",  // nur bei categoryListing
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

### Produkte anzeigen

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

### Sortierung

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

### Filter

**Verfügbare Filter-Codes:**
- `manufacturer` – Hersteller-Filter
- `price` – Preis-Bereich `{ min, max }`
- `rating` – Bewertungs-Filter (Zahl)
- `shipping-free` – Boolean
- `properties` – Eigenschaft-IDs (Array)

**Filter setzen:**
```ts
const { setCurrentFilters, getCurrentFilters, getAvailableFilters } = useListing(/**...*/);

setCurrentFilters({ code: "manufacturer", value: "manufacturer-id" });
setCurrentFilters({ code: "rating", value: 5 });
setCurrentFilters({ code: "properties", value: "property-option-id" });
```

**Aktive Filter auslesen:**
```vue
<template>
  {{ getCurrentFilters.manufacturer }}        <!-- ["id1", "id2"] -->
  {{ getCurrentFilters.price }}               <!-- { min: 0, max: 299 } -->
  {{ getCurrentFilters.rating }}              <!-- null oder Zahl -->
  {{ getCurrentFilters["shipping-free"] }}    <!-- boolean -->
  {{ getCurrentFilters.properties }}          <!-- ["id1", "id2"] -->
</template>
```

**Hersteller-Filter anzeigen:**
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

### Varianten-Präsentation

Im Admin: Produkt → Varianten → Storefront-Darstellung → Produktlisten:

| Konfiguration | API-Output |
|---|---|
| Einzelprodukt (Main) | 1 Element, Eltern-Produktdaten |
| Einzelprodukt (Variante) | 1 Element, Variant-Daten, parentId gesetzt |
| Eigenschaften expandieren | Mehrere Elemente (je Eigenschaft) |

---

## 5. Produktdetailseite (PDP)

```ts
import type { Schemas } from "#shopware";
import { useProductSearch } from "@shopware/composables";

const { search } = useProductSearch();

const productResponse = await search("some-product-id", {
  // withCmsAssociations: true  // für CMS-Seiten
});

const product: Schemas["Product"] = productResponse.product;
const propertyGroups: Schemas["PropertyGroup"][] = productResponse.configurator;

const productName = computed(() => product.value?.translated.name);
const manufacturer = computed(() => product.value?.manufacturer?.name);
const description = computed(() => product.value?.translated.description);
```

### Cross-Sells laden

```ts
const { loadAssociations, isLoading, productAssociations } =
  useProductAssociations(product, {
    associationContext: "cross-selling",
  });
```

Beispiel-Repo: https://github.com/shopware/frontends/tree/main/examples/product-detail-page

---

## 6. Preisanzeige

### Preis-Struktur (`CalculatedPrice`)

| Feld | Beschreibung |
|---|---|
| `unitPrice` | Stückpreis |
| `quantity` | Menge |
| `totalPrice` | Gesamtpreis |
| `calculatedTaxes` | Steuern |
| `referencePrice` | Preis pro Einheit (z.B. 1,99€/100g) |
| `listPrice` | Streichpreis (`price`, `discount`, `percentage`) |
| `regulationPrice` | Günstigster Preis der letzten 30 Tage |

### Standardpreis anzeigen

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

### Tier-Preise anzeigen

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

### Preis-Entscheidungslogik

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
    <!-- Tier-Preise -->
  </ul>
  <div v-else>
    <!-- Standardpreis -->
    {{ getFormattedPrice(defaultPrice.totalPrice) }}
  </div>
</template>
```

### useProductPrice – Produktlisting

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

## 7. Wunschliste (Wishlist)

### Composables-Übersicht

| Composable | Beschreibung |
|---|---|
| `useLocalWishlist` | Lokale (in-memory) Wunschliste |
| `useSyncWishlist` | Remote (Server) Wunschliste |
| `useWishlist` | View-Helper für Wunschlisten-Seite |
| `useProductWishlist` | View-Helper für einzelnes Produkt |

`useWishlist` und `useProductWishlist` wählen automatisch lokal/remote je nach Login-Status.

### Wunschliste laden

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

### Produkt zur Wunschliste hinzufügen/entfernen

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

### Wunschlisten zusammenführen (nach Login)

```ts
const { mergeWishlistProducts } = useSyncWishlist();

const invokeLogin = async () => {
  await login(formData.value);
  mergeWishlistProducts();  // Lokale → Remote-Wishlist
};
```

---

## 8. JSON-LD (SEO)

```ts
// Produktseite
useProductJsonLD(productResponse.value.product);

// Mit Erweiterungen
useProductJsonLD(productResponse.value.product, {
  brand: {
    "@type": "Brand",
    name: "Test",
  },
});
```

JSON-LD verbessert Rich Snippets in Suchergebnissen (Preis, Verfügbarkeit, Bewertungen).

---

## 9. Payment-Flow (allgemein)

### Synchrones Payment

```js
const { createOrder } = useCheckout();
const order = await createOrder();
// Backend verarbeitet Payment direkt
```

### Asynchrones Payment (externe Gateway)

```js
// 1. Order erstellen
const { createOrder } = useCheckout();
const order = await createOrder();

// 2. Payment-Handler initialisieren
const { paymentUrl, handlePayment, isAsynchronous } = useOrderPayment(ref(order));

// 3. Payment verarbeiten
const SUCCESS_URL = `${window.location.origin}/checkout/success/${order.id}/paid`;
const FAILURE_URL = `${window.location.origin}/checkout/success/${order.id}/unpaid`;

const handlePaymentResponse = await handlePayment(SUCCESS_URL, FAILURE_URL, {
  /* payment-provider-spezifische Daten */
});

// 4. Weiterleitung
const redirectUrl = handlePaymentResponse?.redirectUrl;
```

### App Server Integration (Payment Apps)

```ts
const { apiClient } = useShopwareContext();

// JWT-Token für App-Server holen (nur für eingeloggte Kunden)
const tokenResponse = await apiClient.invoke(
  "generateJWTAppSystemAppServer post /app-system/{name}/generate-token",
  { pathParams: { name: "MyPaymentApp" } }
);
// { token, expires, shopId }

// Token für Requests an den App-Server nutzen
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
<!-- Angebot anfordern -->
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

**Weitere Methoden:**
- `getQuoteList()` – Alle Angebote laden
- `declineQuote(id, comment)` – Angebot ablehnen
- `requestChangeQuote(id, changeRequest)` – Änderung anfragen
- `changeShippingMethod(id, shippingId)` – Versandmethode ändern
- `changePaymentMethod(id, paymentId)` – Zahlungsmethode ändern
- `createOrderFromQuote(id, comment)` – Bestellung aus Angebot erstellen

---

## 11. Broadcasting (Tab-Synchronisation)

```ts
// useBroadcastChannelSync – synchronisiert Cart & Session zwischen Tabs
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

**Aktivieren in nuxt.config.ts:**
```ts
runtimeConfig: {
  broadcasting: true,  // default: false (BFCache-Konflikt!)
}
```

---

## Navigation (Breadcrumbs, Navigation-Baum)

Die Navigations-Komponenten verwenden `useNavigation` und `useNavigationSearch`.
Details in Skill `sw-frontends-customization` (Routing).
