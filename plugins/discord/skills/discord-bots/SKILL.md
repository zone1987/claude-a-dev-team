---
name: discord-bots
description: "Discord app fundamentals: base URL, Bot token auth, API versioning, snowflakes, CDN, locales. Use when building a Discord bot or app, or naming discord.com/api."
---

# Discord Bots and Apps

The entry point for building on Discord: what an application is, the conventions every HTTP call
obeys, the walkthroughs, and the platform change log.

A **Discord application** is the core entity representing your integration. Every bot, Activity and
Social SDK integration is backed by an application registered at
https://discord.com/developers/applications. Applications hold your credentials, OAuth2 settings, bot
configuration and metadata.

## What every request needs

**Base URL, with the version pinned.** Omitting the version routes to the default, which is still
v6 (deprecated) — always pin explicitly:

```
https://discord.com/api/v10
```

Versions 10 and 9 are **Available**; 8, 7 and 6 are **Deprecated** (6 is the default); 5, 4 and 3 are
**Discontinued** and return `400 Bad Request`.

**Authorization header**, one of exactly two forms — `TOKEN_TYPE TOKEN`:

```
Authorization: Bot MTk4NjIyNDgzNDcxOTI1MjQ4.EXAMPLE.NOT_A_REAL_TOKEN_REDACTED
Authorization: Bearer EXAMPLE_BEARER_TOKEN_REDACTED
```

`Bot` uses the token from the Bot page of your app's settings; `Bearer` uses an OAuth2 access token.

**User-Agent is mandatory** on the HTTP API, in this exact shape. Requests without a valid one "may
be blocked and return a Cloudflare error":

```
User-Agent: DiscordBot ($url, $versionNumber)
```

**Content-Type** must be `application/json`, `application/x-www-form-urlencoded` or
`multipart/form-data`, else you get error `50035` "Invalid form body".

**Snowflakes are strings, never numbers.** IDs are 64-bit, which exceeds JavaScript's safe integer
range of 2^53, so the HTTP API always returns them as JSON strings "to prevent integer overflows in
some languages". Parsing one into a JS `Number` silently corrupts the low bits. Extract the timestamp
with `(snowflake >> 22) + 1420070400000` — the Discord epoch is the first second of 2015. The other
fields are internal worker ID (bits 21–17), internal process ID (bits 16–12) and increment
(bits 11–0).

## Reference map

- **[references/API-REFERENCE-CONVENTIONS.md](references/API-REFERENCE-CONVENTIONS.md)**: the whole
  API reference page — 8 API versions with status, both auth headers, the snowflake bit layout and
  epoch, the ID-serialization caveat, 3 error-response shapes, nullable/optional notation, 13 message
  formatting types, 9 timestamp styles, 5 guild navigation types, 5 image formats, **all 22 CDN
  endpoints** with path templates and supported formats, the `?size=` power-of-two 16–4096 rule,
  signed attachment URLs, file uploads, 3 file-type filter groups, and **all 32 locale codes**.
- **[references/GETTING-STARTED.md](references/GETTING-STARTED.md)**: the complete first-bot
  walkthrough (5 steps, every command and code block verbatim), plus the platform landing page and
  the overview of the 3 app types and their install targets.
- **[references/LOCAL-DEVELOPMENT.md](references/LOCAL-DEVELOPMENT.md)**: running and testing locally
  — the 3 credentials and where each comes from, token regeneration, `.env` handling, Gateway versus
  HTTP interactions endpoint, global versus guild command registration, the `PING`/`PONG` handshake,
  the 2 signature headers, ngrok tunnelling, and 9 named upstream gaps.
- **[references/TUTORIALS.md](references/TUTORIALS.md)**: all 3 tutorials end to end —
  user-installable apps (4 commands with their `integration_types` and `contexts`), Cloudflare Workers
  hosting, and community invites (`role_ids`, `target_users_file`).
- **[references/COMMUNITY-RESOURCES.md](references/COMMUNITY-RESOURCES.md)**: 21 API libraries across
  12 languages, 16 interactions libraries, 3 permission calculators, 2 intent calculators, 2 embed
  visualizers, 2 API-types modules, 1 Game SDK tool, and the OpenAPI preview spec.
- **[references/CHANGELOG-2024-AND-LATER.md](references/CHANGELOG-2024-AND-LATER.md)**: 124 dated
  entries from January 2024 to 14 August 2026, newest first, with tags, summary and full body — every
  new field, deprecation and breaking-change note.
- **[references/CHANGELOG-EARLIER.md](references/CHANGELOG-EARLIER.md)**: the remaining 103 entries,
  19 July 2017 to December 2023, plus the 41 Social SDK link references the page defines.

## Gotchas

- **`?size=` is ignored** by the Default User Avatar and Sticker endpoints; their size is constant.
- **Animated assets** need a hash starting `a_`, fetched as animated WebP with **both** `.webp` and
  `?animated=true`.
- **Attachment CDN URLs are signed and expire** (`ex`, `is`, `hm`); the 22 standard CDN endpoints are
  not. Pass a CDN URL into an API field **without** parameters and Discord refreshes it.
- **Sticker GIFs bypass the CDN base URL**: `https://media.discordapp.net/stickers/<id>.gif`.
- **`PATCH` with `attachments` removes** any previously-added file not listed.
- **Eventual consistency**: an event may never arrive, arrive once, or arrive N times. Be idempotent.
- **Nullable vs optional**: `?type` may be `null`; `name?` may be absent.

## Related

Call the Skill tool with **"discord-rest"** for resource objects and HTTP endpoints (channels,
guilds, messages, users, invites, webhooks), **"discord-gateway"** for the WebSocket lifecycle,
intents, sharding and gateway events, **"discord-interactions"** for slash commands, components,
modals and response types, **"discord-oauth2"** for scopes and authorization flows,
**"discord-platform"** for permissions, rate limits and teams, **"discord-activities"** for embedded
apps and the Embedded App SDK, **"discord-social-sdk"** for game social features and rich presence,
**"discord-monetization"** for SKUs, entitlements and subscriptions, and **"discord-rpc-voice"** for
the local RPC protocol and voice connections.

## Source

Distilled from the Discord Developer Documentation, retrieved **2026-08-26**:

- [API Reference](https://docs.discord.com/developers/reference)
- [Discord Developer Platform](https://docs.discord.com/developers/intro)
- [Overview of Discord Apps](https://docs.discord.com/developers/quick-start/overview-of-apps)
- [Building your first Discord Bot](https://docs.discord.com/developers/quick-start/getting-started)
- [Developing A User-Installable App](https://docs.discord.com/developers/tutorials/developing-a-user-installable-app)
- [Hosting a Reddit API Discord app on Cloudflare Workers](https://docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers)
- [Using Community Invites](https://docs.discord.com/developers/tutorials/using-community-invites)
- [Community Resources](https://docs.discord.com/developers/developer-tools/community-resources)
- [Change Log](https://docs.discord.com/developers/change-log)

Rights holder: Discord Inc.
