# Building Your First Activity in Discord

The end-to-end tutorial: eight steps from enabling Developer Mode to fetching guild data through the
API, with every command and file body as upstream states them.

Source: `https://docs.discord.com/developers/activities/building-an-activity`, retrieved 2026-08-26.

## Contents

- [Introduction and resources](#introduction-and-resources)
- [Step 0: Enable Developer Mode](#step-0-enable-developer-mode)
- [Step 1: Setting up the project](#step-1-setting-up-the-project)
- [Step 2: Creating an app](#step-2-creating-an-app)
- [Step 3: Setting Up the Embedded App SDK](#step-3-setting-up-the-embedded-app-sdk)
- [Step 4: Running your app in Discord](#step-4-running-your-app-in-discord)
- [Step 5: Authorizing and authenticating users](#step-5-authorizing-and-authenticating-users)
- [Step 6: Use the SDK to fetch the channel](#step-6-use-the-sdk-to-fetch-the-channel)
- [Step 7: Use the API to fetch the guild](#step-7-use-the-api-to-fetch-the-guild)
- [Next steps](#next-steps)

## Introduction and resources

Activities are web-based games and apps that can be run within Discord. Activities are embedded in
iframes within the Discord client, and can be launched from the App Launcher or when responding to
interactions.

In this guide, you build a Discord app with a basic Activity that handles user authentication and
fetches data using the API.

It assumes an understanding of JavaScript and async functions, and a basic understanding of frontend
frameworks like React and Vue. Upstream names The Odin Project, Codecademy and Khan Academy as free
learning resources for those still learning to program.

**Resources used in this guide:**

- **`discord/getting-started-activity`** (`https://github.com/discord/getting-started-activity`), a
  project template to get you started
- **`@discord/embedded-app-sdk`** (`https://github.com/discord/embedded-app-sdk`), the SDK used to
  communicate between your app and Discord when building Activities
- **Node.js** (`https://nodejs.org`), latest version
- **Express** (`https://expressjs.com`), a popular JavaScript web framework used to create a server
  to handle authentication and serve the app
- **Vite** (`https://vite.dev/`), a build tool for modern JavaScript projects that will make your
  application easier to serve
- **cloudflared** (`https://github.com/cloudflare/cloudflared`), for bridging your local development
  server to the internet

(Screenshot: "Building Your First Activity Tutorial" — the finished Activity showing a rocket logo,
the channel name and the server avatar.)

## Step 0: Enable Developer Mode

Before getting started, you need to enable Developer Mode for your Discord account if you don't
already have it enabled. Developer Mode will allow you to run in-development Activities and expose
resource IDs (like users, channels, and servers) in the client which can simplify testing. To enable
Developer Mode:

1. Go to your **User Settings** in your Discord client. On Desktop, you can access **User Settings**
   by clicking on the cogwheel icon near the bottom-left, next to your username.
2. Click on **Advanced** tab from the left-hand sidebar and toggle on `Developer Mode`.

## Step 1: Setting up the project

Open a terminal window and clone the project code:

```
git clone git@github.com:discord/getting-started-activity.git
```

The sample project is broken into two parts:

- `client` is the sample Activity's frontend, built with vanilla JavaScript and integrated with Vite
  to help with local development.
- `server` is a backend using vanilla JavaScript, Node.js, and Express. However, as you're building
  your own Activity, you can use whichever backend you prefer.

**Project structure:**

```
├── client
├────── main.js       -> your Activity frontend
├────── index.html
├────── package.json
├────── rocket.png
├────── vite.config.js
├── server
├────── package.json
├────── server.js     -> your Activity backend
└── .env              -> your credentials, IDs and secrets
```

### Install project dependencies

Navigate to your project folder's `client` directory, which is where all the sample Activity's
frontend code lives:

```
cd getting-started-activity/client
```

Then install the project's dependencies and start up the frontend for the sample Activity:

```
# install project dependencies
npm install

# start frontend
npm run dev
```

If you visit `http://localhost:5173/` you should see a vanilla JS frontend template running with Vite.

**Step 1 Checkpoint.** By the end of Step 1, you should have:

- An understanding of what Discord Activities are
- Developer Mode enabled on your Discord account
- Cloned the sample project to your development environment
- Installed the front-end dependencies (in the `client` folder)

## Step 2: Creating an app

Create a new app in the developer portal if you don't have one already, at
`https://discord.com/developers/applications?new_application=true`. Enter a name for your app, select
a development team, then press **Create**.

**Development Team Access.** Launching a non-distributed Activity is limited to you or members of the
developer team, so if you're collaborating with others during development, create a developer team
(`https://discord.com/developers/teams`) and set it to the owner when you create the app.

After you create your app, you'll land on the **General Information** page of the app's settings,
where you can update basic information about your app like its description and icon.

### Choose installation contexts

Apps in Discord can be installed to different **installation contexts**: servers, user accounts, or
both.

The recommended *and* default behavior for apps is supporting both installation contexts, which lets
the installer choose the context during the installation flow. However, you can change the default
behavior by changing the supported installation contexts in your app's settings.

**Why installation contexts matter.** Installation contexts determine where your app can be
installed. The installation context affects things like who can manage the installation, where the
app's commands can appear, and the data returned in response to interactions.

- Apps installed in a **server context** (server-installed apps) must be authorized by a server
  member with the `MANAGE_GUILD` permission, and are visible to all members of the server.
- Apps installed in a **user context** (user-installed apps) are visible only to the authorizing
  user, and therefore don't require any server-specific permissions. Apps installed to a user context
  are visible across all of the user's servers, DMs, and GDMs — however, they're limited to using
  commands.

Click on **Installation** in the left sidebar
(`https://discord.com/developers/applications/select/installation`), then under **Installation
Contexts** make sure both "User Install" and "Guild Install" are selected. This will make sure users
can launch our app's Activity across Discord servers, DMs, and Group DMs.

### Add a Redirect URI

Next, add a Redirect URI, which is where a user is typically redirected to after authorizing with your
app when going through the standard OAuth flow. While setting up a Redirect URI is required, the
Embedded App SDK automatically handles redirecting users back to your Activity when the RPC `authorize`
command is called.

Since we're only authorizing in an Activity, use a placeholder value (`https://127.0.0.1`) and let the
Embedded App SDK handle the rest.

Click on **OAuth2** in your app's settings
(`https://discord.com/developers/applications/select/oauth2`). Under **Redirects**, enter
`https://127.0.0.1` as a placeholder value then click **Save Changes**.

(Screenshot: "Redirect URI in Activity Settings".)

### Fetch your OAuth2 credentials

To use information related to a user (like their username) or a server (like the server's avatar),
your app must be granted specific OAuth **scopes**.

For this sample app you request three scopes: `identify` to access basic information about a user,
`guilds` to access basic information about the servers a user is in, and `applications.commands` to
install commands.

In the root of your project, there is an `example.env` file. From the root of your project, run:

```
cp example.env .env
```

**Secure your secrets.** Your `DISCORD_CLIENT_SECRET` and `DISCORD_BOT_TOKEN` are *highly* sensitive
secrets. Never share either secret or check them into any kind of version control.

Back in your app's settings, click on **OAuth2**:

1. **Client ID**: Copy the value for Client ID and add it to your `.env` file as **`VITE_CLIENT_ID`**.
   This is the public ID that Discord associates with your app, and is almost always the same as your
   App ID.
2. **Client Secret**: Copy the value for Client Secret and add it to your `.env` as
   **`DISCORD_CLIENT_SECRET`**. This is a private, sensitive identifier that your app will use to
   grant an OAuth2 `access_token`, and should never be shared or checked into version control.

**Why the `VITE_` prefix before the Client ID?** Prefixing the `CLIENT_ID` environment variable with
`VITE_` makes it accessible to client-side code. This security measure ensures that only the variables
you intend to be accessible in the browser are available, and all other environment variables remain
private (see `https://vitejs.dev/guide/env-and-mode`).

Note the naming inconsistency upstream: this step says to store the Client ID as `VITE_CLIENT_ID`,
while every code sample later reads `import.meta.env.VITE_DISCORD_CLIENT_ID`.

**Step 2 Checkpoint.** By the end of Step 2, make sure you have:

- Set up a placeholder Redirect URI
- Added your app's Client ID and Client Secret to your project's `.env` file

## Step 3: Setting Up the Embedded App SDK

The Embedded App SDK is a first-party SDK that handles the communication between Discord and your
Activity with commands to interact with the Discord client (like fetching information about the
channel) and events to listen for user actions and changes in state (like when a user starts or stops
speaking).

The events and commands available in the Embedded App SDK are a subset of the RPC API ones, so
referencing the RPC documentation can be helpful to understand what's happening under the hood when
developing Activities.

### Install the SDK

Back in the project's `client` directory (`getting-started-activity/client`), install the Embedded App
SDK via NPM:

```
npm install @discord/embedded-app-sdk
```

This will add `@discord/embedded-app-sdk` to `getting-started-activity/client/package.json` and
install the SDK in your `node_modules` folder.

### Import the SDK in your project

Once installed, import it into your client code and instantiate it to start the handshake between your
app and the Discord client. To instantiate the SDK, use the environment variables set up in Step 2.

Also set up a check for the `ready` event with an async/await function which allows you to output a log
or perform other actions once the handshake was successful.

In `getting-started-activity/client/main.js`, import and instantiate the SDK:

```js
// Import the SDK
import { DiscordSDK } from "@discord/embedded-app-sdk";

import "./style.css";
import rocketLogo from '/rocket.png';

// Instantiate the SDK
const discordSdk = new DiscordSDK(import.meta.env.VITE_DISCORD_CLIENT_ID);

setupDiscordSdk().then(() => {
  console.log("Discord SDK is ready");
});

async function setupDiscordSdk() {
  await discordSdk.ready();
}

document.querySelector('#app').innerHTML = `
  <div>
    <img src="${rocketLogo}" class="logo" alt="Discord" />
    <h1>Hello, World!</h1>
  </div>
`;
```

**Time to leave your browser behind.** Once you add the SDK to your app, you will *not* be able to
view your app inside your web browser. In the next step, you run your Activity inside of Discord.

**Step 3 Checkpoint.** By the end of Step 3, make sure you have:

- Installed the Embedded App SDK to your project
- Imported the SDK in your project's `client/main.js` file

## Step 4: Running your app in Discord

### Run your app

Open a terminal window, navigate to your project directory's `client` folder, then start the
client-side app:

```
cd client
npm run dev
```

Your app should start and you should see output similar to the following:

```
VITE v5.0.12  ready in 100 ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
➜  press h + enter to show help
```

Use the Local URL as the publicly-accessible URL in the next step.

### Set up a public endpoint

Next, set up the public endpoint that serves the Activity's frontend by creating a tunnel with a
reverse proxy. The guide uses `cloudflared`; ngrok or another reverse proxy solution also works.

While your app is still running, open another terminal window and start a network tunnel that listens
to the port from the last step (in this case, port `5173`):

```
cloudflared tunnel --url http://localhost:5173
```

When you run `cloudflared`, the tunnel will generate a public URL and you'll see output similar to:

```
Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):
https://funky-jogging-bunny.trycloudflare.com
```

Copy the URL from the output; it goes into the app's settings next.

### Set up your Activity URL Mapping

Because Activities are in a sandbox environment and go through the Discord proxy, you'll need to add a
public URL mapping to serve your application and make external requests in your Activity. Since we're
developing locally, use the public endpoint just set up.

Back in your app's settings, click on the **URL Mappings** page
(`https://discord.com/developers/applications/select/embedded/url-mappings`) under **Activities** on
the left-hand sidebar. Enter the URL you generated from `cloudflared`.

(Screenshot: "Configuring your URL Mapping".)

| PREFIX | TARGET |
| ------ | --------------------------------------- |
| `/` | `funky-jogging-bunny.trycloudflare.com` |

Full URL-mapping rules are in `DEVELOPMENT-GUIDES.md` under Local Development.

### Enable Activities

On the left-hand sidebar under **Activities**, click **Settings**
(`https://discord.com/developers/applications/select/embedded/settings`). Find the first checkbox,
labeled `Enable Activities`. Turn it on.

(Screenshot: "Enabling Activities in Settings".)

#### Default Entry Point Command

When you enable Activities for your app, a default Entry Point command called "Launch" is
automatically created. This Entry Point command is the primary way for users to launch your Activity
in Discord.

By default, interactions with this command will result in Discord opening your Activity for the user
and posting a message in the channel where it was launched from. However, if you prefer to handle the
interactions in your app, you can update the `handler` field or create your own. See
`DEVELOPMENT-GUIDES.md` under User Actions for the handler types and the create/edit payloads.

### Running your Activity in Discord

Navigate to your Discord test server and, in any voice and or text channel, open the App Launcher
where your in-development Activity should be present. If you don't see your Activity, try searching
for its name. Clicking on your app will launch your locally running app from inside Discord.

(Screenshot: "Running your activity".)

**Customizing your Activity.** To set images for your Activity, see `DEVELOPMENT-GUIDES.md` under
Assets and Metadata.

**Step 4 Checkpoint.** By the end of Step 4, make sure you have:

- Set up a public endpoint
- Added an Activity URL Mapping in your app's settings
- Enabled Activities for your app
- Successfully launched your Activity in Discord

## Step 5: Authorizing and authenticating users

To authenticate your Activity with the users playing it, finish implementing the server-side app and
get it talking to the client-side app. The example uses `express`, but any backend language or
framework will work.

**OAuth2 Flow Diagram.** (Diagram: the common pattern for granting a user an OAuth2 `access_token` —
the client calls `authorize`, receives a `code`, posts it to the app server, the server exchanges it
with Discord for an `access_token`, and the client then calls `authenticate` with that token.)
Further example implementations:

- Back-end code:
  `https://github.com/discord/embedded-app-sdk-examples/blob/main/discord-activity-starter/packages/server/src/app.ts`
- Front-end code:
  `https://github.com/discord/embedded-app-sdk-examples/blob/main/discord-activity-starter/packages/client/src/main.ts`

```
# move into our server directory
cd server

# install dependencies
npm install
```

The server code is not edited in this guide; it consists of a single POST route for `/api/token` that
performs the OAuth2 flow from the server securely. In the
`getting-started-activity/server/server.js` file, the following code should already be present:

```javascript
import express from "express";
import dotenv from "dotenv";
import fetch from "node-fetch";
dotenv.config({ path: "../.env" });

const app = express();
const port = 3001;

// Allow express to parse JSON bodies
app.use(express.json());

app.post("/api/token", async (req, res) => {

  // Exchange the code for an access_token
  const response = await fetch(`https://discord.com/api/oauth2/token`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      client_id: process.env.VITE_DISCORD_CLIENT_ID,
      client_secret: process.env.DISCORD_CLIENT_SECRET,
      grant_type: "authorization_code",
      code: req.body.code,
    }),
  });

  // Retrieve the access_token from the response
  const { access_token } = await response.json();

  // Return the access_token to our client as { access_token: "..."}
  res.send({access_token});
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
```

Now start the project's backend server:

```
npm run dev
```

You should see output similar to the following:

```
> server@1.0.0 dev
> node server.js

Server listening at http://localhost:3001
```

You can now run the server and client-side apps in separate terminal windows.

### Calling external resources from your activity

Before calling your backend activity server, be aware of the Discord proxy and how to avoid any
Content Security Policy (CSP) issues. See `DEVELOPMENT-GUIDES.md` under Networking for "Construct a
Full URL" and "Using External Resources".

### Calling your backend server from your client

**What is `vite.config.js`?** To allow the frontend app to call the Express server, Vite requires a
proxy for `/api/*` to the backend server, which is running on port 3001.

Copy the following code into `getting-started-activity/client/main.js`:

```javascript
import { DiscordSDK } from "@discord/embedded-app-sdk";

import rocketLogo from '/rocket.png';
import "./style.css";

// Will eventually store the authenticated user's access_token
let auth;

const discordSdk = new DiscordSDK(import.meta.env.VITE_DISCORD_CLIENT_ID);

setupDiscordSdk().then(() => {
  console.log("Discord SDK is authenticated");

  // We can now make API calls within the scopes we requested in setupDiscordSDK()
  // Note: the access_token returned is a sensitive secret and should be treated as such
});

async function setupDiscordSdk() {
  await discordSdk.ready();
  console.log("Discord SDK is ready");

  // Authorize with Discord Client
  const { code } = await discordSdk.commands.authorize({
    client_id: import.meta.env.VITE_DISCORD_CLIENT_ID,
    response_type: "code",
    state: "",
    prompt: "none",
    scope: [
      "identify",
      "guilds",
      "applications.commands"
    ],
  });

  // Retrieve an access_token from your activity's server
  const response = await fetch("/api/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      code,
    }),
  });
  const { access_token } = await response.json();

  // Authenticate with Discord client (using the access_token)
  auth = await discordSdk.commands.authenticate({
    access_token,
  });

  if (auth == null) {
    throw new Error("Authenticate command failed");
  }
}

document.querySelector('#app').innerHTML = `
  <div>
    <img src="${rocketLogo}" class="logo" alt="Discord" />
    <h1>Hello, World!</h1>
  </div>
`;
```

Now if you relaunch the app, you'll be prompted to authorize with Discord using the `identify`,
`guilds`, and `applications.commands` scopes.

(Screenshot: "Prompt to authorize Activity".)

**Safe storage of tokens.** Access tokens and refresh tokens are powerful, and should be treated
similarly to passwords or other highly-sensitive data. Store both types of tokens securely and in an
encrypted manner.

**Step 5 Checkpoint.** By the end of Step 5, make sure you have:

- Updated your `client/main.js` to call the backend to support user authorization and authentication
- Been able to successfully complete the authorization flow for your app when opening your Activity

## Step 6: Use the SDK to fetch the channel

Use the SDK to get details about the channel that your activity is running in, with the
`commands.getChannel` SDK method. In the same `getting-started-activity/client/main.js` file, paste
the following function:

```javascript
async function appendVoiceChannelName() {
  const app = document.querySelector('#app');

  let activityChannelName = 'Unknown';

  // Requesting the channel in GDMs (when the guild ID is null) requires
  // the dm_channels.read scope which requires Discord approval.
  if (discordSdk.channelId != null && discordSdk.guildId != null) {
    // Over RPC collect info about the channel
    const channel = await discordSdk.commands.getChannel({channel_id: discordSdk.channelId});
    if (channel.name != null) {
      activityChannelName = channel.name;
    }
  }

  // Update the UI with the name of the current voice channel
  const textTagString = `Activity Channel: "${activityChannelName}"`;
  const textTag = document.createElement('p');
  textTag.textContent = textTagString;
  app.appendChild(textTag);
}
```

Now, update the callback after `setupDiscordSdk()` to call the function you just added:

```javascript
setupDiscordSdk().then(() => {
  console.log("Discord SDK is authenticated");

  appendVoiceChannelName();
});
```

If you close and rejoin the Activity, you should now see the name of the current channel.

(Screenshot: "Discord Activities" — the Activity showing the channel name.)

**Step 6 Checkpoint.** By the end of Step 6, make sure you have:

- Updated your `client/main.js` code to fetch the channel name using the SDK
- Added a call to the new function in the callback for `setupDiscordSdk()`

## Step 7: Use the API to fetch the guild

Since you requested the `identify` and `guilds` scopes, you can also use the authorized `access_token`
received earlier to fetch those resources via the API. In the following code block, you will:

1. Call the `GET /users/@me/guilds` endpoint with `auth.access_token` to get a list of the guilds the
   authorizing user is in
2. Iterate over each guild to find the guild we are in based on the `guildId` defined in `discordSdk`
3. Create a new HTML image element with the guild avatar and append it to the frontend

The example uses a pure `fetch` request to make the API call, but a community-built library also works.

In the same `client/main.js` file, add the following function:

```javascript
async function appendGuildAvatar() {
  const app = document.querySelector('#app');

  // 1. From the HTTP API fetch a list of all of the user's guilds
  const guilds = await fetch(`https://discord.com/api/v10/users/@me/guilds`, {
    headers: {
      // NOTE: we're using the access_token provided by the "authenticate" command
      Authorization: `Bearer ${auth.access_token}`,
      'Content-Type': 'application/json',
    },
  }).then((response) => response.json());

  // 2. Find the current guild's info, including it's "icon"
  const currentGuild = guilds.find((g) => g.id === discordSdk.guildId);

  // 3. Append to the UI an img tag with the related information
  if (currentGuild != null) {
    const guildImg = document.createElement('img');
    guildImg.setAttribute(
      'src',
      // More info on image formatting here: https://docs.discord.com/developers/reference#image-formatting
      `https://cdn.discordapp.com/icons/${currentGuild.id}/${currentGuild.icon}.webp?size=128`
    );
    guildImg.setAttribute('width', '128px');
    guildImg.setAttribute('height', '128px');
    guildImg.setAttribute('style', 'border-radius: 50%;');
    app.appendChild(guildImg);
  }
}
```

Then, call the new function in the callback for `setupDiscordSdk`:

```javascript
setupDiscordSdk().then(() => {
  console.log("Discord SDK is authenticated");

  appendVoiceChannelName();
  appendGuildAvatar();
});
```

If you relaunch the Activity, you will see the current server's avatar render in the Activity.

(Screenshot: "Discord Activities" — the finished Activity.)

**Step 7 Checkpoint.** At this point, you should have your Activity up and running. For Step 7, you
should have:

- Updated your `client/main.js` code to fetch the guild information using the
  `GET /users/@me/guilds` API endpoint
- Added a call to the new function in the callback for `setupDiscordSdk()`

## Next steps

This is an intentionally simple example to get you started with the communication between your
Activity and Discord using the Embedded App SDK and APIs. Upstream points at three next steps:

- **Development Guides** — suggested development practices and considerations. (Note: upstream's card
  links to `/developers/developer-tools/community-resources`, which appears to be a mistaken link;
  the guides live at `/developers/activities/development-guides`. They are distilled in
  `DEVELOPMENT-GUIDES.md`.)
- **Sample Activity Projects** — `https://github.com/discord/embedded-app-sdk-examples`: the
  playground app plus other examples.
- **Discord Developers** — `https://discord.gg/discord-developers`, the community server for API
  questions and platform-team events.

## Source

Discord Developer Documentation, `https://docs.discord.com/developers/activities/building-an-activity`,
retrieved 2026-08-26.
