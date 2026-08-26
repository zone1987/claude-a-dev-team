---
name: discord-social-sdk
description: "Discord Social SDK for games: provisional accounts, account linking, lobbies, relationships, voice. Use when the request names the Discord Social SDK or a provisional account."
---

# Discord Social SDK

Discord-powered social features inside a game: friends, messaging, voice, lobbies and rich presence.
**The SDK exposes raw data, not UI components** — you build every surface yourself, which is why the
design guidelines carry as much weight as the API reference.

The C++ namespace is `discordpp`; Unity exposes `Discord.Sdk`, Unreal the `DiscordPartnerSDK` plugin
with `UDiscord*` types.

## The client and account model in brief

**One `Client` per player.** Construct it, attach `AddLogCallback` and `SetStatusChangedCallback`,
supply a token with `UpdateToken`, then `Connect`. Nothing works until the status reaches
`Client::Status::Ready`. In standalone C++ you must pump `discordpp::RunCallbacks()` every tick; the
Unity plugin and Unreal's `DiscordLocalPlayerSubsystem` do it for you.

**Two ways a player gets an identity, and they converge:**

- **Provisional account** — a limited Discord account your game owns, created from your own user ID
  (`POST /partner-sdk/token/bot`, the recommended path) or an external identity (OIDC, Steam, EOS,
  Unity, Apple, PSN). No Discord account required; tokens last 7 days.
- **Linked Discord account** — OAuth2 with `Client::Authorize` plus PKCE. `openid` +
  `sdk.social_layer_presence` buys presence and friends; **communication features require
  `sdk.social_layer`**.
- **Merging** turns the first into the second, carrying friends, lobbies and DM history. **Unmerging
  (including a Discord ban) reverses it into a fresh provisional account — without DM history.**
  Discord's recommended architecture is provisional-first, with your own auth provider as the anchor.

**Communication features are rate-limited until you apply for production access:** 100 lobby
create/join, 100 lobby update, 20 lobby link, 100 lobby message and 100 DM operations per 2 hours,
per application — not per user.

## Reference map

- **[references/CORE-CONCEPTS.md](references/CORE-CONCEPTS.md)**: all 8 core-concepts pages — feature
  overview, the full 12-platform compatibility matrix, both OAuth2 scope sets, the mobile feature
  table, release cadence (3 releases/year, 5 supported minors), and the 5 requirement areas for
  unlocking production comms.
- **[references/GETTING-STARTED-CPP.md](references/GETTING-STARTED-CPP.md)**: the 11-step standalone
  C++ walkthrough with the complete `CMakeLists.txt` and final `main.cpp`.
- **[references/GETTING-STARTED-UNITY.md](references/GETTING-STARTED-UNITY.md)**: the 10-step Unity
  walkthrough and the full `DiscordManager.cs`.
- **[references/GETTING-STARTED-UNREAL.md](references/GETTING-STARTED-UNREAL.md)**: the 8-step Unreal
  5.5 walkthrough, all three complete source files, plus the `discordpp`→`UDiscord*` name mapping.
- **[references/ACCOUNT-LINKING.md](references/ACCOUNT-LINKING.md)**: 5 guides — desktop OAuth2,
  mobile PKCE and deep links, console device flow, Discord-side entry points, publisher parent/child
  tokens; 7 HTTP endpoints and the `invalid_grant` / `530010` recovery path.
- **[references/PROVISIONAL-ACCOUNTS.md](references/PROVISIONAL-ACCOUNTS.md)**: all 8 pages — 3
  auth methods, 8 external auth types, the full OIDC requirement tables, 6 endpoints, 12 error codes,
  and the merge/unmerge data-migration matrices.
- **[references/LOBBIES.md](references/LOBBIES.md)**: the SDK lobby guide plus the REST Lobby
  resource — 13 endpoints, the Lobby/Member/Message/Invite objects, `CanLinkLobby`, and both rate
  limit tables.
- **[references/RELATIONSHIPS-AND-FRIENDS.md](references/RELATIONSHIPS-AND-FRIENDS.md)**: Discord vs
  game friend tiers, 14 relationship methods, both unified-friends-list approaches, and the complete
  game-invite flow including mobile deep links.
- **[references/MESSAGING.md](references/MESSAGING.md)**: DMs (history limits, disclosure messages,
  unrenderable content) and Linked Channels (the `GuildChannel` struct, permission requirements,
  guild-join invites).
- **[references/VOICE-CHAT.md](references/VOICE-CHAT.md)**: call lifecycle, 4 global + 3 per-call
  controls, Krisp vs WebRTC processing, raw audio callbacks, and bi-directional block-based muting.
- **[references/RICH-PRESENCE.md](references/RICH-PRESENCE.md)**: all 9 `Activity` fields, timestamps,
  assets, field URLs, 2 buttons, 3 status display types, and RPC presence without authentication.
- **[references/HOW-TO-GUIDES.md](references/HOW-TO-GUIDES.md)**: 6 how-tos — logging and AEC dumps,
  `ClientResult` retry handling, the server-side moderation metadata API with 4 webhook events,
  Unicode display names, backend API use, and the marketing/brand toolkit.
- **[references/DESIGN-GUIDELINES.md](references/DESIGN-GUIDELINES.md)**: all 13 design pages — 5
  principles, 4 button styles, friends-list sectioning and identity priority, the Game Friends tier,
  status colours, linked-channel warnings, and console/Sony restrictions.
- **[references/OVERVIEW.md](references/OVERVIEW.md)**: the 3 index pages, the support channels, and
  the card-to-file map for the whole documentation set.

## Rules that bite

- **Never ship `Public Client` enabled** without security review — every getting-started guide turns it
  on for convenience, and each public-client method has a server-side alternative.
- **Never ship a bot token or client secret in the game client.** The client receives only the access
  token your backend returns.
- **PKCE is mandatory on mobile**, public or confidential client, because custom URL schemes can be
  intercepted.
- **On Sony platforms**: no account-linking entry points, no linked channels, invites and messaging
  limited to players currently in the game, and no off-platform presence or logos.
- **Act only on explicit user intent** for relationships and messages — never auto-send or auto-accept.
- **Blocking a user does not mute them in voice.** Call `Call::SetLocalMute` on both clients.

## Related

Call the Skill tool with "discord-oauth2" for the scopes and token exchange account linking relies on.
Call the Skill tool with "discord-rest" for the guild, channel, message and ban endpoints a game
backend calls alongside the SDK. Call the Skill tool with "discord-bots" for the bot token and
application setup the provisional-account endpoints authenticate with.

## Source

Distilled from the [Discord Developer Documentation](https://docs.discord.com/developers) —
the 55 pages under `docs.discord.com/developers/discord-social-sdk/*` plus
`docs.discord.com/developers/resources/lobby` (56 pages total), retrieved 2026-08-26.
