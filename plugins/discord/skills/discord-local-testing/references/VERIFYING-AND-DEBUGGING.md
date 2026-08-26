# Verifying and Debugging a Local Discord App

How to tell the app actually works, and the failure signatures upstream names. Every figure, code and
quote below is from a docs page cited at the bottom; where a page is silent, this file says so.

## Contents

- [The acceptance checks the guides give](#the-acceptance-checks-the-guides-give)
- [Iteration speed: guild commands are documented as instant](#iteration-speed-guild-commands-are-documented-as-instant)
- [Failure signature: a command appears but does nothing](#failure-signature-a-command-appears-but-does-nothing)
- [Failure signature: a command does not appear at all](#failure-signature-a-command-does-not-appear-at-all)
- [Failure signature: the endpoint will not verify](#failure-signature-the-endpoint-will-not-verify)
- [Failure signature: interactions stop arriving after they worked](#failure-signature-interactions-stop-arriving-after-they-worked)
- [Failure signature: the 3-second deadline](#failure-signature-the-3-second-deadline)
- [Failure signature: a missing privileged intent returns empty fields, not an error](#failure-signature-a-missing-privileged-intent-returns-empty-fields-not-an-error)
- [Failure signature: the Gateway closes the connection](#failure-signature-the-gateway-closes-the-connection)
- [Failure signature: rate limits while iterating](#failure-signature-rate-limits-while-iterating)
- [Failure signature: Cloudflare blocks you](#failure-signature-cloudflare-blocks-you)
- [HTTP response codes](#http-response-codes)
- [JSON error codes for these cases](#json-error-codes-for-these-cases)
- [Form error shapes](#form-error-shapes)
- [Logging](#logging)
- [Where the documentation is silent](#where-the-documentation-is-silent)

## The acceptance checks the guides give

Upstream never presents a checklist, but each walkthrough states an observable outcome at each stage.
Collected, they form a diagnostic ladder — each rung tells you the one below it worked.

| Stage | Observable outcome, verbatim | What it proves |
|---|---|---|
| Installed to a server | "Once your app is added to your test server, you should see it appear in the member list." | Install link, scopes, bot user |
| Installed to a user | "Once it's installed you can open a DM with it." | User install context |
| Commands registered | "If you navigate back to your server, you should see the slash commands appear." | Token, application ID, command payloads |
| Endpoint saved | "Click **Save Changes** and ensure your endpoint is successfully verified." | Tunnel reachable, `PING` answered, signature verified |
| Command runs | "your app should send a message that contains 'hello world' followed by a random emoji" | The whole chain |
| Request logged | "our app is logging incoming requests from Discord, so you can see what the request body for your command invocation looked like" | Payloads arriving as expected |
| Activity launches | "open the App Launcher where your in-development Activity should be present" | URL mapping, Activities enabled, supported platform |

The Gateway equivalent, from the connection lifecycle: Discord "sends the app a Ready (opcode `0`)
event which indicates the handshake was successful and the connection is established." Receiving
`Ready` is the documented proof that a Gateway bot is connected and identified. Before that, the
`Hello (opcode 10)` event with its `heartbeat_interval` proves the socket opened.

Also useful as a cheap credential test: `GET /gateway` "does not require authentication" while
`GET /gateway/bot` "requires authentication using a valid bot token." If the first succeeds and the
second returns `401`, the problem is the token, not the network.

## Iteration speed: guild commands are documented as instant

This is documented fact, not folklore. From `interactions/application-commands`:

> Guild commands are available only within the guild specified on creation. Guild commands update
> **instantly**. We recommend you use guild commands for quick testing, and global commands when
> they're ready for public use.

The endpoint descriptions on the same page repeat it:

- `POST /applications/{application.id}/guilds/{guild.id}/commands` — "New guild commands will be
  available in the guild **immediately**."
- `PATCH /applications/{application.id}/guilds/{guild.id}/commands/{command.id}` — "Updates for guild
  commands will be available **immediately**."

Global registration has no stated duration. What upstream states instead is read-repair:

> Global commands have inherent read-repair functionality. That means that if you make an update to a
> global command, and a user tries to use that command before it has updated for them, Discord will
> do an internal version check and reject the command, and trigger a reload for that command.

and, in the Cloudflare tutorial's `register.js` comment, an order of magnitude: registering globally
"can take o(minutes), so wait until you're sure these are the commands you want."

**So when a freshly-edited command behaves like the old version, the scope is the first thing to
check.** Guild-scoped means the change is live; global means the client may still be repairing.
Full detail, including the traps, is in [COMMAND-REGISTRATION.md](COMMAND-REGISTRATION.md).

## Failure signature: a command appears but does nothing

The most common local state, and the guides call it out twice:

> If you navigate back to your server, you should see the slash commands appear. But if you try to
> run them, nothing will happen since your app isn't receiving or handling any requests from Discord.

> However, if you try to run any of the commands, you'll get an error :(

**What that splits.** The command appearing proves registration succeeded — token, application ID and
payload are all fine. Nothing happening points at delivery: no Interactions Endpoint URL saved, the
tunnel is down, the server is not running, or the endpoint is failing verification. Do not
re-register; check the endpoint.

## Failure signature: a command does not appear at all

Three documented causes, none of which is a failed registration call:

1. **Permissions.** "If you don't have permission to use a command, it will not show up in the
   command picker. Members with the Administrator permission can use all commands." A
   `default_member_permissions` of `"0"` hides the command from everyone but admins.
2. **Contexts.** `contexts` and `integration_types` decide which surfaces show the command. The
   user-installable tutorial's expected-visibility list is the reference for checking this by eye —
   see [COMMAND-REGISTRATION.md](COMMAND-REGISTRATION.md).
3. **Scope mismatch.** "Guild commands are not available in DMs", and "Guild commands don't support
   the `BOT_DM` interaction context." A guild-scoped command will never appear in your bot's DM.

For an Activity that does not appear in the shelf: "the activity will not be shown on the current
platform (web/ios/android) unless you have checked your platform in Settings/Supported Platforms on
the developer portal", the shelf "will only include applications which have been flagged as
'Embedded'", and "If you don't see your Activity, you should try searching for its name."

Confirm what is actually registered with `GET /applications/{application.id}/commands` or the guild
variant before re-registering — that also avoids spending from the 200-creates-per-day budget.

## Failure signature: the endpoint will not verify

The gate, verbatim:

> Before you can add your Interactions Endpoint URL to your app, your endpoint must be prepared for
> two things ahead of time:
>
> 1. Acknowledging `PING` requests from Discord
> 2. Validate security-related request headers (`X-Signature-Ed25519` and `X-Signature-Timestamp`)
>
> If either of these are not complete, your Interactions Endpoint URL will not be validated.

The one troubleshooting note the tutorials give:

> If you have troubles verifying your endpoint, make sure both ngrok and your app are running on the
> same port, and that you've copied the ngrok URL correctly

**What causes a 401 on an interactions endpoint.** Upstream tells you to *produce* the 401 yourself:
"If the signature fails validation, your app should respond with a `401` error code." The Worker
sample's body text for it is exact:

```js
if (!isValidRequest) {
  console.error('Invalid Request');
  return new Response('Bad request signature.', { status: 401 });
}
```

So `Bad request signature.` with status `401` is **your own code's** output, not Discord's. Seeing it
in your logs during a legitimate request means the verification itself is wrong, and the documented
causes are:

- **The body was re-serialised.** The signed message is `timestamp + body` over the *raw* body. The
  JavaScript example's comment says `rawBody is expected to be a string, not raw bytes`; the Worker
  sample clones the request to read an `arrayBuffer`. A framework that parses and re-stringifies JSON
  produces different bytes and the signature fails. The Express sample avoids it by hooking Express's
  `verify` interface: it "makes it conform to Express's `verify` interface. This is run on every
  incoming request to your app."
- **The wrong key.** The verification key is the **Public Key** from General Information, not the bot
  token. Every code sample comments it: "Your public key can be found on your application in the
  Developer Portal."
- **Headers read with the wrong case or from the wrong place.** Upstream names them
  `X-Signature-Ed25519` and `X-Signature-Timestamp`; the Worker sample reads them lowercase
  (`x-signature-ed25519`) because that is how the Fetch API exposes them.

Content type is also a gate: "You must provide a valid `Content-Type` when responding to `PING`s",
and generally "Failing to do so will result in a `50035` 'Invalid form body' error."

The `PING`/`PONG` symmetry catches people: interaction type `PING` is `1` and callback type `PONG` is
also `1`. Full contract and all three verification implementations are in
[GATEWAY-VS-HTTP.md](GATEWAY-VS-HTTP.md).

## Failure signature: interactions stop arriving after they worked

This one is silent in your logs, and it is the reason a permissive signature check is a real hazard:

> In addition to ensuring your app validates security-related request headers at the time of saving
> your endpoint, Discord will also perform automated, routine security checks against your endpoint,
> including purposefully sending you invalid signatures. If you fail the validation, we will remove
> your interactions URL and alert you via email and System DM.

**The consequence is removal of the URL.** An endpoint that returns `200` to a deliberately bad
signature loses its configuration, so commands go back to doing nothing, and the notification arrives
by email and System DM rather than in your terminal. If interactions stopped without a code change,
check whether the Interactions Endpoint URL field is still populated.

The parallel mechanism exists for webhook events too, on `events/webhook-events`: "we will remove
your Webhook Events URL and alert you via email and System DM."

## Failure signature: the 3-second deadline

> Interaction `tokens` are valid for **15 minutes** and can be used to send followup messages but you
> **must send an initial response within 3 seconds of receiving the event**. If the 3 second deadline
> is exceeded, the token will be invalidated.

> Interaction tokens are valid for **15 minutes**, meaning you can respond to an interaction within
> that amount of time.

The platform page states it loosely — "Discord handles delivery and your app needs to respond within
a few seconds" — so use 3 seconds as the figure.

**What the miss looks like.** The documented consequence is that the token is invalidated, so
subsequent calls with it fail. The JSON error codes upstream names for interaction-token problems are
`10062` **Unknown interaction** and `40060` **Interaction has already been acknowledged**.

**The documented fix is deferral, not optimisation.** Respond with callback type `5`
`DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE` — "ACK an interaction and edit a response later, the user sees
a loading state" — then edit within the 15 minutes via
`PATCH /webhooks/{application.id}/{interaction.token}/messages/@original`. For components, type `6`
`DEFERRED_UPDATE_MESSAGE` does the same without a loading state. One restriction: with a deferred
callback "the only valid message flag you may use is `EPHEMERAL`", and an `IS_COMPONENTS_V2` message
must be produced through the edit endpoint instead.

Followup limits worth knowing before you hit them:

> Apps are limited to 5 followup messages per interaction if it was initiated from a user-installed
> app and isn't installed in the server (meaning the authorizing integration owners object only
> contains `USER_INSTALL`)

The matching error code is `40094` **This interaction has hit the maximum number of follow up
messages**.

## Failure signature: a missing privileged intent returns empty fields, not an error

The single most misleading local symptom, because nothing fails:

> Apps **without** the intent will receive empty values in fields that contain user-inputted content
> with a few exceptions:
>
> * Content in messages that an app sends
> * Content in DMs with the app
> * Content in which the app is mentioned
> * Content of the message a message context menu command is used on

Which fields:

> `MESSAGE_CONTENT (1 << 15)` is a unique privileged intent that isn't directly associated with any
> Gateway events. Instead, access to `MESSAGE_CONTENT` permits your app to receive message content
> data across the APIs.
>
> Any fields affected by the message content intent are noted in the relevant documentation. For
> example, the `content`, `embeds`, `attachments`, `components`, and `poll` fields in message objects
> all contain message content and therefore require the intent.

**So a bot reading messages locally sees `content: ""` and no exception.** The exception list is why
it looks intermittent: your own messages, DMs with the app, and messages mentioning the app *do*
carry content. A developer testing by mentioning the bot sees it work, then sees it fail on ordinary
channel messages.

The same shape applies to members. `GUILD_PRESENCES` and `GUILD_MEMBERS` events "are turned **off by
default on all API versions**", and:

> If you do not specify an intent when identifying, you will not receive *any* of the Gateway events
> associated with that intent.

**And it reaches HTTP endpoints too**, independently of the Gateway:

> In addition to Gateway restrictions, privileged intents also affect the HTTP API endpoints your app
> is permitted to call, and the data it can receive. For example, to use the List Guild Members
> endpoint, your app must enable the `GUILD_MEMBERS` intent (and be approved for it if eligible for
> verification).
>
> HTTP API restrictions are independent of Gateway restrictions, and are unaffected by which intents
> your app passes in the `intents` parameter when Identifying.

So an HTTP-only app with no Gateway connection still needs the portal toggle. The toggle location and
the review thresholds are in [APP-SETUP.md](APP-SETUP.md).

Two related asymmetries the Gateway page states:

> Guild Member Update is sent for current-user updates regardless of whether the `GUILD_MEMBERS`
> intent is set.

> Thread Members Update by default only includes if the current user was added to or removed from a
> thread. To receive these updates for other users, request the `GUILD_MEMBERS` Gateway Intent.

The complete intent-to-event mapping belongs to `discord-gateway`; call the Skill tool with
"discord-gateway" for it.

## Failure signature: the Gateway closes the connection

The close code tells you what went wrong and whether reconnecting can ever help:

> In order to prevent broken reconnect loops, you should consider some close codes as a signal to
> stop reconnecting. This can be because your token expired, or your identification is invalid.

| Code | Description | Explanation | Reconnect |
| ---- | --------------------- | ---- | --------- |
| 4000 | Unknown error | We're not sure what went wrong. Try reconnecting? | true |
| 4001 | Unknown opcode | You sent an invalid Gateway opcode or an invalid payload for an opcode. Don't do that! | true |
| 4002 | Decode error | You sent an invalid payload to Discord. Don't do that! | true |
| 4003 | Not authenticated | You sent us a payload prior to identifying, or this session has been invalidated. | true |
| 4004 | Authentication failed | The account token sent with your identify payload is incorrect. | false |
| 4005 | Already authenticated | You sent more than one identify payload. Don't do that! | true |
| 4007 | Invalid `seq` | The sequence sent when resuming the session was invalid. Reconnect and start a new session. | true |
| 4008 | Rate limited | Woah nelly! You're sending payloads to us too quickly. Slow it down! You will be disconnected on receiving this. | true |
| 4009 | Session timed out | Your session timed out. Reconnect and start a new one. | true |
| 4010 | Invalid shard | You sent us an invalid shard when identifying. | false |
| 4011 | Sharding required | The session would have handled too many guilds - you are required to shard your connection in order to connect. | false |
| 4012 | Invalid API version | You sent an invalid version for the gateway. | false |
| 4013 | Invalid intent(s) | You sent an invalid intent for a Gateway Intent. You may have incorrectly calculated the bitwise value. | false |
| 4014 | Disallowed intent(s) | You sent a disallowed intent for a Gateway Intent. You may have tried to specify an intent that you have not enabled or are not approved for. | false |

The three that dominate local development:

- **`4004` — bad token.** The token in `.env` is wrong, stale, or was reset. `Reconnect: false`: no
  retry will fix it. Note this can happen *without* you changing anything, because exceeding the
  1000-IDENTIFY daily limit resets the token for you (see below).
- **`4013` — invalid intents.** "You may have incorrectly calculated the bitwise value." A malformed
  `intents` number, not a permissions problem.
- **`4014` — disallowed intents.** You passed a privileged intent that is not toggled on in the
  portal or not approved. Stated again from the intents side: "If you pass a privileged intent in the
  `intents` parameter without configuring it in your app's settings, or being approved for it during
  verification, your Gateway connection will be closed with a (`4014` close code)."

`4013` versus `4014` is the useful distinction: `4013` means your arithmetic is wrong, `4014` means
your arithmetic is right and the portal disagrees.

Also documented as connection-killers:

- **Payload over 4096 bytes** — "the connection will be closed with a `4002` close event code."
- **Missed heartbeat** — "If your app fails to send a heartbeat event in time, your connection will
  be closed and you will be forced to Resume."
- **A zombied connection** — "If a client does not receive a heartbeat ACK between its attempts at
  sending heartbeats, this may be due to a failed or 'zombied' connection. The client should
  immediately terminate the connection with any close code besides `1000` or `1001`, then reconnect
  and attempt to Resume."
- **No close code at all** is a documented resume trigger: "It's disconnected but doesn't receive
  *any* close code."
- **`Invalid Session (opcode 9)`** with `d: false` — "your app should disconnect. After disconnect,
  your app should create a new connection with your cached URL … then send an Identify (opcode `2`)
  event."

**The restart-loop hazard, verbatim, because it costs you your token:**

> Clients are limited to 1000 `IDENTIFY` calls to the websocket in a 24-hour period. This limit is
> global and across all shards, but does not include `RESUME` calls. Upon hitting this limit, all
> active sessions for the app will be terminated, the bot token will be reset, and the owner will
> receive an email notification. It's up to the owner to update their application with the new token.

A crash-restart loop during local development spends that budget, and the punishment is a token reset
that turns every later attempt into `4004`. Resuming does not count against it.

And a concurrency limit that shows up as `opcode 9` rather than a close code: "Apps are limited by
maximum concurrency (`max_concurrency` in the session start limit object) when identifying. If your
app exceeds this limit, Discord will respond with a Invalid Session (opcode `9`) event." / "Apps also
have a limit for concurrent Identify requests allowed per 5 seconds."

Clean shutdown matters for what you see in the client:

> When you close the connection to the gateway with close code `1000` or `1001`, your session will be
> invalidated and your bot will appear offline.
>
> If you simply close the TCP connection or use a different close code, the session will remain
> active and timeout after a few minutes.

So a bot still showing as online after you killed the process is expected behaviour, not a bug.

Voice close codes and the full opcode tables live on `docs.discord.com/developers/topics/opcodes-and-status-codes`;
call the Skill tool with "discord-gateway" for them in full.

## Failure signature: rate limits while iterating

The general rule first:

> Because rate limits depend on a variety of factors and are subject to change, **rate limits should
> not be hard coded into your app**. Instead, your app should parse response headers to prevent
> hitting the limit, and to respond accordingly in case you do.

The headers to read:

```
X-RateLimit-Limit: 5
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1470173023
X-RateLimit-Reset-After: 1
X-RateLimit-Bucket: abcd1234
```

* **X-RateLimit-Limit** - The number of requests that can be made
* **X-RateLimit-Remaining** - The number of remaining requests that can be made
* **X-RateLimit-Reset** - Epoch time (seconds since 00:00:00 UTC on January 1, 1970) at which the rate limit resets
* **X-RateLimit-Reset-After** - Total time (in seconds) of when the current rate limit bucket will reset. Can have decimals to match previous millisecond ratelimit precision
* **X-RateLimit-Bucket** - A unique string denoting the rate limit being encountered (non-inclusive of top-level resources in the path)
* **X-RateLimit-Global** - Returned only on HTTP 429 responses if the rate limit encountered is the global rate limit (not per-route)
* **X-RateLimit-Scope** - Returned only on HTTP 429 responses. Value can be `user` (per bot or user limit), `global` (per bot or user global limit), or `shared` (per resource limit)

On exceeding one:

> In the case that a rate limit is exceeded, the API will return a HTTP 429 response code with a JSON
> body. Your application should rely on the `Retry-After` header or `retry_after` field to determine
> when to retry the request.

| Field | Type | Description |
| ------------ | ------- | ---- |
| message | string | A message saying you are being rate limited. |
| retry_after | float | The number of seconds to wait before submitting another request. |
| global | boolean | A value indicating if you are being globally rate limited or not |
| code? | integer | An error code for some limits |

**Example Exceeded User Rate Limit Response**

```
< HTTP/1.1 429 TOO MANY REQUESTS
< Content-Type: application/json
< Retry-After: 65
< X-RateLimit-Limit: 10
< X-RateLimit-Remaining: 0
< X-RateLimit-Reset: 1470173023.123
< X-RateLimit-Reset-After: 64.57
< X-RateLimit-Bucket: abcd1234
< X-RateLimit-Scope: user
{
  "message": "You are being rate limited.",
  "retry_after": 64.57,
  "global": false
}
```

**Example Exceeded Resource Rate Limit Response**

```
< HTTP/1.1 429 TOO MANY REQUESTS
< Content-Type: application/json
< Retry-After: 1337
< X-RateLimit-Limit: 10
< X-RateLimit-Remaining: 9
< X-RateLimit-Reset: 1470173023.123
< X-RateLimit-Reset-After: 64.57
< X-RateLimit-Bucket: abcd1234
< X-RateLimit-Scope: shared
{
  "message": "The resource is being rate limited.",
  "retry_after": 1336.57,
  "global": false
}
```

**Example Exceeded Global Rate Limit Response**

```
< HTTP/1.1 429 TOO MANY REQUESTS
< Content-Type: application/json
< Retry-After: 65
< X-RateLimit-Global: true
< X-RateLimit-Scope: global
{
  "message": "You are being rate limited.",
  "retry_after": 64.57,
  "global": true
}
```

The global limit:

> All bots can make up to 50 requests per second to our API. If no authorization header is provided,
> then the limit is applied to the IP address.

Two limits specific to iterating locally:

- **Command creates**: "There is a global rate limit of 200 application command creates per day, per
  guild." A `register` script run repeatedly is spending from this.
- **Gateway events**: "Apps can send 120 gateway events per connection every 60 seconds, meaning an
  average of 2 commands per second. Apps that surpass the limit are immediately disconnected from the
  Gateway." That is the `4008` close code.

Two exemptions worth knowing so you do not misdiagnose:

> Interaction endpoints are not bound to the bot's Global Rate Limit.

> Interactions webhooks share the same rate limit properties as normal webhooks.

And a documented inaccuracy:

> Routes for controlling emojis do not follow the normal rate limit conventions. These routes are
> specifically limited on a per-guild basis to prevent abuse. This means that the quota returned by
> our APIs may be inaccurate, and you may encounter 429s.

Per-route limits are computed per top-level resource, which is why one channel being limited does not
limit another: "if you exceeded a rate limit when calling one endpoint `/channels/1234`, you could
still call another similar endpoint like `/channels/9876` without a problem." Top-level resources are
"channels (`channel_id`), guilds (`guild_id`), and webhooks (`webhook_id` or
`webhook_id + webhook_token`)."

## Failure signature: Cloudflare blocks you

Two distinct causes, both easy to hit locally and neither producing a Discord JSON error.

**Missing User-Agent:**

> Clients using the HTTP API must provide a valid User Agent which specifies information about the
> client library and version in the following format:

```bash
User-Agent: DiscordBot ($url, $versionNumber)
```

> Client requests that do not have a valid User Agent specified may be blocked and return a
> Cloudflare error.

A hand-rolled script using bare `fetch` or `requests` sends the runtime default and can be blocked.

**Too many invalid requests:**

> IP addresses that make too many invalid HTTP requests are automatically and temporarily restricted
> from accessing the Discord API. Currently, this limit is **10,000 per 10 minutes**. An invalid
> request is one that results in **401**, **403**, or **429** statuses.

> All applications should make reasonable attempts to avoid making invalid requests. For example:
>
> * **401** responses are avoided by providing a valid token in the authorization header when required and by stopping further requests after a token becomes invalid
> * **403** responses are avoided by inspecting role or channel permissions and by not making requests that are restricted by such permissions
> * **429** responses are avoided by inspecting the rate limit headers documented above and by not making requests on exhausted buckets until after they have reset. *429 errors returned with `X-RateLimit-Scope: shared` are not counted against you.*

> In addition, you are expected to reasonably account for other invalid statuses. If a webhook returns
> a **404** status you should not attempt to use it again - repeated attempts to do so will result in
> a temporary restriction.

**A local retry loop against a bad token is exactly this pattern**: every attempt is a `401`, and
enough of them get the IP restricted. Upstream distinguishes the two causes explicitly:

> Global rate limit issues generally show up as repeatedly getting banned from the Discord API when
> your bot starts (see below). If your bot gets temporarily Cloudflare banned from the Discord API
> every once in a while, it is most likely **not** a global rate limit issue. You probably had a spike
> of errors that was not properly handled and hit our error threshold.

Escalation path if it is genuinely the global limit: "you can reach out to support to see if you
qualify for increased global rate limits. You can contact Discord support using
[https://dis.gd/rate-limit](https://dis.gd/rate-limit)."

## HTTP response codes

| Code | Meaning |
| ------------------------- | ---- |
| 200 (OK) | The request completed successfully. |
| 201 (CREATED) | The entity was created successfully. |
| 204 (NO CONTENT) | The request completed successfully but returned no content. |
| 304 (NOT MODIFIED) | The entity was not modified (no action was taken). |
| 400 (BAD REQUEST) | The request was improperly formatted, or the server couldn't understand it. |
| 401 (UNAUTHORIZED) | The `Authorization` header was missing or invalid. |
| 403 (FORBIDDEN) | The `Authorization` token you passed did not have permission to the resource. |
| 404 (NOT FOUND) | The resource at the location specified doesn't exist. |
| 405 (METHOD NOT ALLOWED) | The HTTP method used is not valid for the location specified. |
| 429 (TOO MANY REQUESTS) | You are being rate limited, see Rate Limits. |
| 502 (GATEWAY UNAVAILABLE) | There was not a gateway available to process your request. Wait a bit and retry. |
| 5xx (SERVER ERROR) | The server had an error processing your request (these are rare). |

Note the interaction-specific successes so you do not read them as failures:
`POST .../callback` "Returns `204` unless `with_response` is set to `true` which returns `200`", and
delete endpoints return `204 No Content`. If you answer a Gateway-delivered interaction via the
callback endpoint, "respond to the original HTTP request with a 202 and no body."

## JSON error codes for these cases

> Along with the HTTP error code, our API can also return more detailed error codes through a `code`
> key in the JSON error response. The response will also contain a `message` key containing a more
> friendly error string.

The subset upstream names that bears on local verification:

| Code | Meaning |
| ------ | ---- |
| 0 | General error (such as a malformed request body, amongst other things) |
| 10002 | Unknown application |
| 10062 | Unknown interaction |
| 20012 | You are not authorized to perform this action on this application |
| 40001 | Unauthorized. Provide a valid token and try again |
| 40043 | Application interaction failed to send |
| 40060 | Interaction has already been acknowledged |
| 40094 | This interaction has hit the maximum number of follow up messages |
| 50001 | Missing access |
| 50013 | You lack permissions to perform that action |
| 50014 | Invalid authentication token provided |
| 50027 | Invalid webhook token provided |
| 50035 | Invalid form body (returned for both `application/json` and `multipart/form-data` bodies), or invalid `Content-Type` provided |

How to read them against the symptoms above:

- **`10062` Unknown interaction** — the interaction ID or token is not recognised. The documented way
  to invalidate a token is missing the 3-second deadline.
- **`40060` Interaction has already been acknowledged** — a second initial response. Common when both
  an inline HTTP response and a callback request are sent for the same interaction.
- **`40094`** — past the 5-followup ceiling for a user-installed-only interaction.
- **`50014` / `40001`** — the token. Note `50014` names the token as invalid while `40001` asks for a
  valid one; upstream lists both without distinguishing them further.
- **`50035`** — the payload or the `Content-Type`. This is what a malformed command registration
  payload returns, and it is why the Workers `register.js` prints the response body on failure.
- **`50013` / `50001`** — permissions rather than credentials. Relevant when a command runs but the
  app cannot post.
- **`10002`** — the application ID is wrong.

The complete JSON error code table lives on
`docs.discord.com/developers/topics/opcodes-and-status-codes`; call the Skill tool with
"discord-bots" for it in full.

## Form error shapes

Error responses carry the offending key, which is what makes a `50035` actionable:

> Starting in API v8, we've improved error formatting in form error responses. The response will tell
> you which JSON key contains the error, the error code, and a human readable error message. We will
> be frequently adding new error messages, so a complete list of errors is not feasible and would be
> almost instantly out of date. Here are some examples instead:

**Array Error**

```json
{
  "code": 50035,
  "errors": {
    "activities": {
      "0": {
        "platform": {
          "_errors": [
            {
              "code": "BASE_TYPE_CHOICES",
              "message": "Value must be one of ('desktop', 'android', 'ios')."
            }
          ]
        },
        "type": {
          "_errors": [
            {
              "code": "BASE_TYPE_CHOICES",
              "message": "Value must be one of (0, 1, 2, 3, 4, 5)."
            }
          ]
        }
      }
    }
  },
  "message": "Invalid Form Body"
}
```

**Object Error**

```json
{
  "code": 50035,
  "errors": {
    "access_token": {
      "_errors": [
        {
          "code": "BASE_TYPE_REQUIRED",
          "message": "This field is required"
        }
      ]
    }
  },
  "message": "Invalid Form Body"
}
```

**Request Error**

```json
{
  "code": 50035,
  "message": "Invalid Form Body",
  "errors": {
    "_errors": [
      {
        "code": "APPLICATION_COMMAND_TOO_LARGE",
        "message": "Command exceeds maximum size (8000)"
      }
    ]
  }
}
```

That third example is a command registration failure with its own named error string, and it shows
why printing the response body — as the Workers `register.js` does — is worth doing:

```js
if (response.ok) {
  console.log('Registered all commands');
} else {
  console.error('Error registering commands');
  const text = await response.text();
  console.error(text);
}
```

**API version matters for error quality.** Improved form errors start in v8, and the default version
if you omit the path segment is v6 — see [APP-SETUP.md](APP-SETUP.md). Request `v10` explicitly.

## Logging

**For a bot**, the documented technique is logging the incoming request body:

> Back on the command line, our app is logging incoming requests from Discord, so you can see what
> the request body for your command invocation looked like.

The Worker sample does the same with `console.log(message)` on every routed request, plus branch
markers (`'Handling Ping request'`, `'handling cute request'`, `'Unknown Command'`, `'Unknown Type'`)
and `console.error('Invalid Request')` on a failed signature. The Express sample wraps its webhook
calls in `try/catch` with `console.error('Error sending message:', err)`.

Beyond that, upstream describes no bot-side logging facility: there is no Discord-provided log
viewer, no delivery log, and no way to inspect what Discord sent you other than logging it yourself.

**For an Activity**, there is a real facility, and it is documented in full.

> By default, the SDK will send any console `log`, `warn`, `error`, `info`, and `debug` events
> triggered by your app to the Discord application.

**Desktop:**

> Desktop logs are viewable through the console tab inside a browser's Developer Tools. See the
> [Troubleshooting Console Log Errors](https://support.discord.com/hc/en-us/articles/115001239472-Troubleshooting-Console-Log-Errors)
> support article for more information.
>
> The Public Test Build (PTB) Discord client also allows inspecting your logs from the
> `View -> Developer -> Toggle Developer Tools` menu. It can be downloaded at
> [https://discord.com/downloads](https://discord.com/downloads).

**Mobile:**

> Mobile logs are viewable via the `Debug Logs` option inside User Settings on the mobile App. It is
> only discoverable when you have `Developer Mode` enabled.
>
> 1. On the bottom navigation, tap on your avatar and then the gear icon to open your `User Settings`.
> 2. Tap `Appearance`.
> 3. Slide the `Developer Mode` toggle to ON.
> 4. The `Debug Logs` option will be available under the `DEV ONLY` section.

**Finding your own lines in there:**

> Inside the Debug Logs view, you can search for your own application logs with the possible keywords:
>
> * `RpcApplicationLogger`
> * Your Application ID
>
> Each log line is formatted as: `[RpcApplicationLogger] <application-id> - message`
>
> The first section of Debug Logs are not your application logs but Discord specific app startup info
> which is not relevant to your application.
>
> When you scroll down the page, your application logs should be visible.

Screenshot caption: *debug-logs-filtering*.

**Sharing from mobile:**

> With `Developer Mode` enabled, you can share your application logs from within a Voice Channel.
>
> 1. In the voice channel, swipe from the bottom to see the expanded voice controls. Tap on `Share Application Logs`.
> 2. You'll be presented with a native share sheet where you can save the logs to a file or share it as a message.

**Turning forwarding off:**

```javascript
import {DiscordSDK} from '@discord/embedded-app-sdk';
const discordSdk = new DiscordSDK(clientId, {
  disableConsoleLogOverride: true,
});
```

**Forwarding a specific message:**

```javascript
import {DiscordSDK} from '@discord/embedded-app-sdk';
const discordSdk = new DiscordSDK(clientId);
await discordSdk.ready();
discordSdk.commands.captureLog({
  level: 'log',
  message: 'This is my log message!',
});
```

## Where the documentation is silent

- **No way to replay or synthesise an interaction.** Nothing documents a signed test request, a
  fixture, a replay tool, or a dry-run mode. Every verification path goes through the live client, so
  there is no documented way to unit-test a handler end to end.
- **No delivery log.** Discord does not expose what it sent your endpoint or whether it considered a
  delivery successful. Your own logs are the only record.
- **No warning before an endpoint URL is removed.** The security re-check has no documented interval,
  no advance notice, no way to trigger it, and no status field showing whether the endpoint currently
  passes.
- **No retry policy for a failed interaction delivery.** Whether Discord retries a POST to a down or
  slow endpoint is not stated. The only stated consequence of missing 3 seconds is token invalidation.
- **No documented remaining-quota signal for the 200-creates-per-day command limit.** The generic
  `X-RateLimit-*` headers are documented; upstream does not say they cover this limit.
- **No error code list for the specific case of a missing privileged intent.** The documented
  behaviour is empty field values, not an error, so there is no code to match on. Distinguishing
  "no content because of intents" from "no content because the message was empty" is left to you.
- **No stated latency figure for a Gateway event or an HTTP interaction.** Nothing tells you what
  round-trip time is normal, so "it feels slow" has no documented baseline to compare against.
- **No guidance on a laptop sleeping or a network changing mid-session.** Resume and close codes are
  described generically, with no local-development-specific advice.
- **Nothing about testing against Canary or PTB deliberately.** The PTB client is mentioned only as a
  way to open developer tools for an Activity, and `canary.discord.com` / `ptb.discord.com` appear
  only in the Activity CSP exception list. No page describes them as test environments.

## Source

Retrieved 2026-08-26 from:

- `docs.discord.com/developers/interactions/overview`
- `docs.discord.com/developers/interactions/receiving-and-responding`
- `docs.discord.com/developers/interactions/application-commands`
- `docs.discord.com/developers/platform/interactions`
- `docs.discord.com/developers/events/gateway`
- `docs.discord.com/developers/events/webhook-events`
- `docs.discord.com/developers/topics/opcodes-and-status-codes`
- `docs.discord.com/developers/topics/rate-limits`
- `docs.discord.com/developers/reference`
- `docs.discord.com/developers/quick-start/getting-started`
- `docs.discord.com/developers/tutorials/developing-a-user-installable-app`
- `docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers`
- `docs.discord.com/developers/activities/development-guides/local-development`
- `docs.discord.com/developers/activities/building-an-activity`
