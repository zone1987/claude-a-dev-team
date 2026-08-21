# Glossary

OCTO's core terms, reused throughout the specification. Getting these wrong is the most common
source of a mismodelled integration, because several map onto different words in e-commerce.

| Term | Meaning |
|---|---|
| **Reseller** | The distributor connecting to a supplier via the API to resell products. You, in most integrations. |
| **Supplier** | The operator that provides the products and runs Ventrata. |
| **Product** | An attraction, activity or tour offered by a supplier. |
| **Option** | A product variant. **Every product has at least one option.** |
| **Unit** | A ticket type — Adult, Child, Senior. |
| **Unit Item** | A line item for a specific unit inside a booking. One guest, one unit item. |
| **Booking** | A reservation for a specific product option with one or more unit items. |
| **Voucher** | A single admission document for the **whole booking** — barcode, QR code, PDF. |
| **Ticket** | An admission document for **each unit item**. |

## Distinctions that matter

- **Unit versus Unit Item.** A `Unit` is a *type* in the catalogue ("Adult"); a `BookingUnitItem` is
  an *instance* in a booking (this adult). Availability speaks in units; a booking speaks in unit
  items.
- **Voucher versus Ticket.** The difference is granularity, not format: one per booking against one
  per person. `deliveryMethods` on the product says which apply.
- **Option is never optional.** Despite the name, an option is a mandatory variant layer — a product
  always has at least one, usually flagged `default`.
- **Product is not a catalogue entry you own.** It belongs to the supplier and is reached through
  your connection; two suppliers can offer near-identical products with unrelated IDs.

## Source

[docs.ventrata.com/getting-started/glossary-of-terms](https://docs.ventrata.com/getting-started/glossary-of-terms),
retrieved 2026-08-20.
