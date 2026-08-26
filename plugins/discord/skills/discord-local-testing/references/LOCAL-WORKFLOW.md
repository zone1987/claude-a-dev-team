# The Local Development Workflow

The walkthroughs assembled into one sequence. Every command, tree and file name below is verbatim
from a docs page; where a page does not state something, this file says so rather than filling it in.

## Contents

- [Which walkthrough applies](#which-walkthrough-applies)
- [Prerequisites the pages state](#prerequisites-the-pages-state)
- [Path A: an HTTP-interactions bot with Express and ngrok](#path-a-an-http-interactions-bot-with-express-and-ngrok)
  - [Step 0: project setup](#step-0-project-setup)
  - [Step 1: credentials into .env](#step-1-credentials-into-env)
  - [Step 2: register the commands](#step-2-register-the-commands)
  - [Step 3: run the server](#step-3-run-the-server)
  - [Step 4: open the tunnel](#step-4-open-the-tunnel)
  - [Step 5: point Discord at the tunnel](#step-5-point-discord-at-the-tunnel)
  - [Step 6: exercise the command](#step-6-exercise-the-command)
- [Path B: the same flow for a user-installable app](#path-b-the-same-flow-for-a-user-installable-app)
- [Path C: Cloudflare Workers, local then deploy](#path-c-cloudflare-workers-local-then-deploy)
- [Path D: Activity local development](#path-d-activity-local-development)
  - [Option 1: straight from localhost](#option-1-straight-from-localhost)
  - [Option 2: through a tunnel and the Discord proxy](#option-2-through-a-tunnel-and-the-discord-proxy)
  - [URL mapping rules](#url-mapping-rules)
  - [CSP exceptions](#csp-exceptions)
  - [Launching from the Discord client](#launching-from-the-discord-client)
  - [Moving an Activity to production](#moving-an-activity-to-production)
- [Tunnelling: what upstream prescribes and what it leaves open](#tunnelling-what-upstream-prescribes-and-what-it-leaves-open)
- [Secrets handling](#secrets-handling)
- [Where the documentation is silent](#where-the-documentation-is-silent)

## Which walkthrough applies

Four distinct local flows exist in the documentation, and they differ in what they need:

| Flow | Page | Tunnel | Port used in the page |
|---|---|---|---|
| Bot with HTTP interactions | `quick-start/getting-started` | `ngrok` | 3000 |
| User-installable bot | `tutorials/developing-a-user-installable-app` | `ngrok` | 3000 |
| Cloudflare Workers bot | `tutorials/hosting-on-cloudflare-workers` | `ngrok`, via `npm run ngrok` | not stated |
| Activity | `activities/building-an-activity`, `activities/development-guides/local-development` | `cloudflared` (ngrok named as an alternative) | 5173 (guide), 3000 (dev guide example) |

A **Gateway-only** bot has no flow of its own in the documentation, because it needs no public URL —
see [GATEWAY-VS-HTTP.md](GATEWAY-VS-HTTP.md). The pages here all describe HTTP-facing setups.

## Prerequisites the pages state

> If you don't have [NodeJS](https://nodejs.org/en/download/) installed, install that first.

The Cloudflare Workers tutorial is more specific: "This requires at least v16 of
[Node.js](https://nodejs.org/en/)". The Getting Started guide states no minimum version.

> This guide is beginner-focused, but it assumes a basic understanding of
> [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics).

The Activity guide adds: "It assumes an understanding of JavaScript and async functions, and a basic
understanding of frontend frameworks like React and Vue."

The tooling each guide names:

**Getting Started** and **user-installable**:

> * **[GitHub repository](https://github.com/discord/discord-example-app)** where the code from this guide lives along with some additional feature-specific code examples.
> * **[discord-interactions](https://github.com/discord/discord-interactions-js)**, a library that provides types and helper functions for Discord apps.
> * **[Express](https://expressjs.com)**, a popular JavaScript web framework we'll use to create a server where Discord can send us requests.
> * **[ngrok](https://ngrok.com/)**, a tool that lets us tunnel our local server to a public URL where Discord can send requests.

**Cloudflare Workers**:

> * [Discord Interactions API](https://docs.discord.com/developers/interactions/receiving-and-responding) (specifically slash commands)
> * [Cloudflare Workers](https://workers.cloudflare.com/) for hosting
> * [Reddit API](https://www.reddit.com/dev/api/) to send messages back to the user

**Activity**: Vite ("a build tool for modern JavaScript projects that will make your application
easier to serve") and "[cloudflared](https://github.com/cloudflare/cloudflared?tab=readme-ov-file#installing-cloudflared),
for bridging your local development server to the internet".

And the framing sentence both bot tutorials repeat:

> We'll be developing our app locally with a little help from [ngrok](https://ngrok.com/), but you
> can use your preferred development environment.

## Path A: an HTTP-interactions bot with Express and ngrok

### Step 0: project setup

```bash
git clone https://github.com/discord/discord-example-app.git
```

```bash
# navigate to directory
cd discord-example-app

# install dependencies
npm install
```

The project structure, verbatim from the page:

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

### Step 1: credentials into `.env`

> Back in your project folder, rename the `.env.sample` file to `.env`. This is where we'll store
> all of your app's credentials.

The three values and where they come from are in [APP-SETUP.md](APP-SETUP.md). The placeholder names
the page substitutes into are `<YOUR_APP_ID>`, `<YOUR_PUBLIC_KEY>` and `<YOUR_BOT_TOKEN>`.

The only environment variable the page documents as configurable beyond those:

> By default, the server will listen to requests sent to port 3000, but if you want to change the
> port, you can specify a `PORT` variable in your `.env` file.

### Step 2: register the commands

```
npm run register
```

> If you navigate back to your server, you should see the slash commands appear. But if you try to
> run them, nothing will happen since your app isn't receiving or handling any requests from Discord.

Details of what that script calls, and the guild-versus-global choice, are in
[COMMAND-REGISTRATION.md](COMMAND-REGISTRATION.md).

### Step 3: run the server

> To enable your app to receive slash command and other interactions requests, Discord needs a
> public URL to send them. This URL can be configured in your app's settings as **Interaction
> Endpoint URL**.

> To set up a public endpoint, we'll start our app which runs an [Express](https://expressjs.com/)
> server, then use [ngrok](https://ngrok.com/) to expose our server publicly.
>
> First, go to your project's folder and run the following to start your app:

```
npm run start
```

> There should be output indicating your app is running on port `3000`. Behind the scenes, our app
> is ready to handle interactions from Discord, which includes verifying security request headers
> and responding to `PING` requests.

### Step 4: open the tunnel

> Next, we'll start our ngrok tunnel. If you don't have ngrok installed locally, you can install it
> by following the instructions on the [ngrok download page](https://ngrok.com/download).
>
> After ngrok is installed, open a new terminal and create a public endpoint that will forward
> requests to your Express server:

```
ngrok http 3000
```

> You should see your connection open with output similar to the following:

```
Tunnel Status                 online
Version                       2.0/2.0
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://1234-someurl.ngrok.io -> localhost:3000

Connections                  ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

> We'll use **Forwarding** URL as the publicly-accessible URL where Discord will send interactions
> requests in the next step.

Two details in that output worth knowing while debugging: the tunnel is **HTTPS** on the public side
while forwarding to plain `localhost:3000`, and ngrok exposes its own **Web Interface** at
`http://127.0.0.1:4040`. The page prints both but comments on neither, so treat the web interface as
an ngrok feature the docs display rather than a Discord-documented debugging tool.

### Step 5: point Discord at the tunnel

> Go to your [app's settings](https://discord.com/developers/applications) and on the
> [**General Information** page](https://discord.com/developers/applications/select/information)
> under **Interaction Endpoint URL**, paste your new ngrok forwarding URL and append `/interactions`.

Screenshot caption: *Interactions Endpoint URL*.

> Click **Save Changes** and ensure your endpoint is successfully verified.

The user-installable tutorial gives the fully-assembled shape: "paste your new ngrok URL and append
`/interactions` (it'll be something like `https://84c5df474.ngrok-free.dev/interactions`)."

The one troubleshooting note both pages give, verbatim:

> If you have troubles verifying your endpoint, make sure both ngrok and your app are running on the
> same port, and that you've copied the ngrok URL correctly

And what the sample app does to pass verification:

> The verification is handled automatically by the sample app in two ways:
>
> * It uses the `PUBLIC_KEY` and [discord-interactions package](https://github.com/discord/discord-interactions-js#usage) with a wrapper function (imported from `utils.js`) that makes it conform to [Express's `verify` interface](http://expressjs.com/en/5x/api.html#express.json). This is run on every incoming request to your app.
> * It responds to incoming `PING` requests.

**The URL changes every time the tunnel restarts.** The page's example URLs
(`https://1234-someurl.ngrok.io`, `https://84c5df474.ngrok-free.dev`) are randomly generated, so
restarting the tunnel means pasting a new URL into the portal and saving again. Upstream does not say
this explicitly and does not describe a stable-URL option.

### Step 6: exercise the command

> With the endpoint verified, navigate to your project's `app.js` file and find the code block that
> handles the `/test` command:

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

> Go to your server and make sure your app's `/test` slash command works. When you trigger it, your
> app should send a message that contains "hello world" followed by a random emoji.

That sentence is the acceptance test the guide gives for the whole chain: portal → tunnel → server →
verification → response.

One note about the sample's storage that matters if you carry the pattern forward:

> The sample code uses an object as in-memory storage, but for production apps you should use a
> database.

## Path B: the same flow for a user-installable app

Identical shape, different repository and project tree.

```
git clone https://github.com/discord/user-install-example.git
```

```
# navigate to directory
cd user-install-example

# install dependencies
npm install
```

Project structure, verbatim:

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

Then the same `npm run register`, `npm run start`, `ngrok http 3000`, and the same portal step. The
same `PORT` note applies.

What this path adds is the ability to verify **contexts** — the same command behaving differently in
a guild, in the bot's DM, and in a group DM. After the endpoint is live:

> Now that our Interactions Endpoint URL is set up, we should now be able to run our app's commands.
> Go to your app's DM and run `/profile`, and your app should respond with a sample game profile.
>
> Back on the command line, our app is logging incoming requests from Discord, so you can see what
> the request body for your command invocation looked like.

**Logging the raw interaction body is the documented local debugging technique for this path.** The
sample payload to compare against, and the fields worth watching, are in
[GATEWAY-VS-HTTP.md](GATEWAY-VS-HTTP.md).

The context-dependent response the sample demonstrates:

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

## Path C: Cloudflare Workers, local then deploy

This is the one page that carries a local-then-deploy sequence with real secret management.

**Set up the Worker:**

> * Visit the [Cloudflare Dashboard](https://dash.cloudflare.com/)
> * Click on the `Workers` tab, and create a new service using the same name as your Discord bot
> * Make sure to [install the Wrangler CLI](https://developers.cloudflare.com/workers/cli-wrangler/install-update/) and set it up.

**Store the secrets** — "The production service needs access to some of the information we saved
earlier. To set those variables, run:"

```
$ wrangler secret put DISCORD_TOKEN
$ wrangler secret put DISCORD_PUBLIC_KEY
$ wrangler secret put DISCORD_APPLICATION_ID
```

> Once you know your Guild ID, set that variable as well:

```
$ wrangler secret put DISCORD_TEST_GUILD_ID
```

Note that `DISCORD_TEST_GUILD_ID` is set as a secret even though the tutorial's own `register.js`
registers globally. Upstream does not explain the discrepancy.

**Install and run locally:**

> This depends on the beta version of the `wrangler` package, which better supports ESM on Cloudflare
> Workers.

```
$ npm install
```

Project structure, verbatim:

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

`test/test.js` is the only mention of a test file in any of these pages. **The page does not describe
what those tests assert, nor a command to run them** — the CI configuration below shows `test` and
`lint` as jobs the release step depends on, but no invocation is given.

**Register commands, once:**

```
$ DISCORD_TOKEN=**** DISCORD_APPLICATION_ID=**** node src/register.js
```

**Start the dev server:**

```
$ npm run dev
```

**Tunnel** — this page wraps ngrok in an npm script:

> When a user types a slash command, Discord will send an HTTP request to a public endpoint. During
> local development this can be a little challenging, so we're going to use
> [a tool called `ngrok`](https://ngrok.com/) to create an HTTP tunnel.

```
$ npm run ngrok
```

Screenshot caption: *ngrok forwarding address*.

> This is going to bounce requests off of an external endpoint, and forward them to your machine.
> Copy the HTTPS link provided by the tool. It should look something like
> `https://8098-24-22-245-250.ngrok.io`.
>
> Now head back to the Discord Developer Dashboard, and update the `Interactions Endpoint URL` for
> your app:

Screenshot caption: *Interactions Endpoint URL*.

**The switch from local to deployed is one field:**

> This is the process we'll use for local testing and development. When you've published your app to
> Cloudflare, you will **want to update this field to use your Cloudflare Worker URL.**

Note this page does **not** say to append a path segment: the Worker's router handles `POST /`, so
the tunnel root is the endpoint. That differs from the Express samples, which append `/interactions`.

**Deploy:**

> This repository is set up to automatically deploy to Cloudflare Workers when new changes land on
> the `main` branch. To deploy manually, run `npm run publish`, which uses the `wrangler publish`
> command under the hood.
>
> Publishing via a GitHub Action requires obtaining an
> [API Token and your Account ID from Cloudflare](https://developers.cloudflare.com/workers/cli-wrangler/authentication/).
> These are stored [as secrets in the GitHub repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets),
> making them available to GitHub Actions.

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

**One Workers-specific constraint that will look like a bug:**

> When using Cloudflare Workers, your app won't be able to access non-ephemeral CDN media. For
> example, trying to fetch an image like
> `https://cdn.discordapp.com/attachments/1234/56789/my_image.png` would result in a `403` error.
> Cloudflare Workers are still able to access ephemeral CDN media.

The Worker's entry point and router code are in [GATEWAY-VS-HTTP.md](GATEWAY-VS-HTTP.md), since they
are the endpoint contract rather than the workflow.

## Path D: Activity local development

Activities have their own page, and two documented options.

The project the guide clones:

```
git clone git@github.com:discord/getting-started-activity.git
```

> The sample project you cloned is broken into two parts:
>
> * `client` is the sample Activity's frontend, built with vanilla JavaScript and integrated with [Vite](https://vitejs.dev/) to help with local development.
> * `server` is a backend using vanilla JavaScript, Node.js, and Express. However, as you're building your own Activity, you can use whichever backend you prefer.

Project structure, verbatim:

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

Install and run the frontend:

```
cd getting-started-activity/client
```

```
# install project dependencies
npm install

# start frontend
npm run dev
```

> If you visit [http://localhost:5173/](http://localhost:5173/) you should see a vanilla JS frontend
> template running with [Vite](https://vitejs.dev/).

Later in the guide the same start step, with its output:

```
cd client
npm run dev
```

```
VITE v5.0.12  ready in 100 ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
➜  press h + enter to show help
```

> We'll use the Local URL as our publicly-accessible URL in the next step.

Port `5173` is Vite's, as shown in that output. **The page states no flag for changing it and
documents no Discord-side port requirement** — the requirement is on the protocol, not the port.

Environment file:

```
cp example.env .env
```

> **Secure Your Secrets**
>
> Your `DISCORD_CLIENT_SECRET` and `DISCORD_BOT_TOKEN` are *highly* sensitive secrets. Never share
> either secrets or check them into any kind of version control.

The two values, `VITE_CLIENT_ID` and `DISCORD_CLIENT_SECRET`, are in [APP-SETUP.md](APP-SETUP.md),
along with why the `VITE_` prefix exists. The scopes the sample requests: `identify`, `guilds`,
`applications.commands`. A placeholder Redirect URI of `https://127.0.0.1` is set on the OAuth2 page.

Enabling Activities in the portal:

> On the left hand sidebar under **Activities**, click
> [**Settings**](https://discord.com/developers/applications/select/embedded/settings).
>
> Find the first checkbox, labeled `Enable Activities`. Turn it on 🎉

Screenshot caption: *Enabling Activities in Settings*.

And a side effect worth expecting:

> When you enable Activities for your app, a default Entry Point command called "Launch" is
> automatically created. This Entry Point command is the primary way for users to launch your
> Activity in Discord.
>
> By default, interactions with this command will result in Discord opening your Activity for the
> user and posting a message in the channel where it was launched from. However, if you prefer to
> handle the interactions in your app, you can update the `handler` field or create your own.

### Option 1: straight from localhost

> It is possible to load your application via a localhost port or other unique URL. This URL must
> support an HTTPS connection to load on the web/desktop Discord app (HTTPS is not required for
> mobile). The downside to this flow is that your application's network traffic will not pass through
> Discord's proxy, which means any requests made by the application will need to use a full URL
> instead of a "mapped" URL.
>
> To run your locally hosted application, follow the instructions for Launching your Application from
> the Discord Client and set the Application URL Override to the address of your application's web
> server.

Two facts to carry from that: **HTTPS is required on web and desktop but not on mobile**, and taking
this route means writing full URLs rather than mapped ones, so it does not rehearse production
behaviour.

### Option 2: through a tunnel and the Discord proxy

The recommended route, verbatim:

> Although it is possible to test your application locally, we recommend developing and testing
> against the Discord proxy. This is helpful to make sure all URLs behave as expected before your
> application runs in production. One technique to enable testing locally against the proxy is to use
> a network tunneling tool, such as
> [cloudflared](https://github.com/cloudflare/cloudflared#installing-cloudflared). A typical pattern
> is for each developer to have their own "development-only" application. To set up a local
> environment to run through Discord's proxy, you will need to do the following:
>
> 1. Create a new application in the Discord Developer portal.
> 2. Enable Activities for your app.
> 3. Set up the application's URL mapping.
> 4. Locally, spin up your web server.
> 5. Install and run a tunnel solution, such as [cloudflared](https://github.com/cloudflare/cloudflared#installing-cloudflared). You will point it to your local web server.

> Your web server can be HTTP and your network tunnel can upgrade the connection to HTTPS.

> If using cloudflared, you will run the following command, replace `3000` with your web server's
> port.

```
cloudflared tunnel --url http://localhost:3000
```

> Once you run this command, you will receive your publicly accessible network tunnel address from
> cloudflared.

```
Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):
https://funky-jogging-bunny.trycloudflare.com
```

> In the Discord Developer Portal, update the Application URL mapping for `/` url to
> `funky-jogging-bunny.trycloudflare.com` to match your network tunnel address and save your changes.

Screenshot caption: *Configuring your URL Mapping*.

> Follow the instructions for Launching your Application from the Discord Client. Application URL
> Override should not be enabled.

The building-an-activity guide runs the same command against Vite's port:

> While your app is still running, open another terminal window and start a network tunnel that
> listens to the port from the last step (in this case, port `5173`):

```
cloudflared tunnel --url http://localhost:5173
```

```
Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):
https://funky-jogging-bunny.trycloudflare.com
```

> Copy the URL from the output, as we'll need to add it to our app's settings.

> Back in your app's settings, click on the
> [**URL Mappings** page](https://discord.com/developers/applications/select/embedded/url-mappings)
> under **Activities** on the left-hand sidebar. Enter the URL you generated from `cloudflared` in
> the previous step.

| PREFIX | TARGET |
| ------ | --------------------------------------- |
| `/` | `funky-jogging-bunny.trycloudflare.com` |

**A security warning that applies to every free-tier tunnel, verbatim:**

> If you do not own the URL that you are using to host the application (i.e. ngrok's free tier),
> someone else could claim that domain and host a malicious site in its place. Please be aware of
> these risks, and if you have to use a domain you do not own, be sure to reset your URL mapping when
> you are done using the tunnel.

That is the one place upstream tells you to clean up after a local session.

Then launch:

> Navigate to your Discord test server and, in any voice and or text channel, open the App Launcher
> where your in-development Activity should be present. If you don't see your Activity, you should
> try searching for its name.

### URL mapping rules

Why mappings exist at all:

> Activities in Discord are "sandboxed" via a Discord proxy. This is done to hide the users' IP
> addresses, your application's IP addresses, and to block URLs from known malicious endpoints. As an
> application owner, you can configure the proxy to allow network requests to external endpoints.
>
> Because your application is "sandboxed", it will be unable to make network requests to external
> URLs. Let's say you want request `https://some-api.com`. To enable reaching this url from inside
> your application, you will create a new url mapping, with the `PREFIX` set to `/api` and `TARGET`
> set to `some-api.com`. Now you can make requests to `/api` from inside of your application, which
> will be forwarded, via Discord's proxy to `some-api.com`.

Where to set them:

> To add or modify your application's URL mappings, click on
> [Activities -> URL Mappings](https://discord.com/developers/applications/select/embedded/url-mappings)
> and set the prefix and target values for each mapping as needed.

Formatting rules, verbatim:

> * URL mappings can utilize any url protocol, (https, wss, ftp, etc...), which is why the URL target should not include a protocol. For example, for a URL target, do not put `https://your-url.com`, instead, omit `https://` and use `your-url.com`.
> * Parameter matching can be used to help map external domain urls. For example, if an external url has many subdomains, such as `foo.google.com`, `bar.google.com`, then you could use the following mapping:

| PREFIX | TARGET |
| --------------------- | ------------------------ |
| `/google/{subdomain}` | `{subdomain}.google.com` |

> * Targets must point to a directory; setting a target to a file (e.g. `example.com/index.html`) is unsupported and may lead to unexpected behavior.
> * Because of how URL globbing works, if you have multiple prefix urls with the same initial path, you must place the shortest of the prefix paths last in order for each url mapping to be reachable. For example, if you have `/foo` and `/foo/bar`, you must place the url `/foo/bar` before `/foo` or else the mapping for `/foo/bar` will never be reached.

The page's DO / DON'T table is a pair of screenshots. Their captions and the accompanying text:

| ✅ DO | ❌ DON'T |
|---|---|
| Requests mapped correctly (`url-mapping-do.png`) | Requests to /foo/bar will incorrectly be sent to `foo.com` (`url-mapping-dont.png`) |

For production, the mapping requirement is stated slightly more precisely: "Set up the application's
URL Mapping. The URL for your application's html should be set to the `/` route."

### CSP exceptions

> The aforementioned "sandbox" is enforced by a
> [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP). We have
> some notable exceptions to our CSP, meaning application clients may make requests to these URLs
> without hitting the proxy and therefore without establishing mappings. Notable exceptions include:
>
> * `https://discord.com/api/`
> * `https://canary.discord.com/api/`
> * `https://ptb.discord.com/api/`
> * `https://cdn.discordapp.com/attachments/`
> * `https://cdn.discordapp.com/avatars/`
> * `https://cdn.discordapp.com/icons/`
> * `https://media.discordapp.net/attachments/`
> * `https://media.discordapp.net/avatars/`
> * `https://media.discordapp.net/icons/`

Note "Notable exceptions **include**" — the list is explicitly not exhaustive.

### Launching from the Discord client

> You will be able to see and launch all activities owned by you or any teams you are a member of via
> the Developer Activity Shelf. One caveat is that the activity will not be shown on the current
> platform (web/ios/android) unless you have checked your platform in
> [Settings/Supported Platforms](https://discord.com/developers/applications/select/embedded/settings)
> on the developer portal.

**Web**

> 1. Select ⚙️ User Settings > App Settings > Advanced and toggle on `Developer Mode`
> 2. Close the settings window and enter a voice channel.
> 3. From either the RTC Panel or the Center Control Tray, click on the "Rocket Button" to open the Activity shelf. You should now see all of the same applications that you have access to in the developer portal. Note: The shelf will only include applications which have been flagged as "Embedded".
> 4. Click on an activity to launch it!

**Mobile**

> 1. From your User Profile, select Appearance, and then toggle "On" `Developer Mode`
> 2. Enter a voice channel
> 3. Click on an activity to launch it!

Developer Mode is also what the building-an-activity guide starts with:

> Before getting started, you need to enable Developer Mode for your Discord account if you don't
> already have it enabled. Developer Mode will allow you to run in-development Activities and expose
> resource IDs (like users, channels, and servers) in the client which can simplify testing.

> 2. Click on **Advanced** tab from the left-hand sidebar and toggle on `Developer Mode`.

### Moving an Activity to production

> The flow for setting up your production application is very similar:
>
> 1. If not made yet, create a new application.
> 2. Enable Activities for your app.
> 3. Set up the application's URL Mapping. The URL for your application's html should be set to the `/` route.
> 4. Follow the instructions for Launching your Application from the Discord Client. Application URL Override should not be enabled.
>
> This application now uses the same configuration it will use once it is fully published ✨.

## Tunnelling: what upstream prescribes and what it leaves open

**Upstream does name specific tools.** This is not a case where the docs stay abstract:

- `quick-start/getting-started` names **ngrok** and links its download page.
- `tutorials/developing-a-user-installable-app` names **ngrok**.
- `tutorials/hosting-on-cloudflare-workers` names **ngrok**, wrapped as `npm run ngrok`.
- `activities/development-guides/local-development` names **cloudflared** and gives its command.
- `activities/building-an-activity` names **cloudflared** and explicitly permits alternatives:
  "While we'll be using `cloudflared` in this guide, you can use [ngrok](https://ngrok.com/docs) or
  another reverse proxy solution if you prefer."

**And it is explicit that the tool is not the requirement.** Both bot tutorials say "you can use your
preferred development environment"; the Activity guide says "or another reverse proxy solution if you
prefer"; the Activity dev guide says "a network tunneling tool, such as cloudflared."

The requirement itself, stated across the pages:

- **For interactions:** a **public HTTPS endpoint Discord can POST to**. "Discord will send these
  events to a pre-configured HTTPS endpoint (called an Interactions Endpoint URL in an app's
  configuration)"; "Discord needs a public URL to send them."
- **For an Activity on web/desktop:** "This URL must support an HTTPS connection to load on the
  web/desktop Discord app (HTTPS is not required for mobile)."
- **Your own server need not speak HTTPS.** "Your web server can be HTTP and your network tunnel can
  upgrade the connection to HTTPS."

So: any mechanism producing a public HTTPS address that forwards to your local port satisfies the
documented requirement. ngrok and cloudflared are the two the docs demonstrate.

## Secrets handling

Everything upstream says about secrets in a local project, gathered:

- **Never commit them.** "Make sure to never share your token or check it into any kind of version
  control." / "should never be shared or checked into version control." / "Never share either secrets
  or check them into any kind of version control." Every sample project's tree includes a
  `.gitignore`; none of the pages states what it contains.
- **`.env` is the documented local mechanism**, created by renaming `.env.sample` (bot samples) or
  `cp example.env .env` (Activity sample).
- **A password manager for the token itself.** "make sure to keep it somewhere safe (like in a
  password manager)"; "I like to put these tokens in a password manager like 1password or lastpass."
- **`wrangler secret put` for deployed Workers**, one invocation per value.
- **`VITE_` prefix as an exposure boundary** in the Activity sample: "Prefixing the `CLIENT_ID`
  environment variable with `VITE_` makes it accessible to our client-side code. This security
  measure ensures that only the variables you intend to be accessible in the browser are available,
  and all other environment variables remain private."
- **GitHub Actions secrets** for `CF_API_TOKEN` and `CF_ACCOUNT_ID`.
- **The token can be viewed once.** "You won't be able to view your token again unless you regenerate
  it"; "For security reasons, you can only view your bot token once."
- **Reset the URL mapping after using a tunnel domain you do not own.**

## Where the documentation is silent

- **No stable tunnel URL guidance.** Every example URL is randomly generated, and no page mentions
  reserved domains, config files, or how to avoid re-pasting the Interactions Endpoint URL after each
  restart. You decide whether to pay for a fixed subdomain or re-paste.
- **No hot reload story for a bot.** `npm run start` and `npm run dev` are given as-is. No page
  mentions a watcher, `nodemon`, or what to restart after a code change. Whether the tunnel survives
  a server restart is not stated.
- **No local testing without Discord.** There is no documented way to synthesise a signed interaction
  request, no test fixture, no sandbox mode. `test/test.js` exists in the Workers repository tree and
  the page never says what it contains or how to run it. Every documented verification path goes
  through the live Discord client.
- **No stated way to run two developers against one app.** The Activities page recommends
  "development-only" applications per developer; the bot pages never address it, and the
  Interactions Endpoint URL is a single field per app, so two developers cannot both receive HTTP
  interactions from one app. Upstream does not say this — it follows from the field being singular.
- **No `.env` contract.** Only `PORT` is documented as a variable the sample server reads. Every
  other name (`APP_ID`, `PUBLIC_KEY`, `DISCORD_TOKEN`, `VITE_CLIENT_ID`, …) comes from a sample
  repository, not from a documented interface.
- **No guidance on the Activity backend during local development.** The sample has a `server`
  directory, and the guide's tunnel points at the `client` port. How the backend is reached locally
  is not spelled out on these pages.
- **No cleanup procedure beyond the URL mapping reset.** Nothing about removing the Interactions
  Endpoint URL, deleting test commands, or uninstalling the app from a test server when you are done.

## Source

Retrieved 2026-08-26 from:

- `docs.discord.com/developers/quick-start/getting-started`
- `docs.discord.com/developers/tutorials/developing-a-user-installable-app`
- `docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers`
- `docs.discord.com/developers/activities/development-guides/local-development`
- `docs.discord.com/developers/activities/building-an-activity`
- `docs.discord.com/developers/interactions/overview`
