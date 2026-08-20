# Capabilities

## Contents

- [Discovery endpoints](#discovery-endpoints)
- [The Capability object](#the-capability-object)
- [All 23 capabilities](#all-23-capabilities)
- [Requesting capabilities](#requesting-capabilities)
- [Capability IDs are not page names](#capability-ids-are-not-page-names)

## Discovery endpoints

- **`GET /capabilities`** — the non-internal capabilities available from the API. Returns a
  `CapabilityList`. The documentation also writes this route as **`/octo/capabilities`**: `/octo` is
  the server path prefix (`https://api.ventrata.com/octo`), so both spellings mean the same request.
- **`GET /whoami`** — supplier, connection and partner context for the current API key. Returns a
  `WhoAmI`.

There is no `/supplier` endpoint. `Supplier` and `SupplierList` exist as schemas only.

Call `GET /capabilities` once per connection instead of guessing: the supplier decides which
capabilities your connection may use, and requesting one they have not enabled drops it from the
response rather than raising an error.

## The Capability object

The shape returned on product payloads and by `/octo/capabilities`:

| Field | Meaning |
|---|---|
| `id` | Capability ID to include in `Octo-Capabilities`. |
| `revision` | Supported, backward-compatible capability revision. |
| `required` | Whether the capability is required to sell that product. |
| `dependencies` | Capability IDs that are auto-included when needed. |
| `docs` | Documentation URL, when the API provides one. |

`required: true` is the field that changes behaviour: a product can be unsellable without the
capability, so discovery is not merely informational. `dependencies` means you may receive fields
from a capability you did not ask for.

## All 23 capabilities

The API surface column says what each capability actually extends — the reason to enable it.

| ID | Internal | Documentation name | API surface |
|---|---|---|---|
| `octo/pricing` | No | Pricing | Pricing fields across products, availability, bookings, orders, gifts |
| `octo/content` | No | Content | Extends product, option, unit, availability and booking content fields |
| `octo/offers` | No | Promotions / Offers | Supplier offers and offer-aware pricing and booking responses |
| `octo/extras` | No | Extras | Extra upsell inventory and booking extra-item behaviour |
| `octo/packages` | No | Packages | Package includes and package booking flows |
| `octo/pickups` | No | Pickups | Pickup and dropoff fields on product, availability and booking |
| `octo/questions` | No | Custom Questions | Question schemas and `questionAnswers` write flows |
| `octo/waivers` | No | Waivers | Waiver templates on products; submission and status fields on booking and unit-item flows |
| `octo/resources` | No | Resources | Availability resources and resource allocations |
| `octo/rentals` | No | Rentals | `rentalDurationId` behaviour across product, availability and booking |
| `octo/redemption` | No | Redemption | Redemption lookup, redeem and unredeem, no-show, credential resolution |
| `octo/mappings` | No | Self-Service Mapping | Self-service mapping write and read flows |
| `octo/cart` | No | Multi-Booking Cart | Order create, list, update, confirm and cancel flows |
| `octo/gifts` | No | Gift Vouchers | Gift voucher create, list, update, confirm and cancel flows |
| `octo/checkin` | No | Online Check-in | Check-in lookup and check-in fields on bookings, orders and gifts |
| `octo/cardPayments` | No | Card Payments | Card payment flows on booking, order and gift, plus card payment lookup |
| `octo/memberships` | No | Memberships | Membership lookup and membership-booking listing |
| `octo/adjustments` | No | Price Adjustments | Extends booking create and update pricing inputs (`adjustments`) |
| `octo/webhooks` | No | Webhooks | Webhook create, update, list, delete and trigger flows |
| `octo/waitlists` | No | Waitlists | Waitlist create flow |
| `octo/identities` | **Yes** | Identities | Identity create, update, delete and `identityId` linkage |
| `octo/campaigns` | No | Campaigns | Campaign listing endpoint support |
| `octo/notifications` | No | Notifications | Notification subscription CRUD flows |

Where each is documented in this plugin: commerce group — `pricing`, `offers`, `cart`, `packages`,
`cardPayments`, `gifts`, `adjustments`. Fulfilment group — `redemption`, `extras`, `pickups`,
`rentals`, `resources`, `waivers`, `questions`, `checkin`. Platform group — `webhooks`,
`notifications`, `content`, `mappings`, `memberships`, `campaigns`, `waitlists`, `identities`.

`octo/identities` is the only internal capability: it is not returned by `GET /capabilities` and is
not available to a normal reseller connection.

## Requesting capabilities

> Send requested capability IDs in the `Octo-Capabilities` request header on any OCTO endpoint (or
> `X-Capabilities` as the legacy alias). Capability IDs are requested uniformly via headers across
> all endpoints.
>
> The response echoes applied capabilities in the `Octo-Capabilities` response header.

So there is no per-endpoint capability parameter: one header, every route. Compare the response
header against what you sent — a capability your connection cannot use is dropped silently.

## Capability IDs are not page names

Three IDs differ from the documentation page that describes them. Send the ID, not the slug:

| Documentation page | Actual header value |
|---|---|
| `capabilities/gift-vouchers` | `octo/gifts` |
| `capabilities/online-check-in` | `octo/checkin` |
| `capabilities/card-payments` | `octo/cardPayments` |

`octo/cardPayments` is the only camelCase ID; every other ID is lowercase. Getting it wrong returns a
response without the capability's fields rather than an error, which makes it a slow bug to find.

## Source

[docs.ventrata.com/getting-started/request-capabilities](https://docs.ventrata.com/getting-started/request-capabilities),
retrieved 2026-08-20, and `openapi.yaml` 3.0.3 (`GET /capabilities`, `GET /whoami`, `Capability`).
Ventrata documents this set as sourced from their API implementation, so it reflects the
reseller-facing capabilities rather than every internal flag.
