# Gateway Receive Events — Index and Session Events

The complete upstream table of every receive event, plus the five session-level receive events that
are not Dispatch payloads of a resource (Hello, Ready, Resumed, Reconnect, Invalid Session) and the
Rate Limited event.

Receive events are Gateway events encapsulated in an event payload, and are sent by Discord to an app
through a Gateway connection. Receive events correspond to events that happen in a Discord server
where the app is installed.

Source: [Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved
2026-08-26.

## Contents

- [Complete receive event index (82 events)](#complete-receive-event-index-82-events)
- [Hello (opcode 10)](#hello-opcode-10)
- [Ready](#ready)
- [Resumed](#resumed)
- [Reconnect (opcode 7)](#reconnect-opcode-7)
- [Invalid Session (opcode 9)](#invalid-session-opcode-9)
- [Rate Limited](#rate-limited)
- [Where each remaining event is documented](#where-each-remaining-event-is-documented)

## Complete receive event index (82 events)

| Name                                   | Description                                                                                           |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Hello                                  | Defines the heartbeat interval                                                                        |
| Ready                                  | Contains the initial state information                                                                |
| Resumed                                | Response to Resume                                                                                    |
| Reconnect                              | Server is going away, client should reconnect to gateway and resume                                   |
| Rate Limited                           | Application was rate limited for a gateway opcode                                                     |
| Invalid Session                        | Failure response to Identify or Resume or invalid active session                                      |
| Application Command Permissions Update | Application command permission was updated                                                            |
| Auto Moderation Rule Create            | Auto Moderation rule was created                                                                      |
| Auto Moderation Rule Update            | Auto Moderation rule was updated                                                                      |
| Auto Moderation Rule Delete            | Auto Moderation rule was deleted                                                                      |
| Auto Moderation Action Execution       | Auto Moderation rule was triggered and an action was executed (e.g. a message was blocked)            |
| Channel Create                         | New guild channel created                                                                             |
| Channel Update                         | Channel was updated                                                                                   |
| Channel Delete                         | Channel was deleted                                                                                   |
| Channel Info                           | Response to Request Channel Info                                                                      |
| Channel Pins Update                    | Message was pinned or unpinned                                                                        |
| Thread Create                          | Thread created, also sent when being added to a private thread                                        |
| Thread Update                          | Thread was updated                                                                                    |
| Thread Delete                          | Thread was deleted                                                                                    |
| Thread List Sync                       | Sent when gaining access to a channel, contains all active threads in that channel                    |
| Thread Member Update                   | Thread member for the current user was updated                                                        |
| Thread Members Update                  | Some user(s) were added to or removed from a thread                                                    |
| Entitlement Create                     | Entitlement was created                                                                               |
| Entitlement Update                     | Entitlement was updated or renewed                                                                    |
| Entitlement Delete                     | Entitlement was deleted                                                                               |
| Guild Create                           | Lazy-load for unavailable guild, guild became available, or user joined a new guild                    |
| Guild Update                           | Guild was updated                                                                                     |
| Guild Delete                           | Guild became unavailable, or user left/was removed from a guild                                        |
| Guild Audit Log Entry Create           | A guild audit log entry was created                                                                   |
| Guild Ban Add                          | User was banned from a guild                                                                          |
| Guild Ban Remove                       | User was unbanned from a guild                                                                        |
| Guild Emojis Update                    | Guild emojis were updated                                                                             |
| Guild Stickers Update                  | Guild stickers were updated                                                                           |
| Guild Integrations Update              | Guild integration was updated                                                                         |
| Guild Member Add                       | New user joined a guild                                                                               |
| Guild Member Remove                    | User was removed from a guild                                                                         |
| Guild Member Update                    | Guild member was updated                                                                              |
| Guild Members Chunk                    | Response to Request Guild Members                                                                     |
| Guild Role Create                      | Guild role was created                                                                                |
| Guild Role Update                      | Guild role was updated                                                                                |
| Guild Role Delete                      | Guild role was deleted                                                                                |
| Guild Scheduled Event Create           | Guild scheduled event was created                                                                     |
| Guild Scheduled Event Update           | Guild scheduled event was updated                                                                     |
| Guild Scheduled Event Delete           | Guild scheduled event was deleted                                                                     |
| Guild Scheduled Event User Add         | User subscribed to a guild scheduled event                                                            |
| Guild Scheduled Event User Remove      | User unsubscribed from a guild scheduled event                                                        |
| Guild Soundboard Sound Create          | Guild soundboard sound was created                                                                    |
| Guild Soundboard Sound Update          | Guild soundboard sound was updated                                                                    |
| Guild Soundboard Sound Delete          | Guild soundboard sound was deleted                                                                    |
| Guild Soundboard Sounds Update         | Guild soundboard sounds were updated                                                                  |
| Soundboard Sounds                      | Response to Request Soundboard Sounds                                                                 |
| Integration Create                     | Guild integration was created                                                                         |
| Integration Update                     | Guild integration was updated                                                                         |
| Integration Delete                     | Guild integration was deleted                                                                         |
| Interaction Create                     | User used an interaction, such as an Application Command                                              |
| Invite Create                          | Invite to a channel was created                                                                       |
| Invite Delete                          | Invite to a channel was deleted                                                                       |
| Message Create                         | Message was created                                                                                   |
| Message Update                         | Message was edited                                                                                    |
| Message Delete                         | Message was deleted                                                                                   |
| Message Delete Bulk                    | Multiple messages were deleted at once                                                                |
| Message Reaction Add                   | User reacted to a message                                                                             |
| Message Reaction Remove                | User removed a reaction from a message                                                                |
| Message Reaction Remove All            | All reactions were explicitly removed from a message                                                  |
| Message Reaction Remove Emoji          | All reactions for a given emoji were explicitly removed from a message                                |
| Presence Update                        | User was updated                                                                                      |
| Stage Instance Create                  | Stage instance was created                                                                            |
| Stage Instance Update                  | Stage instance was updated                                                                            |
| Stage Instance Delete                  | Stage instance was deleted or closed                                                                  |
| Subscription Create                    | Premium App Subscription was created                                                                  |
| Subscription Update                    | Premium App Subscription was updated                                                                  |
| Subscription Delete                    | Premium App Subscription was deleted                                                                  |
| Typing Start                           | User started typing in a channel                                                                      |
| User Update                            | Properties about the user changed                                                                     |
| Voice Channel Effect Send              | Someone sent an effect in a voice channel the current user is connected to                            |
| Voice Channel Start Time Update        | Voice channel start time was updated                                                                  |
| Voice Channel Status Update            | Voice channel status was updated                                                                      |
| Voice State Update                     | Someone joined, left, or moved a voice channel                                                        |
| Voice Server Update                    | Guild's voice server was updated                                                                      |
| Webhooks Update                        | Guild channel webhook was created, update, or deleted                                                 |
| Message Poll Vote Add                  | User voted on a poll                                                                                  |
| Message Poll Vote Remove               | User removed a vote on a poll                                                                         |

## Hello (opcode 10)

Sent on connection to the websocket. Defines the heartbeat interval that an app should heartbeat to.

###### Hello Structure

| Field              | Type    | Description                                             |
| ------------------ | ------- | ------------------------------------------------------- |
| heartbeat_interval | integer | Interval (in milliseconds) an app should heartbeat with |

###### Example Hello

```json
{
  "op": 10,
  "d": {
    "heartbeat_interval": 45000
  }
}
```

## Ready

The ready event is dispatched when a client has completed the initial handshake with the gateway (for
new sessions). The ready event can be the largest and most complex event the gateway will send, as it
contains all the state required for a client to begin interacting with the rest of the platform.

`guilds` are the guilds of which your bot is a member. They start out as unavailable when you connect
to the gateway. As they become available, your bot will be notified via Guild Create events.

###### Ready Event Fields

| Field              | Type                                    | Description                                                          |
| ------------------ | --------------------------------------- | -------------------------------------------------------------------- |
| v                  | integer                                 | API version                                                          |
| user               | user object                             | Information about the user including email                           |
| guilds             | array of Unavailable Guild objects      | Guilds the user is in                                                |
| session_id         | string                                  | Used for resuming connections                                        |
| resume_gateway_url | string                                  | Gateway URL for resuming connections                                 |
| shard?             | array of two integers (shard_id, num_shards) | Shard information associated with this session, if sent when identifying |
| application        | partial application object              | Contains `id` and `flags`                                            |

Ready carries no example payload upstream. The user, Unavailable Guild and application objects are
REST resources; call the Skill tool with "discord-rest".

## Resumed

The resumed event is dispatched when a client has sent a resume payload to the gateway (for resuming
existing sessions). The upstream documents no payload fields for this event.

## Reconnect (opcode 7)

The reconnect event is dispatched when a client should reconnect to the gateway (and resume their
existing session, if they have one). This can occur at any point in the gateway connection lifecycle,
even before/in place of receiving a Hello event. A few seconds after the reconnect event is
dispatched, the connection may be closed by the server.

###### Example Gateway Reconnect

```json
{
  "op": 7,
  "d": null
}
```

## Invalid Session (opcode 9)

Sent to indicate one of at least three different situations:

* the gateway could not initialize a session after receiving an Opcode 2 Identify
* the gateway could not resume a previous session after receiving an Opcode 6 Resume
* the gateway has invalidated an active session and is requesting client action

The inner `d` key is a boolean that indicates whether the session may be resumable. See
`CONNECTION-LIFECYCLE.md` for connecting and resuming.

###### Example Gateway Invalid Session

```json
{
  "op": 9,
  "d": false
}
```

## Rate Limited

Sent when an app encounters a gateway rate limit for an event, such as Request Guild Members.

Info: see the change log entry "Introducing Rate Limit When Requesting All Guild Members" for more
information and timeline on this new rate limit.

###### Rate Limited Fields

| Field       | Type                            | Description                                                     |
| ----------- | ------------------------------- | --------------------------------------------------------------- |
| opcode      | integer                         | Gateway opcode of the event that was rate limited               |
| retry_after | float                           | The number of seconds to wait before submitting another request |
| meta        | Rate Limit Metadata for Opcode  | Metadata for the event that was rate limited                    |

###### Rate Limit Metadata for Opcode Structure

| Opcode | Type                                     |
| ------ | ---------------------------------------- |
| 8      | Request Guild Member Rate Limit Metadata |

###### Request Guild Member Rate Limit Metadata Structure

| Field    | Type      | Description                                        |
| -------- | --------- | -------------------------------------------------- |
| guild_id | snowflake | ID of the guild to get members for                 |
| nonce?   | string    | nonce to identify the Guild Members Chunk response |

## Where each remaining event is documented

- **Guilds, members, roles, scheduled events, soundboard, integrations, invites, auto moderation,
  channels, threads, entitlements** — `GATEWAY-EVENTS-GUILDS.md`
- **Messages, reactions, polls, presence, activity object, typing, user update** —
  `GATEWAY-EVENTS-MESSAGES.md`
- **Voice, webhooks, interactions, stage instances, subscriptions, application command permissions** —
  `GATEWAY-EVENTS-VOICE-AND-MISC.md`

## Source

Discord Developer Documentation,
[Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved 2026-08-26.
