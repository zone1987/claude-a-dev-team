# Gateway Connection Lifecycle

Connecting, heartbeating, identifying, resuming, disconnecting, rate limits, encoding and compression,
state tracking, guild availability, sharding, and the two Gateway REST endpoints.

Source: [Gateway](https://docs.discord.com/developers/events/gateway) and
[Overview of Events](https://docs.discord.com/developers/events/overview), retrieved 2026-08-26.

## Contents

- [What the Gateway is for](#what-the-gateway-is-for)
- [Transport methods for events](#transport-methods-for-events)
- [Sending events](#sending-events)
- [Receiving events](#receiving-events)
- [Dispatch events](#dispatch-events)
- [Connection lifecycle at a high level](#connection-lifecycle-at-a-high-level)
- [Connecting](#connecting)
- [Gateway URL query string params](#gateway-url-query-string-params)
- [Hello event](#hello-event)
- [Sending heartbeats](#sending-heartbeats)
- [Heartbeat requests](#heartbeat-requests)
- [Identifying](#identifying)
- [Ready event](#ready-event)
- [Disconnecting](#disconnecting)
- [Resuming](#resuming)
- [Rate limiting](#rate-limiting)
- [Encoding and compression](#encoding-and-compression)
- [Payload compression](#payload-compression)
- [ETF encoding](#etf-encoding)
- [Transport compression](#transport-compression)
- [Tracking state](#tracking-state)
- [Guild availability](#guild-availability)
- [Sharding](#sharding)
- [Max concurrency](#max-concurrency)
- [Sharding for large bots](#sharding-for-large-bots)
- [GET /gateway](#get-gateway)
- [GET /gateway/bot](#get-gatewaybot)
- [Session Start Limit Object](#session-start-limit-object)

## What the Gateway is for

The Gateway API lets apps open secure WebSocket connections with Discord to receive events about
actions that take place in a server/guild, like when a channel is updated or a role is created. There
are a few cases where apps will *also* use Gateway connections to update or request resources, like
when updating voice state.

Info: in *most* cases, performing REST operations on Discord resources can be done using the HTTP API
rather than the Gateway API.

The Gateway is Discord's form of real-time communication used by clients (including apps), so there are
nuances and data passed that simply isn't relevant to apps. Interacting with the Gateway can be
tricky, but there are community-built libraries with built-in support that simplify the most
complicated bits and pieces. If you're planning on writing a custom implementation, read the whole of
this file so you understand the sacred secrets of the Gateway (or at least those that matter for apps).

Gateway events are payloads sent over a Gateway connection — either from an app to Discord, or from
Discord to an app. An app typically *sends* events when connecting and managing its connection to the
Gateway, and *receives* events when listening to actions taking place in a server. All Gateway events
are encapsulated in a Gateway event payload.

###### Example Gateway Event

```json
{
  "op": 0,
  "d": {},
  "s": 42,
  "t": "GATEWAY_EVENT_NAME"
}
```

## Transport methods for events

Apps can listen to events happening in Discord to stay up-to-date with changes and updates to servers,
users, and even the app itself. There are many event types that can be accessed using different
transport methods:

* **Gateway events** are sent over a WebSocket connection between your app and Discord, and are the
  primary way to receive and send events. **Most events are only available via Gateway connections.**
  Most events related to resources in Discord, like updates to channels, guilds, roles, and messages,
  are only available over Gateway. To receive Gateway events, your app must open and maintain a
  persistent Gateway connection. Discord suggests using a developer library which helps set up,
  maintain, and handle common pitfalls with Gateway connections (like rate limits).
* **Webhook events** are sent to your app's Webhook Event URL over HTTP. While many events aren't
  supported over HTTP, some events like Application Authorized (sent when your app is installed to a
  user or server) aren't available using other transport methods like Gateway. See
  `WEBHOOK-EVENTS.md`.
* **SDK events** are sent to your app when using the Embedded App SDK. When developing Activities, you
  can listen to a collection of SDK events, like updates to a user's voice status or screen
  orientation. To listen to SDK events, call `subscribe()` with the SDK event name. Call the Skill tool
  with "discord-activities".

## Sending events

When sending a Gateway event (like when performing an initial handshake or updating presence), your app
must send an event payload object with a valid opcode (`op`) and inner data object (`d`).

Event payloads sent over a Gateway connection:

1. Must be serialized in plain-text JSON or binary ETF.
2. Must not exceed 4096 bytes. If an event payload *does* exceed 4096 bytes, the connection will be
   closed with a `4002` close event code.

All events your app can send are in `GATEWAY-EVENTS-SEND.md`. Specific rate limits apply when sending
events; see [Rate limiting](#rate-limiting).

## Receiving events

Receiving a Gateway event from Discord (like when a reaction is added to a message) is much more common
(and slightly more complex) than sending them.

While some events are sent to your app automatically, most events require your app to define intents
when Identifying. Intents are bitwise values that can be ORed (`|`) to indicate which events (or groups
of events) you want Discord to send your app. See `INTENTS.md`.

When receiving events, you can also configure *how* events will be sent to your app, like the encoding
and compression, or whether sharding should be enabled.

## Dispatch events

Dispatch (opcode `0`) events are the most common type of event your app will receive. *Most* Gateway
events which represent actions taking place in a guild will be sent to your app as Dispatch events.

When your app is parsing a Dispatch event:

* The `t` field can be used to determine which Gateway event the payload represents and the data you
  can expect in the `d` field.
* The `s` field represents the sequence number of the event, which is the relative order in which it
  occurred. You need to cache the most recent non-null `s` value for heartbeats, and to pass when
  Resuming a connection.

## Connection lifecycle at a high level

Gateway connections are persistent WebSockets which introduce more complexity than sending HTTP
requests or responding to interactions (like Slash Commands). When interacting with the Gateway, your
app must know how to open the initial connection, as well as maintain it and handle any disconnects.

Upstream illustrates this with a flowchart: "Flowchart with an overview of Gateway connection
lifecycle".

1. App establishes a connection with the Gateway after fetching and caching a WSS URL using the Get
   Gateway or Get Gateway Bot endpoint.
2. Discord sends the app a Hello (opcode `10`) event containing a heartbeat interval in milliseconds.
3. Start the Heartbeat interval. App must send a Heartbeat (opcode `1`) event, then continue to send
   them every heartbeat interval until the connection is closed.
   * Discord will respond to each Heartbeat event with a Heartbeat ACK (opcode `11`) event to confirm
     it was received. If an app doesn't receive a Heartbeat ACK, it should close the connection and
     reconnect.
   * Discord may send the app a Heartbeat (opcode `1`) event, in which case the app should send a
     Heartbeat event immediately.
4. App sends an Identify (opcode `2`) event to perform the initial handshake with the Gateway.
5. Discord sends the app a Ready (opcode `0`) event which indicates the handshake was successful and
   the connection is established. The Ready event contains a `resume_gateway_url` that the app should
   keep track of to determine the WebSocket URL an app should use to Resume.
6. The connection may be dropped for a variety of reasons at any time. Whether the app can Resume the
   connection or whether it must re-identify is determined by a variety of factors like the opcode and
   close code that it receives.
7. If an app **can** resume/reconnect, it should open a new connection using `resume_gateway_url` with
   the same version and encoding, then send a Resume (opcode `6`) event. If an app **cannot**
   resume/reconnect, it should open a new connection using the cached URL from step #1, then repeat the
   whole Gateway cycle. *Yipee!*

Info: there are nuances that aren't included in the overview above; the sections below carry them.

## Connecting

Before your app can establish a connection to the Gateway, it should call the Get Gateway or the Get
Gateway Bot endpoint. Either endpoint will return a payload with a `url` field whose value is the WSS
URL you can use to open a WebSocket connection. In addition to the URL, Get Gateway Bot contains
additional information about the recommended number of shards and the session start limits for your
app.

When initially calling either Get Gateway or Get Gateway Bot, you should cache the value of the `url`
field and use that when re-connecting to the Gateway.

When connecting to the URL, it's a good idea to explicitly pass the API version and encoding as query
parameters. You can also optionally include whether Discord should compress data that it sends your
app.

Info: `wss://gateway.discord.gg/?v=10&encoding=json` is an example of a WSS URL an app may use to
connect to the Gateway.

## Gateway URL query string params

| Field     | Type    | Description                                          | Accepted Values                |
| --------- | ------- | ---------------------------------------------------- | ------------------------------ |
| v         | integer | API Version to use                                   | API version                    |
| encoding  | string  | The encoding of received gateway packets             | `json` or `etf`                |
| compress? | string  | The optional transport compression of gateway packets | `zlib-stream` or `zstd-stream` |

## Hello event

Once connected to the Gateway, your app will receive a Hello (opcode `10`) event that contains your
connection's heartbeat interval (`heartbeat_interval`).

The heartbeat interval indicates a length of time in milliseconds that you should use to determine how
often your app needs to send a Heartbeat event in order to maintain the active connection.

###### Example Hello Event

```json
{
  "op": 10,
  "d": {
    "heartbeat_interval": 45000
  }
}
```

## Sending heartbeats

Heartbeats are pings used to let Discord know that your app is still actively using a Gateway
connection. After connecting to the Gateway, your app should send heartbeats in a background process
until the Gateway connection is closed.

When your app opens a Gateway connection, it will receive a Hello (opcode `10`) event which includes a
`heartbeat_interval` field that has a value representing a length of time in milliseconds.

Upon receiving the Hello event, your app should wait `heartbeat_interval * jitter` where `jitter` is
any random value between 0 and 1, then send its first Heartbeat (opcode `1`) event. From that point
until the connection is closed, your app must continually send Discord a heartbeat every
`heartbeat_interval` milliseconds. If your app fails to send a heartbeat event in time, your connection
will be closed and you will be forced to Resume.

When sending a heartbeat, your app will need to include the last sequence number your app received in
the `d` field. The sequence number is sent to your app in the event payload in the `s` field. If your
app hasn't received any events yet, you can just pass `null` in the `d` field.

Info: in the first heartbeat, `jitter` is an offset value between 0 and `heartbeat_interval` that is
meant to prevent too many clients (both desktop and apps) from reconnecting their sessions at the exact
same time (which could cause an influx of traffic).

You *can* send heartbeats before the `heartbeat_interval` elapses, but you should avoid doing so unless
necessary. There is already tolerance in the `heartbeat_interval` that will cover network latency, so
you don't need to account for it in your implementation.

When you send a Heartbeat event, Discord will respond with a Heartbeat ACK (opcode `11`) event, which
is an acknowledgement that the heartbeat was received:

###### Example Heartbeat ACK

```json
{
  "op": 11
}
```

Info: in the event of a service outage where you stay connected to the Gateway, you should continue to
send heartbeats and receive heartbeat ACKs. The Gateway will eventually respond and issue a session
once it's able to.

If a client does not receive a heartbeat ACK between its attempts at sending heartbeats, this may be
due to a failed or "zombied" connection. The client should immediately terminate the connection with
any close code besides `1000` or `1001`, then reconnect and attempt to Resume.

## Heartbeat requests

In addition to the Heartbeat interval, Discord may request additional heartbeats from your app by
sending a Heartbeat (opcode `1`) event. Upon receiving the event, your app should immediately send back
another Heartbeat event without waiting the remainder of the current interval.

Just like with the interval, Discord will respond with a Heartbeat ACK (opcode `11`) event.

## Identifying

After the connection is open and your app is sending heartbeats, you should send an Identify (opcode
`2`) event. The Identify event is an initial handshake with the Gateway that's required before your app
can begin sending or receiving most Gateway events.

Clients can also opt into a gateway capability in the Identify payload that changes how existing
gateway behaviors work — see the Gateway Capabilities table in `GATEWAY-EVENTS-SEND.md`.

Apps are limited by maximum concurrency (`max_concurrency` in the session start limit object) when
identifying. If your app exceeds this limit, Discord will respond with an Invalid Session (opcode `9`)
event.

After your app sends a valid Identify payload, Discord will respond with a Ready event which indicates
that your app is in a successfully-connected state with the Gateway. The Ready event is sent as a
standard Dispatch (opcode `0`).

Warning: clients are limited to 1000 `IDENTIFY` calls to the websocket in a 24-hour period. This limit
is global and across all shards, but does not include `RESUME` calls. Upon hitting this limit, all
active sessions for the app will be terminated, the bot token will be reset, and the owner will receive
an email notification. It's up to the owner to update their application with the new token.

###### Example Identify Payload

Below is a minimal `IDENTIFY` payload. `IDENTIFY` supports additional fields for other session
properties like payload compression and an initial presence state. See the Identify Structure in
`GATEWAY-EVENTS-SEND.md` for details about the event.

```json
{
  "op": 2,
  "d": {
    "token": "my_token",
    "intents": 513,
    "properties": {
      "os": "linux",
      "browser": "my_library",
      "device": "my_library"
    }
  }
}
```

## Ready event

As mentioned above, the Ready event is sent to your app after it sends a valid Identify payload. The
Ready event includes state, like the guilds your app is in, that it needs to start interacting with the
rest of the platform.

The Ready event also includes fields that you'll need to cache in order to eventually Resume your
connection after disconnects. Two fields in particular are important to call out:

* `resume_gateway_url` is a WebSocket URL that your app should use when it Resumes after a disconnect.
  The `resume_gateway_url` should be used instead of the URL used when connecting.
* `session_id` is the ID for the Gateway session for the new connection. It's required to know which
  stream of events were associated with your disconnected connection.

Full field list: `GATEWAY-EVENTS-RECEIVE-INDEX.md`.

## Disconnecting

Gateway disconnects happen for a variety of reasons, and may be initiated by Discord or by your app.

### Handling a disconnect

Due to Discord's architecture, disconnects are a semi-regular event and should be expected and handled.
When your app encounters a disconnect, it will typically be sent a close code which can be used to
determine whether you can reconnect and Resume the session, or whether you have to start over and
re-Identify.

After you determine whether or not your app can reconnect, you will do one of the following:

* If you determine that your app *can* reconnect and resume the previous session, then you should
  reconnect using the `resume_gateway_url` and `session_id` from the Ready event.
* If you *cannot* reconnect **or the reconnect fails**, you should open a new connection using the URL
  from the initial call to Get Gateway or Get Gateway Bot. In the case you cannot reconnect, you'll
  have to re-identify after opening a new connection.

The full close code table with the reconnect column is in `OPCODES-AND-STATUS-CODES.md`.

### Initiating a disconnect

When you close the connection to the gateway with close code `1000` or `1001`, your session will be
invalidated and your bot will appear offline.

If you simply close the TCP connection or use a different close code, the session will remain active
and timeout after a few minutes. This can be useful when you're Resuming the previous session.

## Resuming

When your app is disconnected, Discord has a process for reconnecting and resuming, which allows your
app to replay any lost events starting from the last sequence number it received. After Resuming, your
app will receive the missed events in the same way it would have had the connection stayed active.
Unlike the initial connection, your app does **not** need to re-Identify when Resuming.

There are a handful of scenarios when your app should attempt to resume:

1. It receives a Reconnect (opcode `7`) event
2. It's disconnected with a close code that indicates it can reconnect
3. It's disconnected but doesn't receive *any* close code
4. It receives an Invalid Session (opcode `9`) event with the `d` field set to `true`. This is an
   unlikely scenario, but it is possible.

### Preparing to resume

Before your app can send a Resume (opcode `6`) event, it will need three values: the `session_id` and
the `resume_gateway_url` from the Ready event, and the sequence number (`s`) from the last Dispatch
(opcode `0`) event it received before the disconnect.

After the connection is closed, your app should open a new connection using `resume_gateway_url` rather
than the URL used to initially connect, with the same query parameters from the initial Connection. If
your app doesn't use the `resume_gateway_url` when reconnecting, it will experience disconnects at a
higher rate than normal.

Once the new connection is opened, your app should send a Gateway Resume event using the `session_id`
and sequence number mentioned above. When sending the event, `session_id` will have the same field
name, but the last sequence number will be passed as `seq` in the data object (`d`).

When Resuming, you do not need to send an Identify event after opening the connection.

If successful, the Gateway will send the missed events in order, finishing with a Resumed event to
signal event replay has finished and that all subsequent events will be new.

Info: when resuming with the `resume_gateway_url` you need to provide the same version and encoding as
the initial connection.

It's possible your app won't reconnect in time to Resume, in which case it will receive an Invalid
Session (opcode `9`) event. If the `d` field is set to `false` (which is most of the time), your app
should disconnect. After disconnect, your app should create a new connection with your cached URL from
the Get Gateway or the Get Gateway Bot endpoint, then send an Identify (opcode `2`) event.

###### Example Gateway Resume Event

```json
{
  "op": 6,
  "d": {
    "token": "my_token",
    "session_id": "session_id_i_stored",
    "seq": 1337
  }
}
```

## Rate limiting

Info: this section refers to Gateway rate limits, not HTTP API rate limits.

Apps can send **120 gateway events per connection every 60 seconds**, meaning an average of 2 commands
per second. Apps that surpass the limit are immediately disconnected from the Gateway. Similar to other
rate limits, repeat offenders will have their API access revoked.

Apps also have a limit for concurrent Identify requests allowed per 5 seconds (`max_concurrency`). If
you hit this limit, the Gateway will respond with an Invalid Session (opcode `9`).

Other Gateway rate limit figures stated upstream:

* 1000 `IDENTIFY` calls per 24-hour period, global across all shards, excluding `RESUME` calls.
* Clients may only update their game status 5 times per 20 seconds.
* Session start limit `total` defaults to 1000 per day; for bots migrated to large bot sharding it is
  `max(2000, (guild_count / 1000) * 5)` per day.
* A new rate limit on the Request Guild Members opcode is being introduced; the gateway signals it with
  the Rate Limited receive event carrying `retry_after`.

## Encoding and compression

When establishing a connection to the Gateway, apps can use the `encoding` parameter to choose whether
to communicate with Discord using a plain-text JSON or binary ETF encoding. You can pick whichever
encoding type you're more comfortable with, but both have their own quirks. If you aren't sure which
encoding to use, JSON is generally recommended.

Apps can also optionally enable compression to receive zlib-compressed or zstd-compressed packets.
Payload compression can only be enabled when using a JSON encoding, but transport compression can be
used regardless of encoding type.

## Payload compression

When using the plain-text JSON encoding, apps have the option to enable payload compression.

Warning: if an app is using payload compression, it cannot use transport compression.

Payload compression enables optional per-packet compression for *some* events when Discord is sending
events over the connection.

Payload compression uses the zlib format (see RFC1950 2.2) when sending payloads. To enable payload
compression, your app can set `compress` to `true` when sending an Identify (opcode `2`) event. Note
that even when payload compression is enabled, not all payloads will be compressed.

When payload compression is enabled, your app (or library) *must* detect and decompress these payloads
to plain-text JSON before attempting to parse them. If you are using payload compression, the gateway
does not implement a shared compression context between events sent.

Payload compression will be disabled if you use transport compression.

## ETF encoding

When using ETF (External Term Format) encoding, there are some specific behaviors you should know:

* Snowflake IDs are transmitted as 64-bit integers or strings.
* Your app can't send compressed messages to the server.
* When sending payloads, you must use string keys. Using atom keys will result in a `4002` decode
  error.

See `erlpack` (github.com/discord/erlpack) for an ETF implementation example.

## Transport compression

Transport compression enables optional compression for all packets when Discord is sending events over
the connection. The currently-available transport compression options are `zlib-stream` and
`zstd-stream`.

### zlib-stream

When zlib transport compression is enabled, your app needs to process received data through a single
Gateway connection using a shared zlib context. However, each Gateway connection should use its own
unique zlib context.

When processing transport-compressed data, you should push received data to a buffer until you receive
the 4-byte `Z_SYNC_FLUSH` suffix (`00 00 ff ff`). After you receive the `Z_SYNC_FLUSH` suffix, you can
then decompress the buffer.

###### Transport Compression Example

```python
# Z_SYNC_FLUSH suffix
ZLIB_SUFFIX = b'\x00\x00\xff\xff'
# initialize a buffer to store chunks
buffer = bytearray()
# create a shared zlib inflation context to run chunks through
inflator = zlib.decompressobj()

# ...
def on_websocket_message(msg):
  # always push the message data to your cache
  buffer.extend(msg)

  # check if the last four bytes are equal to ZLIB_SUFFIX
  if len(msg) < 4 or msg[-4:] != ZLIB_SUFFIX:
    return

  # if the message *does* end with ZLIB_SUFFIX,
  # get the full message by decompressing the buffers
  # NOTE: the message is utf-8 encoded.
  msg = inflator.decompress(buffer)
  buffer = bytearray()

  # here you can treat `msg` as either JSON or ETF encoded,
  # depending on your `encoding` param
```

### zstd-stream

When zstd-stream transport compression is enabled, all data needs to be processed through a zstd
decompression context that stays alive for the lifetime of the gateway connection.

When processing data, each websocket message corresponds to a single gateway message, but does not end
a zstd frame. You will need to repeatedly call `ZSTD_decompressStream` until all data in the frame has
been processed (`ZSTD_decompressStream` will not necessarily return 0, though). Upstream points at the
`silviucpp/ezstd` Erlang + C++ implementation for inspiration.

## Tracking state

Most of a client's state is provided during the initial Ready event and in the Guild Create events that
follow.

As resources continue to be created, updated, and deleted, Gateway events are sent to notify the app of
these changes and to provide associated data. To avoid excessive API calls, apps should cache as many
relevant resource states as possible, and update them as new events are received.

Info: for larger apps, client state can grow to be very large. Discord recommends only storing data in
memory that is *needed* for the app to operate. In some cases, there isn't a need to cache member
information (like roles or permissions) since some events like `MESSAGE_CREATE` have the full member
object included.

An example of state tracking can be considered in the case of an app that wants to track member status:
when initially connecting to the Gateway, the app will receive information about the online status of
guild members (whether they're online, idle, dnd, or offline). To keep the state updated, the app will
track and parse Presence Update events as they're received, then update the cached member objects
accordingly.

## Guild availability

When connecting to the gateway as a bot user, guilds that the bot is a part of will start out as
unavailable. Don't fret — the gateway will automatically attempt to reconnect on your behalf. As guilds
become available to you, you will receive Guild Create events.

## Sharding

As apps grow and are added to an increasing number of guilds, some developers may find it necessary to
divide portions of their app's operations across multiple processes. As such, the Gateway implements a
method of user-controlled guild sharding which allows apps to split events across a number of Gateway
connections. Guild sharding is entirely controlled by an app, and requires no state-sharing between
separate connections to operate. While all apps *can* enable sharding, it's not necessary for apps in a
smaller number of guilds.

Warning: each shard can only support a maximum of **2500 guilds**, and apps that are in 2500+ guilds
*must* enable sharding.

To enable sharding on a connection, the app should send the `shard` array in the Identify payload. The
first item in this array should be the zero-based integer value of the current shard, while the second
represents the total number of shards.

Info: the Get Gateway Bot endpoint provides a recommended number of shards for your app in the `shards`
field.

To calculate which events will be sent to which shard, the following formula can be used:

###### Sharding Formula

```python
shard_id = (guild_id >> 22) % num_shards
```

As an example, if you wanted to split the connection between three shards, you'd use the following
values for `shard` for each connection: `[0, 3]`, `[1, 3]`, and `[2, 3]`.

Info: Gateway events that do not contain a `guild_id` will only be sent to the first shard
(`shard_id: 0`). This includes Direct Message (DM), subscription and entitlement events.

Note that `num_shards` does not relate to (or limit) the total number of potential sessions. It is only
used for *routing* traffic. As such, sessions do not have to be identified in an evenly-distributed
manner when sharding. You can establish multiple sessions with the same `[shard_id, num_shards]`, or
sessions with different `num_shards` values. This allows you to create sessions that will handle more or
less traffic for more fine-tuned load balancing, or to orchestrate "zero-downtime" scaling/updating by
handing off traffic to a new deployment of sessions with a higher or lower `num_shards` count that are
prepared in parallel.

## Max concurrency

If you have multiple shards, you may start them concurrently based on the `max_concurrency` value
returned to you on session start. Which shards you can start concurrently are assigned based on a key
for each shard. The rate limit key for a given shard can be computed with

```
rate_limit_key = shard_id % max_concurrency
```

This puts your shards into "buckets" of `max_concurrency` size. When you start your bot, you may start
up to `max_concurrency` shards at a time, and you must start them by "bucket" **in order**. To explain
another way, let's say you have 16 shards, and your `max_concurrency` is 16:

```
shard_id: 0, rate limit key (0 % 16): 0
shard_id: 1, rate limit key (1 % 16): 1
shard_id: 2, rate limit key (2 % 16): 2
shard_id: 3, rate limit key (3 % 16): 3
shard_id: 4, rate limit key (4 % 16): 4
shard_id: 5, rate limit key (5 % 16): 5
shard_id: 6, rate limit key (6 % 16): 6
shard_id: 7, rate limit key (7 % 16): 7
shard_id: 8, rate limit key (8 % 16): 8
shard_id: 9, rate limit key (9 % 16): 9
shard_id: 10, rate limit key (10 % 16): 10
shard_id: 11, rate limit key (11 % 16): 11
shard_id: 12, rate limit key (12 % 16): 12
shard_id: 13, rate limit key (13 % 16): 13
shard_id: 14, rate limit key (14 % 16): 14
shard_id: 15, rate limit key (15 % 16): 15
```

You may start all 16 of your shards at once, because each has a `rate_limit_key` which fills the bucket
of 16 shards. However, let's say you had 32 shards:

```
shard_id: 0, rate limit key (0 % 16): 0
shard_id: 1, rate limit key (1 % 16): 1
shard_id: 2, rate limit key (2 % 16): 2
shard_id: 3, rate limit key (3 % 16): 3
shard_id: 4, rate limit key (4 % 16): 4
shard_id: 5, rate limit key (5 % 16): 5
shard_id: 6, rate limit key (6 % 16): 6
shard_id: 7, rate limit key (7 % 16): 7
shard_id: 8, rate limit key (8 % 16): 8
shard_id: 9, rate limit key (9 % 16): 9
shard_id: 10, rate limit key (10 % 16): 10
shard_id: 11, rate limit key (11 % 16): 11
shard_id: 12, rate limit key (12 % 16): 12
shard_id: 13, rate limit key (13 % 16): 13
shard_id: 14, rate limit key (14 % 16): 14
shard_id: 15, rate limit key (15 % 16): 15
shard_id: 16, rate limit key (16 % 16): 0
shard_id: 17, rate limit key (17 % 16): 1
shard_id: 18, rate limit key (18 % 16): 2
shard_id: 19, rate limit key (19 % 16): 3
shard_id: 20, rate limit key (20 % 16): 4
shard_id: 21, rate limit key (21 % 16): 5
shard_id: 22, rate limit key (22 % 16): 6
shard_id: 23, rate limit key (23 % 16): 7
shard_id: 24, rate limit key (24 % 16): 8
shard_id: 25, rate limit key (25 % 16): 9
shard_id: 26, rate limit key (26 % 16): 10
shard_id: 27, rate limit key (27 % 16): 11
shard_id: 28, rate limit key (28 % 16): 12
shard_id: 29, rate limit key (29 % 16): 13
shard_id: 30, rate limit key (30 % 16): 14
shard_id: 31, rate limit key (31 % 16): 15
```

In this case, you must start the shard buckets **in "order"**. That means that you can start shard 0 ->
shard 15 concurrently, and then you can start shard 16 -> shard 31.

## Sharding for large bots

If your bot is in more than 150,000 guilds, there are some additional considerations you must take
around sharding. Discord will migrate your bot to large bot sharding when it starts to get near the
large bot sharding threshold. The bot owner(s) will receive a system DM and email confirming this move
has completed as well as what shard number has been assigned.

The number of shards you run must be a multiple of the shard number provided when reaching out to you.
If you attempt to start your bot with an invalid number of shards, your Gateway connection will close
with a `4010` Invalid Shard close code.

The Get Gateway Bot endpoint will always return the correct amount of shards, so if you're already
using this endpoint to determine your number of shards, you shouldn't require any changes.

The session start limit for these bots will also be increased from 1000 to
`max(2000, (guild_count / 1000) * 5)` per day. You also receive an increased `max_concurrency`, the
number of shards you can concurrently start.

## GET /gateway

### GET /gateway

Info: this endpoint does not require authentication.

Returns an object with a valid WSS URL which the app can use when Connecting to the Gateway. Apps
should cache this value and only call this endpoint to retrieve a new URL when they are unable to
properly establish a connection using the cached one.

###### Example Response

```json
{
  "url": "wss://gateway.discord.gg/"
}
```

## GET /gateway/bot

### GET /gateway/bot

Warning: this endpoint requires authentication using a valid bot token.

Returns an object based on the information in Get Gateway, plus additional metadata that can help
during the operation of large or sharded bots. Unlike Get Gateway, this route should not be cached for
extended periods of time as the value is not guaranteed to be the same per-call, and changes as the bot
joins/leaves guilds.

###### JSON Response

| Field               | Type                          | Description                                              |
| ------------------- | ----------------------------- | -------------------------------------------------------- |
| url                 | string                        | WSS URL that can be used for connecting to the Gateway   |
| shards              | integer                       | Recommended number of shards to use when connecting      |
| session_start_limit | session_start_limit object    | Information on the current session start limit            |

###### Example Response

```json
{
  "url": "wss://gateway.discord.gg/",
  "shards": 9,
  "session_start_limit": {
    "total": 1000,
    "remaining": 999,
    "reset_after": 14400000,
    "max_concurrency": 1
  }
}
```

## Session Start Limit Object

###### Session Start Limit Structure

| Field           | Type    | Description                                                    |
| --------------- | ------- | -------------------------------------------------------------- |
| total           | integer | Total number of session starts the current user is allowed     |
| remaining       | integer | Remaining number of session starts the current user is allowed |
| reset_after     | integer | Number of milliseconds after which the limit resets            |
| max_concurrency | integer | Number of identify requests allowed per 5 seconds              |

## Source

Discord Developer Documentation:
[Gateway](https://docs.discord.com/developers/events/gateway) and
[Overview of Events](https://docs.discord.com/developers/events/overview), retrieved 2026-08-26.
