# Discord Developer Platform Change Log — 2024 and later

Every dated entry of the Discord change log from **January 2024 through August 14 2026**, newest
first: 124 entries. Each entry carries its upstream date label, its upstream tags, the upstream RSS
summary, and the full body — every new field, every deprecation, every behavioural change, every
date and every breaking-change note as the upstream states it.

Entries dated before 2024 are in `CHANGELOG-EARLIER.md`.

Source: [Change Log](https://docs.discord.com/developers/change-log), retrieved 2026-08-26.

## Tag vocabulary

The upstream labels every entry with one or more tags. Tags observed across all 227 entries:

| Tag | Entries |
| --- | ---: |
| `Discord Social SDK` | 47 |
| `HTTP API` | 30 |
| `Breaking Change` | 25 |
| `Interactions` | 14 |
| `Activities` | 10 |
| `Embedded App SDK` | 8 |
| `Premium Apps` | 8 |
| `Voice` | 6 |
| `Components` | 5 |
| `User Apps` | 5 |
| `Docs` | 4 |
| `Gateway` | 4 |
| `Documentation` | 1 |
| `Events` | 1 |
| `RPC` | 1 |

99 entries carry no tag.

## Entries

### August 14, 2026

**Tags:** `HTTP API`, `Breaking Change`

**Summary:** Deprecation: Battle.net Connections in Get Current User Connections

Battle.net connections are deprecated and will no longer be returned by the /users/@me/connections endpoint starting September 22, 2026.

#### Deprecation: Battle.net Connections in `Get Current User Connections`

The new Battle.net connection is powered by the [Discord Social SDK](https://docs.discord.com/developers/discord-social-sdk/overview) and application identities. As a result, newly created Battle.net connections are no longer returned by the [`Get Current User Connections`](https://docs.discord.com/developers/resources/user#get-current-user-connections) endpoint (`GET /users/@me/connections`).

Starting September 22, 2026, existing Battle.net connections will also no longer be returned by this endpoint. There is no replacement for this functionality.

### August 13, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.10.18687

Fixed the iOS web-authentication session clobbering the host app's ASWebAuthenticationSession presentation-context delegate during the OAuth flow.

#### Discord Social SDK Release 1.10.18687

A new release of the Discord Social SDK is now available, with the following updates:

##### iOS

* Fixed the iOS web-authentication session overriding `ASWebAuthenticationSession`'s presentation-context delegate, which could clobber the host app's own delegate during the OAuth flow

### August 12, 2026

**Tags:** `Breaking Change`, `Gateway`, `HTTP API`

**Summary:** Channel Obfuscation for Users and Bots

Users will stop receiving full metadata for channels they can't view. Gateway channels are redacted, and GET /guilds/{guild.id}/channels omits them. This becomes mandatory for all bots on November 16, 2026.

#### Channel Obfuscation for Users and Bots

We're changing how users and bots see channels they lack `VIEW_CHANNEL` on.

Today, bots receive every channel in a guild, including ones they can't view, with full metadata over both the Gateway and the HTTP API. Soon, users will be unable to view channels they don't have access to, so we are updating bots to follow the same rule.

* **Over the Gateway**, channels a bot can't view will still be dispatched, but with sensitive fields obfuscated. The channel's `name` becomes `"___hidden___"`, other sensitive fields are nulled or reduced, a new [`CHANNEL_OBFUSCATED` flag](https://docs.discord.com/developers/resources/channel#channel-object-channel-flags) (`1 << 17`) is set on the channel's `flags`, and the `permission_overwrites` will contain a single permission overwrite denying `VIEW_CHANNEL` for the guild's `@everyone` role.
* **Over HTTP**, [`GET /guilds/{guild.id}/channels`](https://docs.discord.com/developers/resources/guild#get-guild-channels) will omit those channels from the response entirely.

A channel stops being obfuscated the moment your bot gains access to it, for example through a permission overwrite change or a role change. When that happens, the Gateway dispatches a [Channel Update](https://docs.discord.com/developers/events/gateway-events#channel-update) event with the channel's full, unobfuscated data. [Interaction](https://docs.discord.com/developers/interactions/receiving-and-responding) payloads are built through a separate path that does not apply obfuscation.

##### Why are we Making This Change?

Channels a user doesn't have access to shouldn't be accessible or visible to that user. This change is happening to respect the privacy of users. Because it's happening for users this means it will also apply to bots.

##### Breaking Change

This affects bots that read data about channels they can't view, such as bots that mirror or audit a server's full channel list, calculate permissions across every channel, or report on channel structure regardless of the bot's own access. If your bot only acts in channels it has permission to view, this change does not affect you.

If your bot manages or organizes channels, see [Obfuscated Channels](https://docs.discord.com/developers/resources/channel#channel-object-obfuscated-channels) for how to detect channels your bot can't see and surface that to users.

##### What Can You Do to Test This Change?

*Figure: Dev portal UI showing the opt-in toggle for private channel obfuscation*

* **Gateway:** If your bot interacts with channels, you can test the obfuscation behavior today by sending `1 << 15` in the `capabilities` field of your [Identify](https://docs.discord.com/developers/events/gateway-events#identify-gateway-capabilities) payload. You can also opt in through the [developer portal](https://discord.com/developers/applications/select/bot) by enabling the **Private Channel Obfuscation** toggle in the **Overview > Bot** tab. This capability and the toggle are temporary and for testing.
* **HTTP:** There is no early opt-in. `GET /guilds/{guild.id}/channels` will start omitting channels that your bot lacks `VIEW_CHANNEL` for on November 16, 2026.

### August 11, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Hotfixes 1.10.18369, 1.9.18337 & 1.8.18335

Hotfix releases across the 1.8, 1.9, and 1.10 branches fixing C# bool marshaling and a PlayStation 5 lobby dispatch crash.

#### Discord Social SDK Hotfix Releases 1.10.18369, 1.9.18337 & 1.8.18335

Hotfix releases of the Discord Social SDK are now available across the 1.8, 1.9, and 1.10 branches, with the following updates:

##### 1.10.18369

###### C\#

* Fixed incorrect marshaling of `bool` values across the C#/native boundary, which could produce garbage data on some platforms (e.g. wrong voice speaking-status indicators on Xbox)

##### 1.9.18337

###### Stability

* Fixed a crash from iterator invalidation in lobby dispatch callbacks, observed on PlayStation 5

###### C\#

* Fixed incorrect marshaling of `bool` values across the C#/native boundary, which could produce garbage data on some platforms (e.g. wrong voice speaking-status indicators on Xbox)

##### 1.8.18335

###### Stability

* Fixed a crash from iterator invalidation in lobby dispatch callbacks, observed on PlayStation 5

###### C\#

* Fixed incorrect marshaling of `bool` values across the C#/native boundary, which could produce garbage data on some platforms (e.g. wrong voice speaking-status indicators on Xbox)

### August 5, 2026

**Tags:** `Interactions`, `Components`

**Summary:** Filter File Types in File Uploads and Attachment Options

File Upload components and ATTACHMENT command options now accept a file_types array that restricts which files a user can upload.

#### Filter File Types in File Uploads and Attachment Options

You can now restrict which files a user is allowed to upload in both [File Upload](https://docs.discord.com/developers/components/reference#file-upload) components and
[`ATTACHMENT`](https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-option-type) command options.

###### Developer Resources

* [File Type Filtering](https://docs.discord.com/developers/reference#file-type-filtering)
* [File Upload Component](https://docs.discord.com/developers/components/reference#file-upload-file-upload-structure)
* [Slash Command Option Structure](https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-option-structure)

### August 5, 2026

**Tags:** `HTTP API`, `Breaking Change`

**Summary:** Channel application_id is Now Nullable

The application_id field on the channel object is now documented as nullable, and will be serialized as null in some cases.

#### Channel `application_id` is Now Nullable

The `application_id` field on the [channel](https://docs.discord.com/developers/resources/channel#channel-object) object is now nullable. For future guild channels, this field can be serialized as `null`. For group DMs, there are no plans to serialize this field as `null`.

Because the field was not previously documented as nullable, this is a slightly breaking change. If your app or library assumes `application_id` is always a snowflake when present, you'll need to update it to handle `null`. The field continues to be optional.

### July 28, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.10.18247

New minimum SDK versions for Xbox and PlayStation 5, Rich Presence over RPC on Android, a repackaged macOS framework, WebRTC M130, and a batch of stability fixes.

#### Discord Social SDK Release 1.10.18247

A new release of the Discord Social SDK is now available, with the following updates:

##### Xbox

* Dropped support for Xbox GDK versions 230600-240605; the new minimum supported GDK version is 241000
* Console integrations can now read a user's presence on Xbox, including a custom status and activity from any application (not just the current game); PlayStation-specific activity is filtered out
* Fixed a crash in the WinRT HTTP client on Xbox when setting restricted headers

##### Playstation 5

* Dropped support for PS5 SDK versions 7.000-9.000; the new minimum supported version is 10.000

##### Android

* Added support for Rich Presence via an unauthenticated RPC transport, matching desktop's existing capability. Games can now publish presence to the signed-in Discord Android client without an OAuth flow.
* Fixed a crash in `AuthenticationActivity` on devices with no browser or Custom Tabs provider capable of handling OAuth

##### iOS

* Fixed a crash when an unsupported URL scheme was passed to the web authorization flow on iOS 26.3

##### macOS

* The macOS SDK is now packaged as `discord_partner_sdk.framework`, with a new signing/notarization pipeline and Krisp bundled inside. This changes how ImGui, Unity, and Unreal integrate and distribute the SDK on macOS.

##### Noise Suppression

* Fixed missing Unity `.meta` files for Krisp libraries, which could break Unity package import/setup

##### WebRTC

* Updated the SDK's base WebRTC version to M130 (up from M116)
* Enabled WebRTC M130 builds for PlayStation 4/5 and Xbox

##### Lobbies

* Added an additional display name field (e.g. a character name) to the lobby message record, readable via `MessageHandle::AdditionalName()`. This must be set server-side by your game backend when adding or updating a lobby member; it cannot be set from the client SDK.

##### Stability

* Fixed a race condition that could crash the SDK when an RPC connection was reused without resetting prior pending state
* Fixed the SDK getting stuck in an infinite reconnect loop after the gateway sent a terminal close code
* Fixed a bug where a timed-out HTTP response could be incorrectly treated as successful, leading to a crash
* Fixed a missing code path that caused every RTC client disconnect to incorrectly trigger voice-backend-version handling
* Fixed a crash from iterator invalidation in lobby dispatch callbacks, observed on PlayStation 5
* Routed the gateway bootstrap request through the shared API client for more reliable connectivity
* Fixed `GetCurrentInputDevice()`/`GetCurrentOutputDevice()` on Linux, which previously always reported the first enumerated device regardless of actual selection

### July 22, 2026

**Tags:** `Discord Social SDK`

**Summary:** Provisional Accounts Documentation Restructure

The Using Provisional Accounts guide has been split into a dedicated Provisional Accounts section, with a focused page for each authentication, merge, and unmerge flow.

#### Provisional Accounts Documentation Restructure

The single **Using Provisional Accounts** guide has been reorganized into a dedicated [Provisional Accounts](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/overview) section, with a focused page for each part of the flow:

* [Overview](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/overview) — core concepts, the account lifecycle, and how to choose an authentication method.
* Creating accounts: [Bot Token Endpoint](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/bot-token-endpoint), [External Credentials Exchange](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/external-credentials-exchange), and [Public Client Integration](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/public-client).
* Reference and lifecycle: [Configuring Identity Providers](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/identity-providers), [Managing Provisional Accounts](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/managing-accounts), [Merging Accounts](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/merging-accounts), and [Unmerging Accounts](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/unmerging-accounts).

The [Bot Token Endpoint](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/bot-token-endpoint) and [Merging Accounts](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/merging-accounts) guides now walk through the full client-to-server integration, with sequence diagrams for each flow.

### July 16, 2026

**Tags:** `Interactions`

**Summary:** Resolved Channel app_permissions in Interactions

Resolved channels in interactions now include the app_permissions field.

#### Resolved Channel `app_permissions` in Interactions

Resolved channel objects in interaction payloads now include an `app_permissions` field containing the bot's permissions in that channel.

This field is only present when the application's bot user is in the guild.

### July 7, 2026

**Tags:** `HTTP API`, `Discord Social SDK`

**Summary:** Deprecation: Riot Games Connections in Get Current User Connections

Riot Games and League of Legends connections are no longer returned by the /users/@me/connections endpoint as part of their migration to the Discord Social SDK.

#### Deprecation: Riot Games Connections in `Get Current User Connections`

The new Riot Games connection is powered by the [Discord Social SDK](https://docs.discord.com/developers/discord-social-sdk/overview) and application identities. As a result, newly created Riot Games connections are no longer returned by the [`Get Current User Connections`](https://docs.discord.com/developers/resources/user#get-current-user-connections) endpoint (`GET /users/@me/connections`).

Starting July 10, 2026, legacy Riot Games and League of Legends connections will also no longer be returned by this endpoint. There is no replacement for this functionality.

### June 30, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.9.17379

Fixed a PlayStation 5 crash caused by re-entrant HTTP requests during connection teardown.

#### Discord Social SDK Release 1.9.17379

A new release of the Discord Social SDK is now available, with the following updates:

##### Stability

* Fixed a crash caused by re-entrant HTTP requests during connection teardown on PlayStation 5.

### June 25, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.9.17228

Fixed an AUTHORIZE_REQUEST re-subscription issue and bundled Krisp noise suppression into the Unity and Unreal plugin packages.

#### Discord Social SDK Release 1.9.17228

A new release of the Discord Social SDK is now available, with the following updates:

##### Authentication

* Fixed an issue where `AUTHORIZE_REQUEST` events would not re-subscribe after Discord disconnected and reconnected while the SDK was already running.

##### Noise Suppression

* Krisp noise suppression binaries and model files are now included in Unity and Unreal plugin packages for Windows, macOS, Android, and iOS.

### June 24, 2026

**Tags:** `HTTP API`

**Summary:** Attachment Editing and is_spoiler Param

Some attachment metadata can now be edited, and the is_spoiler parameter should be used for setting spoiler status.

#### Attachment Editing and `is_spoiler` Param

Apps can now edit the `description` and `is_spoiler` parameters on existing attachments when editing messages.
We have also separated the [attachment request](https://docs.discord.com/developers/resources/message#attachment-object-attachment-request-structure) object in the docs to make it more clear which params you can set for attachments and which fields are provided by the API.

Attachments can be marked as a spoiler by setting `is_spoiler: true` in the attachment request object, and apps can read whether an existing attachment is spoilered by checking for the `IS_SPOILER` [attachment flag](https://docs.discord.com/developers/resources/message#attachment-object-attachment-flags) on the attachment object. The legacy `SPOILER_` filename prefix will continue to mark attachments as a spoiler, but not all spoilered attachments have the prefix.

### June 16, 2026

**Tags:** `HTTP API`

**Summary:** Documentation Fix: Subscription Status Values

Corrected the integer values for the INACTIVE and ENDING subscription statuses, which were swapped in the Subscription reference and the Implementing App Subscriptions guide.

#### Documentation Fix: Subscription Status Values

The integer values for the `INACTIVE` and `ENDING` subscription statuses were previously swapped in the documentation. The correct values are `INACTIVE` = `1` and `ENDING` = `2`, as shown in the [Subscription Statuses](https://docs.discord.com/developers/resources/subscription#subscription-statuses) reference. This has been corrected in both the reference and the [Implementing App Subscriptions](https://docs.discord.com/developers/monetization/implementing-app-subscriptions) guide, which described the subscription lifecycle with the swapped values.

The API has always returned these values, only the documentation was incorrect. If your app branches on the numeric `status` value, double-check that `1` is treated as `INACTIVE` and `2` as `ENDING`.

We discovered this issue while reconciling our documentation against [our OpenAPI spec](https://github.com/discord/discord-api-spec) in [this commit](https://github.com/discord/discord-api-spec/commit/cdbd53a2ac5144536bfee2a34e6d0de13e08eec0).

### June 10, 2026

**Tags:** `HTTP API`, `Gateway`

**Summary:** Changes to Privileged Intent Access for Discord Apps

Changes to the review threshold for privileged intent access, an annual reapplication process for continued access, and the ability for apps to keep growing during review.

#### Changes to Privileged Intent Access for Discord Apps

*Figure: Privileged Intents Requirements*

Today, we're [announcing changes to how Discord Apps access Privileged Intent](https://support-dev.discord.com/hc/articles/40281523410967) with a new user-based threshold for when access requires review and an annual process to reapply for continued access.

> If your app is accessible to fewer than 10,000 users, these changes do not impact your app.

##### What's Changing

###### 1. The review threshold is now based on user count, not server count

Previously, apps in fewer than 100 servers could access Privileged Intents by toggling them on in the Developer Portal, and apps in 100+ servers needed to apply for access.

Starting today, the threshold is based on the number of users your app can access across all the servers it belongs to. If your app has fewer than 10,000 users, you can continue accessing Privileged Intents by toggling them on in the Developer Portal. **Once your app reaches 10,000 users, you'll need to apply for Privileged Intent access**.

###### 2. Apps must now reapply annually for continued access

Apps with Privileged Intent access granted from a prior review will need to reapply to confirm their continued access once per year in the Developer Portal.

###### 3. Apps can keep growing during Privileged Intent review

Under the new user-based threshold, apps can continue joining servers and reaching new users while their submission is under review.

###### 4. App Verification and Privileged Intent review are now separate

Previously, [App Verification](https://support-dev.discord.com/hc/en-us/articles/23926564536471-How-Do-I-Get-My-App-Verified) and Privileged Intent review were part of the same review process. With this change, we have separated App Verification and the Privileged Intent review process.

*Figure: Privileged Intents Requirements*

##### What This Means For Your App

For more information on how this applies to your Discord Apps, please read the [Privileged Intents Change announcement article](https://support-dev.discord.com/hc/articles/40281523410967) in our developer help center.

##### Updated Documentation & Resources

* Updated [Privileged Intents documentation](https://docs.discord.com/developers/events/gateway#privileged-intents) to reflect the new threshold and review process.
* New [Getting Started with Privileged Intents Review](https://docs.discord.com/developers/gateway/getting-started-with-privileged-intent-review) guide.
* New [You Might Not Need a Privileged Intent](https://docs.discord.com/developers/gateway/you-might-not-need-a-privileged-intent) guide to help you determine whether you need a privileged intent or whether an alternative approach will work for your use case.

### June 3, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.9.16441

Fixed a PlayStation 5 crash caused by a use-after-free in WebSocket callbacks.

#### Discord Social SDK Release 1.9.16441

A new release of the Discord Social SDK is now available, with the following updates:

##### Playstation 5

* Fixed crash caused by use-after-free in WebSocket callbacks

### June 3, 2026

**Tags:** `Discord Social SDK`, `HTTP API`

**Summary:** New Lobby HTTP API Endpoints

Reference documentation added for create-or-join, send/get messages, and linked-channel invite endpoints on the Lobby resource.

#### New Lobby HTTP API Endpoints

We've expanded the Discord [Lobby resource](https://docs.discord.com/developers/resources/lobby) reference with several public endpoints:

* **[Create or Join Lobby](https://docs.discord.com/developers/resources/lobby#create-or-join-lobby)** (`PUT /lobbies`) — create a lobby for your application or join an existing one by `secret` in a single call.
* **[Send Lobby Message](https://docs.discord.com/developers/resources/lobby#send-lobby-message)** (`POST /lobbies/{lobby.id}/messages`) — send a message into a lobby on behalf of an authenticated member.
* **[Get Lobby Messages](https://docs.discord.com/developers/resources/lobby#get-lobby-messages)** (`GET /lobbies/{lobby.id}/messages`) — fetch up to 200 of the most recent messages from a lobby the calling user is a member of.
* **[Create Lobby Channel Invite for Self](https://docs.discord.com/developers/resources/lobby#create-lobby-channel-invite-for-self)** and **[for User](https://docs.discord.com/developers/resources/lobby#create-lobby-channel-invite-for-user)** — generate a single-use, one-hour guild invite to a lobby's linked channel.

### May 26, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release Cadence & Support

New release cadence and support lifecycle taking effect with the 1.10 release in July 2026: a 5-version support window (1.6–1.10), and a rolling 18-month console OS SDK window where new Xbox and PlayStation SDKs ship only in new Social SDK releases.

#### Discord Social SDK Release Cadence & Support

We've published a new [Release Cadence & Support](https://docs.discord.com/developers/discord-social-sdk/core-concepts/release-cadence-and-support) page for the Discord Social SDK. It documents:

* Our new three-per-year minor release cadence (April, July, November)
* A new support window covering the five most recent minor versions, with hotfix patches (bug fixes and security fixes) for older supported minor releases
* How new Xbox and PlayStation OS SDK supports ship in new Social SDK releases only — each release bundles roughly the last 18 months of console OS SDKs
* The new end-of-life process for older minor releases

##### What this means for you

* **Over a year and a half of support per minor release.** Three minor releases of the Social SDK per year combined with a 5-version support window means every minor release you ship with gets more than 18 months of patch coverage.
* **A predictable release calendar.** Releases land in April, July, and November, so you can plan Social SDK upgrades and console certification windows well in advance.
* **More bandwidth for new features and stability.** A defined support window lets us focus engineering effort where it matters most, which means more capacity to build new features in current minor releases and keep the versions in the support window robust and reliable.

##### What changes with 1.10

These changes take effect with the 1.10 release, shipping in **July 2026**:

* The supported version window will cover versions **1.6 through 1.10**. Versions **1.5 and earlier** will be end-of-life and no longer eligible for patch updates.
* **New Xbox and PlayStation OS SDK support will ship in new Social SDK releases only**, not as patches to older Social SDK versions. Each Social SDK release will bundle roughly the last 18 months of console OS SDK versions.

**Already-shipped Social SDK releases (1.6–1.9) are unchanged** — they keep the console OS SDK support they were originally built with. The new model applies from 1.10 forward.

We're sharing this ahead of the 1.10 release so developers on older versions have plenty of time to upgrade.

### May 22, 2026

**Tags:** `Discord Social SDK`

**Summary:** Account Linking Failure-Mode Documentation

New documentation covering what happens when a Discord account is banned, when OAuth2 tokens are revoked, and how to design account linking for resilience.

#### Account Linking Failure Modes

We've expanded documentation across the Social SDK guides to cover what happens when the Discord-to-game account link is severed — whether by a Discord account ban, an explicit unmerge, or an OAuth2 token revocation. Highlights:

* **[Ban-Driven Unmerge](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/unmerging-accounts#ban-driven-unmerge)** documents the full lifecycle when a user's Discord account is banned: tokens are deleted immediately, a new cross-platform-restricted provisional account is created carrying the original external identity, and merge attempts return error [`530017`](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/merging-accounts#merge-request-failures) until the ban lifts (or, for permanent bans, indefinitely).
* **[Out-of-Band Revocation](https://docs.discord.com/developers/discord-social-sdk/development-guides/account-linking-with-discord#out-of-band-revocation)** describes the auth-side observable signals (`APPLICATION_DEAUTHORIZED` webhook + `invalid_grant` on refresh) when a user removes your app from Discord or has their account banned.
* **[When Refresh Fails](https://docs.discord.com/developers/discord-social-sdk/development-guides/account-linking-with-discord#when-refresh-fails)** documents the `/oauth2/token` response when the underlying token has been deleted, and recommends treating `invalid_grant` as equivalent to receiving the webhook.

### May 12, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.9.15780

Xbox GDK 260400 support and Krisp noise suppression integration across Android, iOS, macOS, and Windows.

#### Discord Social SDK Release 1.9.15780

A new release of the Discord Social SDK is now available, with the following updates:

##### Xbox

* Added Xbox GDK 260400 support

##### Noise Suppression

* Integrated Krisp noise suppression across Android, iOS, macOS, and Windows

### May 7, 2026

**Tags:** `HTTP API`

**Summary:** New flags_new Field on Application Object

The Application object now includes a `flags_new` field, a string-serialized integer containing all application flag bits including those beyond 32-bit precision.

#### New `flags_new` Field on Application Object

The [Application object](https://docs.discord.com/developers/resources/application#application-object) now includes a `flags_new` field — a string-serialized integer containing the full set of [application flag bits](https://docs.discord.com/developers/resources/application#application-object-application-flags), including any new flag bits introduced beyond bit 30.

The existing `flags` field continues to be serialized as a 32-bit integer. Existing integrations consuming `flags` for bits at or below `2^30` are not impacted, and request payloads that include flag values should continue to use the original `flags` field.

This mirrors the [`permissions_new` / `allow_new` / `deny_new`](https://docs.discord.com/developers/topics/permissions) pattern previously introduced for permission bitfields.

### May 5, 2026

**Tags:** `HTTP API`

**Summary:** User Premium Type Field Now Requires A Scope

The `premium_type` field on the User object now requires the `identify.premium` scope to return a user's Nitro subscription level.

#### User Premium Type Field Now Requires A Scope

The `premium_type` field on the [User object](https://docs.discord.com/developers/resources/user#user-object-user-structure) will return `0` for applications that have not been approved for the `identify.premium` scope. To receive Nitro subscription level, you must request the `identify.premium` scope during OAuth authorization. Without this scope, the field returns `0` regardless of the user's actual subscription status.

The `identify.premium` scope is only available to approved partners.

### April 24, 2026

**Tags:** `Discord Social SDK`, `HTTP API`

**Summary:** Voice Muting Based on Player Blocks Guide

New how-to guide for implementing bi-directional voice muting in lobby voice calls based on block relationships, with client-side and server-side approaches.

#### Voice Muting Based on Player Blocks

We've published a new how-to guide covering how to implement bi-directional voice muting in lobby voice calls based on block relationships. The guide covers two approaches for populating per-member mute lists — client-side using any client-accessible block signal (Discord relationships, in-game block lists, etc.) and server-side via lobby member metadata set at lobby creation — and a shared client-side implementation that applies mutes in both directions.

As part of this work, we've also documented the [`POST /lobbies/{lobby.id}/members/bulk`](https://docs.discord.com/developers/resources/lobby#bulk-update-lobby-members) endpoint, which allows adding, updating, or removing up to 25 lobby members in a single request.

[Voice Muting Based on Player Blocks](https://docs.discord.com/developers/discord-social-sdk/how-to/voice-muting-for-blocked-players)

### April 23, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.9.15332

PlayStation 5 OS 13.000 support and activity invite fix for Publisher Level Account Linking.

#### Discord Social SDK Release 1.9.15332

A new release of the Discord Social SDK is now available, with the following updates:

##### Playstation 5

* Added OS 13.000 support

##### Activity Invites

* Accepting an activity invite over RPC now uses the `application_id` from the invite when provided, fixing cases where invites from sibling applications were sometimes attributed to the wrong app. This only affects teams leveraging Publisher Level Account Linking for having a single auth flow across all the games in their portfolio.

### April 23, 2026

**Tags:** `Discord Social SDK`

**Summary:** Proximity Voice Chat Guide for Game Developers

New guide on how to intercept Discord Social SDK voice audio and route it to Unity's 3D audio system to build proximity voice chat for multiplayer games.

#### Proximity Voice Chat Guide for Game Developers

We've published a new guide on adding proximity voice chat to a multiplayer game using the Discord Social SDK and Unity. The guide walks through the general architecture and the concepts are adaptable to any game or engine.

[Add proximity voice chat to your game](https://docs.discord.com/developers/game-development/how-to-add-proximity-voice-chat-to-your-game)

### April 22, 2026

**Tags:** `Discord Social SDK`

**Summary:** Security Updates for Provisional Account OIDC Integrations

Recent security improvements to provisional account OIDC issuer validation are now documented. Existing integrations are unaffected, but review the new requirements before editing your configuration.

#### Security Updates for Provisional Account OIDC Integrations

We've made security improvements to how Discord validates OIDC issuer URLs and fetches OIDC configuration for [provisional accounts](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/overview) — including stricter hostname checks and blocking HTTP redirects during configuration and JWKS discovery.

**Existing provisional account OIDC integrations are not affected** and will continue to work without any changes on your part.

However, if you need to edit your OIDC configuration in the [Developer Portal](https://discord.com/developers/applications/select/social-sdk/external-auth-providers), your updated configuration will be validated against these requirements. We've published new documentation covering the full set of [OIDC Integration Requirements](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/identity-providers#oidc-integration-requirements) — including issuer URL rules, discovery document requirements, supported signing algorithms, and ID token claims. Before making any changes to a production integration, review those requirements and verify your configuration works in a test application first.

### April 20, 2026

**Tags:** `Documentation`

**Summary:** Voice Channel Status and Start Time Documentation

Documentation for Set Voice Channel Status endpoint, permission, and related Gateway and audit log events.

#### Voice Channel Status and Start Time Documentation

Voice channel status has been available for some time, but we're now officially documenting the endpoint, permission, and related Gateway and audit log events so apps can integrate with it.

The [Set Voice Channel Status](https://docs.discord.com/developers/resources/channel#set-voice-channel-status) endpoint (`PUT /channels/{channel.id}/voice-status`) allows apps to set a short string (up to 500 characters) describing what's happening in a voice channel.

##### Permission

Setting a channel's status requires the `SET_VOICE_CHANNEL_STATUS` permission (`1 << 48`), now documented in the [permissions](https://docs.discord.com/developers/topics/permissions) table. If the bot user is not connected to the voice channel, the `MANAGE_CHANNELS` permission is additionally required.

##### Gateway Events

Voice channel status and voice session start time are ephemeral and are not included on the [channel](https://docs.discord.com/developers/resources/channel#channel-object) object. To read them, apps send the [Request Channel Info](https://docs.discord.com/developers/events/gateway-events#request-channel-info) Gateway command (opcode `43`) and receive a [Channel Info](https://docs.discord.com/developers/events/gateway-events#channel-info) event containing the requested fields (currently `status` and `voice_start_time`) for channels in the guild.

Two receive events are dispatched when these fields change:

* [Voice Channel Status Update](https://docs.discord.com/developers/events/gateway-events#voice-channel-status-update) — fired when a channel's status changes.
* [Voice Channel Start Time Update](https://docs.discord.com/developers/events/gateway-events#voice-channel-start-time-update) — fired when a voice session's start time changes.

##### Audit Log

Two [audit log events](https://docs.discord.com/developers/resources/audit-log#audit-log-events) track status changes: `VOICE_CHANNEL_STATUS_UPDATE` (`192`) and `VOICE_CHANNEL_STATUS_DELETE` (`193`). A `status` field in [Optional Audit Entry Info](https://docs.discord.com/developers/resources/audit-log#audit-log-entry-object-optional-audit-entry-info) carries the new status on `VOICE_CHANNEL_STATUS_UPDATE` entries.

### April 16, 2026

**Tags:** `Discord Social SDK`

**Summary:** Deprecation: OAuth2 Refresh Token Grant for OIDC Provisional Accounts

Using the OAuth2 refresh_token grant to refresh OIDC server-side provisional account tokens is deprecated. Re-authenticate using a fresh provider token instead.

#### Deprecation: OAuth2 Refresh Token Grant for OIDC Provisional Accounts

If you are using [OIDC server-side authentication](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/external-credentials-exchange#server-authentication-with-external-credentials-exchange)
for provisional accounts, a `refresh_token` is returned — but using it via the OAuth2 `refresh_token` grant is now
deprecated.

This brings OIDC in line with all other provisional account authentication methods: when the token
expires, re-authenticate using a fresh provider token and pass the new access token to [`Client::UpdateToken`].

See the [Refreshing Access Tokens](https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/managing-accounts#refreshing-access-tokens)
section for details.

[`Client::UpdateToken`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a606b32cef7796f7fb91c2497bc31afc4

### April 14, 2026

**Tags:** `HTTP API`

**Summary:** Message Forwarding Requires Message Content Access

Starting today, applications must be able to read a message's content in order to forward it.

#### Message Forwarding Requires Message Content Access

Starting today, applications must be able to read a message's content in order to forward it.

An application attempting to forward a message it cannot read will now receive error code `160014` with the message "You cannot forward a message whose content you cannot read."

Most applications will not be affected by this change, but those recently affected have been notified directly via system DM.

### April 6, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.8.14985

Xbox GDK 251002 support.

#### Discord Social SDK Release 1.8.14985

A new release of the Discord Social SDK is now available, with the following updates:

##### Xbox

* Added Xbox GDK 251002 support

### April 3, 2026

**Tags:** `RPC`

**Summary:** RPC over IPC Documentation

Documentation for RPC over IPC transport is now available, covering connection, opcodes, and IPC-specific events.

#### RPC over IPC Documentation

Documentation for Discord's RPC over IPC (Inter-Process Communication) transport is now available. IPC is a transport for native applications to communicate with a local Discord client, offering high-performance local communication without network overhead.

The [RPC documentation](https://docs.discord.com/developers/topics/rpc) covers:

* IPC socket paths for Windows and Linux/macOS
* Handshake flow and opcodes
* IPC-specific events (`READY`, `ERROR`, and `GUILD_STATUS`)

> **Note**
> If you're building a game that integrates Discord social features, we recommend using the [Discord Social SDK](https://docs.discord.com/developers/discord-social-sdk/overview) instead of communicating directly over RPC.

### March 27, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.8.14856

Debug plugins for iOS Unity & Unreal, and fix for party privacy settings not propagating.

#### Discord Social SDK Release 1.8.14856

A new release of the Discord Social SDK is now available, with the following updates:

##### iOS Unity & Unreal

* Unity and Unreal packages now include Debug plugins, which have support for logging at the Info and Verbose severity levels

##### Party Privacy

* Fixed bug in which changes to party privacy settings didn't propagate when calling [`Client::UpdateRichPresence`], meaning switching a party from private to public wouldn't update the join button in Discord

### March 19, 2026

**Tags:** `HTTP API`

**Summary:** Search Guild Messages Endpoint

Search Guild Messages endpoint allows bots to search for messages within a guild using various filters and sorting options

#### Search Guild Messages

We've added documentation for the [Search Guild Messages](https://docs.discord.com/developers/resources/message#search-guild-messages) endpoint, which allows bots to search for messages within a guild using a variety of filters.

The endpoint supports filtering by content, author, channel, mentions, attachments, embeds, and more. Results can be sorted by timestamp or relevance.

This endpoint requires the `READ_MESSAGE_HISTORY` permission and the `MESSAGE_CONTENT` [Privileged Intent](https://docs.discord.com/developers/events/gateway#privileged-intents).

The error code `110000` has been added to the [error codes](https://docs.discord.com/developers/topics/opcodes-and-status-codes#json) table to reflect the index-not-ready response returned when a guild has not yet been indexed for search.

### March 15, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.8.14587

Debug library support for Unity, Unreal, Windows, Mac, Linux, Android, PS5, PS4, and Xbox.

#### Discord Social SDK Release 1.8.14587

A new release of the Discord Social SDK is now available, with the following updates:

##### Debug Support

* Added Debug library support for the following:
  * Unity plugin & sample
  * Unreal plugin & sample
  * Windows, Mac, Linux libraries
  * Android library
  * PS5 11.000 & 12.000 library
  * PS4 12.000 & 12.500 library
  * Scarlett & Xbox One 250400 GDK library

### March 9, 2026

**Tags:** `Docs`

**Summary:** Developer Portal & Docs Refresh

New home page, UI redesign, new developer guides, and improved docs navigation.

#### Developer Portal & Docs Refresh

The Developer Portal and Developer Docs have both been updated with improved navigation, usability, and a redesigned theme, with more developer experience improvements on the way. Latest changes include:

##### Developer Portal

* **New [dev portal home page](https://discord.com/developers/home)** with quick access to apps, docs, and new developer videos.
* **New theme** with updated navigation and updated light/dark support.
* **New Localization support!** This will use the same language you have set in the Discord client.

##### Developer Docs

* **Reorganized structure** with new tabs for each feature area and new sidebars for easier navigation.
* **New guides and overviews** for platform-wide features and use cases, with more on the way!
* **AI & MCP support:** Docs now work with AI development tools via Copy-as-Markdown, an LLMs.txt file, and an MCP server, available at `https://docs.discord.com/mcp`
* **Existing docs URLs** are stable and were preserved during the reorganization. Some titles and content were updated or moved for clarity.

##### What's Next

We are working on more improvements for the portal and docs. We invite you to share any issues or feedback in the [Next Gen Docs discussion thread](https://github.com/discord/discord-api-docs/discussions/categories/next-gen-docs-feedback).

### March 5, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.8.14437

Bearer token filtering, log level changes, debug warning.

#### Discord Social SDK Release 1.8.14437

A new release of the Discord Social SDK is now available, with the following updates:

##### Security

* Filter the bearer token in all levels of logging
* Release builds only emit log statements for Error or Warning levels of severity
* Debug builds will still have logs for Info and Verbose levels of severity
* Added a DEBUG BUILD Warning at the top of the debug log that indicates it should not be used in production

### March 5, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.7.14433

Bearer token filtering, log level changes, debug warning.

#### Discord Social SDK Release 1.7.14433

A new release of the Discord Social SDK is now available, with the following updates:

##### Security

* Filter the bearer token in all levels of logging
* Release builds only emit log statements for Error or Warning levels of severity
* Debug builds will still have logs for Info and Verbose levels of severity
* Added a DEBUG BUILD Warning at the top of the debug log that indicates it should not be used in production

### March 5, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK 1.6.14448

Bearer token filtering, log level changes, debug warning.

#### Discord Social SDK Release 1.6.14448

A new release of the Discord Social SDK is now available, with the following updates:

##### Security

* Filter the bearer token in all levels of logging
* Release builds only emit log statements for Error or Warning levels of severity
* Debug builds will still have logs for Info and Verbose levels of severity
* Added a DEBUG BUILD Warning at the top of the debug log that indicates it should not be used in production

### March 3, 2026

**Tags:** `Interactions`

**Summary:** Updates to Context Menu Commands

New UI for User Commands and Message Commands with increased limits and improved organization

#### Updates to Context Menu Commands

We've redone the UI for [User Commands](https://docs.discord.com/developers/interactions/application-commands#user-commands) and [Message Commands](https://docs.discord.com/developers/interactions/application-commands#message-commands) to make it easier to find commands and unlock higher limits!

###### Refreshed UI

The UI has been updated based on feedback! No longer do you have to scroll through a long list of commands:

* Commands are now organized by their application, providing hierarchy
* Frequently used commands are now hoisted to the top for easy access
* A new search bar lets you quickly find the exact command you're looking for

###### A Higher Limit

We've heard your feedback about the 5 command limit feeling too restrictive! With this new UI, we have increased the limit to 15 per type, providing breathing room for your app.

###### Developer Resources

Check out the [Application Commands](https://docs.discord.com/developers/interactions/application-commands) page for details on all command types.

### February 20, 2026

**Tags:** `Discord Social SDK`, `HTTP API`, `Docs`

**Summary:** Server-Side Message Moderation

New API endpoints for modifying moderation metadata on game direct messages and lobby messages

#### Server-Side Message Moderation

We've released and documented two new API endpoints that enable you to modify the application-scoped moderation metadata on
both game direct messages and lobby messages.

Combined with the [previously announced](https://docs.discord.com/developers/change-log#discord-social-sdk-release-1813395) [`MessageHandle::ModerationMetadata`], and game direct message and lobby [Webhook Events](https://docs.discord.com/developers/events/webhook-events#event-types),
this enables server-side lobby and game direct message moderation workflows. Your game backend can now evaluate messages and attach moderation metadata that the Discord Social SDK can then deliver to game clients in real time, driving in-game message rendering dependent on moderation results.

To see this in detail, have a look at the newly updated [How To Integrate Moderation](https://docs.discord.com/developers/discord-social-sdk/how-to/integrate-moderation) guide with the full server-side moderation flow.

### February 19, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.8.14026

Fixed an occasional crash when linking Discord account while in a Voice Call

#### Discord Social SDK Release 1.8.14026

A new release of the Discord Social SDK is now available, with the following updates:

##### Stabilization

* Fixed an occasional crash when linking your Discord account to your Application while in a Voice Call

### February 18, 2026

**Tags:** `Discord Social SDK`, `Docs`

**Summary:** Publisher Level Account Linking

New documentation for Publisher Level Account Linking, enabling single authorization flow across game portfolios

#### Publisher Level Account Linking

We've published new documentation for **Publisher Level Account Linking**, a feature that enables game publishers with multiple titles to implement a single authorization flow across their entire game portfolio.

> **Note**
> Publisher Level Account Linking requires Discord approval.
>
> To inquire about access, speak to your Discord account representative or [contact us](https://discord.com/developers/contact-us)

With Publisher Level Account Linking, players authenticate once through a publisher application instead of separately for each game. This creates a simplified experience for players while giving publishers centralized account management capabilities.

Key features covered in the guide:

* Setting up parent-child application hierarchies between publisher and game applications
* Exchanging parent access tokens for child access tokens
* Integrating child tokens with the Discord Social SDK
* Understanding token lifecycles and revocation

To learn more and get started, check out the [Publisher Level Account Linking guide](https://docs.discord.com/developers/discord-social-sdk/development-guides/publisher-level-account-linking).

### February 12, 2026

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.8.13870

Added PS5 OS 12.000 support and iOS code stripping for reduced build size

#### Discord Social SDK Release 1.8.13870

A new release of the Discord Social SDK is now available, with the following updates:

##### Playstation 5

* Added OS 12.000 support

##### iOS

* Added code stripping to iOS builds to reduce size

### February 12, 2026

**Tags:** `HTTP API`

**Summary:** Community Invite Guide

New guide showcasing invite endpoints with examples for creating invites with roles and restricting access

#### Community Invite Guide

We're launching a guide to showcase the new [invite endpoints](https://docs.discord.com/developers/change-log#new-invite-endpoints) and functionality. It has examples on how to create invites with roles through the UI and API and how to restrict access to an invite using `target_users` through the API. This guide highlights use cases for community servers and walks through steps for creating and sending invites that grant roles or restrict access to specific users.

[Check out the new guide here!](https://docs.discord.com/developers/tutorials/using-community-invites)

### February 12, 2026

**Tags:** `Interactions`, `Components`

**Summary:** Radio Groups, Checkbox Groups, and Checkboxes in Modals

Three new modal components for single-choice selections, multi-select options, and boolean toggles

#### Radio Groups, Checkbox Groups, and Checkboxes in Modals

We're introducing three new modal components: **Radio Groups**, **Checkbox Groups**, and **Checkboxes**. These components expand the ways users can interact with your app through modals, enabling single-choice selections, multi-select options, and simple yes/no toggles.

###### The New Components

* [**Radio Group**](https://docs.discord.com/developers/components/reference#radio-group): A single-selection component for choosing exactly one option from a list. Supports the `required` field to allow optional selections.
* [**Checkbox Group**](https://docs.discord.com/developers/components/reference#checkbox-group): A multi-selection component with configurable `min_values` and `max_values` constraints for flexible selection requirements.
* [**Checkbox**](https://docs.discord.com/developers/components/reference#checkbox): A simple boolean toggle for yes/no style questions.

All three components must be placed inside a [**Label**](https://docs.discord.com/developers/components/reference#label) component and are only available in modals.

###### Developer Resources

* [Using Modal Components](https://docs.discord.com/developers/components/using-modal-components) - Learn how to create modals
* [Component Reference](https://docs.discord.com/developers/components/reference) - Complete documentation for all available components

### February 10, 2026

**Tags:** `Docs`

**Summary:** Next Generation Docs Project

Launch of the Next Gen Docs project with migration to Mintlify and improved developer experience

#### Next Generation Docs Project

We're excited to announce the launch of our Next Gen Docs project! This initiative aims to improve the way developers interact with Discord's developer documentation, making it more accessible, comprehensive, and user-friendly.

#### Our Goal

The Discord API has evolved far beyond its origins as a platform for bots. Today, we're a comprehensive developer platform supporting:

* **Discord Apps and Bots** - The foundation of our ecosystem, extending Discord's functionality with custom apps, commands, and integrations
* **Discord Activities** - Real-time games and social experiences that users can launch directly inside Discord
* **Social SDK for Games** - Bringing Discord-powered features like voice, chat, rich presence, and social graph to games

Our documentation needs to evolve with us. With this project, we're not just updating our docs. We're aiming to improve the entire developer experience for learning and building on Discord as it exists in 2026 and beyond.

#### Our Next Gen Docs Journey

**What we've done so far:**

* Migrated to [Mintlify](https://mintlify.com) for a modern documentation experience
* For this migration, we preserved our existing content and familiar design but plan to evolve this over time
* We no longer have to maintain and build our own documentation platform and can instead focus on making content and improving our developer experience
* Gained new capabilities:
  * **PR Previews** - See documentation changes before they go live! This works locally as well as in your pull requests
  * **More Components and Docs Features** - We now have access to all of Mintlify's documentation components that will continue to grow over time
  * **AI features & improved search** - You can now send our docs to your LLM of choice or access them via MCP (more on this soon!)

If you're reading this, the migration is complete! 🎉

> **Warning**
> This migration did require us to reorganize the entire repository and make a lot of formatting changes. If you have an open PR, it will be a pretty gnarly merge conflict to resolve. We will be focusing on getting our PR backlog down over the next few weeks.

> **Info**
> We combed through the existing documentation to ensure everything was migrated correctly, but if you spot anything that looks off, please let us know by opening an issue or submitting feedback [here](https://github.com/discord/discord-api-docs/discussions/categories/next-gen-docs-feedback). We will be actively monitoring feedback to quickly address any issues.

#### Why This Matters

Great documentation isn't just about having the right information, it's about presenting it in a way that helps developers succeed.

In the coming months, we'll be shipping changes to our documentation to ensure that it:

* **Reduces time-to-first-success** for new developers
* **Scales with complexity** as your projects grow
* **Stays current** with our rapidly evolving platform
* **Serves all skill levels** from beginners to experts

#### Contributing to Our Vision

This transformation is happening with the developer community at its heart. We welcome:

* **Feedback** on what's working and what isn't
* **Content contributions** through our existing PR process
* **Bug reports** when documentation doesn't match reality

We have created a Github Discussion topic for [Next Gen Docs Feedback](https://github.com/discord/discord-api-docs/discussions/categories/next-gen-docs-feedback) to collect feedback.

See our [Contributing Guidelines](https://github.com/discord/discord-api-docs/blob/main/CONTRIBUTING.md) for how to get involved.

### February 05, 2026

**Tags:** `HTTP API`, `Breaking Change`

**Summary:** Community Invites Update

Updated community invite endpoints with security-related changes to target users and channel invites

#### Community Invites Update

We've updated the community invite endpoints with two changes due to a security concern:

* [Get Target Users](https://docs.discord.com/developers/resources/invite#get-target-users) returns a standardized CSV file with a header `user_id` and each user ID on its own line. If you relied on the header you submitted or weren't reading it from the file you got back you'll need to update to expect only `user_id` as the header in the csv now.
* [Get Channel Invites](https://docs.discord.com/developers/resources/channel#get-channel-invites) returns a partial for [roles](https://docs.discord.com/developers/topics/permissions#role-object) instead of the full role object. This is a breaking change as it used to return the full role object and now only contains `id`, `name`, `position`, `color`, `colors`, `icon`, and `unicode_emoji`.

### January 21, 2026

**Tags:** `Activities`, `Embedded App SDK`

**Summary:** Relationships.read Scope for Activities

The relationships.read scope is now available for Activities under Social SDK terms

#### Relationships.read scope

We've opened up the `relationships.read` scope for Activities under the [Social SDK terms](https://support-dev.discord.com/hc/en-us/articles/30225844245271-Discord-Social-SDK-Terms). To get access to the scope you will need to accept the Social SDK terms for your app in the [Social SDK settings](https://discord.com/developers/applications/select/social-sdk/getting-started). Requesting approval for this scope from Discord is no longer necessary. With this scope `getRelationships()` in the embedded app SDK will now return a player's relationships.

The Embedded App SDK is available via [npm](https://www.npmjs.com/package/@discord/embedded-app-sdk) and [GitHub](https://github.com/discord/embedded-app-sdk). You can check out our [installation guide and reference](https://docs.discord.com/developers/developer-tools/embedded-app-sdk) to get started with it!

### January 13, 2026

**Tags:** `HTTP API`

**Summary:** New Invite Endpoints

New endpoints allowing invites to grant roles and restrict acceptance to specified users

#### New Invite Endpoints

We've added new endpoints and functionality allowing invites to grant roles and to only be accepted by specified users. These are perfect for communities that want to manage access more granularly or reward members with special roles when they join a server.

[Create Channel Invite](https://docs.discord.com/developers/resources/channel#create-channel-invite) has been updated to support `target_users_file` and `role_ids` parameters.

* `target_users_file`: A CSV file with user IDs to specify who can accept the invite
* `role_ids`: Role IDs for roles to assign to users when they accept the invite

Invite endpoints:

* [Get Target Users](https://docs.discord.com/developers/resources/invite#get-target-users): Gets the users allowed to see and accept an invite
* [Update Target Users](https://docs.discord.com/developers/resources/invite#update-target-users): Updates the users allowed to see and accept an invite
* [Get Target Users Job Status](https://docs.discord.com/developers/resources/invite#get-target-users-job-status): Checks the status of the job that processes the target users for an invite from file upload

### December 17, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.8.13395

Added moderation metadata support, WebSocket reporting improvements, and PS5 timing metrics

#### Discord Social SDK Release 1.8.13395

A new release of the Discord Social SDK is now available, with the following updates:

##### Moderation Metadata Support

* \[Coming Soon] Messages will soon support [`MessageHandle::ModerationMetadata`], a set of custom string key-value pairs that can be used
  to communicate moderation-related information between your game backend and client.
  * This SDK version includes the functionality to support this upcoming feature, but it will only become available
    after an upcoming Discord API change.

##### WebSocket Reporting

* WebSocket connection failures will now report an HTTP status code to the SDK log.

##### PlayStation 5

* Improved accuracy of timing metrics used for monitoring the health of connections and voice calls.

### December 16, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.7.13357

Fixed crashes on Steam Deck and iOS

#### Discord Social SDK Release 1.7.13357

A new release of the Discord Social SDK is now available, with the following updates:

* Fixed a crash on Steam Deck when calling RegisterLaunchCommand
* Fixed a crash on iOS when Deeplink Authentication fails.

### December 16, 2025

**Tags:** `Discord Social SDK`

**Summary:** New Social SDK Guide: Account Linking from Discord

New guide for enabling account linking entry points within the Discord client

#### New Social SDK Guide: Account Linking from Discord

We've added a new guide showing how to enable account linking entry points within the Discord client. With Social SDK 1.6+, Discord can now display "Link your account" prompts and buttons throughout the client to encourage players to connect their game accounts, leading to higher linking rates and better social engagement.

The guide covers two implementation flows:

* **Connected Game Flow (recommended)**: Uses new callback methods to launch account linking directly in your game when players click Discord's entry points
* **Web Flow**: Routes players through a web-based OAuth flow (currently only available for select partners)

[Read the full guide →](https://docs.discord.com/developers/discord-social-sdk/development-guides/account-linking-from-discord)

### December 10, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.6.13305

Fixed crashes on Steam Deck and iOS

#### Discord Social SDK Release 1.6.13305

A new release of the Discord Social SDK is now available, with the following updates:

* Fixed a crash on Steam Deck when calling RegisterLaunchCommand
* Fixed a crash on iOS when Deeplink Authentication fails.

### December 09, 2025

**Tags:** `HTTP API`

**Summary:** Get Guild Role Member Counts Endpoint

New endpoint to access the number of members that have each role

#### Get Guild Role Member Counts Endpoint

Apps can now use the [Get Guild Role Member Counts](https://docs.discord.com/developers/resources/guild#get-guild-role-member-counts) endpoint to access the number of members that have each role!

### December 04, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.7.13152

Added macOS 10.15 support for Intel Macs

#### Discord Social SDK Release 1.7.13152

A new release of the Discord Social SDK is now available, with the following updates:

##### macOS

* Added support for macOS 10.15 to the build. The minimum versions are now 10.15 for Intel Macs and 11.0 for Apple Silicon Macs.

### November 24, 2025

**Tags:** `Breaking Change`

**Summary:** Permission Changes Going into Effect February 2026

Breaking permission changes for PIN_MESSAGES, BYPASS_SLOWMODE, CREATE_GUILD_EXPRESSIONS, and CREATE_EVENTS

#### Permission Changes Going into Effect February 2026 for PIN\_MESSAGES, BYPASS\_SLOWMODE, CREATE\_GUILD\_EXPRESSIONS, and CREATE\_EVENTS

We have some important permission changes that will take effect in February 2026.

The introduction of the following permissions were non-breaking changes.

However, the breaking changes described below - where the old permissions will no longer grant these abilities - will take effect on February 23, 2026. These changes involve a few permissions that we split from their original permission to provide more granular control over bot and user actions.

##### What's Changing?

**1. Pin Messages Permission**

* The `PIN_MESSAGES` permission (`1 << 51`) was split from `MANAGE_MESSAGES` on August 20, 2025.
* [Read the change log](https://docs.discord.com/developers/change-log#pin-permission-split).
* Starting February 23, 2026, users and bots will need the `PIN_MESSAGES` permission to pin messages. `MANAGE_MESSAGES` alone will no longer be sufficient.

**2. Bypass Slowmode Permission**

* The `BYPASS_SLOWMODE` permission (`1 << 52`) is being split from `MANAGE_MESSAGES`, `MANAGE_CHANNEL`, and `MANAGE_THREADS`.
* [Read the change log](https://docs.discord.com/developers/change-log#new-bypassslowmode-permission-permission-split).
* Note: This primarily affects users, as bots are not affected by slowmode restrictions.
* Starting on February 23, 2026, users will need the `BYPASS_SLOWMODE` permission to not be affected by slowmode restrictions.

**3. Create Expressions Permission**

* The `CREATE_GUILD_EXPRESSIONS` permission (`1 << 43`) was created in July 2023 and split from `MANAGE_GUILD_EXPRESSIONS` for users in December 2023. [Read the change log](https://docs.discord.com/developers/change-log#clarification-on-permission-splits-for-expressions-and-events).
* As of today, bots now have access to the `CREATE_GUILD_EXPRESSIONS` permission.
* [Read the change log](https://docs.discord.com/developers/change-log#guild-expressions-and-events-permissions-now-available-to-developers).
* Starting on February 23, 2026, bots will need the `CREATE_GUILD_EXPRESSIONS` permission to create custom emoji and stickers. `MANAGE_GUILD_EXPRESSIONS` alone will no longer be sufficient.

**4. Create Events Permission**

* The `CREATE_EVENTS` permission (`1 << 44`) was created in July 2023 and split from `MANAGE_EVENTS` for users in December 2023. [Read the change log](https://docs.discord.com/developers/change-log#clarification-on-permission-splits-for-expressions-and-events).
* As of today, bots now have access to the `CREATE_EVENTS` permission.
* [Read the change log](https://docs.discord.com/developers/change-log#guild-expressions-and-events-permissions-now-available-to-developers).
* Starting on February 23, 2026, bots will need the `CREATE_EVENTS` permission to create scheduled events. `MANAGE_EVENTS` alone will no longer be sufficient.

##### What Do You Need to Do?

If your bot performs any of the following actions, please review and update your bot's permission requests before February 23, 2026:

* **Pins messages:** Request the `Pin Messages` permission
* **Creates custom emoji or stickers:** Request the `Create Expressions` permission
* **Creates scheduled events:** Request the `Create Events` permission

These changes are designed to give server administrators more control over what bots and users can do, ensuring better security and permission management.

### November 24, 2025

**Summary:** New BYPASS_SLOWMODE Permission

New BYPASS_SLOWMODE permission being split from MANAGE_MESSAGES, MANAGE_CHANNEL, and MANAGE_THREADS

#### New BYPASS\_SLOWMODE Permission & Permission Split

We have introduced a new permission: `BYPASS_SLOWMODE`. This permission allows designated roles or users to bypass slowmode restrictions in channels.

* The `BYPASS_SLOWMODE` permission (`1 << 52`) is being split from `MANAGE_MESSAGES`, `MANAGE_CHANNEL`, and `MANAGE_THREADS`.
* Note: This primarily affects users, as bots are not affected by slowmode restrictions.
* Starting on February 23, 2026, users will need the `BYPASS_SLOWMODE` permission to not be affected by slowmode restrictions.

### November 20, 2025

**Tags:** `Breaking Change`

**Summary:** Guild Expressions and Events Permissions

CREATE_GUILD_EXPRESSIONS and CREATE_EVENTS permissions now available for bot developers

#### Guild Expressions and Events Permissions now available to developers

In 2023, we had introduced permission splits for guild expressions (custom emoji and stickers) and scheduled events. These changes were made to give server administrators more granular control over who can create content in their communities. [Read the change log](https://docs.discord.com/developers/change-log#clarification-on-permission-splits-for-expressions-and-events).

Today, we are announcing that these permissions are now available for bot developers to use and will be required for certain actions starting **February 23, 2026**.

**Create Guild Expressions Permission**

* The `CREATE_GUILD_EXPRESSIONS` permission (`1 << 43`) was created in July 2023 and split from `MANAGE_GUILD_EXPRESSIONS` for users in December 2023.
* As of today, bots now have access to the `CREATE_GUILD_EXPRESSIONS` permission.
* Starting on February 23, 2026, bots will need the `CREATE_GUILD_EXPRESSIONS` permission to create custom emoji and stickers. `MANAGE_GUILD_EXPRESSIONS` alone will no longer be sufficient.

**Create Events Permission**

* The `CREATE_EVENTS` permission (`1 << 44`) was created in July 2023 and split from `MANAGE_EVENTS` for users in December 2023.
* As of today, bots now have access to the `CREATE_EVENTS` permission.
* Starting on February 23, 2026, bots will need the `CREATE_EVENTS` permission to create scheduled events. `MANAGE_EVENTS` alone will no longer be sufficient.

### November 20, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.7.13024

Fixed Windows default audio device selection and added Xbox GDK 240605 support

#### Discord Social SDK Release 1.7.13024

A new release of the Discord Social SDK is now available, with the following updates:

#### Windows

* Fixed default audio device selection to once again prefer the default system audio device instead of the default communications device.

#### Xbox

* Added support for GDK 240605 to the build.

### November 12, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.7

New authentication providers, linked channel improvements, PS5 low energy mode, and voice upgrades with WebRTC m130

#### Discord Social SDK Release 1.7

A new release of the Discord Social SDK is now available, with the following updates:

#### Authentication

* Sign in with Apple and PlayStation Network are now supported as external identity providers.

#### Linked Channels

* The results of [`Client::GetGuildChannels`] are now sorted in the order in which they appear in the Discord client.
  Additional properties added to [`GuildChannel`] for type, position and parent category ID.

#### PlayStation 5

* Added Low Energy Mode support. Explicit control of SDK thread affinity is provided by `cpuAffinityMask` property of [`ClientCreateOptions`].
* Fixed a crash when destroying and recreating [`Client`].

#### Windows

* Fixed an issue which caused local crash dumps to be disabled in processes which load the Social SDK.

#### Voice

* The Social SDK now uses our latest audio subsystem on Windows, bringing it more in line with the desktop client. Improves device compatibility and fixes some long-standing issues like Bluetooth devices changing profiles on startup.
* Desktop clients now use WebRTC m130 internally (upgraded from m116).
* Bug fixes and improvements to DAVE E2EE protocol implementation.

### November 05, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.6.12767

Fixed a crash on PlayStation when creating, destroying, and recreating the Discord client

#### Discord Social SDK Release 1.6.12767

A new release of the Discord Social SDK is now available, with the following update:

Implemented a fix for a crash on Playstation when creating the Discord client, destroying it, and creating another.

### October 16, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.5.12211

Fixed a crash when calling GetUserGuilds on iOS devices

#### Discord Social SDK Release 1.5.12211

A new release of the Discord Social SDK is now available, with the following update:

#### Bug Fix

* Fixed a crash when calling [`Client::GetUserGuilds`] on iOS devices. First occurrence of this crash introduced in 1.5.10839

### October 15, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.6.12170

Custom invite banner images, customizable Rich Presence names, Xbox GDK 2025.04 support, and iOS crash fix

#### Discord Social SDK Release 1.6.12170

A new release of the Discord Social SDK is now available, with the following updates:

#### New Features

This small update to v1.6 adds some highly requested features from our partners. We found some time to sneak them in…

* You can now provide custom art to display as a banner image in game invites that appear in Discord. This is done one
  of two ways:
  * By specifying a URL or an `asset key` to an image in the `activity.assets.inviteCoverImage` parameter when
    calling `Client::UpdateRichPresence`. This method even affords you the ability to set a unique image
    on each invite if you want!
  * By uploading cover image art in the `Rich Presence` tab in the Developer Portal for your Application. Note: This
    will be used as the fallback image if you don't specify one via `activity.assets.inviteCoverImage`
* It's now possible to customize the displayed name for your Application in Discord's Rich Presence. To do so, set
  the `activity.name` parameter when calling [`Client::UpdateRichPresence`]
* Added support for Microsoft Xbox GDK version 2025.04
* Fixed a crash when calling [`Client::GetUserGuilds`] on iOS devices

### October 15, 2025

**Tags:** `Interactions`, `Components`

**Summary:** File Upload Component in Modals

New File Upload component for modals, supporting 0-10 files with configurable requirements

#### Introducing the File Upload component in Modals

Have you ever wanted to collect more than text from a user through a modal? With the new [**File Upload**](https://docs.discord.com/developers/components/reference#file-upload) component you can! You can specify a min and max number of files accepted between 0 and 10, and if uploading files within that limit is required before submitting. Any file types are accepted, and the max file size is based on the user's upload limit in that channel.

###### The New Component:

* [**File Upload**](https://docs.discord.com/developers/components/reference#file-upload)

###### Developer Resources

* [Using Modal Components](https://docs.discord.com/developers/components/using-modal-components) - Dive into creating a modal
* Check out our [Component Reference](https://docs.discord.com/developers/components/reference) for details on all available components.

### September 26, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.6

Game profile integration, in-Discord authentication flow, voice improvements, and critical bug fixes

#### Discord Social SDK Release 1.6

A new release of the Discord Social SDK is now available, with the following updates:

##### ✨ New Features

* When calling [`Client::GetGuildChannels`], channels are now sorted by their `position` field, which matches how they are sorted in the Discord client.
* Messages received via the Social SDK, no longer create notifications in a Discord client for the same user, to avoid double notification on the same machine.

**This release adds features to support upcoming Discord experiments that will enhance how games integrate with user profiles and authentication:**

* **Game Profile Integration**: New functionality to display game data on Discord user profiles. This includes `UserApplicationProfile` support with two new methods: `Client::GetUserApplicationProfiles` and `Client::GetUserApplicationProfilesNoLock` on the Users class, which retrieve game identity data from external authentication providers.
* **In-Discord Authentication Flow**: Support for users to start account linking directly from Discord (rather than having to initiate it from within your game). Added [`Client::RegisterAuthorizeRequestCallback`] and [`Client::RemoveAuthorizeRequestCallback`] methods to handle authentication requests that originate from various Discord entry points. These functions support upcoming Discord client experiments that will be gradually rolled out to users over time.

##### ⚠️ Deprecations

This deprecation aims to improve consistence across the SDK's API surface as well as provide a safer implementation that has fewer edge cases and less potential for accidental misuse.

* Deprecated [`Client::GetCurrentUser`] API in favor of [`Client::GetCurrentUserV2`] which returns optional values instead of potentially invalid handles.

##### 🚀 Performance Improvements

* This update implements caching capabilities for the [`Client::GetUserMessagesWithLimit`] function to avoid unnecessary remote API calls when sufficient messages are already cached locally.

##### 🎤 Voice Communications Fixes and Improvements

Fixes several critical bugs with the voice communications system, as well as improved overall reliability, and noise and echo suppression and cancellation.

* Fixed an issue where voice calls would sometimes transition to `Disconnected` state instead of reconnecting properly after a network interruption.
* Extended AGC2 (Automatic Gain Control 2) support to mobile platforms

##### 🐛 General Stability and Bug Fixes

Multiple general critical bugs that can cause crashes and panics. We highly recommend upgrading to 1.6 to avoid them in your game.

* Fixed critical bug where activity party privacy wasn't properly set, causing "ask to join" to appear instead of "join" for public parties.
* Fixed critical memory safety issue preventing connection objects from being deallocated during timer callbacks.
* Fixed C# marshaling alignment bugs and double-free crashes.
* Improved gateway resilience with fallback to generic URLs on zonal gateway failures.
* Fixed WebSocket write-after-close errors preventing connection issues.

To learn more about building with the Discord Social SDK, check out the [Discord Social SDK Overview](https://discord.com/developers/docs/discord-social-sdk/overview), and if you have questions, feel free to drop them in [#social-sdk-dev-help](https://discord.com/channels/613425648685547541/1350223314307776592)!

### September 10, 2025

**Tags:** `Interactions`, `Components`

**Summary:** More Modal Components

All select menus and Text Display component now supported in modals

#### Adding More Modal Components!

We've added more components to modals! All select menus (User, Role, Mentionable, Channel) are now fully supported in modals. In order to use a select menu in a modal, it must be placed inside a [Label](https://docs.discord.com/developers/components/reference#label) component. We've also added the [Text Display](https://docs.discord.com/developers/components/reference#text-display) component with markdown support as a top-level component in modals.

###### Components Now Supported in Modals:

* [**User Select**](https://docs.discord.com/developers/components/reference#user-select)
* [**Role Select**](https://docs.discord.com/developers/components/reference#role-select)
* [**Mentionable Select**](https://docs.discord.com/developers/components/reference#mentionable-select)
* [**Channel Select**](https://docs.discord.com/developers/components/reference#channel-select)
* [**Text Display**](https://docs.discord.com/developers/components/reference#text-display)

###### Getting Started

* [Using Modal Components](https://docs.discord.com/developers/components/using-modal-components) - Dive into creating a modal

###### Developer Resources

Check out our [Component Reference](https://docs.discord.com/developers/components/reference) for details on all available components.

### September 10, 2025

**Tags:** `HTTP API`

**Summary:** Banner, Avatar, and Bio on Modify Current Member

Bots can now set banner, avatar, and bio fields using the modify current member route

#### Banner, avatar, and bio can be set on modify current member

As of September 10, 2025, bots can set `banner`, `avatar`, and `bio` fields using the [modify current member](https://docs.discord.com/developers/resources/guild#modify-current-member) route.

### September 02, 2025

**Tags:** `Voice`

**Summary:** Deprecating Non-E2EE Voice Calls

Starting March 1, 2026, only E2EE calls will be supported for all audio and video conversations on Discord

#### Deprecating Non-E2EE Voice Calls

We started work on end-to-end encryption for Discord over two years ago to enhance our user privacy and security. With
DAVE now supported across all platforms, we’re very close to making every call fully end-to-end encrypted.

##### Developer Impact

To support our long-term privacy goals, we will **only support E2EE calls starting on March 1st, 2026** for all audio
and video conversations in direct messages (DMs), group messages (GDMs), voice channels, and Go Live streams on
Discord. After that date, any client or application not updated for DAVE support will no longer be able to
participate in Discord calls.

##### Implementing E2EE Voice

For developers working with Discord's voice APIs, you can consult
[the updated voice documentation](https://docs.discord.com/developers/topics/voice-connections)
and the implementation examples available in our [open-source repository](https://github.com/discord/libdave) as
well as [the protocol whitepaper](https://github.com/discord/dave-protocol).

The [Discord Developers community](https://discord.gg/discord-developers) is also a
great place to find assistance and answers to any integration questions you may have.

We're committed to making this transition as smooth as possible while delivering the enhanced privacy and security that
DAVE provides to all Discord users.

### August 28, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.5.11353

Fixed crashes in Unity plugin affecting low-end Android devices and large metadata payloads

#### Discord Social SDK Release 1.5.11353

A new release of the Discord Social SDK is now available, with the following updates:

##### Unity Plugin

* Fixed a crash primarily affecting low-end Android devices (those with armv7 architecture) in
  [`Client::CreateOrJoinLobbyWithMetadata`]
* Fixed a crash when passing large amounts of metadata in [`Client::CreateOrJoinLobbyWithMetadata`]

The Discord Social SDK binaries are available for download in the Developer Portal after enabling the Discord Social SDK for your application.

To learn more about building with the Discord Social SDK, check out the [Discord Social SDK Overview](https://docs.discord.com/developers/discord-social-sdk/overview).

[`Client::CreateOrJoinLobbyWithMetadata`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a5c84fa76c73cf3c0bfd68794ca5595c1

### August 25, 2025

**Tags:** `Interactions`, `Components`

**Summary:** New Modal Components

New Label component for modals with String Select support and improved accessibility

#### Introducing New Modal Components!

You asked for them, and now they're here! Modals are getting new components!!

###### What's New

We're introducing a new top-level [Label](https://docs.discord.com/developers/components/reference#label) component for modals that have a `label`, `description`, and can contain a Text Input or a String Select! You heard right, String Selects now work in modals!

* String Selects now work in modals when placed inside a Label component
* Text Inputs can also be used inside a Label component
* When a Text Input is used in a Label component the `label` field on the Text Input is not allowed in favor of `label` on the Label component
* ActionRow + TextInput is now deprecated in favor of the new Label component for better accessibility
* The `required` field is now available on String Selects (defaults to true in modals, ignored in messages)
* The `disabled` field on String Selects is not currently allowed in modals, and will trigger an error if used

We've also documented [modal interaction responses](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-component-interaction-response-structures) and resolved objects for interactive components in each component's Examples section.

###### New Layout Component

* [**Label**](https://docs.discord.com/developers/components/reference#label) - A new top-level component that lets you add a title and description to your modal components!

###### Updates to Modal Components

* [**Text Input**](https://docs.discord.com/developers/components/reference#text-input) - Text Input can now be used in a [Label](https://docs.discord.com/developers/components/reference#label)
* [**String Select**](https://docs.discord.com/developers/components/reference#string-select) - String Selects can be used in modals! Place them in a [Label](https://docs.discord.com/developers/components/reference#label)

###### Getting Started

* [Using Modal Components](https://docs.discord.com/developers/components/using-modal-components) - Dive into creating a modal

###### Developer Resources

Check out our [Component Reference](https://docs.discord.com/developers/components/reference) for details on all available components.

### August 20, 2025

**Tags:** `Breaking Change`, `HTTP API`

**Summary:** Pin Permission Split

PIN_MESSAGES permission split from MANAGE_MESSAGES for more granular control over pinning

#### Pin Permission Split

[Pinning](https://docs.discord.com/developers/resources/message#pin-message) and [unpinning](https://docs.discord.com/developers/resources/message#unpin-message) messages now has its own [permission](https://docs.discord.com/developers/topics/permissions#permissions-bitwise-permission-flags). We split `PIN_MESSAGES` out of `MANAGE_MESSAGES` to give more granular control over who can pin messages in a channel. This is effective immediately for both users and apps. This change will be backwards compatible until January 12th 2026 when `MANAGE_MESSAGES` will no longer grant the ability to pin or unpin messages.

### August 15, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.5

DM history support, new Rich Presence activity types, linked channel guild joining, and native mobile authentication

#### Discord Social SDK Release 1.5

A new release of the Discord Social SDK is now available, with the following updates:

##### **DM History Support**

With the release of DM chat history this patch, the Social SDK can now fully support asynchronous player communication between individual players and in larger chat rooms. Players who go offline or background the game can come back to the history of the chat room and get caught up with what’s happening.

* Added [`Client::GetUserMessageSummaries`] and [`Client::GetUserMessagesWithLimit`] to retrieve direct message history

##### Rich Presence

Rich Presence can now more accurately display the different types of activities a player might be engaged in. Specifically, the “Competing” status may be valuable for games that host tournaments, weekend brackets, or other competitive play. Also, when you receive game invites, you can now accept them cross-device; don’t miss the group forming even if you’re AFK.

* Added support for additional activity types (Listening, Watching, Competing)
* Added support for new clickable URL fields and additional user status customization
* Support for server-to-server rich presence invites and gateway-based invite handling. This means an invite can be accepted on a different device and the [`Client::SetActivityInviteCreatedCallback`] will be invoked on connected SDK sessions.

##### Linked Channels

Linked channels are all about keeping groups of friends connected in and outside the game. You can now join a player to channel’s linked Discord server from in-game, helping them bridge that gap and stay connected with friends even when they stop playing.

* Added [`Client::JoinLinkedLobbyGuild`] to allow members of linked
  lobbies to join the linked lobby's guild from in-game

##### Android

The many-step process of mobile account linking has been simplified for users with Discord installed by deep-linking into the Discord mobile app to authorize with your game

* Implemented native authentication support
* Fixed native authentication callback when activities are terminated
* Added an experimental audio setting on Android to avoid setting the OS to voice comms mode when connected to a Bluetooth headset on Android. This may be used if you wish to avoid the transition to voice volume controls and other related changes when connected to Bluetooth. To enable this setting, pass a [`ClientCreateOptions`] when instantiating the client and set the `experimentalAndroidPreventCommsForBluetooth` flag

    *Figure: Video showing off the account linking process in 1.4 vs 1.5 on Android*

##### iOS

The many-step process of mobile account linking has been simplified for users with Discord installed by deep-linking into the Discord mobile app to authorize with your game

* Added native authentication support
* The experimental Game audio subsystem now makes use of the iOS 18.2+ echo canceller when available and falls back to Standard mode otherwise.

##### Windows

* Added ARM64 support

##### Linux

* Ensured glibc 2.31 compatibility

##### Bug Fixes

* Fixed bug where [`Client::SetVoiceLogDir`] didn’t have any effect
* Added better error event handling to distinguish server authorization errors from user cancellations
* Fixed activity platform validation for console games
* Fixed crash safety issues with [`Client::GetCurrentUser`] when the client is in an unexpected non-Ready state. Added [`Client::GetCurrentUserV2`] which explicitly returns an optional handle instead of dummy data in this situation. This issue also affected the Unity and Unreal versions of the SDK
* Fixed [`Call::SetPTTActive`]

#### Known Issues

* When the network is disconnected temporarily, active Calls may sometimes enter the Disconnected state instead of reconnecting. If a Call reaches Disconnected state, you must end and rejoin the call to reconnect if desired.
* For DM chat history
  * No SDK-side caching for [`Client::GetUserMessagesWithLimit`]
    * Every invocation of [`Client::GetUserMessagesWithLimit`] will directly query the backend rather than using local SDK-side caching. This may have performance implications, particularly under high-frequency usage.
  * Provisional account merge message retrieval
    * After a provisional account is merged into a full account, messages sent while the user was on the provisional account cannot be retrieved.

### August 14, 2025

**Tags:** `Gateway`

**Summary:** Rate Limit for Request Guild Members

New rate limit of 1 request per guild per bot every 30 seconds when requesting all guild members

#### Introducing Rate Limit When Requesting All Guild Members

We're introducing a change to the [Request Guild Members](https://docs.discord.com/developers/events/gateway-events#request-guild-members) gateway opcode.

##### What's changing?

We are implementing a rate limit on the [Request Guild Members](https://docs.discord.com/developers/events/gateway-events#request-guild-members) opcode[.](https://takeb1nzyto.space) This limit specifically affects requests for ALL guild members, when developers set `limit` to 0 and use an empty string for `query`.

> **Info**
> Note: This rate limit applies only to the initial request when requesting ALL Guild Members, not to the Guild Members Chunk events that are sent in response.

* **Rate Limit:** 1 request per guild per bot every 30 seconds
* **Scope:** The limit applies per guild per bot (one bot can request members for different guilds within the 30-second window)
* **Behavior:** Requests that exceed this limit will receive a [`RATE_LIMITED`](https://docs.discord.com/developers/events/gateway-events#rate-limited) event as a response:

```js
{
  "op": 0
  "t": "RATE_LIMITED",
  "d": {
    "opcode": 8,
    "retry_after": ...,
    "meta": {
      "guild_id": ...,
      "nonce": ...
    }
  }
}
```

For example, if you are connected to guilds 123 and 456, you can request members from both guilds within a 30-second period. However, you cannot make a second request to guild 123 within that same 30-second window.

##### Impact on Applications

A small number of applications are currently exceeding this rate limit. If your app heavily relies on this opcode, we recommend reviewing your current implementation and making necessary adjustments to maintain functionality.

##### Timeline

Most apps won't encounter this rate limit until it is rolled out to all servers on **October 1, 2025**. However, if you are the developer of an app that is requesting all guild members in very large guilds then you may start seeing this **as soon as today**, so we can ensure platform stability.

##### What you need to do

If your application uses [Request Guild Members](https://docs.discord.com/developers/events/gateway-events#request-guild-members) to request all members, we recommend:

* Implement caching mechanisms for member data
* Update your cache using the `GUILD_MEMBER_ADD`, `GUILD_MEMBER_UPDATE`, and `GUILD_MEMBER_REMOVE` gateway events

If you hit this limit, you will receive the [`RATE_LIMITED`](https://docs.discord.com/developers/events/gateway-events#rate-limited) event as a response.

### August 13, 2025

**Tags:** `Discord Social SDK`

**Summary:** Social SDK Communication Features GA

Messaging, voice chat, lobbies, and linked channels now generally available with new application process for full access

#### Discord Social SDK Communication Features - General Availability

Communication features (cross-platform messaging, voice chat, lobbies, and linked channels) are now generally available for all Discord
Social SDK users that meet our application process criteria. Previously available only in closed beta, these features
enable seamless player interaction within your game.

* **Direct Messages**: One-on-one private chat functionality
* **Discord voice chat**: Real-time voice communication inside game lobbies
* **Lobbies & In-Game text chat**: Virtual spaces where players can interact through voice and text chat
* **Linked Channels**: Integration with Discord's server-based text channels directly in your game UI

##### New Application Process for Full Access

We've launched an application process for developers who want to remove rate limits and gain production level access to communication features. Developers can now apply through our developer portal with detailed game information and usage projections to unlock production-level capacity.

As part of documenting this application process, we have also documented pre-approval rate limits, so you can build, test and develop against the Social SDK with confidence.

##### Get Started with the Social SDK

The Discord Social SDK binaries are available for download in the Developer Portal after enabling the Discord Social SDK for your application.

To learn more about building with the Discord Social SDK, check out the [Discord Social SDK Overview](https://docs.discord.com/developers/discord-social-sdk/overview).

### August 11, 2025

**Tags:** `Activities`, `Embedded App SDK`

**Summary:** Embedded App SDK Version 2.1 & 2.2

New clickable URL fields for Rich Presence activities and updated patchUrlMappings for simplified proxy URLs

#### Embedded App SDK Version 2.1 & 2.2

We've made a few improvements to the Embedded App SDK for version 2.2.0, here are the highlights:

##### Changes in version 2.1

###### New URL fields

We now support new fields for rich presence activities:

* `state_url` - URL that is linked to when clicking on the state text in the activity card
* `details_url` - URL that is linked to when clicking on the details text in the activity card
* `assets.large_url` - URL that is linked to when clicking on the large image in the activity card
* `assets.small_url` - URL that is linked to when clicking on the small image in the activity card

##### Changes in version 2.2

###### patchUrlMappings

In line with the [recent change](https://docs.discord.com/developers/change-log#remove-proxy-from-discord-activity-proxy-path) to remove the `.proxy/` path from Discord Activity proxy URLs, the `patchUrlMappings` utility has been updated to generate simplified URLs by default. It will now create mappings without the `.proxy/` prefix.

The Embedded App SDK is available via [npm](https://www.npmjs.com/package/@discord/embedded-app-sdk) and [GitHub](https://github.com/discord/embedded-app-sdk). You can check out our [installation guide and reference](https://docs.discord.com/developers/developer-tools/embedded-app-sdk) to get started with it!

### July 30, 2025

**Tags:** `Activities`, `Embedded App SDK`

**Summary:** Remove .proxy/ from Activity Proxy Path

CSP updated to allow requests without the .proxy/ prefix while maintaining full backwards compatibility

#### Remove .proxy/ from Discord Activity proxy path

We've updated the Content Security Policy (CSP) for Discord Activities to remove the `.proxy/` path requirement when making requests through the discordsays.com proxy. This change simplifies the developer experience while maintaining full backwards compatibility. This was made possible by resolving the underlying privacy considerations that originally required the `.proxy/` path restriction.

###### Before

Activities were required to make proxy requests through paths prefixed with `/.proxy/`:

```
https://<application_id>.discordsays.com/.proxy/api/endpoint
```

###### After

Activities can now make proxy requests directly without the `/.proxy/` prefix:

```
https://<application_id>.discordsays.com/api/endpoint
```

###### Technical Details

* **CSP Update**: The Content Security Policy now allows requests to `https://<app_id>.discordsays.com/*` instead of the more restrictive `https://<app_id>.discordsays.com/.proxy/*`
* **Proxy Behavior**: Both URL patterns work identically - your existing proxy mappings (e.g., `/api -> example.com`) will function the same way regardless of whether you use `/.proxy/api` or `/api`
* **Performance**: No performance differences between the two approaches

###### Developer Tooling Updates

The `patchUrlMappings` utility will be updated in an upcoming Embedded App SDK release to generate the simplified URLs by default, though it will continue to support the `.proxy/` format for backward compatibility.

###### Backward Compatibility

**All existing code will continue to work without changes.** The `/.proxy/` path prefix is still fully supported and will be maintained indefinitely. You can:

* Continue using existing `/.proxy/` URLs
* Switch to the new, simplified URLs
* Use both patterns simultaneously in the same application

**No migration is required.** This is a purely additive change that expands what's possible rather than breaking existing functionality.

### July 28, 2025

**Tags:** `HTTP API`

**Summary:** Guild Create Deprecation

Apps can no longer create guilds; endpoints have been removed from documentation and OpenAPI specification

#### Guild Create Deprecation

Apps can no longer create guilds. The documentation for these endpoints has been removed and the endpoints have been removed from the OpenAPI specification.

See our [earlier changelog entry](https://docs.discord.com/developers/change-log#deprecating-guild-creation-by-apps) for more information.

### July 17, 2025

**Tags:** `Activities`, `Embedded App SDK`

**Summary:** Clickable Links and Customizable Statuses in Rich Presence

New clickable link fields and customizable status text for Rich Presence activities

#### Clickable Links and Customizable Statuses in Rich Presence

We've added new functionality to Rich Presences to give users of your application a more interactive and flexible experience. There are two big changes as part of this:

* You can now add clickable links to the state text, details text, large image & small image
* You can now choose which field (name, state, or details) is used in users' status text in the member list (e.g. instead of "Listening to MyMusic" you can now have your status text show "Listening to Rick Astley")

All of these new fields are documented on the [Activity Object](https://docs.discord.com/developers/events/gateway-events#activity-object) section of Gateway Events and also available through the Embedded App SDK.

### July 02, 2025

**Tags:** `HTTP API`

**Summary:** Gradient Roles and Guild Tags

Documented gradient role colors and guild tags; color field on roles deprecated in favor of new colors field

#### Gradient Roles and Guild Tags

We've documented gradient role colors and guild tags in the API. Guild tags let users rep their favorite server with a 1-4 character badge next to their display name. They can be accessed using the `primary_guild` field on the user object. Servers can now give gradient colors to their roles instead of a single, solid color. Gradient colors use the new `colors` field on the role object. As part of this change, the `color` field on roles is now deprecated, but it will still work for backwards compatibility.

###### Gradient Role Colors

* The guild feature `ENHANCED_ROLE_COLORS` will let you know if a guild is able to set gradient colors to roles.
* Guild roles now have `colors` as part of the [structure](https://docs.discord.com/developers/topics/permissions#role-object-role-structure).
* `color` on guild roles is deprecated but will still be returned by the API and continues to work for backwards compatibility.
* [Role color structure](https://docs.discord.com/developers/topics/permissions#role-object-role-colors-object)

###### Guild Tags

* Guild tags can be retrieved through the `primary_guild` field on the user object.
* [User Primary Guild](https://docs.discord.com/developers/resources/user#user-object-user-primary-guild)

### June 26, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.4

A new release of the Discord Social SDK is now available, with the following updates:

#### Discord Social SDK Release 1.4

A new release of the Discord Social SDK is now available, with the following updates:

##### Lobby Chat History

* Added [`Client::GetLobbyMessagesWithLimit`] to retrieve lobby message histories based on a provided lobby ID, with a
  maximum of 200 messages and up to 72 hours.
* Only messages from lobbies the user is currently a member of can be retrieved.
* DM history will be coming soon too!

##### Unified Friends List

* Added [`Client::GetRelationshipsByGroup`] which both logically groups a user’s relationships for the purpose of
  rendering a friends list and sorts users based on
  our [Unified Friends List design guidelines](https://docs.discord.com/developers/discord-social-sdk/design-guidelines/unified-friends-list).
  Before, it was necessary to call [`Client::GetRelationships`] and manually partition each relationship into the
  appropriate friend group, as well as write your own sorting operations.
* Added [`Client::SetRelationshipGroupsUpdatedCallback`] which fires whenever a user change occurs which could invalidate
  a previously sorted friends list retrieved from [`Client::GetRelationshipsByGroup`]. Call
  [`Client::GetRelationshipsByGroup`] again to maintain an up-to-date friends list.
* Added `IsSpamRequest` to [`RelationshipHandle`], returns `true` if Discord believes the request to be spam.

##### Audio Changes

* A new experimental audio mode has been added for mobile devices which uses standard media audio streams instead of
  voice-specific processing. On iOS this causes the voice engine to use the Remote I/O Audio Unit instead of Voice
  Processing I/O and likewise on Android, media stream types are used instead of voice communication types. This mode
  may be enabled by creating a Client with a [`ClientCreateOptions`] parameter whose `experimentalAudioSystem`
  property is
  set to `AudioSystem::Game`. In this case, you should also set [`Client::SetEngineManagedAudioSession`] to true. **We do
  not recommend using this for production** - however, if you are interested in trying it out, we are looking for
  feedback!
* Added [`Client::SetAecDump`] to enable recording of audio diagnostic information.

##### Auth

* Publisher Auth
  * Publisher Auth is a new feature which makes authorization easier for publishers with multiple games. This is an
    early release of this feature and only available to a limited number of partners for now.
  * Added [`Client::ExchangeChildToken`] to facilitate child token exchange for public clients. Confidential clients
    will require a server to server implementation, but this method may be useful for development.
  * Invites from sibling applications will be visible to the SDK. They can be identified by the `applicationId` field
    on the [`ActivityInvite`] payload.
  * Messages sent from other sibling applications will be visible to the SDK. They can be identified by the
    `ApplicationId` method on the [`MessageHandle`].
* Added [`Client::RevokeToken`] and [`Client::UnmergeIntoProvisionalAccount`] to allow games leveraging Public Clients to
  perform token revocation or unmerge operations directly from clients.

##### Android

* The SDK is now compatible with 16KB page size.

##### Misc

* Improved activity serialization, avoiding including null/empty keys in the JSON payload.

### June 25, 2025

**Tags:** `HTTP API`

**Summary:** Paginated Pin Endpoints

We've added new endpoints to manage paginated pins in channels.

#### Paginated Pin Endpoints

We've added new endpoints to manage paginated pins in channels. The Get Channel Pins endpoint allows you to retrieve and manage pinned messages in a more efficient way, especially for channels with a large number of pinned messages. Both Pin and Unpin endpoints remain the same with a new route. As part of this change we have deprecated the old endpoints for pinned messages. Switching to the new endpoints should be straightforward, as they maintain similar functionality but with improved pagination support.

###### New Endpoints

**[Get Channel Pins](https://docs.discord.com/developers/resources/message#get-channel-pins)**: Retrieve a list of pinned messages in a channel with pagination support:
`GET /channels/[\{channel.id}](https://docs.discord.com/developers/resources/channel#channel-object)/messages/pins`

**[Pin Message](https://docs.discord.com/developers/resources/message#pin-message)**: Pin a message in a channel:
`PUT /channels/[\{channel.id}](https://docs.discord.com/developers/resources/channel#channel-object)/messages/pins/[\{message.id}](https://docs.discord.com/developers/resources/message#message-object)`

**[Unpin Message](https://docs.discord.com/developers/resources/message#unpin-message)**: Unpin a message in a channel:
`DELETE /channels/[\{channel.id}](https://docs.discord.com/developers/resources/channel#channel-object)/messages/pins/[\{message.id}](https://docs.discord.com/developers/resources/message#message-object)`

###### Deprecated Endpoints

**[Get Pinned Messages](https://docs.discord.com/developers/resources/message#get-pinned-messages-deprecated)**:
`GET /channels/[\{channel.id}](https://docs.discord.com/developers/resources/channel#channel-object)/pins`

**[Pin Message](https://docs.discord.com/developers/resources/message#pin-message-deprecated)**:
`PUT /channels/[\{channel.id}](https://docs.discord.com/developers/resources/channel#channel-object)/pins/[\{message.id}](https://docs.discord.com/developers/resources/message#message-object)`

**[Unpin Message](https://docs.discord.com/developers/resources/message#unpin-message-deprecated)**:
`DELETE /channels/[\{channel.id}](https://docs.discord.com/developers/resources/channel#channel-object)/pins/[\{message.id}](https://docs.discord.com/developers/resources/message#message-object)`

### June 05, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.3

A new release of the Discord Social SDK is now available, with the following updates:

#### Discord Social SDK Release 1.3

A new release of the Discord Social SDK is now available, with the following updates:

##### Authentication

* Added an `APPLICATION_DEAUTHORIZED` webhook event which can be configured in the developer portal. When a user unlinks their account or revokes authorization for your application in any way, this event will be sent to configured webhooks. The payload will contain serialized user information. See [Webhook Events](https://docs.discord.com/developers/events/webhook-events) docs for more information on configuring webhook events.

##### PC

* Added configurable request timeout SDK HTTP client requests. Support is on PC in this release with console and mobile support coming in future release. Timeout default value is 30000ms (30 seconds) and can be configured using the new Client API: [`Client::SetHttpRequestTimeout`]
* Fixed a crash that can occur when handling certain failed HTTP requests

##### Mobile

* [`Client::SetSpeakerMode`] is now deprecated. Unless [`Client::SetEngineManagedAudioSession`] is used, audio routing will be handled automatically by the SDK

###### Android

* Fixed routing of game and voice audio when external audio devices are connected and/or disconnected. [`Client::SetEngineManagedAudioSession`] has been added to communicate that the SDK should not manage audio routing and automatically enter and leave `MODE_IN_COMMUNICATION` when joining and leaving calls.
* Fixed an issue with the Authorize method when a device configuration change needs to restart the activity

###### iOS

* Various fixes for audio routing and session management. When using the Unity plugin, game audio will no longer stop playing when ending a call. For standalone SDK use, a method [`Client::SetEngineManagedAudioSession`] has been added to communicate that the SDK should not automatically start and stop the `AVAudioSession` when joining and leaving calls.
* Corrected supported platform values in `Info.plist` for iOS .frameworks.

##### Consoles

* Standalone archives now only contain console-specific files, like the Unity and Unreal Engine archives

##### Misc

* Fixed a thread safety issue with [`Client::AddLogCallback`]
* Added \[Flags] declaration for bit flags enums in C#

### May 05, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.2

A new release of the Discord Social SDK is now available, with the following updates:

#### Discord Social SDK Release 1.2

A new release of the Discord Social SDK is now available, with the following updates:

##### Rich Presence

* Added support for adding custom buttons on activity cards via [`Activity::AddButton`]

##### Packaging

* Unity and Unreal plugin artifacts now contain just the additional files for console support so they can be extracted on top of the base plugin
* Unity plugin is now packaged as a .zip that you should extract inside the Packages directory of your project to enable the above
* Console archives now contain a small README with some console-specific documentation

##### Misc

* Added [`Client::OpenConnectedGamesSettingsInDiscord`] for deeplinking into Discord's settings for connected games, which provides players some control over who can DM them
* Fixed a hang that could occur on Linux in [`Client::RegisterLaunchCommand`] and [`Client::RegisterLaunchSteamApplication`]
* [`Client::RegisterLaunchCommand`] and [`Client::RegisterLaunchSteamApplication`] now work from inside the Steam Runtime on Linux
* Fixed a crash on exit that could occur when there were pending callbacks in the queue

### April 29, 2025

**Tags:** `User Apps`, `HTTP API`, `Interactions`

**Summary:** Raised Component Limits

We're removing the top level component limit and raising the limit on number of components in a message to 40 when using the IS_COMPONENTS_V2 message flag!

#### Raised Component Limits

We're removing the top level component limit and raising the limit on number of components in a message to 40 when using the [`IS_COMPONENTS_V2` message flag](https://docs.discord.com/developers/resources/message#message-object-message-flags)! We're also removing the limit on the number of components in a [Container Component](https://docs.discord.com/developers/components/reference#container). Legacy messages have not changed and continue to allow up to 5 action rows.

###### What's New

* **Total components**: The limit for total components in a message has been increased to 40.
* **Top-level components**: There is no longer a limit on top level components in a message (previously it was 10).
* **[Container Component](https://docs.discord.com/developers/components/reference#container)**: There is no longer a limit on the number of components in a Container Component (previously it was 10).

###### Developer Resources

* Check out our [Component Reference](https://docs.discord.com/developers/components/reference) for detailed specifications on all available components.
* Learn how to build rich message layouts with components with [Using Message Components](https://docs.discord.com/developers/components/using-message-components).

### April 22, 2025

**Tags:** `User Apps`, `HTTP API`, `Interactions`

**Summary:** Introducing New Components for Messages!

We're bringing new components to messages that you can use in your apps.

#### Introducing New Components for Messages!

We're bringing new components to messages that you can use in your apps. They allow you to have full control over the layout of your messages.

###### Why We Built Components V2

Our previous components system, while functional, had limitations:

* Content, attachments, embeds, and components had to follow fixed vertical positioning rules
* Visual styling options were limited
* It was difficult to make visually cohesive experiences that combined the various functionalities of messages given they were expressed in a non-unified system

Our new component system addresses these challenges with fully composable components that can be arranged and laid out in any order, allowing for a more flexible and visually appealing design.

###### What's New

[Components V2](https://docs.discord.com/developers/components/overview) introduces several new component types that can be used in messages:

###### New Layout Components

* [**Section**](https://docs.discord.com/developers/components/reference#section) - Combine text with an accessory component for contextually linked elements
* [**Container**](https://docs.discord.com/developers/components/reference#container) - Create visually distinct groupings with a customizable accent color
* [**Separator**](https://docs.discord.com/developers/components/reference#separator) - Add visual spacing and dividers between components

###### New Content Components

* [**Text Display**](https://docs.discord.com/developers/components/reference#text-display) - Add rich markdown-formatted text anywhere in your messages
* [**Thumbnail**](https://docs.discord.com/developers/components/reference#thumbnail) - An image used in a [section](https://docs.discord.com/developers/components/reference#section)
* [**Media Gallery**](https://docs.discord.com/developers/components/reference#media-gallery) - Present collections of images and videos in an organized grid
* [**File**](https://docs.discord.com/developers/components/reference#file) - Embed file attachments as part of your message layout

###### Getting Started

To use the new components, you'll need to send the message flag `1 << 15` (`IS_COMPONENTS_V2`) which activates the components system on a per-message basis.

We've created guides to help you implement these new features:

* [Using Message Components](https://docs.discord.com/developers/components/using-message-components) - Learn how to build rich message layouts with components
* [Using Modal Components](https://docs.discord.com/developers/components/using-modal-components) - Create interactive forms and dialogs

###### Compatibility Notes

[Legacy component behavior](https://docs.discord.com/developers/components/reference#legacy-message-component-behavior) will continue to work as before, so your existing integrations won't break. However, when using the Components V2 flag, you'll need to adapt to a few changes:

* The `content` and `embeds` fields will no longer work but you'll be able to use [Text Display](https://docs.discord.com/developers/components/reference#text-display) and [Container](https://docs.discord.com/developers/components/reference#container) as replacements
* Attachments need to be exposed through components to be visible. You can use a [Media Gallery](https://docs.discord.com/developers/components/reference#media-gallery), [Thumbnail](https://docs.discord.com/developers/components/reference#thumbnail), or [File](https://docs.discord.com/developers/components/reference#file) component to display them
* The `poll` and `stickers` fields are disabled
* A max of 10 top-level components and 30 total components in a message

###### Developer Resources

Check out our [Component Reference](https://docs.discord.com/developers/components/reference) for detailed specifications on all available components.

We can't wait to see what you build!

### April 21, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.1.8318

A new release of the Discord Social SDK is now available, with the following updates:

#### Discord Social SDK Release 1.1.8318

A new release of the Discord Social SDK is now available, with the following updates:

##### Platforms

* Playstation standalone archives now include linker stubs

##### Voice

* Fixed a regression in audio playback on Linux

The Discord Social SDK binaries are available for download in the Developer Portal after enabling the Discord Social SDK
for your application.

To learn more about building with the Discord Social SDK, check out
the [Discord Social SDK Overview](https://docs.discord.com/developers/discord-social-sdk/overview).

### April 16, 2025

**Tags:** `Discord Social SDK`

**Summary:** Discord Social SDK Release 1.1

A new release of the Discord Social SDK is now available, with the following updates:

#### Discord Social SDK Release 1.1

A new release of the Discord Social SDK is now available, with the following updates:

##### Platforms

* Added Xbox One and PS4 console support

##### Auth

* Added support for Unity Services as an external auth provider

##### Voice

* [`Client::StartCallWithAudioCallbacks`] now permits sample data to be modified during record and
  playback for custom effects processing
* Fixed a bug where the speaking state for a user could be stuck in the "on" state
* Added [`Call::GetPTTReleaseDelay`]
* Initialization of the voice engine is now delayed until it's needed
* Fixed a deadlock with the Linux PulseAudio backend where malfunctioning audio devices could cause a voice engine
  lockup

##### Rich Presence

* Added support for sending rich presence updates and invites without connecting to the Discord gateway on desktop

##### Misc

* Added Linux support for [`Client::RegisterLaunchCommand`] and
  [`Client::RegisterLaunchSteamApplication`]
* Fixed a crash when a Unity Editor scripting domain reload (e.g. entering/exiting play mode) happens while an async
  completion callback is pending
* Fixed [`Client::RemoveDiscordAndGameFriend`] only working if you're Discord friends
* Reduced some log spam from desktop client RPC message handling

The Discord Social SDK binaries are available for download in the Developer Portal after enabling the Discord Social SDK
for your application.

To learn more about building with the Discord Social SDK, check out
the [Discord Social SDK Overview](https://docs.discord.com/developers/discord-social-sdk/overview).

### April 15, 2025

**Tags:** `HTTP API`

**Summary:** Deprecating Guild Creation by Apps

To address security concerns, we are deprecating the ability for applications to create guilds using the Create Guild endpoint.

#### Deprecating Guild Creation by Apps

##### Breaking Change

To address security concerns, we are deprecating the ability for applications to create guilds using the `Create Guild`
endpoint.

###### What's Changing

* The Create Guild endpoint (`POST /guilds`) will be restricted for applications starting July 15, 2025
* Existing Guilds owned by bots will have their ownership transferred to a real user
* After the deprecation date, the endpoint will no longer be available

###### Timeline

* **April 15, 2025**: Deprecation announcement
* **June 15, 2025**: System DM/Email notifications sent to affected app owners and designated guild members
* **July 15, 2025**: `Create Guild` endpoint will no longer be available

If your app is affected, you will receive a migration plan via Discord System DM.

We understand this change may affect some legitimate use cases. If you have questions or believe your application
requires continued access to guild creation functionality, please contact us through
the [Developer Support portal](https://support-dev.discord.com/hc).

### April 11, 2025

**Tags:** `Activities`, `Embedded App SDK`

**Summary:** Custom Incentivized Links

Custom Incentivized Links are used to customize how your incentivized link embed appears to users.

#### Custom Incentivized Links

##### Custom Incentivized Links for Activities

Custom Incentivized Links are used to customize how your incentivized link embed appears to users. You can create them in the developer portal or generate them from within your activity. Incentivized Links can be used as referral links, promotions, deep-linking into your activity, and more.

* shareLink will now let you attach custom params to links you share about your game using `custom_id`.
* Removed `referrer_id` from shareLink API. Any uses of `referrer_id` should be moved over to use `custom_id` instead. Passing `referrer_id` to shareLink will silently fail.

Learn more about [creating and managing Custom Incentivized Links](https://docs.discord.com/developers/activities/development-guides/growth-and-referrals#creating-and-managing-custom-incentivized-links) and [how to generate them from within your activity](https://docs.discord.com/developers/activities/development-guides/growth-and-referrals#generating-a-custom-link-within-your-activity) with the shareLink API.

The Embedded App SDK is available via [npm](https://www.npmjs.com/package/@discord/embedded-app-sdk) and [GitHub](https://github.com/discord/embedded-app-sdk). You can check out our [installation guide and reference](https://docs.discord.com/developers/developer-tools/embedded-app-sdk) to get started with it!

### April 03, 2025

**Tags:** `HTTP API`, `Interactions`

**Summary:** Per-Attachment File Upload Behavior for Apps

Starting today, file upload limits for apps are checked per-attachment rather than per-message.

#### Per-Attachment File Upload Behavior for Apps

Starting today, file upload limits for apps are checked per-attachment rather than per-message. This change makes the app attachment behavior the same as when a user uploads multiple attachments on a single message.

* File size limits now apply to each individual attachment
* Previously, limits were applied to the combined size of all attachments in a message
* This aligns app attachment handling with user attachment behavior

The interaction payload will also include a new `attachment_size_limit` key that specifies the maximum allowed attachment size. This limit may be higher than the default attachment size limit, depending on the guild's boost status or the invoking user's Nitro status.

For more information, check out [our documentation on file uploads](https://docs.discord.com/developers/reference#uploading-files).

### March 17, 2025

**Tags:** `Discord Social SDK`

**Summary:** Introducing the Discord Social SDK

Developers can now use the Discord Social SDK to build social features into their games, enabling friends lists, cross-platform messaging, voice and more for all players — with or without a Discord...

#### Introducing the Discord Social SDK

Developers can now use the Discord Social SDK to build social features into their games, enabling friends lists, cross-platform messaging, voice and more for all players — with or without a Discord account.

Discord Social SDK offers features that enhance connectivity and player engagement, including:

* Account Linking
* Provisional Accounts
* Rich Presence
* Deeplink Game Invites

Additionally, available in a closed beta to support in-game communications:

* Cross-Platform Messaging
* Linked Channels
* Voice Chat

Developers can request expanded access to these available features via the closed beta.

###### Discord Social SDK Developer Resources

New resources are available in the Developer Portal to help you get started with the Discord Social SDK:

* [Getting Started Guides](https://docs.discord.com/developers/discord-social-sdk/getting-started) for C++, Unity and Unreal Engine.
* [Development Guides](https://docs.discord.com/developers/discord-social-sdk/development-guides) for building your game's social features.
* [Design Guidelines](https://docs.discord.com/developers/discord-social-sdk/design-guidelines) for designing your game's social features.
* [SDK Reference](http://discord.com/developers/docs/social-sdk/index.html) is now available.
* The Discord Social SDK binaries are available for download in the Developer Portal after enabling the Discord Social SDK for your application.

To learn more about building with the Discord Social SDK, check out the [Discord Social SDK Overview](https://docs.discord.com/developers/discord-social-sdk/overview).

### December 16, 2024

**Tags:** `HTTP API`, `Interactions`, `Breaking Change`

**Summary:** Default File Upload Limit Change

On January 16, 2025, the default file upload limit will change from 25 MiB to 10 MiB.

#### Default File Upload Limit Change

On January 16, 2025, the default file upload limit will change from 25 MiB to 10 MiB.

While this limit is already active for users and bot users, it hasn't yet been applied to webhooks.

* This change will take effect on January 16, 2025.
* The 10 MiB limit will apply to both webhooks and interaction responses.

For more information, check out [our documentation on file uploads](https://docs.discord.com/developers/reference#uploading-files).

### December 12, 2024

**Tags:** `Premium Apps`

**Summary:** Premium Apps: Multiple Subscription Tiers

Developers with monetization enabled can now create and publish multiple subscription SKUs of the same type for their app.

#### Premium Apps: Multiple Subscription Tiers

Developers with monetization enabled can now create and publish multiple subscription SKUs of the same type for their app. This allows developers to offer different subscription tiers with varying benefits and pricing. Users can upgrade and downgrade between published subscription SKUs.

##### What's Changed

###### Developer Portal

* Under the `Monetization` tab, you can now publish multiple subscription SKUs of the same type for your app.

###### App's Store Page

* When multiple subscription SKUs are published: Users can now upgrade or downgrade between different published subscription SKUs.

###### User App Subscription Settings

* When multiple subscription SKUs are published: Users can now upgrade or downgrade between different published subscription SKUs.
* These settings are available under `User Settings → Subscriptions → App Subscriptions`.

###### Subscription Object

* New field `renewal_sku_ids` added to the [subscription object](https://docs.discord.com/developers/resources/subscription#subscription-object) response for `SUBSCRIPTION_UPDATE` events and API endpoints.
* `renewal_sku_ids` is a list of snowflakes that indicate the SKU(s) that the user will be subscribed to at renewal.

###### Updated Guide: Managing SKUs

* The [Managing SKUs](https://docs.discord.com/developers/monetization/managing-skus#creating-a-sku) guide has been updated to include information about creating and managing multiple subscription SKUs.

###### Updated Guide: Implementing App Subscriptions

* The [Implementing App Subscriptions](https://docs.discord.com/developers/monetization/implementing-app-subscriptions#supporting-upgrades-and-downgrades) guide has been updated to include information about supporting upgrades and downgrades between multiple subscription SKUs.

### November 05, 2024

**Tags:** `Premium Apps`

**Summary:** Entitlement Migration Completed

The entitlement migration which began on October 1, 2024, has been successfully completed as of November 1, 2024.

#### Entitlement Migration Completed

The [entitlement migration](https://docs.discord.com/developers/change-log#premium-apps-entitlement-migration-and-new-subscription-api) which began on **October 1, 2024**, has been successfully completed as of **November 1, 2024**.

##### What's Changed

* The documentation has been updated to reflect the new entitlement system as the standard behavior.
* `ENTITLEMENT_UPDATE` event for subscription-related entitlements now only occur when the subscription ends.
* The `ends_at` value on the [entitlement object](https://docs.discord.com/developers/resources/entitlement#entitlement-object) is now set when the subscription ends.
* To determine when a subscription was canceled, listen for `SUBSCRIPTION_UPDATE` events or use the [Subscription API](https://docs.discord.com/developers/resources/subscription) to retrieve the subscription's `status` and `canceled_at` timestamp.

For more details about the migration process, please refer to the [migration guide](https://docs.discord.com/developers/change-log#updates-to-entitlement-migration-guide).

### October 25, 2024

**Tags:** `Events`, `User Apps`

**Summary:** Webhook Events

You can now subscribe to a limited number of HTTP-based outgoing webhook events after configuring a webhook events URL.

#### Webhook Events

You can now subscribe to a limited number of HTTP-based outgoing [webhook events](https://docs.discord.com/developers/events/webhook-events#event-types) after [configuring a webhook events URL](https://docs.discord.com/developers/events/webhook-events#configuring-a-webhook-events-url). Currently, 3 events are available: `APPLICATION_AUTHORIZED`, `ENTITLEMENT_CREATE`, and `QUEST_USER_ENROLLMENT`. Read the [webhook events](https://docs.discord.com/developers/events/webhook-events) documentation for details on subscribing and using webhook events.

> **Info**
> When developing [user-installable apps](https://docs.discord.com/developers/resources/application#user-context), [Application Authorized](https://docs.discord.com/developers/events/webhook-events#application-authorized) (which is not available via [the Gateway](https://docs.discord.com/developers/events/gateway)) is useful to receive events when your app was installed to a user or server.

> **Warning**
> `ENTITLEMENT_CREATE` is the only monetization-related event available using webhook events, so you should still use the Gateway for [entitlement-related events](https://docs.discord.com/developers/events/gateway-events#entitlements). Other monetization-related events will be supported via webhook events soon.

### October 07, 2024

**Tags:** `Premium Apps`

**Summary:** Updates to Entitlement Migration Guide

The entitlement migration started on October 1, 2024 and will continue through 11:59PM PST on November 1, 2024.

#### Updates to Entitlement Migration Guide

The entitlement migration started on **October 1, 2024** and will continue through 11:59PM PST on **November 1, 2024**.

We updated our previous entitlement migration guide to provide more up-to-date information on impacts of developer impacts. Here's a summary of the changes we made:

* The migration will run through November 1, 2024 to ensure that any entitlements that are set to renew in October will be properly migrated to the new entitlement system upon renewal.
* `ENTITLEMENT_UPDATE` events will only occur when a subscription ends.
* The value of the `ends_at` in `ENTITLEMENT_UPDATE` events indicate the timestamp for **when the entitlement is no longer valid**.
* The `ends_at` value on the [entitlement object](https://docs.discord.com/developers/resources/entitlement#entitlement-object) is set when the subscription ends.
* To receive the value of when a subscription was canceled, you should listen for the `SUBSCRIPTION_UPDATE` events or use the [Subscription API](https://docs.discord.com/developers/resources/subscription).

View the [updated migration guide](https://docs.discord.com/developers/change-log#premium-apps-entitlement-migration-and-new-subscription-api).

To see a full diff of the changes, refer to this pull request: [Entitlement Migration Guide Updates](https://github.com/discord/discord-api-docs/pull/7201).

### September 26, 2024

**Tags:** `Activities`, `Embedded App SDK`, `Premium Apps`

**Summary:** Activities General Availability

Following up on the rollout of the App Launcher, we’re excited to announce that Activities are now generally available for developers.

#### Activities General Availability

Following up on [the rollout of the App Launcher](https://discord.com/blog/discover-more-ways-to-play-with-apps-now-anywhere-on-discord), we’re excited to announce that [Activities](https://docs.discord.com/developers/activities/overview) are now generally available for developers. In addition to API stability, this means that apps with Activities can now be [verified](https://support-dev.discord.com/hc/en-us/articles/23926564536471-How-Do-I-Get-My-App-Verified), [discoverable](https://docs.discord.com/developers/discovery/enabling-discovery) in the App Directory, and [implement monetization](https://docs.discord.com/developers/monetization/overview).

##### Recent API Updates

Since the developer preview was announced, there have been a few important API updates:

* Activities can now enable and implement monetization features, and [`getEntitlements`](https://docs.discord.com/developers/developer-tools/embedded-app-sdk#getentitlements),[`getSkus`](https://docs.discord.com/developers/developer-tools/embedded-app-sdk#getskus), and [`startPurchase`](https://docs.discord.com/developers/developer-tools/embedded-app-sdk#startpurchase) are generally available in the Embedded App SDK.
* New [Get Application Activity Instance](https://docs.discord.com/developers/resources/application#get-application-activity-instance) endpoint to make [managing Activity instances](https://docs.discord.com/developers/activities/development-guides/multiplayer-experience#activity-instance-management) easier.
* Apps with Activities can create an [Entry Point command (type `4`)](https://docs.discord.com/developers/interactions/application-commands#entry-point-commands), which are the primary entry point for Activities in the App Launcher. When new apps enable Activities, a [default Entry Point command](https://docs.discord.com/developers/interactions/application-commands#default-entry-point-command) will be created for the app. Read the [original change log](https://docs.discord.com/developers/change-log#entry-point-commands) and the [Entry Point command guide](https://docs.discord.com/developers/activities/development-guides/user-actions#setting-up-an-entry-point-command) for details.
* Activities can now be launched in response to interactions using the `LAUNCH_ACTIVITY` (type `12`) [interaction callback type](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-response-object-interaction-callback-type) for `APPLICATION_COMMAND`, `MESSAGE_COMPONENT`, and `MODAL_SUBMIT` [interaction types](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-interaction-type).
* Apps can now be installed to users (in addition to servers). After [setting up your installation contexts](https://docs.discord.com/developers/resources/application#setting-supported-installation-contexts), make sure to request the `application.commands` scope when authorizing with users to make sure your Activity is available for them across their Discord servers, DMs, and Group DMs.
* In August, there were updates to the Content Security Policy (CSP) for Activities that limits how you can make requests to external resources when building Activities. Read [the change log](https://docs.discord.com/developers/change-log#activities-proxy-csp-update) and the guide on [using external resources](https://docs.discord.com/developers/activities/development-guides/networking#using-external-resources) for details.

##### Documentation Updates

We’ve also added and improved the documentation for Activities and the Embedded App SDK to make it easier to build:

* New reference documentation for [Monetization](https://docs.discord.com/developers/monetization/overview) SDK commands: [`getEntitlements`](https://docs.discord.com/developers/developer-tools/embedded-app-sdk#getentitlements),[`getSkus`](https://docs.discord.com/developers/developer-tools/embedded-app-sdk#getskus), and [`startPurchase`](https://docs.discord.com/developers/developer-tools/embedded-app-sdk#startpurchase)
* Updated [Embedded App SDK Reference](https://docs.discord.com/developers/developer-tools/embedded-app-sdk) documentation that adds signatures and arguments
* Updated development guides for [Activity Instance Management](https://docs.discord.com/developers/activities/development-guides/multiplayer-experience#activity-instance-management) and [Activity Proxy Considerations](https://docs.discord.com/developers/activities/development-guides/networking#activity-proxy-considerations) when using external resources
* New guide on implementing [In-App Purchases (IAP) for Activities](https://docs.discord.com/developers/monetization/implementing-iap-for-activities)
* New guides for [Verification and Discovery Surfaces](https://docs.discord.com/developers/discovery/overview)
* New guide on [Using Rich Presence with the Embedded App SDK](https://docs.discord.com/developers/rich-presence/using-with-the-embedded-app-sdk)

### September 20, 2024

**Summary:** Soundboard API

Soundboard is now available in the API!

#### Soundboard API

[Soundboard](https://docs.discord.com/developers/resources/soundboard) is now available in the API! Apps can now [get](https://docs.discord.com/developers/resources/soundboard#list-default-soundboard-sounds) soundboard sounds, [modify](https://docs.discord.com/developers/resources/soundboard#modify-guild-soundboard-sound) them, [send](https://docs.discord.com/developers/resources/soundboard#send-soundboard-sound) them in voice channels, and listen to other users playing them!

### September 17, 2024

**Tags:** `Voice`

**Summary:** Voice End-to-End Encryption (DAVE Protocol)

Introduced high-level documentation for Discord's Audio and Video End-to-End Encryption (DAVE) protocol, and the new voice gateway opcodes required to support it

#### Voice End-to-End Encryption (DAVE Protocol)

Introduced [high-level documentation](https://docs.discord.com/developers/topics/voice-connections) for Discord's Audio and Video End-to-End Encryption (DAVE) protocol, and the [new voice gateway opcodes](https://docs.discord.com/developers/topics/opcodes-and-status-codes#voice) required to support it

##### **Developer Impact**

Starting September 2024, Discord is migrating voice and video in DMs, Group DMs, voice channels, and Go Live streams to use end-to-end encryption (E2EE).

**Who this affects:** Any libraries or apps that support [Voice Connections](https://docs.discord.com/developers/topics/voice-connections).

You are not immediately required to support the E2EE protocol, as calls will automatically upgrade/downgrade to/from E2EE depending on the support of clients in the call.

##### **Implementing E2EE Voice**

We have added high-level documentation for Discord's Audio and Video End-to-End Encryption (DAVE) protocol, and the new voice gateway opcodes required to support it.

The most thorough documentation on the DAVE protocol is found in the [Protocol Whitepaper](https://daveprotocol.com/). You can also use our open-source library [libdave](https://github.com/discord/libdave) to assist with your implementation. The exact format of the DAVE protocol opcodes is detailed in the [Voice Gateway Opcodes section of the protocol whitepaper](https://daveprotocol.com/#voice-gateway-opcodes).

##### **Future Deprecation and Discontinuation of Non-E2EE Voice**

Non-E2EE connections to voice in DMs, Group DMs, voice channels, and Go Live streams will eventually be deprecated and discontinued.

In 2025, all official Discord clients will support the protocol and it will be an enforced requirement to connect to the end-to-end encryption-eligible audio/video session types listed above.

Once a timeline for deprecation and discontinuation is finalized, we will share details and developers will have **at least six months** to implement before we sunset non-E2EE voice connections.

Read more about Discord's Audio and Video End-to-End Encryption (DAVE) protocol:

* [Meet DAVE: Discord's New End-to-End Encryption for Audio & Video](https://discord.com/blog/meet-dave-e2ee-for-audio-video)
* [DAVE Protocol Whitepaper](https://daveprotocol.com/)
* [libdave open-source library on GitHub](https://github.com/discord/libdave)

### September 04, 2024

**Tags:** `Interactions`

**Summary:** Add Polls when Editing Deferred Interaction Responses

You can now create a poll while editing a deferred interaction response with the Edit Original Interaction Response endpoint.

#### Add Polls when Editing Deferred Interaction Responses

You can now create a poll while editing a deferred interaction response with the [Edit Original Interaction Response](https://docs.discord.com/developers/interactions/receiving-and-responding#edit-original-interaction-response) endpoint. Poll away!

### August 28, 2024

**Tags:** `Premium Apps`, `Breaking Change`

**Summary:** Premium Apps: Entitlement Migration and New Subscription API

Updates to this Change Log entry was published on October 7, 2024 to reflect up-to-date information.

#### Premium Apps: Entitlement Migration and New Subscription API

> **Info**
> Updates to this Change Log entry was published on **October 7, 2024** to reflect up-to-date information. See the [new Change Log entry](https://docs.discord.com/developers/change-log#updates-to-entitlement-migration-guide) for details on updates.

We are migrating our entitlement system to a new behavior where entitlements will not end until explicitly canceled, representing a breaking change for subscription management. We are introducing a [Subscription API](https://docs.discord.com/developers/resources/subscription) and [Subscription Events](https://docs.discord.com/developers/events/gateway-events#subscriptions) to allow handling subscription-related events.

> **Warning**
> This change will be rolled out to all existing applications that have entitlements for user and guild subscription SKUs, starting on October 1, 2024.

###### Entitlement Migration Details

* `ENTITLEMENT_CREATE` events will now be triggered with a null `ends_at` value for all ongoing subscriptions, indicating an indefinite entitlement.
* `ENTITLEMENT_UPDATE` events will occur only when a subscription ends, with the `ends_at` value indicating the end date.
* Discord-managed Subscription entitlements will have an `type` value of `PURCHASE` (type `1`) instead of `APPLICATION_SUBSCRIPTION` (type `8`).

##### Migration Plan & Guide:

As of **October 1, 2024**, all existing entitlements that grant access to user-subscription and guild-subscription SKUs will automatically transfer to the new system on their renewal date. This means we will have a month-long migration window to allow all of your entitlements to migrate to the new system upon renewal.

Developers are advised to update their systems to handle the new `ENTITLEMENT_CREATE` and `ENTITLEMENT_UPDATE` events according to the following migration guide before the rollout date to avoid service disruptions.

##### Introducing a New Subscription API

With the new entitlement behavior, entitlements for subscription SKUs will no longer emit events at the start of a new subscription billing period. Instead, subscription lifecycle management can be handled through the new [Subscription API](https://docs.discord.com/developers/monetization/implementing-app-subscriptions#using-the-subscription-api).
Developers should refer to the [Subscription resource](https://docs.discord.com/developers/resources/subscription) for information on calling the Subscription API and responding to Subscription events. For in-depth implementation details, see our [Implementing App Subscriptions](https://docs.discord.com/developers/monetization/implementing-app-subscriptions#using-the-subscription-api) guide. You can start using this API now.

##### Monetization Documentation Updates

As part of these changes, we've updated the documentation for Premium Apps.

* Created a new [Enabling Monetization](https://docs.discord.com/developers/monetization/enabling-monetization) page to cover setting up your team, managing payouts, and enabling monetization for your apps
* Created a new [Managing SKUs](https://docs.discord.com/developers/monetization/managing-skus#creating-a-sku) page to document how to create, update, publish, and promote your SKUs
* Moved and added [Entitlement](https://docs.discord.com/developers/resources/entitlement), [SKU](https://docs.discord.com/developers/resources/sku) and [Subscription](https://docs.discord.com/developers/resources/subscription) resources to the **Resources** section
* Updated guides for [Implementing App Subscriptions](https://docs.discord.com/developers/monetization/implementing-app-subscriptions) and [Implementing One-Time Purchases](https://docs.discord.com/developers/monetization/implementing-one-time-purchases)

##### Subscription Entitlement Migration Guide

Starting on **October 1, 2024**, we will be migrating our existing entitlement system to a new behavior where **entitlements do not expire until explicitly canceled**. This migration guide outlines the changes and impacts of this migration on developers and guides how to manage these changes effectively.

> **Warning**
> With this update, entitlements for subscription SKUs will no longer emit events when a new subscription billing period begins. If you need to know when a subscription has been renewed, use the new [Subscription API](https://docs.discord.com/developers/resources/subscription) and related [Subscription Gateway Events](https://docs.discord.com/developers/events/gateway-events#subscriptions).

##### Current System

Currently, entitlements for Subscription SKUs purchased through Discord have:

* An `ends_at` date that corresponds to the subscription interval. This date is updated at each billing cycle.
* A entitlement `type` value of `APPLICATION_SUBSCRIPTION` (type `8`).
* An `ENTITLEMENT_UPDATE` event is triggered at the start of each new subscription period.

##### New System

Post-migration, entitlements for Subscription SKUs purchased through Discord will:

* No longer have an end date (`ends_at` will be `null`) until the user decides to cancel the subscription.
* Now have an entitlement `type` value of `PURCHASE` (type `1`).
* No `ENTITLEMENT_UPDATE` events will be triggered until the subscription is canceled.

##### Migration Timeline

* **Migration Start Date:** October 1, 2024
* **Migration End Date:** November 1, 2024

##### Migration Impacts

##### 1) Existing Entitlements Scheduled to Renew

* **During Migration Window:**
  * These will automatically transfer to the new system.
  * A new `ENTITLEMENT_CREATE` event will be triggered to indicate the migration. This does not indicate a net new entitlement.
  * No further events will be generated until the entitlement ends, which will then trigger an `ENTITLEMENT_UPDATE` event.
  * The `ends_at` value in the `ENTITLEMENT_UPDATE` event and in the Entitlement API will indicate the timestamp when the entitlement ends.

##### 2) Existing Entitlements Set to End

* **During Migration Window:**
  * These entitlements will naturally expire and not renew under the new system.
  * No new entitlement events will be generated for these cases.

##### Developer Actions

* **Pre-Migration:**
  * Review and understand the new entitlement event structure.
  * Adjust your system to handle `ends_at` being null, which now indicates an indefinite entitlement.
  * Adjust your system not to expect type `APPLICATION_SUBSCRIPTION` (type `8`) for Discord-managed subscription entitlements.
* **Post-Migration:**
  * Monitor for `ENTITLEMENT_CREATE`, `ENTITLEMENT_UPDATE`, `SUBSCRIPTION_CREATE`, and `SUBSCRIPTION_UPDATE` events.
  * Update any references to an entitlement `ends_at` timestamps, which now indicate the ending of an entitlement. If you need to know when a subscription's period ends, use the [Subscription API](https://docs.discord.com/developers/resources/subscription) and related [Subscription Gateway Events](https://docs.discord.com/developers/events/gateway-events#subscriptions).

### August 26, 2024

**Tags:** `Activities`, `Interactions`

**Summary:** Launching Activities in Response to Interactions

Activities can now be launched as a response to interactions using the LAUNCH_ACTIVITY (type 12) interaction callback type.

#### Launching Activities in Response to Interactions

[Activities](https://docs.discord.com/developers/activities/overview) can now be launched as a response to interactions using the `LAUNCH_ACTIVITY` (type `12`) [interaction callback type](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-response-object-interaction-callback-type). `LAUNCH_ACTIVITY` can be used in response to `APPLICATION_COMMAND`, `MESSAGE_COMPONENT`, and `MODAL_SUBMIT` [interaction types](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-interaction-type).

### August 26, 2024

**Tags:** `Activities`, `Interactions`

**Summary:** Entry Point Commands

Apps with Activities enabled can now create Entry Point commands using the PRIMARY_ENTRY_POINT (type 4) command type.

#### Entry Point Commands

Apps with [Activities](https://docs.discord.com/developers/activities/overview) enabled can now create [Entry Point commands](https://docs.discord.com/developers/interactions/application-commands#entry-point-commands) using the `PRIMARY_ENTRY_POINT` (type `4`) [command type](https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-types). Apps are limited to one globally-scoped Entry Point command, which appears in the App Launcher.

When creating or updating an Entry Point command, an [Entry Point handler](https://docs.discord.com/developers/interactions/application-commands#application-command-object-entry-point-command-handler-types) can be defined using the [`handler` field](https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-structure). The `handler` field determines whether your app wants to manually handle responding to the interaction:

* If the value is `DISCORD_LAUNCH_ACTIVITY` (`2`), Discord will automatically handle the interaction and send a follow-up message to the channel where the Entry Point command was invoked from.
* If the value is `APP_HANDLER` (`1`), your app will receive an interaction token and will be responsible for responding to the interaction. In this case, you can launch your Activity using the `LAUNCH_ACTIVITY` (type `12`) [interaction callback](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-response-object-interaction-callback-type).

More details about Entry Point commands can be found in the [Application Commands documentation](https://docs.discord.com/developers/interactions/application-commands#entry-point-commands) and in the [Activity development guide](https://docs.discord.com/developers/activities/development-guides/user-actions#setting-up-an-entry-point-command).

##### Default Entry Point Commands

Starting today, when you enable Activities in your [app's settings](http://discord.com/developers/applications), a [default Entry Point command](https://docs.discord.com/developers/interactions/application-commands#default-entry-point-command) called "Launch" will automatically be created for your app. This can be customized or deleted like other commands if you want to update the name or handler type.

### August 13, 2024

**Tags:** `Voice`

**Summary:** Voice Encryption Modes

Added documentation for voice encryption modes aead_aes256_gcm_rtpsize and aead_xchacha20_poly1305_rtpsize while announcing the deprecation of all xsalsa20_poly1305 variants and aead_aes256_gcm.

#### Voice Encryption Modes

Added documentation for voice [encryption modes](https://docs.discord.com/developers/topics/voice-connections#transport-encryption-modes) `aead_aes256_gcm_rtpsize` and `aead_xchacha20_poly1305_rtpsize` while announcing the deprecation of all `xsalsa20_poly1305*` variants and `aead_aes256_gcm`. Deprecated encryption modes will be discontinued as of November 18th, 2024.

> **Danger**
> Deprecated encryption modes will be discontinued as of November 18th, 2024.

### August 13, 2024

**Tags:** `Gateway`, `Voice`

**Summary:** Voice Gateway Version 8 and Deprecation of Versions < 4

We are officially deprecating some very old voice gateway versions (> 7 years ago).

#### Voice Gateway Version 8 and Deprecation of Versions \< 4

We are officially deprecating some very old voice gateway versions (> 7 years ago).

* The voice gateway now supports a resume which re-sends lost messages. Use voice gateway version 8 and refer to [Buffered Resume](https://docs.discord.com/developers/topics/voice-connections#buffered-resume).
* We have removed the default option for voice gateway version. Once this is deprecated, you must pass a voice gateway version.

> **Danger**
> You will be required to pass a voice gateway version and deprecated voice gateway versions will be discontinued as of November 18th, 2024. See [Voice Gateway Versioning](https://docs.discord.com/developers/topics/voice-connections#voice-gateway-versioning) for further details.

### August 12, 2024

**Tags:** `HTTP API`

**Summary:** Get Guild Role Endpoint

Need to get just one role, not the whole role list? Use the new Get Guild Role endpoint to fetch a single role by ID.

#### Get Guild Role Endpoint

Need to get just one role, not the whole role list? Use the new [Get Guild Role](https://docs.discord.com/developers/resources/guild#get-guild-role) endpoint to fetch a single role by ID.

### August 09, 2024

**Tags:** `User Apps`

**Summary:** User App Install Count

We've added an approximate user install count to the Application object for user-installable apps.

#### User App Install Count

We've added an approximate user install count to the [Application object](https://docs.discord.com/developers/resources/application#application-object) for user-installable apps. You can also view an app's install counts in the developer portal.

### August 05, 2024

**Tags:** `Voice`, `HTTP API`

**Summary:** Voice State Endpoints

Voice states can now be accessed over the HTTP API!

#### Voice State Endpoints

Voice states can now be accessed over the HTTP API! Apps can use the new [Get Current User Voice State](https://docs.discord.com/developers/resources/voice#get-current-user-voice-state) and [Get User Voice State](https://docs.discord.com/developers/resources/voice#get-user-voice-state) endpoints to fetch a user's voice state without a Gateway connection.

### July 25, 2024

**Summary:** Supported Activity Types for SET_ACTIVITY

The SET_ACTIVITY RPC command has been updated to support 3 additional activity types: Listening (2), Watching (3), and Competing (5).

#### Supported Activity Types for SET\_ACTIVITY

The [`SET_ACTIVITY` RPC command](https://docs.discord.com/developers/topics/rpc#setactivity) has been updated to support 3 additional [activity types](https://docs.discord.com/developers/events/gateway-events#activity-object-activity-types): Listening (`2`), Watching (`3`), and Competing (`5`). Previously, it only accepted Playing (`0`).

> **Warning**
> The [Game SDK](https://docs.discord.com/developers/developer-tools/game-sdk#activities) has not been updated to support setting [`ActivityType`](https://docs.discord.com/developers/developer-tools/game-sdk#activitytype-enum), and is still limited to read-only (to handle events that you receive from Discord).

### July 18, 2024

**Summary:** Application Emoji

You can now upload emojis for your application in your app's settings and use them as custom emojis anywhere on Discord.

#### Application Emoji

You can now upload emojis for your application in your [app's settings](https://discord.com/developers/applications) and use them as custom emojis anywhere on Discord.

* Up to 2000 emojis per app
* Support for user-installable apps
* Can be [managed via the API](https://docs.discord.com/developers/resources/emoji#create-application-emoji) with a bot token

### July 17, 2024

**Tags:** `Activities`, `Embedded App SDK`, `Breaking Change`

**Summary:** Activities Proxy CSP Update

This change is outdated. We have since updated the Activities Proxy CSP and the use of /.proxy/ is no longer required. For the latest information, please refer to this changelog. </Warning>

#### Activities Proxy CSP Update

> **Warning**
> This change is outdated. We have since updated the Activities Proxy CSP and the use of `/.proxy/` is no longer required. For the latest information, please refer to [this changelog](https://docs.discord.com/developers/change-log#remove-proxy-from-discord-activity-proxy-path).

This change will be rolled out to all existing applications on **August 28, 2024**.

We will be updating our Content Security Policy (CSP) for the Activities Domain (`https://<application_id>.discordsays.com`). This represents a **breaking change** for **all Activities**, and as such we have a migration plan in order.

our CSP will be updated as follows:

* all requests must be made through `https://<application_id>.discordsays.com/.proxy/`, and requests to other paths on the `discordsays.com` domain will be blocked.
* requests to `https://discord.com/api/` will be permitted, but other paths on the `discord.com` domain will be blocked.
* Only allowed paths on `cdn.discordapp.com` and `media.discordapp.net` will be permitted such as `/attachments/`, `/icons/`, and `/avatars/`.
* nested child iframes must also mount paths prepended by `/.proxy/`

As of [embedded-app-sdk v1.4.0](https://github.com/discord/embedded-app-sdk/releases/tag/v1.4.0) we have updated `patchUrlMappings` to automatically route requests through `/.proxy/`, so updating your SDK version calling `patchUrlMappings` is a good first step. If you are unfamiliar with `patchUrlMappings`, please consult the [documentation](https://docs.discord.com/developers/activities/development-guides/networking#using-external-resources).

All Application IDs created after `07/17/2024 12:00:00` UTC (applicationID greater than `1263102905548800000`) will also automatically have the new CSP applied. Testing your production code on a new application created after this date is a suggested way for developers to test compliance with this new CSP.

### July 16, 2024

**Summary:** Guild Member Banners

Apps can now access guild member profile banners via the API and Gateway!

#### Guild Member Banners

Apps can now access guild member profile banners via the API and Gateway! The [guild member object](https://docs.discord.com/developers/resources/guild#guild-member-object) now includes a `banner` field which can be used to create the [guild member banner URL](https://docs.discord.com/developers/reference#image-formatting).

### July 15, 2024

**Summary:** Message Forwarding rollout

We are slowly rolling out the message forwarding feature to users.

#### Message Forwarding rollout

We are slowly rolling out the message forwarding feature to users. This feature allows callers to create a message using `message_reference.type = FORWARD` and have the API generate a `message_snapshot` for the sent message. The feature has [some limitations](https://docs.discord.com/developers/resources/message#message-reference-types) and the snapshot is a minimal version of a standard `MessageObject`, but does capture the core parts of a message.

The resulting message will look something like:

```json
{
  "id": "1255957733279273083",
  "message_reference": {
    "type": 1, // Forward
    ...
  }
  "message_snapshots": [
    {
      "message": {
        "content": "original message",
        "embeds": [...],
        "attachments": [...],
        ...
      }
    }
  ],
  ...
}
```

We have applied stricter rate limits for this feature based on the following:

* number of forwards sent by the user
* total attachment size

###### API Updates since preview

This was [previously announced](https://discord.com/channels/613425648685547541/697138785317814292/1233463756160503859) but note that the final API has a few changes since the API was first previewed:

* [`message snapshot`](https://docs.discord.com/developers/resources/message#message-snapshot-object) objects don't include a `guild` field anymore since the `message_reference` already provides that information
* forwarded messages have a distinctive `message_reference` type of `FORWARD` now

### July 09, 2024

**Summary:** Banners in Get Current User Guilds

GET /users/@me/guilds now includes each guild's banner field!

#### Banners in Get Current User Guilds

[`GET /users/@me/guilds`](https://docs.discord.com/developers/resources/user#get-current-user-guilds) now includes each guild's `banner` field! This enables apps using OAuth2 with the `guilds` scope to display guild banners.

### June 27, 2024

**Tags:** `Breaking Change`

**Summary:** User-Installed Apps General Availability

Back in March, we announced the beta for user-installed apps.

#### User-Installed Apps General Availability

Back in March, we announced [the beta for user-installed apps](https://docs.discord.com/developers/change-log#userinstallable-apps-preview). After listening and making updates based on feedback from developers and modmins, we're excited to announce that user-installed apps are now considered generally available and can be used in all servers (regardless of size).

With this update, there are a few API and behavioral updates for user-installed apps.

###### API Updates

* `user_id` has been removed from the `interaction_metadata` field on messages. Instead, you can use the `id` field in the nested `user` object. See the [Message Interaction Metadata Object](https://docs.discord.com/developers/resources/message#message-interaction-metadata-object) for details.
* User-installed apps are now limited to creating a maximum of 5 [follow-ups](https://docs.discord.com/developers/interactions/receiving-and-responding#followup-messages) when responding to interactions. This only affects the [Create Followup Message endpoint](https://docs.discord.com/developers/interactions/receiving-and-responding#create-followup-message), and apps installed to the server are unaffected.
* On [Interactions](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-interaction-structure), the value of `authorizing_integration_owners` is now correctly serialized as a string. Previously, the `"0"` value was incorrectly serialized as a number.
* `app_permissions` on [Interactions](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-interaction-structure) now correctly represents the permissions for user-installed apps. Previously, the value was incorrect for user-installed apps.
* Updating a message can result in a `400` response if the content of the message was blocked by AutoMod, which may be particularly important for [deferred messages](https://docs.discord.com/developers/interactions/receiving-and-responding#responding-to-an-interaction).
* Interaction responses are no longer forced to be ephemeral for servers with over 25 members.

###### New `Use External Apps` Permission

A new [`USE_EXTERNAL_APPS` (`1 << 50`) permission](https://docs.discord.com/developers/topics/permissions#permissions-bitwise-permission-flags) was added, and is enabled for servers by default. The new permission lets modmins control whether user-installed apps can post public replies in a server. If `Use External Apps` is disabled and your app is *not* installed to the server, your app’s responses will be ephemeral for the end user.

Read more in the [Moderating Apps on Discord Help Center article](https://support.discord.com/hc/en-us/articles/23957313048343-Moderating-Apps-on-Discord#h_01HZQQQEADYVN2CM4AX4EZGKHM).

###### Updated Defaults for New Apps

* Newly-created apps now default to having both "User Install" *and* "Guild Install" [installation contexts](https://docs.discord.com/developers/resources/application#installation-context) enabled. This can be updated in the **Installation** tab in an [app's settings](https://discord.com/developers/applications).
* Newly-created apps now default to using the "Discord Provided Link" [install link](https://docs.discord.com/developers/resources/application#install-links). This can be updated in the **Installation** tab in an [app's settings](https://discord.com/developers/applications).
* If Discord Provided Link is selected as the install link type, `application.commands` scope is added to both installation contexts.

### June 17, 2024

**Summary:** Premium Apps: New Premium Button Style & Deep Linking URL Schemes

Introduces a new premium button style to be used with a sku_id which points to an active SKU.

#### Premium Apps: New Premium Button Style & Deep Linking URL Schemes

**New Premium Button Style**

Introduces a new `premium` [button style](https://docs.discord.com/developers/components/reference#button-button-styles) to be used with a `sku_id` which points to an active [SKU](https://docs.discord.com/developers/resources/sku#sku-object). This allows developers to customize their premium experience by returning specific subscription or one-time purchase products.

Learn more about using [button components with interactions](https://docs.discord.com/developers/components/reference#button).

> **Warning**
> This change deprecates Interaction Response Type 10

The `PREMIUM_REQUIRED (10)` interaction response type is now deprecated in favor of using custom premium buttons. This will continue to function but may be eventually unsupported. It is recommended to migrate your bots to use the more flexible [premium button component](https://docs.discord.com/developers/components/reference#button-button-styles).

Learn more about [gating features with premium interactions](https://docs.discord.com/developers/monetization/implementing-app-subscriptions#prompting-users-to-subscribe).

**Deep Linking URL Schemes for SKUs and Store**

Introduces two new url schemes for linking directly to the Application Directory. When these links are used in chat, they are rendered as rich embeds that users can interact with to launch an app's store or open a SKU detail modal.

* New [Store URL Scheme](https://docs.discord.com/developers/monetization/managing-skus#linking-to-your-store): `https://discord.com/application-directory/:appID/store`
* New [SKU URL Scheme](https://docs.discord.com/developers/monetization/managing-skus#linking-to-a-specific-sku): `https://discord.com/application-directory/:appID/store/:skuID`

### May 31, 2024

**Summary:** Auto Moderation Member Profile Rule

Auto Moderation Member Profile Rule

#### Auto Moderation Member Profile Rule

* Add Auto Moderation `MEMBER_PROFILE` rule [trigger\_type](https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-rule-object-trigger-types). This rule type will check if a member's profile contains disallowed keywords.
* Add Auto Moderation `BLOCK_MEMBER_INTERACTION` [action type](https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-action-object-action-types) currently available for the `MEMBER_PROFILE` rule [trigger\_type](https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-rule-object-trigger-types). This action will "quarantine" the member to some extent and prevent them from performing most interactions within a specific server.

### April 24, 2024

**Summary:** Premium Apps: One-Time Purchases and Store

Two new features are now available for Premium Apps: One-Time Purchases and Stores.

#### Premium Apps: One-Time Purchases and Store

Two new features are now available for Premium Apps: One-Time Purchases and Stores.

**One-Time Purchases**

* **Durable Items**: A one-time purchase that is permanent and is not subject to either renewal or consumption, such as lifetime access to an app's premium features.
* **Consumable Items**: A one-time, non-renewable purchase that provides access, such as a temporary power-up or boost in a game.

Learn more about [Implementing One-Time Purchases](https://docs.discord.com/developers/monetization/implementing-one-time-purchases).

**A Store for Your Premium App**

We have also introduced a Store for your Premium App to showcase your app subscriptions and one-time purchase items. You can now create a unique Store page within the developer portal and add your published subscription SKUs or one-time purchase SKUs to your store view, allowing your users to buy these items from your App Directory or Bot User Profile.

To explore these features, eligibility details, and how to enable monetization for your app, check out the [Monetization Overview](https://docs.discord.com/developers/monetization/overview).

**API Documentation Updates**

The following were added to our public Monetization documentation with this update:

* New [SKU Object Types](https://docs.discord.com/developers/resources/sku#sku-object-sku-types)
* New [Entitlement Object Types](https://docs.discord.com/developers/resources/entitlement#entitlement-object-entitlement-types)
* [Consume an Entitlement](https://docs.discord.com/developers/resources/entitlement#consume-an-entitlement) API endpoint
* `consumed` field on the [Entitlement](https://docs.discord.com/developers/resources/entitlement) resource

### April 23, 2024

**Summary:** Modify Guild Member flags field permissions

Update permissions necessary to modify the flags field when calling the Modify Guild Member endpoint.

#### Modify Guild Member flags field permissions

Update permissions necessary to modify the `flags` field when calling the [Modify Guild Member](https://docs.discord.com/developers/resources/guild#modify-guild-member) endpoint.

### April 02, 2024

**Summary:** CSV Export for Premium App Analytics

For apps with Monetization enabled, we have released the ability to export your SKU analytics to CSV.

#### CSV Export for Premium App Analytics

For apps with [Monetization](https://docs.discord.com/developers/monetization/overview) enabled, we have released the ability to export your SKU analytics to CSV. These exports allow you to use your preferred data tools to report on your premium offerings.

You can find the export at the bottom of the `Monetization → Analytics` tab of your app to export data points such as `sales_count`, `sales_amount`, `sales_currencies`, `cancellation_count`, `refund_amount`, and `refund_count`, aggregated by each of your offerings for the selected month.

### March 18, 2024

**Tags:** `Embedded App SDK`, `Activities`

**Summary:** Discord Activities: Developer Preview of the Embedded App SDK

Discord Developers can now build Activities!

#### Discord Activities: Developer Preview of the Embedded App SDK

Discord Developers can now build Activities!

Activities are interactive, multiplayer experiences that run in an iframe in Discord. In order to make the communication between your experience and Discord, we've introduced the Embedded App SDK to assist in communicating between your app and the Discord client.

* New [Discord Activities](https://docs.discord.com/developers/activities/overview) developer docs with a tutorial, code samples, development guides, and design principles.
* The Embedded App SDK is now available via [npm](https://npmjs.com/package/@discord/embedded-app-sdk) and [GitHub](http://github.com/discord/embedded-app-sdk).
* The [Embedded App SDK Reference](https://docs.discord.com/developers/developer-tools/embedded-app-sdk) is now available.

To learn more about how to get started building your own Activity, check out the [Activities Overview](https://docs.discord.com/developers/activities/overview).

### March 18, 2024

**Tags:** `User Apps`

**Summary:** User-Installable Apps Preview

Apps can now be installed to users—making them easier to install, discover, and access across Discord.

#### User-Installable Apps Preview

Apps can now be installed to users—making them easier to install, discover, and access across Discord. User-installed apps can be used across all of a user's servers, within their (G)DMs, and in DMs with the app's bot user.

When creating or updating your app, you can choose which installation types your app supports on the **Installation** page in your [app's settings](https://discord.com/developers/applications). To quickly get started, you can follow the new [Developing a User-Installable App tutorial](https://docs.discord.com/developers/tutorials/developing-a-user-installable-app) or read details about the new changes below.

This change introduces new concepts and fields across the API that apps will now encounter.

###### API Changes

**Concepts:**

* [Installation context](https://docs.discord.com/developers/resources/application#installation-context) defines how an app was installed: to a user, a guild (server), or both. Currently, apps will default to only support the guild installation context, but the default may change in the future.
* Commands can also support one or both installation contexts, with the default being the same as the app's supported installation context(s) at the time of command creation.
* [Interaction context](https://docs.discord.com/developers/interactions/application-commands#interaction-contexts) defines where a command can be used in Discord—within guilds, DM with your app's bot user, and/or within group DMs and DMs other than with your app's bot user.
* The installation flow for apps have been updated so users can select whether they want to install an app to their account or to a server.

**API Fields:**

* New `integration_types_config` field for [Applications](https://docs.discord.com/developers/resources/application#application-object) include the default scopes and permissions for app's supported installation contexts
* New `integration_types` and `contexts` fields for [Commands](https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-structure) are the supported [installation](https://docs.discord.com/developers/interactions/application-commands#installation-context) and [interaction](https://docs.discord.com/developers/interactions/application-commands#interaction-contexts) contexts (respectively) for the command. Read [command contexts](https://docs.discord.com/developers/interactions/application-commands#contexts) documentation for details.
* New `context` field for [Interactions](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-interaction-structure) indicates the [interaction context](https://docs.discord.com/developers/interactions/application-commands#interaction-contexts) where an interaction was triggered from.
* New `authorizing_integration_owners` field for [Interactions](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-interaction-structure) includes a mapping of installation contexts that the interaction was authorized for, to related snowflakes for that context. Read [Authorizing Integration Owners Object](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-authorizing-integration-owners-object) for details.
* `app_permissions` is now always serialized for interactions to indicate what [permissions](https://docs.discord.com/developers/topics/permissions#permissions-bitwise-permission-flags) your app has access to in the context its' responding. For (G)DMs with other users, it will include the `ATTACH_FILES | EMBED_LINKS | MENTION_EVERYONE`, and for DMs with the app's bot user it will also contain `USE_EXTERNAL_EMOJIS` for the bot’s DM
* New `interaction_metadata` on [Messages](https://docs.discord.com/developers/resources/message#message-object) that are created as part of an interaction response (either a response or follow-up). See [Message Interaction Metadata Object](https://docs.discord.com/developers/resources/message#message-interaction-metadata-object) for details.
* `dm_permission` field for [Commands](https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-structure) is deprecated. Apps should use `contexts` instead.
* `interaction` field for [Messages](https://docs.discord.com/developers/resources/message#message-object) is deprecated. Apps should use `interaction_metadata` instead.

###### Limitations and Known Issues

* During the preview, interaction responses for the user installation context will be forced to be ephemeral in servers with over 25  members. Forced ephemerality is enforced at the client-level, so your app does not need to manually pay attention to server size, and will not receive errors via the API.
* All [follow-up messages](https://docs.discord.com/developers/interactions/receiving-and-responding#followup-messages) are currently forced to be ephemeral in DMs
* Follow-up messages have a bug where they will not correctly respect user permissions

### March 15, 2024

**Tags:** `Breaking Change`

**Summary:** Guild Prune Requiring

The Get Guild Prune Count and Begin Guild Prune endpoints now require the MANAGE_GUILD permission alongside the existing KICK_MEMBERS requirement.

#### Guild Prune Requiring

The [Get Guild Prune Count](https://docs.discord.com/developers/resources/guild#get-guild-prune-count) and [Begin Guild Prune](https://docs.discord.com/developers/resources/guild#begin-guild-prune)
endpoints now require the `MANAGE_GUILD` permission alongside the existing `KICK_MEMBERS` requirement.

### February 12, 2024

**Summary:** Enforced Nonces on Create Message Endpoint

The Create message endpoint now supports an enforce_nonce parameter.

#### Enforced Nonces on Create Message Endpoint

The [Create message](https://docs.discord.com/developers/resources/message#create-message) endpoint now supports an `enforce_nonce` parameter. When set to true, the message will be deduped for the same sender within a few minutes. If a message was created with the same nonce, no new message will be created and the previous message will be returned instead. This behavior will become the default for this endpoint in a future API version.
