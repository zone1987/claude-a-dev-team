# Discord Guide Indexes

Complete extraction of the seven `guides*` index pages plus `game-development/how-to-grow-your-game`,
retrieved 2026-08-26.

**Six of these eight pages are navigational hubs**: their body is a set of cards, so what they carry is
the link graph plus each card's own one-line blurb. Both are recorded below verbatim. The one page with
real prose is `game-development/how-to-grow-your-game`, extracted in full at the end.

## Contents

- [guides — Discord Development Guide Library](#guides--discord-development-guide-library)
- [guides/bots — Discord Bot Development Guides](#guidesbots--discord-bot-development-guides)
- [guides/activities — Discord Activity Development Guides](#guidesactivities--discord-activity-development-guides)
- [guides/social-sdk — Discord Social SDK Guides](#guidessocial-sdk--discord-social-sdk-guides)
- [guides/platform — Platform Feature Guides](#guidesplatform--platform-feature-guides)
- [guides/communities — Community Management Guides](#guidescommunities--community-management-guides)
- [guides/game-development — Game Development Guides](#guidesgame-development--game-development-guides)
- [game-development/how-to-grow-your-game — How Can I Grow My Game?](#game-developmenthow-to-grow-your-game--how-can-i-grow-my-game)
- [The complete guide link graph](#the-complete-guide-link-graph)

## guides — Discord Development Guide Library

*Page tagline: "Guides to help you get started on your development journey with Discord."*

**A pure hub: six cards in three sections, no prose of its own.**

### Building on Discord

| Card | Target | Blurb |
| --- | --- | --- |
| **Bot Development** | `guides/bots` | Guides for developing bots on Discord. |
| **Discord Activities** | `guides/activities` | Guides for developing embedded games and experiences on Discord. |
| **Integrating the Social SDK** | `guides/social-sdk` | Guides for integrating games with the Discord Social SDK. |
| **Using Platform Features** | `guides/platform` | Guides for using Discord's features across your game, app, and server experience. |

### Community & Servers

| Card | Target | Blurb |
| --- | --- | --- |
| **Community Management** | `guides/communities` | Guides for managing your Discord community and server effectively. |

### Building Games

| Card | Target | Blurb |
| --- | --- | --- |
| **Game Development** | `guides/game-development` | Guides for building games and game development communities on Discord. |

## guides/bots — Discord Bot Development Guides

*Page tagline: "Guides for developing bots on Discord."*

**A hub.** Its only prose is a `Note`: *Visit Bots & Companion Apps (`bots/overview`) for more on
building bots and companion apps on Discord, including how to get started, best practices, and more.*

### Getting Started

| Card | Target | Blurb |
| --- | --- | --- |
| **Build your first Discord bot** | `quick-start/getting-started` | A step-by-step guide to building your first bot on Discord. |

### Diving Deeper

| Card | Target | Blurb |
| --- | --- | --- |
| **Using Message Components** | `components/using-message-components` | A guide to using message components in your Discord bot. |
| **Using Modal Components** | `components/using-modal-components` | A guide to using modal components in your Discord bot. |
| **Using Community Invites** | `tutorials/using-community-invites` | A guide to using community invites in your Discord bot. |
| **Developing A User-Installable App** | `tutorials/developing-a-user-installable-app` | A guide to developing a user-installable app on Discord. |
| **Hosting on Cloudflare Workers** | `tutorials/hosting-on-cloudflare-workers` | A guide to hosting your Discord bot on Cloudflare Workers. |
| **You Might Not Need a Privileged Intent** | `gateway/you-might-not-need-a-privileged-intent` | A guide to help you determine whether you need a privileged intent or whether an alternative approach will work. |

### Privileged Intents

| Card | Target | Blurb |
| --- | --- | --- |
| **You Might Not Need a Privileged Intent** | `gateway/you-might-not-need-a-privileged-intent` | A guide to help you determine whether you need a privileged intent or whether an alternative approach will work. |
| **Getting Started With Privileged Intent Review** | `gateway/getting-started-with-privileged-intent-review` | A guide to help you get started with the privileged intent review process. |

Note the duplication is upstream's own: **"You Might Not Need a Privileged Intent" appears in both the
Diving Deeper and Privileged Intents sections** of this page.

## guides/activities — Discord Activity Development Guides

*Page tagline: "Guides for developing embedded games and experiences on Discord."*

**A hub.** Its only prose is a `Note`: *Visit Activities (`activities/overview`) for more on building
embedded games and experiences on Discord, including how to get started, best practices, and more.*

### Getting Started

| Card | Target | Blurb |
| --- | --- | --- |
| **Build your first Activity** | `activities/building-an-activity` | A step-by-step guide to building your first Activity on Discord. |

### Diving Deeper

| Card | Target | Blurb |
| --- | --- | --- |
| **Setting Rich Presence** | `rich-presence/using-with-the-embedded-app-sdk` | Learn how to set up Rich Presence for your Activity to display game status and join features. |
| **Implementing IAP for Activities** | `monetization/implementing-iap-for-activities` | A guide to implementing in-app purchases for your Discord Activities. |

### Best Practices

| Card | Target | Blurb |
| --- | --- | --- |
| **Design Patterns for Activities** | `activities/design-patterns` | Best practices and design patterns for creating engaging Activities on Discord. |

## guides/social-sdk — Discord Social SDK Guides

*Page title: "Discord Social SDK Guides."*

**A hub.** Its only prose is a `Note`: *Visit Discord Social SDK (`discord-social-sdk/overview`) for
more on integrating games with the Discord Social SDK, including how to get started, best practices,
and more.*

### Getting Started

| Card | Target | Blurb |
| --- | --- | --- |
| **Getting Started with the Social SDK** | `discord-social-sdk/getting-started` | A guide to integrating your game with the Discord Social SDK. |

### Guides — the nine development guides

| Card | Target | Blurb |
| --- | --- | --- |
| **Account Linking with Discord** | `discord-social-sdk/development-guides/account-linking-with-discord` | Learn how to authenticate users with their Discord accounts using OAuth2. |
| **Creating a Unified Friends List** | `discord-social-sdk/development-guides/creating-a-unified-friends-list` | Combine Discord and game-specific friends in one view. |
| **Setting Rich Presence** | `discord-social-sdk/development-guides/setting-rich-presence` | Display detailed game status in Discord profiles. |
| **Managing Game Invites** | `discord-social-sdk/development-guides/managing-game-invites` | Allow players to invite friends to join their game session or party. |
| **Sending Direct Messages** | `discord-social-sdk/development-guides/sending-direct-messages` | Enable private messaging between players. |
| **Managing Lobbies** | `discord-social-sdk/development-guides/managing-lobbies` | Bring players together in a shared lobby with invites, text chat, and voice comms. |
| **Linked Channels** | `discord-social-sdk/development-guides/linked-channels` | Connect game lobbies to Discord text channels. |
| **Managing Voice Chat** | `discord-social-sdk/development-guides/managing-voice-chat` | Add in-game voice communication. |
| **Using Provisional Accounts** | `discord-social-sdk/development-guides/provisional-accounts/overview` | Give your users a seamless account experience with provisional accounts. |

### Game Development Guides

| Card | Target | Blurb |
| --- | --- | --- |
| **How Do I Get My Game Seen?** | `game-development/how-to-get-your-game-seen` | Implement Rich Presence with game details, lobby joining, game launching, and store links using the Social SDK |
| **How Do I Add Proximity Voice Chat to My Game?** | `game-development/how-to-add-proximity-voice-chat-to-your-game` | Learn how to use the Social SDK's voice chat with Unity's 3D audio system to build proximity voice chat for a multiplayer game. |

## guides/platform — Platform Feature Guides

*Page tagline: "Guides for using Discord's features across your game, app, and server experience."*

**The thinnest hub of the eight: two cards, two sections, one card each, and no prose at all.**

### Account Linking

| Card | Target | Blurb |
| --- | --- | --- |
| **What is Account Linking?** | `platform/account-linking` | An introduction to account linking and its benefits for your game or app. |

### Rich Presence

| Card | Target | Blurb |
| --- | --- | --- |
| **Rich Presence Best Practices** | `rich-presence/best-practices` | Best practices for using Rich Presence to create engaging game integrations on Discord. |

## guides/communities — Community Management Guides

*Page title: "Community Management Guides."*

**A hub: two cards, no sections, no prose.**

| Card | Target | Blurb |
| --- | --- | --- |
| **How Do I Create a Community For My Game?** | `game-development/how-to-create-a-community-for-your-game` | Creating a community for your game involves establishing a Discord server to foster direct communication with players, gather feedback, and keep engagement alive between updates. |
| **Community Invites for Community Managers** | `communities/guides/community-invites` | Learn how to create and manage community invites to grow your community. |

## guides/game-development — Game Development Guides

*Page title: "Game Development Guides."*

**A hub: five cards in two sections, no prose.**

### Strategy

| Card | Target | Blurb |
| --- | --- | --- |
| **How Can I Grow My Game?** | `game-development/how-to-grow-your-game` | Learn how to use Discord to grow your game, build a community, and keep players playing! |

### Guides

| Card | Target | Blurb |
| --- | --- | --- |
| **How Do I Create a Community For My Game?** | `game-development/how-to-create-a-community-for-your-game` | Set up a community server, design roles and channels, and bring players in from your game. |
| **How Do I Get My Game Seen?** | `game-development/how-to-get-your-game-seen` | Use Discord's features to get your game seen by more players and grow your community. Implement Rich Presence with game details, lobby joining, game launching, and store links. |
| **How Do I Keep My Players Engaged?** | `game-development/how-to-keep-your-players-engaged` | Build a bot connected to your game with leaderboards, event announcements, and achievement sharing. |
| **How Do I Add Proximity Voice Chat to My Game?** | `game-development/how-to-add-proximity-voice-chat-to-your-game` | Learn how to use the Discord Social SDK's voice chat with Unity's 3D audio system to build proximity voice chat for a multiplayer game. |

## game-development/how-to-grow-your-game — How Can I Grow My Game?

*The one substantive page in this group.* Hero image caption: "A banner showing players chatting about
playing a game together."

**Building and publishing a game is hard. Getting players to discover, share, and play it is even
harder.** With dozens of incredibly strong games released each day, some with huge marketing budgets,
**it's harder than ever to build a player base and keep it strong**. That doesn't mean it's impossible,
and **Discord has a set of tools to help you**.

### Why Discord? — every statistic upstream states

All figures are marked by upstream with an asterisk footnoted as ***Discord Internal Data, 2025***.

| Statistic | Upstream's framing |
| --- | --- |
| **Over 90 million daily active users** | Discord's scale. |
| **Over 90% of Discord users play video games** | Discord is already where massive communities of gamers connect **across desktop, console, and mobile**. Take advantage of those connections to drive **deeper player engagement, longer gaming sessions, and organic growth** for your game. |
| **66% of Discord users play games with friends weekly** | Discord users **share the games they play with their friends**. **Your players are your biggest cheerleaders — make it easy for them to share what they're playing.** |
| **Discord PC players played a median of 6 times longer if they were playing with at least one friend on Discord, vs playing alone** | **Creating social experiences that players can share with their friends keeps games fresh for longer.** |
| **Over 9,000 official game communities are on Discord, with over 80 million members** | Discord is a leading platform for hosting official game communities. |

**A social game doesn't necessarily have to be a multiplayer experience.** Upstream's two examples:
**daily puzzle games that allow score sharing**, and **roguelikes that have daily runs and
leaderboards**. **Both offer unique opportunities for community engagement and friendly rivalries.**

**Using Discord as part of your game development strategy can help build community, grow your game, and
keep players playing.**

### Build a Community to Capture Your Players

**Whether you're just starting on a new game or you've already got a beta up and running, it's never too
early to think about community.**

**Players who join your game's Discord community can develop a sense of belonging and connection with
your game that goes beyond just playing.** They **become invested in your game's success, provide
valuable feedback, and naturally bring new players into the community**. It also gives you a chance to
**interact directly with your players, get to know them better, provide feature updates and bug fixes,
and learn why they love your game**. **A thriving community with active developers gives players a
reason to stick around between updates and creates lasting relationships that keep your game alive.**

Card: **How Do I Create a Community For My Game?**
(`game-development/how-to-create-a-community-for-your-game`) — "Set up a community server, design roles
and channels, and bring players in from your game".

### Get Your Game Seen With Rich Presence

**Have you ever seen what a friend is playing in the Discord client? This is called Rich Presence** and
there are **so many ways to use it to get your game seen**.

**The Discord Social SDK** (`https://discord.com/developers/social-sdk`) **allows you to control how
Rich Presence is displayed to your players in Discord by adding text, images, links, buttons, and
more.** **You can even add invites that allow players to join your game directly from Discord.**

**With Rich Presence, your player's profiles become organic marketing for your game** and give you a
seamless way to create social experiences. **The easier you make it for players to show off what they're
playing, the faster your game will naturally spread through their social graph.**

Card: **How Do I Get My Game Seen?** (`game-development/how-to-get-your-game-seen`) — "Implement Rich
Presence with game details, lobby joining, game launching, and store links".

### Keeping Your Players Engaged

**A Discord bot or companion app keeps your game present in players' lives even when they're not
actively playing.** You can use them to:

- **bring your game's world into Discord**,
- **announce in-game events**,
- **share achievements and leaderboards**, and
- **run giveaways or promos**.

**This keeps your game top-of-mind in Discord and gives players a reason to jump back in.**

Upstream cites a **case study from Sabotage Studio** (`https://discord.com/developer-case-studies/sabotage`)
— "Read more to learn about how they used community and bots to fill the gap between game updates."

**Bots and companion apps can extend your game's experience into Discord, creating engagement loops that
bring players back.**

- **A guild-installable bot can live in your community server.**
- **User-installable bots allow players to use them anywhere for optimal sharing.**

**A well-built bot helps players organically share your game and community.** **Players sharing their
high scores, leaderboards, builds, and achievements through your bot can drive their friends to return
to the game just to beat them, or even purchase the game to join in the competition.** Upstream's
summary: **"It's re-engagement and community building that works for you around the clock."**

Card: **How Do I Keep My Players Engaged?** (`game-development/how-to-keep-your-players-engaged`) —
"Build a bot connected to your game with leaderboards, event announcements, and achievement sharing".

### Which Strategy Should You Start With?

**You don't need to implement everything here at once. Pick a strategy that matches your current
development state and player base, then build from there.**

| Your stage | Start with | Upstream's reasoning |
| --- | --- | --- |
| **Pre-launch or early development** | **"How Do I Create a Community For My Game?"** | **Create a home for your early testers and first players to join.** A community built during development **gives you valuable feedback and creates a core group of invested players who will champion your game at launch**. |
| **Existing game** | **"How Can I Get My Game Seen?"** | **Rich Presence and the Social SDK make it easy for players to see what their friends are playing and buy the game or join them right from Discord.** This helps **create organic growth through friend groups**. |
| **Live game with an existing community** | **"How Do I Keep My Players Engaged?"** | **Build a bot that bridges your game and Discord.** Think about **what information from your game could be the most helpful thing for players to share**. It can **celebrate achievements, announce events, and build competition through leaderboards**. This **strengthens the connection between your community and your game**. |

The page closes with the same three cards as the table rows above: **How Do I Create a Community For My
Game?**, **How Do I Get My Game Seen?**, **How Do I Keep My Players Engaged?**

## The complete guide link graph

Every distinct target the eight pages in this file link to, with which index pages reach it. Targets
outside this skill's page set are named so a reader knows the guide exists; the sibling skills that
cover them are listed in the skill map.

| Target | Reached from |
| --- | --- |
| `guides/bots` | `guides` |
| `guides/activities` | `guides` |
| `guides/social-sdk` | `guides` |
| `guides/platform` | `guides` |
| `guides/communities` | `guides` |
| `guides/game-development` | `guides` |
| `bots/overview` | `guides/bots` |
| `quick-start/getting-started` | `guides/bots` |
| `components/using-message-components` | `guides/bots` |
| `components/using-modal-components` | `guides/bots` |
| `tutorials/using-community-invites` | `guides/bots` |
| `tutorials/developing-a-user-installable-app` | `guides/bots` |
| `tutorials/hosting-on-cloudflare-workers` | `guides/bots` |
| `gateway/you-might-not-need-a-privileged-intent` | `guides/bots` (twice) |
| `gateway/getting-started-with-privileged-intent-review` | `guides/bots` |
| `activities/overview` | `guides/activities` |
| `activities/building-an-activity` | `guides/activities` |
| `activities/design-patterns` | `guides/activities` |
| `rich-presence/using-with-the-embedded-app-sdk` | `guides/activities` |
| `monetization/implementing-iap-for-activities` | `guides/activities` |
| `discord-social-sdk/overview` | `guides/social-sdk` |
| `discord-social-sdk/getting-started` | `guides/social-sdk` |
| the nine `discord-social-sdk/development-guides/*` guides | `guides/social-sdk` |
| `platform/account-linking` | `guides/platform` |
| `rich-presence/best-practices` | `guides/platform` |
| `communities/guides/community-invites` | `guides/communities` |
| `game-development/how-to-create-a-community-for-your-game` | `guides/communities`, `guides/game-development`, `how-to-grow-your-game` |
| `game-development/how-to-grow-your-game` | `guides/game-development` |
| `game-development/how-to-get-your-game-seen` | `guides/game-development`, `guides/social-sdk`, `how-to-grow-your-game` |
| `game-development/how-to-keep-your-players-engaged` | `guides/game-development`, `how-to-grow-your-game` |
| `game-development/how-to-add-proximity-voice-chat-to-your-game` | `guides/game-development`, `guides/social-sdk` |

## Source

Discord Developer Documentation, retrieved 2026-08-26:
`https://docs.discord.com/developers/guides`,
`https://docs.discord.com/developers/guides/bots`,
`https://docs.discord.com/developers/guides/activities`,
`https://docs.discord.com/developers/guides/social-sdk`,
`https://docs.discord.com/developers/guides/platform`,
`https://docs.discord.com/developers/guides/communities`,
`https://docs.discord.com/developers/guides/game-development`,
`https://docs.discord.com/developers/game-development/how-to-grow-your-game`.
