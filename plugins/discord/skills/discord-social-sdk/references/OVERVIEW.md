# Discord Social SDK — Overview and Index Pages

Distilled from the three index pages of the Discord Social SDK documentation, retrieved 2026-08-26:
`docs.discord.com/developers/discord-social-sdk/overview`,
`.../discord-social-sdk/getting-started`, and `.../discord-social-sdk/how-to`.

These are **navigation pages**: each is a short intro plus a card grid pointing at the detail pages.
Every fact they state is below, and every card they carry is mapped to the reference file in this
skill that holds that page.

## Contents

- [Integrating the Discord Social SDK (overview)](#integrating-the-discord-social-sdk-overview)
- [Getting Started index](#getting-started-index)
- [Core Concepts index](#core-concepts-index)
- [How To Guides index](#how-to-guides-index)
- [Change logs](#change-logs)

---

## Integrating the Discord Social SDK (overview)

Source: `/discord-social-sdk/overview`.

[Image: Discord Social SDK Hero Image]

**The Discord Social SDK lets you integrate Discord-powered social features directly into your game.**
For an overview of available features, see the **Social Layer for Games** platform page
(`/developers/platform/social-layer`).

Start integrating the SDK into your game with the getting started guides, design guidelines, and code
samples.

### Integrate Social Features in Your Game

| Card | Points at | In this skill |
| --- | --- | --- |
| **Core Concepts** | `/discord-social-sdk/core-concepts` — "Learn how the SDK works and explore its key features." | CORE-CONCEPTS.md |
| **Getting Started Guides** | `/discord-social-sdk/getting-started` — "Follow our step-by-step guides to add the SDK to your game engine." | GETTING-STARTED-CPP.md, GETTING-STARTED-UNITY.md, GETTING-STARTED-UNREAL.md |

### Dive Deeper into the Discord Social SDK

The page embeds a YouTube video, **"Power Player Connections with Discord Social SDK"**
(`https://www.youtube.com/embed/voEc21roLas?si=DBc_jBIJHqMtoDYc`).

| Card | Points at | In this skill |
| --- | --- | --- |
| **Development Guides** | `/discord-social-sdk/development-guides` — "Dive into feature guides for **account linking, friends lists, game invites, and voice chat**." | ACCOUNT-LINKING.md, PROVISIONAL-ACCOUNTS.md, LOBBIES.md, RELATIONSHIPS-AND-FRIENDS.md, MESSAGING.md, VOICE-CHAT.md, RICH-PRESENCE.md |
| **Design Guidelines** | `/discord-social-sdk/design-guidelines` — "Learn how to design your game's UI to integrate social features." | DESIGN-GUIDELINES.md |
| **SDK Reference Docs** | `https://discord.com/developers/docs/social-sdk/index.html` — "Explore the SDK's API reference documentation." | The Doxygen reference; every reference file in this skill lists the anchors it cites. |

### Communication Features

**Discord Social SDK features for text and voice communication are available but capped with rate
limits.**

For current rate limits, see CORE-CONCEPTS.md → Development Rate Limits (upstream:
`/discord-social-sdk/core-concepts/communication-features#rate-limits`). For how to access these
features, see CORE-CONCEPTS.md → Communication Features.

### Get Help & Join the Community

- Join the **DDevs Discord Server** (`https://discord.gg/discord-developers`) and get help from the
  community, share best practices, and discover new ways to enhance your game. **Find Discord in the
  `#social-sdk-dev-help` channel.**
- For additional support, **file a ticket with Developer Support** (`https://dis.gd/social-sdk`) to
  report issues.

(Bug reports specifically: `https://dis.gd/social-sdk-bug-report`, cited on every development guide.)

---

## Getting Started index

Source: `/discord-social-sdk/getting-started`.

The Discord Social SDK allows you to integrate Discord social features into your game. **With the
Discord Social SDK, you can offer a seamless social experience for your players, allowing them to
connect with their friends and communities on Discord without leaving your game.**

If this is your first time learning about the Discord Social SDK, check out the Overview and Core
Concepts for more information on what the SDK can do and how it can benefit your game.

### Let's Get Started

Select a platform to get started.

**If you are unsure which platform to choose, Discord recommends starting with the C++ guide to
familiarize yourself with the SDK's core concepts.**

| Card | Description | In this skill |
| --- | --- | --- |
| **Standalone C++** (`/getting-started/using-c++`) | "For use with custom engines or standalone applications." | GETTING-STARTED-CPP.md |
| **Unity** (`/getting-started/using-unity`) | "For use with Unity." | GETTING-STARTED-UNITY.md |
| **Unreal Engine** (`/getting-started/using-unreal-engine`) | "For use with Unreal Engine." | GETTING-STARTED-UNREAL.md |

**To see a complete list of currently compatible platforms**, see CORE-CONCEPTS.md → Platform
Compatibility.

### Next Steps

**After you've run through a guide for your preferred platform, you can implement features such as a
unified friend list, rich presence, and more.** See the Development Guides for detailed information on
using the SDK for each feature.

---

## Core Concepts index

`docs.discord.com/developers/discord-social-sdk/core-concepts` — a hub page whose own prose is one
paragraph, followed by a card grid.

What the page states in its own words: the SDK "allows you to build social features into your game,
including friend lists, messaging, voice chat, and rich presence. Unlike a traditional SDK with
built-in UI components, the Discord Social SDK provides access to raw data, allowing developers to
create a fully customized experience that aligns with their game's aesthetic."

That last sentence is the load-bearing one: **there are no drop-in UI components.** Every surface is
yours to build, which is why the design guidelines exist and why they are requirements rather than
decoration.

### Core Concepts Overview

The page's own words: "Select a topic below to learn more about the Discord Social SDK."

| Card | Points at | In this skill |
| --- | --- | --- |
| **Core Features** | `/discord-social-sdk/core-concepts/core-features` | CORE-CONCEPTS.md |
| **Communication Features** | `/discord-social-sdk/core-concepts/communication-features` | CORE-CONCEPTS.md |
| **Integration Overview** | `/discord-social-sdk/core-concepts/integration-overview` | CORE-CONCEPTS.md |
| **Platform Compatibility** | `/discord-social-sdk/core-concepts/platform-compatibility` | CORE-CONCEPTS.md |
| **OAuth2 Scopes** | `/discord-social-sdk/core-concepts/oauth2-scopes` | CORE-CONCEPTS.md |

Three further core-concept pages exist that this grid does not link — `mobile`,
`release-cadence-and-support` and the SDK's own overview — and all three are covered in
CORE-CONCEPTS.md as well, so the skill carries eight core-concept pages against the grid's five.

### Next Steps

The page's own words: "After exploring these core concepts, you can start implementing the Discord
Social SDK in your game:" followed by links into the getting-started guides.

## How To Guides index

Source: `/discord-social-sdk/how-to`.

**These how-to guides offer common solutions for integrating Discord Social SDK features into your
game.** All seven cards, with upstream's own one-line description:

| Card | Description | In this skill |
| --- | --- | --- |
| **Debug & Log** (`/how-to/debug-log`) | "Use logging and debugging tools to troubleshoot issues." | HOW-TO-GUIDES.md |
| **Use with Discord APIs** (`/how-to/use-with-discord-apis`) | "Make requests to Discord's HTTP APIs from your game." | HOW-TO-GUIDES.md |
| **Integrate Moderation** (`/how-to/integrate-moderation`) | "Integrating and managing content moderation for your game when using the Discord Social SDK." | HOW-TO-GUIDES.md |
| **Market Your Integration** (`/how-to/market-your-integration`) | "Guidelines and best practices for announcing your Discord Social SDK integration to players." | HOW-TO-GUIDES.md |
| **Handle Special Characters in Display Names** (`/how-to/handle-special-characters-display-names`) | "Handling Unicode characters in Discord Display Names for your game's chat and friend lists." | HOW-TO-GUIDES.md |
| **Voice Muting Based on Player Blocks** (`/how-to/voice-muting-for-blocked-players`) | "Apply voice muting in lobbies based on Discord block relationships or external platform signals." | VOICE-CHAT.md |
| **Handle Rate Limits** (`/how-to/handle-rate-limits`) | "Detect and handle rate limit errors using ClientResult." | HOW-TO-GUIDES.md |

---

## Change logs

**Overview:** the page carries no change log.

**Getting Started index:** the page carries no change log.

**How To Guides index:**

| Date          | Changes               |
| ------------- | --------------------- |
| July 23, 2025 | migrated several docs |
| June 17, 2025 | added How To category |
