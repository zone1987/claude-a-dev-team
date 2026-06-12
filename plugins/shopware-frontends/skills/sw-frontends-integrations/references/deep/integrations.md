# Shopware Frontends – Integrationen

Quelle: `apps/docs/src/resources/integrations/`

---

## Payment-Integrationen

### PayPal Integration

**Voraussetzung:** [SwagPayPal](https://github.com/shopware/SwagPayPal) Extension im Shopware-Backend.

**PayPal-spezifische Endpoints:**
- `POST /store-api/paypal/create-order` – Order erstellen
- `POST /store-api/paypal/express/create-order` – Express Checkout Order
- `POST /store-api/paypal/express/prepare-checkout` – Express: Checkout vorbereiten

#### PayPal SDK laden

```ts
import { loadScript } from "@paypal/paypal-js";

loadScript({
  "client-id": "AUA...",
  currency: "EUR",
  locale: "en_US",
});
```

#### Standard Checkout – createOrder

```ts
const divContainer = ref();

window.paypal.Buttons({
  createOrder: async (data, actions) => {
    const response = await apiClient.invoke(
      "createPayPalOrder post /store-api/paypal/create-order"
    );
    return response.data?.token;
  },
  onApprove: async (data, actions) => {
    orderCreated.value = await createOrder({ paypalOrderId: data.orderID });
    refreshCart();
    const handlePaymentResponse = await apiClient.invoke(
      "handlePaymentMethod post /handle-payment",
      {
        query: { paypalOrderId: data.orderID },
        body: {
          orderId: order.id,
          finishUrl: `${window.location.origin}/order/finish?order=${order.id}&success=true`,
        },
      }
    );
    await fetch(handlePaymentResponse.data.redirectUrl);
  },
}).render(divContainer);
```

#### Express Checkout – createOrder

```ts
window.paypal.Buttons({
  createOrder: async (data, actions) => {
    await setPaymentMethod(paypalMethod.value);
    await addToCart();
    const response = await apiClient.invoke(
      "createPayPalExpressOrder post /store-api/paypal/express/create-order"
    );
    return response.data?.token;
  },
  onApprove: async (data, actions) => {
    await apiClient.invoke(
      "preparePayPalExpressCheckout post /store-api/paypal/express/prepare-checkout",
      { body: { token: data.orderID } }
    );
    const order = await createOrder({ paypalOrderId: data.orderID });
    refreshCart();
    const handlePaymentResponse = await apiClient.invoke(
      "handlePaymentMethod post /handle-payment",
      {
        query: { isPayPalExpressCheckout: true, paypalOrderId: data.orderID },
        body: {
          orderId: order.id,
          finishUrl: `${window.location.origin}/order/finish?order=${order.id}&success=true`,
        },
      }
    );
    await fetch(handlePaymentResponse.data.redirectUrl);
  },
}).render(divContainer);
```

#### Weitere PayPal-Methoden

**SDK laden (mit zusätzlichen Methoden):**
```ts
loadScript({
  "enable-funding": "paylater,venmo",
  components: "card-fields,applepay,googlepay",
  ...
});
```

**Pay Later:**
```ts
window.paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  createOrder: createOrder.bind(this, "paylater"),
  onApprove: onApprove.bind(this),
}).render(divContainer);
```

**Kreditkarte (ACDC):**
```ts
const cardFields = paypal.CardFields({ createOrder, onApprove, style: {} });
cardFields.NameField().render("#acdc-name-field-container");
cardFields.NumberField().render("#acdc-number-field-container");
cardFields.CVVField().render("#acdc-cvv-field-container");
cardFields.ExpiryField().render("#acdc-expiry-field-container");

async function onFormSubmit() {
  const state = await cardFields.getState();
  if (state.isFormValid) cardFields.submit();
}
```

**Google Pay:** Erfordert `<script src="https://pay.google.com/gp/p/js/pay.js">` im Head.

**Apple Pay:** Erfordert `<script src="https://applepay.cdn-apple.com/jsapi/v1/apple-pay-sdk.js">` im Head.

StackBlitz-Demo: https://stackblitz.com/github/shopware/frontends/tree/main/examples/express-checkout

---

### Adyen Integration

Basiert auf dem Adyen Drop-in Component-Beispiel.
Repository-Beispiel: `examples/adyen-dropin-component/`

---

### Amazon Pay Integration

Basiert auf dem Amazon Pay Button-Beispiel.
Repository-Beispiel: `examples/amazon-pay-button-example/`

---

### Braintree Integration

**Voraussetzung:** [Shopware Braintree App](https://github.com/shopware/braintree-app) installiert und konfiguriert.

**Ablauf in 3 Schritten:**

**Schritt 1: Client Token holen**
```ts
const { apiClient } = useShopwareContext();
const { sessionContext } = useSessionContext();

// App-Token von Shopware holen
const tokenResponse = await apiClient.invoke(
  "generateJWTAppSystemAppServer post /app-system/{name}/generate-token",
  { pathParams: { name: "SwagBraintreeApp" } }
);
const { token, shopId } = tokenResponse.data;

// Braintree Client Config holen
const configResponse = await fetch(
  `https://braintree.shopware.com/api/client/config?shop-id=${shopId}&...`,
  {
    method: "POST",
    headers: {
      "shopware-app-token": token,  // WICHTIG: nicht Authorization: Bearer!
      "shopware-app-shop-id": shopId,
    },
  }
);
const { clientToken } = await configResponse.json();
```

**Schritt 2: Braintree Drop-in initialisieren**
```ts
import dropin from "braintree-web-drop-in";

const instance = await dropin.create({
  authorization: clientToken,
  container: "#dropin-container",
  dataCollector: true,  // Required für deviceData
  card: { cardholderName: { required: true } },
});
```

**Schritt 3: Order erstellen und Payment abwickeln**
```ts
const { createOrder } = useCheckout();
const { apiClient } = useShopwareContext();

async function onPaymentSubmit() {
  const { nonce, deviceData } = await instance.requestPaymentMethod();
  const order = await createOrder();  // OHNE Braintree-Params!

  await apiClient.invoke("handlePaymentMethod post /handle-payment", {
    body: {
      orderId: order.id,
      finishUrl: `${window.location.origin}/checkout/finish`,
      errorUrl: `${window.location.origin}/checkout/error`,
      braintreeNonce: nonce,           // Params an /handle-payment
      braintreeDeviceData: deviceData, // NICHT an /checkout/order
    },
  });
}
```

**Test-Karte:** 4111 1111 1111 1111 (Visa, any future expiry, any CVV)

Beispiel-Repo: https://github.com/shopware/frontends/tree/main/examples/braintree-credit-card

---

### Mollie Integration

Externes Projekt: https://github.com/mollie/Shopware6Composables

---

## CMS-Integrationen

### Storyblok Integration

**Setup:**
```bash
npx tiged shopware/frontends/templates/vue-blank vue-blank-storyblok
cd vue-blank-storyblok
pnpm i && pnpm run dev
pnpx nuxi@latest module add storyblok
pnpm add @storyblok/vue -D
```

**nuxt.config.ts:**
```ts
modules: ["@shopware/nuxt-module", "@storyblok/nuxt"],
storyblok: {
  accessToken: "super-secret-token"
},
```

**Storyblok-Komponenten (storyblok/):**
```vue
<!-- storyblok/Feature.vue -->
<script setup>
defineProps({ blok: Object });
</script>
<template>
  <div v-editable="blok">
    <h1>{{ blok.name }}</h1>
  </div>
</template>
```

**Routing (pages/storyblok/[slug].vue):**
```vue
<script setup lang="ts">
const route = useRoute();
const slug = route.params.slug.toString() ?? "home";
const story = await useAsyncStoryblok(slug, { version: "draft" });
</script>
<template>
  <StoryblokComponent v-if="story" :blok="story.content" />
</template>
```

---

### Strapi Integration

**Installation:**
```bash
pnpm add -D @nuxtjs/strapi
```

**nuxt.config.ts:**
```ts
export default { modules: ["@nuxtjs/strapi"] }
```

**Einzelelement laden (Global Banner):**
```vue
<script setup lang="ts">
interface GlobalBanner { text: string; color: string; }
const { findOne } = useStrapi();
const { data } = await findOne<GlobalBanner>("global-banner");
const bgColor = computed(() => data.attributes?.color || "#fff");
</script>
<template>
  <section>
    <div class="text-center py-1" :style="{ 'background-color': bgColor }">
      {{ data.attributes.text }}
    </div>
  </section>
</template>
```

**Seiten laden:**
```ts
export function useSWStrapi() {
  const getPage = async (route: string) => {
    const { findOne } = useStrapi();
    return findOne<StripePage>("pages", undefined, {
      filters: { seoUrl: route },
    });
  };

  const resolveComponent = async (route: string) => {
    const page = await getPage(route);
    if (!page.data[0]) return null;
    return h("div", {}, page.data[0].attributes.text);
  };

  return { resolveComponent };
}
```

---

## Commercial Integrationen (Rise/Evolve/Beyond)

### B2B Quick-Order

Beispiel-Repo: `examples/commercial-quick-order/`

Erlaubt das schnelle Hinzufügen von Produkten via Produktnummer/CSV.

### B2B Quote Management

Composable: `useB2bQuoteManagement`

Vollständige Beispiele siehe `sw-frontends-examples`.

### Custom Products

Beispiel-Repo: `examples/commercial-customized-products/`

Ermöglicht Produktkonfiguration (Personalisierung).

### Digital Sales Rooms

Ermöglicht virtuelle Verkaufsräume.
Admin-Dokumentation: https://docs.shopware.com/en/shopware-6-en/extensions/digital-sales-rooms

---

## Community Modules

> Nicht offiziell von Shopware unterstützt.

| Modul | Maintainer | Beschreibung |
|---|---|---|
| [store-api-proxy](https://github.com/KoRoHandelsGmbH/store-api-proxy) | KoRoHandelsGmbH | Dünne Schicht über Store-API mit Nitropack + Vercel Data Cache |
| [Middleware Proxy Module](https://github.com/meeshoogendoorn/shopware-frontends-proxy) | meeshoogendoorn | Nuxt Middleware Proxy, entfernt CORS-Preflight-Requests |
| [Nuxt Cache Tags](https://github.com/mothership-gmbh/nuxt-shopware-caching) | niklaswolf | Shopware Cache-Tags für Full-Page-Cache |
| [Headless CMS POC](https://github.com/meeshoogendoorn/shopware-frontends-headless-cms-integration) | meeshoogendoorn | Prototype Storyblok Integration |
