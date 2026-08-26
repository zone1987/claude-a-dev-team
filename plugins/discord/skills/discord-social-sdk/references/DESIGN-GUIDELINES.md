# Discord Social SDK — Design Guidelines

Distilled from all 13 pages under
`docs.discord.com/developers/discord-social-sdk/design-guidelines/`, retrieved 2026-08-26.

These pages are **UX/UI guidance with mock imagery**; almost every section is illustrated by a
screenshot that carries no additional stated text. Image captions are preserved as
`[Image: ...]` markers so a reader knows a visual exists upstream. Where a page states only guidance
and points at a development guide, that is noted.

## Contents

- [Principles](#principles)
- [Branding Guidelines](#branding-guidelines)
- [Connection Points](#connection-points)
- [Designing for Account Linking (Signing in)](#designing-for-account-linking-signing-in)
- [Provisional Accounts](#provisional-accounts)
- [Social Settings](#social-settings)
- [Unified Friends List](#unified-friends-list)
- [Game Friends](#game-friends)
- [User Status & Rich Presence](#user-status--rich-presence)
- [Direct Messages](#direct-messages)
- [Chat History](#chat-history)
- [Linked Channels](#linked-channels)
- [Consoles](#consoles)
- [Change logs](#change-logs)

**Standing note on all these pages:** "Any in-game imagery used in is purely fictional for concept
purposes." (Upstream's wording, on the Principles, Signing in and Game Friends pages.)

---

## Principles

Source: `/design-guidelines/principles`. Five core design principles.

### 1. Add Value for the Player

This integration aims to bring value to the player's gaming experience. **Branded connection points
should highlight said value-add based on the context.** [Image: Add Value for the Player]

### 2. Foster trust with Discord's brand

**Lean into Discord's visual-styling to establish trust through brand recognition.** The more players
that connect, the more robust the social graph is for the game. [Image: Foster trust with Discord's
brand]

### 3. Promote Understanding through consistency

**Use consistent branding and user-flows across games to build expected behavior. We care about the UX,
not the UI.** [Image: Promote Understanding through consistency]

### 4. Prioritize the player's immersion

The focus is on preserving the player's immersion in the game. **There are no requirements to replicate
Discord's UI.** The visual design should feel as seamlessly integrated into the game as the SDKs.
[Image: Prioritize the player's immersion]

### 5. Uphold data privacy, transparency, and control

**Each platform is in control and responsible for the data on their respective platforms. Players are
informed of where their data shows up.** [Image: Uphold data privacy, transparency, and control]

---

## Branding Guidelines

Source: `/design-guidelines/branding-guidelines`.

### Discord Logo

Download the Discord word-mark assets at `https://discord.com/branding`.

**Please do not edit, change, distort, recolor, or reconfigure the Discord logo.** [Image: Discord Logo]

### Buttons

**There are four sets of button styles for this integration: Blurple, Light, Dark, and Flexible.**

- **Flexible** — intended to be **restyled to match the game's aesthetic**. Flexible buttons include the
  font of the text before the logo as well as the button colors. **The Discord logo and its colors
  should not be altered.** This set is for **in-game connection points**.
- **Blurple / Light / Dark** — pre-styled buttons leveraging **colors vetted by Discord's Design Systems
  team to pass contrast ratios across different backgrounds**.

[Image: Brand Buttons]

### Spacing

**Ensure that there is adequate spacing between button text and the Discord logo as well as the
left/right edges of the button.**

**When using the Flexible button styling, ensure that your typeface's baseline and x-height are aligned
to the Discord logo.** [Image: Brand Spacing]

### Resources

- Discord branding guidelines: `https://discord.com/branding`

---

## Connection Points

Source: `/design-guidelines/connection-points`.

**Connection points are crucial touchpoints where players can login to Discord**, enhancing their
overall gaming experience.

### Signing in

**If the game has account management, then this connection point is required, otherwise it is not.**

**Discord's sign-in button is presented as the primary option to log in for the player** amongst the list
of **external identity-providers**, due to providing deeper user-benefits than a standard OAuth login.

**Use the Blurple Button styling for the sign-in connection point.** [Image: Signing In]

### Friends list

**If the player has not connected their Discord account yet, they will see a persistent call-to-action in
their friend's list until they connect.**

Select your preferred *button styling* for the friends list connection point (see
[Branding Guidelines](#buttons)).

**After the player connects their account, the connection point is no longer visible.** [Image: Friends
List]

### Content Guidelines

**Please use the strings shown here within the relevant contexts.** (The strings themselves are inside
the image upstream and are not stated in text.)

**These connection point strings should be consistent across all games that use the Discord Social SDK**
to help the user build recognition, trust, and understanding when taking this action. [Image: Content
Guidelines]

---

## Designing for Account Linking (Signing in)

Source: `/design-guidelines/signing-in`.

### Overall flow

**Sign-in or log-in flows all begin with the interaction of a Discord-styled button** (see
[Branding Guidelines](#buttons)).

**The Discord Social SDK supports the user journeys for those who already have a Discord account and
those who do not.** It similarly supports those who have Discord installed as well as those who do not
(via browser).

**A player can also proceed without connecting their Discord and continue onwards to playing their
game.** [Image: Overall Flow] [Image: Connecting your Discord account via Browser]

### Overlay Authorization

**Discord's Overlay feature** (`https://support.discord.com/hc/en-us/articles/217659737-Game-Overlay-101`)
**can be used to enable authorization without ever leaving the game.** This is available for games that
support the feature. [Image: Overlay Authorization]

### Before the user connects

**Add a one-time user education modal**, based on feedback from developers and players.

**This modal should include some of the key value props that the Discord Social SDK provides. The modal
should be placed contextually in the game.**

**Suggested Moments:**

- Trigger upon game-start for first time after the Discord Social SDK integration is launched to players
- Show when player interacts with the friends list for the first time
- Show in the authorization flow once a player taps the Discord connection point

[Image: Before the user connects]

### After the user connects

**Add a success state in the game when the authorization completes** — styled in a way that fits the
game's aesthetic.

**Content — include the following points sequentially in the game's writing style. Remove any points that
cover features that the game does not utilize:**

- You successfully connected your Discord account
- You can chat with your friends here and on Discord
- It might take some time for your game friends to show up in your Discord

[Image: After the user connects]

### Error State

**The user will also need to be shown an error state if the authorization fails** — also styled in a way
that fits the game's aesthetic. **Include these key points sequentially in the game's writing style:**

- We were unable to connect your Discord account
- A call-to-action that redirects back to Discord with the initial authorization modal

[Image: Error State]

### Resources

- Development Guide: Account Linking with Discord — see ACCOUNT-LINKING.md.

---

## Provisional Accounts

Source: `/design-guidelines/provisional-accounts`.

### For those who don't connect a Discord account

**Not all users are going to link their Discord account to their game. This creates the potential burden
of having to maintain two different friend systems for each account type.**

The Discord Social SDK has built provisional accounts as a way for game devs to create a lightweight,
**limited Discord account** for unlinked users, **so you can use the same APIs regardless of whether a
user has connected their Discord account or not.** [Image: Badge when online elsewhere]

### What is a provisional account?

**To players, a provisional account is simply a standard account that has yet to be linked to Discord.**
They have access to standard communication features you'd expect any game user to have.

**The complexity around provisional accounts that game developers have to handle are invisible to players
in the game.** [Image: What is a provisional account?]

### How provisional accounts look within the game

**Provisional accounts won't have the Discord badge by their username** in the friends list and other
contexts where their username may appear, because they have not connected their Discord account.

**Only players who've connected their Discord accounts and have provisional account friends from other
games using the Discord Social SDK will see this state.** [Image: How provisional accounts look within
the game]

### How provisional accounts look within Discord

**Provisional accounts will leverage branded avatars and text hints on Discord to differentiate them from
standard Discord users.**

**Because provisional accounts have limited capabilities — for example, you cannot start a voice or video
call with them — it's important to visually distinguish them from Discord users.** [Image: How
provisional accounts look within Discord]

### Resources

- Development Guide: Using Provisional Accounts — see PROVISIONAL-ACCOUNTS.md.

---

## Social Settings

Source: `/design-guidelines/social-settings`.

### Evolving with users

Discord is listening to feedback and releasing settings for players to tailor their social experience.
**These settings will continue to change and evolve with the SDK and Discord client.**

**Discord Social SDK settings are global, meaning they will impact all games that use the Discord Social
SDK. These settings live in the Discord client.** [Image: Evolving with users]

### Main entrypoint

**An entrypoint is required in games to send players to the relevant Discord client settings page** (see
MESSAGING.md → In-Game Direct Message Settings, i.e. `Client::OpenConnectedGamesSettingsInDiscord`).
**Only players who have their Discord account connected should see this.**

**Exactly like the auth flow, players will be redirected to the Discord client to manage their social
settings. If they do not have the client, the browser will be the fallback.** [Image: Main entrypoint]

### Content guidelines

**The official settings title for players is "Discord Social Experience." Use this language when
referring to Social SDK settings to players.**

**The description is optional**, but if your game settings has the space, Discord recommends describing
what users should expect to find when they navigate to Discord. [Image: Content guidelines]

### Resources

- Development Guide: Direct Messages — see MESSAGING.md.

---

## Unified Friends List

Source: `/design-guidelines/unified-friends-list`.

This guide teaches you how to:

- Implement **sectioning** to organize friends by availability and game status.
- Display the **Discord badge** to indicate universal communication capabilities.
- **Prioritize and display different identities** based on the player's relationship with the game and
  Discord.
- Ensure **consistency and familiarity in naming conventions** to reduce confusion.

### Figma File — The Social SDK: Friend List Starter Pack

Discord provides **a Figma resource with a templated design system for building out your game's friends
list**. Change various components to match your game's visual language and see it update in realtime. It
also includes a few common use cases, plus an example of one of Discord's partnered games, **SUPERVIVE**.

Link: `https://www.figma.com/community/file/1512487996808869592/the-social-sdk-friend-list-starter-pack`

Feedback goes to the Discord Developers Server (`https://discord.gg/discord-developers`), a post in the
`#social-sdk-dev-help` channel. [Image: starter pack]

### Sectioning

**Sections are ordered by descending availability to help users find friends they can play with.**

- The **Online — GameTitle** section shows friends who are **online in the same game and are compatible
  to play with**.
- The **Online — Elsewhere** section shows friends who are **online but not in the same game**. However,
  **they can be messaged or invited to play the game**.

[Image: Sectioning Friends List]

### Discord = Communication

**Show the Discord badge next to a player's name when they are online elsewhere AND have connected their
Discord account. Provisional accounts will not have a badge.**

**The Discord logo represents universal communication.** It aims to convey: "As a player, I know I can
message or invite this friend to play a game anywhere Discord is present." **This means via phone,
computer, and even console.** [Image: Discord logo represents universal communication]

### Identities

**Identity priority order:**

1. **If the friend owns the game, display their in-game identity (username).** Prioritize what users are
   already familiar with.
2. **If the friend does not own the game, use their Discord Display Name.**
3. **If the friend does not own the game nor have a linked Discord account, fall back to their
   Provisional identity.**

[Image: Displaying different relationships]

### Examples of friends lists

**A player's console ID is effectively their game ID, as consoles require this.** As such, it's likely the
set of names players will be most familiar with. [Image: Examples of friends lists]

### How did we land here?

**It reduces sudden name changes within the game**, which can be confusing to the player, and reduces
**erratic UI-width shifts**. It's also **scalable** and **inclusive of provisional accounts** who do not
have Discord accounts connected. [Image: How did we land here?]

### Discord Display Names

**When referring to a player's Discord Identity, use their Discord Display Name, and not their
username.**

See HOW-TO-GUIDES.md → Handle Special Characters in Display Names for guidance on handling special
characters in text chat and friend lists. [Image: Discord display names]

### Scaling to Multiple Platforms

**If your game uses more than one platform's friend graph, combine them into "Online Elsewhere."**

**Prioritize player needs by elevating available players to the top of the friends list, regardless of
platform.**

**Avoid friend lists organized by company. This hierarchy dilutes the value-prop of putting online
players first, in favor of platform delineation.** [Image: Scaling to Multiple Platforms]

### Resources

- Development Guide: Creating a Unified Friends List — see RELATIONSHIPS-AND-FRIENDS.md.
- Figma File — The Social SDK: Friend List Starter Pack (link above).

---

## Game Friends

Source: `/design-guidelines/game-friends`.

### User needs

Players want **more of a distinction between connections they make in-game, and friends they spend time
with on Discord** outside of and across games. "Someone I party up with may not necessarily be my
'friend'."

**Users want more controls over how in-game relationships extend beyond the game client with
communication, presence, and identity.** [Image: User needs]

### Game Friends — A new tier

Discord is introducing a new tier of friendship called **Game Friends**: a way to create an in-game
relationship with another player **that provides all of the in-game benefits, but limits how the
relationship extends outside the game**. [Image: Game Friends]

### Game vs Discord Friends

**Communication.** A Game Friend **can reach Discord-connected friends outside the game** by DMing those
in the game who are offline — **these messages will be received on the Discord client. Discord provides
players a setting to disable receiving DMs from Game Friends.**

**Presence.** A Game Friend **cannot see your rich presence beyond the game your friendship originated
in. The exception is if both friends have their Discord accounts connected and are in a shared server.**
[Image: Game vs Discord Friends]

### Equally-weighted

**When adding a new friend, present two options to players with "Game Friends" listed first**, since
it's the more localized/limited friend tier. **Ensure that neither type of friend is pre-selected in the
UI — present them equally to the user** (ordering aside for the above reason). [Image: Equally-weighted
friend options]

### Adding friends

- **If the user is not yet a friend, show both options** of adding as either a Game or Discord Friend.
- **If a user is already your Game Friend, show the action to also add them on Discord.**

[Image: Adding friends]

### Removing friends

**When removing a Game Friend or Discord Friend, show players the standard "Remove Friend" action. The
SDK will remove the friend across whatever friendships are applicable.** [Image: Removing friends]

### Style guidelines

(Upstream repeats the "Removing friends" paragraph verbatim under this heading:) **When removing a Game
Friend or Discord Friend, show players the standard "Remove Friend" action. The SDK will remove the
friend across whatever friendships are applicable.** [Image: Removing friends]

### UX, not UI

**The visual styling of the "Add Friend" menu items is not intended to be prescriptive. So long as both
options are equally weighted, use whichever UI fits your game's needs.** [Image: UX, not UI]

### Setting on Discord

This mock showcases how the corresponding DM looks within Discord's UI. (The page states nothing further
here.) [Image: Removing friends]

### Resources

- Development Guide: Managing Relationships — see RELATIONSHIPS-AND-FRIENDS.md.

---

## User Status & Rich Presence

Source: `/design-guidelines/status-rich-presence`.

This guide teaches you how to:

- Implement a **status matrix** to display player statuses in your friends list.
- Apply **core style guidelines** to ensure consistency and player comprehension.
- **Customize the appearance** to fit your game while maintaining the essential elements of status
  indicators.

### Core statuses, plus game-specific

[Image: Core statuses, plus game-specific] — the page states no additional text under this heading; the
status set itself is enumerated under "Side-by-side" and "Core style guidelines" below.

### Status matrix

[Image: Status matrix] — the matrix exists only as an image upstream; no text accompanies it.

### Side-by-side

**Any of the core statuses (online, idle, DND, offline) will always be the same between the game and the
Discord client.**

**You can customize the status icon, but custom icons will only render within the game.** [Image:
Side-by-side]

### Core style guidelines

**To ensure player comprehension, keep the core colors, symbols, and information architecture consistent
across Discord-powered games** — with choice of styling applied.

**In other words, as long as the status colors read as yellow/green/red, and the symbols as
moon/circle/minus/offline, all other styling is the game's choice.**

**Avatars are not required.** [Image: Core style guidelines]

### Rich Presence

**The game developer should set rich presence — this will show in both the Discord and game client.**

See RICH-PRESENCE.md for the other types of traits that can be included. [Image: Rich Presence]

### Resources

- Development Guide: Setting Rich Presence — see RICH-PRESENCE.md.

---

## Direct Messages

Source: `/design-guidelines/direct-messages`.

### Badge when online elsewhere

**The badging logic in direct messages is consistent with the logic detailed in the
[Unified Friends List](#unified-friends-list) section.**

**If the user is online elsewhere and is not in the game client, their usernames will include a Discord
badge. Once they're online in the game client, they will not retain the Discord badge.** [Image: Badge
when online elsewhere]

### Message styling

**Style the Discord logo to match a player's username color. The logo should feel tied to a user's
identity, not the message content.** [Image: Message styling]

### Unsupported rich media

**Regardless of whether a user has signed into Discord, unsupported rich media content should be paired
with an external link icon.**

**When content isn't clickable, don't show the icon.** [Image: Unsupported rich media]

### Resources

- Development Guide: Direct Messages — see MESSAGING.md.

---

## Chat History

Source: `/design-guidelines/chat-history`.

### Style recommendations

**Chat history is a highly requested optional feature** that helps players pick up conversations where
they left off — whether they're returning to a lobby or jumping back into a linked channel.

**Discord recommends showing timestamps** to give players better context about when messages were sent
and seen. [Image: Badge when online elsewhere] (upstream reuses that caption here)

### Display logic

**If one player is messaging from a game lobby or linked channel, then chat history is preserved, even if
the other player is messaging from Discord.**

**When players return to a lobby or open a linked channel, Discord recommends surfacing 10 to 15 of the
most recent messages to provide meaningful context. This isn't a hard limit** — older messages can be
revealed through scroll or loading more content, depending on your UI constraints. [Image: Message
styling]

(For the API-side limits — 25 messages cached in memory, up to 200 messages and 72 hours retrievable —
see MESSAGING.md and LOBBIES.md.)

### Resources

- Development Guide: Creating and Managing Lobbies — see LOBBIES.md.

---

## Linked Channels

Source: `/design-guidelines/linked-channels`.

### Link in-game chats to Discord

**Empower players to continue their conversations beyond the game.** You can link an in-game chat to a
text channel on Discord. [Image: Linking a channel via the game]

### Style guidelines

**Feature Name & Language.** **The official feature name that will be reflected across the Discord client
is "Linked Channels."** Use the following language when referring to this feature to promote player
comprehension across clients:

- "Linked to {Discord/GameTitle}"
- "Link a {groupChat} to Discord"
- "Edit/Remove Channel Link"

**Entrypoints.** Use the string guidance above: **"Link {groupChat} to Discord."** For interface, use
whichever UI treatment fits your game's needs. [Image: Linked channel style guidelines]

### Selecting a channel

**Players require a channel-selection flow where they can pick a text channel to link their game chat
with. Only one text channel can be linked at a time. Furthermore, the player must have the permissions
to manage the channel.**

**Include the following in the selection UI:**

- **Description of what a channel link does and who can read and write to the channel** after
  establishing the link
- **List of servers and their nested text channels with respective iconography** (i.e. a private channel
  has a lock)
- **Search bar for channel names**

[Image: Selecting a channel]

### Setup warning

**Players can link channels with limited access on Discord. Doing so will allow players from their game
chat to also read and send messages to this channel, regardless of whether or not they have permissions
on Discord. In short, linking a game channel will bypass that channel's existing permissions on
Discord.**

**Show a warning when a user is about to link to a channel with limited access.** Discord strongly
recommends using the copy shown in the upstream image. [Image: Setup warning]

### Success state & Entrypoint

**Once the channel link is established, show a success state to the user detailing which text channel
they've linked to on Discord.**

**Separately, create a persistent entrypoint somewhere in the game UI. This persistent entrypoint should
also show details such as the Discord server and channel name. It will also serve as the entrypoint for
managing the linked channel.**

**The official "Linked Channels" channel icon can be downloaded from Discord's GitHub repository:**
`https://github.com/discord/discord-api-docs/blob/main/resources/discord-social-sdk`. [Image: Success
state & Entrypoint]

### Removing Channel Link

**Players can navigate to the relevant channel settings on Discord from the "Edit settings" menu item.
Pair it with an "open in new window" icon.**

**Players can remove the channel link from either the game client or the Discord client.**

**When "Remove channel-link" is interacted with, show the player a confirmation dialog to confirm this
action.** [Image: Removing Channel Link]

### Resources

- Development Guide: Linked Channels — see MESSAGING.md.
- Design Assets: Linked Channel Icon —
  `https://github.com/discord/discord-api-docs/blob/main/resources/discord-social-sdk`.

---

## Consoles

Source: `/design-guidelines/consoles`.

**To use the Discord Social SDK in your console games, you will need to request middleware approval and
be an approved developer for the target console**
(`https://support-dev.discord.com/hc/en-us/articles/30209074764183`).

**Warning — Exception: Prohibited Off-Platform Interactions by Sony.** For integrations experienced on
Sony Platforms (e.g. PlayStation 5):

1. **Do not allow access to Account Linking** entry points.
2. **Do not allow access to Linked Channels**.
3. **Limit messaging and Invites to other players currently playing** the game.
4. **Do not display off-platform presence and logos** (including Discord).

**Players expect a consistent Discord social experience across devices** — whether on PC, mobile, or
console. While the console experience largely mirrors other devices, the following highlight adjustments
tailored to console navigation.

**Console players will need a secondary device to experience the full benefits of the Discord Social
SDK.** [Image: Connect on console]

### Connect to Discord on console

**The overall connection flow remains the same on console as other devices.** After clicking an in-game
CTA to connect to Discord, a screen with sign in options appears.

**Users will need to use a mobile device or computer in order to avoid the clunky experience of signing in
on a web browser using a controller.**

**A player without an existing Discord account can create one easily on the web.** [Image: Connect on
console]

**Users can skip the device code screen by scanning the QR code with their mobile camera. They will be
prompted to authorize the game. If the Discord app is not detected upon scanning, users are prompted to
sign in and connect via the web browser.**

**If a player does not wish to use the QR scan, they will need to go to `discord.com/activate` to enter
the 8-digit code.** [Image: connecting with your phone]

### Chatting on console

**Game chat will be available for games who support the feature on consoles. However, unsupported rich
media from Discord (i.e. attachments, polls, voice messages, etc.) should not include a clickable link
icon.** Similar to the auth flow, **Discord does not want to encourage players to visit Discord in the
console web browser — they should use secondary devices to view this content.** [Image: chat on console]

### Friends list on console

**Leverage the same friends list guidelines** documented in [Unified Friends List](#unified-friends-list).
**There are no notable differences in the friends list on console in comparison to other devices.
However, consoles do not support hover interactions, so there needs to be a console-friendly way for
players to access secondary information (such as alternate identities) about friends in the list.**
[Image: chat on console]

### Resources

- Development Guide: Account Linking on Consoles — see ACCOUNT-LINKING.md.

---

## Change logs

**Principles:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | initial release |

**Branding Guidelines:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | Initial Release |

**Connection Points:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | initial release |

**Designing for Account Linking (Signing in):**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | initial release |

**Provisional Accounts:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | initial release |

**Social Settings:**

| Date         | Changes         |
| ------------ | --------------- |
| May 08, 2025 | Initial Release |

**Unified Friends List:**

| Date           | Changes                      |
| -------------- | ---------------------------- |
| June 25, 2025  | Added Figma UFL starter pack |
| March 17, 2025 | initial release              |

**Game Friends:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | initial release |

**User Status & Rich Presence:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | Initial Release |

**Direct Messages:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | initial release |

**Chat History:**

| Date          | Changes         |
| ------------- | --------------- |
| July 02, 2025 | initial release |

**Linked Channels:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | initial release |

**Consoles:**

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | initial release |
