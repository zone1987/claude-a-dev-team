# Discord Social SDK — Core Concepts

Distilled from `docs.discord.com/developers/discord-social-sdk/core-concepts` and its 7 sub-pages,
retrieved 2026-08-26.

## Contents

- [What the SDK is](#what-the-sdk-is)
- [Core Features](#core-features)
- [Communication Features](#communication-features)
- [Development Rate Limits](#development-rate-limits)
- [Applying for Increased Rate Limits](#applying-for-increased-rate-limits)
- [Application Requirements for Increased Rate Limits](#application-requirements-for-increased-rate-limits)
- [Integration Overview](#integration-overview)
- [Platform Compatibility](#platform-compatibility)
- [OAuth2 Scopes](#oauth2-scopes)
- [Discord Social SDK on Mobile](#discord-social-sdk-on-mobile)
- [Release Cadence and Support](#release-cadence-and-support)
- [Change logs](#change-logs)

---

## What the SDK is

Source: `/discord-social-sdk/overview`, `/discord-social-sdk/core-concepts`.

The Discord Social SDK lets you integrate Discord-powered social features directly into your game:
friend lists, messaging, voice chat, and rich presence.

**Unlike a traditional SDK with built-in UI components, the Discord Social SDK provides access to raw
data**, allowing developers to create a fully customized experience that aligns with their game's
aesthetic. There are no shipped UI widgets — you build the UI.

Feature overview at platform level: the "Social Layer for Games" platform page
(`/developers/platform/social-layer`).

The SDK API reference (Doxygen) lives at
`https://discord.com/developers/docs/social-sdk/index.html`. Class pages follow the pattern
`https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1<ClassName>.html`.

**Communication features are available but capped with rate limits.** See
[Development Rate Limits](#development-rate-limits).

### Getting help

- The DDevs Discord Server (`https://discord.gg/discord-developers`), channel `#social-sdk-dev-help`.
- File a ticket with Developer Support: `https://dis.gd/social-sdk`.

---

## Core Features

Source: `/discord-social-sdk/core-concepts/core-features`.

The Discord Social SDK offers a range of features to enhance social interactions within games.

### Provisional Accounts

Provisional accounts let players use social features in your game **without linking a Discord
account**, so all players can have a consistent gameplay experience.

Upstream cross-references (all covered in PROVISIONAL-ACCOUNTS.md of this skill):

| Development Guides |
| --- |
| Provisional Accounts Overview |
| Bot Token Endpoint |
| Configuring Identity Providers |
| External Credentials Exchange |
| Public Client Integration |
| Managing Provisional Accounts |
| Merging Accounts |
| Unmerging Accounts |

| Design Guidelines |
| --- |
| Provisional Accounts (see DESIGN-GUIDELINES.md) |

### Account Linking

Account linking allows a game to authenticate users with their Discord credentials, gaining access to
social features like friends, chat, and presence. **This process uses OAuth2 authentication.**

Platform-level overview: `/developers/platform/account-linking`.

| Development Guides |
| --- |
| Account Linking from Your Game (`account-linking-with-discord`) |
| Account Linking on Mobile |
| Account Linking on Consoles |
| Account Linking from Discord Entry Points (`account-linking-from-discord`) |

| Design Guidelines |
| --- |
| Signing in with Discord |
| Consoles |

All five are in ACCOUNT-LINKING.md; the two design pages are in DESIGN-GUIDELINES.md.

### Friend System & Relationships

The SDK models friendships and relationships in two ways:

- **Discord Friends**: persistent across all games.
- **Game-Specific Friends**: limited to the current game.

| Development Guides |
| --- |
| Creating a Unified Friends List |

| Design Guidelines |
| --- |
| Unified Friends List |
| Game Friends |

### Presence & Rich Presence

Presence refers to a user's online status, while Rich Presence provides game-specific activity data:

- Displays if a user is online, idle, or offline.
- Shows detailed game stats (e.g., what level they're playing and time played).
- Allows users to send game invites through Discord and in-game.

| Development Guides |
| --- |
| Setting Rich Presence |

| Design Guidelines |
| --- |
| Status & Rich Presence |

---

## Communication Features

Source: `/discord-social-sdk/core-concepts/communication-features`.

The Discord Social SDK provides communication features to enhance player interaction in your game:
messaging, voice chat, and in-game lobbies.

**Warning (upstream): the following communication features are available for development and testing,
but their usage is capped with a rate limit.**

### Messaging & Communication

Users can communicate via direct messages (DMs) and voice calls:

- **DMs**: one-on-one private chat (`MessageHandle`).
- **Calls**: real-time voice communication inside a game lobby (`Call`).

| Development Guides |
| --- |
| Sending Direct Messages |
| Managing Voice Chat |

| Design Guidelines |
| --- |
| Direct Messages |

### Lobbies & In-Game Chat

A lobby is a virtual space where players can interact through voice and text chat.

- Your game controls lobbies, which can have different membership rules.
- Integrated voice chat allows real-time communication among players in a session.

| Development Guides |
| --- |
| Managing Lobbies |

### Linked Channels

Games can link in-game chat with Discord's server-based text channels in their UI, allowing players
to chat in a Discord server without leaving the game.

| Development Guides |
| --- |
| Linked channels |

| Design Guidelines |
| --- |
| Linked channels |

---

## Development Rate Limits

Source: `/discord-social-sdk/core-concepts/communication-features#rate-limits`.

Prior to successful approval to increase rate limits, communication features have the following
restrictions:

- **Lobby Create/Join operations:** 100 requests every 2 hours.
- **Lobby Update operations:** 100 requests every 2 hours.
  - This includes adding/removing members, updating metadata, and creating Discord server invites for
    linked channels.
- **Lobby Linking operations:** 20 requests every 2 hours.
  - This includes creating or deleting a linked channel.
- **Sending Messages to Lobby operations:** 100 requests every 2 hours.
- **Sending Direct Message operations:** 100 requests every 2 hours.

**These are per-application rate limits, not per-user.**

These limitations are designed to provide sufficient capacity for development, testing, and
small-scale demos while ensuring system stability. Once you gain full access through the rate limit
increase application process, these restrictions are increased, allowing your game to scale to
production levels.

Handling rate-limit errors in code: see HOW-TO-GUIDES.md → Handle Rate Limits.

---

## Applying for Increased Rate Limits

(Upstream anchors: `#applying-for-increased-rate-limits-for-production-releases`, and the legacy
alias `#applying-for-rate-limit-removal`.)

To apply for increased rate limits on Discord Social SDK communication features, you must meet the
requirements in [Application Requirements](#application-requirements-for-increased-rate-limits).
Then:

1. Open the Application page of the Developer Portal (`https://discord.com/developers/applications`).
2. Open the Application you want to apply for rate limit increase.
3. Under the **Discord Social SDK** heading in the sidebar, click the **Comms Access** button
   (`https://discord.com/developers/applications/select/social-sdk/comms-access`).
4. Fill out the application form with the required information and supporting materials.

**Tip:** video capture provided to the application should be in URL format, hosted on a file or
video-sharing service of your choice as an unlisted video.

---

## Application Requirements for Increased Rate Limits

(Upstream anchor alias: `#application-requirements-for-rate-limit-removal`.)

The five requirement areas you must meet before submitting your game for approval to unlock Discord
Social SDK text and/or voice communications for full release:

1. **Minimum required feature set:** your game must have integrated core Discord Social SDK features:
   Discord Account Linking, Rich Presence, Game Invites, and Unified Friends List (including full
   access to Discord friends).
2. **Feature Functionality:** the Discord Social SDK features you choose to integrate must have
   end-to-end functionality — all user interactions can be completed, work as intended across both
   game and Discord clients, and resolve edge cases (such as user denial of options and failure
   states) correctly.
3. **Feature Access and Conveyance:** integrations must include the option for users to link their
   Discord account, and make it accessible and easily understandable for players to activate.
4. **Supporting Materials:** specific documentation of your game for review, such as a capture of
   integration and development timeline.
5. **Age-restricted user protection:** confirm that you have appropriate measures in place for
   players' access to the SDK features in your game, depending on their age.

These requirements detail the **minimum bar** to be eligible for Social SDK communications usage at
scale. Compliance with the Social SDK Terms is also required
(`https://support-dev.discord.com/hc/en-us/articles/30225844245271-Discord-Social-SDK-Terms`).
Discord may approve or deny access after review, and additional terms may apply.

### Minimum Required Feature Set

In order to unlock Discord text and/or voice communications for full release, integrations of the
Social SDK must include **all** of the following features at a minimum. Developers are welcome (and
encouraged) to take advantage of any SDK features beyond these minimum requirements.

**Exception: Prohibited Off-Platform Interactions by Sony.** For integrations experienced on Sony
Platforms (e.g. PlayStation 5):

1. **Do not allow access to Account Linking** entry points.
2. **Do not allow access to Linked Channels**.
3. **Limit messaging and Invites to other players currently playing** the game.
4. **Do not display off-platform presence and logos** (including Discord).

#### Option for Discord Account Linking

**Players must have the opportunity to link their Discord account in-game.** This ensures players can
access the full Social SDK-powered experience, and connects your game to a player's existing social
network. Account linking must also be readily accessible (see
[Feature Access and Conveyance](#feature-access-and-conveyance)).

#### Rich Presence and Discord Joins

**Discord Users must be able to see Rich Presence updates for Discord-linked player accounts and join
their game via Ask to Join.** This feature drives organic discovery and social engagement by showing
friends what players are doing and creating opportunities for spontaneous social interaction and game
sessions.

#### Full Access to Discord Friends

**Account-linked players must have their Discord friends accessible to them in-game, with supporting
UI to take actions like messaging, inviting, blocking, and ignoring.** This can be accomplished as a
Unified Friends List which shows status across platforms, or as a simple in-game Discord friends
list. **Games should never copy and store Discord friend information** (i.e. a player unlinking their
Discord account should automatically remove Discord friend information in-game).

"Full access to Discord friends" means:

1. Players can view all their Discord friends directly within the game immediately after account
   linking.
2. Viewing Discord friends in an in-game friends list is not dependent on any actions other than
   account linking.
3. Discord friends are displayed alongside or integrated with in-game friends.
4. From an in-game friends list, Discord friends can be invited, blocked, or ignored, and messaged if
   the game supports Direct Messages.
5. Discord social features unlock for players at least in parity with other social features in game.
6. Players do not need to manually search for or re-add their Discord friends using in-game friend
   codes or usernames.

The intent is that Discord account linking *immediately grants access to the player's existing, full
Discord social graph* within the game.

### Feature Functionality

**All integrated Social SDK features (whether required as a part of the minimum feature set or not)
must have at a minimum base level functionality for their intended use.** This is a **separate
requirement in addition to the minimum feature set**. "Base level functionality" means each
integrated feature's end-to-end user flow is **completable** and **resolves edge cases** (user denial
of options and failure states) correctly.

#### Discord Account Linking

**Intended Use:** connect a player's game account with their Discord account to enable social features
and cross-platform functionality.

**Complete In-Game User Flow:**

1. Player encounters sign-in prompt (at game start, friends list access, or feature interaction).
2. Player clicks Discord sign-in button.
3. Authorization flow launches (Overlay > Discord Client > Browser fallback).
4. Player completes OAuth authorization on Discord.
5. Game receives authorization confirmation.
6. Success state displays in-game confirming connection.
7. Social features become available and populate with Discord data.

**Edge Cases & Recovery Flows:**

- **User declines authorization:** return to game normally with a provisional account; maintain access
  to sign-in option.
- **Authorization fails/times out:** show clear error message with retry option.
- **User wants to disconnect:** provide deauthorization option in-game and maintain game
  functionality post-disconnect.

#### Rich Presence

**Intended Use:** display detailed, real-time information about a player's in-game activity on their
Discord profile, allowing friends to see what they're doing and potentially join their session.

**Complete In-Game User Flow:**

1. Player launches game and performs actions (enters lobby, starts match, joins party, etc.).
2. Game feeds Rich Presence update to Discord via the SDK (e.g. "In lobby").
3. Rich Presence appears on player's Discord profile with current activity details.
4. Discord friends can view the presence information.
5. Discord Friends can "Ask to Join" or receive direct invites.
6. Game feeds additional Rich Presence updates to Discord via the SDK as the player's in-game status
   changes (e.g. "Looking for a match", "In a match", etc).
7. On game shutdown, Discord automatically handles clearing player's Rich Presence.

**Edge Cases & Recovery Flows:**

- **Network connectivity issues:** queue presence updates and retry when connection restored.
- **Active and inactive clients:** invites can complete even when one player doesn't have the game
  client open on acceptance.

#### Unified Friends List

**Intended Use:** combine Discord friends and in-game relationships into a single, organized friends
list that shows comprehensive social connections.

**Complete In-Game User Flow:**

1. Player opens their in-game friends list.
2. Game UI quickly populates friends in an organized list showing:
   - In-game friends (always visible)
   - "Online Elsewhere" section with Discord friends not currently in-game
   - Appropriate status indicators and Discord badges
3. Player interacts with friends in list (message, invite, block, view profile).
4. Friends list updates dynamically in real time as statuses change.
5. Player can add/remove friends through the interface.

**Edge Cases & Recovery Flows:**

- **Friend removal:** handle removal across both game and Discord systems appropriately.
- **Loading failures:** show loading states and error messages for failed friend data retrieval.
- **Special characters:** non-standard characters in Discord usernames populate as expected.
- **Unlinking Discord:** player's in-game friends list removes Discord friend entries when they unlink
  their Discord account.

#### Direct Messages through Discord

**Intended Use:** enable seamless messaging between players across game platforms through Discord,
maintaining conversation continuity.

**Complete In-Game User Flow:**

1. Player selects friend to message from an in-game friends list or other interface.
2. Message interface opens showing chat history (if available).
3. Player composes and sends message.
4. Message appears in both the game interface and Discord (for linked users).
5. Messages from Discord appear in-game with Discord visual notation.
6. Conversation continues seamlessly across platforms.

**Edge Cases & Recovery Flows:**

- **Message delivery failure:** show retry options and clear error states.
- **Unsupported media:** display placeholder with external link icon for rich media.
- **Blocked users:** respect Discord blocking relationships and show appropriate messaging.
- **Network issues:** queue messages locally and sync when connection restored.

#### Linked Channels

**Intended Use:** link in-game group chats to Discord text channels, enabling persistent conversations
that flow between game platforms through Discord.

**Complete In-Game User Flow:**

1. Player with Discord server admin & game chat admin permissions accesses channel linking option in
   group chat interface.
2. Channel selection interface opens showing available Discord servers/channels.
3. Player selects appropriate text channel (with proper permissions).
4. System shows setup warning if linking to restricted channel.
5. Link establishes successfully with confirmation.
6. Messages flow bidirectionally between game and Discord.
7. Persistent entrypoint shows linked channel info and management options.

**Edge Cases & Recovery Flows:**

- **Insufficient permissions:** show clear error about channel management requirements.
- **No available channels:** provide guidance on creating or accessing appropriate channels.
- **Link establishment failure:** show retry options and clear error messaging.
- **User wants to unlink:** provide confirmation dialog and clean removal process.

#### Voice Communications

**Intended Use:** provide high-quality voice chat integration that works seamlessly between game
platforms through Discord.

**Complete In-Game User Flow:**

1. Player joins voice-enabled game session/party.
2. Voice interface becomes available with Discord-powered audio.
3. Player can mute/unmute, adjust volume, see speaking indicators.
4. Voice streams work for individual users with clear audio quality.
5. Player can leave voice.

**Edge Cases & Recovery Flows:**

- **Voice server unavailable:** provide clear error messaging and retry mechanisms.
- **User leaves voice:** clean up voice states and update interfaces appropriately.

### Feature Access and Conveyance

#### Discord Account Linking (access)

**The option for players to link their Discord account must have top-level surfacing in-game.** Social
SDK integrations must not only include account linking, but also make it accessible and easily
understandable for players to activate and deactivate.

**Access Requirements:**

- The account linking can be started **within two clicks or button presses of social features
  becoming available to players in game**.

Example flow:

1. Player launches the game executable, and the game loads to its main menu.
2. Player opens in-game Friends menu (first click).
3. Player selects Find Friends on Discord (second click), which starts the OAuth process to connect
   their Discord account.

Example flow:

1. Player launches the game executable for the first time, and the game loads to its main menu.
2. Player selects New Game (first click).
3. Player is presented with a modal listing the benefits of linking their Discord account with options
   to "Sign in with Discord" or "Not Now".
4. Player selects Sign in with Discord (second click), which starts the OAuth process to connect their
   Discord account.

Example flow:

1. Player launches the game executable, and the game loads to its main menu.
2. Player sees they have a new message in-game.
3. Player selects the mailbox to check their in-game messages (first click).
4. Player is presented with their first game message listing the benefits of linking their Discord
   account with option to "Sign in with Discord".
5. Player selects Sign in with Discord (second click), which starts the OAuth process to connect their
   Discord account.

Example flow:

1. Player launches the game executable, and the game's first time user experience (FTUE) tutorial
   begins.
2. Player plays through tutorial gameplay.
3. Player completing tutorial gameplay, player sees the in-game chat unlock for them and selects the
   chat (first click).
4. Player is presented with a modal listing the benefits of linking their Discord account with options
   to "Sign in with Discord" or "Not Now".
5. Player selects Sign in with Discord (second click), which starts the OAuth process to connect their
   Discord account.

Further access requirements:

- The entry point for account linking is discoverable by players through normal expected play (i.e.
  not buried in sub-menus or requiring unintuitive right-click access).
- If the game has a social tab or friends list, account linking can be started there.
- Linking a Discord account is surfaced in parity with other platform-linking options.
- The location for account linking is located in a **persistent and accessible** area in-game (e.g.
  Game Settings, Accounts menus).
- The entry point for account linking is visually persistent within its associated menu location (i.e.
  it can't be a one time pop up that players can't access again).
- The option to unlink accounts is also surfaced in-game in a persistent and easily accessible manner.
- Users without linked accounts must have an associated token path for handling social features (see
  Provisional Accounts design guidelines).

**Conveyance Requirements:**

- Developers must provide contextual education about Discord account-linking benefits **before** users
  encounter the authorization flow.
- Acceptable contextual education looks like:
  - **Modal or informational screen** that explains specific benefits the player will receive (e.g.,
    "Chat with friends here and on Discord," "See what your friends are playing," "Join friends' games
    directly").
  - **Contextual tooltips or hints** near social features that explain how they improve with Discord
    linking.
  - **In-game messaging** that appears when players interact with limited social features, explaining
    how linking would enhance the experience.

**Warning: Discord Account Linking entry points are prohibited on Sony platforms.**

#### Direct Messages through Discord (conveyance)

If you've chosen to integrate Direct Messages through Discord in your game, **Direct Messages must be
identifiable as coming from Discord**, and **players must know when their messages are showing up in
Discord**.

**Conveyance Requirements:**

- Cross-platform DMs need to be identified as Discord-specific through visual indicators (e.g. Discord
  logo/badge next to sender name, contextual information on hover about the message source).
- Players must know when their messages are showing up in Discord through clear visual feedback when
  composing or sending messages.
- The messaging interface must indicate the cross-platform nature of the conversation (e.g., "This
  conversation syncs with Discord" or similar messaging).

### Supporting Materials

To unlock Discord text and/or voice communications for full release, Social SDK integrations must have
accompanying supporting materials in your application. Submit your application and supporting
materials under your application in the Developer Portal.

**Warning: for integrations available on multiple platforms including Sony platforms, submit materials
that reflect your non-Sony platform user experience.** For example: Example Studio's *Wumpus Wars* is
available to players on Sony PlayStation 5 and Xbox Series S and Xbox Series X. Example Studio submits
the feature list and *Wumpus Wars* capture for Xbox.

#### List of SDK Features Integrated

Provide a comprehensive list of all Discord Social SDK features implemented in your game, such as:

- Discord Sign-in (Account Linking)
- Rich Presence
- Game Invites and/or Discord Joins
- Unified Friends List
- Direct Messages through Discord
- Voice Communications
- Text Communications (Linked Channels)

#### Release Timeline

Indicate the anticipated release date, and the current development status of your Discord integration:

- Concept / Prototype
- Production (Alpha)
- Post-product (Beta)
- Released (Already commercially available)

#### Capture of Integrated Features

Acceptable format: URL link.

- **1-5 minute video capture** of the complete user flow covering each SDK feature integrated.
- Videos must demonstrate end-to-end user flow as outlined in Feature Functionality.
- Show both successful flows and how negative options (errors, user denials) are handled.
- Include clear narration or on-screen text explaining each step.
- Ensure video quality allows reviewers to clearly see UI elements and user interactions.

### Age-restricted User Protection

You must comply with all age requirements under the Social SDK Terms. This includes ensuring that
**only people who are at least 13 years old and meet the minimum age requirements in their country**
can access Social SDK features integrated in your game.

### Confirmation of Standards Compliance

With your application submission, you confirm that you have met the requirements detailed above.

---

## Integration Overview

Source: `/discord-social-sdk/core-concepts/integration-overview`.

To implement the Discord Social SDK, developers for all platforms will generally follow these steps:

1. **Import the SDK.**
2. **Initialize the SDK:**
   - Create a `Client` instance.
   - Set up event listeners to monitor SDK events and callbacks.
3. **Authenticate users with flexible account options:**
   - Create and manage provisional accounts for users who don't have or want a Discord account
     (`Client::GetProvisionalToken`).
   - Link an existing Discord account via OAuth (`Client::Authorize`).
4. **Implement social features:**
   - Implement unified friends list and relationships.
   - Use rich presence for game activity updates.
   - Set up lobbies for multiplayer interaction and game invites.
   - Manage direct message, linked channels, and voice communication.
5. **Handle events & API calls:**
   - Listen for changes in friend lists, presence updates, and chat messages.
   - Use Discord's APIs to update statuses, send messages, and manage connections.

This page is explicitly a conceptual overview; the step-by-step setup lives in the getting-started
guides (GETTING-STARTED-CPP.md, GETTING-STARTED-UNITY.md, GETTING-STARTED-UNREAL.md).

Referenced SDK symbols and their reference-doc anchors:

- `Client` — `classdiscordpp_1_1Client.html#a91716140c699d8ef0bdf6bfd7ee0ae13`
- `Client::Authorize` — `classdiscordpp_1_1Client.html#ace94a58e27545a933d79db32b387a468`
- `Client::GetProvisionalToken` — `classdiscordpp_1_1Client.html#a8003130b6c46e54ac68442483bf0480c`

---

## Platform Compatibility

Source: `/discord-social-sdk/core-concepts/platform-compatibility`.

Download instructions per platform are in the Getting Started guides.

### Game Engine and Language

| Integration    | Supported Version |
| -------------- | ----------------- |
| Standalone C++ | C++20+            |
| Unity          | 2021.3+           |
| Unreal Engine  | 5.5+              |

- **PlayStation 4 / PS5 exception:** if you're targeting PlayStation 4, or PlayStation 5 with a PS5
  SDK older than 13.000, the Discord Social SDK still supports **C++17**. All other platforms require
  C++20.
- Prior to Social SDK release **1.9**, C++17 is the minimum supported version.

### Platforms

| Platform         | Supported Versions | Support Level       | Standalone C++ | Unreal Engine | Unity |
| ---------------- | ------------------ | ------------------- | -------------- | ------------- | ----- |
| **Desktop**      |                    |                     |                |               |       |
| Windows (x64)    | 10+                | Generally Available | yes            | yes           | yes   |
| Windows (ARM64)  | 11+                | Generally Available | yes            | no            | no    |
| macOS (x64)      | 10.5+              | Generally Available | yes            | no            | yes   |
| macOS (ARM64)    | 11+                | Generally Available | yes            | no            | yes   |
| Linux            | \*glibc 2.31+      | Experimental        | yes            | yes           | yes   |
| **Mobile**       |                    |                     |                |               |       |
| Android          | 7.0+               | Generally Available | yes            | yes           | yes   |
| iOS              | 15.1+              | Generally Available | yes            | yes           | yes   |
| **Console**      |                    |                     |                |               |       |
| Xbox One         | GDK 241000-260400  | Experimental        | yes            | yes           | no    |
| Xbox Series X\|S | GDK 241000-260400  | Generally Available | yes            | yes           | yes   |
| PlayStation 4    | OS 11.500-12.500   | Experimental        | yes            | yes           | no    |
| PlayStation 5    | OS 10.000-13.000   | Generally Available | yes            | yes           | yes   |

(Upstream uses a check mark for supported and a cross for unsupported; rendered here as yes/no.)

- \* There are too many Linux distributions to test, but most distros with glibc 2.31, e.g. Ubuntu
  20.04, or later should work.
- Building for iOS or Android? See
  [Feature Availability on Mobile](#feature-availability-on-mobile) for mobile-specific setup
  requirements and behavior differences.
- **Each Social SDK release supports roughly the last 18 months of Xbox and PlayStation OS SDK
  versions.** See [Console OS SDK Support](#console-os-sdk-support) for how the window rolls forward
  at each release.
- To use the Discord Social SDK in your console games, you will need to **request middleware approval
  and be an approved developer for the target console**. Reference article:
  `https://support-dev.discord.com/hc/en-us/articles/30209074764183`.

**Warning — Exception: Prohibited Off-Platform Interactions by Sony.** For integrations experienced on
Sony Platforms (e.g. PlayStation 5):

1. **Do not allow access to Account Linking** entry points.
2. **Do not allow access to Linked Channels**.
3. **Limit messaging and Invites to other players currently playing** the game.
4. **Do not display off-platform presence and logos** (including Discord).

---

## OAuth2 Scopes

Source: `/discord-social-sdk/core-concepts/oauth2-scopes`.

This page covers OAuth2 scopes specific to the Discord Social SDK. For the full list of Discord API
OAuth2 scopes (bots, webhooks, etc.), see the OAuth2 topic guide
(`/developers/topics/oauth2#shared-resources-oauth2-scopes`) — call the Skill tool with
"discord-oauth2".

OAuth2 scopes define the level of access your app has to a user's Discord account.

What OAuth scopes are available to your integration are set via `AuthorizationArgs::SetScopes` on
`AuthorizationArgs`, which is passed to `Client::Authorize` on Social SDK authentication.

### Default Presence Scopes

At a minimum, the Social SDK uses the following scopes to use features like rich presence and friends
list:

- `openid`
- `sdk.social_layer_presence`

The default presence features include:

- Account Linking
- Provisional Accounts
- Friend System & Relationships
- Presence & Rich Presence

Helper method `Client::GetDefaultPresenceScopes` returns `openid sdk.social_layer_presence`.

**Warning: with only the default presence scopes, your game will not be able to use any of the limited
access communications features.**

### Default Communication Scopes

The communications features are currently available but have limited access. Those features
**require** the scope `sdk.social_layer`, which includes the `sdk.social_layer_presence` scope but
also allows your app to use those limited features on behalf of the user.

- `openid`
- `sdk.social_layer`

These communication features include:

- Messaging & Communication
- Lobbies & In-Game Chat
- Linked Channels

Helper method `Client::GetDefaultCommunicationScopes` returns `openid sdk.social_layer`.

If your game requires additional scopes, you can add them to the default scopes to authorize
additional access from your users. **You should only add scopes that are necessary for your game to
function.** Requesting unnecessary scopes can lead to user distrust and may result in users not
linking their Discord account.

### OAuth2 Client Types

OAuth2 has two client types: **Confidential** and **Public**. **Most games will not want to ship with
Public Client enabled.**

Some Social SDK methods require your Discord application to be a **Public Client**. These methods also
have server-side alternatives that you can use with a **Confidential Client**.

- Using confidential clients with proper secret management for production applications is generally
  recommended.
- Public clients cannot securely store client secrets.
- Your security team should review this setting and authentication flows before releasing your game.

Reference: `https://oauth.net/2/client-types`.

Referenced SDK symbols:

- `AuthorizationArgs` — `classdiscordpp_1_1AuthorizationArgs.html#adb47ac55258db29d4cb8a2c506093eed`
- `AuthorizationArgs::SetScopes` — `classdiscordpp_1_1AuthorizationArgs.html#aa3714d11a196e0d71c8c1cf38c506d92`
- `Client::Authorize` — `classdiscordpp_1_1Client.html#ace94a58e27545a933d79db32b387a468`
- `Client::GetDefaultCommunicationScopes` — `classdiscordpp_1_1Client.html#a71499da752fbdc2d4326ae0fd36c0dd1`
- `Client::GetDefaultPresenceScopes` — `classdiscordpp_1_1Client.html#a7648bd1d2f7d9a86ebd0edb8bef12b5c`

---

## Discord Social SDK on Mobile

Source: `/discord-social-sdk/core-concepts/mobile`.

### Mobile platform support

The Discord Social SDK is **Generally Available** on both mobile platforms:

| Platform | Supported Versions | Standalone C++ | Unreal Engine | Unity |
| -------- | ------------------ | -------------- | ------------- | ----- |
| Android  | 7.0+               | yes            | yes           | yes   |
| iOS      | 15.1+              | yes            | yes           | yes   |

### Feature Availability on Mobile

All Discord Social SDK features are available on mobile. Mobile-specific setup or behavior differences
where they apply:

| Feature | Mobile-Specific Notes |
| --- | --- |
| Provisional Accounts | No special considerations |
| Account Linking | Requires deep linking (`discord-APP_ID:/authorize/callback`). Discord mobile app launches first for authentication, falls back to browser if not installed. See Account Linking on Mobile. |
| Friends & Relationships | No special considerations |
| Rich Presence | On iOS, **requires account linking** — you cannot publish presence without linking first. On Android, presence can also be published **without** account linking, as on desktop, if the Discord app is installed and signed in. See Rich Presence Without Authentication. |
| Game Invites | Requires https URL configured in Developer Portal General tab and specifying supported mobile platforms. See Supporting Mobile Game Invites. |
| Direct Messages | No special considerations |
| Lobbies & In-Game Chat | No special considerations |
| Voice Chat | Request microphone permissions. See platform-specific setup: iOS (Set Microphone Usage Description) and Android (Android Permissions), both in ACCOUNT-LINKING.md → Account Linking on Mobile. |
| Linked Channels | No special considerations |

### Mobile prerequisites

Before integrating on mobile, make sure you have:

- A Discord application with the Social SDK enabled. See the Getting Started guides to create your
  team, application, and enable the SDK.
- A mobile OAuth2 redirect URI configured in the format `discord-YOUR_APP_ID:/authorize/callback`
  (replace `YOUR_APP_ID` with your Discord application ID).
- Your development environment set up for your target platform (Xcode for iOS, Android Studio for
  Android).

**Tip — reduce binary size:** you can reduce the SDK's installation size on mobile by excluding Krisp
noise cancellation. See VOICE-CHAT.md → Excluding Krisp to Reduce Installation Size.

### Choose Your Getting Started Path

- **Standalone C++** — for custom engines or standalone applications targeting iOS and Android.
- **Unity** — for Unity projects building to mobile.
- **Unreal Engine** — for Unreal Engine projects building to mobile.

### Mobile samples

**Unity Mobile Sample.** The Unity sample for the Discord Social SDK
(`https://github.com/discord/social-sdk-unity-sample`) includes a mobile scene
(`Assets/Scenes/Mobile.unity`) that runs on Android and iOS. It contains drop-in prefabs with both
code and UI, with all mobile-specific configuration already set up:

- Mobile redirect URI (`discord-APP_ID:/authorize/callback`) registration
- Build processors that auto-inject the redirect scheme into Android manifest and iOS `Info.plist`
- Portrait-optimized UI that reuses the same Discord SDK integration as the desktop scene

Build instructions: the **Mobile Setup** section of the sample's README
(`https://github.com/discord/social-sdk-unity-sample#mobile-setup`).

[Video: Unity mobile sample walkthrough — `unity-mobile-sample.mov`, hosted on Discord's CDN.]

---

## Release Cadence and Support

Source: `/discord-social-sdk/core-concepts/release-cadence-and-support`.

### Release Schedule

Discord ships **three minor releases of the Discord Social SDK each year**, in **April, July, and
November**. This cadence aligns with the release windows for console OS SDKs so that each Discord
Social SDK release can pick up the most recent supported console SDK versions.

Between minor releases, patch releases are published as needed.

### Supported Version Window

**Hotfix patches** — bug fixes and security fixes — are provided for the **five most recent minor
versions** of the Discord Social SDK. Older versions are End-of-Life (EOL) and will not receive
further updates.

To receive a patch fix on an EOL version, upgrade to a supported release first.

| Version         | Status              |
| --------------- | ------------------- |
| 1.10            | Supported — current |
| 1.9             | Supported           |
| 1.8             | Supported           |
| 1.7             | Supported           |
| 1.6             | Supported           |
| 1.5 and earlier | End-of-Life         |

### Console OS SDK Support

New Xbox and PlayStation OS SDK support ships in **new minor Social SDK releases only** (the three
minor releases per year). They are **not** backported to older Social SDK versions as patches.

Each Social SDK release bundles roughly the last **18 months** of console OS SDK versions — from
whatever Xbox GDK or PlayStation OS was current ~18 months before the release, up through the latest
available at release time. Console OS SDK versions older than that window are dropped at each new
Social SDK release.

In practice:

- If you need the latest Xbox or PlayStation platform SDK, upgrade to the latest Social SDK release.
- Already-shipped Social SDK releases continue to support the console OS SDK versions they were
  originally built with — support for console OS SDKs is neither added nor removed from already
  shipped versions.

This model applies from the **1.10 release (July 2026)** onward. Releases **1.6–1.9** keep the console
OS SDK support they originally shipped with.

The minimum supported Xbox and PlayStation platform SDK versions for the current Social SDK release
are listed in [Platform Compatibility](#platforms).

### End-of-Life Process

When a new minor version of the Social SDK is released, the oldest version in the support window rolls
off and reaches End-of-Life:

1. It is removed from the supported version table.
2. No new hotfix patch builds are produced for that version.
3. Developers on that version should upgrade to the latest supported version.

EOL transitions are announced in the Change Log entry (`/developers/change-log`) for the corresponding
minor release.

### What's Covered

Within the supported Social SDK version window, hotfix patches for a minor version may include:

- Bug-fix and stability hotfix patches
- Security hotfix patches

### What's Not Covered

The following are **not** provided for older minor versions of the Social SDK:

- New feature development
- Backports of features introduced in a newer minor version
- Backports of support for newer console OS SDK versions

---

## Change logs

Upstream per-page change logs, preserved verbatim.

**Core Concepts index:**

| Date           | Changes                   |
| -------------- | ------------------------- |
| July 21, 2025  | restructure core concepts |
| June 30, 2025  | restructure oauth scopes  |
| March 17, 2025 | initial release           |

**Core Features:**

| Date          | Changes         |
| ------------- | --------------- |
| July 21, 2025 | initial release |

**Communication Features:**

| Date          | Changes                    |
| ------------- | -------------------------- |
| July 7, 2026  | clarify comms requirements |
| July 21, 2025 | initial release            |

**Integration Overview:**

| Date          | Changes         |
| ------------- | --------------- |
| July 21, 2025 | initial release |

**Platform Compatibility:**

| Date           | Changes                                                             |
| -------------- | ------------------------------------------------------------------- |
| August 3, 2026 | updated console OS SDK version windows for Social SDK 1.10          |
| May 26, 2026   | added console minimum versions; linked to Release Cadence & Support |
| May 20, 2026   | Added Game Engine and Language section.                             |
| July 21, 2025  | initial release                                                     |

**OAuth2 Scopes:**

| Date          | Changes         |
| ------------- | --------------- |
| July 21, 2025 | initial release |

**Mobile:**

| Date           | Changes                                                |
| -------------- | ------------------------------------------------------ |
| August 3, 2026 | Noted unauthenticated Rich Presence support on Android |
| July 14, 2026  | Initial release                                        |

**Release Cadence & Support:**

| Date           | Changes                      |
| -------------- | ---------------------------- |
| August 3, 2026 | updated for the 1.10 release |
| May 26, 2026   | initial release              |
