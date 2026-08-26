# Implementing Discord Monetization

The four Discord monetization how-to pages, end to end: app subscriptions, one-time purchases,
in-app purchases for Activities, and managing SKUs in the Developer Portal. Retrieved 2026-08-26.

## Table of contents

- [Implementing App Subscriptions](#implementing-app-subscriptions)
  - [Types of subscriptions](#types-of-subscriptions)
  - [How app subscriptions work](#how-app-subscriptions-work)
  - [Working with entitlements](#working-with-entitlements)
  - [Prompting users to subscribe](#prompting-users-to-subscribe)
  - [Supporting subscriptions](#supporting-subscriptions)
  - [Supporting upgrades and downgrades](#supporting-upgrades-and-downgrades)
  - [Using the Subscription API](#using-the-subscription-api)
  - [Testing your app subscription implementation](#testing-your-app-subscription-implementation)
- [Implementing One-Time Purchases](#implementing-one-time-purchases)
  - [Types of one-time purchases](#types-of-one-time-purchases)
  - [How one-time purchases work](#how-one-time-purchases-work)
  - [Working with entitlements for one-time purchases](#working-with-entitlements-for-one-time-purchases)
  - [One-time purchase considerations](#one-time-purchase-considerations)
  - [Prompting users to purchase an item](#prompting-users-to-purchase-an-item)
  - [Testing one-time purchases: Application Test Mode](#testing-one-time-purchases-application-test-mode)
- [Implementing In-App Purchases for Activities](#implementing-in-app-purchases-for-activities)
  - [Key concepts](#key-concepts)
  - [Publishing SKUs for Activities](#publishing-skus-for-activities)
  - [Building a storefront](#building-a-storefront)
  - [Working with entitlements in an Activity](#working-with-entitlements-in-an-activity)
  - [Initiating purchases](#initiating-purchases)
  - [Data security considerations](#data-security-considerations)
  - [Testing your in-app purchases](#testing-your-in-app-purchases)
  - [Example implementation](#example-implementation)
- [Managing SKUs](#managing-skus)
  - [Creating a SKU](#creating-a-sku)
  - [SKU limitations](#sku-limitations)
  - [Customizing your SKUs](#customizing-your-skus)
  - [Pricing your SKUs](#pricing-your-skus)
  - [Publishing and unpublishing SKUs](#publishing-and-unpublishing-skus)
  - [Editing a published SKU](#editing-a-published-sku)
  - [Viewing your Store page](#viewing-your-store-page)
  - [Linking to a specific SKU](#linking-to-a-specific-sku)
  - [Linking to your Store](#linking-to-your-store)
  - [Responding with a premium button](#responding-with-a-premium-button)
- [Source](#source)

---

## Implementing App Subscriptions

Charge users for premium app functionality with a recurring user or guild subscription.

- Before you can add an app subscription to your app, you must enable monetization for your app
  (see `ENABLING-AND-OVERVIEW.md`).
- Once you've confirmed eligibility for your app and team, you will be able to set up a SKU
  (stock-keeping unit) to represent your subscription.

### Types of subscriptions

When creating subscriptions, you will need to choose between user or guild subscriptions:

- **User Subscriptions**: Offers premium features to an individual user across any server where your
  app is installed.
- **Guild Subscriptions**: Provides premium benefits to all members within a specific server.

### How app subscriptions work

- When a user purchases your subscription SKU, Discord creates an Entitlement for the user (or guild)
  and that specific Subscription SKU.
- You will receive an `ENTITLEMENT_CREATE` event via the Gateway.
- This entitlement will be available via the `LIST Entitlements` API endpoint.
- This entitlement will be available on `Interaction Payloads` initiated from the entitled user or
  users in a guild (for guild subscriptions).
- This subscription will be available via the `LIST Subscriptions` API endpoint.
- This entitlement is granted indefinitely until the user decides to cancel their subscription.
  `ends_at` will be null.
- **When a user cancels their subscription, your app will not receive any entitlement events.**
- When a subscription ends, the entitlement to the subscription will end. Developers will receive an
  `ENTITLEMENT_UPDATE` event with an `ends_at` timestamp indicating when the subscription ended.

The subscription-event lifecycle table and the per-scenario event sequences live in
`SUBSCRIPTION.md`.

### Working with entitlements

When a user purchases a subscription, an entitlement is created. Entitlements represent the user's
access to your app's premium features. Depending on your app's features, use a combination of Gateway
events, the Entitlement HTTP API, and interaction payloads to keep track of user and guild
entitlements and grant features to users who are subscribed to your app.

**With Gateway events.** For subscription SKUs, you will receive the following entitlement events:

| Event | Description |
| --- | --- |
| `ENTITLEMENT_CREATE` | When a user is granted an entitlement to your app's subscription SKU |
| `ENTITLEMENT_UPDATE` | When an entitlement to a subscription SKU ends |
| `ENTITLEMENT_DELETE` | When Discord refunds a subscription, removes an entitlement, or when a developer deletes a Test Entitlement |

**With the HTTP API.** For apps requiring background processing or not solely reliant on
interactions, keeping track of entitlements is essential. Use List Entitlements to list active and
expired entitlements. Filter by a specific user or guild with `?user_id=XYZ` or `?guild_id=XYZ`. For
example, you might keep track of entitlements in a database and check if a user still has access to a
specific SKU before performing a cron job or other task.

**On interaction payloads.** Entitlements are available on the `entitlements` field of the
`Interaction Payload` when a user interacts with your app. Use this field to determine if the user or
guild is subscribed to your app.

**With the Embedded App SDK.** When building an Activity, you can also access a user's entitlements
with `getEntitlements()`.

### Prompting users to subscribe

Three routes:

1. **Responding with a premium button** — prompt users to subscribe when they attempt to use a
   premium feature without a subscription. Send a message with a button with a premium style and a
   `sku_id` that allows the user to upgrade to your premium offering. Code below under
   [Responding with a premium button](#responding-with-a-premium-button).
2. **Starting a purchase from an Activity** — with the Embedded App SDK, launch the purchase flow for
   a specific SKU using `startPurchase()`.
3. **Purchasing from the Store page** — users can start, upgrade, or downgrade their subscription
   from your app's Store page. Link directly to it with the Application Directory Store URL scheme.

### Supporting subscriptions

To support subscriptions in your app, create a subscription SKU and handle these scenarios: starting
a new subscription, cancelling an existing subscription, and resuming a cancelled subscription. The
exact event sequences for each are in `SUBSCRIPTION.md`.

### Supporting upgrades and downgrades

If you offer multiple subscription tiers, users can upgrade or downgrade at any time from your Store
page or their App Subscription settings. To create multiple tiers, create multiple subscription SKUs.

- **Upgrade** (same price or higher): the user is charged the difference in price between the two
  subscriptions and the subscription period resets at the time of upgrading. The current entitlement
  for the lower tier ends immediately.
- **Downgrade**: the user is not charged immediately because the price is lower than what was already
  paid. The current plan stays valid until `subscription.current_period_end`.

Event tables for both: `SUBSCRIPTION.md`.

### Using the Subscription API

Entitlements should be considered the source of truth for a user's access to a specific SKU. The
Subscription API is intended for reporting and lifecycle management purposes that happen outside the
flow of a user's interaction with your app.

The Subscription API lets you list subscriptions by user for reporting purposes and check on the
status of subscriptions without having to access entitlements directly:

- **List SKU Subscriptions**: list all subscriptions for a specific SKU in your app.
- **Get SKU Subscription**: get a specific subscription in your app.
- **Subscription Gateway events**: Discord emits gateway events when a subscription is created,
  updated, and very rarely, deleted.

### Testing your app subscription implementation

**Using Test Entitlements.** Test your implementation by creating and deleting test entitlements.
These entitlements let you test your premium offering in both a subscribed and unsubscribed state as
a user or guild. This method will **not** let you test out the full payment flow in Discord but will
let you test your app's behavior when a user is subscribed or unsubscribed.

Test Entitlements do not have a `starts_at` or `ends_at` field as they are valid until they are
deleted.

**Using Live Entitlements.** To test the full payment flow, interact with your Store page or a
premium styled button. **Any team members associated with your app will automatically see a 100%
discount on the price of the subscription**, allowing you to purchase without the use of a live
payment method.

After checkout, you will have a live subscription. This subscription will renew until canceled and
can be used in testing subscription renewals in your app. If you cancel this subscription, it will
remain an active entitlement until the end of the subscription billing period, represented by the
`current_period_end` field on the Subscription.

You can only delete entitlements created using the create test entitlement endpoint. If you need to
toggle access to your premium features during your development process, it is best to use Test
Entitlements.

---

## Implementing One-Time Purchases

One-time purchases enable you to charge your users for premium functionality with in-app items.

- Before you can add one-time purchases to your app, you must enable monetization for your app.
- Once you've confirmed eligibility for your app and team, you will be able to set up a SKU
  (stock-keeping unit) to represent your one-time purchases.

### Types of one-time purchases

- **Durable Items**: A one-time purchase that is permanent and is not subject to either renewal or
  consumption, such as lifetime access to an app's premium features.
- **Consumable Items**: A one-time, non-renewable purchase that provides access, such as a temporary
  power-up or boost in a game.

### How one-time purchases work

**For Durable SKUs**

- When a user purchases your durable SKU, Discord creates an Entitlement for the purchasing user and
  that specific SKU.
- You will receive an `ENTITLEMENT_CREATE` event via the Gateway.
- This entitlement is now available via the `LIST Entitlements` API endpoint.
- This entitlement will be available on `Interaction Payloads` initiated from the entitled user.

**For Consumable SKUs**

- When a user purchases your consumable SKU, Discord creates an Entitlement for the purchasing user
  and that specific SKU.
- You will receive an `ENTITLEMENT_CREATE` event via the Gateway.
- This entitlement is now available via the `LIST Entitlements` API endpoint.
- This entitlement will be available on `Interaction Payloads` initiated from the entitled user or
  users in a guild (for guild subscriptions).
- **Users cannot repurchase this SKU until you consume the entitlement** using the Consume
  Entitlement API endpoint.
  - In Application Test Mode, repeated purchases are permitted without consumption for developer
    convenience.
- When you receive an `ENTITLEMENT_CREATE` event for a consumable SKU, you should process the item
  purchase in your app and consume the entitlement as soon as possible.

### Working with entitlements for one-time purchases

**With Gateway events.** When a user purchases a SKU, Discord emits an `ENTITLEMENT_CREATE` event
containing the entitlement object that represents the user's access to the SKU. Use this event to
keep track of the user's entitlements in near-time. For One-Time Purchases, you may also receive an
`ENTITLEMENT_DELETE` event if the user's entitlement is revoked.

**With the HTTP API.** Entitlements are available via the List Entitlements endpoint. Filter by a
specific user or set of SKUs with `?user_id=XYZ` or `?sku_ids=XYZ`.

**On interaction payloads.** The `entitlements` field of the `Interaction Payload`.

**With the Embedded App SDK.** `getEntitlements()` in an Activity.

Depending on your app's needs, use a combination of these methods to keep track of user entitlements.

### One-time purchase considerations

**For durable one-time purchases.** Users will have access to the SKU indefinitely. Durable items
can't be consumed, so you don't need to worry about the user losing access to the item except in the
case of a refund.

**For consumable one-time purchases.** Users can only have **one unconsumed entitlement at a time**.
To handle consumable items, process and store the consumable item in your app and then call the
Consume Entitlement endpoint so that the user can purchase more of this item in the future.

Consuming the entitlement will update the entitlement to return a true value in the entitlement's
`consumed` field. You will need to think through how your app keeps track of consumable items to
decide on the best strategy for when to consume these entitlements and store the state of the
consumable item and quantity in your app.

### Prompting users to purchase an item

**Responding with a premium button** gives you the ability to prompt users to subscribe to your app
when they attempt to use a premium feature without a subscription. Send a message with a button with
a premium style and a `sku_id`.

**Starting a purchase from an Activity**: use the Embedded App SDK to launch the purchase flow for a
specific SKU.

### Testing one-time purchases: Application Test Mode

**The method of testing purchases for One-Time Purchases differs from the method for App
Subscriptions. Do NOT use Test Entitlements for One-Time Purchases.**

While in Application Test Mode, you can freely make "purchases" of One-Time Purchase SKUs tied to
your application. That means you can test buying your consumable and durable items by going through
the In-App Purchase flow without any credit card charges.

You still need to have a valid payment method on file to "purchase" SKUs in Application Test Mode. It
just won't be charged at checkout.

To enable it, first make sure you have a payment method on file in `User Settings -> Billing` and
then:

1. Open up the Discord app
2. Click on the Settings cog in the bottom left corner
3. Go to the `Advanced` page under App Settings
4. Toggle "Developer Mode" **on** and "Application Test Mode" **on**, and enter your application ID.
   You can leave the other settings as-is.
5. Exit user settings

Once you enabled Application Test Mode successfully, you should see an orange bar across the top of
your screen with the name of your app.

You can now navigate to your Store page and purchase your one-time purchase items without being
charged.

The entitlements tied to items purchased in Application Test Mode can be identified by entitlements
with a `type` value of **4** to represent `TEST_MODE_PURCHASE`.

**Known issue:** the "Go To SKU" button does not currently work. To purchase your SKU in test mode,
go to your Store page.

---

## Implementing In-App Purchases for Activities

In-App Purchases (IAP) for Activities allows developers to easily monetize their Activity by allowing
users to buy premium subscriptions or items natively in Discord, using the Embedded App SDK.

Before you can add premium products with the Embedded App SDK in an Activity, you must enable
monetization for your app.

### Key concepts

- **SKUs**: Represent your app's premium products.
- **Entitlements**: Represent the user's access to your premium products.
- **Subscriptions**: Represent an ongoing agreement for a user to pay for an entitlement on a
  recurring basis until canceled.

Before you can start implementing monetization, create a SKU for each premium product.

### Publishing SKUs for Activities

When publishing SKUs, you can choose to publish them to your **Store and the API** or **API Only**.
Which method you select depends on the purchase experience you want to offer your users.

**Published to Store and the API**

- Your SKUs will be visible to users in the Discord client in your app's store or your Activity's
  custom storefront.
- Your users will be able to purchase them directly from the Discord client **without having your
  Activity open**, so you should handle the purchase flow accordingly.

**Published to API Only**

- Your SKUs will **not** be visible to users in your app's store, and users will only be able to
  purchase them through your Activity's custom storefront.

### Building a storefront

Once you have created your SKUs, you will need to build and render your own custom storefront in your
Activity to display your premium products to users.

**Listing SKUs.** To fetch the list of products for displaying in your Activity, call the
`getSkus()` command from the Embedded App SDK. You can also fetch SKUs using the HTTP API
(`GET /applications/{application.id}/skus`).

**Mapping SKUs to your premium perks.** When a user purchases a SKU, an entitlement is created. Map
your SKUs to the premium perks you are offering to ensure users receive the correct perks. Keep in
mind:

- SKUs should be mapped to product based on `id` attribute, **not** other attributes (such as
  `name`).
- **SKUs can never be deleted**, so once purchased it cannot be revoked and should always be mapped
  to some perk or product in your application.

**Formatting and displaying prices.** The methods for listing SKUs automatically localize currency
and prices. This means `sku.price` has a number `amount` attribute and a string `currency` attribute.
Properly rendering prices with proper currency can be challenging, given the large number of
currencies. The Embedded App SDK provides a `PriceUtils` utility to make this easier:

```javascript
import {PriceUtils} from '@discord/embedded-app-sdk';

const displayPrice = PriceUtils.formatPrice(sku.price);
console.log(`The price is ${displayPrice}!`);
```

### Working with entitlements in an Activity

Depending on your app's features, use a combination of the Embedded App SDK events, Gateway events,
the Entitlement HTTP API, and interaction payloads.

**Fetching entitlements with the Embedded App SDK.** Use the `getEntitlements()` SDK command to fetch
a list of entitlements for a user. This command returns a list of entitlement objects that represent
the user's access to your premium products.

**Handling subscription entitlements.** When a user purchases a subscription SKU, an entitlement is
created — see the App Subscriptions section above.

**Handling one-time purchase entitlements.** When a user purchases a one-time purchase SKU, an
entitlement is created — see the One-Time Purchases section above.

**Consumable and durable items in Activities.** It is common in Activities to have consumable or
one-time-use items, such as a single-use potion or power-up. When a user purchases a consumable SKU,
an entitlement is created marked `consumed: false`. Your application should process the item purchase
and consume the entitlement as soon as possible to grant the user the perks associated with the item.
If you want to offer an item that grants perks for an unlimited amount of time, use a **durable** SKU
instead of a consumable SKU.

### Initiating purchases

After displaying your SKUs in your custom storefront, initiate a purchase when a user selects a SKU.

To initiate a purchase in your activity, use the Embedded App SDK to call the `startPurchase()`
command with the selected SKU `id`. This command opens the purchase flow modal in the Discord client,
allowing users to purchase that SKU.

To know when it has been completed, subscribe to `ENTITLEMENT_CREATE` events. Once a user completes a
purchase, Discord emits an `ENTITLEMENT_CREATE` event. Subscribe with the SDK's `subscribe()` method:

```js
import {DiscordSDK} from '@discord/embedded-app-sdk';
const discordSdk = new DiscordSDK(clientId);
await discordSdk.ready();

const handleEntitlementCreate = () => {
  // refetch entitlements from server using the Entitlement HTTP API endpoint
};
discordSdk.subscribe('ENTITLEMENT_CREATE', handleEntitlementCreate);
```

You can also subscribe to the `ENTITLEMENT_CREATE` event using the Gateway API to receive the event
in your app's backend, or use the List Entitlements HTTP API endpoint to fetch a user's entitlements.

### Data security considerations

When working with SKUs and Entitlements in an Activity, it's crucial to ensure the security and
integrity of your application's data.

Developers should ensure the accuracy of data obtained via Embedded App SDK commands and events. **A
malicious actor could potentially establish their own RPC connection and interact with your
application client, posing as Discord.** While this might not be an issue for most SDK commands and
events, it becomes critical when dealing with perks offered through In-App purchases.

If your application relies solely on SDK data to determine a user's entitlements, a malicious actor
could exploit this to gain access to premium products, features, or advantages without paying. This
is particularly relevant for commands like `getEntitlements()`.

**Use the Discord HTTP API for verification.** Data fetched from the Discord HTTP API from your
application's backend servers can be trusted and should be treated as the source of truth. This data
should be used to validate any inconsistent client-side data.

**Recommended approach**

- **Optimistically** use client-side techniques such as SDK commands and events to fetch SKUs and
  Entitlements.
- **Verify** the results via the Discord HTTP API from your application's backend.

In summary, use the principle of "Trust (the SDK), but Verify (via the API)".

### Testing your in-app purchases

To test your In-App Purchases in your Activity, follow the testing guidelines for **both** types of
SKUs: One-Time Purchases (Application Test Mode) and Subscriptions (test entitlements or live
entitlements with the team discount).

After you've tested your In-App Purchase flows, verify that your application has correctly granted
the user the premium perks associated with the SKUs that were purchased during testing.

### Example implementation

Discord's example implementation of In-App Purchase is the **SDK Playground Example Application**:
`https://github.com/discord/embedded-app-sdk-examples/tree/main/sdk-playground`

The example implementation includes client-side and server-side code. It also follows the security
considerations above. It implements the commands and events available within the Embedded App SDK,
including In-App Purchases.

---

## Managing SKUs

The premium items and subscriptions you offer in your app are represented by SKUs. **SKU** stands for
Stock Keeping Unit and is a unique identifier for your premium offerings. SKUs are the building
blocks of your premium offerings and you manage them in the Developer Portal.

### Creating a SKU

To create a new SKU, navigate to your app's settings (`https://discord.com/developers/applications`)
and select the **Monetization -> Manage SKUs** tab
(`https://discord.com/developers/applications/select/skus`). From there, create a new SKU by clicking
the `Create SKU` button.

When you click on `Create SKU`, you have the option to select from the following:

- **User Subscription**: An auto-recurring subscription that grants benefits to one user in all
  servers
- **Guild Subscription**: An auto-recurring subscription that grants benefits to all users in one
  server
- **Consumable**: A one-time purchase that provides a temporary benefit, which is consumed upon use.
- **Durable**: A one-time purchase that **grants** a permanent addition or enhancement.

Once you select the SKU type, enter a name for your SKU to continue.

**Creating subscription tiers.** You can create multiple subscription tiers to offer different
benefits at different price points. Each tier can have its own set of benefits and price and is
represented by unique SKUs. To support upgrading and downgrading between tiers, see
[Supporting upgrades and downgrades](#supporting-upgrades-and-downgrades).

*(Screenshot caption: "Supporting multiple subscription tiers".)*

### SKU limitations

There are some limitations to the number of SKUs you can create:

- You can create up to **50 total SKUs per app**.
- You can offer **either** user subscription SKUs **or** guild subscription SKUs, **but not both
  simultaneously**.
- SKU prices must be selected from the list of available prices.

If you need more SKUs than the 50 limit, consider creating a consumable in-app currency SKU that can
be used to purchase items that are tracked in your app.

### Customizing your SKUs

Once you've created a SKU, you can customize it to match your app's branding and the benefits you
want to offer. You can customize:

- A name for your premium SKU, **max 80 characters**.
- A description for your premium SKU, **max 160 characters**
- An image for your premium SKU
- A price for your premium SKU

Your list of benefits will be displayed on your app's Store page, the App Directory, and during the
purchase and cancellation flows to explain to users the benefits of your premium offering. These
benefits can have:

- Up to **6 benefits**
- An emoji, standard or custom
- A name, **max 80 characters**
- A description, **max 160 characters**

*(Screenshot caption: "Example of SKU benefits".)*

**Using Unicode emoji.** To set an icon using a standard Unicode emoji, enter the emoji in the
`Unicode Emoji or Custom Emoji Name` field. Using an emoji keyboard can make it easier to pick an
icon to display alongside your SKU benefit — MacOS: `control + command + space bar`; Windows:
`Windows + .` *(Screenshot caption: "Set a unicode emoji".)*

**Using a custom emoji.** To use a custom emoji, set a value for both fields:

- Name of your custom emoji
- ID of the custom emoji

You can find the ID of the emoji in the Discord app by escaping the emoji in a message with a
backslash character `\`. For example, `\:uwu:` will render with the name and ID of the emoji.
*(Screenshot caption: "Set a custom emoji".)*

### Pricing your SKUs

When setting the price for your SKU, you can select from a list of predefined prices. **The prices are
automatically converted to the user's local currency based on their locale.**

Subscription SKUs are automatically charged each month unless canceled. Changing the price of this SKU
will only change it for new subscribers. Existing subscribers will continue to be charged the
existing price.

### Publishing and unpublishing SKUs

When you initially create a SKU, it will be in an `Unavailable` state. This SKU is not yet available
for purchase by users. You can edit the SKU to add a price, benefits, and other details before
publishing it.

While creating and editing SKUs in your app's settings on the **Monetization -> Manage SKUs** tab, you
have a few options for managing your SKUs' visibility and publishing to your users:

- Publish SKU
- Unpublish SKU
- Delete SKU

**Publishing a SKU.** When publishing a SKU, you have the option to make it **Available via the Store
and API** or **Available via the API Only**.

- **Publishing to Store & API**: available to be purchased and visible in your app's store.
- **Publishing to API Only**: you can only make API calls or use the Embedded App SDK to grant
  entitlements for this SKU.

**Unpublishing a SKU.** Danger: unpublishing a SKU can affect your users' existing subscriptions and
entitlements. Unpublishing a SKU removes it from the Store and the API, making it unavailable for
purchase. Unpublishing a SKU has the following effects:

- For subscription SKUs, subscriptions will not be renewed for users and guilds that have this SKU at
  the end of the billing period.
- Users and guilds will still be entitled to the SKU until the end of the billing period.
- For consumable and durable SKUs, users will still be entitled to the SKU if they purchased it before
  it was unpublished.
- Does not delete a SKU.

**Deleting a SKU.** Danger: deleting a SKU can affect your users' existing subscriptions and
entitlements. Deletes a SKU in the UI and makes it unavailable for publishing. **Deleted SKUs are
still listed when calling List SKUs in the API.** Deleting a SKU has the following effects:

- For subscription SKUs, users and guilds will be immediately unsubscribed from the SKU. Their
  entitlement will still be valid until the end of the billing period.
- For consumable and durable SKUs, users will still be entitled to the SKU if they purchased it before
  it was unpublished.

### Editing a published SKU

If you wish to change a SKU that is published, you can do so at any time by first unpublishing the
currently published one. When you unpublish a SKU, it is no longer available for sale and users who
have already subscribed will not renew at the end of their billing period. **You must continue to make
the premium offering available to them until the end of their subscription.**

**Changing a subscription SKU price.** When you change the price of a user or guild subscription SKU,
it will only affect new subscribers. Existing subscribers will continue to be charged the price of the
SKU at the time they subscribed.

### Viewing your Store page

Users can access an app's Store page from the Bot User's profile in a server. This allows users to
view an available subscription and one-time purchases, select a subscription to view its perks,
benefits, and details, and make a purchase directly from an app's Store page.

**Only subscriptions and items that have been published to the Store will be visible to users on the
Store page.**

*(Screenshot captions: "Accessing the store as a user" — accessing your Store page from a Bot User's
profile; "Subscriptions in your Store View"; "Items in your Store View".)*

### Linking to a specific SKU

You can link directly to a specific SKU using the Application Directory Store URL scheme:

`https://discord.com/application-directory/:appID/store/:skuID`

- When used in chat, it will render as a rich embed that allows users to launch a modal to view either
  the SKU details or checkout flow
- When used as a direct URL in a browser, it will take the user to your product in the Application
  Directory on web

*(Screenshot caption: "Embed for direct link to SKU".)*

### Linking to your Store

You can link directly to your Store page using the Application Directory Store URL scheme:

`https://discord.com/application-directory/:appID/store`

- When used in chat, it will render as a rich embed that allows users to launch a modal to your Store
  page
- When used as a direct URL in a browser, it will take the user to your Store page in the Application
  Directory on web

*(Screenshot caption: "Embed for direct link to Store".)*

### Responding with a premium button

You can prompt users to purchase item or subscription SKUs using a button with a premium style and a
`sku_id`. You can use this premium button style anywhere you would use message components, such as in
a command response.

```javascript
return new JsonResponse({
    type: 4, // InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE
    data: {
        content: "This command requires Nelly Premium! Upgrade now to get access to these features!",
        components: [{
            type: MessageComponentTypes.ACTION_ROW,
            components: [
                {
                    type: MessageComponentTypes.BUTTON,
                    style: 6, // ButtonStyleTypes.PREMIUM
                    sku_id: '1234965026943668316',
                },
            ],
        }]
    },
});
```

Button style **6** is `PREMIUM`. *(Screenshot caption: "A premium button".)*

### Integrating SKUs in your app

After you've published your SKUs, you are ready to start implementing your premium features. The two
guides to follow are Implementing App Subscriptions and Implementing One-Time Purchases, both covered
above in this file.

## Source

Discord Developer Documentation:

- `https://docs.discord.com/developers/monetization/implementing-app-subscriptions`
- `https://docs.discord.com/developers/monetization/implementing-one-time-purchases`
- `https://docs.discord.com/developers/monetization/implementing-iap-for-activities`
- `https://docs.discord.com/developers/monetization/managing-skus`

Retrieved 2026-08-26.
