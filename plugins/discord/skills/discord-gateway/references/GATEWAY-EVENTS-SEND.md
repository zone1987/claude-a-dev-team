# Gateway Send Events

Gateway events an app sends to Discord over a Gateway connection, plus the common payload envelope
that wraps every Gateway event in both directions.

Source: [Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved
2026-08-26.

## Contents

- [Event names](#event-names)
- [Payload structure](#payload-structure)
- [Send events index](#send-events-index)
- [Identify (opcode 2)](#identify-opcode-2)
- [Resume (opcode 6)](#resume-opcode-6)
- [Heartbeat (opcode 1)](#heartbeat-opcode-1)
- [Request Guild Members (opcode 8)](#request-guild-members-opcode-8)
- [Request Soundboard Sounds (opcode 31)](#request-soundboard-sounds-opcode-31)
- [Request Channel Info (opcode 43)](#request-channel-info-opcode-43)
- [Update Voice State (opcode 4)](#update-voice-state-opcode-4)
- [Update Presence (opcode 3)](#update-presence-opcode-3)

## Event names

In practice, event names are UPPER-CASED with under_scores joining each word in the name. For
instance, Channel Create would be `CHANNEL_CREATE` and Voice State Update would be
`VOICE_STATE_UPDATE`. For readability, event names in the upstream documentation are typically left
in Title Case.

Undocumented fields: the upstream states explicitly that not all Gateway event fields are documented,
and that you should assume undocumented fields are not supported for apps, with format and data
subject to change at any time.

## Payload structure

Gateway event payloads have a common structure, but the contents of the associated data (`d`) varies
between the different events.

| Field | Type                    | Description                                                    |
| ----- | ----------------------- | -------------------------------------------------------------- |
| op    | integer                 | Gateway opcode, which indicates the payload type               |
| d     | ?mixed (any JSON value) | Event data                                                     |
| s     | ?integer *              | Sequence number of event used for resuming sessions and heartbeating |
| t     | ?string *               | Event name                                                     |

\* `s` and `t` are `null` when `op` is not `0` (the Gateway Dispatch opcode).

###### Example Gateway Event Payload

```json
{
  "op": 0,
  "d": {},
  "s": 42,
  "t": "GATEWAY_EVENT_NAME"
}
```

Gateway opcode numbers are in `OPCODES-AND-STATUS-CODES.md`.

## Send events index

Send events are Gateway events encapsulated in an event payload, and are sent by an app to Discord
through a Gateway connection. Previously, Gateway send events were labeled as commands.

| Name                      | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| Identify                  | Triggers the initial handshake with the gateway           |
| Resume                    | Resumes a dropped gateway connection                      |
| Heartbeat                 | Maintains an active gateway connection                    |
| Request Guild Members     | Requests members for a guild                              |
| Request Soundboard Sounds | Requests soundboard sounds in a set of guilds             |
| Request Channel Info      | Requests ephemeral channel data for channels in a guild   |
| Update Voice State        | Joins, moves, or disconnects the app from a voice channel |
| Update Presence           | Updates an app's presence                                 |

## Identify (opcode 2)

Used to trigger the initial handshake with the gateway. Details about identifying are in
`CONNECTION-LIFECYCLE.md`.

###### Identify Structure

| Field            | Type                                           | Description                                                                                                                    | Default |
| ---------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------- |
| token            | string                                         | Authentication token                                                                                                           | -       |
| properties       | object                                         | Connection properties (see below)                                                                                              | -       |
| compress?        | boolean                                        | Whether this connection supports compression of packets                                                                        | false   |
| large_threshold? | integer                                        | Value between 50 and 250, total number of members where the gateway will stop sending offline members in the guild member list | 50      |
| shard?           | array of two integers (shard_id, num_shards)   | Used for Guild Sharding                                                                                                        | -       |
| presence?        | update presence object                         | Presence structure for initial presence information                                                                            | -       |
| intents          | integer                                        | Gateway Intents you wish to receive                                                                                            | -       |
| capabilities?    | integer                                        | Bitfield representing capabilities of your gateway client                                                                      | 0       |

###### Gateway Capabilities

`capabilities` is a bitfield you can use to opt a bot client into gateway behaviors. It's a separate
Identify bitfield from `intents`: `intents` control which events your bot client receives, while
`capabilities` affects gateway behaviors.

| Flag                | Value     | Description                                                                                                    |
| ------------------- | --------- | -------------------------------------------------------------------------------------------------------------- |
| CHANNEL_OBFUSCATION | `1 << 15` | Opts the client into receiving obfuscated channel metadata over the Gateway for channels it can't view         |

Warning: `CHANNEL_OBFUSCATION` is a temporary, testing-only opt-in for channel obfuscation. This
opt-in mechanism will change before the feature reaches general availability. Obfuscation is then
planned to apply to all bots automatically, even when they don't provide this capability.

Obfuscated channel metadata is described on the Channel resource page (Obfuscated Channels); call the
Skill tool with "discord-rest" for the channel object.

###### Identify Connection Properties

| Field   | Type   | Description           |
| ------- | ------ | --------------------- |
| os      | string | Your operating system |
| browser | string | Your library name     |
| device  | string | Your library name     |

Warning: these fields originally were `$` prefixed (i.e. `$browser`) but this syntax is deprecated.
While they currently still work, it is recommended to move to non-prefixed fields.

###### Example Identify

```json
{
  "op": 2,
  "d": {
    "token": "my_token",
    "properties": {
      "os": "linux",
      "browser": "disco",
      "device": "disco"
    },
    "compress": true,
    "large_threshold": 250,
    "shard": [0, 1],
    "presence": {
      "activities": [{
        "name": "Cards Against Humanity",
        "type": 0
      }],
      "status": "dnd",
      "since": 91879201,
      "afk": false
    },
    // These intents represent 1 << 0 for GUILDS and 1 << 2 for GUILD_MODERATION
    // This connection will only receive the events defined in those two intents
    "intents": 5
  }
}
```

## Resume (opcode 6)

Used to replay missed events when a disconnected client resumes. Details about resuming are in
`CONNECTION-LIFECYCLE.md`.

###### Resume Structure

| Field      | Type    | Description                   |
| ---------- | ------- | ----------------------------- |
| token      | string  | Session token                 |
| session_id | string  | Session ID                    |
| seq        | integer | Last sequence number received |

###### Example Resume

```json
{
  "op": 6,
  "d": {
    "token": "randomstring",
    "session_id": "evenmorerandomstring",
    "seq": 1337
  }
}
```

## Heartbeat (opcode 1)

Used to maintain an active gateway connection. Must be sent every `heartbeat_interval` milliseconds
after the Opcode 10 Hello payload is received. The inner `d` key is the last sequence number — `s` —
received by the client. If you have not yet received one, send `null`.

Details about heartbeats are in `CONNECTION-LIFECYCLE.md`.

###### Example Heartbeat

```json
{
  "op": 1,
  "d": 251
}
```

## Request Guild Members (opcode 8)

Used to request all members for a guild or a list of guilds. When initially connecting, if you don't
have the `GUILD_PRESENCES` Gateway Intent, or if the guild is over 75k members, it will only send
members who are in voice, plus the member for you (the connecting user). Otherwise, if a guild has
over `large_threshold` members (value in the Gateway Identify), it will only send members who are
online, have a role, have a nickname, or are in a voice channel, and if it has under
`large_threshold` members, it will send all members. If a client wishes to receive additional
members, they need to explicitly request them via this operation. The server will send Guild Members
Chunk events in response with up to 1000 members per chunk until all members that match the request
have been sent.

Due to Discord's privacy and infrastructural concerns with this feature, there are some limitations
that apply:

* `GUILD_PRESENCES` intent is required to set `presences = true`. Otherwise, it will always be false
* `GUILD_MEMBERS` intent is required to request the entire member list — `(query='', limit=0<=n)`
* You will be limited to requesting 1 `guild_id` per request
* Requesting a prefix (`query` parameter) will return a maximum of 100 members
* Requesting `user_ids` will continue to be limited to returning 100 members

Info: Discord is introducing a new rate limit to the Request Guild Members opcode. See the change log
entry "Introducing Rate Limit When Requesting All Guild Members" for more information and timeline on
this new rate limit. The gateway signals it with the Rate Limited receive event.

###### Request Guild Members Structure

| Field     | Type                             | Description                                                                                                                           | Required                  |
| --------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| guild_id  | snowflake                        | ID of the guild to get members for                                                                                                    | true                      |
| query?    | string                           | string that username starts with, or an empty string to return all members                                                            | one of query or user_ids  |
| limit     | integer                          | maximum number of members to send matching the `query`; a limit of `0` can be used with an empty string `query` to return all members | true when specifying query |
| presences?| boolean                          | used to specify if we want the presences of the matched members                                                                       | false                     |
| user_ids? | snowflake or array of snowflakes | used to specify which users you wish to fetch                                                                                         | one of query or user_ids  |
| nonce?    | string                           | nonce to identify the Guild Members Chunk response                                                                                    | false                     |

Info: Nonce can only be up to 32 bytes. If you send an invalid nonce it will be ignored and the reply
member_chunk(s) will not have a nonce set.

###### Example Request Guild Members

```json
{
  "op": 8,
  "d": {
    "guild_id": "41771983444115456",
    "query": "",
    "limit": 0
  }
}
```

## Request Soundboard Sounds (opcode 31)

Used to request soundboard sounds for a list of guilds. The server will send Soundboard Sounds events
for each guild in response.

###### Request Soundboard Sounds Structure

| Field     | Type                | Description                                    |
| --------- | ------------------- | ---------------------------------------------- |
| guild_ids | array of snowflakes | IDs of the guilds to get soundboard sounds for |

###### Example Request Soundboard Sounds

```json
{
  "op": 31,
  "d": {
    "guild_ids": ["613425648685547541", "81384788765712384"]
  }
}
```

## Request Channel Info (opcode 43)

Requests ephemeral channel data for channels in a guild. The server will send a Channel Info event in
response.

###### Request Channel Info Structure

| Field    | Type             | Description                                                                              |
| -------- | ---------------- | ---------------------------------------------------------------------------------------- |
| guild_id | snowflake        | The guild id to request channel info for                                                 |
| fields   | array of strings | The fields to request. The current available fields are `status` and `voice_start_time`. |

###### Example Request Channel Info

```json
{
  "op": 43,
  "d": {
    "guild_id": "613425648685547541",
    "fields": ["status", "voice_start_time"]
  }
}
```

## Update Voice State (opcode 4)

Sent when a client wants to join, move, or disconnect from a voice channel.

###### Gateway Voice State Update Structure

| Field      | Type       | Description                                                          |
| ---------- | ---------- | -------------------------------------------------------------------- |
| guild_id   | snowflake  | ID of the guild                                                      |
| channel_id | ?snowflake | ID of the voice channel client wants to join (null if disconnecting)  |
| self_mute  | boolean    | Whether the client is muted                                          |
| self_deaf  | boolean    | Whether the client deafened                                          |

###### Example Gateway Voice State Update

```json
{
  "op": 4,
  "d": {
    "guild_id": "41771983423143937",
    "channel_id": "127121515262115840",
    "self_mute": false,
    "self_deaf": false
  }
}
```

## Update Presence (opcode 3)

Sent by the client to indicate a presence or status update.

###### Gateway Presence Update Structure

| Field      | Type                       | Description                                                                                 |
| ---------- | -------------------------- | ------------------------------------------------------------------------------------------- |
| since      | ?integer                   | Unix time (in milliseconds) of when the client went idle, or null if the client is not idle |
| activities | array of activity objects  | User's activities                                                                           |
| status     | string                     | User's new status                                                                           |
| afk        | boolean                    | Whether or not the client is afk                                                            |

The activity object and its every sub-structure are in `GATEWAY-EVENTS-MESSAGES.md`.

###### Status Types

| Status    | Description                    |
| --------- | ------------------------------ |
| online    | Online                         |
| dnd       | Do Not Disturb                 |
| idle      | AFK                            |
| invisible | Invisible and shown as offline |
| offline   | Offline                        |

###### Example Gateway Presence Update

```json
{
  "op": 3,
  "d": {
    "since": 91879201,
    "activities": [{
      "name": "Save the Oxford Comma",
      "type": 0
    }],
    "status": "online",
    "afk": false
  }
}
```

Rate limit on status updates: clients may only update their game status 5 times per 20 seconds.

## Source

Discord Developer Documentation,
[Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved 2026-08-26.
