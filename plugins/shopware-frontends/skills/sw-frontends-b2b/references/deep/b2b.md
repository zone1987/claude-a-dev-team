# Shopware Frontends – B2B Features

Quelle: `apps/docs/src/getting-started/b2b/`, `apps/docs/src/resources/integrations/commercial/`

> Alle B2B-Features erfordern den **Shopware Rise Plan** oder höher.

---

## B2B Quote Management (Angebotsverwaltung)

Composable: `useB2bQuoteManagement` aus `@shopware/composables`

### 1. Neues Angebot anfragen

Nutzer kann für aktuellen Warenkorb ein individuelles Angebot anfordern.

> Warenkorb darf nicht leer sein!

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

### 2. Angebotsliste laden und anzeigen

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

### 3. Angebot ablehnen (Decline)

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

### 4. Änderung im Angebot anfragen

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

### 5. Zahlungs- oder Versandmethode im Angebot ändern

```ts
const { changeShippingMethod, changePaymentMethod } = useB2bQuoteManagement();

// Versandmethode ändern
changeShippingMethod(quoteId, "example-shipping-id");

// Zahlungsmethode ändern
changePaymentMethod(quoteId, "example-payment-id");
```

### 6. Bestellung aus Angebot erstellen

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

Das Quick-Order-Feature ermöglicht es B2B-Nutzern, schnell mehrere Produkte per SKU/Artikelnummer zum Warenkorb hinzuzufügen.

**Referenz-Implementierung:**  
https://github.com/shopware/frontends/tree/main/examples/commercial-quick-order

---

## useB2bQuoteManagement – API-Übersicht

| Methode | Signatur | Beschreibung |
|---------|----------|-------------|
| `requestQuote` | `(comment: string)` | Neues Angebot für aktuellen Cart anfragen |
| `getQuoteList` | `()` | Liste aller Angebote laden |
| `declineQuote` | `(id: string, comment: string)` | Angebot ablehnen |
| `requestChangeQuote` | `(id: string, comment: string)` | Änderung anfragen |
| `changeShippingMethod` | `(id: string, shippingMethodId: string)` | Versandmethode ändern |
| `changePaymentMethod` | `(id: string, paymentMethodId: string)` | Zahlungsmethode ändern |
| `createOrderFromQuote` | `(id: string, comment: string)` | Bestellung aus Angebot erstellen |

---

## Composable-Referenz

- [`useB2bQuoteManagement`](https://frontends.shopware.com/packages/composables/useB2bQuoteManagement) – offizielle Composable-Dokumentation
