# After confirmation

What to read from the response once `POST /bookings/{uuid}/confirm` succeeds. This is documented
prose on the Bookings page, not derivable from the schema: every field below exists in the schema,
but which ones matter and when is the part that is written down.

## Contents

- [The five fields to prioritise](#the-five-fields-to-prioritise)
- [VOUCHER or TICKET](#voucher-or-ticket)
- [Delivery options](#delivery-options)
- [Example response](#example-response)

## The five fields to prioritise

- **booking.supplierReference**: human-readable supplier reference. Give it to the guest and store
  it — customer support and billing reconciliation run on this value, not on the `uuid`.
- **booking.voucher**: the ticket media object for the whole booking. Use it when
  `booking.deliveryMethods` contains `VOUCHER`.
- **booking.unitItems[].ticket**: one ticket media object per person. Use it when
  `booking.deliveryMethods` contains `TICKET`.
- **booking.pricing.retail**: the amount in minor units you must charge the guest.
- **booking.pricing.net**: the amount in minor units the supplier will invoice you.

`retail` and `net` are both present and both matter: the difference is your margin. Charging `net`
loses money; invoicing `retail` overcharges the supplier. Amounts are in **minor units** —
`4600` with `currencyPrecision: 2` is 46.00, not 4600.

## VOUCHER or TICKET

`booking.deliveryMethods` decides which media object carries the guest's entitlement:

| `deliveryMethods` contains | Read |
|---|---|
| `VOUCHER` only | `booking.voucher` — one object for the booking |
| `TICKET` only | `booking.unitItems[].ticket` — one object per unit item |
| both | either: the reseller picks what the guest prefers |

When both are present the choice is yours — one voucher for the party, or one ticket per person.
Neither is more correct; pick per guest preference and stay consistent within a booking.

Do not assume one shape. A product that returned `VOUCHER` yesterday can return `TICKET` today, so
branch on `deliveryMethods` at read time rather than at integration time.

## Delivery options

`booking.voucher` and `booking.unitItems[].ticket` have **the same shape**, so one rendering
function handles both. Guest-facing media sits in `deliveryOptions[]`, each entry a
`deliveryFormat` / `deliveryValue` pair — for example `PDF_URL`, `QRCODE`, and wallet links.

The URLs are returned directly in `deliveryOptions[].deliveryValue`; there is no separate download
call to make.

## Example response

Trimmed to the fields that matter after confirmation:

```json
{
  "supplierReference": "SUP-20260304-009871",
  "productId": "e7cc8bb4-8d1c-4848-8824-5dbedb718681",
  "optionId": "94cdd032-3d32-416d-b0a4-abf8b7495b8b",
  "availabilityId": "2026-03-04T18:30:00+01:00",
  "deliveryMethods": ["VOUCHER", "TICKET"],
  "voucher": {
    "deliveryOptions": [
      {
        "deliveryFormat": "PDF_URL",
        "deliveryValue": "https://api.ventrata.com/octo/download/booking/89fe0192-….pdf"
      }
    ]
  },
  "unitItems": [
    {
      "ticket": {
        "deliveryOptions": [
          { "deliveryFormat": "QRCODE", "deliveryValue": "TKT-11111111" }
        ]
      }
    }
  ],
  "pricing": { "retail": 4600, "net": 3220, "currency": "USD", "currencyPrecision": 2 }
}
```

## Source

[docs.ventrata.com/octo-core/bookings](https://docs.ventrata.com/octo-core/bookings), section
"After Confirmation: Fields to Use", retrieved 2026-08-20. Field definitions in
[BOOKING-SCHEMA.md](BOOKING-SCHEMA.md) come from `openapi.yaml` 3.0.3.
