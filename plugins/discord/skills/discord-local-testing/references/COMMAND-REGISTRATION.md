# Command Registration: Guild-Scoped versus Global

The single biggest lever on iteration speed. This file carries every stated detail about the two
scopes, their endpoints, and what upstream says about propagation.

## Contents

- [Guild commands update instantly; global commands do not](#guild-commands-update-instantly-global-commands-do-not)
- [What upstream actually states about global propagation](#what-upstream-actually-states-about-global-propagation)
- [Registration is HTTP-only](#registration-is-http-only)
- [Registering a global command](#registering-a-global-command)
- [Registering a guild command](#registering-a-guild-command)
- [Updating and deleting: upsert by name](#updating-and-deleting-upsert-by-name)
- [Name uniqueness across scopes](#name-uniqueness-across-scopes)
- [Command count ceilings](#command-count-ceilings)
- [The 200-creates-per-day limit](#the-200-creates-per-day-limit)
- [All ten command endpoints](#all-ten-command-endpoints)
- [Contexts: integration_types and contexts](#contexts-integration_types-and-contexts)
- [Default permissions](#default-permissions)
- [Retrieving localized commands](#retrieving-localized-commands)
- [What the sample apps do](#what-the-sample-apps-do)
- [Where the documentation is silent](#where-the-documentation-is-silent)

## Guild commands update instantly; global commands do not

The recommendation, verbatim:

> Guild commands are available only within the guild specified on creation. Guild commands update
> **instantly**. We recommend you use guild commands for quick testing, and global commands when
> they're ready for public use.

And on the create endpoint: "New guild commands will be available in the guild immediately." On the
edit endpoint: "Updates for guild commands will be available immediately."

The scope difference itself:

> Commands can be scoped either globally or to a specific guild. Global commands are available for
> every guild that adds your app. An individual app's global commands are also available in DMs if
> that app has a bot that shares a mutual guild with the user.
>
> Guild commands are specific to the guild you specify when making them. Guild commands are not
> available in DMs.

**A consequence for local testing.** Guild commands cannot be tested in a DM at all — "Guild
commands are not available in DMs", and "Guild commands don't support the `BOT_DM` interaction
context." If your test needs the bot's DM, that command has to be global.

## What upstream actually states about global propagation

**Upstream states no propagation duration for global commands.** There is no "up to one hour" or
similar figure anywhere on the application-commands page. What it does state is a repair mechanism:

> Global commands have inherent read-repair functionality. That means that if you make an update to a
> global command, and a user tries to use that command before it has updated for them, Discord will do
> an internal version check and reject the command, and trigger a reload for that command.

So the documented behaviour of using a stale global command is: **the invocation is rejected and the
client reloads the command**, not that it silently runs an old version.

The only quantitative hint upstream gives lives in a code comment in the Cloudflare Workers
tutorial's `register.js`, verbatim:

```js
/**
 * Register all commands globally.  This can take o(minutes), so wait until
 * you're sure these are the commands you want.
 */
async function registerGlobalCommands() {
  const url = `https://discord.com/api/v10/applications/${applicationId}/commands`;
  await registerCommands(url);
}
```

Treat "o(minutes)" as the only order-of-magnitude the documentation offers. Do not report a specific
number to a user; the docs do not give one.

## Registration is HTTP-only

> Commands can only be registered via HTTP endpoint.

That holds regardless of transport: a Gateway bot still registers its commands over the REST API.
Authorization:

> For authorization, all endpoints take either a bot token or client credentials token for your
> application

The examples show both forms:

```py
# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot <my_bot_token>"
}

# or a client credentials token for your app with the applications.commands.update scope
headers = {
    "Authorization": "Bearer <my_credentials_token>"
}
```

## Registering a global command

> Global commands are available on *all* your app's guilds.
>
> To make a **global** command, make an HTTP POST call like this:

```py
import requests


url = "https://discord.com/api/v10/applications/<my_application_id>/commands"

# This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "blep",
    "type": 1,
    "description": "Send a random adorable animal photo",
    "options": [
        {
            "name": "animal",
            "description": "The type of animal",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "Dog",
                    "value": "animal_dog"
                },
                {
                    "name": "Cat",
                    "value": "animal_cat"
                },
                {
                    "name": "Penguin",
                    "value": "animal_penguin"
                }
            ]
        },
        {
            "name": "only_smol",
            "description": "Whether to show only baby animals",
            "type": 5,
            "required": False
        }
    ]
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot <my_bot_token>"
}

# or a client credentials token for your app with the applications.commands.update scope
headers = {
    "Authorization": "Bearer <my_credentials_token>"
}

r = requests.post(url, headers=headers, json=json)
```

## Registering a guild command

> To make a **guild** command, make a similar HTTP POST call, but scope it to a specific `guild_id`:

```py
import requests


url = "https://discord.com/api/v10/applications/<my_application_id>/guilds/<guild_id>/commands"

# This is an example USER command, with a type of 2
json = {
    "name": "High Five",
    "type": 2
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot <my_bot_token>"
}

# or a client credentials token for your app with the applications.commands.update scope
headers = {
    "Authorization": "Bearer <my_credentials_token>"
}

r = requests.post(url, headers=headers, json=json)
```

The `guild_id` for your test server comes from the client URL, per the Cloudflare tutorial:

> This can be found in the URL when you visit any channel in that server. For example, if my URL was
> `https://discord.com/channels/123456/789101112`, the Guild ID is the first number—in this case
> **`123456`**.

## Updating and deleting: upsert by name

> Commands can be deleted and updated by making `DELETE` and `PATCH` calls to the command endpoint.
> Those endpoints are
>
> * `applications/<my_application_id>/commands/<command_id>` for global commands, or
> * `applications/<my_application_id>/guilds/<guild_id>/commands/<command_id>` for guild commands
>
> Because commands have unique names within a type and scope, we treat `POST` requests for new
> commands as upserts. That means **making a new command with an already-used name for your
> application will update the existing command**.

That upsert behaviour is why a `register` script can be run repeatedly without accumulating
duplicates. The endpoints confirm it in their return codes: "Returns `201` if a command with the
same name does not already exist, or a `200` if it does (in which case the previous command will be
overwritten)."

`PATCH` semantics: "All fields are optional, but any fields provided will entirely overwrite the
existing values of those fields."

## Name uniqueness across scopes

> Command names are unique per application, per type, within each scope (global and guild). That
> means:
>
> * Your app **cannot** have two global `CHAT_INPUT` commands with the same name
> * Your app **cannot** have two guild `CHAT_INPUT` commands within the same name **on the same guild**
> * Your app **cannot** have two global `USER` commands with the same name
> * Your app **can** have a global and guild `CHAT_INPUT` command with the same name
> * Your app **can** have a global `CHAT_INPUT` and `USER` command with the same name
> * Your app **cannot** have a `PRIMARY_ENTRY_POINT` guild command
> * Multiple apps **can** have commands with the same names
>
> This list is non-exhaustive. In general, remember that command names must be unique per
> application, per type, and within each scope (global and guild).

**"Can have a global and guild command with the same name" is a local-testing trap.** If you develop
with a guild-scoped `/foo` and later register a global `/foo`, both exist and both appear. Delete the
guild copy when you promote a command to global, or you will be debugging whichever one the client
happened to pick.

## Command count ceilings

> An app can have the following number of commands:
>
> * 100 global `CHAT_INPUT` commands
> * 15 global `USER` commands
> * 15 global `MESSAGE` commands
> * 1 global `PRIMARY_ENTRY_POINT` command
>
> For all command types except `PRIMARY_ENTRY_POINT`, you can have the same amount of guild-specific
> commands per guild.

## The 200-creates-per-day limit

> There is a global rate limit of 200 application command creates per day, per guild

This is the ceiling on how many times you can iterate on a command in one day in one test guild. A
`register` script that creates several commands per run consumes proportionally. Bulk overwrite is
not a way around it:

> Commands that do not already exist will count toward daily application command create limits.

## All ten command endpoints

### GET /applications/{application.id}/commands
Fetch all of the global commands for your application. Returns an array of application command
objects.

Query string params:

| Field | Type | Description |
| ---- | ---- | ---- |
| with_localizations? | boolean | Whether to include full localization dictionaries (`name_localizations` and `description_localizations`) in the returned objects, instead of the `name_localized` and `description_localized` fields. Default `false`. |

> The objects returned by this endpoint may be augmented with additional fields if localization is active.

### POST /applications/{application.id}/commands
Create a new global command. Returns `201` if a command with the same name does not already exist, or
a `200` if it does (in which case the previous command will be overwritten). Both responses include
an application command object.

> Creating a command with the same name as an existing command for your application will overwrite the old command.

### GET /applications/{application.id}/commands/{command.id}
Fetch a global command for your application.

### PATCH /applications/{application.id}/commands/{command.id}
Edit a global command. Returns `200` and an application command object. All parameters are optional;
"any fields provided will entirely overwrite the existing values of those fields."

### DELETE /applications/{application.id}/commands/{command.id}
Deletes a global command. Returns `204 No Content` on success.

### PUT /applications/{application.id}/commands
Bulk overwrite global application commands.

> Takes a list of application commands, overwriting the existing global command list for this
> application. Returns `200` and a list of application command objects. Commands that do not already
> exist will count toward daily application command create limits.

> This will overwrite **all** types of application commands: slash commands, user commands, and
> message commands.

### GET /applications/{application.id}/guilds/{guild.id}/commands
Fetch all of the guild commands for your application for a specific guild. Same
`with_localizations?` query param and the same localization warning as the global variant.

### POST /applications/{application.id}/guilds/{guild.id}/commands
Create a new guild command. **"New guild commands will be available in the guild immediately."**
Returns `201` / `200` with the same upsert semantics.

> Creating a command with the same name as an existing command for your application will overwrite the old command.

### GET /applications/{application.id}/guilds/{guild.id}/commands/{command.id}
Fetch a guild command for your application.

### PATCH /applications/{application.id}/guilds/{guild.id}/commands/{command.id}
Edit a guild command. **"Updates for guild commands will be available immediately."** All parameters
optional; provided fields entirely overwrite.

### DELETE /applications/{application.id}/guilds/{guild.id}/commands/{command.id}
Delete a guild command. Returns `204 No Content` on success.

### PUT /applications/{application.id}/guilds/{guild.id}/commands
Bulk overwrite guild application commands.

> Takes a list of application commands, overwriting the existing command list for this application
> for the targeted guild. Returns `200` and a list of application command objects.

> This will overwrite **all** types of application commands: slash commands, user commands, and
> message commands.

The `handler?` field appears in the create/edit params and is worth knowing about because Discord
creates one such command for you when you enable Activities: "Determines whether the interaction is
handled by the app's interactions handler or by Discord. Only for `PRIMARY_ENTRY_POINT` commands."

The complete JSON params tables for every one of these endpoints belong to `discord-interactions`;
call the Skill tool with "discord-interactions" for them.

## Contexts: `integration_types` and `contexts`

> Commands have two sets of contexts on the application command object that let you to configure when
> and where it can be used:
>
> * `integration_types` defines the **installation contexts** that a command supports
> * `contexts` defines the **interaction contexts** where a command can be used

> Contexts are distinct from, and do not affect, any command permissions for apps installed to a server.

From the object structure table:

| Field | Type | Description |
|---|---|---|
| `integration_types?` | list of integration types | Installation contexts where the command is available, **only for globally-scoped commands**. Defaults to your app's configured contexts |
| `contexts?` | ?list of interaction context types | Interaction context(s) where the command can be used, **only for globally-scoped commands** |
| `dm_permission?` | boolean | **Deprecated (use `contexts` instead)**; Indicates whether the command is available in DMs with the app, only for globally-scoped commands. By default, commands are visible. |

**Both fields are global-only.** A guild-scoped command cannot carry `integration_types` or
`contexts` — another reason a fast guild-scoped loop is not a complete rehearsal of the global
behaviour.

> A command's supported installation context(s) can be set using the `integration_types` field when
> creating or updating a command as long as any included contexts are already supported on the
> application-level.

> A command's value for `integration_types` may affect which interaction contexts a command is
> visible in.

> There are three interaction context types that correspond to different surfaces: `GUILD` (`0`),
> `BOT_DM` (`1`), and `PRIVATE_CHANNEL` (`2`). However, the `PRIVATE_CHANNEL` interaction context is
> only meaningful for commands installed to a user (when the command's `integration_types` includes
> `USER_INSTALL`).

> The supported installation contexts for a command affects which interaction contexts you can set.
> Specifically, the `PRIVATE_CHANNEL` interaction context can only be included in `contexts` if
> `USER_INSTALL` is included in `integration_types` for the command.

On bulk overwrite, `contexts` "defaults to all contexts `[0,1,2]`."

The user-installable tutorial's four-command matrix, which is the clearest worked example of testing
across contexts:

| Name | Description | Installation Contexts (`integration_types`) | Interaction Contexts (`contexts`) |
| -------------- | ------------------------------------------------------ | ------------------------------------------- | ------------------------------------ |
| `/leaderboard` | View game leaderboard for the current server | `GUILD_INSTALL` | `GUILD` |
| `/wiki` | Find information about game items and characters | `GUILD_INSTALL`, `USER_INSTALL` | `GUILD`, `BOT_DM`, `PRIVATE_CHANNEL` |
| `/profile` | Get information about your game inventory and progress | `USER_INSTALL` | `GUILD`, `BOT_DM`, `PRIVATE_CHANNEL` |
| `/link` | Link your game account to Discord | `USER_INSTALL` | `BOT_DM` |

And the expected result after registering them — a concrete checklist for verifying context
configuration by eye:

> * In **channels within the guild you installed your app**, you should see `/leaderboard`, `/wiki`, and `/profile`
> * In **channels within any of your guilds**, you should see `/wiki` and `/profile`
> * In **your app's DM**, you should see `/wiki`, `/profile`, and `link`
> * And finally, **in DMs or GDMs with other users**, you should see `/wiki` and `/profile`

## Default permissions

> Default permissions can be added to a command during creation using the `default_member_permissions`
> and `context` fields. Adding default permissions doesn't require any Bearer token since it's
> configured during command creation and isn't targeting specific roles, users, or channels.

> The `default_member_permissions` field can be used when creating a command to set the permissions a
> user must have to use it. The value for `default_member_permissions` is a bitwise OR-ed set of
> permissions, serialized as a string. Setting it to `"0"` will prohibit anyone in a guild from using
> the command unless a specific overwrite is configured or the user has admin permissions.

> You can also include `BOT_DM` (`1`) in `contexts` when setting a global command's interaction
> contexts to control whether it can be run in DMs with your app. Guild commands don't support the
> `BOT_DM` interaction context.

Admin-only example:

```json
{
    "name": "permissions_test",
    "description": "A test of default permissions",
    "type": 1,
    "default_member_permissions": "0"
}
```

`MANAGE_GUILD`-only example:

```py
permissions = str(1 << 5)

command = {
    "name": "permissions_test",
    "description": "A test of default permissions",
    "type": 1,
    "default_member_permissions": permissions
```

**A command you cannot see may be permissions, not registration.** Upstream: "If you don't have
permission to use a command, it will not show up in the command picker. Members with the
Administrator permission can use all commands." So an invisible command is not proof the
registration call failed — check `GET` on the scope before re-registering.

Command permissions also inherit into threads: "any command permissions for a channel will apply to
the threads it contains."

## Retrieving localized commands

> While most endpoints that return application command objects will return the `name_localizations`
> and `description_localizations` fields, some will not by default. This includes `GET` endpoints
> that return all of an application's guild or global commands. Instead, those endpoints will supply
> additional `name_localized` or `description_localized` fields, which only contain the localization
> relevant to the requester's locale. (The full dictionaries can still be obtained by supplying the
> appropriate query argument).

So when you `GET` your registered commands to check what actually landed, the shape differs from what
you `POST`ed unless you pass `with_localizations=true`.

## What the sample apps do

**The Getting Started app** registers globally via bulk overwrite:

> The project contains a `register` script you can use to install the commands in `ALL_COMMANDS`,
> which is defined at the bottom of `commands.js`. It installs the commands as global commands by
> calling the HTTP API's `PUT /applications/<APP_ID>/commands` endpoint.

```
npm run register
```

> If you navigate back to your server, you should see the slash commands appear. But if you try to
> run them, nothing will happen since your app isn't receiving or handling any requests from Discord.

That sentence is the key diagnostic split: **commands appearing proves registration worked;
commands doing nothing points at the endpoint, not the registration.**

> To install slash commands, the app is using [`node-fetch`](https://github.com/node-fetch/node-fetch).
> You can see the implementation for the installation in `utils.js` within the `DiscordRequest()`
> function.

**The user-installable app** uses the per-command create endpoint:

> The register command will call the Create Global Application Command endpoint for each of the
> command payloads in `commands.js`.

and after registering: "However, if you try to run any of the commands, you'll get an error :(" —
again the same split.

**The Cloudflare Workers app** keeps command definitions in `commands.js`:

```js
export const AWW_COMMAND = {
  name: 'awwww',
  description: 'Drop some cuteness on this channel.',
};

export const INVITE_COMMAND = {
  name: 'invite',
  description: 'Get an invite link to add the bot to your server',
};
```

and registers them from a standalone script, verbatim:

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

Run once, before anything else:

```
$ DISCORD_TOKEN=**** DISCORD_APPLICATION_ID=**** node src/register.js
```

Note the pattern worth copying: the script **fails loudly on a missing environment variable** and
**prints the response body on a non-`ok` response**. That response body is where Discord's `50035`
form errors describing an invalid command payload appear.

The tutorial names the guild alternative even though it does not use it:

> Commands can be registered globally, making them available for all servers with the app installed,
> or they can be registered on a single server.
>
> In this example - we'll just focus on global commands

## Where the documentation is silent

- **No propagation time for global commands.** There is no number. Only the read-repair mechanism
  and the `o(minutes)` code comment.
- **No client-side cache-clearing procedure.** Upstream never tells you to restart the Discord
  client or use `Ctrl+R` to see new commands. It says guild commands are immediate and global
  commands read-repair. If a command does not appear, the documented things to check are
  registration success, command permissions, and context configuration.
- **No documented promote-from-guild-to-global workflow.** The docs recommend guild for testing and
  global for release but describe no migration step, and do not say to delete the guild copy — even
  though they confirm both can coexist under the same name.
- **No stated way to see the daily create counter.** The 200-per-day limit exists with no documented
  header or endpoint reporting remaining quota. Standard `X-RateLimit-*` headers are documented
  generally; upstream does not say they cover this limit.

## Source

Retrieved 2026-08-26 from:

- `docs.discord.com/developers/interactions/application-commands`
- `docs.discord.com/developers/interactions/receiving-and-responding`
- `docs.discord.com/developers/quick-start/getting-started`
- `docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers`
- `docs.discord.com/developers/tutorials/developing-a-user-installable-app`
- `docs.discord.com/developers/resources/application`
