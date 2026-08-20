---
name: octo-capabilities-commerce
description: 'OCTO/Ventrata commerce capabilities: pricing, offers, cart, packages, card payments, gift vouchers, adjustments. Use when the request names an octo/* commerce capability such as octo/pricing.'
---

# OCTO commerce capabilities

Everything that touches money. Request a capability by adding its ID to the `Octo-Capabilities`
header; the fields it adds are merged into the core schemas, and some capabilities also unlock
endpoints of their own.

## The capabilities

- **octo/pricing** (35 fields, 16 schemas): prices on products, options, units, availability and
  bookings. The widest-reaching capability in the API — almost nothing commercial works without it.
  → [PRICING.md](PRICING.md)
- **octo/offers** (37 fields, 1 endpoint): discounts and promotional offers, including
  `offerDiscount` on every pricing object. → [OFFERS.md](OFFERS.md)
- **octo/cart** (11 fields, 10 endpoints): multi-product carts and orders, for a basket that spans
  several products before checkout. → [CART.md](CART.md)
- **octo/packages** (12 fields): products that bundle other products. → [PACKAGES.md](PACKAGES.md)
- **octo/gifts** (8 fields, 10 endpoints): gift vouchers — purchase, redeem, check balance.
  The ID is `octo/gifts`, not `octo/gift-vouchers`. → [GIFTS.md](GIFTS.md)
- **octo/cardPayments** (1 endpoint): card payment records. The only camelCase capability ID in the
  API, and its path is `/card_payments` with an underscore. → [CARD-PAYMENTS.md](CARD-PAYMENTS.md)
- **octo/adjustments** (1 field): booking-level price adjustments and commission handling.
  → [ADJUSTMENTS.md](ADJUSTMENTS.md)

## Combining capabilities

Send several comma-separated: `Octo-Capabilities: octo/pricing, octo/offers`. Some capabilities
declare `dependencies` that are pulled in automatically — check `GET /capabilities` rather than
guessing which.

Request only what you parse. `octo/pricing` alone widens 16 schemas; asking for everything makes
every response larger and slower for no benefit.

## Prices ending in `From` are indicative

Fields such as `pricingFrom` are a "starting at" figure for display, not a quotable price. The
final price comes from availability or from the booking response. Quoting a `From` value as the
price is a real-money bug.

## Source

Field lists generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`,
retrieved 2026-08-20 — see `scripts/extract_caps.py`. Narrative from
[docs.ventrata.com/capabilities](https://docs.ventrata.com/capabilities) (one page per capability).
