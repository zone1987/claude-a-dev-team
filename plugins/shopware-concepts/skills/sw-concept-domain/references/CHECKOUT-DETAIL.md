# Shopware checkout — complete concept documentation

Sources: `concepts/commerce/checkout-concept/index.md`, `cart.md`, `orders.md`, `payments.md`

---

## Contents

- [Checkout overview (index.md)](#checkout-overview-indexmd)
- [Cart (cart.md)](#cart-cartmd)
- [Orders (orders.md)](#orders-ordersmd)
- [Payments (payments.md)](#payments-paymentsmd)

## Checkout overview (index.md)

The checkout covers all steps involved in buying items in the shop.
Core process: **Cart → Order → Payment → Shipping**.

---

## Cart (cart.md)

### Design goals

- **Adaptability** — many services for simple cart usage; the cart can be adapted for many use cases
- **Performance** — minimal calculations, queries and iterations; clear state management
- **Abstraction** — few hard dependencies on core entities; entities referenced via interfaces

### Cart struct (`\Shopware\Core\Checkout\Cart\Cart`)

One instance = one cart. Identified only via a token hash (no user/customer reference in the struct itself).
Allows multiple carts per user, per sales channel, or across channels.

**Contains:**
- **Line items** — order positions (products, bundles, discounts, surcharges)
  - Properties: `stackable` (quantity changeable), `removable` (removable via API)
  - Can contain other line items (bundles)
  - Main extension point for the cart process
- **Transaction** — payment information (payment handler + amount)
- **Delivery** — delivery (date, method, destination address, positions)
- **Error** — validation errors that prevent ordering
- **Tax** — calculated tax rate
- **Price** — total price (incl./excl. VAT, shipping, discounts)

### Cart states

```
Empty → (add line item) → Dirty → (calculate) → Calculated
Calculated → (modify) → Dirty
Calculated → (order invalid) → Calculated
Calculated → (order) → [done]
```

| State | Description |
|---|---|
| Empty | No item; default shipping/payment |
| Dirty | After a change; invalid prices, raw line items, uncertain delivery validity |
| Calculated | After calculation; can be placed as an order or contains errors |

### Calculation (4 phases)

```
[*] → Enrich → Process → Validate → Persist → [*]
                           ↑___↓ (repeat until stable)
```

| Phase | Task |
|---|---|
| **Enrich** | Load images, descriptions, prices for line items |
| **Process** | Update prices, adjust shipping/payment, calculate totals |
| **Validate** | Check the rule system; cart changes based on plausibility checks |
| **Persist** | Update storage |

### Cart enrichment

**Collectors** (`CartDataCollectorInterface`) load data lazily:

| Service | Task |
|---|---|
| `ProductCartProcessor` | Enrich all referenced products |
| `CartPromotionsCollector` | Add, remove, validate promotions |
| `ShippingMethodPriceCollector` | Shipping prices |

Sequence: `collect` (all collectors) → `enrich` (all collectors)

### Context rules and iteration

After processing, the cart is validated against the rule system → possible cart changes → re-validation.

Example scenario (buy a car → free sunglasses → 2% discount):
1. Iteration 1: car in the cart → sunglasses added automatically
2. Iteration 2: 2 products in the cart → 2% discount added
3. Result: car + sunglasses + 2% discount → stable

### Cart storage

- **Not** managed via the DAL — the cart is written/read as a whole
- `CartService` (`\Shopware\Core\Checkout\Cart\SalesChannel\CartService`) — central facade

---

## Orders (orders.md)

### Design goals

#### Denormalisation

- An order does **not** depend on the catalogue or on products
- All line item data + calculated prices are persisted when ordering
- Recalculation only via an explicit API call

#### Workflow-dependent

- State changes happen in a defined, predictable and configurable way
- Only permitted state transitions are possible

### State machines (3 of them)

**Order state machine:**
```
[*] → Open
Open → In Progress (process)
Open → Cancelled (cancel)
In Progress → Cancelled (cancel)
In Progress → Done (complete)
Cancelled → Open (reopen)
Done → Open (reopen)
```

**Order transaction state machine (payment):**
States: Open, In Progress, Authorized, Unconfirmed, Paid, Paid partially,
Reminded, Refunded, Refunded partially, Cancelled, Failed, Chargeback

**Order delivery state machine (shipping):**
States: Open, Shipped, Shipped partially, Returned, Returned partially, Cancelled

---

## Payments (payments.md)

### Payment flow (2 essential steps)

1. **Place order** (Place Order)
2. **Handle payment** (Handle Payment)

### The steps in detail

#### 1. Choose the payment method
- Stored in the user context (`/store-api/context`)

#### 2. Place the order
- Creates the order based on the current context + cart
- Shopware creates the order + an open transaction (placeholder for the payment)
- The transaction contains: a unique ID, the payment method, the total amount

#### 2.1 Prepare the payment (optional)
- Some integrations create a payment reservation / authorisation here
- Not standardised by Shopware

#### 3. Process the payment (Handle Payment)
- Starts the payment; determines the correct payment handler

#### 3.1 Payment handler types

| Type | Description |
|---|---|
| **Synchronous** | Direct API request to the gateway; immediate response |
| **Asynchronous** | User redirect; the redirect URL contains transaction info + callback URL |

Headless: Shopware returns the redirect URL in the API response.
Default storefront: the redirect happens automatically.

#### 3.2 Payment execution at the gateway (asynchronous only)
- The user performs final checks/authorisations in the gateway UI
- The gateway redirects to the callback URL with the payment result

#### 3.3 Finalise the payment (asynchronous only)
- Triggered via the callback URL → `/payment/finalize-transaction`
- Shopware updates the transaction status
- Redirect to the corresponding finish page

### Notes

- Do **not** use the session in headless payment integrations
- No logic in controllers; add Store API routes for headless
- Specific implementation details differ per provider
