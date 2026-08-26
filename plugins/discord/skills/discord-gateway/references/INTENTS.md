# Gateway Intents

Every intent bit with its value and the exact event list it gates, the privileged intents, the review
process, and the documented alternatives to each privileged intent.

Sources: [Gateway](https://docs.discord.com/developers/events/gateway),
[Getting Started with Privileged Intent Review](https://docs.discord.com/developers/gateway/getting-started-with-privileged-intent-review),
[You Might Not Need a Privileged Intent](https://docs.discord.com/developers/gateway/you-might-not-need-a-privileged-intent),
retrieved 2026-08-26.

## Contents

- [What intents are](#what-intents-are)
- [List of intents](#list-of-intents)
- [Intent footnotes](#intent-footnotes)
- [Caveats](#caveats)
- [Privileged intents](#privileged-intents)
- [Enabling privileged intents](#enabling-privileged-intents)
- [Privileged intent access review](#privileged-intent-access-review)
- [Gateway restrictions](#gateway-restrictions)
- [HTTP restrictions](#http-restrictions)
- [Message content intent](#message-content-intent)
- [Privileged intent review guide](#privileged-intent-review-guide)
- [You might not need a privileged intent](#you-might-not-need-a-privileged-intent)

## What intents are

Maintaining a stateful application can be difficult when it comes to the amount of data your app is
expected to process over a Gateway connection, especially at scale. Gateway intents are a system to
help you lower the computational burden.

Intents are bitwise values passed in the `intents` parameter when Identifying which correlate to a set
of related events. For example, the event sent when a guild is created (`GUILD_CREATE`) and when a
channel is updated (`CHANNEL_UPDATE`) both require the same `GUILDS (1 << 0)` intent. If you do not
specify an intent when identifying, you will not receive *any* of the Gateway events associated with
that intent.

Info: intents are optionally supported on the v6 gateway but required as of v8.

Two types of intents exist:

* **Standard intents** can be passed by default. You don't need any additional permissions or
  configurations.
* **Privileged intents** require you to toggle the intent for your app in your app's settings within
  the Developer Portal before passing said intent. For verified apps (required for apps in 100+
  guilds), the intent must also be approved after the verification process to use the intent.

The connection with your app will be closed if it passes invalid intents (`4013` close code), or a
privileged intent that hasn't been configured or approved for your app (`4014` close code).

## List of intents

Below is the complete upstream list of all intents and the Gateway events associated with them. Any
event *not* listed is not associated with an intent and will always be sent to your app.

```
GUILDS (1 << 0)
  - GUILD_CREATE
  - GUILD_UPDATE
  - GUILD_DELETE
  - GUILD_ROLE_CREATE
  - GUILD_ROLE_UPDATE
  - GUILD_ROLE_DELETE
  - CHANNEL_CREATE
  - CHANNEL_UPDATE
  - CHANNEL_DELETE
  - CHANNEL_PINS_UPDATE
  - THREAD_CREATE
  - THREAD_UPDATE
  - THREAD_DELETE
  - THREAD_LIST_SYNC
  - THREAD_MEMBER_UPDATE
  - THREAD_MEMBERS_UPDATE *
  - STAGE_INSTANCE_CREATE
  - STAGE_INSTANCE_UPDATE
  - STAGE_INSTANCE_DELETE
  - VOICE_CHANNEL_STATUS_UPDATE
  - VOICE_CHANNEL_START_TIME_UPDATE

GUILD_MEMBERS (1 << 1) **
  - GUILD_MEMBER_ADD
  - GUILD_MEMBER_UPDATE
  - GUILD_MEMBER_REMOVE
  - THREAD_MEMBERS_UPDATE *

GUILD_MODERATION (1 << 2)
  - GUILD_AUDIT_LOG_ENTRY_CREATE
  - GUILD_BAN_ADD
  - GUILD_BAN_REMOVE

GUILD_EXPRESSIONS (1 << 3)
  - GUILD_EMOJIS_UPDATE
  - GUILD_STICKERS_UPDATE
  - GUILD_SOUNDBOARD_SOUND_CREATE
  - GUILD_SOUNDBOARD_SOUND_UPDATE
  - GUILD_SOUNDBOARD_SOUND_DELETE
  - GUILD_SOUNDBOARD_SOUNDS_UPDATE

GUILD_INTEGRATIONS (1 << 4)
  - GUILD_INTEGRATIONS_UPDATE
  - INTEGRATION_CREATE
  - INTEGRATION_UPDATE
  - INTEGRATION_DELETE

GUILD_WEBHOOKS (1 << 5)
  - WEBHOOKS_UPDATE

GUILD_INVITES (1 << 6)
  - INVITE_CREATE
  - INVITE_DELETE

GUILD_VOICE_STATES (1 << 7)
  - VOICE_CHANNEL_EFFECT_SEND
  - VOICE_STATE_UPDATE

GUILD_PRESENCES (1 << 8) **
  - PRESENCE_UPDATE

GUILD_MESSAGES (1 << 9)
  - MESSAGE_CREATE
  - MESSAGE_UPDATE
  - MESSAGE_DELETE
  - MESSAGE_DELETE_BULK

GUILD_MESSAGE_REACTIONS (1 << 10)
  - MESSAGE_REACTION_ADD
  - MESSAGE_REACTION_REMOVE
  - MESSAGE_REACTION_REMOVE_ALL
  - MESSAGE_REACTION_REMOVE_EMOJI

GUILD_MESSAGE_TYPING (1 << 11)
  - TYPING_START

DIRECT_MESSAGES (1 << 12)
  - MESSAGE_CREATE
  - MESSAGE_UPDATE
  - MESSAGE_DELETE
  - CHANNEL_PINS_UPDATE

DIRECT_MESSAGE_REACTIONS (1 << 13)
  - MESSAGE_REACTION_ADD
  - MESSAGE_REACTION_REMOVE
  - MESSAGE_REACTION_REMOVE_ALL
  - MESSAGE_REACTION_REMOVE_EMOJI

DIRECT_MESSAGE_TYPING (1 << 14)
  - TYPING_START

MESSAGE_CONTENT (1 << 15) ***

GUILD_SCHEDULED_EVENTS (1 << 16)
  - GUILD_SCHEDULED_EVENT_CREATE
  - GUILD_SCHEDULED_EVENT_UPDATE
  - GUILD_SCHEDULED_EVENT_DELETE
  - GUILD_SCHEDULED_EVENT_USER_ADD
  - GUILD_SCHEDULED_EVENT_USER_REMOVE

AUTO_MODERATION_CONFIGURATION (1 << 20)
  - AUTO_MODERATION_RULE_CREATE
  - AUTO_MODERATION_RULE_UPDATE
  - AUTO_MODERATION_RULE_DELETE

AUTO_MODERATION_EXECUTION (1 << 21)
  - AUTO_MODERATION_ACTION_EXECUTION

GUILD_MESSAGE_POLLS (1 << 24)
  - MESSAGE_POLL_VOTE_ADD
  - MESSAGE_POLL_VOTE_REMOVE

DIRECT_MESSAGE_POLLS (1 << 25)
  - MESSAGE_POLL_VOTE_ADD
  - MESSAGE_POLL_VOTE_REMOVE
```

Bits `1 << 17`, `1 << 18`, `1 << 19`, `1 << 22` and `1 << 23` are not listed upstream; the page is
silent on them.

## Intent footnotes

\* Thread Members Update contains different data depending on which intents are used.

\*\* Events under the `GUILD_PRESENCES` and `GUILD_MEMBERS` intents are turned **off by default on all
API versions**. If you are using **API v6**, you will receive those events if you are authorized to
receive them and have enabled the intents in the Developer Portal. You do not need to use intents on
API v6 to receive these events; you just need to enable the flags. If you are using **API v8** or
above, intents are mandatory and must be specified when identifying.

\*\*\* `MESSAGE_CONTENT` does not represent individual events, but rather affects what data is present
for events that could contain message content fields.

## Caveats

Guild Member Update is sent for current-user updates regardless of whether the `GUILD_MEMBERS` intent
is set.

Guild Create and Request Guild Members are uniquely affected by intents. See those events in
`GATEWAY-EVENTS-GUILDS.md` and `GATEWAY-EVENTS-SEND.md` for the specifics (75k-member and
`large_threshold` behaviour).

Thread Members Update by default only includes if the current user was added to or removed from a
thread. To receive these updates for other users, request the `GUILD_MEMBERS` Gateway Intent.

## Privileged intents

Some intents have additional requirements for access due to the nature of their data. Currently, those
intents include:

* `GUILD_PRESENCES`
* `GUILD_MEMBERS`
* `MESSAGE_CONTENT`

Apps that qualify for verification **must** be approved for the privileged intent(s) before they can
use them. After your app is verified, you can request privileged intents within the app's settings
within the Developer Portal.

Before you can specify any of these privileged intents in your `IDENTIFY` payload, you must enable the
specific privileged intents you need in the Developer Portal.

You may only enable a privileged intent if your use case requires it to function and is consistent with
Discord's Developer Policy.

| Intent              | What it controls                                                                                                                                                                                                                    |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Guild Presences** | Access to presence update events: when users go online/offline, change their status, or update their activity via Rich Presence.                                                                                                     |
| **Guild Members**   | Access to guild member events (joins, updates, leaves) and the ability to request full member lists.                                                                                                                                 |
| **Message Content** | Access to message content fields (`content`, `embeds`, `attachments`, `components`, `poll`) across Gateway events and API responses. Unlike the other two, this isn't tied to specific events; it controls data within message objects everywhere. |

## Enabling privileged intents

Before using privileged intents, you must enable them in your app's settings. In the Developer Portal,
navigate to your app's settings, then toggle the privileged intents on the **Bot** page
(`https://discord.com/developers/applications/select/bot`) under the "Privileged Gateway Intents"
section. You may only toggle privileged intents that your bot requires to function.

## Privileged intent access review

Apps with fewer than 10,000 users can access privileged intents by enabling them in the Developer
Portal.

When an app has more than 10,000 unique users who can see your app across all the servers it's in, it
requires review for continued access to Privileged Intents. Once you hit this threshold, the app or team
owner will receive a system DM and/or an email. There will also be a callout visible on your app in the
Developer Portal. You will need to submit a request with information about your app and its use of
Privileged Intents for review. If access is granted, you can enable the relevant intents for your app
in the Developer Portal and you will be notified annually to reapply for continued access.

## Gateway restrictions

Privileged intents affect which Gateway events your app is permitted to receive. When using **API v8**
and above, all intents (privileged and not) must be specified in the `intents` parameter when
Identifying. If you pass a privileged intent in the `intents` parameter without configuring it in your
app's settings, or being approved for it during verification, your Gateway connection will be closed
with a `4014` close code.

Info: for **API v6**, you will receive events associated with the privileged intents your app has
configured and is authorized to receive *without* passing those intents into the `intents` parameter
when Identifying.

Events associated with the `GUILD_PRESENCES` and `GUILD_MEMBERS` intents are turned off by default
regardless of the API version.

## HTTP restrictions

In addition to Gateway restrictions, privileged intents also affect the HTTP API endpoints your app is
permitted to call, and the data it can receive. For example, to use the List Guild Members endpoint,
your app must enable the `GUILD_MEMBERS` intent (and be approved for it if eligible for verification).

HTTP API restrictions are independent of Gateway restrictions, and are unaffected by which intents your
app passes in the `intents` parameter when Identifying.

## Message content intent

`MESSAGE_CONTENT (1 << 15)` is a unique privileged intent that isn't directly associated with any
Gateway events. Instead, access to `MESSAGE_CONTENT` permits your app to receive message content data
across the APIs.

Any fields affected by the message content intent are noted in the relevant documentation. For example,
the `content`, `embeds`, `attachments`, `components`, and `poll` fields in message objects all contain
message content and therefore require the intent.

Info: like other privileged intents, `MESSAGE_CONTENT` must be approved for your app. After your app is
verified, you can apply for the intent from your app's settings within the Developer Portal. The
message content intent review policy is described in the Discord Help Center article
`support-dev.discord.com/hc/en-us/articles/5324827539479`.

Apps **without** the intent will receive empty values in fields that contain user-inputted content with
a few exceptions:

* Content in messages that an app sends
* Content in DMs with the app
* Content in which the app is mentioned
* Content of the message a message context menu command is used on

## Privileged intent review guide

From "Getting Started with Privileged Intent Review".

Discord gates access to certain data behind Privileged Intents. Currently, there are three of them:

* **Guild Presences**: user online/offline status, activities, and platform info
* **Guild Members**: member join/leave/update events and the ability to list all members in a server
* **Message Content**: the `content`, `embeds`, `attachments`, `components`, and `poll` fields in
  message objects

These intents are disabled by default due to the nature of their data and should only be enabled as
needed. If your app doesn't have them enabled, it simply won't have access to the data they grant.

### What changed as of June 10th, 2026

The upstream page carries an image captioned "Privileged Intents Requirements".

1. **The review threshold is now based on users, not servers.** Previously, apps in fewer than 100
   servers could access Privileged Intents by toggling them on in the Developer Portal, and apps in
   100+ servers needed to apply for access. That threshold is now based on the number of unique users
   who can see your app across all the servers it's in. If that number exceeds 10,000, your app needs
   to apply for Privileged Intent access. This means a bot in 50 large servers could hit the threshold,
   while a bot in 200 small servers might not.
2. **Apps must reapply annually for continued access.** Apps that already have Privileged Intent access
   granted from a prior review must reapply each year through the Developer Portal. You'll receive
   advance notice before your reapplication date.
3. **Apps can continue to use intents and join servers while in review.** While in review for
   privileged intent access, your app will continue to function with the intents you are requesting
   access to, and may continue to grow and join new servers during this time.

### Step 1: figure out where your app stands

Discord counts the number of unique users who have access to your app across all the servers it's
installed in.

* **Under 10,000 users** — you can turn privileged intents on and off from the Developer Portal as
  needed. No need to apply for access. Go to your app's **Bot** page, scroll to **Privileged Gateway
  Intents**, and toggle on what your app needs to function. Even though you *can technically* enable
  these intents, you may only enable what you actually need. Building with the minimum set of intents
  from the start means less work later.
* **Approaching or over 10,000 users** — if your app reaches the 10,000-user threshold and has any
  Privileged Intent enabled (or attempts to enable one), you'll receive a notification in the Developer
  Portal. You will have **90 days** from the date of the notification to apply. Your app can continue
  joining servers and reaching new users while its submission is under review. If you don't apply
  during this window, your app's current Privileged Intents access will be removed, but you can still
  apply at any time to request access again.
* **Access already granted** — you're good for now, but you will need to reapply annually. After you
  receive the notification, you have 90 days to reapply. If access is granted, you will be notified
  before your next annual review. If you don't apply during the 90-day window, access is removed, but
  you can still apply at any time.

### Step 2: audit what privileged intents your app uses

Before applying for anything, take stock of what data your bot actually needs. This is the most
important step, and skipping it is the most common mistake developers make. Review your app to make
sure its use case requires Privileged Intent access and is consistent with the Developer Policy and
Developer Terms of Service.

### Step 3: decide whether to adopt an alternative or apply

**Path A: remove the dependency.** If you can accomplish the same thing without the Privileged Intent,
choose this path. It is also less work in the long run: no review submission, no annual reapplication,
no risk of losing access. Common migrations:

* **Text commands to slash commands** — the most common reason developers request the Message Content
  privileged intent. Slash commands are the recommended replacement and don't require any privileged
  intents.
* **Full member list to on-demand lookups** — if your app caches every server member but only ever
  looks up a few, switch to fetching individual members via the API when you need them.

**Path B: apply for privileged intent access.** If your bot genuinely needs the data for a compliant use
case and there's no alternative, apply. How to set yourself up for success:

* **Be specific about your use case.** "My bot needs message content" is not a justification. "My bot
  provides automated content moderation by scanning messages for phishing links and known scam
  patterns" is a better example. Explain what your bot does with the data and why interactions can't
  replace it.
* **Only request what you need.** If your bot needs Message Content for moderation but doesn't need
  Guild Presences for anything, don't request Guild Presences. Requesting intents you can't demonstrate
  your bot needs hurts your submission.
* **Explain how you handle the data responsibly.** If you're storing the data, explain why it's
  necessary and describe your retention policy and security measures. If you're processing it in memory
  and discarding it, say so.
* **Think about annual review from the start.** Write responses that are easy to understand and update,
  and keep records of how your bot uses the data.
* **Ensure the information you submit is clear, accurate, and complete.** Otherwise it may result in
  review delays or denial of your request.

### Step 4: enable the intent in the Dev Portal and your code

There are **two places you need to enable a privileged intent if you have access**, and missing either
one will throw an error.

1. **The Developer Portal** — select your app, click the **Bot** tab, scroll to **Privileged Gateway
   Intents**, and toggle on the intents you need (and have been granted access for, if review was
   required).
2. **Your code** — enabling the intent in the portal tells Discord your app is *technically allowed* to
   receive the data. You also need to *request* it when your bot connects to the Gateway. How you do
   this depends on your library.

If you enable an intent in your code but not in the portal (or vice versa), you'll get a
`[DisallowedIntents]` error when your app tries to connect (Gateway close code `4014`).

### Step 5: test and verify

1. **Restart your bot.** Intent changes only take effect on a new Gateway connection. A running bot
   won't pick up portal changes until it reconnects.
2. **Check your error logs.** Look for `DisallowedIntents` errors, which mean there's a mismatch
   between your code and your portal settings.
3. **Test affected features.** If you removed a Privileged Intent, make sure the features that depended
   on it still work with their new implementation. If you migrated prefix commands to slash commands,
   verify they're registered and responding correctly.
4. **Test with a second account.** Some things behave differently depending on whether the message
   author is the bot itself. Use a separate Discord account to test interactions as a real user would.

### Common situations and what to do

* **"My bot's commands stopped working"** — if your bot uses prefix commands (like `!help`) and you were
  relying on the Message Content intent, your bot can no longer read the content of messages. It
  receives the `MESSAGE_CREATE` event, but the `content` field is empty, so it never sees the prefix.
  **Fix:** migrate to slash commands.
* **"My welcome messages stopped firing"** — for a bot to send a message in real-time when new members
  join, it needs to be able to receive `GUILD_MEMBER_ADD` events. **Fix:** enable and request the Guild
  Members intent demonstrating the access is required for your app's stated functionality.
* **"I got a DisallowedIntents error"** — your code is requesting an intent that isn't enabled in the
  Developer Portal, or that your bot hasn't been granted access for. **Fix:** check the portal. If the
  toggle is off, turn it on as needed. If your app is over the 10,000 user threshold and the toggle is
  locked, you need to apply for Privileged Intent access.
* **"My intent application was denied"** — requests may be denied when the information provided does not
  demonstrate that the stated use case requires access (e.g. it can be accomplished through interactions
  or other means without privileged intents) or is otherwise not consistent with Discord's requirements
  (e.g. the submission is unclear or incomplete; the described use case violates policy). In many cases
  you may be given additional time to resubmit with updated information or make necessary changes while
  your app retains its current access. In other cases access will be removed but you can still submit a
  new request at any time. **Fix:** re-evaluate whether you truly need the intent. If you do, submit a
  request with more specific and complete information and include evidence (screenshots, video) of the
  feature in action. If the feature can be rebuilt using slash commands, components, modals or other
  alternatives, do that instead and drop the intent request.
* **"I already have access granted, and it's been a year or more"** — you'll receive advance notice when
  it's time to reapply; submit through the same process as the initial application. If you haven't
  received a notice yet and think you are due, wait until you receive the notice.
* **"I'm not sure if I need an intent or not"** — follow the decision checklists below.

## You might not need a privileged intent

From "You Might Not Need a Privileged Intent". The upstream page opens with an image captioned
"Privileged Intents Requirements".

Privileged Intents give your Discord app access to additional data from servers they're added to, which
can be useful when building your app, but they also come with extra review requirements and
responsibility. Before you reach for one, ask yourself: *Do I actually need this?*

Many developers may enable privileged intents out of habit or because a tutorial told them to, only to
later discover that the API offers alternatives that accomplish many of the same goals without the
overhead. Developers may access only the data necessary for their app's functionality.

**Who this applies to:** all apps that are considering or have already enabled privileged intents. Apps
with server-installed user counts fewer than 10,000 can toggle privileged intents in the Developer
Portal. Once your app grows past 10,000 users, you'll need to apply for continued access and share
information about your app and intended use cases for the requested intents. Planning ahead saves you
from a migration later.

### Guild Members intent

**What you get with the intent** — the Guild Members intent unlocks two categories of functionality:

* **Member events via the Gateway:** the `GUILD_MEMBER_ADD`, `GUILD_MEMBER_UPDATE`, and
  `GUILD_MEMBER_REMOVE` events fire when members join, change their profile/roles, or leave a server.
* **Full member list:** the ability to request a complete list of every member in a server via the
  Gateway with the Request Guild Members opcode or the List Guild Members API endpoint.

**What you can do without the intent** — several REST endpoints work **without** the Guild Members
intent:

* **Get Guild Member:** fetch a single member by their user ID. If you know *who* you're looking for,
  you don't need to enumerate every member.
* **Search Guild Members:** search for members by username or nickname prefix. Great for autocomplete,
  lookup commands, or finding specific users.
* **Get User:** get basic user information (username, avatar, etc.) without any guild-specific context.
* **Interaction-provided member data:** when a user triggers a slash command, button, select menu, or
  modal, the API includes the member object in the interaction payload. You get their roles, nickname,
  permissions, and more, with no intent required.

**Decision checklist**

1. Do I need to know about every member, or just specific ones I can look up by ID or search query?
2. Do I need real-time events when members join, leave, or update, or can I fetch member data on demand
   when a user interacts with my bot using interactions?

If your answers lean toward "specific ones" and "on demand", you probably don't need this intent since
the REST API and interaction payloads cover those use cases well.

### Guild Presences intent

**What you get with the intent** — access to `PRESENCE_UPDATE` events, which include:

* `status`: whether the user is online, idle, do not disturb, or offline.
* `activities`: what the user is currently playing, streaming, listening to, or watching (Rich Presence
  data).
* `client_status`: which platform(s) the user is active on (desktop, mobile, web).

**What you can do without the intent** — this data is not available through any other means. Before
building your app, consider whether you actually need this real-time presence data about users.
Endpoints that work without the intent:

* **Get User:** fetch a user's basic profile information (username, avatar, banner) without the intent.
  This covers many "user info" command scenarios.
* **Guild object `approximate_presence_count`:** available on the Guild object via the API. Tells you
  roughly how many members are online without accessing individual presences.
* **Update Bot's Own Status:** setting your bot's own status/activity does not require the Guild
  Presences intent.

**Decision checklist**

1. Does my bot actually do something with presence data, or am I just displaying it in a "user info"
   command?
2. Could I accomplish my goal with `approximate_presence_count` instead of accessing individual users'
   presence?
3. Am I requesting this intent "just in case" or because a core feature depends on it?

### Message Content intent

**What you get with the intent** — control of access to several fields within message objects across
both Gateway events and REST API responses:

* `content`: the text body of the message
* `embeds`: embedded content
* `attachments`: files attached to the message
* `components`: message components (buttons, selects, etc.) sent by users
* `poll`: poll data

Without this intent, these fields will be empty strings or empty arrays when your app receives
messages, with a few important exceptions.

**Exceptions: when you get message content without the privileged intent**

* **Messages your app sends**
* **Direct Messages sent to your app**
* **Messages that @mention your app**
* **Replies to your app's messages.** Note: this applies to replies sent using Discord's reply feature
  to a regular bot message (not an interaction response) and the user has "ping on reply" enabled. It
  does not apply to replies to slash command responses.

If your app's functionality can be built to work with this access, you should not request the Message
Content intent.

**What you can do without the intent** — Discord has built a robust set of interaction primitives
specifically so that most bots don't need access to the Message Content intent:

* **Slash Commands** — the most direct replacement for text commands. Users type `/command` and Discord
  handles argument parsing, validation, and autocomplete for you. Slash commands accept `string`,
  `integer`, `number`, `boolean`, `user`, `channel`, `role`, `mentionable`, and `attachment` option
  types, covering the vast majority of input scenarios.
* **Message Context Menu Commands** — these appear when a user right-clicks (or long-presses) a
  message. Your bot receives the full message object, including its content. Ideal for "act on this
  message" features like reporting, translating, pinning, or saving, without needing to read every
  message in a channel.
* **Message Components** — buttons and select menus let you gather structured user input. Perfect for
  polls, verification systems, role selection, confirmations, and multi-step workflows.
* **Modals with Text Inputs** — pop-up forms that collect freeform text, checkboxes, and other
  structured input from users. Great for forms, applications, feedback collection, or any scenario where
  you need the user to type a specific response.

**Decision checklist**

1. Is my bot using prefix commands (`!help`, `?play`) that could be migrated to slash commands?
2. Could my feature work if users explicitly invoked or interacted with it (i.e. via a command or
   context menu)?
3. Does my bot need to read the content of messages, or does it just need to know that a message was
   sent?
4. Is my bot's intended use case for moderation, and if so, does it provide functionality beyond what is
   possible with the AutoMod API? Providing what the AutoMod API already supports is generally not
   considered a compelling use case for access.

## Source

Discord Developer Documentation:
[Gateway](https://docs.discord.com/developers/events/gateway),
[Getting Started with Privileged Intent Review](https://docs.discord.com/developers/gateway/getting-started-with-privileged-intent-review),
[You Might Not Need a Privileged Intent](https://docs.discord.com/developers/gateway/you-might-not-need-a-privileged-intent),
retrieved 2026-08-26.
