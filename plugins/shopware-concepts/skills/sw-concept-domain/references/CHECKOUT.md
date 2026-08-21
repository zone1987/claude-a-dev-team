# Shopware checkout — concept

Complete concept documentation: `CHECKOUT-DETAIL.md`

## Quick overview

### Cart

- **Not via the DAL** — the cart is stored/loaded as a whole (no EntityRepository)
- **States**: Empty → Dirty (after a change) → Calculated
- **Calculation** (4 phases): Enrich → Process → Validate → Persist
- **Line items** — stackable, removable; can contain other line items (bundles)
- **Enrichment** — products, promotions, shipping costs are loaded lazily
- **Rule validation** — iterative until stable (e.g. buy product → free sunglasses → discount)
- **CartService** — central facade for all cart operations

### Orders

- **Denormalised** — all data is persisted at the time of ordering (no catalogue dependency)
- **Three state machines**: Order, Order Transaction (payment), Order Delivery (shipping)
- **Workflow-optimised** — only defined state transitions are allowed

### Payments

- **Synchronous** — direct feedback from the gateway
- **Asynchronous** — redirect flow; callback URL `/payment/finalize-transaction`
- **Payment handler** — central extension point; registered in the database

Technical implementation: `shopware-checkout` (dev plugin)
