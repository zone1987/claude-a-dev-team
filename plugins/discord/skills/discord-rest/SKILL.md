---
name: discord-rest
description: "Discord HTTP API resources: Guild, Channel, Message, User, Emoji, Invite, Webhook, Poll objects and endpoints. Use when the request names a Discord guild, channel or message."
---

# Discord REST API Resources

The resource layer of the Discord HTTP API: every resource object with its complete field
table, every enum and bitfield with its numeric values, and every endpoint with its query
parameters, JSON parameters, response and caveats. Reach for the sibling file that owns the
resource; each one is the verbatim distillation of one upstream page.

## Core model

- **Base URL**: `https://discord.com/api/v10`. The version segment is part of the path, so
  `/guilds/{guild.id}` is requested as `https://discord.com/api/v10/guilds/{guild.id}`.
- **Snowflake IDs are strings** in JSON, not numbers: a snowflake is a 64-bit integer, which
  exceeds the precision JavaScript numbers carry. Compare them as strings.
- **Field notation in every table**, exactly as upstream writes it:
  - `field?` — the field is **optional** and may be absent from the payload.
  - `?type` — the value is **nullable**; the key is present with `null`.
  - `field?` with `?type` — both: may be absent, and may be `null` when present.
- **Read and write shapes differ.** A resource object as returned by a `GET` is not the body a
  `POST` or `PATCH` accepts. The endpoint's own *JSON Params* table is authoritative for a
  write; the object's *Structure* table describes only what comes back.
- **Bitfield values are decimal in the tables** and combine with bitwise OR. Flags marked
  deprecated stay listed because they still arrive on old objects.
- **`X-Audit-Log-Reason`** is accepted by the endpoints whose page says so, and the reason
  surfaces in the guild audit log.

Full request conventions — authentication, rate limits, snowflake structure, image formatting,
error codes — belong to `discord-bots`; this skill covers the resources themselves.

## Reference map

- **[GUILD.md](references/GUILD.md)**: the Guild object plus 14 sub-objects (member, integration, ban,
  widget, welcome screen, onboarding, incidents) and 45 endpoints — the largest resource.
- **[MESSAGE.md](references/MESSAGE.md)**: the Message object, 14 sub-objects (embed, attachment, reaction,
  reference, snapshot, allowed mentions, pin) and 20 endpoints including message search.
- **[CHANNEL.md](references/CHANNEL.md)**: the Channel object, 7 sub-objects (overwrite, thread metadata,
  thread member, forum tag, default reaction) and 24 endpoints covering threads and permissions.
- **[USER.md](references/USER.md)**: the User object, avatar decorations, collectibles, nameplate,
  connections and role connections, with 12 endpoints.
- **[APPLICATION.md](references/APPLICATION.md)**: the Application object, install params, installation
  contexts and install links, with 3 endpoints.
- **[WEBHOOK.md](references/WEBHOOK.md)**: the Webhook object, its three types, and 15 endpoints including
  execution against Slack and GitHub compatible routes.
- **[GUILD-SCHEDULED-EVENT.md](references/GUILD-SCHEDULED-EVENT.md)**: the scheduled event object, its user
  object, the recurrence rule with its limitations and examples, and 6 endpoints.
- **[AUTO-MODERATION.md](references/AUTO-MODERATION.md)**: the rule and action objects, trigger and event
  types, keyword preset lists, and 5 endpoints.
- **[AUDIT-LOG.md](references/AUDIT-LOG.md)**: the audit log, entry and change objects, the complete audit
  log event table and every change key, behind 1 endpoint.
- **[EMOJI.md](references/EMOJI.md)**: the Emoji object with 10 endpoints, split across guild emojis and
  application emojis.
- **[STICKER.md](references/STICKER.md)**: the Sticker, sticker item and sticker pack objects, format and
  type enums, and 8 endpoints.
- **[INVITE.md](references/INVITE.md)**: the Invite object, its metadata and stage instance sub-objects,
  target types, and 5 endpoints including the target-user job.
- **[POLL.md](references/POLL.md)**: the Poll object, create request, media, answer and results objects,
  the layout type, and 2 endpoints.
- **[SOUNDBOARD.md](references/SOUNDBOARD.md)**: the Soundboard Sound object, the sound file constraints,
  and 7 endpoints for guild and default sounds.
- **[VOICE.md](references/VOICE.md)**: the Voice State and Voice Region objects with 5 endpoints for
  reading and modifying voice state.
- **[STAGE-INSTANCE.md](references/STAGE-INSTANCE.md)**: the Stage Instance object, its privacy level, the
  liveness and moderator definitions, auto-closing, and 4 endpoints.
- **[GUILD-TEMPLATE.md](references/GUILD-TEMPLATE.md)**: the Guild Template object and its 6 endpoints.

## Related

Call the Skill tool with "discord-gateway" for the event payloads these objects arrive in.
Call the Skill tool with "discord-interactions" for slash commands, components and interaction
responses that reference these resources.
Call the Skill tool with "discord-oauth2" for scopes, bearer tokens and authorization flows.
Call the Skill tool with "discord-platform" for API versioning, rate limits and error codes.

## Source

Distilled from the [Discord Developer Documentation](https://docs.discord.com/developers),
`docs.discord.com/developers/resources/*` — all 17 resource pages (application, audit-log,
auto-moderation, channel, emoji, guild, guild-scheduled-event, guild-template, invite, message,
poll, soundboard, stage-instance, sticker, user, voice, webhook), retrieved 2026-08-26.

Files in `references/` are generated, not hand-written: `scripts/build_rest_reference.py`
transforms each mirrored page into one reference file, stamped with its source page and sha256.
`scripts/verify_rest_coverage.py` proves coverage in both directions — every upstream table
row, endpoint, code block and heading appears in the output, and no endpoint appears that is
not upstream. Last run: 1,784 table rows, 178 endpoints, 66 code examples, 631 headings,
0 failures.
