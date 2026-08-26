---
name: discord-local-testing
description: "Running and testing a Discord app locally: app setup, tunnelling, guild-scoped commands, debugging. Use when testing a Discord bot locally or before deploying."
---

# Testing a Discord App Locally

Discord's documentation covers local development across several pages and never as one subject.
This skill assembles it: the two transports, the credentials each needs, the tunnel an HTTP app
requires, and the failure signatures upstream names. Every statement here comes from a docs page
cited in `## Source`; where upstream is silent, the reference file says so.

## The decision that governs everything: Gateway or HTTP

An app receives interactions in one of two **mutually exclusive** ways, and this choice decides
whether local development needs a public URL at all:

- **Gateway (the default).** "By default your app will receive interactions via a Gateway
  connection." Your app opens an outbound WebSocket to a WSS URL it fetched from `GET /gateway` or
  `GET /gateway/bot`. Nothing inbound, so **no public URL and no tunnel are needed** — a laptop
  behind NAT works. "If your app is using Gateway-based interactions, you don't need to configure
  an Interactions Endpoint URL."
- **HTTP (opt-in).** You set an **Interactions Endpoint URL** in the app's settings and Discord
  POSTs interactions to it. Discord must reach that URL, so during local development the docs use
  a tunnel that exposes your local server on a public HTTPS address.

Setting an Interactions Endpoint URL opts you *out* of Gateway interactions. Responses to
interactions always go over HTTP, even when the interaction arrived over the Gateway: "If you are
receiving Interactions over the gateway, you **have to respond via HTTP**."

## The fastest iteration loop: guild-scoped commands

This is the single biggest lever on iteration speed, and upstream states it plainly:

> "Guild commands update **instantly**. We recommend you use guild commands for quick testing, and
> global commands when they're ready for public use."

- **Guild**: `POST /applications/{application.id}/guilds/{guild.id}/commands` — "New guild commands
  will be available in the guild immediately."
- **Global**: `POST /applications/{application.id}/commands` — upstream states no propagation
  duration. It states a read-repair mechanism instead, and the Cloudflare tutorial's own comment
  says registering globally "can take o(minutes)". See
  [COMMAND-REGISTRATION.md](references/COMMAND-REGISTRATION.md) for the exact wording of both.
- **Ceiling while iterating**: "There is a global rate limit of 200 application command creates per
  day, per guild."

## Deadlines you will hit before anything else

- **3 seconds** to send an initial response. "You **must send an initial response within 3 seconds
  of receiving the event**. If the 3 second deadline is exceeded, the token will be invalidated."
- **15 minutes** for the interaction token, for editing the response and sending followups.
- **`PING` and signature verification are both mandatory** before an Interactions Endpoint URL will
  save: "If either of these are not complete, your Interactions Endpoint URL will not be
  validated." Discord also re-checks later with deliberately invalid signatures and removes the URL
  if the check fails.

## Reference map

- **[APP-SETUP.md](references/APP-SETUP.md)**: creating the app, the Developer Portal pages
  involved, where Application ID, Public Key and bot token come from and what each is for, token
  reset, privileged intent toggles, installation contexts, install links, and installing to a test
  server and a user account.
- **[GATEWAY-VS-HTTP.md](references/GATEWAY-VS-HTTP.md)**: the two transports side by side and what
  each demands locally. The full HTTP endpoint contract: the `PING`/`PONG` handshake, Ed25519
  verification of `X-Signature-Ed25519` and `X-Signature-Timestamp` against the app's public key
  with upstream's JavaScript, Python and Java code, and what Discord does to an endpoint that fails
  either check. The Gateway connection lifecycle, `IDENTIFY`, heartbeats and the identify limits.
- **[COMMAND-REGISTRATION.md](references/COMMAND-REGISTRATION.md)**: guild-scoped versus global,
  all 10 command endpoints, upsert-by-name semantics, per-scope name uniqueness rules, command
  count ceilings, the 200-creates-per-day limit, `integration_types` and `contexts`, and exactly
  what upstream states about propagation and read-repair.
- **[LOCAL-WORKFLOW.md](references/LOCAL-WORKFLOW.md)**: the walkthroughs assembled into one
  sequence — project setup, `.env` handling, `ngrok http 3000` and `cloudflared tunnel --url` as
  the docs give them, wiring the forwarding URL into the portal, the Cloudflare Workers
  local-then-deploy flow with `wrangler secret put`, and Activity local development with URL
  mappings.
- **[VERIFYING-AND-DEBUGGING.md](references/VERIFYING-AND-DEBUGGING.md)**: how to tell the app
  works, and the documented failure signatures — the missing privileged intent that yields empty
  fields instead of an error, the gateway close codes that mean bad token (`4004`) or bad intents
  (`4013`/`4014`), rate-limit responses and Cloudflare bans while iterating, the JSON error codes
  upstream names for interaction failures, and Activity log viewing on desktop and mobile.

## Related

Call the Skill tool with "discord-bots" for request conventions, authentication and error codes.
Call the Skill tool with "discord-interactions" for the full command, component and response
reference these local tests exercise.
Call the Skill tool with "discord-gateway" for every intent, event and close code in full.
Call the Skill tool with "discord-oauth2" for scopes, bearer tokens and authorization flows.

## Source

Distilled from the [Discord Developer Documentation](https://docs.discord.com/developers),
retrieved 2026-08-26, from these pages:

- `docs.discord.com/developers/quick-start/getting-started`
- `docs.discord.com/developers/tutorials/hosting-on-cloudflare-workers`
- `docs.discord.com/developers/tutorials/developing-a-user-installable-app`
- `docs.discord.com/developers/activities/development-guides/local-development`
- `docs.discord.com/developers/activities/building-an-activity`
- `docs.discord.com/developers/interactions/overview`
- `docs.discord.com/developers/interactions/receiving-and-responding`
- `docs.discord.com/developers/interactions/application-commands`
- `docs.discord.com/developers/platform/interactions`
- `docs.discord.com/developers/events/gateway`
- `docs.discord.com/developers/topics/opcodes-and-status-codes`
- `docs.discord.com/developers/topics/rate-limits`
- `docs.discord.com/developers/reference`
- `docs.discord.com/developers/resources/application`
- `docs.discord.com/developers/bots/overview`
- `docs.discord.com/developers/developer-tools/community-resources`
