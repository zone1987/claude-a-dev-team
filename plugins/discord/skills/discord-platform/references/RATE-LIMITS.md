# Discord Rate Limits

Complete extraction of `https://docs.discord.com/developers/topics/rate-limits`, retrieved 2026-08-26.

## Contents

- [The model](#the-model)
- [Per-route rate limits](#per-route-rate-limits)
- [Top-level resources](#top-level-resources)
- [Global rate limits](#global-rate-limits)
- [The emoji route exception](#the-emoji-route-exception)
- [Header format](#header-format)
- [Every rate limit header](#every-rate-limit-header)
- [Exceeding a rate limit](#exceeding-a-rate-limit)
- [Rate Limit Response Structure](#rate-limit-response-structure)
- [Example: exceeded user rate limit response](#example-exceeded-user-rate-limit-response)
- [Example: exceeded resource rate limit response](#example-exceeded-resource-rate-limit-response)
- [Example: exceeded global rate limit response](#example-exceeded-global-rate-limit-response)
- [Global rate limit figures](#global-rate-limit-figures)
- [Invalid Request Limit, also known as Cloudflare bans](#invalid-request-limit-also-known-as-cloudflare-bans)
- [Every numeric figure the page states](#every-numeric-figure-the-page-states)

## The model

Rate limits exist across Discord's APIs to prevent spam, abuse, and service overload. Limits are
applied to individual bots and users both **on a per-route basis** and **globally**. Individuals are
determined using a request's authentication — for example, a bot token for a bot.

**Never hard code a rate limit.** Upstream states this as an explicit `Info` callout: because rate
limits depend on a variety of factors and are subject to change, rate limits should not be hard coded
into your app. Instead, your app should parse the response headers to prevent hitting the limit, and
to respond accordingly in case you do.

## Per-route rate limits

Per-route rate limits exist for many individual endpoints, and **may include the HTTP method**
(`GET`, `POST`, `PUT`, or `DELETE`).

In some cases, per-route limits will be **shared across a set of similar endpoints**, indicated in
the `X-RateLimit-Bucket` header. Upstream recommends using this header as a unique identifier for a
rate limit, which allows you to group shared limits as you encounter them.

## Top-level resources

During calculation, per-route rate limits often account for **top-level resources** within the path
using an identifier — for example, `guild_id` when calling `/guilds/{guild.id}/channels`.

Top-level resources are **currently limited to three**:

| Top-level resource | Identifier |
| --- | --- |
| channels | `channel_id` |
| guilds | `guild_id` |
| webhooks | `webhook_id` or `webhook_id + webhook_token` |

This means an endpoint with two different top-level resources **may calculate limits independently**.
Upstream's own example: if you exceeded a rate limit when calling one endpoint `/channels/1234`, you
could still call another similar endpoint like `/channels/9876` without a problem.

## Global rate limits

Global rate limits apply to the **total number of requests** a bot or user makes, independent of any
per-route limits. See [Global rate limit figures](#global-rate-limit-figures) below.

## The emoji route exception

Upstream carries this as a `Warning`: the routes for controlling emojis (`List Guild Emojis` and its
siblings on the Emoji resource) **do not follow the normal rate limit conventions**. These routes are
specifically limited **on a per-guild basis** to prevent abuse. This means:

- the quota returned by Discord's APIs **may be inaccurate**, and
- you **may encounter 429s** even when the headers suggest you have quota left.

## Header format

For most API requests made, Discord returns **optional** HTTP response headers containing the rate
limit encountered during your request.

### Rate Limit Header Examples

```
X-RateLimit-Limit: 5
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1470173023
X-RateLimit-Reset-After: 1
X-RateLimit-Bucket: abcd1234
```

## Every rate limit header

Seven headers, with the exact semantics upstream states for each:

| Header | Semantics |
| --- | --- |
| `X-RateLimit-Limit` | The number of requests that can be made. |
| `X-RateLimit-Remaining` | The number of remaining requests that can be made. |
| `X-RateLimit-Reset` | Epoch time (seconds since 00:00:00 UTC on January 1, 1970) at which the rate limit resets. |
| `X-RateLimit-Reset-After` | Total time (in seconds) of when the current rate limit bucket will reset. Can have decimals to match previous millisecond ratelimit precision. |
| `X-RateLimit-Bucket` | A unique string denoting the rate limit being encountered (**non-inclusive of top-level resources in the path**). |
| `X-RateLimit-Global` | Returned **only on HTTP 429 responses** if the rate limit encountered is the global rate limit (not per-route). |
| `X-RateLimit-Scope` | Returned **only on HTTP 429 responses**. Value can be `user` (per bot or user limit), `global` (per bot or user global limit), or `shared` (per resource limit). |

### `X-RateLimit-Scope` values

| Value | Meaning |
| --- | --- |
| `user` | Per bot or user limit. |
| `global` | Per bot or user global limit. |
| `shared` | Per resource limit. |

`shared` carries a consequence documented under the invalid request limit: 429 errors returned with
`X-RateLimit-Scope: shared` are **not counted against you**.

## Exceeding a rate limit

In the case that a rate limit is exceeded, the API returns an **HTTP 429** response code with a JSON
body. Your application should rely on the **`Retry-After` header** or the **`retry_after` field** to
determine when to retry the request.

Normal route rate-limiting headers are **also sent** in a 429 response.

## Rate Limit Response Structure

| Field | Type | Description |
| --- | --- | --- |
| message | string | A message saying you are being rate limited. |
| retry_after | float | The number of seconds to wait before submitting another request. |
| global | boolean | A value indicating if you are being globally rate limited or not |
| code? | integer | An error code (see the JSON error codes in the opcodes and status codes reference) for some limits |

`code?` is optional — the `?` is upstream's own optionality marker.

## Example: exceeded user rate limit response

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

## Example: exceeded resource rate limit response

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

Note the two details this example carries that the user example does not: the message text is
`"The resource is being rate limited."` rather than `"You are being rate limited."`, and
`X-RateLimit-Remaining` is `9` — a shared resource limit can fire while your own bucket still has
quota.

## Example: exceeded global rate limit response

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

The global example carries **no** `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`,
`X-RateLimit-Reset-After` or `X-RateLimit-Bucket` headers — only `X-RateLimit-Global: true` and
`X-RateLimit-Scope: global`.

## Global rate limit figures

- **All bots can make up to 50 requests per second** to the API.
- If **no authorization header** is provided, the limit is applied to the **IP address**.
- The global limit is **independent of any individual rate limit on a route**.
- Upstream's own caveat: if your bot gets big enough, based on its functionality, it may be
  impossible to stay below 50 requests per second during normal operations.

### Diagnosing global rate limit issues

- Global rate limit issues **generally show up as repeatedly getting banned from the Discord API when
  your bot starts**.
- If your bot gets temporarily Cloudflare banned from the Discord API **every once in a while**, it is
  most likely **not** a global rate limit issue. You probably had a **spike of errors that was not
  properly handled** and hit Discord's error threshold.
- If you are experiencing **repeated** Cloudflare bans within normal operations of your bot, you can
  reach out to support to see if you qualify for **increased global rate limits**. Contact Discord
  support at `https://dis.gd/rate-limit`.

### The interaction endpoint exemption

**Interaction endpoints are not bound to the bot's Global Rate Limit.** (Upstream links this to the
Receiving and Responding endpoints section of the Interactions documentation.)

## Invalid Request Limit, also known as Cloudflare bans

IP addresses that make too many invalid HTTP requests are **automatically and temporarily restricted**
from accessing the Discord API.

- **The limit is 10,000 per 10 minutes.**
- **An invalid request is one that results in a 401, 403, or 429 status.**

### How to avoid each invalid status

| Status | How upstream says to avoid it |
| --- | --- |
| **401** | Provide a valid token in the authorization header when required, and stop further requests after a token becomes invalid. |
| **403** | Inspect role or channel permissions, and do not make requests that are restricted by such permissions. |
| **429** | Inspect the rate limit headers documented above, and do not make requests on exhausted buckets until after they have reset. *429 errors returned with `X-RateLimit-Scope: shared` are not counted against you.* |

All applications should make reasonable attempts to avoid making invalid requests.

### The sustained-rate figure

Large applications — especially those that can potentially make 10,000 requests per 10 minutes, which
upstream computes as **a sustained 16 to 17 requests per second** — should consider **logging and
tracking the rate of invalid requests** to avoid reaching this hard limit.

### Other invalid statuses

You are expected to reasonably account for other invalid statuses beyond 401, 403 and 429. Upstream's
worked example: **if a webhook returns a 404 status you should not attempt to use it again** —
repeated attempts to do so will result in a temporary restriction.

## Every numeric figure the page states

| Figure | Where it applies |
| --- | --- |
| **50 requests per second** | Global rate limit for all bots; applied to the IP address when no authorization header is provided. |
| **10,000 per 10 minutes** | Invalid request limit (Cloudflare ban threshold). |
| **16 to 17 requests per second** | Upstream's restatement of 10,000 per 10 minutes as a sustained rate. |
| **429** | HTTP status returned when a rate limit is exceeded. |
| **401, 403, 429** | The three statuses that count as an invalid request. |
| **404** | The status upstream names as an example of another invalid status you must account for (a dead webhook). |
| **3** | Number of top-level resources used in per-route limit calculation (channel, guild, webhook). |
| **7** | Number of rate limit response headers (5 always-optional plus 2 returned only on 429). |
| **1470173023**, **1470173023.123** | Example `X-RateLimit-Reset` epoch values, integer and decimal forms. |
| **64.57**, **1336.57** | Example `retry_after` values (user/global and resource examples). |
| **65**, **1337** | Example `Retry-After` header values, integer seconds. |

## Source

Discord Developer Documentation, `https://docs.discord.com/developers/topics/rate-limits`,
retrieved 2026-08-26.
