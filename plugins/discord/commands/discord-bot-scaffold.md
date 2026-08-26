---
name: discord-bot-scaffold
description: Scaffold a Discord bot with the right intents, permissions, scopes and interaction handling for the features you name.
argument-hint: <what the bot should do> [--library discord.js|discord.py|raw] [--transport gateway|http]
allowed-tools: Read, Glob, Grep, Bash, Write, Edit
model: sonnet
---

# /discord-bot-scaffold

Scaffold a Discord bot for what $ARGUMENTS describes. Ask one question at a time, and skip whatever
the arguments already answer.

## Establish first (one question at a time)

1. **The features**, concretely: which commands, which events, which channels or members it touches.
2. **The transport.** `gateway` for a bot that holds a WebSocket and reacts to events; `http` for one
   that only answers interactions over a webhook endpoint. Both, when it needs events and commands.
3. **The library**, or `raw` for direct HTTP and WebSocket. Ask rather than assume — the project may
   already have one.
4. **Where it runs**, since a serverless target rules out a Gateway connection.

## Then derive, from the reference files rather than from memory

Call the Skill tool with `discord-bots`, then `discord-interactions` and `discord-gateway` as the
features require, plus `discord-rest` for the objects involved and `discord-oauth2` for the install
URL.

For each feature the user named, state:

- **the Gateway intents** it needs, with their bit values, and whether any is privileged,
- **the permission bits** it needs, and the resulting `permissions` integer for the invite URL,
- **the OAuth2 scopes** — `bot`, `applications.commands`, and any others,
- **the endpoints** it calls, with method and path,
- **the interaction callback types** it responds with.

## Then write

- the command registration payload, with every option typed as the documentation specifies,
- the event or interaction handlers, each carrying its required intent as a named constant,
- the signature verification, when the transport is `http` — Ed25519, and answering the `PING` type,
- a deferred response wherever handling can exceed 3 seconds,
- rate limit handling that reads `X-RateLimit-Bucket` and honours `Retry-After`,
- an `.env.example` naming every secret, and never a real token in a tracked file.

## Close by reporting

The files written, the invite URL with its computed `permissions` integer, the intents to enable in
the Developer Portal — flagging any privileged one and that it needs review above 100 guilds — and
the exact reference files each value came from.

Invent no field, intent bit or endpoint path. Take every exact value from the reference files.
