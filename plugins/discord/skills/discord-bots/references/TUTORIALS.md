# Discord App Tutorials

The three Discord tutorial pages end to end: developing a user-installable app, hosting a Reddit API
app on Cloudflare Workers, and using community invites.

Sources, all retrieved 2026-08-26:
[Developing A User-Installable App](https://docs.discord.com/developers/tutorials/developing-a-user-installable-app),
[Hosting a Reddit API Discord app on Cloudflare Workers](https://docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers),
[Using Community Invites](https://docs.discord.com/developers/tutorials/using-community-invites).

## Contents

- [Developing a user-installable app](#developing-a-user-installable-app)
  - [Step 0: Project setup](#step-0-project-setup)
  - [Step 1: Creating an app](#step-1-creating-an-app)
  - [Step 2: Setting up commands](#step-2-setting-up-commands)
  - [Step 3: Handling interactivity](#step-3-handling-interactivity)
  - [Understanding metadata for interactions](#understanding-metadata-for-interactions)
  - [Using metadata for command interactions](#using-metadata-for-command-interactions)
  - [Using metadata for message component interactions](#using-metadata-for-message-component-interactions)
- [Hosting a Reddit API Discord app on Cloudflare Workers](#hosting-a-reddit-api-discord-app-on-cloudflare-workers)
  - [Creating an app on Discord](#creating-an-app-on-discord)
  - [Adding bot permissions](#adding-bot-permissions)
  - [Creating your Cloudflare Worker](#creating-your-cloudflare-worker)
  - [Running locally](#running-locally)
  - [Deployment](#deployment)
  - [Code deep dive](#code-deep-dive)
- [Using community invites](#using-community-invites)
  - [Understanding community invites features](#understanding-community-invites-features)
  - [Role granting invite example](#role-granting-invite-example)
  - [Target users example](#target-users-example)

## Developing a user-installable app

> Tutorial for creating Discord apps that can be installed to user accounts.

Discord apps can be installed to **servers, users, or both**. This guide walks through building a
basic game integration app that is installable to both Discord users and servers.

While the tutorial focuses on supporting different installation contexts, it builds a basic game
integration along the way with a wiki lookup with user-specific bookmarking and a server
leaderboard. The app has four commands (`/link`, `/profile`, `/leaderboard`, and `/wiki`) that can be
run in different installation and interaction contexts.

**Resources used in this guide**

- **[GitHub repository](https://github.com/discord/user-install-example)** where the code from this
  guide lives.
- **[discord-interactions](https://github.com/discord/discord-interactions-js)**, a library that
  provides types and helper functions for Discord apps.
- **[Express](https://expressjs.com/)**, a popular JavaScript web framework used to create a server
  where Discord can send requests.
- **[ngrok](https://ngrok.com/)**, a tool that lets you tunnel your local server to a public URL
  where Discord can send requests.

### Step 0: Project setup

You need the project code from the
[sample app repository](https://github.com/discord/user-install-example).

**Project structure**

```
├── .env.sample -> sample .env file
├── app.js      -> main entrypoint for the app
├── commands.js -> slash command payloads + helpers
├── game.js     -> logic specific to the fake game
├── utils.js    -> utility functions and enums
├── package.json
├── README.md
└── .gitignore
```

> **Info**
> The guide develops the app locally with a little help from [ngrok](https://ngrok.com/), but you can
> use your preferred development environment.

If you don't have [NodeJS](https://nodejs.org/en/download/) installed, install that first.

Now, clone the project code to your machine using the command line:

```
git clone https://github.com/discord/user-install-example.git
```

Then navigate to the directory and install the project's dependencies:

```
# navigate to directory
cd user-install-example

# install dependencies
npm install
```

### Step 1: Creating an app

First, create an app in the developer portal if you don't have one already: **Create App** →
https://discord.com/developers/applications?new_application=true

Enter a name for your app, then press **Create**. After you create your app, you land on the
**General Information** page of the app's settings where you can update basic information about your
app like its description and icon.

#### Fetching app credentials

> **Warning**
> Your token is used to authorize API requests and carry your app's permissions, so they are
> *highly* sensitive. Make sure to never share your token or check it into any kind of version
> control.

Back in your project folder, rename the `.env.sample` file to `.env`. `.env` is where all of your
app's credentials are stored.

Three values are needed from your app's settings for your `.env` file:

- On the **General Information** page
  (https://discord.com/developers/applications/select/information), copy the value for
  **Application ID**. In `.env`, replace `<YOUR_APP_ID>` with the ID you copied.
- Back on the **General Information** page, copy the value for **Public Key**, which is used to
  ensure HTTP requests are coming from Discord. In `.env`, replace `<YOUR_PUBLIC_KEY>` with the
  value you copied.
- On the **Bot** page (https://discord.com/developers/applications/select/bot) under **Token**,
  click "Reset Token" to generate a new bot token. In `.env`, replace `<YOUR_BOT_TOKEN>` with your
  new token.

#### Add Guild Members intent

The sample app fetches members in the server when constructing a fake game leaderboard. Getting
server members requires a special permission called a **privileged intent**.

Go to the **Bot** page and find the **Privileged Gateway Intents** section. Toggle **"Server Member
Intent"** to be active.

#### Choosing supported installation contexts

An app's **installation context** defines how it's installed: to a server, to a user, or both.

This app is configured to support both installation contexts, and while that's a good default for
most apps, some apps may only make sense in one context or the other.

In your app's settings, go to the **Installation** page
(https://discord.com/developers/applications/select/installation) from the sidebar. Under
**Installation Contexts**, check both **User Install** and **Guild Install**, then press
**Save Changes**.

#### Configuring default install settings

The default install settings of your app determine the default **scopes** and **bot user permissions**
for each supported installation context. **At the moment, apps installed to a user context only
support the `applications.commands` scope** (which allows your app to install commands) in the default
install settings.

**Update Install Link** — Before adding default install settings, select Discord Provided Link for
the app's install link. Under the **Install Link** section, select `Discord Provided Link` from the
dropdown if it isn't already selected (it should be by default). Once it's selected, the **Default
Install Settings** appear.

**Adding Default Install Settings** — Under the **Default Install Settings** section:

- For **User Install**, add the `applications.commands` scope
- For **Guild Install**, add the `applications.commands` scope and `bot` scope. When you select
  `bot`, a new **Permissions** menu appears to select the bot user's permissions. Select any
  permissions that you may want for your app — the guide selects just `Send Messages`.

> **Info**
> Permissions for a bot user are very similar to permissions for other Discord users. For details
> about permissions and the list of available permissions, call the Skill tool with
> `"discord-platform"`.

After you've selected the scopes and permissions for your app, click **Save Changes**.

*Figure: Installation settings in App Settings*

#### Installing your app

Install your new app to **both** a test server and your user account so that you can test in both
installation contexts.

**Install to server** — To install your app to your test server, copy the default Install Link for
your app from the **Installation** page. Paste the link in your browser and hit enter, then select
"Add to server" in the installation prompt. Select your test server, and follow the installation
prompt. Once your app is added to your test server, you should see it appear in the member list.

**Install to user account** — Next, install your app to your user account. Paste the same Install
Link in your browser and hit enter. This time, select "Add to my apps" in the installation prompt.
Follow the installation prompt to install your app to your user account. Once it's installed you can
open a DM with it.

### Step 2: Setting up commands

Next, register the application commands for your app. Before touching code, understand the concept of
**command contexts**:

Commands have **two context fields** that can be set when creating or updating a command which let you
limit the supported install methods and surfaces in Discord for that command:

- **`integration_types`** lets you control which **installation contexts** a command is supported in
  (user, guild, or both). For example, the `/link` and `/profile` commands are only available when
  the app is installed to a user.
- **`contexts`** lets you set the **interaction contexts**, or the surfaces in Discord, where a
  command can be used (in a guild channel, in your bot user's DM, and within other DMs or GDMs). For
  example, the `/leaderboard` command is only available when the command is run from a guild channel.

#### Commands in the sample project

Four commands are set up for the sample app, all with *slightly* different contexts:

| Name           | Description                                            | Installation Contexts (`integration_types`) | Interaction Contexts (`contexts`)    |
| -------------- | ------------------------------------------------------ | ------------------------------------------- | ------------------------------------ |
| `/leaderboard` | View game leaderboard for the current server           | `GUILD_INSTALL`                             | `GUILD`                              |
| `/wiki`        | Find information about game items and characters       | `GUILD_INSTALL`, `USER_INSTALL`             | `GUILD`, `BOT_DM`, `PRIVATE_CHANNEL` |
| `/profile`     | Get information about your game inventory and progress | `USER_INSTALL`                              | `GUILD`, `BOT_DM`, `PRIVATE_CHANNEL` |
| `/link`        | Link your game account to Discord                      | `USER_INSTALL`                              | `BOT_DM`                             |

> **Info**
> The supported installation contexts for a command affects which interaction contexts you can set.
> Specifically, **the `PRIVATE_CHANNEL` interaction context can only be included in `contexts` if
> `USER_INSTALL` is included in `integration_types`** for the command.

The payloads for the app's commands are in `commands.js` in the project folder in case you want to
change any values or see what the command's context fields (`integration_types` and `contexts`) look
like for each of the commands in the table above.

#### Registering the commands

Now register your app's commands so you can see them in Discord. In your project folder run:

```
npm run register
```

The register command calls the **Create Global Application Command** endpoint for each of the command
payloads in `commands.js`.

After your new commands have been created, go into Discord and look for the commands in the surfaces
where they were made available:

- In **channels within the guild you installed your app**, you should see `/leaderboard`, `/wiki`,
  and `/profile`
- In **channels within any of your guilds**, you should see `/wiki` and `/profile`
- In **your app's DM**, you should see `/wiki`, `/profile`, and `link`
- And finally, **in DMs or GDMs with other users**, you should see `/wiki` and `/profile`

However, if you try to run any of the commands, you'll get an error — which the next step fixes.

### Step 3: Handling interactivity

To receive and handle interactive requests, set up an **Interactions Endpoint URL**, which is a public
URL where Discord sends your app's interactions.

#### Set up a public endpoint

To set up a public endpoint, start your app, which runs an [Express](https://expressjs.com/) server,
then use [ngrok](https://ngrok.com/) to expose your server publicly.

First, go to your project's folder and run the following to start your app:

```
npm run start
```

There should be some output indicating your app is running on port 3000. Behind the scenes, the app
is ready to handle interactions from Discord, which includes verifying security request headers and
responding to `PING` requests.

> **Info**
> By default, the server will listen to requests sent to port 3000, but if you want to change the
> port, you can specify a `PORT` variable in your `.env` file.

Next, start the ngrok tunnel. If you don't have ngrok installed locally, install it by following the
instructions on the [ngrok download page](https://ngrok.com/download).

After ngrok is installed locally, open a new terminal and create a public endpoint that will forward
requests to your Express server:

```
ngrok http 3000
```

The output includes a **Forwarding** URL, which is the publicly-accessible URL used for the
Interactions Endpoint URL in the next step.

#### Configuring an interaction endpoint URL

Go to your app's settings (https://discord.com/developers/applications) and on the **General
Information** page under **Interaction Endpoint URL**, paste your new ngrok URL and append
`/interactions` (it'll be something like `https://84c5df474.ngrok-free.dev/interactions`).

Click **Save Changes** and if all is well, your Interactions Endpoint URL should be verified by
Discord.

> **Info**
> If you have troubles verifying your endpoint, make sure both ngrok and your app is running on the
> same port, and that you've copied the ngrok URL correctly.

### Understanding metadata for interactions

Now that the Interactions Endpoint URL is set up, you should be able to run the app's commands. Go to
your app's DM and run `/profile`, and your app responds with a sample game profile.

Back on the command line, the app logs incoming requests from Discord, so you can see what the
request body for your command invocation looked like.

**Sample interaction payload** — condensed to be more readable, but the interaction request body
looks something like this:

```json
{
  "app_permissions": "442368",
  "application_id": "234248956100616262",
  "authorizing_integration_owners": { "1": "1090372582781497424" },
  "channel": {
    // Partial channel object corresponding to channel_id
  },
  "channel_id": "1234563982236504123",
  "context": 1,
  "data": { "id": "1234358421659193405", "name": "link", "type": 1 },
  "entitlements": [],
  "id": "1234968734674853908",
  "locale": "en-US",
  "token": "a really long interactions token that your app can use to respond to the interactions",
  "type": 2,
  "user": {
    // Partial user object
  },
  "version": 1
}
```

To see which command was run, look at the `data` object.

The tutorial focuses on the metadata related to installation and interaction contexts. There are a
few metadata fields to pay attention to when building an app that can be installed to multiple
interaction contexts:

#### `context`

`context` tells you which **interaction context** the command was invoked from. In the example the
command was triggered from the app's DM, so the `context` is `1` (or `BOT_DM`).

With interaction context, something to keep in mind is that `BOT_DM` is only the *DM with your bot
user*. If you run the same command in a DM with a friend, or in a group DM, the interaction context
is `PRIVATE_CHANNEL` (`2`).

#### `authorizing_integration_owners`

`authorizing_integration_owners` provides data about any ID relevant to the installation context(s)
associated with the interaction.

The keys in the object are the relevant installation context(s) (`GUILD_INSTALL`/`"0"` and/or
`USER_INSTALL`/`"1"`). The values depend on the key, but **for `USER_INSTALL` the key will always be
the ID of the user that authorized your app**.

> **Info**
> `authorizing_integration_owners` is **not** the same as the user that triggered the interaction.
> Information about the user that triggered the interaction is in the `user` object.

#### `app_permissions`

`app_permissions` are the **bitwise set of permissions your app has in the place where the interaction
was triggered**. The permissions your app has will be different for DMs with your app, in servers, and
G(DM)s with other users. In the sample payload, the value is `"442368"`.

These values can be helpful when deciding how you want your app to respond to the interaction. For
example, perhaps you want your app to respond ephemerally when a specific command is invoked from a
server, which the sample app does for the `/profile` command.

### Using metadata for command interactions

The `/profile` command responds **ephemerally**, meaning only the invoking user sees the response,
when invoked from a server. If it's invoked within a DM with the bot user, it responds with a
non-ephemeral message. In the project, you can see this logic in `app.js`:

```javascript
// "profile" command
if (name === 'profile') {
  const profile = getFakeProfile(0);
  const profileEmbed = createPlayerEmbed(profile);

  // Use interaction context that the interaction was triggered from
  const interactionContext = req.body.context;

  // Construct `data` for our interaction response. The profile embed will be included regardless of interaction context
  let profilePayloadData = {
    embeds: [profileEmbed],
  };

  // If profile isn't run in a DM with the app, we'll make the response ephemeral and add a share button
  if (interactionContext !== 1) {
    // Make message ephemeral
    profilePayloadData['flags'] = 64;
    // Add button to components
    profilePayloadData['components'] = [
      {
        type: 1,
        components: [
          {
            type: 2,
            label: 'Share Profile',
            custom_id: 'share_profile',
            style: 2,
          },
        ],
      },
    ];
  }

  // Send response
  return res.send({
    type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
    data: profilePayloadData,
  });
}
```

In the sample app code, the value of `context` in the request body is assigned to a new
`interactionContext` variable. Based on the context, the response to the command interaction is
modified. If it was run in a guild or within a G(DM) other than the DM with the app's bot user,
`flags` is set to `64` to make the response ephemeral, and a new button component is added so that
the user can share their profile if they want.

### Using metadata for message component interactions

Message component interactions can be triggered by **any user the component is visible to**,
regardless of the installation context. Since potentially any user can trigger the component, it can
be helpful to use metadata to understand context about the installation.

Consider adding a new `/game` command supported in the `USER_INSTALL` installation context that a
user could trigger to send a message to whatever guild or group DM they're in to ask others if
they're interested in joining a game match:

*Figure: Sample game command response*

When someone clicks on the button, the app would care about two users when handling the interaction:

1. **User B**, who clicked the "Join" button so the app can track who is interested in joining the
   match
2. **User A**, who ran the `/game` command so the app can tell them who is interested in joining the
   match

There are two additional fields to know about in this scenario:

#### `interaction_metadata`

Messages created in response to an interaction include an **`interaction_metadata` object** which
includes metadata related to the interaction.

#### `authorizing_integration_owners` (for component interactions)

For user-installed apps, it can be used to **differentiate between the user that installed an app and
the user that triggered an app's interaction**, since messages sent in response to interactions
(either an interaction response or a follow-up message) can be visible to users that don't have the
app installed to their account.

**Next Steps** cards: Interactions documentation (`/developers/interactions/overview`) and the
[GitHub repository with sample project](https://github.com/discord/user-install-example).

## Hosting a Reddit API Discord app on Cloudflare Workers

> Tutorial for deploying Discord apps on Cloudflare Workers.

When building Discord apps, your app can receive common events from the client as **webhooks** when
users interact with your app through interactions like application commands or message components.

Discord sends these events to a pre-configured HTTPS endpoint (called an **Interactions Endpoint URL**
in an app's configuration) as a JSON payload with details about the event.

This tutorial walks through building a Discord app powered by
[`r/aww`](https://www.reddit.com/r/aww) using JavaScript. All of the code for this app can be found
**[on GitHub](https://github.com/discord/cloudflare-sample-app)**.

### Features and technologies used

- Discord Interactions API (specifically slash commands)
- [Cloudflare Workers](https://workers.cloudflare.com/) for hosting
- [Reddit API](https://www.reddit.com/dev/api/) to send messages back to the user

### Creating an app on Discord

Create the app through the [Discord Developer Dashboard](https://discord.com/developers/applications):

- Visit https://discord.com/developers/applications
- Click `New Application`, and choose a name
- Copy your **Public Key** and **Application ID**, and put them somewhere locally (needed later)

*Figure: IDs found in app settings*

- Now click on the **Bot** tab (https://discord.com/developers/applications/select/bot) on the left
  sidebar.
- Grab the `token` for your bot, and store it somewhere safe (the guide suggests a password manager
  like [1password](https://1password.com/) or [lastpass](https://www.lastpass.com/)).

> **Warning**
> For security reasons, you can only view your bot token once. If you misplace your token, you'll
> have to generate a new one.

### Adding bot permissions

Now configure the bot with permissions required to create and use slash commands, as well as send
messages in channels.

- Click on the **OAuth2** tab
  (https://discord.com/developers/applications/select/oauth2/url-generator), and choose the
  `URL Generator`. Click the `bot` and `applications.commands` scopes.
- Check the boxes next to `Send Messages` and `Use Slash Commands`, then copy the `Generated URL`.

*Figure: Configuring bot permissions in app settings*

- Paste the URL into the browser and follow the OAuth flow, selecting the server where you'd like to
  develop and test your bot.

### Creating your Cloudflare Worker

Cloudflare Workers are a convenient way to host Discord apps due to the free tier, simple development
model, and automatically managed environment (no VMs).

> **Warning**
> When using Cloudflare Workers, your app **won't be able to access non-ephemeral CDN media**. For
> example, trying to fetch an image like
> `https://cdn.discordapp.com/attachments/1234/56789/my_image.png` would result in a `403` error.
> Cloudflare Workers **are** still able to access ephemeral CDN media.

- Visit the [Cloudflare Dashboard](https://dash.cloudflare.com/)
- Click on the `Workers` tab, and create a new service using the same name as your Discord bot
- Make sure to
  [install the Wrangler CLI](https://developers.cloudflare.com/workers/cli-wrangler/install-update/)
  and set it up.

#### Storing secrets

The production service needs access to some of the information saved earlier. To set those variables,
run:

```
$ wrangler secret put DISCORD_TOKEN
$ wrangler secret put DISCORD_PUBLIC_KEY
$ wrangler secret put DISCORD_APPLICATION_ID
```

You'll also need the **Guild ID** for the server where your app is installed. This can be found in
the URL when you visit any channel in that server.

> **Info**
> For example, if the URL was `https://discord.com/channels/123456/789101112`, the Guild ID is the
> first number — in this case **`123456`**.

Once you know your Guild ID, set that variable as well:

```
$ wrangler secret put DISCORD_TEST_GUILD_ID
```

### Running locally

> **Info**
> This depends on the beta version of the `wrangler` package, which better supports ESM on Cloudflare
> Workers.

Start by cloning the repository and installing dependencies. This requires at least v16 of
[Node.js](https://nodejs.org/en/):

```
$ npm install
```

#### Project structure

```
├── .github/workflows/ci.yaml -> GitHub Action configuration
├── src
├── ├── commands.js           -> JSON payloads for commands
├── ├── reddit.js             -> Interactions with the Reddit API
├── ├── register.js           -> Sets up commands with the Discord API
├── ├── server.js             -> Discord app logic and routing
├── test
├── ├── test.js               -> Tests for app
├── wrangler.toml             -> Configuration for Cloudflare Workers
├── package.json
├── README.md
├── renovate.json             -> Configuration for repo automation
├── .eslintrc.json
├── .prettierignore
├── .prettierrc.json
└── .gitignore
```

#### Registering commands

Before testing the app, register the desired slash commands. For this app there is an `/awwww`
command and an `/invite` command. The name and description for these are kept separate in
`commands.js`:

```js
  name: 'awwww',
  description: 'Drop some cuteness on this channel.',
};

  name: 'invite',
  description: 'Get an invite link to add the bot to your server',
};
```

The code to register commands lives in `register.js`. Commands can be **registered globally**, making
them available for all servers with the app installed, or they can be **registered on a single
server**. This example focuses on global commands:

```js
import { AWW_COMMAND, INVITE_COMMAND } from './commands.js';
import fetch from 'node-fetch';

/**
 * This file is meant to be run from the command line, and is not used by the
 * application server.  It's allowed to use node.js primitives, and only needs
 * to be run once.
 */

const token = process.env.DISCORD_TOKEN;
const applicationId = process.env.DISCORD_APPLICATION_ID;

if (!token) {
  throw new Error('The DISCORD_TOKEN environment variable is required.');
}
if (!applicationId) {
  throw new Error(
    'The DISCORD_APPLICATION_ID environment variable is required.'
  );
}

/**
 * Register all commands globally.  This can take o(minutes), so wait until
 * you're sure these are the commands you want.
 */
async function registerGlobalCommands() {
  const url = `https://discord.com/api/v10/applications/${applicationId}/commands`;
  await registerCommands(url);
}

async function registerCommands(url) {
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bot ${token}`,
    },
    method: 'PUT',
    body: JSON.stringify([AWW_COMMAND, INVITE_COMMAND]),
  });

  if (response.ok) {
    console.log('Registered all commands');
  } else {
    console.error('Error registering commands');
    const text = await response.text();
    console.error(text);
  }
  return response;
}

await registerGlobalCommands();
```

#### Running the server

This command needs to be run locally, once before getting started:

```
$ DISCORD_TOKEN=**** DISCORD_APPLICATION_ID=**** node src/register.js
```

Then start the local development server:

```
$ npm run dev
```

#### Setting up ngrok

When a user types a slash command, Discord sends an HTTP request to a public endpoint. During local
development this can be a little challenging, so the guide uses
[a tool called `ngrok`](https://ngrok.com/) to create an HTTP tunnel.

```
$ npm run ngrok
```

*Figure: ngrok forwarding address*

This bounces requests off of an external endpoint, and forwards them to your machine. Copy the HTTPS
link provided by the tool. It should look something like `https://8098-24-22-245-250.ngrok.io`.

Now head back to the Discord Developer Dashboard, and update the `Interactions Endpoint URL` for your
app:

*Figure: Interactions Endpoint URL*

This is the process used for local testing and development. When you've published your app to
Cloudflare, you **will want to update this field to use your Cloudflare Worker URL**.

### Deployment

The repository is set up to automatically deploy to Cloudflare Workers when new changes land on the
`main` branch. To deploy manually, run `npm run publish`, which uses the `wrangler publish` command
under the hood.

Publishing via a GitHub Action requires obtaining an
[API Token and your Account ID from Cloudflare](https://developers.cloudflare.com/workers/cli-wrangler/authentication/).
These are stored
[as secrets in the GitHub repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets),
making them available to GitHub Actions.

The following configuration in `.github/workflows/ci.yaml` demonstrates how to tie it all together:

```yaml
release:
  if: github.ref == 'refs/heads/main'
  runs-on: ubuntu-latest
  needs: [test, lint]
  steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-node@v2
      with:
        node-version: 16
    - run: npm install
    - run: npm run publish
      env:
        CF_API_TOKEN: ${{ secrets.CF_API_TOKEN }}
        CF_ACCOUNT_ID: ${{ secrets.CF_ACCOUNT_ID }}
```

### Code deep dive

Most of the interesting code in this app lives in `src/server.js`. Cloudflare Workers require exposing
a `fetch` function, which is called as the entry point for each request. This code largely does two
things: **validate the request is valid and actually came from Discord**, and hand the request over to
a router.

```js
export default {
  /**
   * Every request to a worker will start in the `fetch` method.
   * Verify the signature with the request, and dispatch to the router.
   * @param {*} request A Fetch Request object
   * @param {*} env A map of key/value pairs with env vars and secrets from the cloudflare env.
   * @returns
   */
  async fetch(request, env) {
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

    // Dispatch the request to the appropriate route
    return router.handle(request, env);
  },
};
```

All of the API calls from Discord in this example are POSTed to `/`. From here, the
[`discord-interactions`](https://github.com/discord/discord-interactions-js) npm module helps
interpret the event and send results.

```js
/**
 * Main route for all requests sent from Discord.  All incoming messages will
 * include a JSON payload described here:
 * /developers/docs/interactions/receiving-and-responding#interaction-object
 */
router.post('/', async (request, env) => {
  const message = await request.json();
  console.log(message);
  if (message.type === InteractionType.PING) {
    // The `PING` message is used during the initial webhook handshake, and is
    // required to configure the webhook in the developer portal.
    console.log('Handling Ping request');
    return new JsonResponse({
      type: InteractionResponseType.PONG,
    });
  }

  if (message.type === InteractionType.APPLICATION_COMMAND) {
    // Most user commands will come as `APPLICATION_COMMAND`.
    switch (message.data.name.toLowerCase()) {
      case AWW_COMMAND.name.toLowerCase(): {
        console.log('handling cute request');
        const cuteUrl = await getCuteUrl();
        return new JsonResponse({
          type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
          data: {
            content: cuteUrl,
          },
        });
      }
      case INVITE_COMMAND.name.toLowerCase(): {
        const applicationId = env.DISCORD_APPLICATION_ID;
        const INVITE_URL = `https://discord.com/oauth2/authorize?client_id=${applicationId}&scope=applications.commands`;
        return new JsonResponse({
          type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
          data: {
            content: INVITE_URL,
            flags: InteractionResponseFlags.EPHEMERAL,
          },
        });
      }
      default:
        console.error('Unknown Command');
        return new JsonResponse({ error: 'Unknown Type' }, { status: 400 });
    }
  }

  console.error('Unknown Type');
  return new JsonResponse({ error: 'Unknown Type' }, { status: 400 });
});
```

### Next steps

With your app built and deployed, you can start customizing it to be your own:

- Use **message components** in your app to add more interactivity (like buttons and select menus).
- Take a look at different **[public APIs](https://github.com/public-apis/public-apis)** on GitHub.
- Join the **[Discord Developers server](https://discord.gg/discord-developers)** to ask questions
  about the API, attend events hosted by the Discord API team, and interact with other developers.

## Using community invites

> Automate role assignment and targeted invites using the Discord Community Invites API.

Community invites extend Discord's invite system with **two API-powered features**: the `role_ids`
parameter for automatic role assignment, and the `target_users_file` parameter for restricting which
users can accept an invite.

> **Info**
> If you're a server admin or community manager looking to create role invites without code, see the
> Community Invites guide (`/developers/communities/guides/community-invites`) for the Discord UI
> walkthrough.

By the end of this tutorial you'll know how to:

- Create invites that assign roles through the API
- Create targeted invites for specific groups of users through the API

### Understanding community invites features

#### Role assignment

When using the API, the **`role_ids`** parameter lets you specify one or more Discord roles that will
be automatically assigned when a player accepts the invite. No manual role management needed.

**Example use cases:**

- Giving roles to supporters
- Giving roles related to characters or achievements from your game
- Giving roles that have permissions to access channels

> **Info**
> Once a user accepts an invite and receives the roles, **those roles remain even after the invite
> expires or is deleted**. You'll need to remove roles manually (via a bot or Discord's interface).

#### Targeted invites

Setting which users are allowed to accept an invite **can only be done through the Discord API**. The
**`target_users_file`** parameter accepts a **CSV file containing Discord user IDs**. Only users in
that list can see and accept the invite.

**Example use cases:**

- Preventing invite sharing for exclusive achievements (for example, create a unique invite for a
  player with a 100% completion role)
- When combined with roles to give out mod/admin privileges
- Combined with roles to give special roles/channel access to paying supporters

These features work with **all standard invite parameters** like `max_age`, `max_uses`, and more.

### Role granting invite example

**Auto-assigning player roles.** This example grants roles as part of an invite using the channel
invite API (Create Channel Invite).

#### Prerequisites

- A Discord server for testing
- Developer Mode enabled on your account (so you can copy role, channel, and user IDs)
- A Discord app with a bot token (create one in the
  [Developer Portal](https://discord.com/developers/applications))
- Node.js installed, or the ability to make HTTP requests from your bot or app
- Bot permissions for:
  - **Create Instant Invite** (required to create invites)
  - **Manage Roles** (required for automatic role assignment with `role_ids`)

#### Coding the invite

When players join your Discord server from your game, you can give them a **Player** role for access
to game-specific channels. Here's how to create an invite that does this automatically:

```javascript
// IMPORTANT: Never hardcode tokens or commit them to version control
// Use environment variables or a secure configuration management system
// Replace the placeholder below with your actual bot token, channel ID, and role ID
const BOT_TOKEN = 'REPLACE_WITH_YOUR_BOT_TOKEN_FROM_THE_DEV_PORTAL';
const CHANNEL_ID = '1234567890123456789';
const ROLE_ID = '9876543210987654321';

const response = await fetch(
    `https://discord.com/api/v10/channels/${CHANNEL_ID}/invites`,
    {
        method: 'POST',
        headers: {
        'Authorization': `Bot ${BOT_TOKEN}`,
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({
        role_ids: [ROLE_ID]
        })
    }
);

if (!response.ok) {
const error = await response.json().catch(() => ({
    message: `HTTP ${response.status}`
}));
throw new Error(
    `Failed to create invite: ${error.message}${error.code ? ` (code: ${error.code})` : ''}`
);
}

const invite = await response.json();
console.log(`Created invite: https://discord.gg/${invite.code}`);
```

#### What's happening

1. **`role_ids` array**: Contains the Discord role IDs to assign when the invite is accepted (only
   one is assigned in this example, but you can assign any number of roles using this array)
2. **Response**: Returns an invite object with a `code` you can share

#### Testing it out

1. Create a **Player** role in your Discord server
2. Right click the role and click **"Copy Role ID"** then paste it in `ROLE_ID` in the script
3. Right click the channel for the invite and click **"Copy Channel ID"** then paste it in
   `CHANNEL_ID` in the script
4. Paste your bot token in `BOT_TOKEN` in the script
5. Run the code to generate an invite code
6. Share the `discord.gg/...` link with a test account
7. When they accept, they'll automatically get the **Player** role

*Figure: Example of an invite granting a Player role*

### Target users example

**Creating targeted supporter invites.** This example only allows specific users to accept an invite
using the channel invite API.

#### Prerequisites

- A Discord server for testing
- Developer Mode enabled on your account (so you can copy role, channel, and user IDs)
- A Discord app with a bot token (create one in the
  [Developer Portal](https://discord.com/developers/applications))
- Node.js installed, or the ability to make HTTP requests from your bot or app
- Bot permissions for:
  - **Create Instant Invite** (required to create invites)
  - **Manage Guild** (required for targeted invites with `target_users_file`)
  - **Manage Roles** (required for automatic role assignment with `role_ids`)

#### Coding the invite

If you run a subscription service for your game or community, you can create exclusive invites that
only your paying supporters can accept. Those roles can grant access to channels that other users in
the server can't see.

```javascript
// IMPORTANT: Never hardcode tokens or commit them to version control
// Use environment variables or a secure configuration management system
// Replace the placeholder below with your actual bot token, channel ID, and role ID
const BOT_TOKEN = "REPLACE_WITH_YOUR_BOT_TOKEN_FROM_THE_DEV_PORTAL";
const SUPPORTER_CHANNEL_ID = '1234567890123456789';
const SUPPORTER_ROLE_ID = '1111222233334444555';

// In production you would fetch this from your subscription database
// Replace these example user IDs with actual Discord user IDs of your test accounts
const activeSupporterIds = [
    '111111111111111111',
    '222222222222222222',
    '333333333333333333',
];

// Create CSV content with user IDs
const csvContent = activeSupporterIds.join('\n');
const csvBlob = new Blob([csvContent], { type: 'text/csv' });

// Use FormData for multipart/form-data request
const formData = new FormData();
formData.append('target_users_file', csvBlob, 'supporters.csv');

formData.append('payload_json', JSON.stringify({
    role_ids: [SUPPORTER_ROLE_ID]
}));

const response = await fetch(
`https://discord.com/api/v10/channels/${SUPPORTER_CHANNEL_ID}/invites`,
{
    method: 'POST',
    headers: {
    'Authorization': `Bot ${BOT_TOKEN}`
    },
    body: formData
}
);

if (!response.ok) {
    const error = await response.json().catch(() => ({
        message: `HTTP ${response.status}`
    }));

    let errorMessage = `Failed to create invite: ${error.message || response.statusText}`;

    if (error.code) {
        errorMessage += ` (code: ${error.code})`;
    }

    if (error.errors) {
        errorMessage += '\nDetailed errors:\n' + JSON.stringify(error.errors, null, 2);
    }

    throw new Error(errorMessage);
}

const invite = await response.json();

console.log(`Share this link with supporters: https://discord.gg/${invite.code}`);
```

#### What's happening

1. **`target_users_file`**: A CSV file containing Discord user IDs of paying supporters. Only these
   users can see and accept the invite.
2. **`role_ids` array**: Assigns the **Supporter** role automatically, giving them access to exclusive
   channels
3. **FormData**: Required when uploading files; the other parameters go in `payload_json`

> **Info**
> When using only JSON parameters like `role_ids`, use `Content-Type: application/json`. When
> uploading `target_users_file`, you **must** use `multipart/form-data`.

#### Setting up the supporter role

For the best experience, configure your **Supporter** role with these permissions:

1. Create a **Supporter** role in your Discord server
2. Create a private channel (#supporter-polls or #supporter-chat)
3. Right click the channels and **"Edit Channel"** to set the channel permissions so only users with
   the **Supporter** role can view and message in it
   - **View Channel** for the supporter exclusive channels
   - **Send Messages** and **Add Reactions**

#### Testing it out

1. Create a **Supporter** role in your Discord server
2. Right click the role and click **"Copy Role ID"** then paste it in `SUPPORTER_ROLE_ID` in the
   script
3. Right click the channel for the invite and click **"Copy Channel ID"** then paste it in
   `SUPPORTER_CHANNEL_ID` in the script
4. Paste your bot token in `BOT_TOKEN` in the script
5. Right click each user you want to be able to accept the invite and click **"Copy User ID"** then
   paste that in `activeSupporterIds` in the script
6. Run the code to generate an invite code
7. Share the `discord.gg/...` link with one of the users you added to `activeSupporterIds` and one
   that you didn't
8. The users in `activeSupporterIds` will be able to accept and receive the **Supporter** role

*Figure: Example of an invite granting a Supporter role*

*Figure: Example of an invite that can't be accepted*

### Resources

For complete API reference details, the upstream points at the invite and channel API documentation:
Invites (`/developers/resources/invite`) — complete API reference for invite objects, endpoints, and
parameters; and Create Channel Invite (`/developers/resources/channel#create-channel-invite`) —
detailed documentation for the create invite endpoint. Both are covered by the `discord-rest` skill.

## Source

[Developing A User-Installable App](https://docs.discord.com/developers/tutorials/developing-a-user-installable-app),
[Hosting a Reddit API Discord app on Cloudflare Workers](https://docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers),
[Using Community Invites](https://docs.discord.com/developers/tutorials/using-community-invites) —
all retrieved 2026-08-26. Rights holder: Discord Inc.
