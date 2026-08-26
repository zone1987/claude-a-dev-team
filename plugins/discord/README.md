# discord

Source of truth for the **Discord developer platform** — the HTTP API, the Gateway, interactions and
components, OAuth2 and permissions, Activities, the Social SDK, monetization, RPC and voice.

Distilled from **all 159 pages** of the
[Discord Developer Documentation](https://docs.discord.com/developers/intro), published by
Discord Inc. Every field name, type, enum value, intent bit, permission bit, opcode, error code and
endpoint path here was **extracted from those pages**, not written from memory.

## Coverage

| | Count |
|---|---:|
| Documentation pages covered | 159 of 159 |
| Source term coverage | 99.7 % (4,303 of 4,316) |
| Reference files | 84, 55,002 lines |
| Skills | 11 |
| Agents | 4 |
| Commands | 3 |

Every page is fetched as its **markdown twin** — Discord serves one at each page's URL plus `.md` —
so the extraction starts from the documentation's own source rather than from rendered HTML.

Two scripts hold the completeness claim up, and both check in **both directions**:

- **`scripts/verify_page_coverage.py`** — every page in `PAGE-COVERAGE.json` is claimed by a skill
  that carries content, and every skill that exists is assigned pages. With `--refresh-sitemap` it
  compares the live sitemap against the recorded sha256, so a page Discord adds later surfaces as a
  gap instead of going unnoticed.
- **`scripts/verify_references.py`** — every reference file is **linked directly from its
  `SKILL.md`**, every relative link resolves, no file sits at the wrong depth, and every reference
  over 100 lines carries a table of contents. A reference nothing links to is unreachable, which
  loses its content as surely as deleting it.

- **`scripts/audit_terms.py`** — the content check the other two cannot make. It extracts every
  backticked identifier, `SCREAMING_SNAKE` constant, route and table number from each source page and
  looks for it in the reference files, per page. Page coverage proves a page was assigned; link
  checking proves a file is reachable; only this proves the *facts* arrived. Per-page reporting is
  the point: 98 % spread evenly is healthy, while 98 % with one page at 20 % means that page was
  skimmed. Its reverse direction, `--invented`, reports plugin terms absent upstream — which is what
  catches a plausible-sounding field name that Discord never documented.

```bash
python3 scripts/verify_references.py
python3 scripts/verify_page_coverage.py --refresh-sitemap
python3 scripts/audit_terms.py --mirror <mirror-dir> --show 20
python3 scripts/build_inventory.py --check --fetch     # per-page hash comparison
```

`INVENTORY.json` records each page's sha256, its source line count and the files covering it, so
"is this still complete?" is answered by comparing hashes rather than by re-reading the source.

## Skills

Eleven skills, costing **3,003 characters** of the skill listing budget — about 38 % of the 8,000
available at a 200k context window, with 25 to 42 characters of headroom per description so nothing
truncates when Discord is enabled beside another plugin. The depth sits in reference files, which
cost nothing until read.

| Skill | Pages | Covers |
|---|---:|---|
| `discord-bots` | 9 | Base URL, Bot token auth, API versioning, snowflakes, CDN endpoints, locales, the tutorials, the changelog. **Start here.** |
| `discord-local-testing` | cross-cut | Running and testing an app locally: app setup, the transport decision, tunnelling, guild-scoped registration, and the documented failure signatures |
| `discord-rest` | 17 | Guild, Channel, Message, User, Emoji, Sticker, Invite, Webhook, Poll, Audit Log and AutoMod objects, fields and endpoints |
| `discord-gateway` | 7 | The WebSocket connection, sharding, resuming, every intent, every event payload, opcodes, close codes, JSON error codes |
| `discord-interactions` | 7 | Slash commands, interaction responses, and every message component and modal type |
| `discord-oauth2` | 7 | OAuth2 flows and scopes, the complete permission bitfield, teams, linked roles |
| `discord-activities` | 17 | Activities and the Embedded App SDK: every command, event and type, plus the platform guides |
| `discord-social-sdk` | 56 | The game SDK: provisional accounts, account linking, lobbies, relationships, voice, C++/Unity/Unreal |
| `discord-monetization` | 11 | SKUs, entitlements, subscriptions, one-time purchases, IAP for Activities |
| `discord-rpc-voice` | 3 | The local RPC protocol and the voice connection protocol, with every opcode and encryption mode |
| `discord-platform` | 25 | The rate limit model, threads, App Discovery, and the platform feature overviews |

## Agents

| Agent | Model | For |
|---|---|---|
| `discord-dev` | sonnet | **Orchestrator and entry point.** Routes a task to the right skills and specialists; use it when the work spans more than one domain |
| `discord-api-expert` | sonnet | Looking up an exact endpoint, field, intent bit, permission bit, opcode or error code. Read-only |
| `discord-bot-builder` | sonnet | Writing and reviewing bot code, with the right intents, permissions, scopes and response deadlines |
| `discord-activity-dev` | sonnet | Activities and the Embedded App SDK, including the iframe proxy and URL mappings |

## Commands

| Command | For |
|---|---|
| `/discord-lookup <term>` | Print what the documentation says about an endpoint, object, field, intent, permission, opcode or error code — with the source file named |
| `/discord-bot-scaffold <what it should do>` | Scaffold a bot, deriving its intents, permissions, scopes and handlers from the reference files |
| `/discord-docs-sync [--check\|--apply]` | Report drift against docs.discord.com, and re-distil the pages that moved |

## Hook

A `UserPromptSubmit` hook injects a routing hint when a prompt names **exact** Discord API
vocabulary — `MESSAGE_CONTENT`, `applications.commands`, `X-RateLimit-Bucket`, a component type. It
is deliberately silent on the bare word "discord", because a hint on every passing mention is noise,
and noise is what makes a hint ignored. A hook cannot force a skill to load; it only makes the right
choice visible.

## Building a bot with this

1. **Start with `discord-bots`** for the base URL, the auth header and snowflake handling — every
   call needs those.
2. **Pick the transport**: a Gateway bot holds a WebSocket and receives events (`discord-gateway`);
   an HTTP-interactions bot answers POSTs and holds nothing (`discord-interactions`). Many are both.
3. **Derive the intents, permissions and scopes** for each feature before writing code. Missing any
   one of the three produces a different silent failure, and `discord-oauth2` plus `discord-gateway`
   carry the exact bits.
4. **Respect the deadlines**: 3 seconds to acknowledge an interaction, 15 minutes for a followup.
5. **Handle rate limits per bucket**, not globally — `discord-platform` carries every header.

Or hand the whole task to the orchestrator: `@agent-discord:discord-dev`.

## Source

Distilled from the [Discord Developer Documentation](https://docs.discord.com/developers/intro),
© Discord Inc. — all 159 pages listed in
[`sitemap.xml`](https://docs.discord.com/sitemap.xml), sha256
`5f88bd8ed24253a5fc624762d2cfaf5b31fde94edb9ec2f1bbc71851082900ed`, retrieved **2026-08-26** as
their markdown twins.

The page-to-skill map with per-page paths is [`PAGE-COVERAGE.json`](PAGE-COVERAGE.json). Discord
owns the documentation this plugin is derived from; the distillation is licensed MIT as part of this
marketplace.
