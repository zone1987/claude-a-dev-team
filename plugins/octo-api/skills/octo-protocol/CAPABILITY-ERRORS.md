# Capability error codes

Error codes a capability adds on top of the ten protocol-wide codes in [ERRORS.md](ERRORS.md). They arrive in the same `400` body shape: `error` carries the code, `errorMessage` the localized text.

21 codes across 9 capabilities. A code only ever appears when its capability is active, so switch on `error` and fall back on the protocol codes.

## Contents

- [`octo/adjustments`](#octoadjustments)
- [`octo/cardPayments`](#octocardpayments)
- [`octo/checkin`](#octocheckin)
- [`octo/extras`](#octoextras)
- [`octo/gifts`](#octogifts)
- [`octo/pricing`](#octopricing)
- [`octo/questions`](#octoquestions)
- [`octo/rentals`](#octorentals)
- [`octo/waivers`](#octowaivers)

## `octo/adjustments`

- **ADJUSTMENTS_INVALID_NET_DISCOUNT**: fires when the adjustment's `netDiscount` value is not one of the allowed modes.
- **ADJUSTMENTS_INVALID_PER**: fires when the adjustment's `per` value is not one of `BOOKING`, `UNIT`, `PERCENTAGE`.
- **ADJUSTMENTS_NET_DISCOUNT_NOT_ALLOWED**: fires when a `netDiscount` was sent where the connection does not permit one.

## `octo/cardPayments`

- **GATEWAY_CURRENCY_MISMATCH**: fires when the payment currency differs from the booking currency.
- **GATEWAY_INVALID_SOURCE**: fires when `source` is not one of `POS`, `ECOM`, `MOTO` for this gateway.
- **GATEWAY_MISMATCH**: fires when the gateway in the request does not match the one on the connection.
- **INVALID_CARD_ID**: fires when the `cardId` sent does not exist.
- **PAYMENT_PENDING**: fires when the payment has not settled yet; poll rather than treating it as a failure.

## `octo/checkin`

- **BOOKING_NOT_FOUND**: fires when no booking matches the check-in lookup.

## `octo/extras`

- **EXTRAS_QTY_LIMIT**: fires when a booking-level extra exceeds its configured quantity limit.
- **EXTRAS_RETAIL_ABOVE_MAXIMUM**: fires when the custom `retail` amount is above `restrictions.maxCustomRetail`.
- **EXTRAS_RETAIL_BELOW_MINIMUM**: fires when the custom `retail` amount is below `restrictions.minCustomRetail`.
- **EXTRAS_RETAIL_REQUIRED**: fires when a custom-retail extra was sent without a `retail` amount.
- **EXTRAS_UNIT_QTY_LIMIT**: fires when a unit-level extra exceeds its configured quantity limit.

## `octo/gifts`

- **GIFTS_FIELDS_REQUIRED**: fires when a required gift field is missing from the request.

## `octo/pricing`

- **PRICING_MATCH_REQUIRED**: fires when the price sent does not match the current price; re-read availability and retry.

## `octo/questions`

- **INVALID_QUESTION_ID**: fires when the `questionId` sent is not one of the product's questions.

## `octo/rentals`

- **INVALID_RENTAL_DURATION_ID**: fires when the rental duration ID sent is not offered by the product.

## `octo/waivers`

- **INVALID_WAIVER_ID**: fires when `waiverId` does not match any entry in `product.waivers[]`.
- **WAIVER_ON_BOOKING_ONLY**: fires when a `waiverId` was sent per unit item where the product requires it per booking.
- **WAIVER_ON_TICKET_ONLY**: fires when a `waiverId` was sent at booking level where the product requires it per unit item.

## Source

Extracted from the capability pages at [docs.ventrata.com/capabilities](https://docs.ventrata.com/capabilities), retrieved 2026-08-20, by `scripts/extract_cap_errors.py`. These codes are documented in prose only: the OpenAPI document does not list them.

<!-- prose below this line is written by hand and preserved on regeneration -->
