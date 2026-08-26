---
name: discord-gateway
description: "Discord Gateway WebSocket: connecting, resuming, sharding, intents, event payloads, opcodes. Use when the request names the Discord Gateway, an intent, or a GUILD_ event."
---

# Discord Gateway

The Gateway is Discord's real-time WebSocket API. An app opens a persistent connection, identifies with
a token and an intent bitfield, heartbeats to keep the socket alive, and receives Dispatch events for
everything happening in the guilds it is installed in. A few events travel the other way: requesting
guild members, joining voice, updating presence. Everything else belongs on the HTTP API.

## The connection state machine

1. `GET /gateway` (or `GET /gateway/bot` for shard count and session limits) returns a WSS `url`. Cache
   it. Connect with `?v=10&encoding=json`, optionally `&compress=zlib-stream` or `zstd-stream`.
2. **Hello (op 10)** arrives with `heartbeat_interval` in milliseconds.
3. Wait `heartbeat_interval * jitter` (jitter random 0–1), then send **Heartbeat (op 1)** carrying the
   last sequence number `s` in `d` (`null` if none yet). Repeat every interval. Each is answered by
   **Heartbeat ACK (op 11)**. A missing ACK means a zombied connection: close with any code *except*
   1000 or 1001 (those invalidate the session), then resume.
4. Send **Identify (op 2)** with `token`, `properties` and `intents`. Discord answers **Ready**, which
   carries `session_id` and `resume_gateway_url` — cache both, plus the running `s`.
5. On a drop, **resume**: reconnect to `resume_gateway_url` with the same version and encoding, send
   **Resume (op 6)** with `token`, `session_id` and `seq`. Replay ends with **Resumed**.
6. Or **re-identify**: open a new socket from the *cached* `GET /gateway` URL and start at step 2.

Resume on **Reconnect (op 7)**, on **Invalid Session (op 9)** with `d: true`, on no close code at all,
and on close codes `4000`, `4001`, `4002`, `4003`, `4005`, `4007`, `4008`, `4009`. Re-identify on
Invalid Session with `d: false`. **Stop reconnecting** on `4004` (bad token), `4010` (invalid shard),
`4011` (sharding required), `4012` (bad API version), `4013` (invalid intents), `4014` (disallowed
intents) — retrying these loops forever without fixing the cause.

**A missing privileged intent does not raise an error.** The event still arrives, with the gated fields
empty — an empty `content` string reads exactly like a parsing bug. The three privileged intents are
`GUILD_PRESENCES`, `GUILD_MEMBERS` and `MESSAGE_CONTENT`; each must be toggled in the Developer Portal
*and* requested in the `intents` bitfield. Enabled in one place only closes the socket with `4014`.
Past 10,000 unique users they need review.

Hard limits: 120 events per connection per 60 seconds; 1000 IDENTIFYs per 24 hours globally across
shards (exceeding it resets the bot token); payloads at most 4096 bytes; 2500 guilds per shard; 5
status updates per 20 seconds.

## Reference map

- **[references/CONNECTION-LIFECYCLE.md](references/CONNECTION-LIFECYCLE.md)**: the full lifecycle —
  3 URL query params, Hello, heartbeating, identifying, Ready, disconnecting, resuming, every rate
  limit figure, JSON and ETF encoding, payload plus both transport compressions with the worked Python
  example, state tracking, guild availability, sharding formula, `max_concurrency` buckets, large-bot
  sharding, and the 2 Gateway REST endpoints with the session start limit object.
- **[references/INTENTS.md](references/INTENTS.md)**: all 21 intent bits with their values and the exact
  event list each gates, the 3 footnotes, the caveats, the 3 privileged intents, the review threshold
  and 5-step process, Gateway and HTTP restrictions, message content exceptions, and per-intent
  alternatives with decision checklists.
- **[references/GATEWAY-EVENTS-SEND.md](references/GATEWAY-EVENTS-SEND.md)**: the payload envelope
  (`op`, `d`, `s`, `t`) and all 8 send events, every field — Identify with Gateway Capabilities and
  connection properties, Resume, Heartbeat, Request Guild Members, Request Soundboard Sounds, Request
  Channel Info, Update Voice State, Update Presence with its 5 status types.
- **[references/GATEWAY-EVENTS-RECEIVE-INDEX.md](references/GATEWAY-EVENTS-RECEIVE-INDEX.md)**: the
  complete upstream table of all 82 receive events, plus the fields of Hello, Ready, Resumed, Reconnect,
  Invalid Session and Rate Limited.
- **[references/GATEWAY-EVENTS-GUILDS.md](references/GATEWAY-EVENTS-GUILDS.md)**: 51 events across auto
  moderation, channels, Channel Info, voice channel status and start time, threads, channel pins,
  entitlements, guilds with the 12 Guild Create extra fields, members, Guild Members Chunk, roles,
  scheduled events, soundboard sounds, integrations and invites.
- **[references/GATEWAY-EVENTS-MESSAGES.md](references/GATEWAY-EVENTS-MESSAGES.md)**: 13 events —
  message create/update/delete/delete-bulk, 4 reaction events, 2 poll vote events, Presence Update,
  client status — plus the complete activity object: 18 fields, 6 types, 3 status display types,
  timestamps, emoji, party, assets, asset image, secrets, 9 flags, buttons, both examples.
- **[references/GATEWAY-EVENTS-VOICE-AND-MISC.md](references/GATEWAY-EVENTS-VOICE-AND-MISC.md)**: 12
  events — application command permissions update, Voice Channel Effect Send with its 2 animation
  types, Voice State Update, Voice Server Update, Webhooks Update, Interaction Create, 3 stage instance
  and 3 subscription events.
- **[references/OPCODES-AND-STATUS-CODES.md](references/OPCODES-AND-STATUS-CODES.md)**: every numeric
  code — 13 Gateway opcodes, 14 Gateway close codes with the reconnect column, 23 voice opcodes, 16
  voice close codes, 12 HTTP response codes, all 240 JSON error codes, 16 RPC error and 6 RPC close
  codes.
- **[references/WEBHOOK-EVENTS.md](references/WEBHOOK-EVENTS.md)**: HTTP webhook events — subscribing,
  the PING handshake, `X-Signature-Ed25519` validation, the 3-second/204 rule, the payload envelope,
  all 12 event types with structures and examples, and the 3 Social SDK message objects.

## Related

Call the Skill tool with "discord-rest" for the guild, channel, message, user and entitlement objects
these events carry.
Call the Skill tool with "discord-interactions" for the Interaction object behind `INTERACTION_CREATE`.
Call the Skill tool with "discord-bots" for building, hosting and scaling a bot on this Gateway.

## Source

Distilled from the Discord Developer Documentation, retrieved 2026-08-26:

- https://docs.discord.com/developers/events/gateway
- https://docs.discord.com/developers/events/gateway-events
- https://docs.discord.com/developers/events/overview
- https://docs.discord.com/developers/events/webhook-events
- https://docs.discord.com/developers/gateway/getting-started-with-privileged-intent-review
- https://docs.discord.com/developers/gateway/you-might-not-need-a-privileged-intent
- https://docs.discord.com/developers/topics/opcodes-and-status-codes
