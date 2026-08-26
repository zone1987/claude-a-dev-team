# Discord OAuth2 Flows

Every OAuth2 flow Discord supports, with its URLs, parameters, request and response payloads: the
authorization code grant, the implicit grant, the client credentials grant, bot authorization,
advanced bot authorization, the webhook flow, token refresh, token revocation, and the two OAuth2
information endpoints.

Source: `https://docs.discord.com/developers/topics/oauth2`, retrieved 2026-08-26.

## Contents

- [Shared Resources](#shared-resources)
- [State and Security](#state-and-security)
- [Authorization Code Grant](#authorization-code-grant)
- [Implicit Grant](#implicit-grant)
- [Client Credentials Grant](#client-credentials-grant)
- [Bot Users](#bot-users)
- [Bot Authorization Flow](#bot-authorization-flow)
- [Advanced Bot Authorization](#advanced-bot-authorization)
- [Two-Factor Authentication Requirement](#two-factor-authentication-requirement)
- [Webhooks](#webhooks)
- [GET /oauth2/applications/@me](#get-oauth2applicationsme)
- [GET /oauth2/@me](#get-oauth2me)
- [Two ways to authenticate: bot token vs user token](#two-ways-to-authenticate-bot-token-vs-user-token)

OAuth2 enables application developers to build applications that utilize authentication and data from
the Discord API. Within Discord, there are multiple types of OAuth2 authentication. Discord supports
the authorization code grant, the implicit grant, client credentials, and some modified
special-for-Discord flows for Bots and Webhooks.

## Shared Resources

The first step in implementing OAuth2 is registering a developer application
(`https://discord.com/developers/applications`) and retrieving your client ID and client secret. Most
people who will be implementing OAuth2 will want to find and utilize a library in the language of
their choice. For those implementing OAuth2 from scratch, see RFC 6749
(`https://tools.ietf.org/html/rfc6749`) for details. After you create your application with Discord,
make sure that you have your `client_id` and `client_secret` handy. The next step is to figure out
which OAuth2 flow is right for your purposes.

### OAuth2 URLs

| URL | Description |
| --- | --- |
| `https://discord.com/oauth2/authorize` | Base authorization URL |
| `https://discord.com/api/oauth2/token` | Token URL |
| `https://discord.com/api/oauth2/token/revoke` | Token Revocation URL (RFC 7009, `https://tools.ietf.org/html/rfc7009`) |

**Warning.** In accordance with the relevant RFCs, the token and token revocation URLs will **only**
accept a content type of `application/x-www-form-urlencoded`. JSON content is not permitted and will
return an error. The upstream page does not state the shape of that error response.

For the complete scope list see `SCOPES.md`.

## State and Security

Before diving into the semantics of the different OAuth2 grants, stop and consider security,
specifically the use of the `state` parameter. Cross-site request forgery (CSRF) and Clickjacking are
security vulnerabilities that must be addressed by individuals implementing OAuth. This is typically
accomplished using the `state` parameter. `state` is sent in the authorization request and returned
back in the response and should be a value that binds the user's request to their authenticated
state. For example, `state` could be a hash of the user's session cookie, or some other nonce that
can be linked to the user's session.

When a user begins an authorization flow on the client, a `state` is generated that is unique to that
user's request. This value is stored somewhere only accessible to the client and the user, i.e.
protected by the same-origin policy. When the user is redirected, the `state` parameter is returned.
The client validates the request by checking that the `state` returned matches the stored value. If
they match, it is a valid authorization request. If they do not match, it is possible that someone
intercepted the request or otherwise falsely authorized themselves to another user's resources, and
the request should be denied.

While Discord does not require the use of the `state` parameter, Discord supports it and highly
recommends that you implement it for the security of your own applications and data.

## Authorization Code Grant

The authorization code grant is what most developers will recognize as "standard OAuth2" and involves
retrieving an access code and exchanging it for a user's access token. It allows the authorization
server to act as an intermediary between the client and the resource owner, so the resource owner's
credentials are never shared directly with the client.

**All calls to the OAuth2 endpoints require either HTTP Basic authentication or `client_id` and
`client_secret` supplied in the form data body.**

### Authorization URL Example

```
https://discord.com/oauth2/authorize?response_type=code&client_id=157730590492196864&scope=identify%20guilds.join&state=15773059ghq9183habn&redirect_uri=https%3A%2F%2Fnicememe.website&prompt=consent&integration_type=0
```

Parameters used above:

- **`response_type`** — `code` for the authorization code grant.
- **`client_id`** — your application's `client_id`.
- **`scope`** — a list of OAuth2 scopes separated by url encoded spaces (`%20`).
- **`redirect_uri`** — whatever URL you registered when creating your application, url-encoded.
- **`state`** — the unique string described in [State and Security](#state-and-security).
- **`prompt`** — controls how the authorization flow handles existing authorizations. If a user has
  previously authorized your application with the requested scopes and `prompt` is set to `consent`,
  it will request them to reapprove their authorization. If set to `none`, it will skip the
  authorization screen and redirect them back to your redirect URI without requesting their
  authorization. For passthrough scopes, like `bot` and `webhook.incoming`, authorization is always
  required.
- **`integration_type`** — specifies the installation context for the authorization. The installation
  context determines where the application will be installed, and is only relevant when `scope`
  contains `applications.commands`. When set to **0 (GUILD_INSTALL)** the application will be
  authorized for installation to a server, and when set to **1 (USER_INSTALL)** the application will
  be authorized for installation to a user. The application must be configured in the Developer
  Portal to support the provided `integration_type`.

When someone navigates to this URL, they will be prompted to authorize your application for the
requested scopes. On acceptance, they will be redirected to your `redirect_uri`, which will contain an
additional querystring parameter, `code`. `state` will also be returned if previously sent, and
should be validated at this point.

### Redirect URL Example

```
https://nicememe.website/?code=NhhvTDYsFcdgNLnnLijcl7Ku7bEEeee&state=15773059ghq9183habn
```

### Access token exchange

`code` is now exchanged for the user's access token by making a `POST` request to the
[token URL](#oauth2-urls) with the following parameters:

- `grant_type` — must be set to `authorization_code`
- `code` — the code from the querystring
- `redirect_uri` — the `redirect_uri` associated with this authorization, usually from your
  authorization URL

#### POST https://discord.com/api/oauth2/token (authorization_code)

###### Access Token Exchange Example

```python
import requests

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '332269999912132097'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'https://nicememe.website'

def exchange_code(code):
  data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  r.raise_for_status()
  return r.json()
```

###### Access Token Response

```json
{
  "access_token": "6qrZcUqja7812RVdnEKjpzOL4CvHBFG",
  "token_type": "Bearer",
  "expires_in": 604800,
  "refresh_token": "D43f5y0ahjqew82jZ4NViEr2YafMKhue",
  "scope": "identify"
}
```

Having the user's access token allows your application to make certain requests to the API on their
behalf, restricted to whatever scopes were requested. `expires_in` is how long, in seconds, until the
returned access token expires, allowing you to anticipate the expiration and refresh the token.

### Refreshing a token

To refresh, make another `POST` request to the [token URL](#oauth2-urls) with the following
parameters:

- `grant_type` — must be set to `refresh_token`
- `refresh_token` — the user's refresh token

#### POST https://discord.com/api/oauth2/token (refresh_token)

###### Refresh Token Exchange Example

```python
import requests

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '332269999912132097'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

def refresh_token(refresh_token):
  data = {
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  r.raise_for_status()
  return r.json()
```

The response is a fresh [Access Token Response](#access-token-response) as shown above.

### Revoking a token

#### POST https://discord.com/api/oauth2/token/revoke

To disable an access or refresh token, you can revoke it by making a `POST` request to the
[token revocation URL](#oauth2-urls) with the following parameters:

- `token` — the access token or refresh token to revoke
- `token_type_hint` *(optional)* — the `token` parameter's type: either `access_token` or
  `refresh_token`

**Warning.** When you revoke a token, any active access or refresh tokens associated with that
authorization will be revoked, **regardless of the `token` and `token_type_hint` values you pass in**.

###### Token Revocation Example

```python
import requests

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '332269999912132097'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

def revoke_access_token(access_token):
  data = {
    'token': access_token,
    'token_type_hint': 'access_token'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  requests.post('%s/oauth2/token/revoke' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
```

The upstream page documents no response body for revocation.

## Implicit Grant

The implicit OAuth2 grant is a simplified flow optimized for in-browser clients. Instead of issuing
the client an authorization code to be exchanged for an access token, the client is directly issued an
access token. The URL is formatted as follows:

### Authorization URL Example

```
https://discord.com/oauth2/authorize?response_type=token&client_id=290926444748734499&state=15773059ghq9183habn&scope=identify
```

On redirect, your redirect URI will contain additional **URI fragments**: `access_token`,
`token_type`, `expires_in`, `scope`, and `state` (if specified). **These are not querystring
parameters.** Be mindful of the `#` character:

### Redirect URL Example

```
https://findingfakeurlsisprettyhard.tv/#access_token=RTfP0OK99U3kbRtHOoKLmJbOn45PjL&token_type=Bearer&expires_in=604800&scope=identify&state=15773059ghq9183habn
```

There are tradeoffs in using the implicit grant flow. It is both quicker and easier to implement, but
rather than exchanging a code and getting a token returned in a secure HTTP body, the access token is
returned in the URI fragment, which makes it possibly exposed to unauthorized parties. **You also are
not returned a refresh token, so the user must explicitly re-authorize once their token expires.**

`role_connections.write` cannot be used with the implicit grant type.

## Client Credentials Grant

The client credential flow is a quick and easy way for bot developers to get their own bearer tokens
for testing purposes. By making a `POST` request to the [token URL](#oauth2-urls) with a grant type of
`client_credentials`, using Basic authentication with your client id as the username and your client
secret as the password, you will be returned an access token for the bot owner. Therefore, always be
super-extra-very-we-are-not-kidding-like-really-be-secure-make-sure-your-info-is-not-in-your-source-code
careful with your `client_id` and `client_secret`. Discord does not take kindly to imposters around
these parts.

You can specify scopes with the `scope` parameter, which is a list of OAuth2 scopes separated by
spaces.

**Team applications are limited to the `identify` and `applications.commands.update` scope**, because
teams are not bound to a specific user.

#### POST https://discord.com/api/oauth2/token (client_credentials)

###### Client Credentials Token Request Example

```python
import requests

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '332269999912132097'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

def get_token():
  data = {
    'grant_type': 'client_credentials',
    'scope': 'identify connections'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  r.raise_for_status()
  return r.json()
```

In return, you will receive an access token (**without a refresh token**):

###### Client Credentials Access Token Response

```json
{
  "access_token": "6qrZcUqja7812RVdnEKjpzOL4CvHBFG",
  "token_type": "Bearer",
  "expires_in": 604800,
  "scope": "identify connections"
}
```

## Bot Users

Discord's API provides bot users, which are a separate type of user dedicated to automation. Bot users
are automatically added to all apps, and are authenticated using the bot token found in your app's
settings (`https://discord.com/developers/applications`). Unlike the normal OAuth2 flow, bot users
have full access to most API routes without using bearer tokens, and can connect to the Real Time
Gateway.

### Bot vs User Accounts

**Warning.** Developers must abide by the terms of service
(`https://support-dev.discord.com/hc/articles/8562894815383-Discord-Developer-Terms-of-Service`),
which includes refraining from automating standard user accounts (generally called "self-bots")
outside of the OAuth2/bot API.

Bot users have a few differences compared to standard Discord users:

1. Bots are added to guilds through the OAuth2 API, and cannot accept normal invites.
2. Bots cannot have friends or be added to or join Group DMs.
3. Verified bots
   (`https://support-dev.discord.com/hc/en-us/articles/23926564536471-How-Do-I-Get-My-App-Verified`)
   do not have a maximum number of guilds.
4. Bots have an entirely separate set of rate limits.

## Bot Authorization Flow

Bot authorization is a special server-less and callback-less OAuth2 flow that makes it easy for users
to add bots to guilds. The URL you create looks similar to what is used for a full stack
implementation.

### Bot Auth Parameters

| name | description |
| --- | --- |
| client_id | your app's client id |
| scope? | needs to include `bot` for the bot flow |
| permissions? | the permissions you're requesting (see `PERMISSIONS.md`) |
| guild_id? | pre-fills the dropdown picker with a guild for the user |
| disable_guild_select? | `true` or `false` — disallows the user from changing the guild dropdown |
| integration_type? | the installation context for the authorization |

### URL Example

```
https://discord.com/oauth2/authorize?client_id=157730590492196864&scope=bot&permissions=1
```

In the case of bots, the `scope` parameter should be set to `bot`. There is also a new parameter,
`permissions`, which is an integer corresponding to the permission calculations for the bot (see
`PERMISSIONS.md` → Bitwise Permission Flags). Notice the absence of `response_type` and
`redirect_uri`. Bot authorization does not require these parameters because there is no need to
retrieve the user's access token.

When the user navigates to this page, they will be prompted to add the bot to a guild in which they
have proper permissions. On acceptance, the bot will be added.

If you happen to already know the ID of the guild the user will add your bot to, you can provide this
ID in the URL as a `guild_id=GUILD_ID` parameter. When the authorization page loads, that guild will
be preselected in the dialog if that user has permission to add the bot to that guild. You can use
this in conjunction with the parameter `disable_guild_select=true` to disallow the user from picking a
different guild.

If you only provide the `client_id` parameter (with optionally `permissions`, `guild_id`, or
`disable_guild_select`), the authorization will use the **default install settings** configured in the
developer portal. Specifying `scope`, `integration_type`, or `redirect_uri` will override this
behavior.

If your bot is super specific to your private clubhouse, or you just do not like sharing, you can
leave the **`Public Bot`** option unchecked in your application's settings. If unchecked, only you can
add the bot to guilds. If marked as public, anyone with your bot's URL can add it to guilds in which
they have proper permissions.

**In order to add a user to a guild, your bot has to already belong to that guild.**

## Advanced Bot Authorization

Developers can extend the bot authorization functionality. You can request additional scopes outside
of `bot` and `applications.commands`, which will prompt a continuation into a complete
[authorization code grant flow](#authorization-code-grant) and add the ability to request the user's
access token. If you request any scopes outside of `bot` and `applications.commands`, `response_type`
is again mandatory; Discord will also automatically redirect the user to the first URI in your
application's registered list unless `redirect_uri` is specified.

When receiving the access code on redirect, there will be additional querystring parameters of
`guild_id` and `permissions`. The `guild_id` parameter should only be used as a hint as to the
relationship between your bot and a guild. To be sure of the relationship between your bot and the
guild, consider requiring the OAuth2 code grant in your bot's settings. Enabling it requires anyone
adding your bot to a server to go through a full OAuth2
[authorization code grant flow](#authorization-code-grant). When you retrieve the user's access token,
you will also receive information about the guild to which your bot was added:

###### Extended Bot Authorization Access Token Example

```json
{
  "token_type": "Bearer",
  "guild": {
    "mfa_level": 0,
    "emojis": [],
    "application_id": null,
    "name": "SomeTest",
    "roles": [
      {
        "hoist": false,
        "name": "@everyone",
        "mentionable": false,
        "color": 0,
        "position": 0,
        "id": "290926798626357250",
        "managed": false,
        "permissions": 49794241,
        "permissions_new": "49794241"
      }
    ],
    "afk_timeout": 300,
    "system_channel_id": null,
    "widget_channel_id": null,
    "region": "us-east",
    "default_message_notifications": 1,
    "explicit_content_filter": 0,
    "splash": null,
    "features": [],
    "afk_channel_id": null,
    "widget_enabled": false,
    "verification_level": 0,
    "owner_id": "53908232999183680",
    "id": "2909267986347357250",
    "icon": null,
    "description": null,
    "public_updates_channel_id": null,
    "safety_alerts_channel_id": null,
    "rules_channel_id": null,
    "max_members": 100000,
    "vanity_url_code": null,
    "premium_subscription_count": 0,
    "premium_tier": 0,
    "preferred_locale": "en-US",
    "system_channel_flags": 0,
    "banner": null,
    "max_presences": null,
    "discovery_splash": null,
    "max_video_channel_users": 25
  },
  "access_token": "zMndOe7jFLXGawdlxMOdNvXjjOce5X",
  "scope": "bot",
  "expires_in": 604800,
  "refresh_token": "mgp8qnvBwJcmadwgCYKyYD5CAzGAX4"
}
```

## Two-Factor Authentication Requirement

For bots with **elevated permissions** (permissions with a `*` next to them in `PERMISSIONS.md` →
Bitwise Permission Flags), Discord enforces two-factor authentication on the owner's account when
added to guilds that have server-wide 2FA enabled.

## Webhooks

Discord's webhook flow is a specialized version of an [authorization code](#authorization-code-grant)
implementation. In this case, the `scope` querystring parameter needs to be set to
`webhook.incoming`:

### URL Example

```
https://discord.com/oauth2/authorize?response_type=code&client_id=157730590492196864&scope=webhook.incoming&state=15773059ghq9183habn&redirect_uri=https%3A%2F%2Fnicememe.website
```

When the user navigates to this URL, they will be prompted to select a channel in which to allow the
webhook. When the webhook is executed, it will post its message into this channel. On acceptance, the
user will be redirected to your `redirect_uri`. The URL will contain the `code` querystring parameter
which should be [exchanged for an access token](#access-token-exchange). In return, you will receive a
slightly modified token response:

###### Webhook Token Response Example

```json
{
  "token_type": "Bearer",
  "access_token": "GNaVzEtATqdh173tNHEXY9ZYAuhiYxvy",
  "scope": "webhook.incoming",
  "expires_in": 604800,
  "refresh_token": "PvPL7ELyMDc1836457XCDh1Y8jPbRm",
  "webhook": {
    "application_id": "310954232226357250",
    "name": "testwebhook",
    "url": "https://discord.com/api/webhooks/347114750880120863/kKDdjXa1g9tKNs0-_yOwLyALC9gydEWP6gr9sHabuK1vuofjhQDDnlOclJeRIvYK-pj_",
    "channel_id": "345626669224982402",
    "token": "kKDdjXa1g9tKNs0-_yOwLyALC9gydEWP6gr9sHabuK1vuofjhQDDnlOclJeRIvYK-pj_",
    "type": 1,
    "avatar": null,
    "guild_id": "290926792226357250",
    "id": "347114750880120863"
  }
}
```

From this object, you should store the `webhook.token` and `webhook.id`. See the Execute Webhook
documentation (call the Skill tool with "discord-rest") for how to send messages with the webhook.

Any user that wishes to add your webhook to their channel will need to go through the full OAuth2
flow. **A new webhook is created each time**, so you will need to save the token and id. If you wish
to send a message to all your webhooks, you will need to iterate over each stored `id:token`
combination and make `POST` requests to each one. Be mindful of Discord's rate limits.

## GET /oauth2/applications/@me

**Get Current Bot Application Information.** Returns the bot's application object (see the Application
resource; call the Skill tool with "discord-rest").

The upstream page documents no query string parameters, no request body, and no error responses for
this route.

## GET /oauth2/@me

**Get Current Authorization Information.** Returns info about the current authorization. **Requires
authentication with a bearer token.**

###### Response Structure

| Field | Type | Description |
| --- | --- | --- |
| application | partial application object | the current application |
| scopes | array of strings | the scopes the user has authorized the application for |
| expires | ISO8601 timestamp | when the access token expires |
| user? | user object | the user who has authorized, if the user has authorized with the `identify` scope |

###### Example Authorization Information

```json
{
    "application": {
        "id": "159799960412356608",
        "name": "AIRHORN SOLUTIONS",
        "icon": "f03590d3eb764081d154a66340ea7d6d",
        "description": "",
        "hook": true,
        "bot_public": true,
        "bot_require_code_grant": false,
        "verify_key": "c8cde6a3c8c6e49d86af3191287b3ce255872be1fff6dc285bdb420c06a2c3c8"
    },
    "scopes": [
        "guilds.join",
        "identify"
    ],
    "expires": "2021-01-23T02:33:17.017000+00:00",
    "user": {
        "id": "268473310986240001",
        "username": "discord",
        "avatar": "f749bb0cbeeb26ef21eca719337d20f1",
        "discriminator": "0",
        "global_name": "Discord",
        "public_flags": 131072
    }
}
```

The upstream page documents no query string parameters, no request body, and no error responses for
this route.

## Two ways to authenticate: bot token vs user token

From `https://docs.discord.com/developers/platform/oauth2-and-permissions`. Discord uses OAuth2 as the
standard authorization framework for granting apps access to users and servers. Understanding OAuth2
and the permissions model is essential for any Discord app.

### Bot Token

When you create a bot user in the Developer Portal, Discord generates a **bot token**. Your code uses
this token to authenticate as the bot user, a dedicated application account separate from a regular
user account.

Bot tokens:

- Authenticate as the bot user, not on behalf of any person
- Are used for Gateway connections and most REST API calls
- Grant the permissions the bot was given when added to a server
- Should be treated like passwords and never exposed publicly

### OAuth2 User Token

When you need to act on behalf of a user, you use OAuth2 to get a user access token. The user logs in
with Discord and authorizes your app for specific scopes.

User tokens:

- Let your app read or write data on behalf of the user as authorized by requested scopes
- Are scoped, so you only get access to what the user grants
- Are short-lived and must be refreshed
- Should be treated like passwords and never exposed publicly

### Permissions in brief

Permissions control what a **bot** can do in a specific server or channel. When a bot is added to a
server via OAuth2, the server admin grants it a set of permissions. Permissions are stored as a
bitfield. They can be:

- **Guild-level:** apply across the entire server
- **Channel-level:** overrides that apply to specific channels

Your app should request only the permissions it needs. Requesting excessive permissions reduces trust
with users. Your app should request only the permissions it needs as described in the Discord
Developer Policy
(`https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy`).

Scopes define what your app is allowed to do. They are requested during the OAuth2 authorization flow
and **must be declared in the Developer Portal**.

## Source

Discord Developer Documentation — `https://docs.discord.com/developers/topics/oauth2` and
`https://docs.discord.com/developers/platform/oauth2-and-permissions`, retrieved 2026-08-26.
