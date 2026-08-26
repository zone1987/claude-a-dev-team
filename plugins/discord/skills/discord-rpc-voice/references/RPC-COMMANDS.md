# Discord RPC Commands

Every RPC command: exact `cmd` name, argument structure, response structure, and the upstream's own
example payloads verbatim. Commands are requests made to the RPC socket by a client.

Upstream warning: "The structure of responses from the RPC server is similar to the HTTP API but may
not be exactly equivalent."

## Contents

- [RPC commands table](#rpc-commands-table)
- [AUTHORIZE](#authorize)
- [AUTHENTICATE](#authenticate)
- [GET_GUILDS](#get_guilds)
- [GET_GUILD](#get_guild)
- [GET_CHANNEL](#get_channel)
- [GET_CHANNELS](#get_channels)
- [SET_USER_VOICE_SETTINGS](#set_user_voice_settings)
- [SELECT_VOICE_CHANNEL](#select_voice_channel)
- [GET_SELECTED_VOICE_CHANNEL](#get_selected_voice_channel)
- [SELECT_TEXT_CHANNEL](#select_text_channel)
- [GET_VOICE_SETTINGS](#get_voice_settings)
- [SET_VOICE_SETTINGS](#set_voice_settings)
- [SUBSCRIBE](#subscribe)
- [UNSUBSCRIBE](#unsubscribe)
- [SET_CERTIFIED_DEVICES](#set_certified_devices)
- [SET_ACTIVITY](#set_activity)
- [SEND_ACTIVITY_JOIN_INVITE](#send_activity_join_invite)
- [CLOSE_ACTIVITY_REQUEST](#close_activity_request)

## RPC commands table

| Name                        | Description                                                     |
| --------------------------- | --------------------------------------------------------------- |
| DISPATCH                    | event dispatch                                                  |
| AUTHORIZE                   | used to authorize a new client with your app                    |
| AUTHENTICATE                | used to authenticate an existing client with your app           |
| GET_GUILD                   | used to retrieve guild information from the client              |
| GET_GUILDS                  | used to retrieve a list of guilds from the client               |
| GET_CHANNEL                 | used to retrieve channel information from the client            |
| GET_CHANNELS                | used to retrieve a list of channels for a guild from the client |
| SUBSCRIBE                   | used to subscribe to an RPC event                               |
| UNSUBSCRIBE                 | used to unsubscribe from an RPC event                           |
| SET_USER_VOICE_SETTINGS     | used to change voice settings of users in voice channels        |
| SELECT_VOICE_CHANNEL        | used to join or leave a voice channel, group dm, or dm          |
| GET_SELECTED_VOICE_CHANNEL  | used to get the current voice channel the client is in          |
| SELECT_TEXT_CHANNEL         | used to join or leave a text channel, group dm, or dm           |
| GET_VOICE_SETTINGS          | used to retrieve the client's voice settings                    |
| SET_VOICE_SETTINGS          | used to set the client's voice settings                         |
| SET_CERTIFIED_DEVICES       | used to send info about certified hardware devices              |
| SET_ACTIVITY                | used to update a user's Rich Presence                           |
| SEND_ACTIVITY_JOIN_INVITE   | used to consent to a Rich Presence Ask to Join request          |
| CLOSE_ACTIVITY_REQUEST      | used to reject a Rich Presence Ask to Join request              |

`DISPATCH` appears in the command table but is the `cmd` value the server uses when pushing an event;
see RPC-EVENTS.md.

## AUTHORIZE

Used to authenticate a new client with your app. By default this pops up a modal in-app that asks the
user to authorize access to your app.

**Discord currently does not allow access to RPC for unapproved apps without being on the game's list
of testers.** Discord grants 50 testing spots, which should be ample for development. After approval,
this restriction is removed and your app will be accessible to anyone.

Discord also has an RPC token system to bypass the user authorization modal. This is usable by
approved games as well as by users on a game's list of testers, and also disallows use of the
`messages.read` scope. If you have been granted access, you can send a POST request to
`https://discord.com/api/oauth2/token/rpc` with your application's `client_id` and `client_secret` in
the body (sent as a url-encoded body, **not JSON**). You can then pass the returned `rpc_token` value
to the `rpc_token` field in your RPC authorize request.

###### Authorize Argument Structure

| Field      | Type                    | Description                                                               |
| ---------- | ----------------------- | ------------------------------------------------------------------------- |
| scopes     | array of OAuth2 scopes  | scopes to authorize                                                       |
| client_id  | string                  | OAuth2 application id                                                     |
| rpc_token  | string                  | one-time use RPC token                                                    |
| username   | string                  | username to create a guest account with if the user does not have Discord |

OAuth2 scope values: call the Skill tool with `"discord-oauth2"`.

###### Authorize Response Structure

| Field | Type   | Description               |
| ----- | ------ | ------------------------- |
| code  | string | OAuth2 authorization code |

###### Example Authorize Command Payload

```json
{
  "nonce": "f48f6176-4afb-4c03-b1b8-d960861f5216",
  "args": {
    "client_id": "192741864418312192",
    "scopes": ["rpc", "identify"]
  },
  "cmd": "AUTHORIZE"
}
```

###### Example Authorize Response Payload

```json
{
  "cmd": "AUTHORIZE",
  "data": {
    "code": "O62Q9JzFe8BEOUzIfsAndOjNd2V4sJ"
  },
  "nonce": "f48f6176-4afb-4c03-b1b8-d960861f5216"
}
```

## AUTHENTICATE

Used to authenticate an existing client with your app.

###### Authenticate Argument Structure

| Field        | Type   | Description         |
| ------------ | ------ | ------------------- |
| access_token | string | OAuth2 access token |

###### Authenticate Response Structure

| Field       | Type                        | Description                     |
| ----------- | --------------------------- | ------------------------------- |
| user        | partial user object         | the authed user                 |
| scopes      | array of OAuth2 scopes      | authorized scopes               |
| expires     | date                        | expiration date of OAuth2 token |
| application | OAuth2 application object   | application the user authorized |

###### OAuth2 Application Structure

| Field       | Type             | Description              |
| ----------- | ---------------- | ------------------------ |
| description | string           | application description  |
| icon        | string           | hash of the icon         |
| id          | snowflake        | application client id    |
| rpc_origins | array of strings | array of rpc origin urls |
| name        | string           | application name         |

###### Example Authenticate Command Payload

```json
{
  "nonce": "5bb10a43-1fdc-4391-9512-0c8f4aa203d4",
  "args": {
    "access_token": "EXAMPLE_BEARER_TOKEN_REDACTED"
  },
  "cmd": "AUTHENTICATE"
}
```

###### Example Authenticate Response Payload

```json
{
  "cmd": "AUTHENTICATE",
  "data": {
    "application": {
      "description": "test app description",
      "icon": "d6b51c21c48482d5b64aa4832d92fe14",
      "id": "192741864418312192",
      "rpc_origins": ["http://localhost:3344"],
      "name": "test app"
    },
    "expires": "2017-06-29T19:09:52.361000+00:00",
    "user": {
      "username": "test user",
      "discriminator": "7479",
      "id": "190320984123768832",
      "avatar": "b004ec1740a63ca06ae2e14c5cee11f3"
    },
    "scopes": ["rpc", "identify"]
  },
  "nonce": "5bb10a43-1fdc-4391-9512-0c8f4aa203d4"
}
```

## GET_GUILDS

Used to get a list of guilds the client is in.

###### Get Guilds Response Structure

| Field  | Type                            | Description               |
| ------ | ------------------------------- | ------------------------- |
| guilds | array of partial guild objects  | the guilds the user is in |

###### Example Get Guilds Command Payload

```json
{
  "nonce": "e16fcbed-8bfa-4fd4-ba09-73b72e809833",
  "args": {},
  "cmd": "GET_GUILDS"
}
```

###### Example Get Guilds Response Payload

```json
{
  "cmd": "GET_GUILDS",
  "data": {
    "guilds": [
      {
        "id": "199737254929760256",
        "name": "test"
      }
    ]
  },
  "nonce": "e16fcbed-8bfa-4fd4-ba09-73b72e809833"
}
```

## GET_GUILD

Used to get a guild the client is in.

###### Get Guild Argument Structure

| Field    | Type    | Description                                                  |
| -------- | ------- | ------------------------------------------------------------ |
| guild_id | string  | id of the guild to get                                       |
| timeout  | integer | asynchronously get guild with time to wait before timing out |

A timeout produces RPC error `5002` (`GET_GUILD` timed out).

###### Get Guild Response Structure

| Field    | Type                          | Description                                           |
| -------- | ----------------------------- | ----------------------------------------------------- |
| id       | string                        | guild id                                              |
| name     | string                        | guild name                                            |
| icon_url | string                        | guild icon url                                        |
| members  | array of guild member objects | members of the guild (deprecated; always empty array) |

###### Example Get Guild Command Payload

```json
{
  "nonce": "9524922c-3d32-413a-bdaa-0804f4332588",
  "args": {
    "guild_id": "199737254929760256"
  },
  "cmd": "GET_GUILD"
}
```

###### Example Get Guild Response Payload

```json
{
  "cmd": "GET_GUILD",
  "data": {
    "id": "199737254929760256",
    "name": "test",
    "icon_url": null,
    "members": []
  },
  "nonce": "9524922c-3d32-413a-bdaa-0804f4332588"
}
```

## GET_CHANNEL

Used to get a channel the client is in.

###### Get Channel Argument Structure

| Field      | Type   | Description              |
| ---------- | ------ | ------------------------ |
| channel_id | string | id of the channel to get |

###### Get Channel Response Structure

| Field        | Type                         | Description                                                      |
| ------------ | ---------------------------- | ---------------------------------------------------------------- |
| id           | string                       | channel id                                                       |
| guild_id     | string                       | channel's guild id                                               |
| name         | string                       | channel name                                                     |
| type         | integer                      | channel type (guild text: 0, guild voice: 2, dm: 1, group dm: 3) |
| topic        | string                       | (text) channel topic                                             |
| bitrate      | integer                      | (voice) bitrate of voice channel                                 |
| user_limit   | integer                      | (voice) user limit of voice channel (0 for none)                 |
| position     | integer                      | position of channel in channel list                              |
| voice_states | array of voice state objects | (voice) channel's voice states                                   |
| messages     | array of message objects     | (text) channel's messages                                        |

###### Example Get Channel Command Payload

```json
{
  "nonce": "f682697e-d257-4a17-ac0a-7e4b84e66663",
  "args": {
    "channel_id": "199737254929760257"
  },
  "cmd": "GET_CHANNEL"
}
```

###### Example Get Channel Response Payload

```json
{
  "cmd": "GET_CHANNEL",
  "data": {
    "id": "199737254929760257",
    "name": "General",
    "type": 2,
    "bitrate": 64000,
    "user_limit": 0,
    "guild_id": "199737254929760256",
    "position": 0,
    "voice_states": [
      {
        "voice_state": {
          "mute": false,
          "deaf": false,
          "self_mute": false,
          "self_deaf": false,
          "suppress": false
        },
        "user": {
          "id": "190320984123768832",
          "username": "test 2",
          "discriminator": "7479",
          "avatar": "b004ec1740a63ca06ae2e14c5cee11f3",
          "bot": false
        },
        "nick": "test user 2",
        "volume": 110,
        "mute": false,
        "pan": {
          "left": 1.0,
          "right": 1.0
        }
      }
    ]
  },
  "nonce": "f682697e-d257-4a17-ac0a-7e4b84e66663"
}
```

## GET_CHANNELS

Used to get a guild's channels the client is in.

###### Get Channels Argument Structure

| Field    | Type   | Description                         |
| -------- | ------ | ----------------------------------- |
| guild_id | string | id of the guild to get channels for |

###### Get Channels Response Structure

| Field    | Type                             | Description                   |
| -------- | -------------------------------- | ----------------------------- |
| channels | array of partial channel objects | guild channels the user is in |

###### Example Get Channels Command Payload

```json
{
  "nonce": "0dee7bd4-8f62-4ecc-9e0f-1b1839a4fa93",
  "args": {
    "guild_id": "199737254929760256"
  },
  "cmd": "GET_CHANNELS"
}
```

###### Example Get Channels Response Payload

```json
{
  "cmd": "GET_CHANNELS",
  "data": {
    "channels": [
      {
        "id": "199737254929760256",
        "name": "general",
        "type": 0
      },
      {
        "id": "199737254929760257",
        "name": "General",
        "type": 2
      }
    ]
  },
  "nonce": "0dee7bd4-8f62-4ecc-9e0f-1b1839a4fa93"
}
```

## SET_USER_VOICE_SETTINGS

Used to change voice settings of users in voice channels.

###### Set User Voice Settings Argument and Response Structure

| Field    | Type        | Description                                              |
| -------- | ----------- | -------------------------------------------------------- |
| user_id  | string      | user id                                                  |
| pan?     | pan object  | set the pan of the user                                  |
| volume?  | integer     | set the volume of user (defaults to 100, min 0, max 200) |
| mute?    | boolean     | set the mute state of the user                           |

Upstream note (verbatim): "In the current release, we only support a single modifier of voice settings
at a time over RPC. If an app changes voice settings, it will lock voice settings so that other apps
connected simultaneously lose the ability to change voice settings. Settings reset to what they were
before being changed after the controlling app disconnects. When an app that has previously set voice
settings connects, the client will swap to that app's configured voice settings and lock voice
settings again. This is a temporary situation that will be changed in the future."

###### Pan Object

| Field | Type  | Description                            |
| ----- | ----- | -------------------------------------- |
| left  | float | left pan of user (min: 0.0, max: 1.0)  |
| right | float | right pan of user (min: 0.0, max: 1.0) |

###### Example Set User Voice Settings Command Payload

```json
{
  "nonce": "eafc8152-2248-4478-9827-8457b7900cb4",
  "args": {
    "user_id": "192731515703001088",
    "pan": {
      "left": 1.0,
      "right": 1.0
    },
    "volume": 120,
    "mute": false
  },
  "cmd": "SET_USER_VOICE_SETTINGS"
}
```

###### Example Set User Voice Settings Response Payload

```json
{
  "cmd": "SET_USER_VOICE_SETTINGS",
  "data": {
    "user_id": "192731515703001088",
    "pan": {
      "left": 1.0,
      "right": 1.0
    },
    "volume": 120,
    "mute": false
  },
  "nonce": "eafc8152-2248-4478-9827-8457b7900cb4"
}
```

## SELECT_VOICE_CHANNEL

Used to join and leave voice channels, group dms, or dms. Returns the [GET_CHANNEL](#get_channel)
response, `null` if none.

###### Select Voice Channel Argument Structure

| Field      | Type    | Description                                                     |
| ---------- | ------- | --------------------------------------------------------------- |
| channel_id | string  | channel id to join (or `null` to leave)                         |
| timeout    | integer | asynchronously join channel with time to wait before timing out |
| force      | boolean | forces a user to join a voice channel                           |
| navigate   | boolean | after joining the voice channel, navigate to it in the client   |

Upstream warning: "When trying to join the user to a voice channel, you will receive a `5003` error
coded response if the user is already in a voice channel. The `force` parameter should only be
specified in response to the case where a user is already in a voice channel and they have
**approved** to be moved by your app to a new voice channel."

A timeout produces RPC error `5001` (Select channel timed out).

###### Example Select Voice Channel Command Payload

```json
{
  "nonce": "5d9df76d-6408-46a1-9368-33dca74fa423",
  "args": {
    "channel_id": "199737254929760257"
  },
  "cmd": "SELECT_VOICE_CHANNEL"
}
```

###### Example Select Voice Channel Response Payload

```json
{
  "cmd": "SELECT_VOICE_CHANNEL",
  "data": {
    "id": "199737254929760257",
    "name": "General",
    "type": 2,
    "bitrate": 64000,
    "user_limit": 0,
    "guild_id": "199737254929760256",
    "position": 0,
    "voice_states": [
      {
        "voice_state": {
          "mute": false,
          "deaf": false,
          "self_mute": false,
          "self_deaf": false,
          "suppress": false
        },
        "user": {
          "id": "190320984123768832",
          "username": "test 2",
          "discriminator": "7479",
          "avatar": "b004ec1740a63ca06ae2e14c5cee11f3",
          "bot": false
        },
        "nick": "test user 2",
        "mute": false,
        "volume": 110,
        "pan": {
          "left": 1.0,
          "right": 1.0
        }
      }
    ]
  },
  "nonce": "5d9df76d-6408-46a1-9368-33dca74fa423"
}
```

## GET_SELECTED_VOICE_CHANNEL

Used to get the client's current voice channel. **There are no arguments for this command.** Returns
the [GET_CHANNEL](#get_channel) response, or `null` if none.

## SELECT_TEXT_CHANNEL

Used to join and leave text channels, group dms, or dms. Returns the [GET_CHANNEL](#get_channel)
response, or `null` if none.

###### Select Text Channel Argument Structure

| Field      | Type    | Description                                                     |
| ---------- | ------- | --------------------------------------------------------------- |
| channel_id | string  | channel id to join (or `null` to leave)                         |
| timeout    | integer | asynchronously join channel with time to wait before timing out |

A timeout produces RPC error `5001` (Select channel timed out).

## GET_VOICE_SETTINGS

The upstream page states no arguments and no prose for this command beyond its response structures.

###### Get Voice Settings Response Structure

| Field                   | Type                        | Description                       |
| ----------------------- | --------------------------- | --------------------------------- |
| input                   | voice settings input object  | input settings                    |
| output                  | voice settings output object | output settings                   |
| mode                    | voice settings mode object   | voice mode settings               |
| automatic_gain_control  | boolean                     | state of automatic gain control   |
| echo_cancellation       | boolean                     | state of echo cancellation        |
| noise_suppression       | boolean                     | state of noise suppression        |
| qos                     | boolean                     | state of voice quality of service |
| silence_warning         | boolean                     | state of silence warning notice   |
| deaf                    | boolean                     | state of self-deafen              |
| mute                    | boolean                     | state of self-mute                |

###### Voice Settings Input Object

| Field             | Type             | Description                                                                |
| ----------------- | ---------------- | -------------------------------------------------------------------------- |
| device_id         | string           | device id                                                                  |
| volume            | float            | input voice level (min: 0, max: 100)                                       |
| available_devices | array of objects | array of *read-only* device objects containing `id` and `name` string keys |

###### Voice Settings Output Object

| Field             | Type             | Description                                                                |
| ----------------- | ---------------- | -------------------------------------------------------------------------- |
| device_id         | string           | device id                                                                  |
| volume            | float            | output voice level (min: 0, max: 200)                                      |
| available_devices | array of objects | array of *read-only* device objects containing `id` and `name` string keys |

###### Voice Settings Mode Object

| Field          | Type                     | Description                                                         |
| -------------- | ------------------------ | ------------------------------------------------------------------- |
| type           | string                   | voice setting mode type (can be `PUSH_TO_TALK` or `VOICE_ACTIVITY`) |
| auto_threshold | boolean                  | voice activity threshold automatically sets its threshold           |
| threshold      | float                    | threshold for voice activity (in dB) (min: -100, max: 0)            |
| shortcut       | shortcut key combo object | shortcut key combos for PTT                                         |
| delay          | float                    | the PTT release delay (in ms) (min: 0, max: 2000)                   |

###### Shortcut Key Combo Object

| Field | Type    | Description        |
| ----- | ------- | ------------------ |
| type  | integer | see key types      |
| code  | integer | key code           |
| name  | string  | key name           |

###### Key Types

| Type                  | Id |
| --------------------- | -- |
| KEYBOARD_KEY          | 0  |
| MOUSE_BUTTON          | 1  |
| KEYBOARD_MODIFIER_KEY | 2  |
| GAMEPAD_BUTTON        | 3  |

Attempting to capture more than one shortcut key at once produces RPC error `5004` (Capture shortcut
already listening).

###### Example Get Voice Settings Response Payload

```json
{
  "cmd": "GET_VOICE_SETTINGS",
  "data": {
    "input": {
      "available_devices": [
        {
          "id": "default",
          "name": "Default"
        },
        {
          "id": "Built-in Microphone",
          "name": "Built-in Microphone"
        }
      ],
      "device_id": "default",
      "volume": 49.803921580314636
    },
    "output": {
      "available_devices": [
        {
          "id": "default",
          "name": "Default"
        },
        {
          "id": "Built-in Output",
          "name": "Built-in Output"
        }
      ],
      "device_id": "default",
      "volume": 93.00000071525574
    },
    "mode": {
      "type": "VOICE_ACTIVITY",
      "auto_threshold": true,
      "threshold": -46.92622950819673,
      "shortcut": [{ "type": 0, "code": 12, "name": "i" }],
      "delay": 98.36065573770492
    },
    "automatic_gain_control": false,
    "echo_cancellation": false,
    "noise_suppression": false,
    "qos": false,
    "silence_warning": false,
    "deaf": false,
    "mute": false
  },
  "nonce": "fa07c532-bb03-4f75-8b9a-397f5109afb6"
}
```

Note the example shows `shortcut` as an **array** of shortcut key combo objects, while the Voice
Settings Mode Object table types it as a single object. Both are as upstream states them.

## SET_VOICE_SETTINGS

Upstream note (verbatim): "In the current release, we only support a single modifier of voice settings
at a time over RPC. If an app changes voice settings, it will lock voice settings so that other apps
connected simultaneously lose the ability to change voice settings. Settings reset to what they were
before being changed after the controlling app disconnects. When an app that has previously set voice
settings connects, the client will swap to that app's configured voice settings and lock voice
settings again. This is a temporary situation that will be changed in the future."

**When setting voice settings, all fields are optional. Only passed fields are updated.**

###### Set Voice Settings Argument and Response Structure

| Field                   | Type                        | Description                       |
| ----------------------- | --------------------------- | --------------------------------- |
| input                   | voice settings input object  | input settings                    |
| output                  | voice settings output object | output settings                   |
| mode                    | voice settings mode object   | voice mode settings               |
| automatic_gain_control  | boolean                     | state of automatic gain control   |
| echo_cancellation       | boolean                     | state of echo cancellation        |
| noise_suppression       | boolean                     | state of noise suppression        |
| qos                     | boolean                     | state of voice quality of service |
| silence_warning         | boolean                     | state of silence warning notice   |
| deaf                    | boolean                     | state of self-deafen              |
| mute                    | boolean                     | state of self-mute                |

Sub-object shapes are identical to [GET_VOICE_SETTINGS](#get_voice_settings).

###### Example Set Voice Settings Command Payload

```json
{
  "nonce": "3d64ed55-ef6e-4bd5-99c9-677533babc22",
  "args": {
    "input": {
      "volume": 90.5
    }
  },
  "cmd": "SET_VOICE_SETTINGS"
}
```

###### Example Set Voice Settings Response Payload

```json
{
  "cmd": "SET_VOICE_SETTINGS",
  "data": {
    "input": {
      "available_devices": [
        {
          "id": "default",
          "name": "Default"
        },
        {
          "id": "Built-in Microphone",
          "name": "Built-in Microphone"
        }
      ],
      "device_id": "default",
      "volume": 90.5
    },
    "output": {
      "available_devices": [
        {
          "id": "default",
          "name": "Default"
        },
        {
          "id": "Built-in Output",
          "name": "Built-in Output"
        }
      ],
      "device_id": "default",
      "volume": 93.00000071525574
    },
    "mode": {
      "type": "VOICE_ACTIVITY",
      "auto_threshold": true,
      "threshold": -46.92622950819673,
      "shortcut": [{ "type": 0, "code": 12, "name": "i" }],
      "delay": 98.36065573770492
    },
    "automatic_gain_control": false,
    "echo_cancellation": false,
    "noise_suppression": false,
    "qos": false,
    "silence_warning": false,
    "deaf": false,
    "mute": false
  },
  "nonce": "3d64ed55-ef6e-4bd5-99c9-677533babc22"
}
```

## SUBSCRIBE

Used to subscribe to events. `evt` of the payload should be set to the event being subscribed to.
`args` of the payload should be set to the args needed for the event.

###### Subscribe Response Structure

| Field | Type   | Description                  |
| ----- | ------ | ---------------------------- |
| evt   | string | event name now subscribed to |

###### Example Subscribe Command Payload

```json
{
  "nonce": "be9a6de3-31d0-4767-a8e9-4818c5690015",
  "args": {
    "guild_id": "199737254929760256"
  },
  "evt": "GUILD_STATUS",
  "cmd": "SUBSCRIBE"
}
```

###### Example Subscribe Response Payload

```json
{
  "cmd": "SUBSCRIBE",
  "data": {
    "evt": "GUILD_STATUS"
  },
  "nonce": "be9a6de3-31d0-4767-a8e9-4818c5690015"
}
```

An invalid event name produces RPC error `4004` (Invalid event).

## UNSUBSCRIBE

Used to unsubscribe from events. `evt` of the payload should be set to the event that was subscribed
to. `args` of the payload should be set to the args needed for the previously subscribed event.

###### Unsubscribe Response Structure

| Field | Type   | Description                      |
| ----- | ------ | -------------------------------- |
| evt   | string | event name now unsubscribed from |

###### Example Unsubscribe Command Payload

```json
{
  "nonce": "647d814a-4cf8-4fbb-948f-898aad24f55b",
  "args": {
    "guild_id": "199737254929760256"
  },
  "evt": "GUILD_STATUS",
  "cmd": "UNSUBSCRIBE"
}
```

###### Example Unsubscribe Response Payload

```json
{
  "cmd": "UNSUBSCRIBE",
  "data": {
    "evt": "GUILD_STATUS"
  },
  "nonce": "647d814a-4cf8-4fbb-948f-898aad24f55b"
}
```

## SET_CERTIFIED_DEVICES

Used by hardware manufacturers to send information about the current state of their certified devices
that are connected to Discord. Full program guide, HTTP transport variant and UUID retrieval:
CERTIFIED-DEVICES.md.

###### Set Certified Devices Argument Structure

| Field   | Type                             | Description                                                   |
| ------- | -------------------------------- | ------------------------------------------------------------- |
| devices | array of certified device objects | a list of devices for your manufacturer, in order of priority |

###### Device Object

| Field                     | Type        | Description                                              |
| ------------------------- | ----------- | -------------------------------------------------------- |
| type                      | device type | the type of device                                       |
| id                        | string      | the device's Windows UUID                                |
| vendor                    | vendor object | the hardware vendor                                    |
| model                     | model object  | the model of the product                               |
| related                   | array of strings | UUIDs of related devices                            |
| echo_cancellation?\*      | boolean     | if the device's native echo cancellation is enabled      |
| noise_suppression?\*      | boolean     | if the device's native noise suppression is enabled      |
| automatic_gain_control?\* | boolean     | if the device's native automatic gain control is enabled |
| hardware_mute?\*          | boolean     | if the device is hardware muted                          |

\*These fields are only applicable for `AUDIO_INPUT` device types

###### Vendor Object

| Field | Type   | Description        |
| ----- | ------ | ------------------ |
| name  | string | name of the vendor |
| url   | string | url for the vendor |

###### Model Object

| Field | Type   | Description       |
| ----- | ------ | ----------------- |
| name  | string | name of the model |
| url   | string | url for the model |

###### Device Type

| Type         | Value         |
| ------------ | ------------- |
| AUDIO_INPUT  | "audioinput"  |
| AUDIO_OUTPUT | "audiooutput" |
| VIDEO_INPUT  | "videoinput"  |

###### Example Set Certified Devices Command Payload

```json
{
  "nonce": "9b4e9711-97f3-4f35-b047-32c82a51978e",
  "cmd": "SET_CERTIFIED_DEVICES",
  "args": {
    "devices": [
      {
        "type": "audioinput",
        "id": "aafc2003-da0e-42a3-b982-6a17a2812510",
        "vendor": {
          "name": "SteelSeries",
          "url": "https://steelseries.com"
        },
        "model": {
          "name": "Arctis 7",
          "url": "https://steelseries.com/gaming-headsets/arctis-7"
        },
        "related": ["aafc2003-da0e-42a3-b982-6a17a2819999"],
        "echo_cancellation": true,
        "noise_suppression": true,
        "automatic_gain_control": true,
        "hardware_mute": false
      }
    ]
  }
}
```

###### Example Set Certified Devices Response Payload

```json
{
  "nonce": "9b4e9711-97f3-4f35-b047-32c82a51978e",
  "cmd": "SET_CERTIFIED_DEVICES",
  "data": null,
  "evt": null
}
```

## SET_ACTIVITY

Used to update a user's Rich Presence.

Upstream note: "When using `SET_ACTIVITY`, the `activity` object is limited to a `type` of Playing
(`0`), Listening (`2`), Watching (`3`), or Competing (`5`)."

###### Set Activity Argument Structure

| Field    | Type            | Description                             |
| -------- | --------------- | --------------------------------------- |
| pid      | integer         | the application's process id            |
| activity | activity object | the rich presence to assign to the user |

The activity object is the Gateway activity object — call the Skill tool with `"discord-gateway"`.

###### Example Set Activity Payload

Reproduced verbatim; the upstream example embeds pseudo-code calls (`time(nullptr)`,
`GameEngine.GetPartyId()`) rather than literal JSON values.

```json
{
  "cmd": "SET_ACTIVITY",
  "args": {
    "pid": 9999,
    "activity": {
      "state": "In a Group",
      "state_url": "https://example.com/groups/50335231-9d9d-4ebd-873b-984787ee4d1d",
      "details": "Competitive | In a Match",
      "details_url": "https://example.com/matches/42340203-2f25-4534-8ff6-2a6509e81207",
      "timestamps": {
        "start": time(nullptr),
        "end": time(nullptr) + (60 * 5 + 23)
      },
      "assets": {
        "large_image": "numbani_map",
        "large_text": "Numbani",
        "large_url": "https://example.wiki/maps/Numbani",
        "small_image": "pharah_profile",
        "small_text": "Pharah",
        "small_url": "https://example.wiki/characters/Pharah"
      },
      "party": {
        "id": GameEngine.GetPartyId(),
        "size": [3, 6]
      },
      "secrets": {
        "join": "025ed05c71f639de8bfaa0d679d7c94b2fdce12f",
        "spectate": "e7eb30d2ee025ed05c71ea495f770b76454ee4e0",
        "match": "4b2fdce12f639de8bfa7e3591b71a0d679d7c93f"
      },
      "instance": true
    }
  },
  "nonce": "647d814a-4cf8-4fbb-948f-898abd24f55b"
}
```

The upstream page documents no response structure for `SET_ACTIVITY`.

## SEND_ACTIVITY_JOIN_INVITE

Used to accept an Ask to Join request.

###### Send Activity Join Invite Argument Structure

| Field   | Type      | Description                   |
| ------- | --------- | ----------------------------- |
| user_id | snowflake | the id of the requesting user |

###### Example Send Activity Join Invite Payload

```json
{
  "nonce": "5dc0c062-98c6-47a0-8922-15aerg126",
  "cmd": "SEND_ACTIVITY_JOIN_INVITE",
  "args": {
    "user_id": "53908232506183680"
  }
}
```

The upstream page documents no response structure for this command.

## CLOSE_ACTIVITY_REQUEST

Used to reject an Ask to Join request.

###### Close Activity Request Argument Structure

| Field   | Type      | Description                   |
| ------- | --------- | ----------------------------- |
| user_id | snowflake | the id of the requesting user |

###### Example Close Activity Request Payload

```json
{
  "nonce": "5dc0c062-98c6-47a0-8922-15aerg126",
  "cmd": "CLOSE_ACTIVITY_REQUEST",
  "args": {
    "user_id": "53908232506183680"
  }
}
```

The upstream page documents no response structure for this command.

## Source

Discord Developer Documentation: <https://docs.discord.com/developers/topics/rpc>.
Error code numbers cross-referenced from
<https://docs.discord.com/developers/topics/opcodes-and-status-codes>.
Retrieved 2026-08-26.
