# Shopware Frontends – Integrations

Source: `apps/docs/src/resources/integrations/`

---

## Contents

- [Payment integrations](#payment-integrations)
- [CMS integrations](#cms-integrations)
- [Commercial integrations (Rise/Evolve/Beyond)](#commercial-integrations-riseevolvebeyond)
- [Community Modules](#community-modules)

## Payment integrations

### PayPal integration

**Prerequisite:** the [SwagPayPal](https://github.com/shopware/SwagPayPal) extension in the Shopware backend.

**PayPal-specific endpoints:**
- `POST /store-api/paypal/create-order` – create an order
- `POST /store-api/paypal/express/create-order` – Express Checkout order
- `POST /store-api/paypal/express/prepare-checkout` – Express: prepare checkout

#### Loading the PayPal SDK

```ts
import { loadScript } from "@paypal/paypal-js";

loadScript({
  "client-id": "AUA...",
  currency: "EUR",
  locale: "en_US",
});
```

#### Standard checkout – createOrder

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

#### Express checkout – createOrder

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

#### Further PayPal methods

**Loading the SDK (with additional methods):**
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

**Credit card (ACDC):**
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

**Google Pay:** requires `<script src="https://pay.google.com/gp/p/js/pay.js">` in the head.

**Apple Pay:** requires `<script src="https://applepay.cdn-apple.com/jsapi/v1/apple-pay-sdk.js">` in the head.

StackBlitz demo: https://stackblitz.com/github/shopware/frontends/tree/main/examples/express-checkout

---

### Adyen integration

Based on the Adyen drop-in component example.
Repository example: `examples/adyen-dropin-component/`

---

### Amazon Pay integration

Based on the Amazon Pay button example.
Repository example: `examples/amazon-pay-button-example/`

---

### Braintree integration

**Prerequisite:** the [Shopware Braintree App](https://github.com/shopware/braintree-app) installed and configured.

**Procedure in 3 steps:**

**Step 1: fetch the client token**
```ts
const { apiClient } = useShopwareContext();
const { sessionContext } = useSessionContext();

// fetch the app token from Shopware
const tokenResponse = await apiClient.invoke(
  "generateJWTAppSystemAppServer post /app-system/{name}/generate-token",
  { pathParams: { name: "SwagBraintreeApp" } }
);
const { token, shopId } = tokenResponse.data;

// fetch the Braintree client config
const configResponse = await fetch(
  `https://braintree.shopware.com/api/client/config?shop-id=${shopId}&...`,
  {
    method: "POST",
    headers: {
      "shopware-app-token": token,  // IMPORTANT: not Authorization: Bearer!
      "shopware-app-shop-id": shopId,
    },
  }
);
const { clientToken } = await configResponse.json();
```

**Step 2: initialise the Braintree drop-in**
```ts
import dropin from "braintree-web-drop-in";

const instance = await dropin.create({
  authorization: clientToken,
  container: "#dropin-container",
  dataCollector: true,  // Required for deviceData
  card: { cardholderName: { required: true } },
});
```

**Step 3: create the order and handle the payment**
```ts
const { createOrder } = useCheckout();
const { apiClient } = useShopwareContext();

async function onPaymentSubmit() {
  const { nonce, deviceData } = await instance.requestPaymentMethod();
  const order = await createOrder();  // WITHOUT Braintree params!

  await apiClient.invoke("handlePaymentMethod post /handle-payment", {
    body: {
      orderId: order.id,
      finishUrl: `${window.location.origin}/checkout/finish`,
      errorUrl: `${window.location.origin}/checkout/error`,
      braintreeNonce: nonce,           // params go to /handle-payment
      braintreeDeviceData: deviceData, // NOT to /checkout/order
    },
  });
}
```

**Test card:** 4111 1111 1111 1111 (Visa, any future expiry, any CVV)

Example repo: https://github.com/shopware/frontends/tree/main/examples/braintree-credit-card

---

### Mollie integration

External project: https://github.com/mollie/Shopware6Composables

---

## CMS integrations

### Storyblok integration

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

**Storyblok components (storyblok/):**
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

### Strapi integration

**Installation:**
```bash
pnpm add -D @nuxtjs/strapi
```

**nuxt.config.ts:**
```ts
export default { modules: ["@nuxtjs/strapi"] }
```

**Loading a single item (global banner):**
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

**Loading pages:**
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

## Commercial integrations (Rise/Evolve/Beyond)

### B2B quick order

Example repo: `examples/commercial-quick-order/`

Allows products to be added quickly via product number/CSV.

### B2B quote management

Composable: `useB2bQuoteManagement`

For complete examples see `sw-frontends-examples`.

### Custom Products

Example repo: `examples/commercial-customized-products/`

Enables product configuration (personalisation).

### Digital Sales Rooms

Enables virtual sales rooms.
Admin documentation: https://docs.shopware.com/en/shopware-6-en/extensions/digital-sales-rooms

---

## Community Modules

> Not officially supported by Shopware.

| Module | Maintainer | Description |
|---|---|---|
| [store-api-proxy](https://github.com/KoRoHandelsGmbH/store-api-proxy) | KoRoHandelsGmbH | Thin layer over the Store API with Nitropack + Vercel Data Cache |
| [Middleware Proxy Module](https://github.com/meeshoogendoorn/shopware-frontends-proxy) | meeshoogendoorn | Nuxt middleware proxy, removes CORS preflight requests |
| [Nuxt Cache Tags](https://github.com/mothership-gmbh/nuxt-shopware-caching) | niklaswolf | Shopware cache tags for the full-page cache |
| [Headless CMS POC](https://github.com/meeshoogendoorn/shopware-frontends-headless-cms-integration) | meeshoogendoorn | Prototype Storyblok integration |
