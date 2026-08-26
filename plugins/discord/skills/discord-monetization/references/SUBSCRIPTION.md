# Discord Subscription Resource

Complete reference for the Discord Subscription object, its statuses, both endpoints, the
subscription Gateway events and the full subscription lifecycle event tables. Distilled from
`https://docs.discord.com/developers/resources/subscription` and
`https://docs.discord.com/developers/monetization/implementing-app-subscriptions`,
retrieved 2026-08-26.

## Table of contents

- [What a subscription is](#what-a-subscription-is)
- [Subscription Object](#subscription-object)
  - [Subscription Structure](#subscription-structure)
  - [Subscription Example](#subscription-example)
  - [Subscription Statuses](#subscription-statuses)
  - [Status is not entitlement](#status-is-not-entitlement)
- [Endpoints](#endpoints)
  - [GET /skus/{sku.id}/subscriptions](#get-skusskuidsubscriptions)
  - [GET /skus/{sku.id}/subscriptions/{subscription.id}](#get-skusskuidsubscriptionssubscriptionid)
- [Subscription Gateway events](#subscription-gateway-events)
- [Lifecycle event tables](#lifecycle-event-tables)
- [Source](#source)

## What a subscription is

Subscriptions in Discord represent a user making recurring payments for at least one SKU over an
ongoing period. Successful payments grant the user access to entitlements associated with the SKU.

Subscription SKUs are automatically charged each month unless canceled.

## Subscription Object

### Subscription Structure

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | ID of the subscription |
| user_id | snowflake | ID of the user who is subscribed |
| sku_ids | array of snowflakes | List of SKUs subscribed to |
| entitlement_ids | array of snowflakes | List of entitlements granted for this subscription |
| renewal_sku_ids | ?array of snowflakes | List of SKUs that this user will be subscribed to at renewal |
| current_period_start | ISO8601 timestamp | Start of the current subscription period |
| current_period_end | ISO8601 timestamp | End of the current subscription period |
| status | SubscriptionStatus | Current status of the subscription — see [Subscription Statuses](#subscription-statuses) |
| canceled_at | ?ISO8601 timestamp | When the subscription was canceled |
| country? | string | ISO3166-1 alpha-2 country code of the payment source used to purchase the subscription. Missing unless queried with a private OAuth scope. |

Reading the markers: `?` after a field name means optional; `?` before the type means nullable.

- **Optional**: `country` — and it is more than optional, it is *missing unless queried with a
  private OAuth scope*.
- **Nullable**: `renewal_sku_ids`, `canceled_at`.
- **Always present per the table**: `id`, `user_id`, `sku_ids`, `entitlement_ids`,
  `current_period_start`, `current_period_end`, `status`.

Behaviour the page states:

- **The start of a subscription is determined by its ID.** When the subscription renews, its current
  period is updated.
- **If the user cancels**, the subscription enters the `ENDING` status and the `canceled_at`
  timestamp reflects the time of the cancellation.
- `entitlement_ids` can be an empty array immediately after creation — the example payload shows
  exactly that, alongside `status: 0`.

### Subscription Example

```json
{
  "id": "1278078770116427839", 
  "user_id": "1088605110638227537", 
  "sku_ids": ["1158857122189168803"], 
  "entitlement_ids": [], 
  "renewal_sku_ids": null,
  "current_period_start": "2024-08-27T19:48:44.406602+00:00", 
  "current_period_end": "2024-09-27T19:48:44.406602+00:00", 
  "status": 0, 
  "canceled_at": null
}
```

### Subscription Statuses

| Type | Value | Description |
| --- | --- | --- |
| ACTIVE | 0 | Subscription is active and scheduled to renew. |
| INACTIVE | 1 | Subscription is inactive and not being charged. |
| ENDING | 2 | Subscription is active but will not renew. |

Subscriptions can start and change between any of these statuses within the current period. A
subscription can be `ACTIVE` outside its current period or `INACTIVE` within its current period.

Some examples of this behavior include:

- While a failed payment is being retried, the subscription would remain `ACTIVE` until it succeeds
  or Discord's system determines the payment is not recoverable.
- A refund or chargeback during the current period would make the subscription `INACTIVE`.

### Status is not entitlement

**Subscription status should not be used to grant perks.** Use entitlements as the indication of
whether a user should have access to a specific SKU. The Subscription API and its events are intended
for reporting and lifecycle management purposes and should not be used as the source of truth for
whether a user has access to your premium features. The Subscription API is for reporting and
lifecycle management that happens outside the flow of a user's interaction with your app.

## Endpoints

### GET /skus/{sku.id}/subscriptions

**List SKU Subscriptions.** Returns all subscriptions containing the SKU, filtered by user. Returns a
list of Subscription objects.

`{sku.id}` resolves against the SKU object.

#### Query String Params

| Field | Type | Description | Default |
| --- | --- | --- | --- |
| before? | snowflake | List subscriptions before this ID | absent |
| after? | snowflake | List subscriptions after this ID | absent |
| limit? | integer | Number of results to return (1-100) | 50 |
| user_id? | snowflake | User ID for which to return subscriptions. Required except for OAuth queries. | absent |

`limit` defaults to **50** here — note this differs from List Entitlements, which defaults to 100.

`user_id` is marked optional by its `?` but its description makes it **required except for OAuth
queries**: a bot token request must supply it.

The upstream page documents no error responses and shows no example response body for this endpoint.

### GET /skus/{sku.id}/subscriptions/{subscription.id}

**Get SKU Subscription.** Get a subscription by its ID. Returns a Subscription object.

`{sku.id}` resolves against the SKU object, `{subscription.id}` against the Subscription object. No
query or JSON parameters, no error responses and no example body are documented.

There is no documented endpoint for creating, cancelling or modifying a subscription over HTTP. Users
cancel, resume, upgrade and downgrade from their own Subscription settings or your Store page.

## Subscription Gateway events

Discord will emit gateway events when a subscription is created, updated, and "very rarely, deleted".
The monetization pages name only two of the three explicitly — `SUBSCRIPTION_CREATE` and
`SUBSCRIPTION_UPDATE`. The delete event's exact event name is **not stated** on any monetization page;
confirm it against the Gateway events reference before handling it.

Because entitlements are granted indefinitely and don't update on renewal or cancellation, you can
use subscription events to track the lifecycle of a subscription.

This is not a complete list of when events may occur. Use the presence of an entitlement to determine
whether a user has access to your premium features.

| Event Name | Subscription Behavior | Updated Fields |
| --- | --- | --- |
| `SUBSCRIPTION_CREATE` | Subscription is created | `status` is either `0 (active)` if an entitlement has been granted or `1 (inactive)` if an entitlement has not yet been granted |
| `SUBSCRIPTION_UPDATE` | Subscription is granted an entitlement | `status` is `0 (active)` |
| `SUBSCRIPTION_UPDATE` | Subscription is renewed | `current_period_start`, `current_period_end` timestamps updated |
| `SUBSCRIPTION_UPDATE` | Subscription is upgraded or downgraded | `sku_ids`, `entitlement_ids`, `renewal_sku_ids` may be updated |
| `SUBSCRIPTION_UPDATE` | Subscription is canceled | `canceled_at` timestamp updated, `status` is `2 (ending)` |
| `SUBSCRIPTION_UPDATE` | Subscription ends | `status` is `1 (inactive)`, this event is processed asynchronously and will not be immediate |
| `SUBSCRIPTION_UPDATE` | Subscription is resumed/uncanceled by user | `status` is `0 (active)` |

A subscription delete event is stated to exist ("very rarely") but the monetization pages describe no
scenario that produces it, name no event constant for it, and list no updated fields for it.

## Lifecycle event tables

The exact event sequences per user action, verbatim from the Implementing App Subscriptions page.

### Starting a new subscription

| Event | Event Trigger |
| --- | --- |
| `SUBSCRIPTION_CREATE` | when the subscription is initially created. `status` is `0 (active)` if the entitlement has been granted or `1 (inactive)` if the entitlement has not yet been granted. |
| `ENTITLEMENT_CREATE` | when the user is granted an entitlement for the new subscription |
| `SUBSCRIPTION_UPDATE` | when the subscription is updated with the `entitlement_ids`, `renewal_sku_ids`, and `status` (`0 (active)`) |

### Cancelling an existing subscription

Users can cancel their subscription at any time from their Subscription settings.

| Event | Event Trigger |
| --- | --- |
| `SUBSCRIPTION_UPDATE` | when the subscription is updated to end with a `status` of `2 (ending)` and `canceled_at` is set to the timestamp the user canceled |

The user's subscription and entitlement are still valid until the subscription `current_period_end`
is reached.

If the subscription is not resumed before `current_period_end`, it will end and you will receive:

| Event | Event Trigger |
| --- | --- |
| `ENTITLEMENT_UPDATE` | when the current entitlement ends. `ends_at` gets updated with a timestamp |
| `SUBSCRIPTION_UPDATE` | when the subscription is updated with the `status` of `1 (inactive)` |

### Resuming a cancelled subscription

Users can resume their subscription at any time before the `current_period_end` is reached in their
Subscription settings.

| Event | Event Trigger |
| --- | --- |
| `SUBSCRIPTION_UPDATE` | when the subscription is set to continue with a `status` of `0 (active)` and `canceled_at` is set to null |

### Upgrading an existing subscription

If a user is on a lower tier subscription and upgrades to a subscription tier that is the same price
or higher, the user is charged the difference in price between the two subscriptions and the
subscription period resets at the time of upgrading.

When the subscription is upgraded, the current entitlement for the lower tier will end immediately
and you will receive:

| Event | Event Trigger |
| --- | --- |
| `ENTITLEMENT_UPDATE` | when the current entitlement ends. `ends_at` gets updated with a timestamp |
| `ENTITLEMENT_CREATE` | when a new entitlement is created for the upgrade subscription SKU |
| `SUBSCRIPTION_UPDATE` | when the subscription is updated with the new `entitlement_ids`, `sku_ids`, `current_period_start`, `current_period_end` |

### Downgrading an existing subscription

If a user is on a higher tier subscription and downgrades to a lower tier subscription, the user is
not charged immediately because the price is lower than what was already paid.

The user has already paid for their current plan until `subscription.current_period_end` so their
current plan will be valid until then and you will receive:

| Event | Event Trigger |
| --- | --- |
| `SUBSCRIPTION_UPDATE` | when the subscription is updated to reflect the renewal SKU ID in `subscription.renewal_sku_ids` |

Once the user's current subscription expires on `subscription.current_period_end`, you will receive:

| Event | Event Trigger |
| --- | --- |
| `ENTITLEMENT_UPDATE` | when the current entitlement ends. `ends_at` gets updated with a timestamp |
| `ENTITLEMENT_CREATE` | when a new entitlement is created for the downgraded subscription SKU |
| `SUBSCRIPTION_UPDATE` | when the subscription is updated with the new `entitlement_ids`, `sku_ids`, `current_period_start`, `current_period_end` |

Note the asymmetry between upgrade and downgrade: an upgrade ends the old entitlement **immediately**
and resets the period; a downgrade changes nothing until `current_period_end`, and only signals its
intent through `renewal_sku_ids`.

Users can upgrade or downgrade at any time from your Store page or their App Subscription settings.
To offer tiers, create multiple subscription SKUs.

## Source

Discord Developer Documentation:

- `https://docs.discord.com/developers/resources/subscription`
- `https://docs.discord.com/developers/monetization/implementing-app-subscriptions`

Retrieved 2026-08-26.
