# Discord OAuth2 Scopes

Every OAuth2 scope Discord supports, with its exact string, what it grants, and whether it needs
Discord's approval.

Source: `https://docs.discord.com/developers/topics/oauth2#shared-resources-oauth2-scopes`, retrieved
2026-08-26.

## Contents

- [How to request scopes](#how-to-request-scopes)
- [OAuth2 Scopes (complete table)](#oauth2-scopes-complete-table)
- [Restrictions and caveats](#restrictions-and-caveats)
- [Scopes requiring approval](#scopes-requiring-approval)
- [The commonly used subset](#the-commonly-used-subset)

## How to request scopes

Scopes are passed in the `scope` query parameter of the authorization URL, separated by url encoded
spaces (`%20`). In the token endpoint's form body (client credentials grant) they are separated by
plain spaces. Scopes must also be declared in the Developer Portal.

**Some scopes require approval from Discord to use. Requesting them from a user without approval from
Discord may cause errors or undocumented behavior in the OAuth2 flow.** To inquire about access to
scopes that are only available to approved partners, speak to your Discord account representative to
see if they are a fit for your needs.

## OAuth2 Scopes (complete table)

| Name | Description |
| --- | --- |
| activities.read | allows your app to fetch data from a user's "Now Playing/Recently Played" list — not currently available for apps |
| activities.write | allows your app to update a user's activity - not currently available for apps (NOT REQUIRED FOR GAMESDK ACTIVITY MANAGER, see `https://docs.discord.com/developers/developer-tools/game-sdk#activities`) |
| applications.builds.read | allows your app to read build data for a user's applications |
| applications.builds.upload | allows your app to upload/update builds for a user's applications - only available to approved partners |
| applications.commands | allows your app to add commands to a guild - included by default with the `bot` scope |
| applications.commands.update | allows your app to update its commands using a Bearer token - client credentials grant only |
| applications.commands.permissions.update | allows your app to update permissions for its commands in a guild a user has permissions to |
| applications.entitlements | allows your app to read entitlements for a user's applications |
| applications.store.update | allows your app to read and update store data (SKUs, store listings, achievements, etc.) for a user's applications |
| bot | for oauth2 bots, this puts the bot in the user's selected guild by default |
| connections | allows `/users/@me/connections` to return linked third-party accounts |
| dm_channels.read | allows your app to see information about the user's DMs and group DMs - only available to approved partners |
| email | enables `/users/@me` to return an `email` |
| gdm.join | allows your app to join users to a group dm (`/channels/{channel.id}/recipients/{user.id}`, Group DM Add Recipient) |
| guilds | allows `/users/@me/guilds` to return basic information about all of a user's guilds |
| guilds.join | allows `/guilds/{guild.id}/members/{user.id}` to be used for joining users to a guild |
| guilds.members.read | allows `/users/@me/guilds/{guild.id}/member` to return a user's member information in a guild |
| identify | allows `/users/@me` without `email` |
| identify.premium | allows your app to read a user's Nitro subscription type as defined by `premium_type` on the User object - only available to approved partners |
| messages.read | for local rpc server api access, this allows you to read messages from all client channels (otherwise restricted to channels/guilds your app creates) |
| relationships.read | Allows your app to access a user's Discord Friends list, their pending requests, and blocked users. This scope is part of Discord's Social SDK - submit for access at `https://discord.com/developers/applications/select/social-sdk/getting-started`. Social SDK Terms apply (`https://support-dev.discord.com/hc/en-us/articles/30225844245271-Discord-Social-SDK-Terms`), including Section 5(a)(ii) to the data you obtain |
| role_connections.write | allows your app to update a user's connection and metadata for the app |
| rpc | for local rpc server access, this allows you to control a user's local Discord client - only available to approved partners |
| rpc.activities.write | for local rpc server access, this allows you to update a user's activity - only available to approved partners |
| rpc.notifications.read | for local rpc server access, this allows you to receive notifications pushed out to the user - only available to approved partners |
| rpc.voice.read | for local rpc server access, this allows you to read a user's voice settings and listen for voice events - only available to approved partners |
| rpc.voice.write | for local rpc server access, this allows you to update a user's voice settings - only available to approved partners |
| voice | allows your app to connect to voice on user's behalf and see all the voice members - only available to approved partners |
| webhook.incoming | this generates a webhook that is returned in the oauth token response for authorization code grants |

**29 scopes** in total.

## Restrictions and caveats

- **`guilds.join`** — in order to add a user to a guild, your bot has to already belong to that guild.
- **`role_connections.write`** — cannot be used with the implicit grant type.
- **`applications.commands`** — included by default with the `bot` scope. It is also the only scope for
  which the `integration_type` authorization parameter is relevant.
- **`applications.commands.update`** — client credentials grant only.
- **Team applications** are limited to the `identify` and `applications.commands.update` scopes,
  because teams are not bound to a specific user.
- **Passthrough scopes** — for `bot` and `webhook.incoming`, authorization is always required, so
  `prompt=none` will not skip the consent screen.
- **`activities.read` and `activities.write`** — "not currently available for apps" per upstream.
- **`activities.write`** is not required for the GameSDK Activity Manager.

## Scopes requiring approval

The nine scopes upstream marks "only available to approved partners":
`applications.builds.upload`, `dm_channels.read`, `identify.premium`, `rpc`,
`rpc.activities.write`, `rpc.notifications.read`, `rpc.voice.read`, `rpc.voice.write`, `voice`.

`relationships.read` is not marked "approved partners" but requires a separate Social SDK access
submission.

## The commonly used subset

From `https://docs.discord.com/developers/platform/oauth2-and-permissions`, Discord's own shortlist of
common scopes:

| Scope | What It Grants |
| --- | --- |
| `bot` | Adds your bot to a guild |
| `identify` | Read the user's basic profile (e.g., id, username, avatar) |
| `guilds` | List the guilds the user belongs to |
| `guilds.join` | Add the user to a guild |
| `email` | Read the user's email address |
| `connections` | View the user's linked accounts (Twitch, Steam, etc.) |
| `applications.commands` | Register slash commands in a guild |

## Source

Discord Developer Documentation — `https://docs.discord.com/developers/topics/oauth2` and
`https://docs.discord.com/developers/platform/oauth2-and-permissions`, retrieved 2026-08-26.
