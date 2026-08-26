---
name: discord-monetization
description: "Discord app monetization: SKUs, entitlements, subscriptions and in-app purchases. Use when the request names Discord monetization, a Discord SKU or an entitlement."
---

# Discord Monetization

Charge for app features inside Discord: recurring user and guild subscriptions, durable and
consumable one-time purchases, in-app purchases in Activities, and Social Commerce Game Shops.
Discord handles billing, fraud detection and receipts; your app grants access.

App monetization applies to **bots** and **Activities**.

## The model: SKU to entitlement to subscription

- **SKU** — one premium offering. Types: `DURABLE` (2), `CONSUMABLE` (3), `SUBSCRIPTION` (5),
  `SUBSCRIPTION_GROUP` (6). Integrate against `type: 5` for subscriptions; the group SKU is
  auto-created and unused. Flags distinguish `GUILD_SUBSCRIPTION` (`1 << 7`) from `USER_SUBSCRIPTION`
  (`1 << 8`).
- **Entitlement** — proof that a user or guild has access. **The single source of truth for granting
  a perk.**
- **Subscription** — the recurring payment agreement. Statuses `ACTIVE` (0), `INACTIVE` (1),
  `ENDING` (2).

Three gates that decide correct implementations:

1. **Never grant a perk from subscription status.** Check for an entitlement. Subscription status and
   its events exist for reporting and lifecycle management, and a subscription can be `ACTIVE`
   outside its period or `INACTIVE` inside it.
2. **Consume every consumable entitlement.** A user holds at most one unconsumed entitlement per
   consumable SKU and cannot repurchase until you call the consume endpoint.
3. **Test entitlements are for subscriptions only.** For one-time purchases use Application Test
   Mode instead; those purchases carry `type: 4` (`TEST_MODE_PURCHASE`).

Two asymmetries the docs are explicit about: cancellation and renewal emit **no** entitlement event
(only `SUBSCRIPTION_UPDATE`), and an upgrade ends the old entitlement immediately while a downgrade
changes nothing until `current_period_end`.

## Endpoints at a glance

| Method | Path |
| --- | --- |
| GET | `/applications/{application.id}/skus` |
| GET | `/applications/{application.id}/entitlements` |
| GET | `/applications/{application.id}/entitlements/{entitlement.id}` |
| POST | `/applications/{application.id}/entitlements/{entitlement.id}/consume` |
| POST | `/applications/{application.id}/entitlements` (create test entitlement) |
| DELETE | `/applications/{application.id}/entitlements/{entitlement.id}` (delete test entitlement) |
| GET | `/skus/{sku.id}/subscriptions` |
| GET | `/skus/{sku.id}/subscriptions/{subscription.id}` |

There is no HTTP endpoint for creating, editing, publishing or deleting a SKU: that is Developer
Portal only.

## Reference map

- **[SKU.md](references/SKU.md)**: the SKU object, all 6 documented fields, all 4 SKU types with numeric values,
  all 3 flags with their shifts, List SKUs, plus the 7 payload keys the upstream leaves undocumented.
- **[ENTITLEMENT.md](references/ENTITLEMENT.md)**: the Entitlement object with all 10 fields and their
  optionality, all 8 entitlement types, all 5 endpoints with every query and JSON parameter, and the
  three entitlement Gateway events.
- **[SUBSCRIPTION.md](references/SUBSCRIPTION.md)**: the Subscription object with all 10 fields, the 3 statuses,
  both endpoints, the subscription event table and the full per-scenario lifecycle event sequences
  for start, cancel, resume, upgrade and downgrade.
- **[IMPLEMENTING.md](references/IMPLEMENTING.md)**: the four how-to pages end to end — app subscriptions,
  one-time purchases, IAP for Activities with `getSkus()`/`getEntitlements()`/`startPurchase()` and
  the trust-but-verify rule, and managing SKUs (the 50-SKU limit, character limits, publishing,
  premium button code, Store URL schemes).
- **[ENABLING-AND-OVERVIEW.md](references/ENABLING-AND-OVERVIEW.md)**: the 6 setup steps, the full eligibility
  checklist, Stripe payouts and the $100 threshold, the region restriction, the platform Premium Apps
  page, and Social Commerce & Game Shops.

## Related

Call the Skill tool with "discord-gateway" for the `ENTITLEMENT_CREATE`, `ENTITLEMENT_UPDATE`,
`ENTITLEMENT_DELETE`, `SUBSCRIPTION_CREATE` and `SUBSCRIPTION_UPDATE` dispatch mechanics and intents,
and for the name of the rarely emitted subscription delete event.
Call the Skill tool with "discord-interactions" for the `entitlements` field on the interaction
payload and for the premium button component.
Call the Skill tool with "discord-activities" or "discord-social-sdk" for the Embedded App SDK
commands `getSkus()`, `getEntitlements()`, `startPurchase()` and `PriceUtils`.
Call the Skill tool with "discord-rest" for authentication, rate limits and the boolean query string
convention these endpoints use.
Call the Skill tool with "discord-oauth2" for the private scope that exposes `subscription.country`.
Call the Skill tool with "discord-platform" for teams, app verification and the App Directory.
Call the Skill tool with "discord-bots" for slash commands, which the eligibility checklist requires.

## Source

Distilled from the Discord Developer Documentation, retrieved 2026-08-26:

- `https://docs.discord.com/developers/resources/sku`
- `https://docs.discord.com/developers/resources/entitlement`
- `https://docs.discord.com/developers/resources/subscription`
- `https://docs.discord.com/developers/monetization/overview`
- `https://docs.discord.com/developers/monetization/enabling-monetization`
- `https://docs.discord.com/developers/monetization/managing-skus`
- `https://docs.discord.com/developers/monetization/implementing-app-subscriptions`
- `https://docs.discord.com/developers/monetization/implementing-one-time-purchases`
- `https://docs.discord.com/developers/monetization/implementing-iap-for-activities`
- `https://docs.discord.com/developers/platform/app-monetization`
- `https://docs.discord.com/developers/social-commerce/overview`
