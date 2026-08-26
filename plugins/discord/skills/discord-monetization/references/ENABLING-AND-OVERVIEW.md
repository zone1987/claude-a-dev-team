# Enabling Discord Monetization, Overview and Social Commerce

Eligibility, team requirements, payouts, the platform-level Premium Apps positioning, and Social
Commerce & Game Shops. Retrieved 2026-08-26.

## Table of contents

- [Enabling Monetization](#enabling-monetization)
  - [Steps to enable monetization](#steps-to-enable-monetization)
  - [Step 1. Set up your developer team and app](#step-1-set-up-your-developer-team-and-app)
  - [Step 2. Complete the eligibility checklist](#step-2-complete-the-eligibility-checklist)
  - [Step 3. Set up team payouts](#step-3-set-up-team-payouts)
  - [Step 4. Create your premium offering](#step-4-create-your-premium-offering)
  - [Step 5. Implement monetization in your app](#step-5-implement-monetization-in-your-app)
  - [Step 6. Start offering your premium features](#step-6-start-offering-your-premium-features)
- [Monetization Overview](#monetization-overview)
  - [Components of a premium app](#components-of-a-premium-app)
  - [Types of SKUs](#types-of-skus)
- [Premium Apps & Activities (platform page)](#premium-apps--activities-platform-page)
- [Social Commerce & Game Shops](#social-commerce--game-shops)
- [Source](#source)

---

## Enabling Monetization

Before you can add monetization to your app, you must ensure that your app and team meet the
eligibility criteria.

### Steps to enable monetization

1. Set up your developer team and app to be eligible for monetization
2. Complete the eligibility criteria for monetization
3. Set up developer team payouts to get paid
4. Create your premium offering
5. Implement monetization in your app
6. Start offering your premium features

Once these are complete, you can create SKUs to represent your premium offerings and add support for
your premium offering in your app.

### Step 1. Set up your developer team and app

Before monetization can be enabled, you will need:

- A **team** in the developer portal. If you don't have one, you can create one on the Teams page:
  `https://discord.com/developers/teams`
- A **verified app** that is *owned by that team*. Verification guide:
  `https://support-dev.discord.com/hc/en-us/articles/23926564536471-How-Do-I-Get-My-App-Verified`
- Your app and team must be eligible for monetization. See the eligibility checklist below.

### Step 2. Complete the eligibility checklist

Before you can start creating SKUs and offering payments in your app, your app and team must be
eligible for monetization. When a team owner enables monetization, they'll be taken through a series
of steps and checks to ensure the following criteria are met:

**Eligibility Checklist**

- App must be **verified**
- App belongs to a **developer team**
- Team owner must be at least **18 years old**
- Team must have **verified emails and 2FA** set up
- App uses **slash commands**, or has been approved for the privileged `Message Content` intent
- App has a link to your **Terms of Service**
  - This document is an agreement between you and users governing the use of your app.
- App has a link to your **Privacy Policy**
  - This document should clearly and accurately describe to users of your app the user data you
    collect and how you use and share such data with Discord and third parties, consistent with the
    Developer Terms of Service and Developer Policy.
- App must **not contain any harmful or bad language** in the name, description, commands, or role
  connection metadata.
- **Payouts must be set up** with a valid payment method
- Agreement to the **Monetization Terms**
  (`https://support.discord.com/hc/articles/5330075836311`) and the **Discord Developer Policy**
  (`https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy`).

### Step 3. Set up team payouts

Discord processes **all payouts through Stripe**, so part of setting up payouts will go through
Stripe's onboarding flow.

- **Only the owner of the team** can enable payout settings for the team.
- Once your app has made its **first $100** it will become eligible for payout.
- A **review** will be conducted and if everything looks good, your team will begin to receive
  payouts.

**If you are based in the United States, European Union, or United Kingdom**

- Click on your team on the Teams page (`https://discord.com/developers/teams`).
- Select **Payout Settings**.
  - If you do not see **Payout Settings**, you are not the owner of the team. Only the owner of the
    team can enable payout settings for the team.
- Complete the onboarding flow through Stripe.

**If you are based outside of the United States, European Union, or United Kingdom**

Premium Apps is **not currently available** outside of these regions. These features will be made
available to more regions soon.

For more information, read the Premium Apps Payouts Help Center article:
`https://support-dev.discord.com/hc/articles/17299902720919`

The page states no fee percentage, no revenue share split, no payout schedule and no minimum payout
beyond the $100 eligibility threshold. Those numbers are not documented on any of the monetization
pages; the Monetization Terms and the Payouts help article are the upstream's pointers for them.

### Step 4. Create your premium offering

You are now ready to start setting up your SKUs and offering premium features in your app. See
`IMPLEMENTING.md` → Managing SKUs → Creating a SKU, to create one-time purchases and subscriptions
for your app.

### Step 5. Implement monetization in your app

Now that you've set up your app for monetization, you can start adding code to support your premium
features. Discord provides guides for these monetization strategies, both distilled in
`IMPLEMENTING.md`:

- **Implementing App Subscriptions** — how to start and manage recurring subscriptions within your
  app.
- **Implementing One-Time Purchases** — how to implement one-time purchases in your app.

### Step 6. Start offering your premium features

Once your app is set up for monetization you can start earning money from your app and providing
premium features to your users. Three ways to let users purchase:

- Link to your **Store** page
- Link to a **specific SKU**
- Include a **premium styled button** in Message Components

All three are documented in `IMPLEMENTING.md` → Managing SKUs.

---

## Monetization Overview

Add subscriptions and one-time purchases to your app using Discord's built-in checkout and payment
flow.

**App Monetization applies to Bots and Activities.**

### Components of a premium app

To integrate a premium feature into your application, there are three primary components of the
Monetization API:

- **SKUs** represent specific items or subscription options your app offers. Each SKU is a unique
  offering. (Full reference: `SKU.md`.)
- **Entitlements** indicate whether a user has access to a specific premium offering or SKU. (Full
  reference: `ENTITLEMENT.md`.)
- **Subscriptions** represent an ongoing agreement where a user commits to paying for an entitlement
  on a recurring basis until canceled. (Full reference: `SUBSCRIPTION.md`.)

### Types of SKUs

There are two types of SKUs that you can create for your app.

**One-Time Purchase SKUs.** A one-time purchase SKU represents a single item or feature that a user
can purchase once. Developers can offer two types of one-time purchases:

- **Durable items**: Items that a user can purchase once and keep forever. For example, a user might
  purchase a "premium" upgrade that unlocks premium features in an app.
- **Consumable items**: Items that a user can purchase once and use up. For example, a user might
  purchase a "boost" item that gives them a temporary boost in an app.

**Subscription SKUs.** A subscription SKU represents a recurring purchase that a user can subscribe
to for a set period of time. Developers can offer two types of subscriptions:

- **User subscriptions**: A user subscribes to a SKU for themselves. In this case, only the
  purchasing user is considered entitled to the SKU.
- **Guild subscriptions**: A user subscribes to a SKU for their guild. All members of that guild are
  considered entitled to the SKU.

*(Hero image caption: "Monetizing Your Discord App".)*

---

## Premium Apps & Activities (platform page)

Add subscriptions and one-time purchases to your Discord app with Premium Apps.

App Monetization applies to **Bots** and **Activities**. If you're building a game integration, see
[Social Commerce & Game Shops](#social-commerce--game-shops) for how to monetize your game with
Discord.

The Premium Apps features let you charge for your app's features **directly within Discord**, using
Discord's built-in payment and checkout flow. Users never leave the platform to subscribe or make a
purchase, which reduces friction and keeps the experience native. **Discord handles billing, fraud
detection, and receipts, while you handle granting access to your premium features.**

You can offer two types of monetization:

- **Recurring monthly subscriptions** with the option to offer to individuals or whole servers
- **One-Time purchases** with the option to offer durable upgrades or consumable items

Both types integrate through the same **SKU** and **Entitlement** APIs, so your app checks whether a
user is entitled to a feature before granting access.

**Monetized apps also get additional surface area on the App Directory**, including a store page
where users can browse and purchase your offerings **without having to install your app first**.

The page links onward to two guides: the Monetization Overview ("Full guide to SKUs, Entitlements,
Subscriptions, and the App Directory store page") and Enabling Monetization ("Step-by-step setup for
enabling payments and creating your first SKU").

*(Hero image caption: "Monetizing Your Discord App Hero Image".)*

---

## Social Commerce & Game Shops

Sell in-game items, cosmetics, and bundles directly within Discord through a user-facing Game Shop
that lives directly in your server.

Discord Social Commerce brings your game's store directly into Discord, where your players already
are. Instead of sending players to an external store, Game Shops let them browse items, make
purchases, and send gifts to friends without ever leaving Discord.

### Discord Game Shops

Your Game Shop lives inside your Discord server and surfaces items across Discord: on player
profiles, in DMs, and in voice chats. Players discover items organically through social activity, not
just because they went looking for a store.

When a player makes a purchase, **Discord handles payment processing and creates an entitlement
representing that the player is owed the item.** Your backend listens for the **fulfillment webhook**,
checks that their Discord account is linked to their game account, and grants the item.

### Gifting & Wishlists

Game Shops also unlock a category of purchaser that traditional in-game stores can't reach: people who
don't play your game but want to buy something for someone who does.

A player's friends, family members, or community followers can browse your Game Shop, pick an item off
a wishlist, and send it as a gift. **They don't need to own or ever launch your game to do it.** For
you as a developer, every player in your Discord community becomes a potential storefront for your
items, and the people in their social circles become a new pool of buyers.

Wishlists make this loop even tighter. Players pin the items they want, making it easy for gift-givers
to find something meaningful rather than guessing. Birthdays, game launches, seasonal events: any
moment that drives gifting behavior on Discord becomes a revenue opportunity for your shop.

### Social Commerce APIs

Social Commerce is backed by a set of APIs that give you full control over your catalog, purchases,
and fulfillment:

- **SKU & Storefront Management**: Define your catalog of items including cosmetics, bundles, and
  consumables. Set pricing, availability, and metadata through the API so your store stays in sync
  with your game.
- **Entitlements**: Query and manage what players own. When a purchase is made, Discord creates an
  entitlement your backend can verify and act on.
- **Fulfillment**: Receive webhook events the moment a purchase completes. Grant the item in your
  game, then **mark the entitlement as fulfilled via the API** to close the loop.

Together, these APIs let you build a fully automated purchase-to-fulfillment pipeline with Discord
handling the payment surface and your backend handling item delivery.

**The overview page names these three API groups but documents no endpoint, no object, no field, no
webhook event name and no payload for any of them.** There is no public reference for the Social
Commerce SKU & Storefront Management API, the fulfillment webhook, or the "mark fulfilled" call. Do
not assume the entitlement endpoints in `ENTITLEMENT.md` are the same surface — the page does not say
they are.

### Get access to Social Commerce

**Social Commerce is currently in early access.** If you're interested in bringing your Game Shop to
Discord, get in touch and Discord will follow up as they expand access. The interest form is at
`https://discord.com/developers/commerce-contact-us` — "Request Access to Social Commerce: Fill out
our interest form and we'll reach out when we're ready to onboard new studios."

*(Hero image caption: "Discord Social Commerce Hero Image".)*

## Source

Discord Developer Documentation:

- `https://docs.discord.com/developers/monetization/enabling-monetization`
- `https://docs.discord.com/developers/monetization/overview`
- `https://docs.discord.com/developers/platform/app-monetization`
- `https://docs.discord.com/developers/social-commerce/overview`

Retrieved 2026-08-26.
