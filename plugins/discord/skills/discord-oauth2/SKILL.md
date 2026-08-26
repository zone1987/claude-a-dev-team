---
name: discord-oauth2
description: "Discord OAuth2 flows, scopes, the permission bitfield and teams. Use when the request names Discord OAuth2, Discord permissions, a bot invite URL, or linked roles."
---

# Discord OAuth2 and Permissions

Authorization for Discord apps: which grant to use, which scope grants which route, how the
permission bitfield is computed, how a developer team owns an app, and how linked roles verify
external data.

## The authorization model in brief

Two credential kinds, and they are not interchangeable.

- **Bot token** — authenticates as the bot user, not on behalf of any person. Used for Gateway
  connections and most REST calls. Carries the permissions the guild granted when the bot was added.
- **OAuth2 user access token** — acts on behalf of a user, limited to the scopes that user approved.
  Short-lived; refresh with the `refresh_token` grant. The implicit grant returns **no** refresh
  token.

Three OAuth2 URLs, and the token endpoints accept **only** `application/x-www-form-urlencoded`;
JSON returns an error.

| URL | Purpose |
| --- | --- |
| `https://discord.com/oauth2/authorize` | Base authorization URL |
| `https://discord.com/api/oauth2/token` | Token exchange, refresh, client credentials |
| `https://discord.com/api/oauth2/token/revoke` | Token revocation |

**Scopes** say what your app may do with a user token; they are requested in the authorization URL
and must be declared in the Developer Portal. **Permissions** say what your bot may do inside a
guild or channel, as a bitfield the installing admin grants. The two are separate systems: a scope
never grants a guild permission, and a permission never grants API scope access.

Permissions are a variable-length integer **serialized as a string** — deserialize with a Big Integer
library, combine with `|`, test with `&`. Final channel permissions are base guild permissions
modified by overwrites in a fixed eight-step order, with `ADMINISTRATOR` and guild ownership
short-circuiting to all permissions.

Always send `state` on an authorization request and validate it on return; that is the CSRF and
clickjacking defense.

## Reference map

- **[OAUTH2-FLOWS.md](references/OAUTH2-FLOWS.md)**: all 6 flows and 6 endpoints — authorization code
  grant (URL parameters, `prompt`, `integration_type`, exchange, refresh, revocation), implicit grant,
  client credentials grant, bot authorization with its 6 parameters, advanced bot authorization with
  the extended guild payload, the `webhook.incoming` flow, the 2FA requirement, plus `GET /oauth2/@me`
  and `GET /oauth2/applications/@me` with response structures and 8 worked payloads.
- **[SCOPES.md](references/SCOPES.md)**: all 29 OAuth2 scopes with exact strings and what each grants,
  the 9 approved-partner scopes, and every per-scope restriction (`guilds.join` needs prior
  membership, `role_connections.write` is barred from the implicit grant, team apps get 2 scopes only).
- **[PERMISSIONS.md](references/PERMISSIONS.md)**: the complete bitfield — all **52** flags with hex
  value, bit shift, description and channel-type applicability; the 11 elevated 2FA permissions; 4
  hierarchy rules; the 8-step overwrite order and the exact `compute_permissions` algorithm; implicit
  permissions; thread inheritance; permission syncing; channel visibility and the November 16, 2026
  obfuscation change; the Role (12 fields), Role Tags (6), Role Colors (3) and Role Flags objects;
  timed-out members.
- **[TEAMS.md](references/TEAMS.md)**: creating a team, the 75-app limit, transferring an app
  (irreversible), the 4 member roles with their `role` values, and the Team (5 fields), Team Member
  (4 fields) and 2-value Membership State objects.
- **[LINKED-ROLES.md](references/LINKED-ROLES.md)**: the application role connection metadata object
  with all 6 fields and all **8** metadata types by number, both metadata endpoints with the
  5-record maximum, and the linked-roles tutorial end to end (portal setup, `.env`, schema
  registration, creating and acquiring the role, token storage).
- **[ACCOUNT-LINKING.md](references/ACCOUNT-LINKING.md)**: game account linking via the Social SDK —
  Game Flow versus Web Flow compared across 4 dimensions, the 5-step OAuth2 sequence, 3 Discord entry
  points, provisional accounts.

## Related

Call the Skill tool with "discord-rest" for the User and Guild objects a token grants access to.
Call the Skill tool with "discord-bots" for creating an app and getting the bot token.
Call the Skill tool with "discord-interactions" for what the `applications.commands` scope registers.

## Source

Discord Developer Documentation, retrieved 2026-08-26:

- `https://docs.discord.com/developers/topics/oauth2`
- `https://docs.discord.com/developers/topics/permissions`
- `https://docs.discord.com/developers/topics/teams`
- `https://docs.discord.com/developers/resources/application-role-connection-metadata`
- `https://docs.discord.com/developers/tutorials/configuring-app-metadata-for-linked-roles`
- `https://docs.discord.com/developers/platform/oauth2-and-permissions`
- `https://docs.discord.com/developers/platform/account-linking`
