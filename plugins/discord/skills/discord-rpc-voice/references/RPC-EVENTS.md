# Discord RPC Events

Every RPC event: its subscription arguments, its dispatch data structure, and the upstream's own
example payloads verbatim. Events are payloads sent over the socket to a client that correspond to
events in Discord.

Subscribed events arrive with `cmd` set to `DISPATCH` and `evt` set to the event name. `READY` and
`ERROR` are non-subscription events. Subscribe and unsubscribe with the `SUBSCRIBE` /`UNSUBSCRIBE`
commands in RPC-COMMANDS.md.

## Contents

- [RPC events table](#rpc-events-table)
- [READY](#ready)
- [ERROR](#error)
- [CURRENT_USER_UPDATE](#current_user_update)
- [RELATIONSHIP_UPDATE](#relationship_update)
- [GUILD_STATUS](#guild_status)
- [GUILD_CREATE](#guild_create)
- [CHANNEL_CREATE](#channel_create)
- [VOICE_CHANNEL_SELECT](#voice_channel_select)
- [VOICE_STATE_CREATE / VOICE_STATE_UPDATE / VOICE_STATE_DELETE](#voice_state_create--voice_state_update--voice_state_delete)
- [VOICE_SETTINGS_UPDATE](#voice_settings_update)
- [VOICE_CONNECTION_STATUS](#voice_connection_status)
- [SPEAKING_START / SPEAKING_STOP](#speaking_start--speaking_stop)
- [MESSAGE_CREATE / MESSAGE_UPDATE / MESSAGE_DELETE](#message_create--message_update--message_delete)
- [NOTIFICATION_CREATE](#notification_create)
- [ACTIVITY_JOIN](#activity_join)
- [ACTIVITY_SPECTATE](#activity_spectate)
- [ACTIVITY_JOIN_REQUEST](#activity_join_request)
- [ACTIVITY_INVITE](#activity_invite)
- [ENTITLEMENT_CREATE](#entitlement_create)
- [ENTITLEMENT_DELETE](#entitlement_delete)

## RPC events table

| Name                    | Description                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| READY                   | non-subscription event sent immediately after connecting, contains server information      |
| ERROR                   | non-subscription event sent when there is an error, including command responses            |
| CURRENT_USER_UPDATE     | sent when the local user's data (avatar, username, etc.) changes                           |
| RELATIONSHIP_UPDATE     | sent when a relationship (friend, block, etc.) is added or removed                         |
| GUILD_STATUS            | sent when a subscribed server's state changes                                              |
| GUILD_CREATE            | sent when a guild is created/joined on the client                                           |
| CHANNEL_CREATE          | sent when a channel is created/joined on the client                                         |
| VOICE_CHANNEL_SELECT    | sent when the client joins a voice channel                                                 |
| VOICE_STATE_CREATE      | sent when a user joins a subscribed voice channel                                          |
| VOICE_STATE_UPDATE      | sent when a user's voice state changes in a subscribed voice channel (mute, volume, etc.)  |
| VOICE_STATE_DELETE      | sent when a user parts a subscribed voice channel                                          |
| VOICE_SETTINGS_UPDATE   | sent when the client's voice settings update                                               |
| VOICE_CONNECTION_STATUS | sent when the client's voice connection status changes                                     |
| SPEAKING_START          | sent when a user in a subscribed voice channel speaks                                      |
| SPEAKING_STOP           | sent when a user in a subscribed voice channel stops speaking                              |
| MESSAGE_CREATE          | sent when a message is created in a subscribed text channel                                |
| MESSAGE_UPDATE          | sent when a message is updated in a subscribed text channel                                |
| MESSAGE_DELETE          | sent when a message is deleted in a subscribed text channel                                |
| NOTIFICATION_CREATE     | sent when the client receives a notification (mention or new message in eligible channels) |
| ACTIVITY_JOIN           | sent when the user clicks a Rich Presence join invite in chat to join a game               |
| ACTIVITY_SPECTATE       | sent when the user clicks a Rich Presence spectate invite in chat to spectate a game       |
| ACTIVITY_JOIN_REQUEST   | sent when the user receives a Rich Presence Ask to Join request                            |
| ACTIVITY_INVITE         | sent when the user receives an activity invitation                                         |
| ENTITLEMENT_CREATE      | sent when a user purchases or receives a new entitlement (SKU/Game)                        |
| ENTITLEMENT_DELETE      | sent when an entitlement is removed                                                        |

## READY

###### Ready Dispatch Data Structure

| Field  | Type                              | Description                        |
| ------ | --------------------------------- | ---------------------------------- |
| v      | integer                           | RPC version                        |
| config | rpc server configuration object   | server configuration               |
| user   | partial user object               | the user to whom you are connected |

###### RPC Server Configuration Object

| Field        | Type   | Description           |
| ------------ | ------ | --------------------- |
| cdn_host     | string | server's cdn          |
| api_endpoint | string | server's api endpoint |
| environment  | string | server's environment  |

###### Example Ready Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "v": 1,
    "config": {
      "cdn_host": "cdn.discordapp.com",
      "api_endpoint": "//discord.com/api",
      "environment": "production"
    },
    "user": {
      "id": "53908232506183680",
      "username": "Mason",
      "discriminator": "1337",
      "avatar": null
    }
  },
  "evt": "READY"
}
```

## ERROR

###### Error Data Structure

| Field   | Type    | Description       |
| ------- | ------- | ----------------- |
| code    | integer | RPC Error Code    |
| message | string  | Error description |

The full numeric code list is in RPC-PROTOCOL.md.

###### Example Error Payload

```json
{
  "cmd": "AUTHORIZE",
  "data": {
    "code": 4007,
    "message": "No client id provided"
  },
  "evt": "ERROR",
  "nonce": "5102b6f0-c769-4f37-8cca-25fb0ab22628"
}
```

Note the `cmd` on an error is the command that failed, not `DISPATCH`.

## CURRENT_USER_UPDATE

No arguments. Dispatches the current user's profile whenever it changes (avatar, username, etc.).

###### Current User Update Dispatch Data Structure

| Field                  | Type    | Description                                                                                    |
| ---------------------- | ------- | ---------------------------------------------------------------------------------------------- |
| id                     | string  | user's id                                                                                      |
| username               | string  | user's username                                                                                |
| discriminator          | string  | user's discriminator                                                                           |
| global_name            | string  | user's display name                                                                            |
| avatar                 | string  | user's avatar hash                                                                             |
| avatar_decoration_data | object  | avatar decoration data, if any (`null` if none)                                                |
| bot                    | boolean | whether the user is a bot                                                                      |
| flags                  | integer | the public flags on a user's account                                                           |
| premium_type           | integer | type of Nitro subscription. **Requires `identify.premium` scope.**                             |

###### Example Current User Update Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "id": "53908232506183680",
    "username": "Mason",
    "discriminator": "0",
    "global_name": "Mason",
    "avatar": "a_bab14f271d565501444b2ca3be944b25",
    "avatar_decoration_data": null,
    "bot": false,
    "flags": 64,
    "premium_type": 0
  },
  "evt": "CURRENT_USER_UPDATE"
}
```

User flags and premium types: call the Skill tool with `"discord-rest"`.

## RELATIONSHIP_UPDATE

No arguments. **Requires the `relationships_read` OAuth2 scope.**

Fired when a relationship is added, updated (e.g. presence change), or removed. When a relationship is
removed, `type` will be `0` (`NONE`).

###### Relationship Update Dispatch Data Structure

| Field    | Type                | Description                         |
| -------- | ------------------- | ----------------------------------- |
| type     | integer             | relationship type                   |
| user     | partial user object | the related user                    |
| presence | presence object     | the related user's current presence |

###### Relationship Types

| Type             | Value | Description                              |
| ---------------- | ----- | ---------------------------------------- |
| NONE             | 0     | relationship removed                     |
| FRIEND           | 1     | user is a friend                         |
| BLOCKED          | 2     | user is blocked                          |
| PENDING_INCOMING | 3     | incoming friend request                  |
| PENDING_OUTGOING | 4     | outgoing friend request                  |
| IMPLICIT         | 5     | user is in a mutual guild (not a friend) |

###### Presence Object

| Field    | Type            | Description                                                   |
| -------- | --------------- | ------------------------------------------------------------- |
| status   | string          | user's status (`online`, `idle`, `dnd`, `offline`)            |
| activity | activity object | user's current activity for this application (`null` if none) |

###### Example Relationship Update Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "type": 1,
    "user": {
      "id": "190320984123768832",
      "username": "test user 2",
      "discriminator": "0",
      "global_name": "test user 2",
      "avatar": "b004ec1740a63ca06ae2e14c5cee11f3",
      "bot": false,
      "flags": 0,
      "premium_type": 0
    },
    "presence": {
      "status": "online",
      "activity": null
    }
  },
  "evt": "RELATIONSHIP_UPDATE"
}
```

## GUILD_STATUS

###### Guild Status Argument Structure

| Field    | Type   | Description                         |
| -------- | ------ | ----------------------------------- |
| guild_id | string | id of guild to listen to updates of |

###### Guild Status Dispatch Data Structure

| Field  | Type                 | Description                                            |
| ------ | -------------------- | ------------------------------------------------------ |
| guild  | partial guild object | guild with requested id                                |
| online | integer              | number of online users in guild (deprecated; always 0) |

###### Example Guild Status Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "guild": {
      "id": "199737254929760256",
      "name": "test",
      "icon_url": null
    },
    "online": 0
  },
  "evt": "GUILD_STATUS"
}
```

## GUILD_CREATE

**No arguments.**

###### Guild Create Dispatch Data Structure

| Field | Type   | Description       |
| ----- | ------ | ----------------- |
| id    | string | guild id          |
| name  | string | name of the guild |

###### Example Guild Create Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "id": "199737254929767562",
    "name": "Test Server"
  },
  "evt": "GUILD_CREATE"
}
```

## CHANNEL_CREATE

**No arguments.**

###### Channel Create Dispatch Data Structure

| Field | Type    | Description                                                      |
| ----- | ------- | ---------------------------------------------------------------- |
| id    | string  | channel id                                                       |
| name  | string  | name of the channel                                              |
| type  | integer | channel type (guild text: 0, guild voice: 2, dm: 1, group dm: 3) |

###### Example Channel Create Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "id": "199737254929760257",
    "name": "General",
    "type": 0
  },
  "evt": "CHANNEL_CREATE"
}
```

## VOICE_CHANNEL_SELECT

**No arguments.**

###### Voice Channel Select Dispatch Data Structure

| Field      | Type   | Description                    |
| ---------- | ------ | ------------------------------ |
| channel_id | string | id of channel (`null` if none) |
| guild_id   | string | id of guild (`null` if none)   |

###### Example Voice Channel Select Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "channel_id": "199737254929760257",
    "guild_id": "199737254929760256"
  },
  "evt": "VOICE_CHANNEL_SELECT"
}
```

## VOICE_STATE_CREATE / VOICE_STATE_UPDATE / VOICE_STATE_DELETE

Dispatches channel voice state objects.

###### Voice State Argument Structure

| Field      | Type   | Description                           |
| ---------- | ------ | ------------------------------------- |
| channel_id | string | id of channel to listen to updates of |

The upstream page gives no field table for the dispatched object, only the example below. The observed
shape is a wrapper carrying `voice_state`, `user`, `nick`, `volume`, `mute` and `pan`.

###### Example Voice State Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "evt": "VOICE_STATE_CREATE",
  "data": {
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
}
```

## VOICE_SETTINGS_UPDATE

###### Voice Settings Argument Structure

**No arguments.** Dispatches the `GET_VOICE_SETTINGS` response (see RPC-COMMANDS.md).

###### Example Voice Settings Dispatch Payload

Note the dispatch example omits `deaf` and `mute`, which the `GET_VOICE_SETTINGS` response includes.

```json
{
  "cmd": "DISPATCH",
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
    "silence_warning": false
  },
  "evt": "VOICE_SETTINGS_UPDATE"
}
```

## VOICE_CONNECTION_STATUS

**No arguments.**

###### Voice Connection Status Dispatch Data Structure

| Field        | Type              | Description                                     |
| ------------ | ----------------- | ----------------------------------------------- |
| state        | string            | one of the voice connection states listed below |
| hostname     | string            | hostname of the connected voice server          |
| pings        | array of integers | last 20 pings (in ms)                           |
| average_ping | integer           | average ping (in ms)                            |
| last_ping    | integer           | last ping (in ms)                               |

###### Voice Connection States

| Field              | Description                       |
| ------------------ | --------------------------------- |
| DISCONNECTED       | TCP disconnected                  |
| AWAITING_ENDPOINT  | Waiting for voice endpoint        |
| AUTHENTICATING     | TCP authenticating                |
| CONNECTING         | TCP connecting                    |
| CONNECTED          | TCP connected                     |
| VOICE_DISCONNECTED | TCP connected, Voice disconnected |
| VOICE_CONNECTING   | TCP connected, Voice connecting   |
| VOICE_CONNECTED    | TCP connected, Voice connected    |
| NO_ROUTE           | No route to host                  |
| ICE_CHECKING       | WebRTC ice checking               |

###### Example Voice Connection Status Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "evt": "VOICE_CONNECTION_STATUS",
  "data": {
    "state": "VOICE_CONNECTED",
    "hostname": "some-server.discord.gg",
    "pings": [20, 13.37],
    "average_ping": 13.37,
    "last_ping": 20
  }
}
```

## SPEAKING_START / SPEAKING_STOP

###### Speaking Argument Structure

| Field      | Type   | Description                           |
| ---------- | ------ | ------------------------------------- |
| channel_id | string | id of channel to listen to updates of |

###### Speaking Dispatch Data Structure

| Field   | Type   | Description                             |
| ------- | ------ | --------------------------------------- |
| user_id | string | id of user who started/stopped speaking |

###### Example Speaking Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "user_id": "190320984123768832"
  },
  "evt": "SPEAKING_STOP"
}
```

## MESSAGE_CREATE / MESSAGE_UPDATE / MESSAGE_DELETE

Dispatches message objects, with the exception of deletions, which only contains the id in the message
object.

###### Message Argument Structure

| Field      | Type   | Description                           |
| ---------- | ------ | ------------------------------------- |
| channel_id | string | id of channel to listen to updates of |

###### Example Message Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "channel_id": "199737254929760256",
    "message": {
      "id": "199743874640379904",
      "blocked": false,
      "content": "test",
      "content_parsed": [
        {
          "content": "test",
          "type": "text"
        }
      ],
      "author_color": "#ffffff",
      "edited_timestamp": null,
      "timestamp": "2016-07-05T04:30:50.776Z",
      "tts": false,
      "mentions": [],
      "mention_roles": [],
      "mention_everyone": false,
      "embeds": [],
      "attachments": [],
      "type": 0,
      "pinned": false,
      "author": {
        "id": "190320984123768832",
        "username": "test user 2",
        "discriminator": "7479",
        "avatar": "b004ec1740a63ca06ae2e14c5cee11f3",
        "bot": false
      }
    }
  },
  "evt": "MESSAGE_CREATE"
}
```

The RPC message object carries fields the HTTP API message object does not: `blocked`,
`content_parsed` and `author_color`. This is the "similar but may not be exactly equivalent" caveat in
practice.

## NOTIFICATION_CREATE

**No arguments. This event requires the `rpc.notifications.read` OAuth2 scope.**

###### Notification Create Dispatch Data Structure

| Field      | Type           | Description                               |
| ---------- | -------------- | ----------------------------------------- |
| channel_id | string         | id of channel where notification occurred |
| message    | message object | message that generated this notification  |
| icon_url   | string         | icon url of the notification              |
| title      | string         | title of the notification                 |
| body       | string         | body of the notification                  |

###### Example Notification Create Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "channel_id": "199737254929760256",
    "message": {
      "id": "199743874640379904",
      "blocked": false,
      "content": "test",
      "content_parsed": [
        {
          "content": "test",
          "type": "text"
        }
      ],
      "author_color": "#ffffff",
      "edited_timestamp": null,
      "timestamp": "2016-07-05T04:30:50.776Z",
      "tts": false,
      "mentions": [],
      "mention_roles": [],
      "mention_everyone": false,
      "embeds": [],
      "attachments": [],
      "type": 0,
      "pinned": false,
      "author": {
        "id": "190320984123768832",
        "username": "test user 2",
        "discriminator": "7479",
        "avatar": "b004ec1740a63ca06ae2e14c5cee11f3",
        "bot": false
      }
    },
    "icon_url": "https://cdn.discordapp.com/avatars/155607406007681024/8ab559b8286e48270c04471ae382cd9d.jpg",
    "title": "test_user (#general)",
    "body": "test message"
  },
  "evt": "NOTIFICATION_CREATE"
}
```

## ACTIVITY_JOIN

**No arguments.**

###### Activity Join Dispatch Data Structure

| Field  | Type   | Description                             |
| ------ | ------ | --------------------------------------- |
| secret | string | the `join_secret` for the given invite  |

###### Example Activity Join Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "secret": "025ed05c71f639de8bfaa0d679d7c94b2fdce12f"
  },
  "evt": "ACTIVITY_JOIN"
}
```

## ACTIVITY_SPECTATE

**No arguments.**

###### Activity Spectate Dispatch Data Structure

| Field  | Type   | Description                                |
| ------ | ------ | ------------------------------------------ |
| secret | string | the `spectate_secret` for the given invite |

###### Example Activity Spectate Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "secret": "e7eb30d2ee025ed05c71ea495f770b76454ee4e0"
  },
  "evt": "ACTIVITY_SPECTATE"
}
```

## ACTIVITY_JOIN_REQUEST

**No arguments.**

###### Activity Join Request Data Structure

| Field | Type                | Description                                   |
| ----- | ------------------- | --------------------------------------------- |
| user  | partial user object | information about the user requesting to join |

Respond with `SEND_ACTIVITY_JOIN_INVITE` to accept or `CLOSE_ACTIVITY_REQUEST` to reject
(RPC-COMMANDS.md).

###### Example Activity Join Request Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "user": {
      "id": "53908232506183680",
      "username": "Mason",
      "discriminator": "1337",
      "avatar": "a_bab14f271d565501444b2ca3be944b25"
    }
  },
  "evt": "ACTIVITY_JOIN_REQUEST"
}
```

## ACTIVITY_INVITE

**No arguments.**

###### Activity Invite Dispatch Data Structure

| Field      | Type                | Description                              |
| ---------- | ------------------- | ---------------------------------------- |
| type       | integer             | invite type; `1` for join                |
| user       | partial user object | user who sent the invite                 |
| activity   | activity object     | the activity associated with the invite   |
| channel_id | string              | id of the channel the invite was sent in |
| message_id | string              | id of the invite message                 |

Upstream documents only value `1` for `type`.

###### Example Activity Invite Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "type": 1,
    "user": {
      "id": "53908232506183680",
      "username": "Mason",
      "discriminator": "1337",
      "avatar": "a_bab14f271d565501444b2ca3be944b25"
    },
    "activity": {
      "application_id": "192741864418312192",
      "name": "My Game",
      "party": {
        "id": "party1234",
        "size": [2, 5]
      }
    },
    "channel_id": "199737254929760256",
    "message_id": "199743874640379904"
  },
  "evt": "ACTIVITY_INVITE"
}
```

## ENTITLEMENT_CREATE

**No arguments.** Fired when the user acquires a new entitlement for this application.

###### Entitlement Create Dispatch Data Structure

| Field       | Type               | Description                      |
| ----------- | ------------------ | -------------------------------- |
| entitlement | entitlement object | the entitlement that was created |

###### Entitlement Object

| Field          | Type    | Description                                                            |
| -------------- | ------- | ---------------------------------------------------------------------- |
| id             | string  | entitlement id                                                         |
| sku_id         | string  | id of the SKU this entitlement is for                                  |
| application_id | string  | id of the application                                                  |
| user_id        | string  | id of the user that owns the entitlement                               |
| type           | integer | entitlement type                                                       |
| deleted        | boolean | whether the entitlement has been deleted                               |
| starts_at?     | ISO8601 | start date of the entitlement                                          |
| ends_at?       | ISO8601 | end date of the entitlement                                            |
| guild_id?      | string  | id of the guild the entitlement applies to                             |
| consumed?      | boolean | for consumable entitlements, whether the entitlement has been consumed |

###### Entitlement Types

| Type                    | Value | Description                    |
| ----------------------- | ----- | ------------------------------ |
| PURCHASE                | 1     | purchased by a user            |
| PREMIUM_SUBSCRIPTION    | 2     | a Nitro subscription           |
| DEVELOPER_GIFT          | 3     | gifted by a developer          |
| TEST_MODE_PURCHASE      | 4     | purchased in test mode         |
| FREE_PURCHASE           | 5     | granted for free               |
| USER_GIFT               | 6     | gifted by another user         |
| PREMIUM_PURCHASE        | 7     | purchased as a premium feature |
| APPLICATION_SUBSCRIPTION | 8    | an app subscription            |

###### Example Entitlement Create Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "entitlement": {
      "id": "1019653849998299136",
      "sku_id": "1019475255913222144",
      "application_id": "192741864418312192",
      "user_id": "53908232506183680",
      "type": 8,
      "deleted": false,
      "starts_at": "2022-09-14T17:00:18.704163+00:00",
      "ends_at": "2022-10-14T17:00:18.704163+00:00"
    }
  },
  "evt": "ENTITLEMENT_CREATE"
}
```

## ENTITLEMENT_DELETE

**No arguments.** Fired when an entitlement for this application is removed. The entitlement object in
the payload reflects the state of the entitlement at the time of deletion.

###### Entitlement Delete Dispatch Data Structure

| Field       | Type               | Description                      |
| ----------- | ------------------ | -------------------------------- |
| entitlement | entitlement object | the entitlement that was deleted |

Same Entitlement Object and Entitlement Types as [ENTITLEMENT_CREATE](#entitlement_create).

###### Example Entitlement Delete Dispatch Payload

```json
{
  "cmd": "DISPATCH",
  "data": {
    "entitlement": {
      "id": "1019653849998299136",
      "sku_id": "1019475255913222144",
      "application_id": "192741864418312192",
      "user_id": "53908232506183680",
      "type": 8,
      "deleted": true,
      "starts_at": "2022-09-14T17:00:18.704163+00:00",
      "ends_at": "2022-10-14T17:00:18.704163+00:00"
    }
  },
  "evt": "ENTITLEMENT_DELETE"
}
```

## Source

Discord Developer Documentation: <https://docs.discord.com/developers/topics/rpc>.
Retrieved 2026-08-26.
