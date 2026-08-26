# Gateway versus HTTP Interactions

The transport choice decides whether local development needs a public URL. This file states what
each transport demands, and gives the complete HTTP endpoint contract.

## Contents

- [Mutually exclusive, and what that means locally](#mutually-exclusive-and-what-that-means-locally)
- [Side by side](#side-by-side)
- [The HTTP endpoint contract](#the-http-endpoint-contract)
  - [1. Acknowledge PING](#1-acknowledge-ping)
  - [2. Verify the Ed25519 signature](#2-verify-the-ed25519-signature)
  - [What Discord does to an endpoint that fails either check](#what-discord-does-to-an-endpoint-that-fails-either-check)
  - [Adding the URL in the portal](#adding-the-url-in-the-portal)
- [Interaction types your endpoint must switch on](#interaction-types-your-endpoint-must-switch-on)
- [Responding: the two shapes](#responding-the-two-shapes)
- [Response deadlines and the token window](#response-deadlines-and-the-token-window)
- [Followup endpoints](#followup-endpoints)
- [The Gateway path](#the-gateway-path)
  - [Connection lifecycle](#connection-lifecycle)
  - [Identify](#identify)
  - [Heartbeats](#heartbeats)
  - [Intents](#intents)
  - [Gateway rate limits](#gateway-rate-limits)
- [Where the documentation is silent](#where-the-documentation-is-silent)

## Mutually exclusive, and what that means locally

> Your app can receive an interaction in one of two ways:
>
> * Via Interaction Create gateway event
> * Via outgoing webhook
>
> These two methods are **mutually exclusive**; you can *only* receive Interactions one of the two
> ways. The `INTERACTION_CREATE` Gateway Event may be handled by connected clients, while the
> webhook method detailed below does not require a connected client.

Which one is active is decided by whether an Interactions Endpoint URL is configured:

> By default your app will receive interactions via a Gateway connection, but you can opt-in to
> HTTP-based interactions by adding a **Interactions Endpoint URL** to your app's settings.

> A **Interactions Endpoint URL** is a public endpoint for your app where Discord can send your app
> HTTP-based interactions. If your app is using Gateway-based interactions, you don't need to
> configure an Interactions Endpoint URL.

**The local consequence.** A Gateway bot dials out over WebSocket, so it works from any machine with
outbound internet — no port forwarding, no tunnel, no HTTPS certificate. An HTTP-interactions bot
receives inbound POSTs from Discord's servers, so a locally-bound port at `localhost:3000` is
unreachable and something must expose it publicly. That is the whole reason the tutorials introduce
a tunnel.

The platform overview frames the trade-off:

> By default, your app receives interactions over the Gateway, the same persistent WebSocket
> connection used for all other real-time events. If your bot is already connected to the Gateway to
> listen for messages, member joins, or other activity, interactions arrive through the same
> connection.

> Alternatively, you can configure an **Interactions Endpoint URL** in your app's settings to receive
> interactions as HTTP POST requests sent directly to your server. Discord handles delivery and your
> app needs to respond within a few seconds.
>
> This model works well for apps that only need to respond to commands and UI components. No
> persistent connection is required and it scales naturally with standard web infrastructure. To use
> it, your endpoint must validate Discord's request signatures and handle the initial `PING`
> handshake.

## Side by side

| | Gateway | HTTP interactions |
|---|---|---|
| Direction | app dials out, WebSocket (WSS) | Discord POSTs in |
| Public URL needed locally | **no** | **yes**, HTTPS |
| Tunnel needed locally | no | yes, per the tutorials |
| Endpoint config in portal | none | Interactions Endpoint URL on General Information |
| Signature verification | not applicable | **mandatory** (Ed25519) |
| `PING` handshake | not applicable | **mandatory** |
| Connection state | persistent, heartbeats, resume | stateless requests |
| Intents | required to receive most events | not applicable to interaction delivery |
| Sending responses | still over HTTP | over HTTP, or inline in the response body |
| Receives non-interaction events | yes (guild, message, member events) | no |

`GET /gateway` returns the WSS URL and "does not require authentication". `GET /gateway/bot`
"requires authentication using a valid bot token" and adds `shards` and `session_start_limit`.

## The HTTP endpoint contract

Two things must both work before the URL will save:

> Before you can add your Interactions Endpoint URL to your app, your endpoint must be prepared for
> two things ahead of time:
>
> 1. Acknowledging `PING` requests from Discord
> 2. Validate security-related request headers (`X-Signature-Ed25519` and `X-Signature-Timestamp`)
>
> If either of these are not complete, your Interactions Endpoint URL will not be validated.

### 1. Acknowledge PING

> When adding your Interactions Endpoint URL, Discord will send a `POST` request with a `PING`
> payload with a `type: 1` to your endpoint. Your app is expected to acknowledge the request by
> returning a `200` response with a `PONG` payload (which has the same `type: 1`).

> You must provide a valid `Content-Type` when responding to `PING`s.

Upstream's example, verbatim:

```py
@app.route('/', methods=['POST'])
def my_command():
    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })
```

Note the symmetry that trips people up: interaction **type** `PING` is `1`, and interaction
callback **type** `PONG` is also `1`. They are different enums with the same value.

The Cloudflare Workers sample handles it explicitly, and the comment states why:

```js
router.post('/', async (request, env) => {
  const message = await request.json();
  console.log(message);
  if (message.type === InteractionType.PING) {
    // The `PING` message is used during the initial webhook handshake, and is
    // required to configure the webhook in the developer portal.
    console.log('Handling Ping request');
    return new JsonResponse({
      type: InteractionResponseType.PONG,
    });
  }
```

### 2. Verify the Ed25519 signature

> The internet is a scary place, especially for people hosting public, unauthenticated endpoints. To
> receive interactions via HTTP, there are some security steps you **must** take before your app is
> eligible to receive requests.
>
> Each interaction is sent with the following headers:
>
> * `X-Signature-Ed25519` as a signature
> * `X-Signature-Timestamp` as a timestamp
>
> Using your favorite security library, you **must validate the request each time you receive an
> interaction**. If the signature fails validation, your app should respond with a `401` error code.

The signed message is `timestamp + body`, verified against the app's **Public Key** from the
General Information page. Three implementations, verbatim from upstream.

**JavaScript**

```js
const nacl = require("tweetnacl");

// Your public key can be found on your application in the Developer Portal
const PUBLIC_KEY = "APPLICATION_PUBLIC_KEY";

const signature = req.get("X-Signature-Ed25519");
const timestamp = req.get("X-Signature-Timestamp");
const body = req.rawBody; // rawBody is expected to be a string, not raw bytes

const isVerified = nacl.sign.detached.verify(
    Buffer.from(timestamp + body),
    Buffer.from(signature, "hex"),
    Buffer.from(PUBLIC_KEY, "hex")
);

if (!isVerified) {
    return res.status(401).end("invalid request signature");
}
```

**Python**

```py
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

# Your public key can be found on your application in the Developer Portal
PUBLIC_KEY = 'APPLICATION_PUBLIC_KEY'

verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

signature = request.headers["X-Signature-Ed25519"]
timestamp = request.headers["X-Signature-Timestamp"]
body = request.data.decode("utf-8")

try:
    verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
except BadSignatureError:
    abort(401, 'invalid request signature')
```

**Java**

> We will use `tink-java` ([`com.google.crypto.tink:tink:1.22.0`](https://mvnrepository.com/artifact/com.google.crypto.tink/tink/1.22.0)),
> the minimum Java version required is 11.

```java
import com.google.crypto.tink.subtle.Ed25519Verify;
import com.google.crypto.tink.subtle.Hex;

import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;

public class Ed25519WebhookVerifier {
    private final Ed25519Verify verifier;

    public Ed25519WebhookVerifier(String publicKey) {
        this.verifier = new Ed25519Verify(Hex.decode(publicKey));
    }

    public boolean verify(String signature, String timestamp, String body) {
        try {
            verifier.verify(Hex.decode(signature), (timestamp + body).getBytes(StandardCharsets.UTF_8));
            return true;
        } catch (GeneralSecurityException e) {
            return false;
        }
    }
}
```

```java
// Your public key can be found on your application in the Developer Portal
var verifier = new Ed25519WebhookVerifier("PUBLIC_KEY");

// Get those from your favorite web server library
// The "X-Signature-Ed25519" header
String signature;
// The "X-Signature-Timestamp" header
String timestamp;
// Request body
String body;
if (!verifier.verify(signature, timestamp, body)) {
    // Signature is invalid, return an HTTP 401 response
    throw new UnsupportedOperationException("Return a HTTP 401 response");
}
```

The Cloudflare Workers sample does the same at the Worker entry point:

```js
export default {
  /**
   * Every request to a worker will start in the `fetch` method.
   * Verify the signature with the request, and dispatch to the router.
   * @param {*} request A Fetch Request object
   * @param {*} env A map of key/value pairs with env vars and secrets from the cloudflare env.
   * @returns
   */
  async fetch(request, env) {
    if (request.method === 'POST') {
      // Using the incoming headers, verify this request actually came from discord.
      const signature = request.headers.get('x-signature-ed25519');
      const timestamp = request.headers.get('x-signature-timestamp');
      const body = await request.clone().arrayBuffer();
      const isValidRequest = verifyKey(
        body,
        signature,
        timestamp,
        env.DISCORD_PUBLIC_KEY
      );
      if (!isValidRequest) {
        console.error('Invalid Request');
        return new Response('Bad request signature.', { status: 401 });
      }
    }

    // Dispatch the request to the appropriate route
    return router.handle(request, env);
  },
};
```

**The raw body is what gets verified.** The JavaScript comment says `rawBody is expected to be a
string, not raw bytes`, and the Worker sample clones the request to read an `arrayBuffer`. A
framework that has already parsed and re-serialised JSON will produce a different byte sequence and
the signature will fail. The Getting Started guide's app solves this by hooking Express's parser:

> It uses the `PUBLIC_KEY` and discord-interactions package with a wrapper function (imported from
> `utils.js`) that makes it conform to
> [Express's `verify` interface](http://expressjs.com/en/5x/api.html#express.json). This is run on
> every incoming request to your app.

### What Discord does to an endpoint that fails either check

At save time: "If either of these are not complete, your Interactions Endpoint URL will not be
validated."

Afterwards, and this is the part that catches people who verified once and then loosened the check:

> In addition to ensuring your app validates security-related request headers at the time of saving
> your endpoint, Discord will also perform automated, routine security checks against your endpoint,
> including purposefully sending you invalid signatures. If you fail the validation, we will remove
> your interactions URL and alert you via email and System DM.

So an endpoint that returns `200` to a bad signature gets its URL **removed** — the app silently
stops receiving interactions, and the notice arrives by email and System DM rather than in your
logs. An endpoint that always returns `401`, including to genuine requests, also never validates.

### Adding the URL in the portal

> After you have a public endpoint to use as your app's Interactions Endpoint URL, you can add it to
> your app by going to your [app's settings](https://discord.com/developers/applications).
>
> On the [**General Information** page](https://discord.com/developers/applications/select/information),
> look for the **Interactive Endpoint URL** field. Paste your public URL that is set up to
> acknowledge `PING` messages and correctly handles security-related signature headers.

The tutorials append the route path to the tunnel URL — see
[LOCAL-WORKFLOW.md](LOCAL-WORKFLOW.md) for the exact steps and the troubleshooting note.

## Interaction types your endpoint must switch on

| Name | Value |
| ---- | ----- |
| PING | 1 |
| APPLICATION_COMMAND | 2 |
| MESSAGE_COMPONENT | 3 |
| APPLICATION_COMMAND_AUTOCOMPLETE | 4 |
| MODAL_SUBMIT | 5 |

The `data` payload varies by type:

| Interaction Type | Interaction Data |
| ---- | ---- |
| PING (`1`) | N / A |
| APPLICATION_COMMAND (`2`) | Application Command Data Structure |
| MESSAGE_COMPONENT (`3`) | Message Component Data Structure |
| APPLICATION_COMMAND_AUTOCOMPLETE (`4`) | Application Command Data Structure |
| MODAL_SUBMIT (`5`) | Modal Submit Data Structure |

> While the `data` field is guaranteed to be present for all interaction types besides `PING`, its
> structure will vary.

Interaction context types — where the interaction came from, which matters when testing the same
command in a guild, in your bot's DM, and in a group DM:

| Name | Type | Description |
| ---- | ---- | ---- |
| GUILD | 0 | Interaction can be used within servers |
| BOT_DM | 1 | Interaction can be used within DMs with the app's bot user |
| PRIVATE_CHANNEL | 2 | Interaction can be used within Group DMs and DMs other than the app's bot user |

> With interaction context, something to keep in mind in `BOT_DM` is only the *DM with your bot
> user*. If you run the same command in a DM with your bestie, or in a group DM, the interaction
> context will be `PRIVATE_CHANNEL` (`2`).

**Where the invoking user's ID lives differs by context**, and this is a common local bug:

> `member` is sent when the interaction is invoked in a guild, and `user` is sent when invoked in a DM

The sample app's handling, verbatim:

```javascript
// Interaction context
const context = req.body.context;
// User ID is in user field for (G)DMs, and member for servers
const userId = context === 0 ? req.body.member.user.id : req.body.user.id;
```

A sample interaction request body from the user-installable tutorial, condensed by upstream for
readability — useful as a shape to compare your logs against:

```json
{
  "app_permissions": "442368",
  "application_id": "234248956100616262",
  "authorizing_integration_owners": { "1": "1090372582781497424" },
  "channel": {
    // Partial channel object corresponding to channel_id
  },
  "channel_id": "1234563982236504123",
  "context": 1,
  "data": { "id": "1234358421659193405", "name": "link", "type": 1 },
  "entitlements": [],
  "id": "1234968734674853908",
  "locale": "en-US",
  "token": "a really long interactions token that your app can use to respond to the interactions",
  "type": 2,
  "user": {
    // Partial user object
  },
  "version": 1
}
```

Other fields worth watching while debugging locally:

- **`app_permissions`** — "Bitwise set of permissions the app has in the source location of the
  interaction". It "includes `ATTACH_FILES | EMBED_LINKS | MENTION_EVERYONE` permissions for (G)DMs
  with other users, and additionally includes `USE_EXTERNAL_EMOJIS` for DMs with the app's bot
  user." So the permissions your app has genuinely differ between a guild channel, a bot DM and a
  group DM.
- **`authorizing_integration_owners`** — a map from installation context to user or guild ID. "If
  the key is `GUILD_INSTALL` (`"0"`) … the value will be the guild ID if the interaction is
  triggered from a server; the value will be `"0"` if the interaction is triggered from a DM with
  the app's bot user. If the key is `USER_INSTALL` (`"1"`), the value will be the ID of the
  authorizing user." And: "`authorizing_integration_owners` is not the same as the user that
  triggered the interaction."
- **`locale`** — "This is available on all interaction types except PING".
- **`token`** — "Continuation token for responding to the interaction".
- **`version`** — "Read-only property, always `1`".
- **`attachment_size_limit`** — attachment size limit in bytes.

## Responding: the two shapes

**Callback endpoint.**

> When responding to an interaction received, you can make a `POST` request to
> `/interactions/<interaction_id>/<interaction_token>/callback`. `interaction_id` is the unique id of
> that individual Interaction from the received payload. `interaction_token` is the unique token for
> that interaction from the received payload.

```py
import requests

url = "https://discord.com/api/v10/interactions/<interaction_id>/<interaction_token>/callback"

json = {
    "type": 4,
    "data": {
        "content": "Congrats on sending your command!"
    }
}
r = requests.post(url, json=json)
```

> If you are receiving Interactions over the gateway, you **have to respond via HTTP**. Responses to
> Interactions **are not sent as commands over the gateway**.

> **If you send this request for an interaction received over HTTP, respond to the original HTTP
> request with a 202 and no body.**

**Inline in the HTTP response**, which is what the Express and Worker samples do:

> If you receive interactions over HTTP, your server can also respond to the received `POST`
> request. You'll want to respond with a `200` status code (if everything went well), as well as
> specifying a `type` and `data`, which is an Interaction Response object:

```py
@app.route('/', methods=['POST'])
def my_command():
    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })

    else:
        return jsonify({
            "type": 4,
            "data": {
                "tts": False,
                "content": "Congrats on sending your command!",
                "embeds": [],
                "allowed_mentions": { "parse": [] }
            }
        })
```

Interaction callback types:

| Name | Value | Description |
| ---- | ----- | ---- |
| PONG | 1 | ACK a `Ping` |
| CHANNEL_MESSAGE_WITH_SOURCE | 4 | Respond to an interaction with a message |
| DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE | 5 | ACK an interaction and edit a response later, the user sees a loading state |
| DEFERRED_UPDATE_MESSAGE\* | 6 | For components, ACK an interaction and edit the original message later; the user does not see a loading state |
| UPDATE_MESSAGE\* | 7 | For components, edit the message the component was attached to |
| APPLICATION_COMMAND_AUTOCOMPLETE_RESULT | 8 | Respond to an autocomplete interaction with suggested choices |
| MODAL\*\* | 9 | Respond to an interaction with a popup modal |
| PREMIUM_REQUIRED | 10 | **Deprecated**; respond to an interaction with an upgrade button, only available for apps with monetization enabled |
| LAUNCH_ACTIVITY | 12 | Launch the Activity associated with the app. Only available for apps with Activities enabled |

\* Only valid for component-based interactions
\*\* Not available for `MODAL_SUBMIT` and `PING` interactions.

`POST .../callback` "Returns `204` unless `with_response` is set to `true` which returns `200` with
the body as interaction callback response."

**Type 5 is the answer to slow local work.** If your handler talks to a database, a game server, or
anything else that might exceed 3 seconds, ACK first with
`DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE` and edit afterwards. One constraint:

> If you create a callback with the type `DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE` the only valid
> message flag you may use is `EPHEMERAL`. If you'd like to create a component based message with
> `IS_COMPONENTS_V2` you must do that with the edit original response endpoint, not this one.

## Response deadlines and the token window

> Interaction `tokens` are valid for **15 minutes** and can be used to send followup messages but
> you **must send an initial response within 3 seconds of receiving the event**. If the 3 second
> deadline is exceeded, the token will be invalidated.

> Interaction tokens are valid for **15 minutes**, meaning you can respond to an interaction within
> that amount of time.

The platform page puts the same figure loosely: "Discord handles delivery and your app needs to
respond within a few seconds." Treat 3 seconds as the number.

## Followup endpoints

> * `PATCH /webhooks/<application_id>/<interaction_token>/messages/@original` to edit your initial response to an Interaction
> * `DELETE /webhooks/<application_id>/<interaction_token>/messages/@original` to delete your initial response to an Interaction
> * `POST /webhooks/<application_id>/<interaction_token>` to send a new followup message
> * `PATCH /webhooks/<application_id>/<interaction_token>/messages/<message_id>` to edit a message sent with that `token`

Full list, with methods:

### POST /interactions/{interaction.id}/{interaction.token}/callback
Create a response to an Interaction. Query param `with_response?` (boolean) — whether to include an
interaction callback object as the response. Supports file attachments and `multipart/form-data`.

### GET /webhooks/{application.id}/{interaction.token}/messages/@original
Returns the initial Interaction response.

### PATCH /webhooks/{application.id}/{interaction.token}/messages/@original
Edits the initial Interaction response.

### DELETE /webhooks/{application.id}/{interaction.token}/messages/@original
Deletes the initial Interaction response. Returns `204 No Content` on success.

### POST /webhooks/{application.id}/{interaction.token}
Create a followup message. "Functions the same as Execute Webhook, but `wait` is always true. The
`thread_id`, `avatar_url`, and `username` parameters are not supported when using this endpoint for
interaction followups. You can use the `EPHEMERAL` message flag `1 << 6` (64) to send a message that
only the user can see. You can also use the `IS_COMPONENTS_V2` message flag `1 << 15` (32768) to
send a component-based message."

> Apps are limited to 5 followup messages per interaction if it was initiated from a user-installed
> app and isn't installed in the server (meaning the authorizing integration owners object only
> contains `USER_INSTALL`)

> When using this endpoint directly after responding to an interaction with
> `DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE`, this endpoint will function as Edit Original Interaction
> Response for backwards compatibility. In this case, no new message will be created, and the
> loading message will be edited instead. The ephemeral flag will be ignored, and the value you
> provided in the initial defer response will be preserved, as an existing message's ephemeral state
> cannot be changed. This behavior is deprecated, and you should use the Edit Original Interaction
> Response endpoint in this case instead.

### GET /webhooks/{application.id}/{interaction.token}/messages/{message.id}
Returns a followup message.

### PATCH /webhooks/{application.id}/{interaction.token}/messages/{message.id}
Edits a followup message.

### DELETE /webhooks/{application.id}/{interaction.token}/messages/{message.id}
Deletes a followup message. Returns `204 No Content` on success.

Two rate-limit facts about these:

> The endpoints below are not bound to the application's Global Rate Limit.

> Interactions webhooks share the same rate limit properties as normal webhooks.

> Interaction responses have the same header requirements as normal HTTP API requests.

## The Gateway path

### Connection lifecycle

> 1. App establishes a connection with the Gateway after fetching and caching a WSS URL using the Get Gateway or Get Gateway Bot endpoint.
> 2. Discord sends the app a Hello (opcode `10`) event containing a heartbeat interval in milliseconds.
> 3. Start the Heartbeat interval. App must send a Heartbeat (opcode `1`) event, then continue to send them every heartbeat interval until the connection is closed.
>    * Discord will respond to each Heartbeat event with a Heartbeat ACK (opcode `11`) event to confirm it was received. If an app doesn't receive a Heartbeat ACK, it should close the connection and reconnect.
>    * Discord may send the app a Heartbeat (opcode `1`) event, in which case the app should send a Heartbeat event immediately.
> 4. App sends an Identify (opcode `2`) event to perform the initial handshake with the Gateway.
> 5. Discord sends the app a Ready (opcode `0`) event which indicates the handshake was successful and the connection is established. The Ready event contains a `resume_gateway_url` that the app should keep track of to determine the WebSocket URL an app should use to Resume.
> 6. The connection may be dropped for a variety of reasons at any time. Whether the app can Resume the connection or whether it must re-identify is determined by a variety of factors like the opcode and close code that it receives.
> 7. If an app **can** resume/reconnect, it should open a new connection using `resume_gateway_url` with the same version and encoding, then send a Resume (opcode `6`) event. If an app **cannot** resume/reconnect, it should open a new connection using the cached URL from step #1, then repeat the whole Gateway cycle.

The WSS URL should carry version and encoding explicitly:

> `wss://gateway.discord.gg/?v=10&encoding=json` is an example of a WSS URL an app may use to
> connect to the Gateway.

| Field | Type | Description | Accepted Values |
| ----- | ---- | ---- | ---- |
| v | integer | API Version to use | API version |
| encoding | string | The encoding of received gateway packets | `json` or `etf` |
| compress? | string | The optional transport compression of gateway packets | `zlib-stream` or `zstd-stream` |

> If you aren't sure which encoding to use, JSON is generally recommended.

`GET /gateway` example response:

```json
{
  "url": "wss://gateway.discord.gg/"
}
```

> Apps should cache this value and only call this endpoint to retrieve a new URL when they are
> unable to properly establish a connection using the cached one.

`GET /gateway/bot` adds `shards` (recommended shard count) and `session_start_limit`, and "should
not be cached for extended periods of time as the value is not guaranteed to be the same per-call,
and changes as the bot joins/leaves guilds."

### Identify

Minimal payload, verbatim:

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

Two limits that matter during a restart-heavy local session:

> Apps are limited by maximum concurrency (`max_concurrency` in the session start limit object) when
> identifying. If your app exceeds this limit, Discord will respond with a Invalid Session (opcode
> `9`) event.

> Clients are limited to 1000 `IDENTIFY` calls to the websocket in a 24-hour period. This limit is
> global and across all shards, but does not include `RESUME` calls. Upon hitting this limit, all
> active sessions for the app will be terminated, the bot token will be reset, and the owner will
> receive an email notification. It's up to the owner to update their application with the new
> token.

The Ready event carries what you need to resume:

> * `resume_gateway_url` is a WebSocket URL that your app should use when it Resumes after a disconnect. The `resume_gateway_url` should be used instead of the URL used when connecting.
> * `session_id` is the ID for the Gateway session for the new connection.

Resume payload:

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

Closing deliberately, which is what a clean local shutdown should do:

> When you close the connection to the gateway with close code `1000` or `1001`, your session will
> be invalidated and your bot will appear offline.
>
> If you simply close the TCP connection or use a different close code, the session will remain
> active and timeout after a few minutes. This can be useful when you're Resuming the previous
> session.

### Heartbeats

Hello event:

```json
{
  "op": 10,
  "d": {
    "heartbeat_interval": 45000
  }
}
```

> Upon receiving the Hello event, your app should wait `heartbeat_interval * jitter` where `jitter`
> is any random value between 0 and 1, then send its first Heartbeat (opcode `1`) event. From that
> point until the connection is closed, your app must continually send Discord a heartbeat every
> `heartbeat_interval` milliseconds. If your app fails to send a heartbeat event in time, your
> connection will be closed and you will be forced to Resume.

> When sending a heartbeat, your app will need to include the last sequence number your app received
> in the `d` field. … If your app hasn't received any events yet, you can just pass `null` in the
> `d` field.

Heartbeat ACK:

```json
{
  "op": 11
}
```

> If a client does not receive a heartbeat ACK between its attempts at sending heartbeats, this may
> be due to a failed or "zombied" connection. The client should immediately terminate the connection
> with any close code besides `1000` or `1001`, then reconnect and attempt to Resume.

### Intents

> Intents are bitwise values passed in the `intents` parameter when Identifying which correlate to a
> set of related events. … If you do not specify an intent when identifying, you will not receive
> *any* of the Gateway events associated with that intent.

> * **Standard intents** can be passed by default. You don't need any additional permissions or configurations.
> * **Privileged intents** require you to toggle the intent for your app in your app's settings within the Developer Portal before passing said intent. For verified apps (required for apps in 100+ guilds), the intent must also be approved after the verification process to use the intent.

> The connection with your app will be closed if it passes invalid intents (`4013` close code), or a
> privileged intent that hasn't been configured or approved for your app (`4014` close code).

> Intents are optionally supported on the v6 gateway but required as of v8

> Events under the `GUILD_PRESENCES` and `GUILD_MEMBERS` intents are turned **off by default on all
> API versions**.

Sending a payload that is too large also closes the connection:

> Must not exceed 4096 bytes. If an event payload *does* exceed 4096 bytes, the connection will be
> closed with a `4002` close event code.

Payloads must be "serialized in plain-text JSON or binary ETF."

The full intent table and every event it maps to belong to `discord-gateway`; call the Skill tool
with "discord-gateway" for it.

### Gateway rate limits

> Apps can send 120 gateway events per connection every 60 seconds, meaning an average of 2 commands
> per second. Apps that surpass the limit are immediately disconnected from the Gateway. Similar to
> other rate limits, repeat offenders will have their API access revoked.

> Apps also have a limit for concurrent Identify requests allowed per 5 seconds. If you hit this
> limit, the Gateway will respond with an Invalid Session (opcode `9`).

These are separate from HTTP rate limits: "This section refers to Gateway rate limits, not HTTP API
rate limits."

## Where the documentation is silent

- **Whether you can switch transports back and forth freely.** The docs state the two modes are
  mutually exclusive and that adding an Interactions Endpoint URL opts you into HTTP. They do not
  state what happens to a Gateway connection at the moment you save a URL, nor whether clearing the
  field restores Gateway interactions immediately.
- **The re-check schedule.** "automated, routine security checks" is all upstream says. There is no
  documented interval, no warning before removal, and no documented way to trigger a re-check.
- **Whether Discord retries a failed interaction delivery.** No retry policy is stated for an
  endpoint that is down or slow. The only stated consequence of missing the 3-second window is that
  the token is invalidated.
- **What a locally-running Gateway bot should do about a laptop going to sleep.** The docs describe
  resume and close codes generically; there is no local-development-specific advice.
