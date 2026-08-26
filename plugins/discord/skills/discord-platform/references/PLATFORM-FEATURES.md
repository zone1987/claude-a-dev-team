# Discord Platform Feature Pages

Complete extraction of the 12 `platform/*` pages plus `bots/overview`, retrieved 2026-08-26. One `##`
section per page, in the order the skill map lists them.

Several of these pages are **short overviews whose main job is to point elsewhere**. Where that is the
case it is stated explicitly at the top of the section, with the pointer target named, rather than
padded out.

## Contents

- [platform/bots — Bots & Companion Apps](#platformbots--bots--companion-apps)
- [bots/overview — Discord Bots & Companion Apps](#botsoverview--discord-bots--companion-apps)
- [platform/interactions — Interactions & Commands](#platforminteractions--interactions--commands)
- [platform/components — Components & Modals](#platformcomponents--components--modals)
- [platform/webhooks — Webhooks](#platformwebhooks--webhooks)
- [platform/server-and-channel-management — Server and Channel Management](#platformserver-and-channel-management--server-and-channel-management)
- [platform/discovery — App Discovery](#platformdiscovery--app-discovery)
- [platform/community-servers — Community Servers](#platformcommunity-servers--community-servers)
- [platform/claim-your-game — Claim Your Game](#platformclaim-your-game--claim-your-game)
- [platform/game-profiles — Game Profiles](#platformgame-profiles--game-profiles)
- [platform/rich-presence — Rich Presence](#platformrich-presence--rich-presence)
- [platform/social-layer — Social Layer for Games](#platformsocial-layer--social-layer-for-games)
- [Which pages are thin](#which-pages-are-thin)

## platform/bots — Bots & Companion Apps

*Page tagline: "Build bots and companion apps that connect to Discord and interact with servers,
members, and events."*

Upstream opens with a jump line: *Already familiar? Jump to the Bots & Companion Apps docs
(`bots/overview`) or Getting Started guide (`quick-start/getting-started`).*

**Bots are the most common type of Discord app.** They appear in servers as **bot users with an `APP`
tag** and can **listen to events, respond to slash commands, moderate servers, send messages, and much
more**, all powered by your code via the Discord API.

### The two connection models

Bots can connect to Discord in **two ways**:

| Model | What it is | What it carries |
| --- | --- | --- |
| **Gateway WebSocket** | A **persistent** connection | Real-time events |
| **HTTP interactions endpoint** | **No persistent connection** required | Slash commands and UI components |

**Most bots use one or both depending on their use case.**

### Common use cases

Upstream names five: **moderation tools, server utilities, games, integrations with external services,
and automated workflows.**

### Bot versus webhook

**If you only need to push messages into a channel, a webhook might be a better fit than a full bot.**
Webhooks are **simpler to set up** and **can send messages with rich embeds**, but they **can't listen
to events or respond to interactions** like bots can.

### Cards on this page

Three: **Bots Overview** ("What bots are, how they work, and when to use one"), **Getting Started**
("Build and run your first Discord bot end to end"), **Bot Dev Guides** ("Guides on interactions,
components, monetization, and more").

## bots/overview — Discord Bots & Companion Apps

*Page tagline: "Start building bots and companion apps for Discord."*
Hero image caption: "Discord Bots & Companion Apps Hero Image".

**Bots are applications that connect to Discord using the Discord API.** They appear in servers as
**users with an `APP` tag** and can **interact with members, respond to events, and perform actions
programmatically**. For a deeper look at what bots can do and when to use one, upstream points at the
`platform/bots` platform page (the section above).

### Getting Started — the four steps

To build a bot, upstream states you'll need to:

1. **Create an application** in the Discord Developer Portal. **This is where your bot token, OAuth2
   credentials, and configuration live.**
2. **Add a bot user** to your application **from the Bot tab**. **This generates the token your code
   uses to authenticate.**
3. **Invite the bot** to a server **using an OAuth2 URL with the bot scope and the permissions your bot
   requires**.
4. **Connect to the API** using **the Gateway for real-time events**, **the HTTP API for REST
   operations**, or **both**.

**Most developers use a community-maintained library in their language of choice rather than
interfacing with the API directly.** Official and community libraries are listed on the Community
Resources page (`developer-tools/community-resources`).

The **Getting Started guide** (`quick-start/getting-started`) walks through building and running your
first bot end to end.

### Building Your Bot — the five areas

| Area | What upstream says it covers |
| --- | --- |
| **Interactions** (`interactions/overview`) | Slash commands, context menu commands, buttons, select menus, and modals that let users interact with your bot. |
| **Components** (`components/overview`) | Layout, content, and interactive UI elements you can attach to messages and modals. |
| **Monetization** (`monetization/overview`) | Add subscriptions and one-time purchases to your bot using Discord's built-in payment flow. |
| **Discovery** (`discovery/overview`) | Get your app listed in the App Directory and App Launcher so users can find and install it. |
| **Guides & Tutorials** (`guides/bots`) | Practical guides on implementing common bot features and best practices. |

### Cards on this page

Two: **Build Your First App** ("Step-by-step guide to building and running your first Discord bot"),
**Bot Development Guides** ("Explore guides on implementing common bot features and best practices").

## platform/interactions — Interactions & Commands

*Page tagline: "Build interactive slash commands, buttons, modals, and more using HTTP or the
Gateway."*

**Interactions are the foundation of user-facing Discord app features.** When a user **invokes a slash
command, clicks a button, selects from a dropdown, or submits a modal**, Discord sends your app an
**interaction payload** that your app can respond to directly.

Your app can receive interactions **over the Gateway** or **via HTTP requests to a dedicated
endpoint**. Both models are designed to be easy to implement and scale with your app's needs, whether
you're building a simple command handler or a complex interactive experience.

### Application Commands — the four types

| Type | How users reach it |
| --- | --- |
| **Slash commands** | Accessed by **typing `/` in the chat input**. |
| **Message commands** | Accessed from the **context menu on a message**. |
| **User commands** | Accessed from the **context menu on a user profile**. |
| **Entry Point commands** | Used to **launch Activities from the App Launcher**. |

When a user invokes a command, Discord sends your app an interaction payload you can respond to with
**a message, a modal, or a deferred response for longer-running work**.

### Message Components and Modals

**Message components also generate interactions when users act on them.** When a user **clicks a button
or submits a select menu** attached to one of your app's messages, **Discord delivers an interaction
the same way it would for a command**.

**Modals work the same way.** Your app responds to an interaction (a command or component click) by
**opening a modal**, and **the user's submission arrives as another interaction** your app handles.

### Gateway interactions

**By default, your app receives interactions over the Gateway** — the same persistent WebSocket
connection used for all other real-time events. If your bot is already connected to the Gateway to
listen for messages, member joins, or other activity, **interactions arrive through the same
connection**.

### HTTP interactions

Alternatively, you can configure an **Interactions Endpoint URL** in your app's settings to receive
interactions as **HTTP POST requests sent directly to your server**. **Discord handles delivery and
your app needs to respond within a few seconds.**

This model **works well for apps that only need to respond to commands and UI components**. **No
persistent connection is required and it scales naturally with standard web infrastructure.** To use
it, **your endpoint must validate Discord's request signatures and handle the initial `PING`
handshake.**

### Cards on this page

Three: **Interactions Overview** ("Full guide to interaction types, endpoint setup, and security
validation"), **Application Commands** ("Create slash commands, message commands, user commands, and
entry point commands"), **Receiving & Responding** ("Technical reference for handling interaction
payloads and sending responses").

## platform/components — Components & Modals

*Page tagline: "Add interactive buttons, menus, layout elements, and modal dialogs to your Discord
app."*
Hero image caption: "Discord Bots & Companion Apps Hero Image".

**Discord's component system lets your app build rich, interactive UI directly inside the Discord
client, with no custom frontend needed.**

### Message Components

Message Components are **interactive and layout elements attached to messages your app sends**. Discord
supports **three categories**:

| Category | What it is for |
| --- | --- |
| **Layout components** | Organizing content. |
| **Content components** | Displaying text and media. |
| **Interactive components** | Buttons, select menus, and text inputs that users can act on. |

**Components are sent as structured data alongside your message and rendered natively in the Discord
client.**

### Modals

Modals are **form-like overlays** that your app can present to users **in response to an interaction**,
such as **a button click, slash command, or select menu selection**. They **collect freeform input
through text fields** and are a natural fit for **multi-field data entry, confirmations, bug reports,
or any configuration flow that needs more than a single tap to complete**.

**Unlike message components, modals aren't attached to a message.** They are **sent as an interaction
response** and **appear as a focused overlay in the client**. **The user fills in the fields and
submits, which triggers a new interaction your app can handle.**

### Cards on this page

Three: **Components Overview** ("Full guide to available component types and how components are sent in
messages"), **Using Message Components** ("A guide on sending Message Components with code examples"),
**Using Modal Components** ("A guide on building and displaying Modal Components with code examples").

## platform/webhooks — Webhooks

*Page tagline: "Send messages into Discord channels or receive event notifications from Discord
delivered to your app over HTTP."*

**Discord supports two distinct types of webhooks that work in opposite directions**: **incoming
webhooks** for posting messages into Discord, and **webhook events** for receiving notifications from
Discord when something happens in your app.

### Incoming Webhooks

Incoming webhooks are **HTTP endpoints tied to a specific Discord channel**. **You POST a payload to
the URL and the message appears in that channel. No bot or persistent connection required.** The full
API reference is the Webhook Resource (`resources/webhook`).

This makes them **ideal for one-way integrations where an external system needs to push data into
Discord**. Upstream's four examples:

- **CI/CD pipelines** posting build results or deployment notifications
- **Monitoring systems** alerting on errors or anomalies
- **External apps** posting updates (GitHub commits, Jira tickets, form submissions)
- **Scheduled digests or reports** from cron jobs

**If you need your app to also listen to events or respond to users, building a Discord bot is the
better fit.**

### Webhook Events

**Webhook events work in the opposite direction. Discord POSTs to a public URL on your server when
specific events occur in your app.** Instead of your app polling the API, **Discord pushes the
notification to you**.

**You subscribe to the specific event types you care about through the Developer Portal**, and Discord
delivers them as **signed HTTP POST requests** to your endpoint. **Your endpoint must validate
Discord's request signatures and acknowledge events promptly.**

Events you can subscribe to **include** (upstream's three examples, not the full list):

- **Application authorized or de-authorized by a user**
- **Entitlement created** (a user purchased something from your app)
- **Quest enrollment and completion events**

For the full list of subscribable events and setup instructions, upstream points at the Webhook Events
documentation (`events/webhook-events`).

### Cards on this page

Two: **Webhook Resource Reference** ("Full API reference for incoming webhook endpoints and objects"),
**Webhook Events** ("Subscribable event types and how to set up your endpoint to receive them").

## platform/server-and-channel-management — Server and Channel Management

*Page tagline: "What Discord apps can do with servers and channels, and what permissions they need."*

Discord apps can **programmatically interact with Discord servers (guilds) and channels**. This
includes **reading content, posting messages, managing members, creating channels, and more**. **Nearly
all of these actions require the bot to have the appropriate permissions in the target server or
channel.**

Upstream frames the capability lists below as **examples**, pointing at the API Reference
(`/developers/reference`) for a complete list of endpoints and capabilities.

### What apps can do — Guilds

- **Read guild metadata**: name, icon, member count, features
- **List and manage roles** (create, update, delete, assign to members)
- **Kick and ban members**
- **Manage and audit server events**
- **List guild integrations and webhooks**

### What apps can do — Channels

- **List and read channels** across the server
- **Create, edit, and delete channels and threads**
- **Set channel permissions and position**
- **Read and send messages** (subject to message permissions)
- **Manage pinned messages**

### What apps can do — Members

- **Fetch member profiles and role assignments**
- **Add or remove roles from members**
- **Modify member nicknames**
- **Manage member timeouts**

### Key Permissions

Most server and channel operations require explicit permissions. The full list is the Permissions
reference (`topics/permissions`); upstream reproduces these eight common ones verbatim:

| Permission        | What It Enables                                      |
| ----------------- | ---------------------------------------------------- |
| `MANAGE_GUILD`    | Edit server settings, view audit log                 |
| `MANAGE_CHANNELS` | Create, edit, delete channels                        |
| `MANAGE_ROLES`    | Create and manage roles below the bot's highest role |
| `KICK_MEMBERS`    | Remove members from the server                       |
| `BAN_MEMBERS`     | Permanently ban members                              |
| `MANAGE_MESSAGES` | Delete messages from other users, pin messages       |
| `VIEW_CHANNEL`    | See a channel and its message history                |
| `SEND_MESSAGES`   | Post messages in a channel                           |

**Permissions can be overridden at the channel level**, so **a bot may have server-wide permissions but
be restricted in specific channels (or vice versa)**.

### Cards on this page

Two: **Guild Resource** ("Full API reference for guild endpoints and objects"), **Channel Resource**
("Full API reference for channel endpoints, message sending, and threads").

## platform/discovery — App Discovery

*Page tagline: "Make your Discord app discoverable through the App Directory, App Launcher, and social
sharing."*

**This is an overview page pointing at the three `discovery/*` pages** — see `DISCOVERY.md` in this
skill for the full treatment. The content unique to this page:

**App Discovery gives users multiple ways to find and install your app across Discord.**

- **App Directory** — at `https://discord.com/discovery/applications`. A **searchable hub where users
  can browse apps by name, category, or collection, and view a full product page with descriptions,
  screenshots, and links**. **To appear here, your app needs to be verified and opted into discovery.**
- **App Launcher** — **accessible from the app shapes icon throughout Discord**, and **surfaces
  recently used apps and apps curated by collection**. Upstream links the help centre article "How to
  Discover and Add Apps" (`https://support-apps.discord.com/hc/en-us/articles/26592957841303`).
- **Organic Discovery & Sharing** — once your app is discoverable, **social interactions within Discord
  become a natural acquisition channel**. When users interact with your app in a server, **others in
  that server can see it and visit your app's profile to install it themselves**. Each Discord app also
  has **sharable links that take users to your app's profile or store page**
  (`monetization/managing-skus#linking-to-your-store`), **shareable anywhere from Discord messages to
  external websites**.

### Cards on this page

Three: **Discovery Overview** ("Full guide to discovery surfaces, the App Directory, App Launcher, and
social discovery"), **Enabling Discovery**, **Discovery Best Practices**.

## platform/community-servers — Community Servers

*Page tagline: "Build and grow a player community around your game by building out a community server
on Discord."*

**This page is a short overview whose feature list points entirely at Discord's support help centre**,
not at developer documentation. Nothing on it is an API surface.

**Community Servers are Discord servers with a dedicated set of features for building a public
audience** — five features, each a help centre link:

| Feature | Help centre article |
| --- | --- |
| **Structured Community Onboarding** | Community Onboarding Examples (`support.discord.com/.../10394859532823`) |
| **Announcement Channels** | Announcement Channel FAQ (`.../360032008192`) |
| **AutoMod** | AutoMod FAQ (`.../4421269296535`) |
| **Server Discovery** | Server Discovery (`.../360023968311`) |
| **Server Insights** | Server Insights FAQ (`.../360032807371`) |

**Most game developers use a Community Server as the official home for their players** — a place to
**share updates, offer support, and keep the community connected between game sessions**.

### Enabling Community Server features

**Any server can become a Community Server** by following the steps in "Enabling Your Community Server"
(`support.discord.com/hc/en-us/articles/360047132851`). **Once you enable Community features, you can
start building out your server with the features listed above.**

### Official Game Communities

Once you have a Community Server set up, **you can claim it as your Official Game Community by Claiming
Your Game** (see the `platform/claim-your-game` section below). **This gives you access to**:

- **a custom vanity URL**,
- **a verified badge**, and
- **the ability to link your game to your server** so players can easily find it **from your game's
  store page and Discord profile**.

### Cards on this page

Three: **Enabling Community Server Features** ("Step-by-step instructions for enabling Community
features on your Discord server"), **Create a Community For Your Game**
(`game-development/how-to-create-a-community-for-your-game` — "Set up a community server, design roles
and channels, and bring players in from your game"), **Community Management Guides** (`guides/communities`).

## platform/claim-your-game — Claim Your Game

*Page tagline: "Learn how to claim your game on Discord to unlock a verified checkmark and take control
of your game's profile."*
Hero image caption: "A rendition of the benefits that come with the verified checkmark".

This is the **longest platform page** and is a full procedure, not an overview.

### What is Game Claiming?

**Claiming your game connects your Discord community server and game profile to your verified
developer identity.** **Players get a verified place to find the official game community, and you get
direct control over how your game is represented on the Discord app.**

### Benefits — Game Profile Customization

Discord **automatically generates a game profile for every game it detects**. Once you claim your game,
**you control the information and visual appearance of that profile across four sections**:

| Section | Contents |
| --- | --- |
| **Title** | description, genres, platforms |
| **Visual Assets** | cover, icon, banner, screenshots |
| **Links** | official website, social media |
| **Company** | name, publisher or developer role |

**Changes are made directly in the Developer Portal**, making it easy to keep your game's identity
current with **live service updates or seasonal content**.

### Benefits — Verified Checkmark

**Once your claim is confirmed, your Discord server receives a green verified badge on its server
profile**, marking it as **the verified community for your game on Discord**. **The checkmark is
visible in Server Discovery and is only available to servers associated with a claimed game.**

### Before You Begin — every eligibility requirement

**Six requirements**, exactly as upstream states them:

1. **Your game must have a Steam store page.** **Other storefronts are not yet supported.**
2. **Your Steam store page must have a publicly visible Discord invite link.** During the claim
   process, **you'll receive a `proof` value to append to that link** before the claim can be
   submitted.
3. **Games whose primary purpose is the delivery of sexual content, or are Mods of other games, are not
   eligible for claiming.**
4. **Your Discord application must be assigned to a development team** (`topics/teams#teams`), **not
   owned by an individual account**.
5. **The server owner must be a member of your Team.** **Discord verifies ownership by sending a
   verification code to the server owner's email address.**
6. **Discord must have an official record of your game.** **Discord automatically recognizes games that
   have established a sufficient playerbase and play time among Discord users over an extended
   period.**

**How to check whether Discord has a record of your game** (upstream `Tip`): **search for it in the Game
Identity dropdown in Step 2.** **If your game does not appear there, Discord does not yet have an
official record of it.** As your game's playerbase and playtime grow, **it will become eligible for
automatic recognition**.

**Implementing Rich Presence via the Discord Social SDK is separate from automatic game detection** —
these are **independent systems**, and **having Rich Presence alone does not make a game claimable**.

**Games in private beta or limited release are not supported at this time.** **Your game must be
publicly available and playable to be eligible for claiming.** (Upstream `Info`.)

### Claiming Your Game — the six steps

#### Step 1: Open Game Identity in the Developer Portal

Visit Game Identity in the Developer Portal
(`https://discord.com/developers/applications/select/game-identity`) and **select your application**.
**The game claiming interface will appear automatically.**

**If you're an existing SDK partner, claim your game to the application you're already using for your
SDK integration.** (Upstream `Info`.)

#### Step 2: Find and Select Your Game

**Search for your game by name in the Game Identity interface and select it to begin the claim.**

**If your game does not appear there, Discord does not yet have an official record of it.** As such,
**you will not be able to claim your game at this time**. As your game's playerbase and playtime grow,
it will become eligible for automatic recognition.

#### Step 3: Update Your Steam Invite Link

After selecting your game, **the claim interface will display a `proof` query parameter**. **Copy this
value and append it to your Discord invite link on your Steam store page.**

1. **Copy the `proof` value shown in the Developer Portal.**
2. **Update the Discord invite link on your Steam store page to include it** — upstream's example form:
   `discord.gg/yourcode?proof=<string>`.

**Once your link is updated, Discord will verify the `proof` value before you can continue.**

#### Step 4: Verify Server Ownership

To confirm you own the Discord server linked on your Steam store page, **Discord will send a
verification code to the server owner's email address**.

1. **Check the email inbox associated with the owning Discord account.**
2. **Enter the code when prompted to continue.**

#### Step 5: Provide Your Details

You'll be asked to provide:

| Detail | Required? |
| --- | --- |
| **Your full legal name** | **required** |
| **A professional contact email** | **required** |
| **Your role at the company** | optional |
| **Your company or game website** | optional |

**This information will be used as described in Discord's Developer Terms of Service**
(`https://support-dev.discord.com/hc/en-us/articles/8562894815383`). (Upstream `Info`.)

#### Step 6: Submit for Review

**Once all steps are complete, submit your claim.** **Discord will notify you if the claim is
successful, or reach out if additional information is needed.**

### If your claim is successful

**You'll be notified by email** and the **Game Identity** section in your **Developer Portal** will
update. **You can then begin customizing your game's profile.**

### If your claim is rejected

**Work within the Developer Support ticket** (`https://dis.gd/developer-support/game-development`) **to
address any concerns.**

### Current Limitations

**Three**, exactly as upstream states them:

- **No mobile support:** **Games must be playable on non-mobile platforms (PC, Mac, or consoles).
  Mobile-only games cannot currently be claimed.**
- **Steam only:** **Only games with a Steam store page can currently be claimed. Support for other
  platforms is not yet available.**
- **Released only:** **Only games listed on Steam and playable by the public (no private betas) can
  currently be claimed.**

Upstream states it is **actively working on expanding coverage so more games can be claimed over
time**, and that if you believe your game should be listed and cannot find it, you should contact
Discord at `https://dis.gd/developer-support/game-development`.

### Cards on this page

Two: **Discord Social SDK** ("Build social features directly into your game — friends, voice, lobbies,
and more"), **Game Profiles** ("Learn how Discord surfaces your game's profile and where it appears
across the platform").

## platform/game-profiles — Game Profiles

*Page tagline: "Learn how Discord surfaces game information to users and where your game's profile
appears across the platform."*

**Discord generates a profile for games it detects users playing.** Each game profile is a **dedicated
page with the game's description, screenshots, and social media links**. **Game profiles allow users to
learn more about what friends are playing or discover their next game.**

### Where game profiles appear — four surfaces

| Surface | How the profile is reached |
| --- | --- |
| **Rich Presence** | When a user is **actively playing a game**, their current activity appears **on their profile and in the member list**. **Clicking the activity, then the game's cover art, opens the game's profile page.** |
| **Game Collections in User Profiles** | Discord users can **add widgets to their profile, curating lists of games** that appear on their profile. **Clicking a game's cover art in any widget opens the game's profile page.** |
| **Activity** | The **Activity tab** on a user's profile shows **games they have played recently**. **Clicking a game's cover art opens the game's profile page.** |
| **Game Profile Page** | The **full** game profile page. |

### The four areas of the game profile page

Identical to the four sections on the claim page:

| Area | Contents |
| --- | --- |
| **Title** | description, genres, platforms |
| **Visual Assets** | cover, icon, banner, screenshots |
| **Links** | official website, social media |
| **Company** | name, publisher or developer role |

### Take control of your game profile

If you're a **game developer or publisher**, you can **take ownership of your game's profile on
Discord**. Claiming your game lets you:

- **Update your game description**
- **Curate your screenshots with your best visuals**
- **Ensure your publisher and developer names are accurate**
- **Point players directly to your official Discord community and socials**
- **Get an official game community checkmark on your Discord server**

**Changes you make go live immediately without additional review**, so you can keep your profile current
with **new content updates or seasonal events**.

### Cards on this page

One: **Claim Your Game** ("Learn how to claim your game on Discord and customize your game's profile").

## platform/rich-presence — Rich Presence

*Page tagline: "Display real-time game activity on Discord user profiles with rich presence."*
Hero image caption: "Rich Presence".
Embedded video: "Boost Game Discovery with Discord Rich Presence [Discord DevBytes]"
(`https://www.youtube.com/embed/NlRtLGwemMw`).

**Rich Presence lets your game display live, actionable data on a Discord user's profile when they have
activity sharing enabled**: **what they're playing, what level they're on, how long they've been in a
session, or a prompt for friends to join**. It's a **lightweight integration that connects your app to
Discord's social layer**.

### What Rich Presence can carry

**The data you surface is entirely up to you.** Rich Presence supports:

- **custom text fields**,
- **timestamps**,
- **party size indicators**, and
- **uploaded art assets**.

**When configured with a "Join" button, friends can jump directly into a user's game session from the
profile card.**

### Choosing an SDK

Rich Presence is available through **two SDKs** depending on what you're building:

| SDK | When to use it |
| --- | --- |
| **Discord Social SDK** (`discord-social-sdk/overview`) | **Build social features into your game or app**, including **friends lists, game invites, and more**. Used for **native game integrations**. |
| **Embedded App SDK** (`developer-tools/embedded-app-sdk`) | Use **if you're building an Activity in Discord**. |

**Rich Presence data appears publicly on your Discord profile, so during development you should use a
test account that only belongs to your private development server(s).** (Upstream `Info`.)

#### Discord Social SDK

Used for **building social features directly into your game**. When a user is playing your game, **you
can show what they're up to in their Discord profile and even prompt their friends to join in with game
invites**.

When integrating Rich Presence with an **off-platform game**, data can be shown about what a user is up
to in your game. **A "Join" button can also be configured to allow a user's friends to jump into their
game and enable sending game invites.**

Implementation guide: `discord-social-sdk/development-guides/setting-rich-presence`.

#### Embedded App SDK

Used to **build Activities**, which are **multiplayer games and social experiences hosted in an iframe
within Discord**. **The SDK handles communication between Discord and the Activity and helps integrate
platform features (like Rich Presence).**

**After a user joins an Activity, Rich Presence can be used to dynamically show data about what that
user is doing or playing, as well as prompt others to join in and play along.**

Implementation guide: `rich-presence/using-with-the-embedded-app-sdk`.

### Cards on this page

Three: **Using Rich Presence with the Embedded App SDK**, **Using Rich Presence with the Discord Social
SDK**, **Rich Presence Best Practices** ("Design tips and a launch checklist for shipping a polished
Rich Presence integration").

## platform/social-layer — Social Layer for Games

*Page tagline: "Add Discord-powered social features directly into your game using the Discord Social
SDK."*
Embedded video: "Bring the Social Power of Discord Into Your Game with the Discord Social SDK [Discord
DevBytes]" (`https://www.youtube.com/embed/Uc8wLXMBRnM`).

Upstream opens with a jump line: *Already familiar? Jump to the Discord Social SDK docs
(`discord-social-sdk/overview`) or Getting Started guides (`discord-social-sdk/getting-started`).*

**The Social Layer for Games is a set of Discord-powered features that game developers can add to their
games using the Discord Social SDK.** **You can integrate individual features alongside your existing
social systems or build out a Discord-powered social experience.**

**The SDK is available for C++, Unity, and Unreal Engine, and works across PC, mobile, and console
platforms.**

### The eight feature areas

#### Account Linking

**Players can link their Discord account to your game to unlock the full social experience.** Once
linked, **they get access to their Discord friends list, game invites, rich presence, and voice directly
inside your game**. **The link persists across sessions, so players authenticate once and never need to
re-link.**

**Account linking supports both a Game Flow (from inside your game via the Social SDK) and a Web Flow
(through a standard OAuth2 page)**, giving players flexibility in how they connect. See
`platform/account-linking`.

#### Provisional Accounts

**Players who prefer not to link a Discord account can still use the SDK's social features through
provisional accounts** (`discord-social-sdk/development-guides/provisional-accounts/overview`). **This
lets you ship a consistent social experience for your full player base, regardless of whether they have
or want a Discord account.**

#### Friends List

**The SDK provides a friends list that works for all players, whether or not they've linked a Discord
account.** **Players using provisional accounts can add and manage in-game friends, while players who
have linked their Discord account also see their Discord friends alongside any in-game friends.**

#### Rich Presence

**Rich Presence surfaces what a player is doing in your game directly on their Discord profile when
they have activity sharing enabled.** **Friends browsing Discord can see the game, the mode, the map,
and how many slots are open in a party, and can request to join with one click.** **This drives organic
discovery and gives other players a direct path to join in.**

#### Game Invites

**Players can invite Discord friends to join their game session with a single click.** **Invites appear
in Discord and link directly back into your game**, making it easy to **fill a party or share a
session**.

#### Direct Messages

**Players can send direct messages to their Discord friends from inside your game.** **This keeps
communication in context without pulling players out of the experience.**

#### Lobbies and Voice Chat

**The SDK provides lobby-based voice and text chat that your game can create and manage
programmatically.** **Players can talk to each other in a game session, a party, or any grouping your
game defines, using Discord's voice infrastructure without requiring them to have the Discord app open
separately.**

### Cards on this page

Three: **Social SDK Overview** ("Full introduction to the SDK, feature set, and where to start"),
**Core Concepts** ("How the SDK works, key features, and platform compatibility"), **Getting Started**
("Step-by-step guides for C++, Unity, and Unreal Engine").

## Which pages are thin

Recorded so a reader knows what to expect before opening a page upstream. "Thin" here means the page's
own body is a short orientation and its substance lives at the target it names.

| Page | Character |
| --- | --- |
| `platform/bots` | **Thin.** Points at `bots/overview`, `quick-start/getting-started`, `guides/bots`. Its own content: the `APP` tag, the two connection models, five use cases, the bot-versus-webhook comparison. |
| `platform/discovery` | **Thin.** An introduction pointing at the three `discovery/*` pages. Unique content: the two App Directory URLs and the store-page sharing link. |
| `platform/components` | **Thin.** Points at the three `components/*` pages. Unique content: the three component categories and the modal-versus-message-component distinction. |
| `platform/community-servers` | **Thin, and points off the developer docs entirely** — the five features are Discord help centre articles, not API surfaces. |
| `platform/game-profiles` | **Medium.** Four surfaces and the four profile areas; points at `platform/claim-your-game`. |
| `platform/interactions` | **Medium.** Substantive on the four command types and the Gateway/HTTP split; points at the three `interactions/*` pages for the reference. |
| `platform/webhooks` | **Medium.** Substantive on the two-direction distinction; the full event list is at `events/webhook-events`. |
| `platform/server-and-channel-management` | **Medium.** Carries a real permission table; capability lists are explicitly examples. |
| `platform/rich-presence` | **Medium.** Substantive on the SDK choice; both implementation guides are elsewhere. |
| `platform/social-layer` | **Substantive.** Eight named feature areas with descriptions. |
| `platform/claim-your-game` | **Substantive.** A complete six-step procedure with six eligibility requirements and three limitations. |
| `bots/overview` | **Medium.** A real four-step getting-started list and the five building areas. |

## Source

Discord Developer Documentation, retrieved 2026-08-26:
`https://docs.discord.com/developers/platform/bots`,
`https://docs.discord.com/developers/bots/overview`,
`https://docs.discord.com/developers/platform/interactions`,
`https://docs.discord.com/developers/platform/components`,
`https://docs.discord.com/developers/platform/webhooks`,
`https://docs.discord.com/developers/platform/server-and-channel-management`,
`https://docs.discord.com/developers/platform/discovery`,
`https://docs.discord.com/developers/platform/community-servers`,
`https://docs.discord.com/developers/platform/claim-your-game`,
`https://docs.discord.com/developers/platform/game-profiles`,
`https://docs.discord.com/developers/platform/rich-presence`,
`https://docs.discord.com/developers/platform/social-layer`.
