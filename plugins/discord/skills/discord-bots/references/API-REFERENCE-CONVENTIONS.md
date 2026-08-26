# Discord API Reference Conventions

Everything the Discord API reference page states: base URL, versioning, authentication, snowflakes,
serialisation, HTTP and Gateway conventions, message formatting, image and CDN formats, file
uploads, and locales.

Source: [API Reference](https://docs.discord.com/developers/reference), retrieved 2026-08-26.

## Contents

- [Base URL](#base-url)
- [API versioning](#api-versioning)
- [Error messages](#error-messages)
- [Authentication](#authentication)
- [Encryption](#encryption)
- [Snowflakes](#snowflakes)
- [Snowflake IDs in pagination](#snowflake-ids-in-pagination)
- [ID serialization](#id-serialization)
- [ISO8601 date/time](#iso8601-datetime)
- [Nullable and optional resource fields](#nullable-and-optional-resource-fields)
- [Consistency](#consistency)
- [HTTP API](#http-api)
- [Gateway (WebSocket) API](#gateway-websocket-api)
- [Message formatting](#message-formatting)
- [Image formatting](#image-formatting)
- [CDN endpoints](#cdn-endpoints)
- [Image data](#image-data)
- [Signed attachment CDN URLs](#signed-attachment-cdn-urls)
- [Uploading files](#uploading-files)
- [Editing message attachments](#editing-message-attachments)
- [File type filtering](#file-type-filtering)
- [Locales](#locales)

The Discord API is a REST API that allows you to interact with Discord data from your own
applications. It is the primary way to interact with Discord from your own code.

## Base URL

```
https://discord.com/api
```

## API versioning

> **Danger**
> Some API and Gateway versions are now non-functioning, and are labeled as discontinued in the
> table below for posterity. Trying to use these versions will fail and return
> `400 Bad Request`.

Discord exposes different versions of the API. Specify which version to use by including it in the
request path like `https://discord.com/api/v{version_number}`. Omitting the version number from the
route routes requests to the current default version (marked below).

**API Versions**

| Version | Status       | Default |
| ------- | ------------ | ------- |
| 10      | Available    |         |
| 9       | Available    |         |
| 8       | Deprecated   |         |
| 7       | Deprecated   |         |
| 6       | Deprecated   | ✓       |
| 5       | Discontinued |         |
| 4       | Discontinued |         |
| 3       | Discontinued |         |

The change log for the newest API version is the Discord change log — see `CHANGELOG-2024-AND-LATER.md`
and `CHANGELOG-EARLIER.md` in this skill.

## Error messages

Starting in API v8, error formatting in form error responses was improved. The response tells you
which JSON key contains the error, the error code, and a human readable error message. Discord adds
new error messages frequently, so a complete list of errors is not feasible and would be almost
instantly out of date. The upstream gives these three examples instead.

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

## Authentication

Authenticating with the Discord API can be done in one of two ways:

1. Using a **bot token** found on the Bot page within your app's settings. For more information on
   bots see "bots vs user accounts" in the OAuth2 documentation.
2. Using an **OAuth2 bearer token** gained through the OAuth2 API.

For all authentication types, authentication is performed with the `Authorization` HTTP header in
the format `Authorization: TOKEN_TYPE TOKEN`.

**Example Bot Token Authorization Header**

```
Authorization: Bot MTk4NjIyNDgzNDcxOTI1MjQ4.EXAMPLE.NOT_A_REAL_TOKEN_REDACTED
```

Discord's own page prints a full example token here. It is replaced above with a placeholder of the same shape, because a literal token string trips secret scanners in any repository that carries this plugin. The shape is what the page teaches: three parts separated by dots, the first being the base64-encoded application ID.

**Example Bearer Token Authorization Header**

```
Authorization: Bearer EXAMPLE_BEARER_TOKEN_REDACTED
```

## Encryption

All HTTP-layer services and protocols (e.g. HTTP, WebSocket) within the Discord API are using
**TLS 1.2**.

## Snowflakes

Discord utilizes Twitter's
[snowflake](https://github.com/twitter-archive/snowflake/tree/snowflake-2010) format for uniquely
identifiable descriptors (IDs). These IDs are guaranteed to be unique across all of Discord, except
in some unique scenarios in which child objects share their parent's ID. Because snowflake IDs are
up to **64 bits** in size (e.g. a `uint64`), they are **always returned as strings** in the HTTP API
to prevent integer overflows in some languages. See Gateway ETF/JSON encoding and compression for
more information regarding Gateway encoding.

**Snowflake ID Broken Down in Binary**

```
111111111111111111111111111111111111111111 11111 11111 111111111111
64                                         22    17    12          0
```

**Snowflake ID Format Structure (Left to Right)**

| Field               | Bits     | Number of bits | Description                                                                  | Retrieval                           |
| ------------------- | -------- | -------------- | ---------------------------------------------------------------------------- | ----------------------------------- |
| Timestamp           | 63 to 22 | 42 bits        | Milliseconds since Discord Epoch, the first second of 2015 or 1420070400000. | `(snowflake >> 22) + 1420070400000` |
| Internal worker ID  | 21 to 17 | 5 bits         |                                                                              | `(snowflake & 0x3E0000) >> 17`      |
| Internal process ID | 16 to 12 | 5 bits         |                                                                              | `(snowflake & 0x1F000) >> 12`       |
| Increment           | 11 to 0  | 12 bits        | For every ID that is generated on that process, this number is incremented   | `snowflake & 0xFFF`                 |

The upstream leaves the Description column blank for Internal worker ID and Internal process ID.

### Convert snowflake to DateTime

The upstream renders an inline diagram walking one snowflake through the conversion. Its stated
values:

- Snowflake: `175928847299117063`
- To binary: `000000100111000100000110010110101100000100` (42-bit timestamp, blue) `00001` (5-bit
  internal worker ID, red) `00000` (5-bit internal process ID, green) `000000000111` (12-bit
  increment, incremented for every generated ID on that process, blue)
- Bit boundaries marked on the diagram: `64`, `22`, `17`, `12`, `0`
- Timestamp portion to decimal: `41944705796`
- Plus the Discord Epoch (unix timestamp in ms) `1420070400000` = `1462015105796`
- Parsed as a unix timestamp in ms: `2016-04-30 11:18:25.796 UTC`

The 42-bit timestamp field is annotated "Number of milliseconds since the Discord epoch (first
seconds of 2015)".

## Snowflake IDs in pagination

Discord typically uses snowflake IDs in many API routes for pagination. The standardized pagination
paradigm is one in which you can specify IDs `before` and `after` in combination with `limit` to
retrieve a desired page of results. Refer to the specific endpoint documentation for details.

Snowflake IDs are just numbers with a timestamp, so when dealing with pagination where you want
results from the beginning of time (in Discord Epoch, but `0` works here too) or before/after a
specific time, you can generate a snowflake ID for that time.

**Generating a snowflake ID from a Timestamp Example**

```
(timestamp_ms - DISCORD_EPOCH) << 22
```

## ID serialization

There are some cases in which the API and Gateway may return IDs in an unexpected format.
Internally, Discord stores IDs as integer snowflakes. When IDs are serialized to JSON, `bigints` are
transformed into strings. Given that all Discord IDs are snowflakes, **you should always expect a
string**.

However, there are cases in which passing something to the API will instead return IDs serialized as
an integer; this is the case when you send the API or Gateway a value in an `id` field that is not
`bigint` size. For example, when requesting `GUILD_MEMBERS_CHUNK` from the gateway:

```
// Send
{
  op: 8,
  d: {
    guild_id: '308994132968210433',
    user_ids: [ '123123' ]
  }
}

// Receive
{
  t: 'GUILD_MEMBERS_CHUNK',
  s: 3,
  op: 0,
  d: {
    not_found: [ 123123 ],
    members: [],
    guild_id: '308994132968210433'
  }
}
```

The sent `user_id` is not a `bigint`; therefore, when it is serialized back to JSON by Discord, it is
not transformed into a string. **This will never happen with IDs that come from Discord.** But it can
happen if you send malformed data in your requests.

## ISO8601 date/time

Discord utilizes the
[ISO8601 format](https://www.loc.gov/standards/datetime/iso-tc154-wg5_n0038_iso_wd_8601-1_2016-02-16.pdf)
for most Date/Times returned in its models. This format is referred to as type `ISO8601` within
tables in the Discord documentation.

## Nullable and optional resource fields

Resource fields that may contain a `null` value have **types** that are prefixed with a question
mark. Resource fields that are optional have **names** that are suffixed with a question mark.

**Example Nullable and Optional Fields**

| Field                        | Type    |
| ---------------------------- | ------- |
| optional\_field?             | string  |
| nullable\_field              | ?string |
| optional\_and\_nullable\_field? | ?string |

## Consistency

Discord operates at a scale where true consistency is impossible. Because of this, lots of
operations in the API and in between Discord's services are
[eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency). Due to this, client
actions can never be serialized and may be executed in any order (if executed at all). Along with
these constraints, events in Discord may:

- Never be sent to a client
- Be sent exactly one time to the client
- Be sent up to N times per client

Clients should operate on events and results from the API in as much of an idempotent behavior as
possible.

## HTTP API

### User Agent

Clients using the HTTP API **must** provide a valid
[User Agent](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.1.5) which specifies information
about the client library and version in the following format:

**User Agent Example**

```
User-Agent: DiscordBot ($url, $versionNumber)
```

Clients may append more information and metadata to the end of this string as they wish.

> **Note**
> Client requests that do not have a valid User Agent specified may be blocked and return a
> [Cloudflare error](https://support.cloudflare.com/hc/en-us/articles/360029779472-Troubleshooting-Cloudflare-1XXX-errors).

### Content Type

Clients using the HTTP API must provide a valid `Content-Type` header, either `application/json`,
`application/x-www-form-urlencoded`, or `multipart/form-data`, except where specified. Failing to do
so results in a `50035` "Invalid form body" error.

### Rate Limiting

The HTTP API implements a process for limiting and preventing excessive requests in accordance with
[RFC 6585](https://tools.ietf.org/html/rfc6585#section-4). API users that regularly hit and ignore
rate limits will have their API keys revoked, and be blocked from the platform. For more information
on rate limiting of requests, the upstream points at its Rate Limits topic page — call the Skill
tool with `"discord-platform"`.

### Boolean Query Strings

Certain endpoints in the API are documented to accept booleans for their query string parameters.
While there is no standard system for boolean representation in query string parameters, Discord
represents such cases using `True`, `true`, or `1` for true and `False`, `false` or `0` for false.

### Array Query Strings

Certain endpoints in the API are documented to accept arrays for their query string parameters.
Unless otherwise specified, Discord represents such cases using multiple instances of the same query
string parameter. For example, `?id=123&id=456` for `["123", "456"]`.

## Gateway (WebSocket) API

Discord's Gateway API is used for maintaining persistent, stateful websocket connections between
your client and Discord's servers. These connections are used for sending and receiving real-time
events your client can use to track and update local state. The Gateway API uses secure websocket
connections as specified in [RFC 6455](https://tools.ietf.org/html/rfc6455). For information on
opening Gateway connections, call the Skill tool with `"discord-gateway"`.

## Message formatting

Discord utilizes a subset of markdown for rendering message content on its clients, while also
adding some custom functionality to enable things like mentioning users and channels. This
functionality uses the following formats.

**Formats**

| Type                                | Structure                                | Example                               |
| ----------------------------------- | ---------------------------------------- | ------------------------------------- |
| User                                | `<@USER_ID>`                             | `<@80351110224678912>`                |
| User \*                             | `<@!USER_ID>`                            | `<@!80351110224678912>`               |
| Channel                             | `<#CHANNEL_ID>`                          | `<#103735883630395392>`               |
| Role                                | `<@&ROLE_ID>`                            | `<@&165511591545143296>`              |
| Slash command                       | `</NAME:COMMAND_ID>`                     | `</airhorn:816437322781949972>`       |
| Slash command with subcommand       | `</NAME SUBCOMMAND:ID>`                  | `</foo bar:123456789012345678>`       |
| Slash command with subcommand group | `</NAME SUBCOMMAND_GROUP SUBCOMMAND:ID>` | `</foo group bar:123456789012345678>` |
| Standard emoji                      | Unicode characters                       | 🪴                                    |
| Custom emoji                        | `<:NAME:ID>`                             | `<:mmLol:216154654256398347>`         |
| Animated custom emoji               | `<a:NAME:ID>`                            | `<a:b1nzy:392938283556143104>`        |
| Unix timestamp                      | `<t:TIMESTAMP>`                          | `<t:1618953630>`                      |
| Styled unix timestamp               | `<t:TIMESTAMP:STYLE>`                    | `<t:1618953630:d>`                    |
| Guild navigation                    | `<id:TYPE>`                              | See below                             |

Using the markdown for users or roles will mention the target(s), and notify them depending on the
sender's permissions as well as the value of the `allowed_mentions` field when creating a message.

Standard emoji are currently rendered using [Twemoji](https://github.com/jdecked/twemoji) for
Desktop and Android while iOS devices use Apple's native emoji set.

Timestamps are expressed in **seconds** and display the given timestamp in the user's timezone and
locale.

\* User mentions with an exclamation point are **deprecated** and should be handled like any other
user mention.

**Timestamp Styles**

| Style | Example Output                   | Description             |
| ----- | -------------------------------- | ----------------------- |
| t     | 16:20                            | Short Time              |
| T     | 16:20:30                         | Medium Time             |
| d     | 20/04/2021                       | Short Date              |
| D     | April 20, 2021                   | Long Date               |
| f \*  | April 20, 2021 at 16:20          | Long Date, Short Time   |
| F     | Tuesday, April 20, 2021 at 16:20 | Full Date, Short Time   |
| s     | 20/04/2021, 16:20                | Short Date, Short Time  |
| S     | 20/04/2021, 16:20:30             | Short Date, Medium Time |
| R     | 4 years ago                      | Relative Time           |

\* default

**Guild Navigation Types**

Guild navigation types link to the corresponding resource in the current server.

| Full Syntax            | Linked Resource                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| `<id:customize>`       | Channel & Roles tab with Onboarding prompts (see Guild Onboarding object in `discord-rest`)  |
| `<id:browse>`          | Browse Channels tab                                                                          |
| `<id:guide>`           | [Server Guide](https://support.discord.com/hc/en-us/articles/13497665141655) tab              |
| `<id:linked-roles>`    | [Linked Roles](https://support.discord.com/hc/en-us/articles/10388356626711) tab               |
| `<id:linked-roles:id>` | Specific linked role, opening the connection modal on click (the second `id` is the role id) |

## Image formatting

**Image Base URL**

```
https://cdn.discordapp.com/
```

Discord uses ids and hashes to render images in the client. These hashes can be retrieved through
various API requests, like Get User. Below are the formats, size limitations, and CDN endpoints for
images in Discord. **The returned format can be changed by changing the extension name at the end of
the URL. The returned size can be changed by appending a querystring of `?size=desired_size` to the
URL. Image size can be any power of two between 16 and 4096.**

> **Note**
> Animated images uploaded as WebP or AVIF do not convert cleanly to GIF. Apps should request
> animated images as WebP for maximum compatibility, as this works regardless of the original upload
> format.

**Image Formats**

| Name   | Extension   |
| ------ | ----------- |
| JPEG   | .jpg, .jpeg |
| PNG    | .png        |
| WebP   | .webp       |
| GIF    | .gif        |
| Lottie | .json       |

## CDN endpoints

All 22 CDN endpoints, with the exact path template and the formats each supports. Paths are relative
to the image base URL `https://cdn.discordapp.com/`. Bracketed segments are the field the value comes
from; the object each field belongs to is named in parentheses.

| Type                        | Path                                                                                                              | Supports             |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------- |
| Custom Emoji                | `emojis/{emoji_id}.png` \*\*\*\*\* (emoji object)                                                                  | PNG, JPEG, WebP, GIF |
| Guild Icon                  | `icons/{guild_id}/{guild_icon}.png` \* (guild object)                                                              | PNG, JPEG, WebP, GIF |
| Guild Splash                | `splashes/{guild_id}/{guild_splash}.png` (guild object)                                                            | PNG, JPEG, WebP      |
| Guild Discovery Splash      | `discovery-splashes/{guild_id}/{guild_discovery_splash}.png` (guild object)                                        | PNG, JPEG, WebP      |
| Guild Banner                | `banners/{guild_id}/{guild_banner}.png` \* (guild object)                                                          | PNG, JPEG, WebP, GIF |
| User Banner                 | `banners/{user_id}/{user_banner}.png` \* (user object)                                                             | PNG, JPEG, WebP, GIF |
| Default User Avatar         | `embed/avatars/{index}.png` \*\* \*\*\* (user object)                                                              | PNG                  |
| User Avatar                 | `avatars/{user_id}/{user_avatar}.png` \* (user object)                                                             | PNG, JPEG, WebP, GIF |
| Guild Member Avatar         | `guilds/{guild_id}/users/{user_id}/avatars/{member_avatar}.png` \* (guild, user, guild member objects)              | PNG, JPEG, WebP, GIF |
| Avatar Decoration           | `avatar-decoration-presets/{avatar_decoration_data_asset}.png` (avatar decoration data object)                      | PNG                  |
| Application Icon            | `app-icons/{application_id}/{icon}.png` (application object)                                                       | PNG, JPEG, WebP      |
| Application Cover           | `app-icons/{application_id}/{cover_image}.png` (application object)                                                | PNG, JPEG, WebP      |
| Application Asset           | `app-assets/{application_id}/{asset_id}.png` (application object; asset_id from activity assets)                    | PNG, JPEG, WebP      |
| Achievement Icon            | `app-assets/{application_id}/achievements/{achievement_id}/icons/{icon_hash}.png` (legacy Game SDK user achievement) | PNG, JPEG, WebP      |
| Store Page Asset            | `app-assets/{application_id}/store/asset_id` (application object)                                                  | PNG, JPEG, WebP      |
| Sticker Pack Banner         | `app-assets/710982414301790216/store/{sticker_pack_banner_asset_id}.png` (sticker pack object)                      | PNG, JPEG, WebP      |
| Team Icon                   | `team-icons/{team_id}/{team_icon}.png` (team object)                                                               | PNG, JPEG, WebP      |
| Sticker                     | `stickers/{sticker_id}.png` \*\*\* \*\*\*\* (sticker object)                                                       | PNG, Lottie, GIF     |
| Role Icon                   | `role-icons/{role_id}/{role_icon}.png` (role object)                                                               | PNG, JPEG, WebP      |
| Guild Scheduled Event Cover | `guild-events/{scheduled_event_id}/{scheduled_event_cover_image}.png` (guild scheduled event object)                | PNG, JPEG, WebP      |
| Guild Member Banner         | `guilds/{guild_id}/users/{user_id}/banners/{member_banner}.png` \* (guild, user, guild member objects)              | PNG, JPEG, WebP, GIF |
| Guild Tag Badge             | `guild-tag-badges/{guild_id}/{badge_hash}.png` (guild object; badge_hash from user primary guild)                   | PNG, JPEG, WebP      |

**\*** In the case of endpoints that support GIFs, the hash will begin with `a_` if it is available in
an animated format (example: `a_1269e74af4df7417b13759eae50c83dc`). These images can be retrieved as
animated WebP using the `.webp` file extension **and** the `?animated=true` querystring parameter.

**\*\*** In the case of the Default User Avatar endpoint, the value for `index` depends on whether the
user is migrated to the new username system. For users on the **new** username system, `index` is
`(user_id >> 22) % 6`. For users on the **legacy** username system, `index` is `discriminator % 5`.

**\*\*\*** In the case of the Default User Avatar and Sticker endpoints, the size of images returned
is constant with the `size` querystring parameter being **ignored**.

**\*\*\*\*** In the case of the Sticker endpoint, the sticker will be available as **PNG** if its
`format_type` is `PNG` or `APNG`, **GIF** if its `format_type` is `GIF`, and as
[**Lottie**](https://airbnb.io/lottie/#/) if its `format_type` is `LOTTIE`.

**\*\*\*\*\*** For Custom Emoji, Discord highly recommends requesting emojis as **WebP** for maximum
performance and compatibility. Emojis can be uploaded as JPEG, PNG, GIF, WebP, and AVIF formats. WebP
and AVIF formats must be requested as WebP since they don't convert well to other formats. The
Discord client uses WebP for all emojis displayed in-app.

> **Info**
> Sticker GIFs do **not** use the CDN base URL, and can be accessed at
> `https://media.discordapp.net/stickers/<sticker_id>.gif`.

## Image data

Image data is a [Data URI scheme](https://en.wikipedia.org/wiki/Data_URI_scheme) that supports
**JPG, GIF, and PNG** formats. An example Data URI format is:

```
data:image/jpeg;base64,BASE64_ENCODED_JPEG_IMAGE_DATA
```

Ensure you use the proper content type (`image/jpeg`, `image/png`, `image/gif`) that matches the
image data being provided.

## Signed attachment CDN URLs

Attachments uploaded to Discord's CDN (like user and bot-uploaded images) have **signed URLs with a
preset expiry time**. Discord automatically refreshes attachment CDN URLs that appear within the
client, so when your app receives a payload with a signed URL (like when you fetch a message), it
will be valid.

When passing CDN URLs into API fields, like `url` in an embed image object and `avatar_url` for
webhooks, your app can pass the CDN URL **without any parameters** as the value and Discord will
automatically render and refresh the URL.

The standard CDN endpoints listed above are **not signed**, so they will not expire.

**Example Attachment CDN URL**

```
https://cdn.discordapp.com/attachments/1012345678900020080/1234567891233211234/my_image.png?ex=65d903de&is=65c68ede&hm=2481f30dd67f503f54d020ae3b5533b9987fae4e55f2b4e3926e08a3fa3ee24f&
```

**Attachment CDN URL Parameters**

| Parameter | Description                                                     |
| --------- | --------------------------------------------------------------- |
| ex        | Hex timestamp indicating when an attachment CDN URL will expire |
| is        | Hex timestamp indicating when the URL was issued                |
| hm        | Unique signature that remains valid until the URL's expiration  |

## Uploading files

> **Info**
> The file upload size limit applies to **each file** in a request. The default limit is `10 MiB`
> for all users, but may be higher for users depending on their
> [Nitro](https://support.discord.com/hc/en-us/articles/115000435108-What-are-Nitro-Nitro-Basic)
> status or by the server's
> [Boost Tier](https://support.discord.com/hc/en-us/articles/360028038352-Server-Boosting-FAQ-#h_419c3bd5-addd-4989-b7cf-c7957ef92583).
> The `attachment_size_limit` value provided when working with interactions is calculated as the
> **maximum** of these values.

Some endpoints support file attachments, indicated by the `files[n]` parameter. To add file(s), the
standard `application/json` body must be replaced by a `multipart/form-data` body. The JSON message
body can optionally be provided using the `payload_json` parameter.

All `files[n]` parameters must include a valid `Content-Disposition` subpart header with a `filename`
and unique `name` parameter. Each file parameter must be uniquely named in the format `files[n]` such
as `files[0]`, `files[1]`, or `files[42]`. The suffixed index `n` is the **snowflake placeholder**
that can be used in the `attachments` field, which can be passed to the `payload_json` parameter (or
to interaction callback data payloads).

Images can also be referenced in embeds using the `attachment://filename` URL.

## Editing message attachments

The `attachments` JSON parameter includes **all** files that will be appended to the message,
including new files and their respective snowflake placeholders. When making a `PATCH` request, only
files listed in the `attachments` parameter will be appended to the message. **Any previously-added
files that aren't included will be removed.**

The `description` and `is_spoiler` fields of existing attachments can optionally be updated.

**Example Request Bodies (multipart/form-data)**

These examples are small sections of an HTTP request to demonstrate behavior of this endpoint —
client libraries will set their own form boundaries (`boundary` is just an example). For more
information, refer to the
[multipart/form-data spec](https://tools.ietf.org/html/rfc7578#section-4).

This example demonstrates usage of the endpoint **without** `payload_json`.

```
--boundary
Content-Disposition: form-data; name="content"

Hello, World!
--boundary
Content-Disposition: form-data; name="tts"

true
--boundary--
```

This example demonstrates usage of the endpoint **with** `payload_json` and all content fields
(`content`, `embeds`, `files[n]`) set.

```
--boundary
Content-Disposition: form-data; name="payload_json"
Content-Type: application/json

{
  "content": "Hello, World!",
  "embeds": [{
    "title": "Hello, Embed!",
    "description": "This is an embedded message.",
    "thumbnail": {
      "url": "attachment://myfilename.png"
    },
    "image": {
      "url": "attachment://mygif.gif"
    }
  }],
  "message_reference": {
    "message_id": "233648473390448641"
  },
  "attachments": [{
      "id": 0,
      "description": "Image of a cute little cat",
      "filename": "myfilename.png"
  }, {
      "id": 1,
      "description": "Rickroll gif",
      "filename": "mygif.gif"
  }]
}
--boundary
Content-Disposition: form-data; name="files[0]"; filename="myfilename.png"
Content-Type: image/png

[image bytes]
--boundary
Content-Disposition: form-data; name="files[1]"; filename="mygif.gif"
Content-Type: image/gif

[image bytes]
--boundary--
```

**Using Attachments within Embeds**

You can upload attachments when creating a message and use those attachments within your embed. To
do this, upload files as part of your `multipart/form-data` body. Make sure that you're uploading
files which contain a filename, as you will need to reference it in your payload.

> **Note**
> Only `.jpg`, `.jpeg`, `.png`, `.webp`, and `.gif` may be used at this time. Other file types are
> not supported.

Within an embed object, you can set an image to use an attachment as its URL with the attachment
scheme syntax: `attachment://filename.png`

For example:

```
{
  "embeds": [{
    "image": {
      "url": "attachment://screenshot.png"
    }
  }]
}
```

## File type filtering

You can filter for **up to 10** file types in File Upload components and Slash Command Options. Each
value must be either one of the group names below, or a dot-prefixed file extension (e.g. `.pdf`).
Extensions are case-insensitive and are normalized to lowercase, so `.PDF` and `.pdf` are
equivalent.

Discord recommends using the file groups rather than listing extensions individually. If you do list
extensions individually, include `.jpg` for image uploads and both `.mp4` and `.mov` for video
uploads, as some mobile clients rely on those extensions.

> **Warning**
> This feature only checks the file extension against the filename and **does not inspect the file
> contents**. You are still responsible for validating the actual contents of the file.

The following preset groups are available:

| Group Name | Extensions                                                 |
| ---------- | ---------------------------------------------------------- |
| `image`    | `.png`, `.gif`, `.jpg`, `.jpeg`, `.jfif`, `.webp`, `.avif` |
| `video`    | `.mp4`, `.mov`, `.qt`, `.webm`                             |
| `audio`    | `.mp3`, `.m4a`, `.wav`, `.ogg`, `.opus`, `.flac`           |

> **Warning**
> Do **not** hardcode the extension lists above. They match the file types Discord natively
> supports and are subject to change.

## Locales

All 32 locale codes with their language name and native name.

| Locale | Language Name         | Native Name         |
| ------ | --------------------- | ------------------- |
| id     | Indonesian            | Bahasa Indonesia    |
| da     | Danish                | Dansk               |
| de     | German                | Deutsch             |
| en-GB  | English, UK           | English, UK         |
| en-US  | English, US           | English, US         |
| es-ES  | Spanish               | Español             |
| es-419 | Spanish, LATAM        | Español, LATAM      |
| fr     | French                | Français            |
| hr     | Croatian              | Hrvatski            |
| it     | Italian               | Italiano            |
| lt     | Lithuanian            | Lietuviškai         |
| hu     | Hungarian             | Magyar              |
| nl     | Dutch                 | Nederlands          |
| no     | Norwegian             | Norsk               |
| pl     | Polish                | Polski              |
| pt-BR  | Portuguese, Brazilian | Português do Brasil |
| ro     | Romanian, Romania     | Română              |
| fi     | Finnish               | Suomi               |
| sv-SE  | Swedish               | Svenska             |
| vi     | Vietnamese            | Tiếng Việt          |
| tr     | Turkish               | Türkçe              |
| cs     | Czech                 | Čeština             |
| el     | Greek                 | Ελληνικά            |
| bg     | Bulgarian             | български           |
| ru     | Russian               | Pусский             |
| uk     | Ukrainian             | Українська          |
| hi     | Hindi                 | हिन्दी              |
| th     | Thai                  | ไทย                 |
| zh-CN  | Chinese, China        | 中文                |
| ja     | Japanese              | 日本語              |
| zh-TW  | Chinese, Taiwan       | 繁體中文            |
| ko     | Korean                | 한국어              |

## Source

[Discord Developer Documentation — API Reference](https://docs.discord.com/developers/reference),
retrieved 2026-08-26. Rights holder: Discord Inc.
