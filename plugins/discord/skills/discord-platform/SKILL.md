---
name: discord-platform
description: "Discord platform rules: the rate limit model, threads and App Discovery. Use when the request names Discord rate limits, X-RateLimit-Bucket or a Discord thread."
---

# Discord Platform

Discord's platform-level model: how requests are throttled, how threads behave as a channel variant,
how an app becomes discoverable, and what each platform feature area covers. Distilled from 25 pages
of the Discord Developer Documentation, complete down to every header name, numeric limit, field and
eligibility requirement those pages state.

## The two load-bearing subjects

**Rate limits.** Never hard code a limit — parse the response headers. Seven headers carry the state:
`X-RateLimit-Limit`, `-Remaining`, `-Reset`, `-Reset-After`, `-Bucket` on most responses, plus
`-Global` and `-Scope` only on a 429. The global limit is **50 requests per second per bot**; the
invalid request limit (Cloudflare ban) is **10,000 per 10 minutes** across 401, 403 and 429 statuses.
Per-route buckets key on three top-level resources: `channel_id`, `guild_id`,
`webhook_id`/`webhook_id + webhook_token`. Interaction endpoints are exempt from the global limit.

**Threads.** A thread is a channel object with `owner_id` and `parent_id` repurposed, plus
`member_count` (stops at 50), `message_count`, `total_message_sent` and a `thread_metadata` object of
`archived`, `archive_timestamp`, `auto_archive_duration`, `locked`. Threads require **API v9 or
above**. `SEND_MESSAGES` has no effect in a thread — `SEND_MESSAGES_IN_THREADS` is the one that
matters. Forum channels are type `15`, media channels type `16`, and both accept only threads.

## Reference map

- **[RATE-LIMITS.md](references/RATE-LIMITS.md)**: the complete rate limit model — all seven headers with exact
  semantics, the three `X-RateLimit-Scope` values, per-route buckets and top-level resources, the
  emoji route exception, the Rate Limit Response Structure, all three worked 429 payloads (user,
  resource, global), global limits, the invalid request limit with per-status avoidance guidance, and
  every numeric figure the page states in one table.
- **[THREADS.md](references/THREADS.md)**: the complete thread model — the 13 gateway events dropped below API
  v9, every re-used, repurposed and thread-only field, public/private/announcement thread types,
  locked and archived semantics, auto-archive behaviour, the three thread permission bits, the
  four-field thread member object and both syncing directions, the edit/delete permission matrix, the
  new and repurposed message types, the four enumeration routes, forum (`15`) and media (`16`)
  channels with their own fields and the `PINNED` `(1 << 1)` flag.
- **[DISCOVERY.md](references/DISCOVERY.md)**: App Directory and App Launcher surfaces, the five launcher
  collections and four marker tags, the two-step enabling procedure (verify then opt in) with every
  portal path, the 24-hour appearance delay, the three description fields with their 400/200-character
  limits, tags, support server guidance, and the four-item final compliance checklist.
- **[PLATFORM-FEATURES.md](references/PLATFORM-FEATURES.md)**: one section per platform overview page — bots,
  interactions, components, webhooks, server and channel management, discovery, community servers,
  claim your game, game profiles, rich presence, social layer, plus `bots/overview`. Carries the
  eight-permission table, the four application command types, the six game-claiming eligibility
  requirements and six-step procedure, and a closing table stating which pages are thin overviews.
- **[GUIDE-INDEXES.md](references/GUIDE-INDEXES.md)**: the seven `guides*` navigational hubs with every card,
  target and blurb, plus `how-to-grow-your-game` in full including all five Discord Internal Data
  2025 statistics and the three-stage strategy table. Ends with the complete guide link graph.

## Working notes

- **Parse, do not assume.** Every rate limit figure above is what the page states today; the page
  itself says limits are subject to change and must come from headers at runtime.
- **`X-RateLimit-Scope: shared` is free.** A 429 with that scope does not count toward the invalid
  request limit, so a shared-resource 429 is not a step toward a Cloudflare ban.
- **Emoji routes lie.** They are limited per guild, so the returned quota may be inaccurate and a 429
  can arrive with remaining quota showing.
- **Archived threads are nearly read-only.** Only message deletion is expected to happen in one;
  sending a message auto-unarchives unless a moderator locked it.
- **Discovery criteria live in the portal.** Upstream deliberately does not list the App Verification
  or Discovery qualification criteria in the documentation — it names the portal screens that do.
  `DISCOVERY.md` records that silence rather than guessing at the criteria.
- **Game claiming is Steam-only, non-mobile-only and released-only.** Three hard limitations, plus a
  requirement that the app belong to a team rather than an individual account.

## Related

Call the Skill tool with "discord-rest" for the Channel object a thread is a variant of, the Guild and
Webhook resources, and the JSON error codes a 429 body's `code` field references.
Call the Skill tool with "discord-gateway" for the thread gateway events, intents including
`GUILD_MEMBERS`, and the Guild Create payload carrying the `threads` array.
Call the Skill tool with "discord-interactions" for application commands, message components, modals,
and the interaction endpoints exempt from the global rate limit.
Call the Skill tool with "discord-oauth2" for the bot invite URL, scopes and account linking web flow.
Call the Skill tool with "discord-activities" for Activities, the Embedded App SDK and Entry Point
commands.
Call the Skill tool with "discord-social-sdk" for the Social Layer feature set, provisional accounts,
lobbies and native Rich Presence.
Call the Skill tool with "discord-monetization" for in-app purchases, subscriptions, SKUs and store
page links.
Call the Skill tool with "discord-rpc-voice" for voice infrastructure and RPC.
Call the Skill tool with "discord-bots" for bot building guides and privileged intent review.

## Source

Distilled from the Discord Developer Documentation, retrieved 2026-08-26 — 25 pages:

`topics/rate-limits`, `topics/threads`, `bots/overview`, `discovery/overview`,
`discovery/enabling-discovery`, `discovery/best-practices`, `platform/bots`, `platform/components`,
`platform/interactions`, `platform/webhooks`, `platform/discovery`, `platform/community-servers`,
`platform/claim-your-game`, `platform/game-profiles`, `platform/rich-presence`,
`platform/server-and-channel-management`, `platform/social-layer`, `guides`, `guides/bots`,
`guides/activities`, `guides/social-sdk`, `guides/platform`, `guides/communities`,
`guides/game-development`, `game-development/how-to-grow-your-game`.

Each page is at `https://docs.discord.com/developers/<path>`. Distilled from a local markdown mirror
of those 25 pages, concatenated sha256 `1c6b9113a974dc8f73a81461b2a740e6f17a4efbe5d36e386a9686a3073c653a`.
Original documentation © Discord, Inc.
