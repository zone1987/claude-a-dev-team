# Local Development of a Discord App

How to run and test a Discord app locally, assembled strictly from what the three walkthrough pages
state: `quick-start/getting-started`, `tutorials/hosting-on-cloudflare-workers`, and
`tutorials/developing-a-user-installable-app`.

Everything below is what those pages state. Where they are silent, that is said explicitly rather
than filled in.

Sources, all retrieved 2026-08-26:
[Building your first Discord Bot](https://docs.discord.com/developers/quick-start/getting-started),
[Hosting a Reddit API Discord app on Cloudflare Workers](https://docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers),
[Developing A User-Installable App](https://docs.discord.com/developers/tutorials/developing-a-user-installable-app).

## Contents

- [Creating the app and getting credentials](#creating-the-app-and-getting-credentials)
- [Token security and regeneration](#token-security-and-regeneration)
- [`.env` handling](#env-handling)
- [Gateway connection versus HTTP interactions endpoint](#gateway-connection-versus-http-interactions-endpoint)
- [Registering commands: guild-scoped versus global](#registering-commands-guild-scoped-versus-global)
- [Setting up the Interactions Endpoint URL](#setting-up-the-interactions-endpoint-url)
- [What Discord requires of the endpoint](#what-discord-requires-of-the-endpoint)
- [Local tunnelling with ngrok](#local-tunnelling-with-ngrok)
- [Installing the app for testing](#installing-the-app-for-testing)
- [Deploying instead of tunnelling: Cloudflare Workers](#deploying-instead-of-tunnelling-cloudflare-workers)
- [What the upstream pages do not state](#what-the-upstream-pages-do-not-state)

## Creating the app and getting credentials

Every app starts as an application in the Developer Portal. Create it at
https://discord.com/developers/applications?new_application=true — enter a name, press **Create**.
You land on the **General Information** page.

Three credentials are needed, and each page names the same three with the same source location:

| Credential | Where it comes from | What it is for |
| --- | --- | --- |
| **Application ID** | **General Information** page (https://discord.com/developers/applications/select/information) | Identifies the app; used in HTTP API paths such as `applications/<APP_ID>/commands` and in the `webhooks/<APP_ID>/<token>/...` routes |
| **Public Key** | **General Information** page | "used to ensure HTTP requests are coming from Discord" — the Ed25519 key used to verify interaction request signatures |
| **Bot token** | **Bot** page (https://discord.com/developers/applications/select/bot), under **Token**, click "Reset Token" | Authorizes API requests and carries the app's permissions |

In the sample projects these map to the `.env` placeholders `<YOUR_APP_ID>`, `<YOUR_PUBLIC_KEY>` and
`<YOUR_BOT_TOKEN>`. In the Cloudflare Workers tutorial the same three values become the Worker
secrets `DISCORD_APPLICATION_ID`, `DISCORD_PUBLIC_KEY` and `DISCORD_TOKEN`.

The Cloudflare tutorial additionally uses a **Guild ID** as the secret `DISCORD_TEST_GUILD_ID`. It
states where to find it: "This can be found in the URL when you visit any channel in that server."
For the URL `https://discord.com/channels/123456/789101112`, the Guild ID is the first number, here
`123456`.

**Bot user existence.** Newly-created apps have a bot user **enabled by default**. Bot users allow
your app to appear and behave similarly to other server members when it is installed to a server.

**Privileged intents.** Whether you need to toggle anything on the **Bot** page depends on the app.
The getting-started guide states that nothing additional needs configuring for its rock-paper-scissors
app. The user-installable tutorial does need one: its sample app fetches members in the server to
build a leaderboard, so it instructs going to the **Bot** page, finding the **Privileged Gateway
Intents** section, and toggling **"Server Member Intent"** to active. Privileged intents "must be
approved before you verify your app"; standard, non-privileged intents "don't require any additional
permissions or configurations".

## Token security and regeneration

All three pages state the same rule with the same emphasis.

- "Your token is used to authorize API requests and carry your app's permissions, so they are
  *highly* sensitive. Make sure to **never share your token or check it into any kind of version
  control**."
- "You won't be able to view your token again unless you regenerate it, so make sure to keep it
  somewhere safe (like in a password manager)." The Cloudflare tutorial puts the same point as: "For
  security reasons, you can only view your bot token once. **If you misplace your token, you'll have
  to generate a new one.**"
- Regeneration is the same control as first retrieval: on the **Bot** page under **Token**, click
  **"Reset Token"**. The getting-started guide uses that button to obtain the first token, so a
  leaked token is replaced by the same action, which invalidates the old one.
- The community-invites tutorial repeats the rule inside its code samples as a comment: "IMPORTANT:
  Never hardcode tokens or commit them to version control. Use environment variables or a secure
  configuration management system."

## `.env` handling

What the pages state about `.env`, and nothing more:

- Both Express-based sample projects ship a **`.env.sample`** file. The instruction is to **rename
  `.env.sample` to `.env`** — "`.env` is where we'll store all of your app's credentials."
- The placeholders inside are replaced in place: `<YOUR_APP_ID>`, `<YOUR_PUBLIC_KEY>`,
  `<YOUR_BOT_TOKEN>`.
- Both sample project structures list a **`.gitignore`** alongside `.env`, and the getting-started
  project structure annotates `.env` as "your credentials and IDs".
- One further variable is documented: **`PORT`**. "By default, the server will listen to requests
  sent to port 3000, but if you want to change the port, you can specify a `PORT` variable in your
  `.env` file."
- The app code reads these through `process.env` — the sample code uses `process.env.APP_ID` when
  building webhook routes, and the Cloudflare `register.js` uses `process.env.DISCORD_TOKEN` and
  `process.env.DISCORD_APPLICATION_ID`.

The pages do **not** state that `.env` is listed inside `.gitignore`, only that a `.gitignore` exists
in the project. They also do not describe any `.env` loading library or mechanism.

## Gateway connection versus HTTP interactions endpoint

This is the decision that determines whether you need a public URL at all, and the pages state both
sides.

**The two APIs.** The overview and getting-started pages describe them as:

- **HTTP API** — "a REST-like API for general operations like sending and updating data in Discord,
  or fetching data about a resource."
- **Gateway API** — "a WebSocket-based API that is helpful for maintaining state or listening to
  events happening in a Discord server." The Gateway is "a WebSocket connection between your app and
  Discord", and "the connection is bidirectional" — your app can also send events to Discord over
  the same connection.

**Why an interactions endpoint needs a public URL.** The pages are explicit about the direction of
the request. From the Cloudflare tutorial: "your app can receive common events from the client as
webhooks when users interact with your app… **Discord will send these events to a pre-configured
HTTPS endpoint** (called an Interactions Endpoint URL in an app's configuration) as a JSON payload
with details about the event."

From the getting-started guide: "To enable your app to receive slash command and other interactions
requests, **Discord needs a public URL to send them**."

Because Discord initiates that request, a locally-running server is not reachable, which is exactly
why the tutorials introduce a tunnel: "When a user types a slash command, Discord will send an HTTP
request to a public endpoint. **During local development this can be a little challenging**, so we're
going to use a tool called `ngrok` to create an HTTP tunnel."

**The Gateway side.** The Gateway is a connection your app **opens outward** to Discord, described as
"maintaining persistent, stateful websocket connections between your client and our servers". None of
these three pages instruct configuring any URL, tunnel or public endpoint for Gateway use, and the
getting-started guide explicitly notes "We won't be using it in this guide" while still having the app
work end to end over the interactions endpoint alone. So the contrast the pages support is: the
interactions endpoint requires a public HTTPS URL (hence a tunnel locally), whereas the Gateway
walkthroughs on these pages involve no endpoint configuration at all.

**Explicit gap:** none of these three pages states the phrase "the Gateway needs no public URL", nor
do they walk through opening a Gateway connection locally. For the Gateway connection lifecycle, call
the Skill tool with `"discord-gateway"`.

## Registering commands: guild-scoped versus global

The pages document both scopes and one propagation-related fact.

**Global registration.** The getting-started project's `register` script "installs the commands as
global commands by calling the HTTP API's `PUT /applications/<APP_ID>/commands` endpoint" — Bulk
Overwrite Global Application Commands. The command to run, in the project folder:

```
npm run register
```

The user-installable tutorial registers the same way but via the singular endpoint: "The register
command will call the **Create Global Application Command** endpoint for each of the command payloads
in `commands.js`." Same command:

```
npm run register
```

**Guild-scoped registration.** The Cloudflare tutorial names both options directly: "Commands can be
**registered globally**, making them available for all servers with the app installed, or they can be
**registered on a single server**." That tutorial then chooses one: "In this example - we'll just
focus on global commands." Its global registration URL is spelled out in full:

```js
const url = `https://discord.com/api/v10/applications/${applicationId}/commands`;
```

registered with `method: 'PUT'` and the header `Authorization: Bot ${token}`.

The tutorial still provisions a guild ID as a secret (`DISCORD_TEST_GUILD_ID`) for the server where
the app is installed, but the registration code shown uses only the global route.

**The propagation difference these pages document.** One statement, and it concerns global commands.
The comment above `registerGlobalCommands()` in the Cloudflare tutorial's `register.js`:

```js
/**
 * Register all commands globally.  This can take o(minutes), so wait until
 * you're sure these are the commands you want.
 */
```

So the documented cost of global registration is that it "can take o(minutes)". Locally, run it once
before getting started:

```
$ DISCORD_TOKEN=**** DISCORD_APPLICATION_ID=**** node src/register.js
```

**Where the authoritative statement lives.** These three walkthrough pages do not state a
propagation time for guild-scoped commands, do not compare the two numerically, and give no
guild-command registration code sample. The rule itself is documented, but on another page:
`interactions/application-commands` states that "Guild commands update **instantly**" and recommends
guild commands for quick testing and global commands once ready for public use, and its endpoint
descriptions add that a created or edited guild command "will be available in the guild immediately".
Call the Skill tool with `"discord-interactions"` for that page's full scoping and propagation rules
— this is the fastest iteration lever there is, so take it from there rather than from these pages.

**What you should see after registering.** The getting-started guide: "If you navigate back to your
server, you should see the slash commands appear. But if you try to run them, nothing will happen
since your app isn't receiving or handling any requests from Discord." The user-installable tutorial
lists per-surface expectations, and notes the same failure mode: "if you try to run any of the
commands, you'll get an error".

## Setting up the Interactions Endpoint URL

The procedure, identical in substance across the getting-started guide and the user-installable
tutorial:

1. Start your app locally. In the project folder: `npm run start`. "There should be output indicating
   your app is running on port `3000`."
2. Start the tunnel in a **new terminal**: `ngrok http 3000`.
3. Take the **Forwarding** URL from the ngrok output.
4. Go to your app's settings at https://discord.com/developers/applications, and on the **General
   Information** page under **Interaction Endpoint URL**, paste the ngrok forwarding URL and
   **append `/interactions`**. The user-installable tutorial gives a worked example of the result:
   `https://84c5df474.ngrok-free.dev/interactions`.
5. Click **Save Changes** and ensure the endpoint is successfully verified.

Troubleshooting, stated on both pages: "If you have troubles verifying your endpoint, make sure both
ngrok and your app are running on the same port, and that you've copied the ngrok URL correctly."

The Cloudflare tutorial does the same step from its own dashboard flow, and adds the production
hand-off: "This is the process we'll use for local testing and development. When you've published
your app to Cloudflare, you will **want to update this field to use your Cloudflare Worker URL**."

## What Discord requires of the endpoint

Discord verifies the URL before accepting it, and the pages name exactly two requirements the app
must satisfy.

From the getting-started guide, on what the app is already doing behind the scenes: it is "ready to
handle interactions from Discord, which includes **verifying security request headers and responding
to `PING` requests**."

The same page states how the sample app satisfies verification, in two parts:

- "It uses the `PUBLIC_KEY` and
  [discord-interactions package](https://github.com/discord/discord-interactions-js#usage) with a
  wrapper function (imported from `utils.js`) that makes it conform to Express's `verify` interface.
  **This is run on every incoming request to your app.**"
- "It responds to incoming `PING` requests."

**The `PING` handshake.** The Cloudflare tutorial's router code carries the authoritative comment:

```js
if (message.type === InteractionType.PING) {
  // The `PING` message is used during the initial webhook handshake, and is
  // required to configure the webhook in the developer portal.
  console.log('Handling Ping request');
  return new JsonResponse({
    type: InteractionResponseType.PONG,
  });
}
```

So a `PING` interaction must be answered with an interaction response of type `PONG`, and that
handshake is what makes configuring the endpoint in the developer portal possible.

**Signature verification, concretely.** The Cloudflare tutorial shows the exact headers and the exact
check, for a `POST`:

```js
if (request.method === 'POST') {
  // Using the incoming headers, verify this request actually came from discord.
  const signature = request.headers.get('x-signature-ed25519');
  const timestamp = request.headers.get('x-signature-timestamp');
  const body = await request.clone().arrayBuffer();
  const isValidRequest = verifyKey(
    body,
    signature,
    timestamp,
    env.DISCORD_PUBLIC_KEY
  );
  if (!isValidRequest) {
    console.error('Invalid Request');
    return new Response('Bad request signature.', { status: 401 });
  }
}
```

The two request headers are therefore **`x-signature-ed25519`** and **`x-signature-timestamp`**, they
are verified against the raw body and the app's **public key**, and the documented response to a
failed check is **HTTP 401** with the body `Bad request signature.`

Both these pages state that they are "skipping over a lot of the details"; for the full preparation
requirements, call the Skill tool with `"discord-interactions"`.

## Local tunnelling with ngrok

All three tutorials use ngrok, and it is the only tunnelling tool they name.

- Installation: "If you don't have ngrok installed locally, you can install it by following the
  instructions on the [ngrok download page](https://ngrok.com/download)."
- Purpose: ngrok is "a tool that lets us tunnel our local server to a public URL where Discord can
  send requests", and it "is going to bounce requests off of an external endpoint, and forward them
  to your machine."
- Invocation, in a **new terminal** while the app keeps running: `ngrok http 3000`
- Expected output, quoted in full by the getting-started guide:

```
Tunnel Status                 online
Version                       2.0/2.0
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://1234-someurl.ngrok.io -> localhost:3000

Connections                  ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

- The **Forwarding** URL is the value you use, and the example forms given across the pages are
  `https://1234-someurl.ngrok.io`, `https://8098-24-22-245-250.ngrok.io` and
  `https://84c5df474.ngrok-free.dev`.
- The Cloudflare project wraps it as an npm script instead: `npm run ngrok`. That project runs its own
  dev server with `npm run dev`.
- A **Web Interface** is exposed at `http://127.0.0.1:4040`; the page shows it in the output but does
  not describe using it.

Both pages note the environment is a choice: "We'll be developing our app locally with a little help
from ngrok, but you can use your preferred development environment."

**Explicit gap:** the pages do not document any alternative tunnel, nor a reserved or stable ngrok
domain, so with a free ephemeral URL the Interaction Endpoint URL has to be re-pasted whenever the
tunnel URL changes. The pages do not state that consequence.

## Installing the app for testing

Testing needs the app installed, and the pages state where to test.

> "When developing apps, you should build and test on your **user account** (for user-installable
> apps) and in a **server that isn't actively used by others** (for server-installable apps). If you
> don't have your own server already, you can
> [create one for free](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-)."

Both Express tutorials install to both contexts using the same link:

- **Install to server** — copy the default Install Link from the **Installation** page, paste it in
  your browser, hit enter, select **"Add to server"**, select your test server, follow the prompt.
  "Once your app is added to your test server, you should see it appear in the member list."
- **Install to user account** — paste the same Install Link, hit enter, select **"Add to my apps"**,
  follow the prompt. "Once it's installed you can open a DM with it."

Prerequisite configuration for that link, from the same pages: under **Installation Contexts** select
both **User Install** and **Guild Install**; under **Install Link** select **Discord Provided Link**;
then in **Default Install Settings** give User Install the `applications.commands` scope, and Guild
Install `applications.commands` plus `bot` (which reveals a **Permissions** menu — both tutorials
select just `Send Messages`).

The Cloudflare tutorial instead uses the **OAuth2 → URL Generator**: select the `bot` and
`applications.commands` scopes, check `Send Messages` and `Use Slash Commands`, copy the
`Generated URL`, "Paste the URL into the browser and follow the OAuth flow, selecting the server
where you'd like to develop and test your bot."

The community-invites tutorial adds one local prerequisite of its own: "**Developer Mode** enabled on
your account (so you can copy role, channel, and user IDs)", used via right-click →
**"Copy Role ID"** / **"Copy Channel ID"** / **"Copy User ID"**.

## Deploying instead of tunnelling: Cloudflare Workers

The Cloudflare tutorial is the one page here that covers hosting rather than tunnelling.

Why it recommends Workers: "Cloudflare Workers are a convenient way to host Discord apps due to the
free tier, simple development model, and automatically managed environment (no VMs!)."

Setup: visit the [Cloudflare Dashboard](https://dash.cloudflare.com/), click the `Workers` tab, create
a new service using the same name as your Discord bot, and
[install the Wrangler CLI](https://developers.cloudflare.com/workers/cli-wrangler/install-update/).

Secrets are set through Wrangler, not `.env`:

```
$ wrangler secret put DISCORD_TOKEN
$ wrangler secret put DISCORD_PUBLIC_KEY
$ wrangler secret put DISCORD_APPLICATION_ID
$ wrangler secret put DISCORD_TEST_GUILD_ID
```

Local run requirements: "This requires at least v16 of Node.js", `npm install`, then `npm run dev`.
The tutorial notes "This depends on the beta version of the `wrangler` package, which better supports
ESM on Cloudflare Workers."

Deploying: the repository "is set up to automatically deploy to Cloudflare Workers when new changes
land on the `main` branch. To deploy manually, run `npm run publish`, which uses the
`wrangler publish` command under the hood." A GitHub Action needs an
[API Token and Account ID from Cloudflare](https://developers.cloudflare.com/workers/cli-wrangler/authentication/)
stored as repository secrets `CF_API_TOKEN` and `CF_ACCOUNT_ID`.

**One constraint that bites in this environment**, stated as a warning: "When using Cloudflare
Workers, your app **won't be able to access non-ephemeral CDN media**. For example, trying to fetch an
image like `https://cdn.discordapp.com/attachments/1234/56789/my_image.png` would result in a `403`
error. Cloudflare Workers are still able to access **ephemeral** CDN media."

The entry point a Worker must expose is a `fetch` function: "Cloudflare Workers require exposing a
`fetch` function, which is called as the entry point for each request." The full code for signature
verification and routing is in `TUTORIALS.md` in this skill.

## What the upstream pages do not state

Named gaps, so a reader does not mistake absence for a rule:

- **No guild-command propagation figure on these pages.** They state that global registration "can
  take o(minutes)" and give no comparable figure for guild-scoped commands. The qualitative rule is
  documented elsewhere: `interactions/application-commands` says guild commands update "instantly"
  and are available "immediately" — call the Skill tool with `"discord-interactions"`.
- **No guild-scoped registration code.** The Cloudflare tutorial names the option and links it, then
  explicitly restricts itself to global commands. No `applications/{app_id}/guilds/{guild_id}/commands`
  sample appears on any of these three pages.
- **No statement that the Gateway needs no public URL.** The contrast is implied by what each API does
  and by the fact that no Gateway URL is ever configured, but the sentence is not on these pages.
- **No local Gateway walkthrough.** None of these pages opens a Gateway connection, sends an
  `Identify`, or handles heartbeats.
- **No `.env` gitignore statement.** A `.gitignore` is listed in both project trees; its contents are
  never shown.
- **No `.env` loader named.** The samples read `process.env`; no dotenv-style library or load step is
  described.
- **No tunnel alternative to ngrok**, and no mention of stable or reserved tunnel URLs.
- **No rate-limit guidance for local testing.** The API reference states rate limits exist and that
  ignoring them gets keys revoked; these three walkthrough pages add nothing about local development.
- **No local test-suite instructions.** The Cloudflare project tree lists `test/test.js` -> "Tests for
  app" and a CI job named `test`, but no page states how to run the tests.

## Source

[Building your first Discord Bot](https://docs.discord.com/developers/quick-start/getting-started),
[Hosting a Reddit API Discord app on Cloudflare Workers](https://docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers),
[Developing A User-Installable App](https://docs.discord.com/developers/tutorials/developing-a-user-installable-app),
with the credential and Developer-Mode prerequisites from
[Using Community Invites](https://docs.discord.com/developers/tutorials/using-community-invites) —
all retrieved 2026-08-26. Rights holder: Discord Inc.
