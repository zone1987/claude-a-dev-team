# Gateway Receive Events — Messages, Reactions, Polls, Presence

Every field of every receive event in the message, reaction, poll and presence domains, plus the
complete activity object with all of its sub-structures and enums.

Source: [Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved
2026-08-26.

## Contents

- [Messages](#messages)
- [Reactions](#reactions)
- [Polls](#polls)
- [Presence Update](#presence-update)
- [Client Status Object](#client-status-object)
- [Activity Object](#activity-object)
- [Activity Types](#activity-types)
- [Status Display Types](#status-display-types)
- [Activity Timestamps](#activity-timestamps)
- [Activity Emoji](#activity-emoji)
- [Activity Party](#activity-party)
- [Activity Assets](#activity-assets)
- [Activity Asset Image](#activity-asset-image)
- [Activity Secrets](#activity-secrets)
- [Activity Flags](#activity-flags)
- [Activity Buttons](#activity-buttons)
- [Activity examples](#activity-examples)
- [Typing Start](#typing-start)
- [User Update](#user-update)

## Messages

Warning: unlike persistent messages, ephemeral messages are sent directly to the user and the bot who
sent the message rather than through the guild channel. Because of this, ephemeral messages are tied
to the `DIRECT_MESSAGES` intent, and the message object won't include `guild_id` or `member`.

### Message Create

Sent when a message is created. The inner payload is a message object with the following extra fields:

###### Message Create Extra Fields

| Field         | Type                                                                     | Description                                                                                            |
| ------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| guild_id?     | snowflake                                                                | ID of the guild the message was sent in - unless it is an ephemeral message                            |
| member?       | partial guild member object                                              | Member properties for this message's author. Missing for ephemeral messages and messages from webhooks |
| mentions      | array of user objects, optionally with an additional partial member field | Users specifically mentioned in the message                                                            |
| channel_type? | integer                                                                  | The type of channel the message was sent in                                                            |

### Message Update

Sent when a message is updated. The inner payload is a message object with the same extra fields as
`MESSAGE_CREATE`.

Warning: the value for `tts` will always be false in message updates.

### Message Delete

Sent when a message is deleted.

###### Message Delete Event Fields

| Field      | Type      | Description       |
| ---------- | --------- | ----------------- |
| id         | snowflake | ID of the message |
| channel_id | snowflake | ID of the channel |
| guild_id?  | snowflake | ID of the guild   |

### Message Delete Bulk

Sent when multiple messages are deleted at once.

###### Message Delete Bulk Event Fields

| Field      | Type                | Description         |
| ---------- | ------------------- | ------------------- |
| ids        | array of snowflakes | IDs of the messages |
| channel_id | snowflake           | ID of the channel   |
| guild_id?  | snowflake           | ID of the guild     |

## Reactions

### Message Reaction Add

Sent when a user adds a reaction to a message.

###### Message Reaction Add Event Fields

| Field              | Type                        | Description                                                  |
| ------------------ | --------------------------- | ------------------------------------------------------------ |
| user_id            | snowflake                   | ID of the user                                               |
| channel_id         | snowflake                   | ID of the channel                                            |
| message_id         | snowflake                   | ID of the message                                            |
| guild_id?          | snowflake                   | ID of the guild                                              |
| member?            | member object               | Member who reacted if this happened in a guild               |
| emoji              | a partial emoji object      | Emoji used to react                                          |
| message_author_id? | snowflake                   | ID of the user who authored the message which was reacted to |
| burst              | boolean                     | true if this is a super-reaction                             |
| burst_colors?      | array of strings            | Colors used for super-reaction animation in "#rrggbb" format |
| type               | integer                     | The type of reaction                                         |

### Message Reaction Remove

Sent when a user removes a reaction from a message.

###### Message Reaction Remove Event Fields

| Field      | Type                   | Description                       |
| ---------- | ---------------------- | --------------------------------- |
| user_id    | snowflake              | ID of the user                    |
| channel_id | snowflake              | ID of the channel                 |
| message_id | snowflake              | ID of the message                 |
| guild_id?  | snowflake              | ID of the guild                   |
| emoji      | a partial emoji object | Emoji used to react               |
| burst      | boolean                | true if this was a super-reaction |
| type       | integer                | The type of reaction              |

### Message Reaction Remove All

Sent when a user explicitly removes all reactions from a message.

###### Message Reaction Remove All Event Fields

| Field      | Type      | Description       |
| ---------- | --------- | ----------------- |
| channel_id | snowflake | ID of the channel |
| message_id | snowflake | ID of the message |
| guild_id?  | snowflake | ID of the guild   |

### Message Reaction Remove Emoji

Sent when a bot removes all instances of a given emoji from the reactions of a message.

###### Message Reaction Remove Emoji Event Fields

| Field      | Type                 | Description            |
| ---------- | -------------------- | ---------------------- |
| channel_id | snowflake            | ID of the channel      |
| guild_id?  | snowflake            | ID of the guild        |
| message_id | snowflake            | ID of the message      |
| emoji      | partial emoji object | Emoji that was removed |

## Polls

### Message Poll Vote Add

Sent when a user votes on a poll. If the poll allows multiple selection, one event will be sent per
answer.

###### Message Poll Vote Add Fields

| Field      | Type      | Description       |
| ---------- | --------- | ----------------- |
| user_id    | snowflake | ID of the user    |
| channel_id | snowflake | ID of the channel |
| message_id | snowflake | ID of the message |
| guild_id?  | snowflake | ID of the guild   |
| answer_id  | integer   | ID of the answer  |

### Message Poll Vote Remove

Sent when a user removes their vote on a poll. If the poll allows for multiple selections, one event
will be sent per answer.

###### Message Poll Vote Remove Fields

| Field      | Type      | Description       |
| ---------- | --------- | ----------------- |
| user_id    | snowflake | ID of the user    |
| channel_id | snowflake | ID of the channel |
| message_id | snowflake | ID of the message |
| guild_id?  | snowflake | ID of the guild   |
| answer_id  | integer   | ID of the answer  |

## Presence Update

Warning: if you are using Gateway Intents, you *must* specify the `GUILD_PRESENCES` intent in order to
receive Presence Update events.

A user's presence is their current state on a guild. This event is sent when a user's presence or
info, such as name or avatar, is updated.

Warning: the user object within this event can be partial, the only field which must be sent is the
`id` field, everything else is optional. Along with this limitation, no fields are required, and the
types of the fields are **not** validated. Your client should expect any combination of fields and
types within this event.

###### Presence Update Event Fields

| Field         | Type                      | Description                                  |
| ------------- | ------------------------- | -------------------------------------------- |
| user          | user object               | User whose presence is being updated         |
| guild_id      | snowflake                 | ID of the guild                              |
| status        | string                    | Either "idle", "dnd", "online", or "offline" |
| activities    | array of activity objects | User's current activities                    |
| client_status | client_status object      | User's platform-dependent status             |

## Client Status Object

Active sessions are indicated with an "online", "idle", or "dnd" string per platform. If a user is
offline or invisible, the corresponding field is not present.

| Field    | Type   | Description                                                                       |
| -------- | ------ | --------------------------------------------------------------------------------- |
| desktop? | string | User's status set for an active desktop (Windows, Linux, Mac) application session |
| mobile?  | string | User's status set for an active mobile (iOS, Android) application session          |
| web?     | string | User's status set for an active web (browser, bot user) application session        |
| vr?      | string | User's status set for an active virtual reality application session                |

## Activity Object

###### Activity Structure

| Field                | Type                | Description                                                                                                                    |
| -------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| name                 | string              | Activity's name                                                                                                                |
| type                 | integer             | Activity type                                                                                                                  |
| url?                 | ?string             | Stream URL, is validated when type is 1                                                                                        |
| created_at           | integer             | Unix timestamp (in milliseconds) of when the activity was added to the user's session                                          |
| timestamps?          | timestamps object   | Unix timestamps for start and/or end of the game                                                                               |
| application_id?      | snowflake           | Application ID for the game                                                                                                    |
| status_display_type? | ?integer            | Status display type; controls which field is displayed in the user's status text in the member list                             |
| details?             | ?string             | What the player is currently doing                                                                                             |
| details_url?         | ?string             | URL that is linked when clicking on the details text                                                                           |
| state?               | ?string             | User's current party status, or text used for a custom status                                                                   |
| state_url?           | ?string             | URL that is linked when clicking on the state text                                                                             |
| emoji?               | ?emoji object       | Emoji used for a custom status                                                                                                 |
| party?               | party object        | Information for the current party of the player                                                                                |
| assets?              | assets object       | Images for the presence and their hover texts                                                                                  |
| secrets?             | secrets object      | Secrets for Rich Presence joining and spectating                                                                               |
| instance?            | boolean             | Whether or not the activity is an instanced game session                                                                       |
| flags?               | integer             | Activity flags `OR`d together, describes what the payload includes                                                             |
| buttons?             | array of buttons    | Custom buttons shown in the Rich Presence (max 2)                                                                              |

Info: bot users are only able to set `name`, `state`, `type`, and `url`.

## Activity Types

| ID | Name      | Format                | Example                              |
| -- | --------- | --------------------- | ------------------------------------ |
| 0  | Playing   | Playing `{name}`      | "Playing Rocket League"              |
| 1  | Streaming | Streaming `{details}` | "Streaming Rocket League"            |
| 2  | Listening | Listening to `{name}` | "Listening to Spotify"               |
| 3  | Watching  | Watching `{name}`     | "Watching YouTube Together"          |
| 4  | Custom    | `{emoji}` `{state}`   | ":smiley: I am cool"                 |
| 5  | Competing | Competing in `{name}` | "Competing in Arena World Champions" |

Info: the streaming type currently only supports Twitch and YouTube. Only `https://twitch.tv/` and
`https://youtube.com/` urls will work.

## Status Display Types

| ID | Name    | Example                                |
| -- | ------- | -------------------------------------- |
| 0  | Name    | "Listening to Spotify"                 |
| 1  | State   | "Listening to Rick Astley"             |
| 2  | Details | "Listening to Never Gonna Give You Up" |

Info: this applies to all activity types. "Listening" was used to serve as a consistent example of what
the different fields might be used for.

## Activity Timestamps

| Field  | Type    | Description                                              |
| ------ | ------- | -------------------------------------------------------- |
| start? | integer | Unix time (in milliseconds) of when the activity started |
| end?   | integer | Unix time (in milliseconds) of when the activity ends    |

Info: for Listening and Watching activities, you can include both start and end timestamps to display
a time bar.

## Activity Emoji

| Field     | Type      | Description                   |
| --------- | --------- | ----------------------------- |
| name      | string    | Name of the emoji             |
| id?       | snowflake | ID of the emoji               |
| animated? | boolean   | Whether the emoji is animated |

## Activity Party

| Field | Type                                          | Description                                       |
| ----- | --------------------------------------------- | ------------------------------------------------- |
| id?   | string                                        | ID of the party                                   |
| size? | array of two integers (current_size, max_size)| Used to show the party's current and maximum size |

## Activity Assets

| Field               | Type   | Description                                                                                 |
| ------------------- | ------ | ------------------------------------------------------------------------------------------- |
| large_image?        | string | See Activity Asset Image                                                                    |
| large_text?         | string | Text displayed when hovering over the large image of the activity                            |
| large_url?          | string | URL that is opened when clicking on the large image                                          |
| small_image?        | string | See Activity Asset Image                                                                    |
| small_text?         | string | Text displayed when hovering over the small image of the activity                            |
| small_url?          | string | URL that is opened when clicking on the small image                                          |
| invite_cover_image? | string | See Activity Asset Image. Displayed as a banner on a Game Invite.                            |

## Activity Asset Image

Activity asset images are arbitrary strings which usually contain snowflake IDs or prefixed image IDs.
Treat data within this field carefully, as it is user-specifiable and not sanitized.

To use an external image via media proxy, specify the URL as the field's value when sending. You will
only receive the `mp:` prefix via the gateway.

| Type              | Format                   | Image URL                                            |
| ----------------- | ------------------------ | ---------------------------------------------------- |
| Application Asset | `{application_asset_id}` | See Application Asset Image Formatting               |
| Media Proxy Image | `mp:{image_id}`          | `https://media.discordapp.net/{image_id}`            |

Info: **uploaded assets** (Application Asset type) support PNG, JPEG, and WebP. Animated images are
not supported for uploaded assets. **External URL assets** (Media Proxy Image type) support any
publicly accessible image URL, including GIF, animated WebP, and AVIF.

## Activity Secrets

| Field     | Type   | Description                           |
| --------- | ------ | ------------------------------------- |
| join?     | string | Secret for joining a party            |
| spectate? | string | Secret for spectating a game          |
| match?    | string | Secret for a specific instanced match |

## Activity Flags

| Name                        | Value    |
| --------------------------- | -------- |
| INSTANCE                    | `1 << 0` |
| JOIN                        | `1 << 1` |
| SPECTATE                    | `1 << 2` |
| JOIN_REQUEST                | `1 << 3` |
| SYNC                        | `1 << 4` |
| PLAY                        | `1 << 5` |
| PARTY_PRIVACY_FRIENDS       | `1 << 6` |
| PARTY_PRIVACY_VOICE_CHANNEL | `1 << 7` |
| EMBEDDED                    | `1 << 8` |

## Activity Buttons

When received over the gateway, the `buttons` field is an array of strings, which are the button
labels. Bots cannot access a user's activity button URLs. When sending, the `buttons` field must be an
array of the below object:

| Field | Type   | Description                                            |
| ----- | ------ | ------------------------------------------------------ |
| label | string | Text shown on the button (1-32 characters)             |
| url   | string | URL opened when clicking the button (1-512 characters) |

## Activity examples

###### Example Activity

```json
{
  "details": "24H RL Stream for Charity",
  "state": "Rocket League",
  "name": "Twitch",
  "type": 1,
  "url": "https://www.twitch.tv/discord"
}
```

###### Example Activity with Rich Presence

```json
{
  "name": "Rocket League",
  "type": 0,
  "application_id": "379286085710381999",
  "state": "In a Match",
  "details": "Ranked Duos: 2-1",
  "timestamps": {
    "start": 15112000660000
  },
  "party": {
    "id": "9dd6594e-81b3-49f6-a6b5-a679e6a060d3",
    "size": [2, 2]
  },
  "assets": {
    "large_image": "351371005538729000",
    "large_text": "DFH Stadium",
    "small_image": "351371005538729111",
    "small_text": "Silver III"
  },
  "secrets": {
    "join": "025ed05c71f639de8bfaa0d679d7c94b2fdce12f",
    "spectate": "e7eb30d2ee025ed05c71ea495f770b76454ee4e0",
    "match": "4b2fdce12f639de8bfa7e3591b71a0d679d7c93f"
  }
}
```

Warning: clients may only update their game status 5 times per 20 seconds.

## Typing Start

Sent when a user starts typing in a channel.

###### Typing Start Event Fields

| Field      | Type          | Description                                            |
| ---------- | ------------- | ------------------------------------------------------ |
| channel_id | snowflake     | ID of the channel                                      |
| guild_id?  | snowflake     | ID of the guild                                        |
| user_id    | snowflake     | ID of the user                                         |
| timestamp  | integer       | Unix time (in seconds) of when the user started typing |
| member?    | member object | Member who started typing if this happened in a guild  |

## User Update

Sent when properties about the current bot's user change. Inner payload is a user object.

## Source

Discord Developer Documentation,
[Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved 2026-08-26.
The message, user, member, emoji and reaction-type objects referenced above are REST resources; call
the Skill tool with "discord-rest".
