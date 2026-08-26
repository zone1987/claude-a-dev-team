# Discord Linked Roles and Role Connection Metadata

The application role connection metadata object with all eight metadata types, both metadata
endpoints, and the "Configuring App Metadata for Linked Roles" tutorial end to end.

Sources: `https://docs.discord.com/developers/resources/application-role-connection-metadata` and
`https://docs.discord.com/developers/tutorials/configuring-app-metadata-for-linked-roles`, retrieved
2026-08-26.

## Contents

- [What linked roles are](#what-linked-roles-are)
- [Application Role Connection Metadata Object](#application-role-connection-metadata-object)
- [Application Role Connection Metadata Type](#application-role-connection-metadata-type)
- [GET /applications/{application.id}/role-connections/metadata](#get-applicationsapplicationidrole-connectionsmetadata)
- [PUT /applications/{application.id}/role-connections/metadata](#put-applicationsapplicationidrole-connectionsmetadata)
- [Tutorial: Configuring App Metadata for Linked Roles](#tutorial-configuring-app-metadata-for-linked-roles)

## What linked roles are

A representation of role connection metadata for an application.

When a guild has added a bot and that bot has configured its `role_connections_verification_url` (in
the developer portal), the application will render as a potential verification method in the guild's
role verification configuration.

If an application has configured role connection metadata, its metadata will appear in the role
verification configuration when the application has been added as a verification method to the role.

When a user connects their account using the bot's `role_connections_verification_url`, the bot will
update a user's role connection with metadata (`PUT /users/@me/applications/{application.id}/role-connection`,
Update Current User Application Role Connection — call the Skill tool with "discord-rest") using the
OAuth2 `role_connections.write` scope.

From the tutorial: linked roles are a type of role in Discord that requires a user to connect to
3rd-party services and meet defined criteria. A role's criteria could just include the user connecting
to that service, but it is often more narrow — like having a verified account, having certain stats, or
having more than a certain number of followers. Apps can define their own role connection metadata,
which admins can use to configure linked roles in servers where that app is installed. Apps must also
set up an OAuth2 flow to allow users to authenticate and grant the required `role_connections.write`
scope.

## Application Role Connection Metadata Object

###### Application Role Connection Metadata Structure

| Field | Type | Description |
| --- | --- | --- |
| type | [ApplicationRoleConnectionMetadataType](#application-role-connection-metadata-type) | type of metadata value |
| key | string | dictionary key for the metadata field (must be `a-z`, `0-9`, or `_` characters; 1-50 characters) |
| name | string | name of the metadata field (1-100 characters) |
| name_localizations? | dictionary with keys in available locales (see the API reference locale list) | translations of the name |
| description | string | description of the metadata field (1-200 characters) |
| description_localizations? | dictionary with keys in available locales | translations of the description |

## Application Role Connection Metadata Type

| Type | Value | Description |
| --- | --- | --- |
| INTEGER_LESS_THAN_OR_EQUAL | 1 | the metadata value (`integer`) is less than or equal to the guild's configured value (`integer`) |
| INTEGER_GREATER_THAN_OR_EQUAL | 2 | the metadata value (`integer`) is greater than or equal to the guild's configured value (`integer`) |
| INTEGER_EQUAL | 3 | the metadata value (`integer`) is equal to the guild's configured value (`integer`) |
| INTEGER_NOT_EQUAL | 4 | the metadata value (`integer`) is not equal to the guild's configured value (`integer`) |
| DATETIME_LESS_THAN_OR_EQUAL | 5 | the metadata value (`ISO8601 string`) is less than or equal to the guild's configured value (`integer`; `days before current date`) |
| DATETIME_GREATER_THAN_OR_EQUAL | 6 | the metadata value (`ISO8601 string`) is greater than or equal to the guild's configured value (`integer`; `days before current date`) |
| BOOLEAN_EQUAL | 7 | the metadata value (`integer`) is equal to the guild's configured value (`integer`; `1`) |
| BOOLEAN_NOT_EQUAL | 8 | the metadata value (`integer`) is not equal to the guild's configured value (`integer`; `1`) |

Each metadata type offers a comparison operation that allows guilds to configure role requirements
based on metadata values stored by the bot. Bots specify a `metadata value` for each user and guilds
specify the required `guild's configured value` within the guild role settings.

## GET /applications/{application.id}/role-connections/metadata

**Get Application Role Connection Metadata Records.** Returns a list of
[application role connection metadata](#application-role-connection-metadata-object) objects for the
given application.

The upstream page documents no query string parameters, no request body and no error responses for
this route.

## PUT /applications/{application.id}/role-connections/metadata

**Update Application Role Connection Metadata Records.** Updates and returns a list of
[application role connection metadata](#application-role-connection-metadata-object) objects for the
given application.

**An application can have a maximum of 5 metadata records.**

The upstream page documents the request body only as a list of application role connection metadata
objects, and documents no error responses for this route.

## Tutorial: Configuring App Metadata for Linked Roles

This tutorial walks through building a Discord app in JavaScript with linked roles support. All of the
sample code used in this tutorial can be found in the `linked-roles-sample` GitHub repo
(`https://github.com/discord/linked-roles-sample`).

### Creating an app

The first thing to do is create an app through the developer dashboard
(`https://discord.com/developers/applications`). If you already have an app created, jump right to
[Running your app](#running-your-app). Basic steps to create an app are outlined below, but a more
detailed walkthrough is in the Getting Started guide
(`https://docs.discord.com/developers/quick-start/getting-started`).

- Navigate to the developer dashboard (`https://discord.com/developers/applications`)
- Click **New Application** in the upper right corner, then select a name and create your app
- Click on the **Bot** tab (`https://discord.com/developers/applications/select/bot`) on the left
  sidebar. On that page, click **Reset Token** and store the token somewhere safe (like in a password
  manager)

**Warning.** Bot tokens are used to authorize API requests and carry your bot's permissions, making
them highly sensitive. Never share your token or check it into any kind of version control.

### Adding scopes

Apps need approval from installing users to perform actions inside of Discord. So before installing
your app, add some scopes to request during installation.

- Click on OAuth2 (`https://discord.com/developers/applications/select/oauth2/url-generator`) in the
  left sidebar, then `URL generator`
- Check the `bot` scope
- After the scope is selected, you should see a **Generated URL** which can be used to install your app

See `SCOPES.md` for the full list of OAuth2 scopes, and `PERMISSIONS.md` for user permissions.

### Installing your app

Copy the **Generated URL** from above, and paste it into your browser. You will be guided through the
installation flow, where you should make sure you are installing the app on a server where you can
develop and test.

After installing your app, you can head over to your server and see that it has joined.

### Running your app

All of the code used in the example app can be found in the GitHub repository
(`https://github.com/discord/linked-roles-sample`).

#### Remix the project

This guide uses Glitch, which allows you to quickly clone and develop an app from within your browser.
There are also instructions on developing locally using ngrok in the README if you would prefer.

While Glitch is great for development and testing, it has technical limitations
(`https://help.glitch.com/kb/article/17-technical-restrictions/`) so other hosting providers should be
considered for production apps.

To start, remix (or clone) the Glitch project
(`https://glitch.com/edit/#!/remix/linked-role-discord-bot`).

When you remix the project, you will see a new Glitch project with a unique name.
*(Upstream screenshot: "Glitch Remix".)*

#### Project structure

All of the files for the project are on the left-hand side. Here is a quick glimpse at the structure:

```
├── assets     -> images used in this tutorial
├── src
├──├── config.js  -> Parsing of local configuration
├──├── discord.js -> Discord specific auth & API wrapper
├──├── register.js -> Tool to register the metadata schema
├──├── server.js  -> Main entry point for the application
├──├── storage.js -> Provider for storing OAuth2 tokens
├── .env -> your credentials and IDs
├── .gitignore
├── package.json
└── README.md
```

#### Configure your app

There is already some code in your `server.js` file, but you will need your app's token and ID to make
requests. All of your credentials can be stored directly in the `.env` file.

**Warning.** It bears repeating that you should never check any credentials or secrets into source
control. The getting started project's `.gitignore` comes pre-loaded with `.env` to prevent it.

1. Copy your bot user's token from earlier and paste it in the `DISCORD_TOKEN` variable in your `.env`
   file.
2. Navigate to your app settings in the developer portal
   (`https://discord.com/developers/applications`), and navigate to **OAuth2 -> General**
   (`https://discord.com/developers/applications/select/oauth2`). Copy the Client ID and Client Secret
   for your application, and paste the values as `DISCORD_CLIENT_ID` and `DISCORD_CLIENT_SECRET` in
   your `.env`. *(Upstream screenshot: "Configure OAuth2".)*
3. Set the Redirect URL that will be used for the OAuth2 flow. Go back to Glitch, and click the
   `Share` button for your project. Copy the public live URL for your app.
   *(Upstream screenshot: "Glitch Share".)*
4. Go back to the **OAuth2 -> General** tab in the Discord developer portal, and add a new redirect
   for your app using the Glitch URL and the `/discord-oauth-callback` route. Copy this URL, then
   paste it as `DISCORD_REDIRECT_URI` in your `.env`.
5. Go to the **General Information** tab
   (`https://discord.com/developers/applications/select/information`) in the developer portal, and
   scroll down to the `Linked Roles Verification Url` field. Paste the base URL to your Glitch app,
   add the `/linked-role` route, then save. For the Glitch project used in the upstream screenshots,
   the verification URL would be `https://adjoining-crawling-yamamomo.glitch.me/linked-role`.
   *(Upstream screenshot: "Verify endpoint".)*
6. Finally, to generate a unique cookie secret, go back to Glitch, and click on the `Terminal` tab.
   Run the following commands:

```
$ node
crypto.randomUUID()
```

Copy the randomly generated UUID, and paste it into your `.env` as `COOKIE_SECRET`. Your `.env` should
look something like this:

```
DISCORD_CLIENT_ID: <your OAuth2 client Id>
DISCORD_CLIENT_SECRET: <your OAuth2 client secret>
DISCORD_TOKEN: <your bot token>
DISCORD_REDIRECT_URI: https://<your-project-name>.glitch.me/discord-oauth-callback
COOKIE_SECRET: <random generated UUID>
```

### Registering your metadata schema

As a **one-time step**, you must tell Discord which metadata fields you are going to allow admins to
use for linked roles associated with your app.

To configure connection metadata for your app, you will call the
`PUT /users/@me/applications/<application_id>/role-connection` method with application connection role
metadata (see [Update Application Role Connection Metadata Records](#put-applicationsapplicationidrole-connectionsmetadata)
and the [metadata object](#application-role-connection-metadata-object)). In the sample app, this is
handled in `src/register.js`
(`https://github.com/discord/linked-roles-sample/blob/main/src/register.js`), and can be run via the
command line.

Note the path discrepancy: the tutorial names `PUT /users/@me/applications/<application_id>/role-connection`
while the resource page documents the metadata route as
`PUT /applications/{application.id}/role-connections/metadata`. Both strings appear upstream as
written; the resource page is the reference for the metadata records route.

Go back to Glitch, click the **terminal** tab, and run the following command:

```
$ node src/register.js
```

*(Upstream screenshot: "Register Metadata Schema".)*

### Trying it out

Now that you have built your app, try it both from the server owner and the user's perspective.

#### Creating the linked role

To try out the app, create a linked role in a server where you have admin permissions. Open up the
**Server Settings**, select **Roles**, and click on `Create Role`.

Give the role a name, save it, then click on `Links`. Click the `Add requirement` button, and you
should see your bot in the list of available Apps. Click on it, and you will see a setup screen where
you can configure specific criteria for your role.
*(Upstream screenshot: "Verification Setup".)*

#### Acquiring the role

To acquire your newly created role, click the server name in the upper left corner of the screen, and
select `Linked Roles`. Click on your role, and it will present the opportunity to connect your account.

When you connect your account, one of the scopes requested in the OAuth flow is
`role_connections.write`, which is required for an app to update a user's role connection information.
*(Upstream screenshot: "Connect accounts".)*

Click on the linked role criteria. This should lead to the Discord OAuth2 consent screen. Click
`Authorize`, and then return to Discord.
*(Upstream screenshot: "Consent Dialog".)*

After returning to Discord, you should see your account granted the linked role.
*(Upstream screenshot: "Connected".)*

Finally, create a new private channel, and add the new linked role.

### Tips & Tricks

#### Token storage

This app largely relies on Discord's OAuth2 implementation to obtain access tokens. This model of user
based authentication relies on storing refresh tokens, and using them to acquire access tokens. The
example code in `src/storage.js`
(`https://github.com/discord/linked-roles-sample/blob/main/src/storage.js`) uses in-memory storage to
manage these tokens, but **for any production deployment a database with persistent storage should be
used**.

#### Advanced examples

For a more complex example using the Fitbit API, see
`https://github.com/JustinBeckwith/fitbit-discord-bot/`.

## Source

Discord Developer Documentation —
`https://docs.discord.com/developers/resources/application-role-connection-metadata` and
`https://docs.discord.com/developers/tutorials/configuring-app-metadata-for-linked-roles`, retrieved
2026-08-26.
