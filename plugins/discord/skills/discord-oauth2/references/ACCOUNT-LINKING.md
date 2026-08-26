# Discord Account Linking

Connecting a player's Discord account to their in-game account: the two flows, the OAuth2 sequence,
Discord entry points, and provisional accounts. This is game account linking (Social SDK), which is a
separate feature from linked roles — see `LINKED-ROLES.md` for role connection metadata.

Source: `https://docs.discord.com/developers/platform/account-linking`, retrieved 2026-08-26.

*(Upstream header image: "Account Linking Hero Image".)*

## Contents

- [What is Account Linking?](#what-is-account-linking)
- [Why Account Linking Matters](#why-account-linking-matters)
- [How Account Linking Works](#how-account-linking-works)
- [Two Ways to Link](#two-ways-to-link)
- [Implementing Account Linking](#implementing-account-linking)
- [Linking from Discord Entry Points](#linking-from-discord-entry-points)
- [Provisional Accounts](#provisional-accounts)
- [Next Steps](#next-steps)

## What is Account Linking?

Account linking connects a player's Discord account to their account in your game. Once linked,
players gain access to their Discord friends list, game invites, rich presence, and voice directly
inside your game.

This link persists across sessions, so players authenticate once and will not need to re-link unless
your account linking scopes change (see the Social SDK OAuth2 scopes page,
`https://docs.discord.com/developers/discord-social-sdk/core-concepts/oauth2-scopes`). Players who are
not ready to link (or do not have a Discord account yet) can still use social features through
provisional accounts. When they do link later, their friends, DM history, and lobby memberships
transfer automatically to their Discord account.

Account linking is also important for Social Commerce
(`https://docs.discord.com/developers/social-commerce/overview`) in Discord communities. Players with
linked accounts can claim in-game items that they purchase or receive as gifts from Discord Game Shops.

## Why Account Linking Matters

### For Players

Account linking transforms Discord from a second-screen utility into a personalized gaming companion:

- **Seamless social experiences:** Access Discord friends and game invites directly within games.
- **Rich presence integration:** Show detailed game status and activity to friends.
- **Social Commerce:** Claim in-game items purchased or gifted from Discord Game Shops.

### For Developers

Linked players are demonstrably more valuable to your game:

- Players who link in-game accounts to Discord via Social SDK **play more often** — median game launch
  days increase is 25%\*
- Players who link in-game accounts to Discord via the Social SDK **play longer** — median session
  length increase is 16%\*
- Players who link in-game accounts to Discord via the Social SDK **retain better** — median D28
  retention is 34%\*

These are not projections. This is causal data from games that have implemented account linking.

\* *Discord Internal Data, 2025*

## How Account Linking Works

### Understanding the OAuth2 Flow

Account linking is built on OAuth2, an industry-standard authorization protocol. Here is what happens
under the hood when a player links their account:

1. **Your game asks Discord to start the OAuth flow.**
2. **Discord shows the player an OAuth modal asking them to authorize your game and the OAuth scopes
   being requested.**
3. **The player approves** (authorizes).
4. **Discord gives your game a temporary access token**, which is proof the player agreed to
   authorize.
5. **Your game uses that token** to access Discord social features on the player's behalf.

You do not need to implement OAuth2 from scratch. The Discord Social SDK handles the authorization
flow, token management, and API communication for you. Web Flow uses standard OAuth2, which most web
frameworks support out of the box.

The access token your game receives is **scoped**, meaning it can only access the Discord features you
have requested. The Social SDK provides two default scope sets: **`GetDefaultPresenceScopes`** for
presence and friends, and **`GetDefaultCommunicationScopes`** for messaging, lobbies, and voice. See
the OAuth2 Scopes for Social SDK page
(`https://docs.discord.com/developers/discord-social-sdk/core-concepts/oauth2-scopes`) for full
details.

*(Upstream image: "Account Linking in Action".)*

## Two Ways to Link

You can implement account linking through two flows:

| | **Game Flow** | **Web Flow** |
| --- | --- | --- |
| **What it is** | Player authorizes from inside your game via the Discord client, overlay, or browser | Player authorizes through a web page on any device |
| **Requires** | Discord Social SDK | Standard OAuth2 implementation |
| **Platforms** | Desktop, Mobile, Console | All platforms that support web |
| **Player experience** | Seamless, stays in-game context (Discord app/overlay launches, or falls back to browser) | Opens a browser / web page |

Both flows produce the same result: the player's Discord account is linked to your game. Neither flow
is better than the other, and as long as the same OAuth2 scopes are used, the player gets the same
features regardless of which flow they used to link.

Discord recommends offering both flows to give players the most flexibility. Game Flow only works when
the player is actively playing your game on the same device, while Web Flow is a more portable option
that supports account linking when the player is engaging with your game through your Official Game
Community, Game Shop, or any other web-based touchpoint.

**Note.** Once a player links through either method, they are linked for both. You can start with one
flow and add the other later, and players will not need to re-link.

**Warning.** Web Flow does **not** mean launching a web browser inside your game. Web Flow is a
standalone web-based OAuth2 flow, typically used from Discord entry points or external URLs.

## Implementing Account Linking

### Linking from Your Game

Use the Discord Social SDK to let players link their accounts directly from your game. Choose the
guide for your platform:

- **Desktop (Windows, Mac, Linux)** — guide on implementing account linking from your desktop game
  using the Social SDK:
  `https://docs.discord.com/developers/discord-social-sdk/development-guides/account-linking-with-discord`
- **Mobile (iOS, Android)** — guide on implementing account linking from your mobile game using the
  Social SDK:
  `https://docs.discord.com/developers/discord-social-sdk/development-guides/account-linking-on-mobile`
- **Console (PlayStation, Xbox)** — guide on implementing account linking from your console game using
  the Social SDK:
  `https://docs.discord.com/developers/discord-social-sdk/development-guides/account-linking-on-consoles`

### Linking from the Web

Use a standard OAuth2 flow to let players link their accounts through a web page on any device. This
does not require the Social SDK and works well if you already have web infrastructure. Web Flow is the
primary method for enabling Social Commerce features like Game Shops and Game Stat Widgets. For the
standard OAuth2 web flow itself see `OAUTH2-FLOWS.md`.

## Linking from Discord Entry Points

Entry points are buttons and prompts Discord displays throughout the Discord client encouraging
players to link their account with your game, even when the game is not running. Accounts linked from
Discord work exactly the same as those linked from your game.

*(Upstream image: "Account Linking from Discord Entry Points".)*

When a player uses a Discord entry point, Discord determines which flow to use:

1. **Game Flow** is used if the game is running and the developer has called the
   `RegisterAuthorizeRequestCallback` function in the Social SDK
2. **Web Flow** is used if a **Connection Entrypoint URL** is configured in the Developer Portal

Some of the current Discord entry points include:

- **Game Detection** — Discord detects the player is playing your game and provides an entry point to
  link if they have not already. *(Upstream screenshot: "Discord entry points for account linking".)*
- **Game Invites** — players are optionally able to link when receiving an invite for your game, which
  helps them get set up and playing with their friends faster.
  *(Upstream screenshot: "Game Invite entry points for account linking".)*
- **Claiming Game Shop Items** — players need to account link when redeeming items from your Game Shop
  to be able to receive their in-game rewards.
  *(Upstream screenshot: "Game Shop entry points for account linking".)*

**Note.** Configuring Web Flow to work from official Discord entry points is currently available to
select partners. Contact Discord if you are interested in enabling this for your game.

Guide on enabling Discord entry points so players can link from within the Discord client:
`https://docs.discord.com/developers/discord-social-sdk/development-guides/account-linking-from-discord`

## Provisional Accounts

Players who do not have Discord, or who choose not to link yet, can still use social features through
provisional accounts. They can add friends, join lobbies, send messages, and participate in voice chat
without a Discord account.

When they later link a Discord account, their friends, DM history, and lobby memberships transfer
automatically. Learn more in the Provisional Accounts guide
(`https://docs.discord.com/developers/discord-social-sdk/development-guides/provisional-accounts/overview`).

## Next Steps

Upstream links onward to:

- **Social Layer for Games** (`https://docs.discord.com/developers/platform/social-layer`) — the
  Discord-powered social features that account linking unlocks for your game.
- **Design Guidelines**
  (`https://docs.discord.com/developers/discord-social-sdk/design-guidelines/signing-in`) — best
  practices for designing the account linking experience in your game.
- **Getting Started** (`https://docs.discord.com/developers/discord-social-sdk/getting-started`) —
  step-by-step guides for integrating the Discord Social SDK with C++, Unity, and Unreal Engine.

## Source

Discord Developer Documentation — `https://docs.discord.com/developers/platform/account-linking`,
retrieved 2026-08-26.
