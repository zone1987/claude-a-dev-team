# Discord SKU Resource

Complete reference for the Discord SKU object, its types, its flags and the List SKUs endpoint.
Distilled from `https://docs.discord.com/developers/resources/sku`, retrieved 2026-08-26.

## Table of contents

- [What a SKU is](#what-a-sku-is)
- [SKU Object](#sku-object)
  - [SKU Structure](#sku-structure)
  - [SKU Example](#sku-example)
  - [SKU Types](#sku-types)
  - [SKU Flags](#sku-flags)
- [Endpoints](#endpoints)
  - [GET /applications/{application.id}/skus](#get-applicationsapplicationidskus)
- [Fields present in the payload but absent from the documented structure](#fields-present-in-the-payload-but-absent-from-the-documented-structure)
- [Source](#source)

## What a SKU is

SKUs (stock-keeping units) in Discord represent premium offerings that can be made available to
your application's users or guilds.

## SKU Object

### SKU Structure

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | ID of SKU |
| type | integer | Type of SKU — see [SKU Types](#sku-types) |
| application_id | snowflake | ID of the parent application |
| name | string | Customer-facing name of your premium offering |
| slug | string | System-generated URL slug based on the SKU's name |
| flags | integer | SKU flags combined as a bitfield — see [SKU Flags](#sku-flags). A bitfield is the standard bitwise-packed-integer representation (`https://en.wikipedia.org/wiki/Bit_field`) |

No field in this table is marked optional or nullable by the upstream page: the SKU structure table
carries no `?` markers and no `?Type` prefixes.

### SKU Example

```json
{
  "id": "1088510058284990888",
  "type": 5,
  "dependent_sku_id": null,
  "application_id": "788708323867885999",
  "manifest_labels": null,
  "access_type": 1,
  "name": "Test Premium",
  "features": [],
  "release_date": null,
  "premium": false,
  "slug": "test-premium",
  "flags": 128,
  "show_age_gate": false
}
```

### SKU Types

For subscriptions, SKUs will have a type of either `SUBSCRIPTION` represented by `type: 5` or
`SUBSCRIPTION_GROUP` represented by `type: 6`. For any current implementations, you will want to use
the SKU defined by `type: 5`. A `SUBSCRIPTION_GROUP` is automatically created for each `SUBSCRIPTION`
SKU and are not used at this time.

| Type | Value | Description |
| --- | --- | --- |
| DURABLE | 2 | Durable one-time purchase |
| CONSUMABLE | 3 | Consumable one-time purchase |
| SUBSCRIPTION | 5 | Represents a recurring subscription |
| SUBSCRIPTION_GROUP | 6 | System-generated group for each SUBSCRIPTION SKU created |

Values `0`, `1` and `4` are not documented on the SKU page: the upstream table lists only 2, 3, 5
and 6.

### SKU Flags

For subscriptions, there are two types of access levels you can offer to users:

- **Guild Subscriptions**: A subscription purchased by a user and applied to a single server.
  Everyone in that server gets your premium benefits.
- **User Subscriptions**: A subscription purchased by a user for themselves. They get access to your
  premium benefits in every server.

The `flags` field can be used to differentiate user and server subscriptions with a bitwise `&`
operator.

| Type | Value | Description |
| --- | --- | --- |
| AVAILABLE | `1 << 2` | SKU is available for purchase |
| GUILD_SUBSCRIPTION | `1 << 7` | Recurring SKU that can be purchased by a user and applied to a single server. Grants access to every user in that server. |
| USER_SUBSCRIPTION | `1 << 8` | Recurring SKU purchased by a user for themselves. Grants access to the purchasing user in every server. |

Decimal equivalents of those shifts: `1 << 2` is 4, `1 << 7` is 128, `1 << 8` is 256. The example
payloads on the page carry `"flags": 128`, which is `GUILD_SUBSCRIPTION` set and `AVAILABLE` clear.

## Endpoints

### GET /applications/{application.id}/skus

**List SKUs.** Returns all SKUs for a given application.

`{application.id}` is the ID of the application whose SKUs are listed; it resolves against the
Application object.

Because of how Discord's SKU and subscription systems work, you will see two SKUs for your
subscription offering. For integration and testing entitlements for Subscriptions, you should use
the SKU with `type: 5`.

The upstream page documents no query string parameters, no JSON parameters, no pagination and no
error responses for this endpoint. It states only the success payload, which is an array of SKU
objects:

```json
[
  {
    "id": "1088510053843210999",
    "type": 6,
    "dependent_sku_id": null,
    "application_id": "788708323867885999",
    "manifest_labels": null,
    "access_type": 1,
    "name": "Test Premium",
    "features": [],
    "release_date": null,
    "premium": false,
    "slug": "test-premium",
    "flags": 128,
    "show_age_gate": false
  },
  {
    "id": "1088510058284990888",
    "type": 5,
    "dependent_sku_id": null,
    "application_id": "788708323867885999",
    "manifest_labels": null,
    "access_type": 1,
    "name": "Test Premium",
    "features": [],
    "release_date": null,
    "premium": false,
    "slug": "test-premium",
    "flags": 128,
    "show_age_gate": false
  }
]
```

Note the pairing in that response: the `type: 6` entry is the auto-created `SUBSCRIPTION_GROUP`, the
`type: 5` entry is the `SUBSCRIPTION` SKU you integrate against. Both share the same `name` and
`slug`.

There is no documented endpoint for creating, updating, publishing, unpublishing or deleting a SKU
over HTTP. SKU lifecycle management happens in the Developer Portal — see the SKU management steps
in `IMPLEMENTING.md`. Deleted SKUs are still listed by this endpoint.

## Fields present in the payload but absent from the documented structure

The SKU examples on the page contain nine keys that the SKU Structure table does not define. The
upstream page is silent on their type and meaning; they are recorded here verbatim because a client
will receive them:

| Key seen in payload | Observed value in the examples | Upstream description |
| --- | --- | --- |
| dependent_sku_id | `null` | not documented |
| manifest_labels | `null` | not documented |
| access_type | `1` | not documented |
| features | `[]` | not documented |
| release_date | `null` | not documented |
| premium | `false` | not documented |
| show_age_gate | `false` | not documented |

Two further keys appear in the Social Commerce and Activities prose rather than in the SKU page's own
tables:

- **price**: the SKU listing methods of the Embedded App SDK automatically localize currency and
  prices, so `sku.price` has a number `amount` attribute and a string `currency` attribute. See
  `IMPLEMENTING.md` for `PriceUtils.formatPrice`. The SKU Structure table does not list `price`, so
  its presence on an HTTP API SKU object is not documented.

Do not depend on an undocumented key. Map SKUs to your perks by `id`, never by `name` or any other
attribute.

## Source

Discord Developer Documentation:

- `https://docs.discord.com/developers/resources/sku`
- `https://docs.discord.com/developers/monetization/overview` (the two types of SKUs)
- `https://docs.discord.com/developers/monetization/implementing-iap-for-activities` (`sku.price`)

Retrieved 2026-08-26.
