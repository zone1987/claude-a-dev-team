# App Setup for Local Development

Creating the app, fetching its credentials, and configuring it so a locally-running process can act
as it. Every step below is stated on one of the pages cited at the bottom; nothing is inferred.

## Contents

- [Creating the app](#creating-the-app)
- [The three credentials](#the-three-credentials)
- [Token handling and reset](#token-handling-and-reset)
- [Configuring the bot user](#configuring-the-bot-user)
- [Privileged intents in the portal](#privileged-intents-in-the-portal)
- [Installation contexts](#installation-contexts)
- [Install links](#install-links)
- [Default install settings: scopes and permissions](#default-install-settings-scopes-and-permissions)
- [Installing to a test server and a user account](#installing-to-a-test-server-and-a-user-account)
- [Authentication headers](#authentication-headers)
- [API versioning](#api-versioning)
- [The User-Agent requirement](#the-user-agent-requirement)
- [Libraries the docs point at](#libraries-the-docs-point-at)
- [Where the documentation is silent](#where-the-documentation-is-silent)

## Creating the app

From the Getting Started walkthrough:

> First, you'll need to create an app in the developer portal if you don't have one already.

The create-app entry point is `https://discord.com/developers/applications?new_application=true`.
Enter a name, press **Create**.

> After you create your app, you'll land on the **General Information** page of the app's settings
> where you can update basic information about your app like its description and icon. You'll also
> see an **Application ID** and **Interactions Endpoint URL**, which we'll use a bit later in the
> guide.

The Cloudflare Workers tutorial gives the same sequence more briefly:

* Visit [https://discord.com/developers/applications](https://discord.com/developers/applications)
* Click `New Application`, and choose a name
* Copy your **Public Key** and **Application ID**, and put them somewhere locally (we'll need these later)

Caption of the accompanying screenshot: *IDs found in app settings*.

The `bots/overview` page states the same four steps as a checklist:

* **Create an application** in the Discord Developer Portal. This is where your bot token, OAuth2 credentials, and configuration live.
* **Add a bot user** to your application from the Bot tab. This generates the token your code uses to authenticate.
* **Invite the bot** to a server using an OAuth2 URL with the bot scope and the permissions your bot requires.
* **Connect to the API** using the Gateway for real-time events, the HTTP API for REST operations, or both.

For an Activity, the app creation step adds a note about teams:

> Launching a non-distributed Activity is limited to you or members of the developer team, so if
> you're collaborating with others during development, create a
> [developer team](https://discord.com/developers/teams) and set it to the owner when you create the app.

## The three credentials

Both tutorials pull exactly three values into `.env`. Verbatim from the Getting Started guide:

> We'll need three values from your app's settings for your `.env` file:
>
> * On the [**General Information** page](https://discord.com/developers/applications/select/information), copy the value for **Application ID**. In `.env`, replace `<YOUR_APP_ID>` with the ID you copied.
> * Back on the [**General Information** page](https://discord.com/developers/applications/select/information), copy the value for **Public Key**, which is used to ensure HTTP requests are coming from Discord. In `.env`, replace `<YOUR_PUBLIC_KEY>` with the value you copied.
> * On the [**Bot** page](https://discord.com/developers/applications/select/bot) under **Token**, click "Reset Token" to generate a new bot token. In `.env`, replace `<YOUR_BOT_TOKEN>` with your new token.

What each is for, in upstream's own words:

| Credential | Portal page | Purpose upstream states |
|---|---|---|
| **Application ID** | General Information | The app's identifier; appears in every command and webhook route as `{application.id}` |
| **Public Key** | General Information | "used to ensure HTTP requests are coming from Discord" — the Ed25519 verification key |
| **Bot token** | Bot → Token | "used to authorize API requests and carry your app's permissions" |

An Activity needs a different pair, from the **OAuth2** page rather than General Information:

> 1. **Client ID**: Copy the value for Client ID and add it to your `.env` file as **`VITE_CLIENT_ID`**. This is the public ID that Discord associates with your app, and is almost always the same as your App ID.
> 2. **Client Secret**: Copy the value for Client Secret and add it to your `.env` as **`DISCORD_CLIENT_SECRET`**. This is a private, sensitive identifier that your app will use to grant an OAuth2 `access_token`, and should never be shared or checked into version control.

The Cloudflare Workers tutorial adds a fourth value for testing, the Guild ID of your test server:

> You'll also need the Guild ID for the server where your app is installed. This can be found in
> the URL when you visit any channel in that server.
>
> For example, if my URL was `https://discord.com/channels/123456/789101112`, the Guild ID is the
> first number—in this case **`123456`**.

## Token handling and reset

Two warnings, both verbatim:

> Your token is used to authorize API requests and carry your app's permissions, so they are
> *highly* sensitive. Make sure to never share your token or check it into any kind of version
> control.

> You won't be able to view your token again unless you regenerate it, so make sure to keep it
> somewhere safe (like in a password manager).

The Cloudflare tutorial says the same:

> For security reasons, you can only view your bot token once. If you misplace your token, you'll
> have to generate a new one.

and recommends storage: "I like to put these tokens in a password manager like
[1password](https://1password.com/) or [lastpass](https://www.lastpass.com/))."

**Reset is the documented mechanism for getting a token at all.** The setup step is "click 'Reset
Token' to generate a new bot token" — so the same button is both first issuance and rotation after
a leak. Upstream does not describe a separate revoke action.

**Discord can reset your token for you.** From the Gateway page:

> Clients are limited to 1000 `IDENTIFY` calls to the websocket in a 24-hour period. This limit is
> global and across all shards, but does not include `RESUME` calls. Upon hitting this limit, all
> active sessions for the app will be terminated, the bot token will be reset, and the owner will
> receive an email notification. It's up to the owner to update their application with the new token.

That is a real hazard while iterating: a crash-restart loop that re-identifies is spending from a
1000-per-day budget, and exhausting it invalidates the token you have in `.env`.

## Configuring the bot user

> Newly-created apps have a bot user enabled by default. Bot users allow your app to appear and
> behave similarly to other server members when it's installed to a server.

> On the left hand sidebar in your app's settings, there's a [**Bot** page](https://discord.com/developers/applications/select/bot)
> (where we fetched the token from). On this page, you can also configure settings like its
> privileged intents or whether it can be installed by other users.

## Privileged intents in the portal

The Getting Started guide's introduction to intents:

> Intents determine which events Discord will send your app when you're creating a Gateway API
> connection. For example, if you want your app to perform an action when users add a reaction to a
> message, you can pass the `GUILD_MESSAGE_REACTIONS` (`1 << 10`) intent.
>
> Some intents are privileged, meaning they allow your app to access data that may be considered
> sensitive (like the contents of messages). Privileged intents can be toggled on the **Bot** page
> in your app's settings, but they must be approved before you verify your app. Standard,
> non-privileged intents don't require any additional permissions or configurations.

The three privileged intents, from the Gateway page:

* `GUILD_PRESENCES`
* `GUILD_MEMBERS`
* `MESSAGE_CONTENT`

How to enable them:

> Before using privileged intents, you must enable them in your app's settings. In the Developer
> Portal, you can navigate to your app's settings, then toggle the privileged intents on the
> [**Bot** page](https://discord.com/developers/applications/select/bot) under the "Privileged
> Gateway Intents" section. You may only toggle privileged intents that your bot requires to
> function.

> Before you can specify any of these privileged intents in your `IDENTIFY` payload, you must
> enable the specific privileged intents you need in the Developer Portal.

The user-installable tutorial shows a concrete case:

> The sample app fetches members in the server when constructing a fake game leaderboard. Getting
> server members requires a special permission called a privileged intent, so we'll add that to our
> app.
>
> Go to the **Bot** page and find the **Privileged Gateway Intents** section. Toggle "Server Member
> Intent" to be active.

**Thresholds for review**, which decide whether toggling is enough:

> Apps with fewer than 10,000 users can access privileged intents by enabling them in the Developer
> Portal.

> When an app has more than 10,000 unique users who can see your app across all the servers it's
> in, it requires review for continued access to Privileged Intents. Once you hit this threshold,
> the app or team owner will receive a system DM and/or an email. There will also be a callout
> visible on your app in the Developer Portal. You will need to submit a request with information
> about your app and its use of Privileged Intents for review. If access is granted, you can enable
> the relevant intents for your app in the Developer Portal and you will be notified annually to
> reapply for continued access.

> Apps that qualify for verification **must** be approved for the privileged intent(s) before they
> can use them. After your app is verified, you can request privileged intents within the app's
> settings within the Developer Portal.

**Privileged intents also gate HTTP endpoints, independently of the Gateway:**

> In addition to Gateway restrictions, privileged intents also affect the HTTP API endpoints your
> app is permitted to call, and the data it can receive. For example, to use the List Guild Members
> endpoint, your app must enable the `GUILD_MEMBERS` intent (and be approved for it if eligible for
> verification).
>
> HTTP API restrictions are independent of Gateway restrictions, and are unaffected by which intents
> your app passes in the `intents` parameter when Identifying.

So an HTTP-only app with no Gateway connection still needs the portal toggle to read members. See
[VERIFYING-AND-DEBUGGING.md](VERIFYING-AND-DEBUGGING.md) for what a missing intent looks like at
runtime.

## Installation contexts

> **Installation contexts** determine where your app can be installed: to servers, to users, or
> both. Apps can choose which installation contexts they support within the app's settings.
>
> * Apps installed in a **server context** (server-installed apps) must be authorized by a server member with the `MANAGE_GUILD` permission, and are visible to all members of the server.
> * Apps installed in a **user context** (user-installed apps) are visible only to the authorizing user, and therefore don't require any server-specific permissions. Apps installed to a user context are visible across all of the user's servers, DMs, and GDMs—however, they're limited to using commands.

The two integration type IDs, from the Application resource page:

| Type | ID | Description |
|---|---|---|
| `GUILD_INSTALL` | 0 | App is installable to servers |
| `USER_INSTALL` | 1 | App is installable to users |

**The default matters for local testing:** "By default, newly-created apps only support
installation to guilds."

How to change it:

> Click on [**Installation**](https://discord.com/developers/applications/select/installation) in
> the left sidebar, then under **Installation Contexts** make sure both "User Install" and "Guild
> Install" are selected.

> Some apps may only want to support one installation context—for example, a moderation app may
> only support a server context. However, by default, we recommend supporting both installation
> contexts.

And a consequence that will bite mid-development:

> If you update your app to support a new installation context, you will need to update your
> existing commands if you want them to be supported in the new context.

Detail on each context:

> Apps installed in a server context (server-installed apps) must be authorized by a server member
> with the `MANAGE_GUILD` permission. Server-installed apps are *visible* to all members of the
> server, but other factors (like command permissions) determine where and when specific members
> can interact with the app.

> Apps that support the user installation context are visible across all of an authorizing user's
> servers, DMs, and GDMs, but are forced to respect the user's permissions in the surface where the
> app is being used. For example, if a user invokes a command for a user-installed app from a
> server's channel where they don't have permission to send messages, the app won't be able to
> respond to an interaction with a non-ephemeral message.

## Install links

Three options exist:

> There are three options when configuring an install link for your app: "Discord Provided Link",
> "Custom URL", and "None". If you don't configure an install link (by selecting "None"), the "Add
> App" button will not appear for your app, and your app will not be eligible for the App Directory.

The tutorials both select the Discord Provided Link:

> On the [**Installation** page](https://discord.com/developers/applications/select/installation),
> go to the **Install Link** section and select "Discord Provided Link" if it's not already
> selected.
>
> When Discorded Provided Link is selected, a new **Default Install Settings** section will appear.

What a Discord Provided Link is:

> The default Discord Provided Link is a short link that guides users through the installation flow
> with your app's configured installation contexts. If your app has both **User Install** and
> **Guild Install** enabled, the user can choose which way to install your app.
>
> Discord Provided Links don't have scopes or bot user permissions defined in the URL. For example:

```
https://discord.com/oauth2/authorize?client_id=1234567895647001626
```

> Instead, these links will prompt the user for the scopes and bot user permissions configured in
> your Default Install Settings.

> Discord Provided Links are limited to the `application.commands` and `bot` scopes

A Custom URL is the alternative: "commonly an OAuth2 `/authorize` URL that has defined scopes,
permissions, and an installation context (`integration_type`)."

## Default install settings: scopes and permissions

> When creating an app, scopes and permissions determine what your app can do and access in Discord.
>
> * OAuth2 Scopes determine what data access and actions your app can take, granted on behalf of an installing or authenticating user.
> * Permissions are the granular permissions for your bot user, the same as other users in Discord have. They can be approved by the installing user or later updated within server settings or with permission overwrites. Since apps installed to a user context can only respond to commands, these permissions are only relevant to apps installed to a server.

The concrete configuration both tutorials use:

> On the [**Installation** page](https://discord.com/developers/applications/select/installation) in
> the **Default Install Settings** section:
>
> * For **User Install**, add the `applications.commands` scope
> * For **Guild Install**, add the `applications.commands` scope and `bot` scope. When you select `bot`, a new **Permissions** menu will appear to select the bot user's permissions. Select any permissions that you may want for your app—for now, I'll just select `Send Messages`.

Screenshot caption: *Default Install Settings*.

> At the moment, apps installed to a user context only support the `applications.commands` scope
> (which allows your app to install commands) in the default install settings.

The Cloudflare Workers tutorial uses the older **OAuth2 URL Generator** path instead:

> * Click on the [OAuth2 tab](https://discord.com/developers/applications/select/oauth2/url-generator), and choose the `URL Generator`. Click the `bot` and `applications.commands` scopes.
> * Check the boxes next to `Send Messages` and `Use Slash Commands`, then copy the `Generated URL`.
> * Paste the URL into the browser and follow the OAuth flow, selecting the server where you'd like to develop and test your bot.

Screenshot caption: *Configuring bot permissions in app settings*.

## Installing to a test server and a user account

The one explicit piece of guidance upstream gives about *where* to test:

> When developing apps, you should build and test on your user account (for user-installable apps)
> and in a server that isn't actively used by others (for server-installable apps). If you don't
> have your own server already, you can
> [create one for free](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-).

**Install to server**

> To install your app to your test server, copy the default Install Link for your app from the
> **Installation** page. Paste the link in your browser and hit enter, then select "Add to server"
> in the installation prompt.
>
> Select your test server, and follow the installation prompt. Once your app is added to your test
> server, you should see it appear in the member list.

That last sentence is the first working verification: **the app appearing in the member list means
installation succeeded**, before any code runs.

**Install to user account**

> Next, install your app to your user account. Paste the same Install Link in your browser and hit
> enter. This time, select "Add to my apps" in the installation prompt.
>
> Follow the installation prompt to install your app to your user account. Once it's installed you
> can open a DM with it.

## Authentication headers

From the API Reference:

> Authenticating with the Discord API can be done in one of two ways:
>
> 1. Using a bot token found on the Bot page within your app's settings.
> 2. Using an OAuth2 bearer token gained through the OAuth2 API.
>
> For all authentication types, authentication is performed with the `Authorization` HTTP header in
> the format `Authorization: TOKEN_TYPE TOKEN`.

**Example Bot Token Authorization Header**

```bash
Authorization: Bot MTk4NjIyNDgzNDcxOTI1MjQ4.EXAMPLE.NOT_A_REAL_TOKEN_REDACTED
```

Discord's own page prints a full example token here. It is replaced above with a placeholder of the same shape, because a literal token string trips secret scanners in any repository that carries this plugin. The shape is what the page teaches: three parts separated by dots, the first being the base64-encoded application ID.

**Example Bearer Token Authorization Header**

```bash
Authorization: Bearer EXAMPLE_BEARER_TOKEN_REDACTED
```

Command registration accepts either: "For authorization, all endpoints take either a bot token or
client credentials token for your application" — the latter needing the
`applications.commands.update` scope.

`GET /gateway` "does not require authentication"; `GET /gateway/bot` "requires authentication using
a valid bot token." So a token problem shows up on `/gateway/bot` and not on `/gateway`, which
makes the pair a cheap credential test.

## API versioning

> Discord exposes different versions of our API. You should specify which version to use by
> including it in the request path like `https://discord.com/api/v{version_number}`. Omitting the
> version number from the route will route requests to the current default version (marked below).

| Version | Status | Default |
| ------- | ------------ | ------- |
| 10 | Available | |
| 9 | Available | |
| 8 | Deprecated | |
| 7 | Deprecated | |
| 6 | Deprecated | ✓ (default) |
| 5 | Discontinued | |
| 4 | Discontinued | |
| 3 | Discontinued | |

> Some API and Gateway versions are now non-functioning, and are labeled as discontinued in the
> table below for posterity. Trying to use these versions will fail and return 400 Bad Request.

**The default is v6, which is deprecated** — so omitting the version segment locally is a trap.
Both sample apps use `v10` explicitly: `https://discord.com/api/v10/applications/...`.

> All HTTP-layer services and protocols (e.g. HTTP, WebSocket) within the Discord API are using TLS 1.2.

## The User-Agent requirement

> Clients using the HTTP API must provide a valid User Agent which specifies information about the
> client library and version in the following format:

**User Agent Example**

```bash
User-Agent: DiscordBot ($url, $versionNumber)
```

> Clients may append more information and metadata to the end of this string as they wish.

> Client requests that do not have a valid User Agent specified may be blocked and return a
> Cloudflare error.

A local script written with raw `fetch` or `requests` sends whatever default User-Agent the runtime
supplies, so this is a real local-development failure mode: a Cloudflare error rather than a Discord
JSON error.

Content type, from the same page:

> Clients using the HTTP API must provide a valid `Content-Type` header, either `application/json`,
> `application/x-www-form-urlencoded`, or `multipart/form-data`, except where specified. Failing to
> do so will result in a `50035` "Invalid form body" error.

And for the `PING` handshake specifically: "You must provide a valid `Content-Type` when responding
to `PING`s."

## Libraries the docs point at

> Discord does not maintain official SDKs. The following table is an inexhaustive list of
> third-party libraries that have valid rate limit implementations, are recently maintained, and
> have large communities of active bots.

| Name | Language |
| ---- | -------- |
| [Concord](https://github.com/Cogmasters/concord) | C |
| [Discord.Net](https://github.com/discord-net/Discord.Net) | C# |
| [DSharpPlus](https://github.com/DSharpPlus/DSharpPlus) | C# |
| [D++](https://github.com/brainboxdotcc/DPP) | C++ |
| [discljord](https://github.com/discljord/discljord) | Clojure |
| [DiscordGo](https://github.com/bwmarrin/discordgo) | Go |
| [Discord4J](https://github.com/Discord4J/Discord4J) | Java |
| [JDA](https://github.com/DV8FromTheWorld/JDA) | Java |
| [discord.js](https://github.com/discordjs/discord.js) | JavaScript |
| [Eris](https://github.com/abalabahaha/eris) | JavaScript |
| [Oceanic](https://github.com/OceanicJS/Oceanic) | JavaScript |
| [Discordia](https://github.com/SinisterRectus/Discordia) | Lua |
| [DiscordPHP](https://github.com/discord-php/DiscordPHP) | PHP |
| [discord.py](https://github.com/Rapptz/discord.py) | Python |
| [disnake](https://github.com/DisnakeDev/disnake) | Python |
| [hikari](https://github.com/hikari-py/hikari) | Python |
| [interactions.py](https://github.com/interactions-py/library) | Python |
| [nextcord](https://github.com/nextcord/nextcord) | Python |
| [pycord](https://github.com/Pycord-Development/pycord) | Python |
| [discordrb](https://github.com/shardlab/discordrb) | Ruby |
| [Serenity](https://github.com/serenity-rs/serenity) | Rust |

For HTTP interactions specifically, the docs recommend a library over hand-rolling verification:

> We highly recommend checking out our Community Resources and the libraries found there. They not
> only provide typing for Interactions data models, but also include decorators for API frameworks
> like Flask and Express to make validation easy.

The interaction-verification libraries upstream lists:

* C# — [Discord.Net.Rest](https://github.com/discord-net/Discord.Net), [DSharpPlus.Http.AspNetCore](https://github.com/DSharpPlus/DSharpPlus)
* Clojure — [ring-discord-auth](https://github.com/JohnnyJayJay/ring-discord-auth)
* Dart — [nyxx_interactions](https://github.com/l7ssha/Nyxx)
* Go — [tempest](https://github.com/amatsagu/tempest)
* Javascript — [discord-interactions-js](https://github.com/discord/discord-interactions-js), [discord-slash-commands](https://github.com/MeguminSama/discord-slash-commands) and its [Deno fork](https://deno.land/x/discord_slash_commands), [slash-create](https://github.com/Snazzah/slash-create)
* Python — [discord-interactions-python](https://github.com/discord/discord-interactions-python), [discord-interactions.py](https://github.com/LiBa001/discord-interactions.py), [dispike](https://github.com/ms7m/dispike), [flask-discord-interactions](https://github.com/breqdev/flask-discord-interactions)
* PHP — [discord-interactions-php](https://github.com/discord/discord-interactions-php)
* Other — [caddy-discord-interactions-verifier](https://github.com/CarsonHoffman/caddy-discord-interactions-verifier), [BotForge's Application Commands Builder & Previewer](https://tools.botforge.org/appbuilder), [Bsati's Slash Command Builder](https://bsati.github.io/dc-app-command-builder/)

Tools relevant while testing locally:

* **Intent calculators**: [ziad87's](https://ziad87.net/intents/), [Larko's](https://discord-intents-calculator.vercel.app/)
* **Permission calculators**: [BotForge's](https://tools.botforge.org/permissions), [FiniteReality's](https://finitereality.github.io/permissions-calculator/?v=0), [abalabahaha's](https://discordapi.com/permissions.html#0)
* **Embed previewers**: [JohnyTheCarrot's](https://github.com/JohnyTheCarrot/discord-embed-previewer) (browser extension), [AshMW's](https://embedl.ink) (embed HTML generation)
* **API types**: [dasgo](https://github.com/switchupcb/dasgo) (Go), [discord-api-types](https://github.com/discordjs/discord-api-types) (JavaScript)
* **OpenAPI spec**: [discord/discord-api-spec](https://github.com/discord/discord-api-spec), an OpenAPI 3.1 spec — "currently in public preview and **is subject to breaking changes**"

The support hub upstream names: the
[Official Discord Developers server](https://discord.gg/discord-developers), "a developer ran, but
community driven, support hub."

## Where the documentation is silent

- **No separate token revoke.** "Reset Token" is the only documented action. Upstream does not
  describe invalidating a leaked token without issuing a replacement, nor how long an old token
  remains valid after a reset.
- **No guidance on separate development and production apps for bots.** The Activities local
  development page recommends it ("A typical pattern is for each developer to have their own
  'development-only' application"), but no bot page says whether to use one app or two. You decide.
- **No `.env` file format specification.** The tutorials say to rename `.env.sample` to `.env` and
  substitute placeholders; the placeholder names come from the sample repositories, not from a
  documented contract. Only `PORT` is documented as a variable the sample app reads.
- **Nothing on secret management for a locally-run bot** beyond "use a password manager" and "never
  check it into version control." `wrangler secret put` is documented only for Cloudflare Workers.

## Source

Retrieved 2026-08-26 from:

- `docs.discord.com/developers/quick-start/getting-started`
- `docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers`
- `docs.discord.com/developers/tutorials/developing-a-user-installable-app`
- `docs.discord.com/developers/activities/building-an-activity`
- `docs.discord.com/developers/bots/overview`
- `docs.discord.com/developers/resources/application`
- `docs.discord.com/developers/events/gateway`
- `docs.discord.com/developers/interactions/application-commands`
- `docs.discord.com/developers/interactions/overview`
- `docs.discord.com/developers/reference`
- `docs.discord.com/developers/developer-tools/community-resources`
