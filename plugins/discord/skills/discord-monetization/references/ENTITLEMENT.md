# Discord Entitlement Resource

Complete reference for the Discord Entitlement object, its types, all five endpoints and the
entitlement Gateway events. Distilled from
`https://docs.discord.com/developers/resources/entitlement`, retrieved 2026-08-26.

## Table of contents

- [What an entitlement is](#what-an-entitlement-is)
- [Entitlement Object](#entitlement-object)
  - [Entitlement Structure](#entitlement-structure)
  - [Entitlement Example](#entitlement-example)
  - [Entitlement Types](#entitlement-types)
  - [Fields present in the payload but absent from the documented structure](#fields-present-in-the-payload-but-absent-from-the-documented-structure)
- [Endpoints](#endpoints)
  - [GET /applications/{application.id}/entitlements](#get-applicationsapplicationidentitlements)
  - [GET /applications/{application.id}/entitlements/{entitlement.id}](#get-applicationsapplicationidentitlementsentitlementid)
  - [POST /applications/{application.id}/entitlements/{entitlement.id}/consume](#post-applicationsapplicationidentitlementsentitlementidconsume)
  - [POST /applications/{application.id}/entitlements](#post-applicationsapplicationidentitlements)
  - [DELETE /applications/{application.id}/entitlements/{entitlement.id}](#delete-applicationsapplicationidentitlementsentitlementid)
- [Entitlement Gateway events](#entitlement-gateway-events)
- [Three ways to read an entitlement](#three-ways-to-read-an-entitlement)
- [Source](#source)

## What an entitlement is

Entitlements in Discord represent that a user or guild has access to a premium offering in your
application.

**Entitlements are the source of truth for access.** Subscription status is not. When implementing
monetization, use the presence of an entitlement to decide whether to grant a premium feature; the
Subscription API exists for reporting and lifecycle management that happens outside a user's
interaction flow.

## Entitlement Object

### Entitlement Structure

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | ID of the entitlement |
| sku_id | snowflake | ID of the SKU |
| application_id | snowflake | ID of the parent application |
| user_id? | snowflake | ID of the user that is granted access to the entitlement's sku |
| type | integer | Type of entitlement — see [Entitlement Types](#entitlement-types) |
| deleted | boolean | Entitlement was deleted |
| starts_at | ?ISO8601 timestamp | Start date at which the entitlement is valid. |
| ends_at | ?ISO8601 timestamp | Date at which the entitlement is no longer valid. |
| guild_id? | snowflake | ID of the guild that is granted access to the entitlement's sku |
| consumed? | boolean | For consumable items, whether or not the entitlement has been consumed |

Reading the markers: `?` after a field name means the field is optional and may be absent;
`?` before the type means the value is nullable.

- **Optional**: `user_id`, `guild_id`, `consumed`.
- **Nullable**: `starts_at`, `ends_at`.
- **Always present and non-null per the table**: `id`, `sku_id`, `application_id`, `type`, `deleted`.

Behavioural notes the pages state about these fields:

- **`ends_at` is null for an active app subscription.** The entitlement is granted indefinitely until
  the user cancels. When the subscription ends, an `ENTITLEMENT_UPDATE` arrives with an `ends_at`
  timestamp indicating when the subscription ended.
- **A test entitlement has no `starts_at` or `ends_at`** — it is valid in perpetuity until deleted.
  The create-test-entitlement response also omits `subscription_id`.
- **`consumed` becomes `true`** after a successful call to the consume endpoint, visible on List
  Entitlements.

### Entitlement Example

```json
{
  "id": "1019653849998299136",
  "sku_id": "1019475255913222144",
  "application_id": "1019370614521200640",
  "user_id": "771129655544643584",
  "promotion_id": null,
  "type": 8,
  "deleted": false,
  "gift_code_flags": 0,
  "consumed": false,
  "starts_at": "2022-09-14T17:00:18.704163+00:00",
  "ends_at": "2022-10-14T17:00:18.704163+00:00",
  "guild_id": "1015034326372454400",
  "subscription_id": "1019653835926409216"
}
```

### Entitlement Types

| Type | Value | Description |
| --- | --- | --- |
| PURCHASE | 1 | Entitlement was purchased by user |
| PREMIUM_SUBSCRIPTION | 2 | Entitlement for Discord Nitro subscription |
| DEVELOPER_GIFT | 3 | Entitlement was gifted by developer |
| TEST_MODE_PURCHASE | 4 | Entitlement was purchased by a dev in application test mode |
| FREE_PURCHASE | 5 | Entitlement was granted when the SKU was free |
| USER_GIFT | 6 | Entitlement was gifted by another user |
| PREMIUM_PURCHASE | 7 | Entitlement was claimed by user for free as a Nitro Subscriber |
| APPLICATION_SUBSCRIPTION | 8 | Entitlement was purchased as an app subscription |

`type: 4` (`TEST_MODE_PURCHASE`) is how you identify entitlements created by purchases made while
Application Test Mode is on. `type: 8` (`APPLICATION_SUBSCRIPTION`) is what an app subscription
purchase produces, and it is the type in every example payload on the page.

### Fields present in the payload but absent from the documented structure

The example payloads carry three keys the Entitlement Structure table does not define. The upstream
page states no type or meaning for them:

| Key seen in payload | Observed value in the examples | Upstream description |
| --- | --- | --- |
| promotion_id | `null` | not documented |
| gift_code_flags | `0` | not documented |
| subscription_id | `"1019653835926409216"` | not documented in the structure table, but named twice in prose: the create-test-entitlement response will **not** contain it |

`subscription_id` is the link from an entitlement back to the Subscription object that produced it,
and the Subscription object carries the reverse link in `entitlement_ids`.

## Endpoints

### GET /applications/{application.id}/entitlements

**List Entitlements.** Returns all entitlements for a given app, active and expired.

#### Query String Params

| param | type | description |
| --- | --- | --- |
| user_id? | snowflake | User ID to look up entitlements for |
| sku_ids? | comma-delimited set of snowflakes | Optional list of SKU IDs to check entitlements for |
| before? | snowflake | Retrieve entitlements before this entitlement ID |
| after? | snowflake | Retrieve entitlements after this entitlement ID |
| limit? | integer | Number of entitlements to return, 1-100, default 100 |
| guild_id? | snowflake | Guild ID to look up entitlements for |
| exclude_ended? | boolean | Whether or not ended entitlements should be omitted. Defaults to false, ended entitlements are included by default. |
| exclude_deleted? | boolean | Whether or not deleted entitlements should be omitted. Defaults to true, deleted entitlements are not included by default. |

Every parameter is optional. The two boolean parameters follow Discord's boolean query string
convention (`true`/`false` as literal strings in the query, documented at
`https://docs.discord.com/developers/reference#boolean-query-strings`).

Response:

```json
[
  {
    "id": "1019653849998299136",
    "sku_id": "1019475255913222144",
    "application_id": "1019370614521200640",
    "user_id": "771129655544643584",
    "promotion_id": null,
    "type": 8,
    "deleted": false,
    "gift_code_flags": 0,
    "consumed": false,
    "starts_at": "2022-09-14T17:00:18.704163+00:00",
    "ends_at": "2022-10-14T17:00:18.704163+00:00",
    "guild_id": "1015034326372454400",
    "subscription_id": "1019653835926409216"
  }
]
```

The upstream page documents no error responses and no explicit success status code for this endpoint.

### GET /applications/{application.id}/entitlements/{entitlement.id}

**Get Entitlement.** Returns an entitlement.

`{entitlement.id}` resolves against the Entitlement object. No query or JSON parameters are
documented.

Response:

```json
{
  "id": "1019653849998299136",
  "sku_id": "1019475255913222144",
  "application_id": "1019370614521200640",
  "user_id": "771129655544643584",
  "promotion_id": null,
  "type": 8,
  "deleted": false,
  "gift_code_flags": 0,
  "consumed": false,
  "starts_at": "2022-09-14T17:00:18.704163+00:00",
  "ends_at": "2022-10-14T17:00:18.704163+00:00",
  "guild_id": "1015034326372454400",
  "subscription_id": "1019653835926409216"
}
```

### POST /applications/{application.id}/entitlements/{entitlement.id}/consume

**Consume an Entitlement.** For One-Time Purchase consumable SKUs, marks a given entitlement for the
user as consumed. The entitlement will have `consumed: true` when using List Entitlements.

Returns a `204 No Content` on success.

No query or JSON parameters are documented; there is no request body.

Why it matters: **users cannot repurchase a consumable SKU until you consume the entitlement.** A
user can hold only one unconsumed entitlement per consumable SKU at a time. On receiving
`ENTITLEMENT_CREATE` for a consumable SKU, process the purchase in your app and consume the
entitlement as soon as possible. In Application Test Mode, repeated purchases are permitted without
consumption for developer convenience.

### POST /applications/{application.id}/entitlements

**Create Test Entitlement.** Creates a test entitlement to a given SKU for a given guild or user.
Discord will act as though that user or guild has entitlement to your premium offering.

This endpoint returns a **partial** entitlement object. It will **not** contain `subscription_id`,
`starts_at`, or `ends_at`, as it's valid in perpetuity.

After creating a test entitlement, you'll need to reload your Discord client. After doing so, you'll
see that your server or user now has premium access.

#### JSON Params

| param | type | description |
| --- | --- | --- |
| sku_id | string | ID of the SKU to grant the entitlement to |
| owner_id | string | ID of the guild or user to grant the entitlement to |
| owner_type | integer | `1` for a guild subscription, `2` for a user subscription |

All three parameters are documented without a `?` marker, so all three are required. Note that
`sku_id` and `owner_id` are typed `string`, not `snowflake`, in this table.

```json
{
  "sku_id": "999184799365857331",
  "owner_id": "847184799365857999",
  "owner_type": 1
}
```

**Do NOT use Test Entitlements for One-Time Purchases.** The documented method for testing one-time
purchases is Application Test Mode; test entitlements are the method for App Subscriptions. See
`IMPLEMENTING.md`.

### DELETE /applications/{application.id}/entitlements/{entitlement.id}

**Delete Test Entitlement.** Deletes a currently-active test entitlement. Discord will act as though
that user or guild *no longer has* entitlement to your premium offering.

Returns `204 No Content` on success.

**You can only delete entitlements created using the Create Test Entitlement endpoint.** If you need
to toggle access to your premium features during development, use test entitlements rather than a
live purchase.

## Entitlement Gateway events

Three entitlement events exist. Their payloads are Entitlement objects; the dispatch mechanics live
in the Gateway skill.

| Event | Description |
| --- | --- |
| `ENTITLEMENT_CREATE` | When a user is granted an entitlement to your app's subscription SKU. For one-time purchases, when a user purchases a SKU. |
| `ENTITLEMENT_UPDATE` | When an entitlement to a subscription SKU ends. `ends_at` gets updated with a timestamp. |
| `ENTITLEMENT_DELETE` | When Discord refunds a subscription, removes an entitlement, or when a developer deletes a Test Entitlement. For one-time purchases, you may also receive this if the user's entitlement is revoked. |

Notable silences and asymmetries the pages call out:

- **Cancellation emits no entitlement event.** "When a user cancels their subscription, your app will
  not receive any entitlement events." The `SUBSCRIPTION_UPDATE` event carries the cancellation.
- **Renewal emits no entitlement event either** — entitlements are granted indefinitely and do not
  update on renewal, which is why subscription events exist for lifecycle tracking.
- In an Activity, `ENTITLEMENT_CREATE` is also available through the Embedded App SDK
  `subscribe()` method, and is how you learn that a `startPurchase()` flow completed.

Entitlement events per lifecycle scenario (starting, cancelling, resuming, upgrading, downgrading a
subscription) are tabulated in `SUBSCRIPTION.md`.

## Three ways to read an entitlement

Depending on your app's features, combine these:

1. **Gateway events** — `ENTITLEMENT_CREATE` / `_UPDATE` / `_DELETE`, for near-time tracking.
2. **The HTTP API** — List Entitlements, for background processing and apps not solely reliant on
   interactions. Filter with `?user_id=XYZ`, `?guild_id=XYZ` or `?sku_ids=XYZ`. Example use: keep
   entitlements in a database and check a user still has access to a SKU before running a cron job.
3. **Interaction payloads** — the `entitlements` field on the Interaction Payload when a user
   interacts with your app. Use it to decide whether the user or guild is subscribed. For guild
   subscriptions, the entitlement is present on interactions initiated by any user in that guild.
4. **The Embedded App SDK** — `getEntitlements()` in an Activity.

**Trust the SDK, but verify via the API.** Data fetched from the Discord HTTP API by your backend can
be trusted and is the source of truth; SDK data can be forged by a malicious actor who establishes
their own RPC connection posing as Discord. Use SDK commands and events optimistically on the client,
then verify server-side. This matters most for `getEntitlements()`.

## Source

Discord Developer Documentation:

- `https://docs.discord.com/developers/resources/entitlement`
- `https://docs.discord.com/developers/monetization/implementing-app-subscriptions`
- `https://docs.discord.com/developers/monetization/implementing-one-time-purchases`
- `https://docs.discord.com/developers/monetization/implementing-iap-for-activities`

Retrieved 2026-08-26.
