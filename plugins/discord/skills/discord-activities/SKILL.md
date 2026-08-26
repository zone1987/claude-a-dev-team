---
name: discord-activities
description: "Discord Activities and the Embedded App SDK: commands, events, types, layout and mobile. Use when the request names a Discord Activity or the Embedded App SDK."
---

# Discord Activities

Build a Discord Activity: a web app that runs inside the Discord client on desktop, mobile and web,
talking to Discord through `@discord/embedded-app-sdk`.

## Three constraints that catch every first-time author

These are design constraints, not implementation details. Decide the architecture around them.

1. **It runs in an iframe inside the Discord client, not in a browser tab.** Discord loads your public
   URL in an iframe and appends query parameters identifying the launch; communication runs over the
   `postMessage` protocol, which the SDK manages for you. Once the SDK is installed you can no longer
   open the app in your own browser to test it — it has to be launched from Discord. You are also
   competing with the Discord client for CPU, RAM and GPU, because that client keeps running.
   The SDK targets a **single-page** app; nest any other framework inside one.
2. **All network traffic goes through Discord's proxy, so every external host needs a declared URL
   mapping.** Your app is served from `{clientId}.discordsays.com` and a Content Security Policy blocks
   anything unmapped, failing with `blocked:csp`. In the Developer Portal you map a `PREFIX` (`/api`)
   to a `TARGET` (`some-api.com`, protocol omitted, pointing at a directory). This is the single most
   common cause of "works locally, fails in Discord" — a third-party npm module calling its own
   host fails until you map it or call `patchUrlMappings`. WebRTC is unsupported; WebSockets work.
   Only a short list of `discord.com/api` and Discord CDN paths is exempt.
3. **Authorization is the SDK's `authorize` command plus a server-side token exchange, not a
   redirect.** `await discordSdk.ready()` first, then `commands.authorize()` returns a `code`; your
   own server exchanges it at `POST https://discord.com/api/oauth2/token` with the client secret; then
   `commands.authenticate({access_token})` completes the flow. A Redirect URI must still be configured
   but is a placeholder — the SDK handles the return itself. Calling a command outside a granted scope
   errors.

Two more facts worth knowing before you design state: **`instanceId`** is available immediately, before
`ready()`, and is the key every participant of one launch shares — when the last participant leaves,
that instance never returns. And **data from the Discord client is neither trustworthy nor
sanitized**; verify anything that matters through the API from your server.

## Reference map

- **[EMBEDDED-APP-SDK-COMMANDS.md](references/EMBEDDED-APP-SDK-COMMANDS.md)**: installation, the 4 SDK
  methods and all **21 commands**, each with signature, Web/iOS/Android support, required scopes and a
  worked example; plus the instance properties, the layout compat helpers and `patchUrlMappings`.
- **[EMBEDDED-APP-SDK-EVENTS.md](references/EMBEDDED-APP-SDK-EVENTS.md)**: all **13 events** with
  scopes and sample payloads, all **58 interfaces** with every property and type, and all **10 enums**
  with every value including `RPCCloseCodes` and the 24 `OAuthScopes`.
- **[BUILDING-AN-ACTIVITY.md](references/BUILDING-AN-ACTIVITY.md)**: the **8-step** walkthrough, every
  command and file body verbatim — template clone, app creation, tunnel, URL mapping, the Express
  `/api/token` server, `getChannel`, `GET /users/@me/guilds`.
- **[DEVELOPMENT-GUIDES.md](references/DEVELOPMENT-GUIDES.md)**: all **9 development guides** — local
  development and logging, user actions, mobile, layout, networking, multiplayer, growth and referrals,
  assets and metadata, production readiness.
- **[HOW-ACTIVITIES-WORK.md](references/HOW-ACTIVITIES-WORK.md)**: the **6-stage lifecycle**, both
  launch paths (Entry Point command, `LAUNCH_ACTIVITY` callback type `12`), sample projects, and the
  complete design-patterns guide with its iframe-performance and accessibility checklists.
- **[RICH-PRESENCE-IN-ACTIVITIES.md](references/RICH-PRESENCE-IN-ACTIVITIES.md)**: `setActivity()`, the
  `rpc.activities.write` scope, the **6 activity-partial fields**, the 300-asset upload limit and
  external asset URLs.

## Working rules

- **Check platform support before calling a command.** It is uneven: `setOrientationLockState` is
  mobile-only; `encourageHardwareAcceleration`, `setConfig`, `openShareMomentDialog` and
  `startPurchase` are web-only.
- **Guard every newer command.** An older Discord client answers with `RPCErrorCodes.INVALID_COMMAND`;
  catch it and degrade instead of failing.
- **Subscribe to layout through the compat helpers.** `subscribeToLayoutModeUpdatesCompat` covers both
  `ACTIVITY_LAYOUT_MODE_UPDATE` and the older `ACTIVITY_PIP_MODE_UPDATE`.
- **Cache-bust every non-HTML asset.** The proxy strips cache headers only from `text/html`.
- **Set cookies as `SameSite=None Partitioned`** on the full `{clientId}.discordsays.com` domain, or an
  iframe will refuse to store them.

## Related

- Call the Skill tool with "discord-oauth2" for the scopes an activity authorizes with.
- Call the Skill tool with "discord-monetization" for SKUs, entitlements and the purchase flow.
- Call the Skill tool with "discord-rest" for the HTTP endpoints an activity calls, and rate limits.
- Call the Skill tool with "discord-bots" for the bot token the activity-instances API requires.

## Source

Distilled from the Discord Developer Documentation, retrieved 2026-08-26 — all pages under
`https://docs.discord.com/developers/`:

- `developer-tools/embedded-app-sdk`
- `activities/overview`, `activities/how-activities-work`, `activities/building-an-activity`,
  `activities/design-patterns`, `activities/development-guides`
- `activities/development-guides/` + `local-development`, `user-actions`, `mobile`, `layout`,
  `networking`, `multiplayer-experience`, `growth-and-referrals`, `assets-and-metadata`,
  `production-readiness`
- `rich-presence/using-with-the-embedded-app-sdk`
- `platform/activities`
