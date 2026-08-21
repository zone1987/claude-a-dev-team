# Shopware Frontends – B2B Features

Source: `apps/docs/src/getting-started/b2b/`, `apps/docs/src/resources/integrations/commercial/`

> All B2B features require the **Shopware Rise Plan** or higher.

---

## Contents

- [B2B Quote Management](#b2b-quote-management)
- [B2B Quick Order](#b2b-quick-order)
- [useB2bQuoteManagement – API overview](#useb2bquotemanagement-api-overview)
- [Composable reference](#composable-reference)

## B2B Quote Management

Composable: `useB2bQuoteManagement` from `@shopware/composables`

### 1. Request a new quote

The user can request an individual quote for the current cart.

> The cart must not be empty!

```vue
<script setup lang="ts">
import { ref } from "vue";
import { useCart, useB2bQuoteManagement } from "@shopware/composables";

const { cartItems } = useCart();
const { requestQuote } = useB2bQuoteManagement();
const comment = ref("");

const handleRequestQuote = async () => {
  await requestQuote(comment.value);
};
</script>
<template>
  <textarea v-model="comment"></textarea>
  <button :disabled="cartItems.length <= 0" @click="handleRequestQuote">
    Request quote
  </button>
</template>
```

### 2. Load and display the quote list

```vue
<script setup lang="ts">
import { ref, onBeforeMount } from "vue";
import { useB2bQuoteManagement } from "@shopware/composables";

const quotesList = ref([]);
const { getQuoteList } = useB2bQuoteManagement();

onBeforeMount(async () => {
  quotesList.value = await getQuoteList();
});
</script>
<template>
  <table>
    <thead>
      <tr>
        <th>Quote #</th>
        <th>Created at</th>
        <th>Valid until</th>
        <th>Grand total</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="quote in quotesList" :key="quote.id">
        <td>{{ quote.quoteNumber }}</td>
        <td>{{ quote.createdAt }}</td>
        <td>{{ quote.expirationDate }}</td>
        <td>{{ quote.price.totalPrice }}</td>
        <td>{{ quote.stateMachineState.translated.name }}</td>
      </tr>
    </tbody>
  </table>
</template>
```

### 3. Decline a quote

```vue
<script setup lang="ts">
import { ref } from "vue";
import { useB2bQuoteManagement } from "@shopware/composables";

const declineComment = ref("");
const quote = ref("example-id");
const { declineQuote } = useB2bQuoteManagement();

const handleDecline = async () => {
  declineQuote(quote.value.id, declineComment.value);
  declineComment.value = "";
};
</script>
<template>
  <form @submit.prevent="handleDecline">
    <textarea v-model="declineComment"></textarea>
    <button>Decline</button>
  </form>
</template>
```

### 4. Request a change to the quote

```vue
<script setup lang="ts">
const quote = ref("example-id");
const changeRequest = ref("");
const { requestChangeQuote } = useB2bQuoteManagement();

const handleChangeRequest = async () => {
  requestChangeQuote(quote.value.id, changeRequest.value);
  changeRequest.value = "";
};
</script>
<template>
  <form @submit.prevent="handleChangeRequest">
    <textarea v-model="changeRequest"></textarea>
    <button type="submit">Send</button>
  </form>
</template>
```

### 5. Change the payment or shipping method on the quote

```ts
const { changeShippingMethod, changePaymentMethod } = useB2bQuoteManagement();

// Change the shipping method
changeShippingMethod(quoteId, "example-shipping-id");

// Change the payment method
changePaymentMethod(quoteId, "example-payment-id");
```

### 6. Create an order from a quote

```vue
<script setup lang="ts">
const quote = ref("example-id");
const comment = ref("");
const { createOrderFromQuote } = useB2bQuoteManagement();

const handleCreateOrder = async () => {
  await createOrderFromQuote(quote.value.id, comment.value);
};
</script>
<template>
  <form @submit.prevent="handleCreateOrder">
    <textarea v-model="comment"></textarea>
    <button type="submit">Create order</button>
  </form>
</template>
```

---

## B2B Quick Order

The quick order feature lets B2B users quickly add several products to the cart by SKU/product number.

**Reference implementation:**  
https://github.com/shopware/frontends/tree/main/examples/commercial-quick-order

---

## useB2bQuoteManagement – API overview

| Method | Signature | Description |
|---------|----------|-------------|
| `requestQuote` | `(comment: string)` | Request a new quote for the current cart |
| `getQuoteList` | `()` | Load the list of all quotes |
| `declineQuote` | `(id: string, comment: string)` | Decline a quote |
| `requestChangeQuote` | `(id: string, comment: string)` | Request a change |
| `changeShippingMethod` | `(id: string, shippingMethodId: string)` | Change the shipping method |
| `changePaymentMethod` | `(id: string, paymentMethodId: string)` | Change the payment method |
| `createOrderFromQuote` | `(id: string, comment: string)` | Create an order from a quote |

---

## Composable reference

- [`useB2bQuoteManagement`](https://frontends.shopware.com/packages/composables/useB2bQuoteManagement) – official composable documentation
