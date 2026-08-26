# Getting Started with Discord Apps

The Discord Developer Platform entry point, what a Discord application is, the three app types, and
the complete step-by-step walkthrough for building your first bot.

Sources, all retrieved 2026-08-26:
[Discord Developer Platform](https://docs.discord.com/developers/intro),
[Overview of Discord Apps](https://docs.discord.com/developers/quick-start/overview-of-apps),
[Building your first Discord Bot](https://docs.discord.com/developers/quick-start/getting-started).

## Contents

- [The Discord Developer Platform landing page](#the-discord-developer-platform-landing-page)
- [Overview of Discord apps](#overview-of-discord-apps)
  - [The three types of Discord apps](#the-three-types-of-discord-apps)
  - [Where apps install](#where-apps-install)
  - [What APIs can apps use?](#what-apis-can-apps-use)
- [Building your first Discord bot](#building-your-first-discord-bot)
  - [Step 0: Project setup](#step-0-project-setup)
  - [Step 1: Creating an app](#step-1-creating-an-app)
  - [Step 2: Running your app](#step-2-running-your-app)
  - [Step 3: Handling interactivity](#step-3-handling-interactivity)
  - [Step 4: Adding message components](#step-4-adding-message-components)
  - [Next steps](#next-steps)

## The Discord Developer Platform landing page

> Build bots and integrations on Discord, or connect your game with rich presence, voice chat, and
> more.

*Figure: Discord Developer Platform (hero image)*

**What do you want to build?** — the three entry cards:

| Card | Destination | Description |
| --- | --- | --- |
| Bots & Apps | `/developers/platform/bots` | Build automated apps, commands, and integrations that run inside Discord servers. |
| Activities | `/developers/platform/activities` | Create multiplayer games and social experiences that launch directly inside Discord. |
| Social Layer for Games | `/developers/platform/social-layer` | Add rich presence, voice chat, and social features to your game across all platforms. |

**New to Discord development?**

| Card | Destination | Description |
| --- | --- | --- |
| Overview of Apps | `/developers/quick-start/overview-of-apps` | Understand what Discord apps are, the different types, and how to get started. |
| Build Your First App | `/developers/quick-start/getting-started` | Follow a step-by-step guide to build and run your first Discord bot. |

**Resources**

| Card | Link | Description |
| --- | --- | --- |
| Join the Developer Discord | https://discord.com/invite/discord-developers | Get support, API announcements, and participate in developer events. |
| Report Issues on GitHub | https://github.com/discord/discord-api-docs | Report issues with the Discord API and SDKs. |
| Visit the Developer Help Center | https://support-dev.discord.com/ | Find articles, FAQs, and reach out to Discord's developer support team. |

## Overview of Discord apps

> Build Discord apps to customize, extend, and enhance Discord for millions of users.

A **Discord application** is the core entity that represents your integration with the Discord
platform. Every bot, Activity, and Social SDK integration is backed by an application registered in
the [Discord Developer Portal](https://discord.com/developers/applications).

Applications hold your credentials, OAuth2 settings, bot configuration, and metadata. Whether you're
building a simple command-response bot or a full game integration with voice chat and rich presence,
it all starts with creating an application.

The page embeds the YouTube video "Discord Apps 101: Bots, Activities, and Social SDK
[Discord DevBytes]" (https://www.youtube.com/embed/CFxo5w3SY2w).

### The three types of Discord apps

#### Bots

Bots are **automated user accounts operated by application code**. They appear in servers with an
`APP` tag and can respond to events, slash commands, and user actions.

Use bots when you want to:

- Add commands, moderation tools, or utilities to a server
- React to events (messages, joins, reactions) in real time
- Build interactive experiences with buttons, menus, and modals
- Post automated updates from external systems

Bots can be **guild-installed** (added to a specific server) or **user-installed** (available
everywhere the user goes, without requiring server permissions).

#### Activities

Activities are **embedded web applications that run inside Discord channels**. They're built with
the Embedded App SDK and can be launched by any user in a channel or from a bot with the
`LAUNCH_ACTIVITY` interaction callback.

Use Activities when you want to:

- Build a game or interactive experience that runs inside Discord
- Create collaborative tools (watch parties, drawing apps, trivia games)
- Leverage Discord's existing social context: voice, friends, servers

#### Social Layer for Games

The Discord Social SDK lets you add Discord-powered social features to your game across PC, mobile,
and console. You can integrate individual features alongside your existing social systems or build
out a more complete Discord-powered experience.

Use the Social SDK when you want to:

- Add rich presence, friends lists, and voice chat to your game
- Support cross-platform social features with Discord account linking
- Let players interact through Discord without leaving your game

### Where apps install

| App Type              | Install Target | What It Unlocks                              |
| --------------------- | -------------- | -------------------------------------------- |
| Bot (guild-installed) | A server       | Access to server channels, members, events   |
| Bot (user-installed)  | A user         | Available in DMs, group DMs, and any server  |
| Activity              | An application | Launchable from any voice channel            |
| Social SDK            | Your game      | Social features embedded in your game client |

### What APIs can apps use?

There are a handful of different APIs that you can pick and choose from based on your app's
functionality and which Discord features you want to access.

#### HTTP API

The **HTTP API** is a REST API that lets you interact and modify core Discord resources like
channels, servers (or guilds), users, and messages.

Use the HTTP API to:

- Retrieve information about a resource
- Create, update, or delete a resource

#### Gateway API

The **Gateway API** is a WebSocket connection between your app and Discord. While it's most commonly
used to receive a real-time stream of events from Discord, **the connection is bidirectional**. Your
app can also send events to Discord over the same connection.

Use the Gateway API to:

- Receive real-time events from Discord (messages, member joins, reactions, voice state changes, and
  more)
- Update your bot's presence and status
- Manage voice state and connect to voice channels
- Perform the connection handshake and manage the lifecycle of your Gateway connection

**Start Building** cards: Bots & Companion Apps (`/developers/bots/overview`), Social Layer for
Games (`/developers/discord-social-sdk/overview`), Activities (`/developers/activities/overview`).

## Building your first Discord bot

> Step-by-step tutorial for building your first Discord app.

Discord apps let you customize and extend Discord using a collection of APIs and interactive
features. This guide walks through building your first Discord app using JavaScript; by the end you
have an app that uses slash commands, sends messages, and responds to component interactions.

> **Info**
> If you're interested in building a game or social experience in an iframe, follow the tutorial for
> building an Activity (`/developers/activities/building-an-activity`).

The app built is a Discord app that lets users play **rock-paper-scissors** (with 7 choices instead
of 3). The guide is beginner-focused, but it assumes a basic understanding of JavaScript.

**What we'll be building** — the finished user flow:

*Figure: Demo of example app*

1. User A initiates a new game and picks their object using the app's `/challenge` slash command
2. A message is sent to channel with a button inviting others to accept the challenge
3. User B presses the **Accept** button
4. User B is sent an ephemeral message where they select their object of choice
5. The result of the game is posted back into the original channel for all to see

**Resources used in this guide**

- **[GitHub repository](https://github.com/discord/discord-example-app)** where the code from this
  guide lives along with some additional feature-specific code examples.
- **[discord-interactions](https://github.com/discord/discord-interactions-js)**, a library that
  provides types and helper functions for Discord apps.
- **[Express](https://expressjs.com)**, a popular JavaScript web framework used to create a server
  where Discord can send requests.
- **[ngrok](https://ngrok.com/)**, a tool that lets you tunnel your local server to a public URL
  where Discord can send requests.

### Step 0: Project setup

Before getting started, set up your local environment and get the project code from the
[sample app repository](https://github.com/discord/discord-example-app).

> **Info**
> The guide develops the app locally with a little help from [ngrok](https://ngrok.com/), but you
> can use your preferred development environment.

If you don't have [NodeJS](https://nodejs.org/en/download/) installed, install that first.

After NodeJS is installed, open your command line and clone the project code:

```bash
git clone https://github.com/discord/discord-example-app.git
```

Then navigate to the directory and install the project's dependencies:

```bash
# navigate to directory
cd discord-example-app

# install dependencies
npm install
```

**Project structure** of the sample app:

```
├── examples    -> short, feature-specific sample apps
├──── app.js  -> finished app.js code
├──── button.js
├──── command.js
├──── modal.js
├──── selectMenu.js
├── .env        -> your credentials and IDs
├── app.js      -> main entrypoint for app
├── commands.js -> slash command payloads + helpers
├── game.js     -> logic specific to Rock, Paper, Scissors
├── utils.js    -> utility functions and constants
├── package.json
├── README.md
└── .gitignore
```

With that out of the way, open your new project in the code editor of your choice.

### Step 1: Creating an app

First, create an app in the developer portal if you don't have one already: **Create App** →
https://discord.com/developers/applications?new_application=true

Enter a name for your app, then press **Create**.

After you create your app, you land on the **General Information** page of the app's settings where
you can update basic information about your app like its description and icon. You will also see an
**Application ID** and **Interactions Endpoint URL**, used later in the guide.

#### Fetching your credentials

You need to set up and fetch a few sensitive values for your app, like its token and ID.

> **Warning**
> Your token is used to authorize API requests and carry your app's permissions, so they are
> *highly* sensitive. Make sure to never share your token or check it into any kind of version
> control.

Back in your project folder, rename the `.env.sample` file to `.env`. This is where all of your
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

> **Warning**
> You won't be able to view your token again unless you regenerate it, so make sure to keep it
> somewhere safe (like in a password manager).

#### Configuring your bot

Newly-created apps have a **bot user enabled by default**. Bot users allow your app to appear and
behave similarly to other server members when it's installed to a server.

On the left hand sidebar in your app's settings, there's a **Bot** page (where the token was
fetched). On this page, you can also configure settings like its privileged intents or whether it
can be installed by other users.

**What are intents?** Intents determine which events Discord will send your app when you're creating
a Gateway API connection. For example, if you want your app to perform an action when users add a
reaction to a message, you can pass the `GUILD_MESSAGE_REACTIONS` (`1 << 10`) intent.

Some intents are **privileged**, meaning they allow your app to access data that may be considered
sensitive (like the contents of messages). Privileged intents can be toggled on the **Bot** page in
your app's settings, but they must be approved before you
[verify your app](https://support-dev.discord.com/hc/en-us/articles/23926564536471-How-Do-I-Get-My-App-Verified).
Standard, non-privileged intents don't require any additional permissions or configurations. For the
full intent list, call the Skill tool with `"discord-gateway"`.

For this guide, nothing additional needs to be configured here, but you may need to in the future
depending on your app's use case.

#### Choosing installation contexts

Next, select where your app can be installed in Discord, which is determined by the **installation
contexts** that your app supports.

**What are installation contexts?** Installation contexts determine where your app can be installed:
to servers, to users, or both. Apps can choose which installation contexts they support within the
app's settings.

- Apps installed in a **server context** (server-installed apps) must be authorized by a server
  member with the `MANAGE_GUILD` permission, and are visible to all members of the server.
- Apps installed in a **user context** (user-installed apps) are visible only to the authorizing
  user, and therefore don't require any server-specific permissions. Apps installed to a user
  context are visible across all of the user's servers, DMs, and GDMs — however, **they're limited
  to using commands**.

Click on **Installation** (https://discord.com/developers/applications/select/installation) in the
left sidebar, then under **Installation Contexts** make sure both "User Install" and "Guild Install"
are selected.

> **Info**
> Some apps may only want to support one installation context — for example, a moderation app may
> only support a server context. However, by default, Discord recommends supporting both
> installation contexts. For detailed information about supporting user-installed apps, see
> `TUTORIALS.md` in this skill.

#### Setting up an install link

**Install links** provide an easy way for users to install your app in Discord. The guide sets up the
default **Discord Provided Link**.

On the **Installation** page, go to the **Install Link** section and select "Discord Provided Link"
if it's not already selected.

When Discord Provided Link is selected, a new **Default Install Settings** section appears.

#### Adding scopes and bot permissions

Apps need approval from installing users to perform actions in Discord (like creating a slash command
or fetching a list of server members). Add scopes and permissions before installing the app.

**What are scopes and permissions?** When creating an app, scopes and permissions determine what your
app can do and access in Discord.

- **OAuth2 Scopes** determine what data access and actions your app can take, granted on behalf of
  an installing or authenticating user.
- **Permissions** are the granular permissions for your bot user, the same as other users in Discord
  have. They can be approved by the installing user or later updated within server settings or with
  permission overwrites. Since apps installed to a user context can only respond to commands, these
  permissions are **only relevant to apps installed to a server**.

On the **Installation** page in the **Default Install Settings** section:

- For **User Install**, add the `applications.commands` scope
- For **Guild Install**, add the `applications.commands` scope **and** `bot` scope. When you select
  `bot`, a new **Permissions** menu appears to select the bot user's permissions. Select any
  permissions that you may want for your app — the guide selects just `Send Messages`.

*Figure: Default Install Settings*

For the full scope list, call the Skill tool with `"discord-oauth2"`; for permissions, with
`"discord-platform"`.

#### Installing your app

> **Info**
> When developing apps, you should build and test on your user account (for user-installable apps)
> and in a server that isn't actively used by others (for server-installable apps). If you don't
> have your own server already, you can
> [create one for free](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-).

Once you add scopes, copy the URL from the **Install Link** section from before.

Since the app supports both installation contexts, install the new app to both a test server and
your user account so that you can test in both installation contexts.

**Install to server** — To install your app to your test server, copy the default Install Link for
your app from the **Installation** page. Paste the link in your browser and hit enter, then select
"Add to server" in the installation prompt. Select your test server, and follow the installation
prompt. Once your app is added to your test server, you should see it appear in the member list.

**Install to user account** — Next, install your app to your user account. Paste the same Install
Link in your browser and hit enter. This time, select "Add to my apps" in the installation prompt.
Follow the installation prompt to install your app to your user account. Once it's installed you can
open a DM with it.

### Step 2: Running your app

With your app configured and installed to your test server and account, look at the code.

> **Info**
> To make development a bit simpler, the app uses
> [discord-interactions](https://github.com/discord/discord-interactions-js), which provides types
> and helper functions. If you prefer to use other languages or libraries, see
> `COMMUNITY-RESOURCES.md` in this skill.

#### Installing slash commands

> **Info**
> To install slash commands, the app is using
> [`node-fetch`](https://github.com/node-fetch/node-fetch). You can see the implementation for the
> installation in `utils.js` within the `DiscordRequest()` function.

The project contains a `register` script you can use to install the commands in `ALL_COMMANDS`, which
is defined at the bottom of `commands.js`. It installs the commands as **global commands** by calling
the HTTP API's `PUT /applications/<APP_ID>/commands` endpoint (Bulk Overwrite Global Application
Commands).

If you want to customize your commands or add additional ones, reference the command structure in the
commands documentation — call the Skill tool with `"discord-interactions"`.

In your terminal within the project folder, run the following command:

```
npm run register
```

If you navigate back to your server, you should see the slash commands appear. But if you try to run
them, nothing will happen since your app isn't receiving or handling any requests from Discord.

**What are Discord's APIs?** Apps have access to APIs that you can mix-and-match to build apps:

- **HTTP API** is a REST-like API for general operations like sending and updating data in Discord,
  or fetching data about a resource.
- **Gateway API** is a WebSocket-based API that is helpful for maintaining state or listening to
  events happening in a Discord server. This guide does not use it.

### Step 3: Handling interactivity

To enable your app to receive slash command and other interactions requests, Discord needs a public
URL to send them. This URL is configured in your app's settings as **Interaction Endpoint URL**.

#### Set up a public endpoint

To set up a public endpoint, start your app which runs an [Express](https://expressjs.com/) server,
then use [ngrok](https://ngrok.com/) to expose your server publicly.

First, go to your project's folder and run the following to start your app:

```
npm run start
```

There should be output indicating your app is running on port `3000`. Behind the scenes, the app is
ready to handle interactions from Discord, which includes **verifying security request headers and
responding to `PING` requests**.

> **Info**
> By default, the server will listen to requests sent to port 3000, but if you want to change the
> port, you can specify a `PORT` variable in your `.env` file.

Next, start the ngrok tunnel. If you don't have ngrok installed locally, install it by following the
instructions on the [ngrok download page](https://ngrok.com/download).

After ngrok is installed, open a new terminal and create a public endpoint that will forward requests
to your Express server:

```
ngrok http 3000
```

You should see your connection open with output similar to the following:

```
Tunnel Status                 online
Version                       2.0/2.0
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://1234-someurl.ngrok.io -> localhost:3000

Connections                  ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

The **Forwarding** URL is the publicly-accessible URL where Discord will send interactions requests.

#### Adding an interaction endpoint URL

Go to your app's settings (https://discord.com/developers/applications) and on the **General
Information** page under **Interaction Endpoint URL**, paste your new ngrok forwarding URL and
**append `/interactions`**.

*Figure: Interactions Endpoint URL*

Click **Save Changes** and ensure your endpoint is successfully verified.

> **Info**
> If you have troubles verifying your endpoint, make sure both ngrok and your app are running on the
> same port, and that you've copied the ngrok URL correctly.

The verification is handled automatically by the sample app in two ways:

- It uses the `PUBLIC_KEY` and
  [discord-interactions package](https://github.com/discord/discord-interactions-js#usage) with a
  wrapper function (imported from `utils.js`) that makes it conform to
  [Express's `verify` interface](http://expressjs.com/en/5x/api.html#express.json). This is run on
  **every** incoming request to your app.
- It responds to incoming `PING` requests.

#### Handling slash command requests

With the endpoint verified, navigate to your project's `app.js` file and find the code block that
handles the `/test` command:

```javascript
// "test" command
if (name === 'test') {
  // Send a message into the channel where command was triggered from
  return res.send({
    type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
    data: {
      flags: InteractionResponseFlags.IS_COMPONENTS_V2,
      components: [
        {
          type: MessageComponentTypes.TEXT_DISPLAY,
          // Fetches a random emoji to send from a helper function
          content: `hello world ${getRandomEmoji()}`
        }
      ]
    },
  });
}
```

The code above responds to the interaction with a message in the channel, DM, or Group DM it
originated from. For all available response types, like responding with a modal, call the Skill tool
with `"discord-interactions"`.

> **Info**
> `InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE` is a constant exported from
> `discord-interactions`
> (https://github.com/discord/discord-interactions-js/blob/main/src/index.ts#L33).

Go to your server and make sure your app's `/test` slash command works. When you trigger it, your app
should send a message that contains "hello world" followed by a random emoji.

### Step 4: Adding message components

The `/challenge` command is how the rock-paper-scissors-style game is initiated. When the command is
triggered, the app sends message components to the channel, which guide the users to complete the
game.

#### Adding a command with options

The `/challenge` command, called `CHALLENGE_COMMAND` in `commands.js`, has an array of `options`. In
the app, the options are objects representing different things that a user can select while playing
rock-paper-scissors, generated using keys of `RPSChoices` in `game.js`.

For command options and their structure, call the Skill tool with `"discord-interactions"`.

#### Handling the command interaction

To handle the `/challenge` command, add the following code after the `if name === "test"` if block:

```javascript
// "challenge" command
if (name === 'challenge' && id) {
  // Interaction context
  const context = req.body.context;
  // User ID is in user field for (G)DMs, and member for servers
  const userId = context === 0 ? req.body.member.user.id : req.body.user.id;
  // User's object choice
  const objectName = req.body.data.options[0].value;

  // Create active game using message ID as the game ID
  activeGames[id] = {
    id: userId,
    objectName,
  };

  return res.send({
    type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
    data: {
      flags: InteractionResponseFlags.IS_COMPONENTS_V2,
      components: [
        {
          type: MessageComponentTypes.TEXT_DISPLAY,
          // Fetches a random emoji to send from a helper function
          content: `Rock papers scissors challenge from <@${userId}>`,
        },
        {
          type: MessageComponentTypes.ACTION_ROW,
          components: [
            {
              type: MessageComponentTypes.BUTTON,
              // Append the game ID to use later on
              custom_id: `accept_button_${req.body.id}`,
              label: 'Accept',
              style: ButtonStyleTypes.PRIMARY,
            },
          ],
        },
      ],
    },
  });
}
```

> **Info**
> If you aren't sure where to paste the code, you can see the full code in `examples/app.js`.

The above code does a few things:

1. Parses the request body to get the ID of the user who triggered the slash command (`userId`), and
   the option (object choice) they selected (`objectName`). If the interaction is run in a server
   (`context === 0`), the user ID is nested in the `member` object. If it's in a DM or Group DM, it
   is in the `user` object.
2. Adds a new game to the `activeGames` object using the interaction ID. The active game records the
   `userId` and `objectName`.
3. Sends a message back to the channel with a button with a `custom_id` of
   `accept_button_<SOME_ID>`.

> **Warning**
> The sample code uses an object as in-memory storage, but for production apps you should use a
> database.

When sending a message with message components, the individual payloads are appended to a
`components` array. **Actionable components (like buttons) need to be inside of an action row**, as
in the code sample.

Note the unique `custom_id` sent with message components, in this case `accept_button_` with the
active game's ID appended to it. A `custom_id` can be used to handle requests that Discord sends you
when someone interacts with the component.

Now when you run the `/challenge` command and pick an option, your app sends a message with an
**Accept** button.

#### Handling button interactions

When users interact with a message component, Discord sends a request with an **interaction type of
`3`** (or the `MESSAGE_COMPONENT` value when using `discord-interactions`).

To set up a handler for the button, check the `type` of interaction, followed by matching the
`custom_id`. Paste the following code under the type handler for `APPLICATION_COMMAND`s:

```javascript
if (type === InteractionType.MESSAGE_COMPONENT) {
  // custom_id set in payload when sending message component
  const componentId = data.custom_id;

  if (componentId.startsWith('accept_button_')) {
    // get the associated game ID
    const gameId = componentId.replace('accept_button_', '');
    // Delete message with token in request body
    const endpoint = `webhooks/${process.env.APP_ID}/${req.body.token}/messages/${req.body.message.id}`;
    try {
      await res.send({
        type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data: {
          // Indicates it'll be an ephemeral message
          flags: InteractionResponseFlags.EPHEMERAL | InteractionResponseFlags.IS_COMPONENTS_V2,
          components: [
            {
              type: MessageComponentTypes.TEXT_DISPLAY,
              content: 'What is your object of choice?',
            },
            {
              type: MessageComponentTypes.ACTION_ROW,
              components: [
                {
                  type: MessageComponentTypes.STRING_SELECT,
                  // Append game ID
                  custom_id: `select_choice_${gameId}`,
                  options: getShuffledOptions(),
                },
              ],
            },
          ],
        },
      });
      // Delete previous message
      await DiscordRequest(endpoint, { method: 'DELETE' });
    } catch (err) {
      console.error('Error sending message:', err);
    }
  }
  return;
}
```

The above code:

1. Checks for a `custom_id` that matches what was originally sent (in this case, it starts with
   `accept_button_`). The custom ID also has the active game ID appended, so that is stored in
   `gameID`.
2. **Deletes the original message** by calling a webhook using `node-fetch` and passing the unique
   interaction `token` in the request body. This is done to clean up the channel, and so other users
   can't click the button.
3. Responds to the request by sending a message that contains a select menu with the object choices
   for the game. The payload looks fairly similar to the previous one, with the exception of the
   `options` array and `flags: 64`, which indicates that the message is ephemeral.

The `options` array is populated using the `getShuffledOptions()` method in `game.js`, which
manipulates the `RPSChoices` values to conform to the shape of string select options.

#### Handling select menu interactions

The last thing to add is code to handle select menu interactions, and to send the result of the game
to the channel. Since select menus are just another message component, the code to handle their
interactions is almost identical to buttons.

Modify the code above to handle the select menu:

```javascript
if (type === InteractionType.MESSAGE_COMPONENT) {
  // custom_id set in payload when sending message component
  const componentId = data.custom_id;

  if (componentId.startsWith('accept_button_')) {
    // get the associated game ID
    const gameId = componentId.replace('accept_button_', '');
    // Delete message with token in request body
    const endpoint = `webhooks/${process.env.APP_ID}/${req.body.token}/messages/${req.body.message.id}`;
    try {
      await res.send({
        type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data: {
          // Indicates it'll be an ephemeral message
          flags: InteractionResponseFlags.EPHEMERAL | InteractionResponseFlags.IS_COMPONENTS_V2,
          components: [
            {
              type: MessageComponentTypes.TEXT_DISPLAY,
              content: 'What is your object of choice?',
            },
            {
              type: MessageComponentTypes.ACTION_ROW,
              components: [
                {
                  type: MessageComponentTypes.STRING_SELECT,
                  // Append game ID
                  custom_id: `select_choice_${gameId}`,
                  options: getShuffledOptions(),
                },
              ],
            },
          ],
        },
      });
      // Delete previous message
      await DiscordRequest(endpoint, { method: 'DELETE' });
    } catch (err) {
      console.error('Error sending message:', err);
    }
  } else if (componentId.startsWith('select_choice_')) {
    // get the associated game ID
    const gameId = componentId.replace('select_choice_', '');

    if (activeGames[gameId]) {
      // Interaction context
      const context = req.body.context;
      // Get user ID and object choice for responding user
      // User ID is in user field for (G)DMs, and member for servers
      const userId = context === 0 ? req.body.member.user.id : req.body.user.id;
      const objectName = data.values[0];
      // Calculate result from helper function
      const resultStr = getResult(activeGames[gameId], {
        id: userId,
        objectName,
      });

      // Remove game from storage
      delete activeGames[gameId];
      // Update message with token in request body
      const endpoint = `webhooks/${process.env.APP_ID}/${req.body.token}/messages/${req.body.message.id}`;

      try {
        // Send results
        await res.send({
          type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
          data: {
            flags: InteractionResponseFlags.IS_COMPONENTS_V2,
            components: [
              {
                type: MessageComponentTypes.TEXT_DISPLAY,
                content: resultStr
              }
            ]
            },
        });
        // Update ephemeral message
        await DiscordRequest(endpoint, {
          method: 'PATCH',
          body: {
            components: [
              {
                type: MessageComponentTypes.TEXT_DISPLAY,
                content: 'Nice choice ' + getRandomEmoji()
              }
            ],
          },
        });
      } catch (err) {
        console.error('Error sending message:', err);
      }
    }
  }

  return;
}
```

Similar to earlier code, the code above gets the user ID and their object selection from the
interaction request. That information, along with the original user's ID and selection from the
`activeGames` object, are passed to the `getResult()` function. `getResult()` determines the winner,
then builds a readable string to send back to the channel.

Another webhook is called, this time to **update the follow-up ephemeral message** since it can't be
deleted. Finally, the results are sent in the channel using the `CHANNEL_MESSAGE_WITH_SOURCE`
interaction response type.

### Next steps

The upstream closes with four cards:

| Card | Destination | Description |
| --- | --- | --- |
| Overview of Apps | `/developers/quick-start/overview-of-apps` | Explore the platform features and APIs you have access to when building an app on Discord |
| Explore developer tools | `/developers/developer-tools/community-resources` | Explore 1st party and community-built libraries and tools to speed up and simplify your development |
| Developing User-Installable Apps | `/developers/tutorials/developing-a-user-installable-app` | Tutorial on building and handling interactions for apps installed to a user |
| Discord Developers | https://discord.gg/discord-developers | Join the community to ask questions about the API, attend events hosted by the Discord platform team, and interact with other devs |

## Source

[Discord Developer Platform](https://docs.discord.com/developers/intro),
[Overview of Discord Apps](https://docs.discord.com/developers/quick-start/overview-of-apps),
[Building your first Discord Bot](https://docs.discord.com/developers/quick-start/getting-started) —
all retrieved 2026-08-26. Rights holder: Discord Inc.
