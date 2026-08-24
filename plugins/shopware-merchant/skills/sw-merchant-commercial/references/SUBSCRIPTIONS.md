# Shopware Subscriptions

Recurring orders with configurable intervals. A commercial feature, available from the Beyond plan
and part of the Shopware Commercial extension, from Shopware 6.5.4.0 onwards.

## Contents

- [Overview](#overview)
- [Configuration and setup](#configuration-and-setup)
- [Plans](#plans)
- [Intervals](#intervals)
- [Settings and mixed carts](#settings-and-mixed-carts)
- [Storefront experience](#storefront-experience)
- [Payment methods](#payment-methods)
- [Customer self-service](#customer-self-service)
- [Cancellation behaviour](#cancellation-behaviour)
- [Admin management](#admin-management)
- [Rule and Flow Builder](#rule-and-flow-builder)

## Overview

Subscriptions let a merchant offer recurring orders on a configurable interval.

| | |
|---|---|
| Availability | the Beyond plan, as part of the Shopware Commercial extension |
| Minimum version | 6.5.4.0 |
| Mixed carts | 6.7.4.0 and later |

A **mixed cart** combines one-off products and subscription items in a single order. The system
distinguishes the one-off deliveries from the recurring ones by itself, and applies discounts and
shipping costs correctly to both.

## Configuration and setup

The subscriptions live under **Settings > Commerce > Subscriptions**.

## Plans

A plan is the base configuration of a subscription. In the **Plans** tab you add, edit and delete
them.

### General

| Field | What it does |
|---|---|
| Name | names the subscription |
| Active | the switch that activates or deactivates it |
| Use a different name in the Storefront | shows the **Label** field instead of the name, for the front end |
| Description | free text explaining the subscription to the customer |

### Availability

An availability rule is configured under **Availability**. Subscriptions are fully compatible with
the Rule Builder, so a plan can be limited to a customer group, a sales channel, or any other
condition the rule system can express.

### Intervals on a plan

**Intervals** defines which intervals the end customer is finally offered.

| Field | What it does |
|---|---|
| Minimum term | the minimum use of the subscription, e.g. 24 months on a monthly interval |
| Discount (%) | a discount applied when the product is bought as a subscription, making it more attractive |

### Products

The **Products** tab adds products to the subscription. It works in both directions: a subscription
can equally be assigned to a product from the product's own settings. **Add product** opens a modal
where products are picked by checkbox, identified by product name and product number.

## Intervals

The **Intervals** tab manages intervals themselves: **Add interval** creates one, and the
three-dot menu edits or deletes an existing one.

| Field | What it does |
|---|---|
| Name | names the interval |
| Active | activates or deactivates it |
| Availability | an availability rule, as for a plan |
| Frequency | how often it recurs, e.g. every week or every second week |
| Time interval | the unit: days, weeks or months |

The preview shows the next dates the subscription would fall on if bought now. **View more**
extends that list beyond the first three.

### Advanced settings

Where a regular frequency is not specific enough, **Advanced settings** adds, on top of the
frequency, the weekdays, the days in the month and the months in the year. The preview covers this
configuration too.

## Settings and mixed carts

From 6.7.4.0, the subscription settings decide whether mixed carts are allowed. With **Activate
mixed carts** enabled, a customer combines subscription products and one-off purchases in a single
order; disabled, subscription products have to be bought on their own.

## Storefront experience

- The subscription choice appears beside the **Add to cart** option.
- Several plans are offered as a radio-button selection.
- Choosing a plan changes the button to **Subscribe now**.
- Subscriptions go through a checkout process of their own.

With a mixed cart, the order overview shows the price components of both parts separately.

## Payment methods

| Method | Requirement |
|---|---|
| Credit card | recurring payments supported by the provider |
| SEPA direct debit | recurring debits supported by the provider |
| PayPal | vaulting enabled |

**Not every payment provider supports recurring debits, and PayPal vaulting has to be enabled
separately.** The Rule Builder can restrict or exclude specific payment methods for subscription
purchases, which matters where a method is unsuitable for recurring orders.

## Customer self-service

A customer manages their own subscriptions in the storefront account:

| Action | What it does |
|---|---|
| Overview | the dashboard listing every active subscription |
| Pause | a single pause, for one cycle |
| Cancel | ends the subscription |
| Status | the current state of each subscription |

## Cancellation behaviour

The system distinguishes two cases.

**With a minimum term** — the status becomes *marked for cancellation* and stays there until the
term expires. Orders continue automatically until the end of the term, and the cancellation takes
effect only afterwards.

**Without a minimum term** — the status becomes *marked for cancellation* at once. The last order
is still processed, then the subscription ends.

## Admin management

In the admin, a merchant can:

- view and filter every customer subscription
- change a status by hand
- pause or cancel a subscription on the customer's behalf
- read the log of every subscription action

A mixed order is shown in full in the admin. The upper section carries the order information —
customer details, status and total — for the **first delivery**. Under **Items**, subscription items
are marked with a subscription number and one-off products are not; a discount such as the
subscription discount is assigned to its subscription automatically. The subscription number links
straight to that subscription.

**Path:** Orders → Subscriptions, or Settings → Subscriptions.

## Rule and Flow Builder

Subscriptions work with both builders, so rules and automations can target them specifically.

**Rule Builder** — availability rules for plans (a customer group, for instance), and restrictions
on which payment methods a subscription purchase may use.

**Flow Builder** — dedicated triggers cover the subscription lifecycle: created, paused, cancelled.
Typical automations send a reminder email or delay an action before a term expires, for example an
email three days before the next delivery.

## Source

Distilled from
[docs.shopware.com/en/shopware-6-en/settings/shop/subscriptions](https://docs.shopware.com/en/shopware-6-en/settings/shop/subscriptions),
retrieved 2026-08-21.
