# Community Resources

Every library, tool and resource the Discord community resources page lists, with its language and
link.

Source: [Community Resources](https://docs.discord.com/developers/developer-tools/community-resources),
retrieved 2026-08-26.

## Contents

- [Discord Developers server](#discord-developers-server)
- [Libraries (21)](#libraries-21)
- [Interactions libraries (16)](#interactions-libraries-16)
- [OpenAPI specification](#openapi-specification)
- [Permission calculators (3)](#permission-calculators-3)
- [Intent calculators (2)](#intent-calculators-2)
- [Embed visualizers (2)](#embed-visualizers-2)
- [API types (2)](#api-types-2)
- [Game SDK tools (1)](#game-sdk-tools-1)

Community members create tools and resources that help developers build and maintain their apps. From
permissions calculators and embed visualizers to comprehensive libraries for interfacing with the
API, the community has built a wealth of resources.

## Discord Developers server

The [Official Discord Developers server](https://discord.gg/discord-developers) is a **developer ran,
but community driven, support hub**. If you need help with developing something on Discord or want
official updates from the developers, this is the place to be.

## Libraries (21)

**Discord does not maintain official SDKs.** The following table is an *inexhaustive* list of
third-party libraries that have valid rate limit implementations, are recently maintained, and have
large communities of active bots.

###### Discord Libraries

| Name                                                          | Language   |
| ------------------------------------------------------------- | ---------- |
| [Concord](https://github.com/Cogmasters/concord)              | C          |
| [Discord.Net](https://github.com/discord-net/Discord.Net)     | C#         |
| [DSharpPlus](https://github.com/DSharpPlus/DSharpPlus)        | C#         |
| [D++](https://github.com/brainboxdotcc/DPP)                   | C++        |
| [discljord](https://github.com/discljord/discljord)           | Clojure    |
| [DiscordGo](https://github.com/bwmarrin/discordgo)            | Go         |
| [Discord4J](https://github.com/Discord4J/Discord4J)           | Java       |
| [JDA](https://github.com/DV8FromTheWorld/JDA)                 | Java       |
| [discord.js](https://github.com/discordjs/discord.js)         | JavaScript |
| [Eris](https://github.com/abalabahaha/eris)                   | JavaScript |
| [Oceanic](https://github.com/OceanicJS/Oceanic)               | JavaScript |
| [Discordia](https://github.com/SinisterRectus/Discordia)      | Lua        |
| [DiscordPHP](https://github.com/discord-php/DiscordPHP)       | PHP        |
| [discord.py](https://github.com/Rapptz/discord.py)            | Python     |
| [disnake](https://github.com/DisnakeDev/disnake)              | Python     |
| [hikari](https://github.com/hikari-py/hikari)                 | Python     |
| [interactions.py](https://github.com/interactions-py/library) | Python     |
| [nextcord](https://github.com/nextcord/nextcord)              | Python     |
| [pycord](https://github.com/Pycord-Development/pycord)        | Python     |
| [discordrb](https://github.com/shardlab/discordrb)            | Ruby       |
| [Serenity](https://github.com/serenity-rs/serenity)           | Rust       |

Language breakdown: C 1, C# 2, C++ 1, Clojure 1, Go 1, Java 2, JavaScript 3, Lua 1, PHP 1, Python 6,
Ruby 1, Rust 1.

## Interactions libraries (16)

Interactions are described by the upstream as "the great, new way of making a Discord bot". The
following **open-source** libraries provide help for the **security and authentication checks that are
mandatory if you are receiving Interactions via outgoing webhook**. They also include some types for
the Interactions data models.

- **C#**
  - [Discord.Net.Rest](https://github.com/discord-net/Discord.Net)
  - [DSharpPlus.Http.AspNetCore](https://github.com/DSharpPlus/DSharpPlus)
- **Clojure**
  - [ring-discord-auth](https://github.com/JohnnyJayJay/ring-discord-auth)
- **Dart**
  - [nyxx\_interactions](https://github.com/l7ssha/Nyxx)
- **Go**
  - [tempest](https://github.com/amatsagu/tempest)
- **Javascript**
  - [discord-interactions-js](https://github.com/discord/discord-interactions-js)
  - [discord-slash-commands](https://github.com/MeguminSama/discord-slash-commands) and its
    [Deno fork](https://deno.land/x/discord_slash_commands)
  - [slash-create](https://github.com/Snazzah/slash-create)
- **Python**
  - [discord-interactions-python](https://github.com/discord/discord-interactions-python)
  - [discord-interactions.py](https://github.com/LiBa001/discord-interactions.py)
  - [dispike](https://github.com/ms7m/dispike)
  - [flask-discord-interactions](https://github.com/breqdev/flask-discord-interactions)
- **PHP**
  - [discord-interactions-php](https://github.com/discord/discord-interactions-php)
- **Other**
  - [caddy-discord-interactions-verifier](https://github.com/CarsonHoffman/caddy-discord-interactions-verifier)
  - [BotForge's Application Commands Builder & Previewer](https://tools.botforge.org/appbuilder)
  - [Bsati's Slash Command Builder](https://bsati.github.io/dc-app-command-builder/)

## OpenAPI specification

> **Warning**
> The OpenAPI spec is currently in **public preview** and **is subject to breaking changes**.

The public preview of the
[Discord HTTP API specification](https://github.com/discord/discord-api-spec) provides a standard
[OpenAPI 3.1 spec](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md) for the
HTTP API.

## Permission calculators (3)

Permissions in Discord are tricky. These calculators help if you're making a bot for others and
aren't sure how to properly calculate permissions or generate your authorization URL:

- [BotForge's Permissions Calculator](https://tools.botforge.org/permissions)
- [FiniteReality's Permissions Calculator](https://finitereality.github.io/permissions-calculator/?v=0)
- [abalabahaha's Permissions Calculator](https://discordapi.com/permissions.html#0)

## Intent calculators (2)

Gateway Intents are confusing at first. If you're not sure what to send in your Identify payload,
these tools may help:

- [ziad87's Intent Calculator](https://ziad87.net/intents/)
- [Larko's Intent Calculator](https://discord-intents-calculator.vercel.app/)

## Embed visualizers (2)

These tools help you test how embeds will appear inside of Discord:

- [JohnyTheCarrot's Embed Previewer](https://github.com/JohnyTheCarrot/discord-embed-previewer)
  (Browser Extension)
- [AshMW's Embed Previewer](https://embedl.ink) (Embed HTML Generation)

## API types (2)

If you're working on a project that interacts with the API, an API types module can be useful as it
provides type inspection/completion for the Discord API.

| Name                                                                | Language   |
| ------------------------------------------------------------------- | ---------- |
| [dasgo](https://github.com/switchupcb/dasgo)                        | Go         |
| [discord-api-types](https://github.com/discordjs/discord-api-types) | JavaScript |

## Game SDK tools (1)

Discord Game SDK's lobby and networking layer shares similarities with other gaming platforms (i.e.
Valve's Steamworks SDK). The following open source library provides developers a uniform interface for
these shared features and can simplify developing for multiple platforms. **Note: this library is
tailored for Unity3D development.**

- [HouraiNetworking](https://github.com/HouraiTeahouse/HouraiNetworking)

## Source

[Discord Developer Documentation — Community Resources](https://docs.discord.com/developers/developer-tools/community-resources),
retrieved 2026-08-26. Rights holder: Discord Inc.
