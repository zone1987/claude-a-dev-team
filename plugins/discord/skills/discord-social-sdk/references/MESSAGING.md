# Messaging: Direct Messages and Linked Channels

Distilled from two Discord Social SDK development guides:

- [Sending Direct Messages](https://docs.discord.com/developers/discord-social-sdk/development-guides/sending-direct-messages) — change log last entry August 29, 2025
- [Linked Channels](https://docs.discord.com/developers/discord-social-sdk/development-guides/linked-channels) — change log last entry June 30, 2025

Read from a local mirror on 2026-08-26.

## Contents

- [Sending Direct Messages](#sending-direct-messages)
  - [Rate limits and scopes](#rate-limits-and-scopes)
  - [Types of chat messages and channel types](#types-of-chat-messages-and-channel-types)
  - [Sending a direct message to a user](#sending-a-direct-message-to-a-user)
  - [Syncing messages with Discord](#syncing-messages-with-discord)
  - [Receiving and rendering messages](#receiving-and-rendering-messages)
  - [Suppressing double notifications](#suppressing-double-notifications)
  - [Legal disclosure message type](#legal-disclosure-message-type)
  - [Message history in memory](#message-history-in-memory)
  - [Working with unrenderable content](#working-with-unrenderable-content)
  - [Getting direct message history](#getting-direct-message-history)
  - [In-game direct message settings](#in-game-direct-message-settings)
  - [Development rate limits](#development-rate-limits)
  - [Change log — sending direct messages](#change-log--sending-direct-messages)
- [Linked Channels](#linked-channels)
  - [Access status and scopes](#access-status-and-scopes)
  - [What linking does](#what-linking-does)
  - [Linked channel requirements](#linked-channel-requirements)
  - [Private channels](#private-channels)
  - [User requirements](#user-requirements)
  - [Lobby requirements](#lobby-requirements)
  - [Creating a linked channel](#creating-a-linked-channel)
  - [Try it out with the Discord API](#try-it-out-with-the-discord-api)
  - [Example implementation](#example-implementation)
  - [Joining Discord servers via linked lobbies](#joining-discord-servers-via-linked-lobbies)
  - [Change log — linked channels](#change-log--linked-channels)
- [Support and bug reports](#support-and-bug-reports)
- [What upstream leaves undocumented on these pages](#what-upstream-leaves-undocumented-on-these-pages)

---

# Sending Direct Messages

Direct Messages (DMs) allow players to communicate privately. The guide covers sending text messages
between users, handling display of messages in your game, and retrieving conversation history and
summaries.

## Rate limits and scopes

**Warning (upstream).** This feature is currently available with rate limits. To increase the rate
limits for your game, follow *Communication Features: Applying for Increased Rate Limits for
Production Releases* — see the communication features section of `CORE-CONCEPTS.md`.

**Prerequisites stated upstream**: set up the Discord Social SDK with the Getting Started guide (see
`GETTING-STARTED-CPP.md`, `GETTING-STARTED-UNITY.md`, `GETTING-STARTED-UNREAL.md`).

**Warning (upstream).** To utilize this communication feature, you must enable
[`Client::GetDefaultCommunicationScopes`] in your OAuth Scope configuration. See the OAuth Scopes core
concepts guide (`CORE-CONCEPTS.md`) for more details.

[`Client::GetDefaultCommunicationScopes`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a71499da752fbdc2d4326ae0fd36c0dd1

## Types of chat messages and channel types

The Discord Social SDK supports two types of chat:

- Direct messages (DMs) between two users — see [Sending a direct message to a
  user](#sending-a-direct-message-to-a-user) below.
- Chat messages within a lobby — see the "sending messages to a lobby" section of `LOBBIES.md`.

The SDK receives messages in the following channel types:

- DM
- Ephemeral DM
- Lobby

## Sending a direct message to a user

**Info (upstream).** While the SDK allows you to send messages on behalf of a user, you must only do
so in response to a user action. You should never automatically send messages.

You need the recipient's Discord ID and the message you want to send.

```cpp
std::string message = "ready to queue?";
uint64_t recipientId = 1234567890; // The recipient's Discord ID

client->SendUserMessage(recipientId, message, [](auto result, uint64_t messageId) {
  if (result.Successful()) {
    std::cout << "✅ Message sent successfully\n";
  } else {
    std::cout << "❌ Failed to send message: " << result.Error() << "\n";
  }
});
```

## Syncing messages with Discord

In some situations, messages from your game with the Social SDK also appear in Discord. This happens
for:

- 1 on 1 chat when at least one of the users is a full Discord user
- Lobby chat when the lobby is linked to a Discord channel (see [Linked Channels](#linked-channels)
  below)
- The message must have been sent by a user who is not banned on Discord.

When messaging between provisional accounts or non-friends, channel ID and recipient ID is set to the
other user's ID. These messages are sent **ephemerally** and do not persist within a channel. Because
of that, you will not be able to resolve a [`ChannelHandle`] for them.

[`ChannelHandle`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1ChannelHandle.html#ac32096b2ef15c5c220e9b7b92253cc46

## Receiving and rendering messages

When a user sends a message, the SDK can respond to new messages by registering
[`Client::SetMessageCreatedCallback`]. You can access the message content and sender's ID in your
callback from the [`MessageHandle`] object. The [`MessageHandle`] represents a single message received
by the SDK.

```cpp
client->SetMessageCreatedCallback([&client](uint64_t messageId) {
  if (auto message = client->GetMessageHandle(messageId)) {
    std::cout << "New message from " << message->AuthorId() << ": " << message->Content() << "\n";
  }
});
```

There are also callbacks for when a message is updated or deleted. Register these with
[`Client::SetMessageUpdatedCallback`] and [`Client::SetMessageDeletedCallback`].

[`Client::SetMessageCreatedCallback`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a28325a8e8c688a84ac851da4bc86e148
[`Client::SetMessageUpdatedCallback`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#aa01cf3c15403f29780dabfcfaf3b1dcd
[`Client::SetMessageDeletedCallback`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a2b6079eded10bea29abbb9695702637b
[`MessageHandle`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1MessageHandle.html#ae25595b43bc74b0c4c92c5165d16382f

## Suppressing double notifications

Suppose the user has the Discord desktop application open on the same machine as the game. In that
case, they will hear notifications from the Discord application, even though they can see those
messages in-game. So to avoid double-notifying users, call [`Client::SetShowingChat`] whenever the
chat is shown or hidden to suppress those duplicate notifications.

[`Client::SetShowingChat`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#acdf400ecb926392d1a110da73152b594

## Legal disclosure message type

As a convenience for game developers, the first time a user sends a message in the game, that message
shows up on the Discord client. The SDK will inject a "fake" message into the chat that contains a
basic English explanation of what is happening to the user. You can identify these messages with the
[`MessageHandle::DisclosureType`] method. Discord encourages you to customize the rendering of these
messages, possibly changing the wording, translating them, and making them look more "official". You
can choose to avoid rendering these as well.

[`MessageHandle::DisclosureType`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1MessageHandle.html#abefb9be7836951a6acf78a4bb1676638

## Message history in memory

The SDK keeps the **25 most recent messages** in each channel in memory, including direct messages.
For older messages, see [Getting direct message history](#getting-direct-message-history) below to
retrieve additional history from Discord's servers.

A [`MessageHandle`] will keep working even after the SDK has discarded the message for being too old.
You just will not be able to create new [`MessageHandle`] objects for that message via
[`Client::GetMessageHandle`].

[`Client::GetMessageHandle`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a7825220b28952a2156bd0e46db40ea5c

## Working with unrenderable content

Messages sent on Discord can contain content that may not be renderable in-game, such as images,
videos, embeds, polls, and more. The game is not expected to render these. Instead, it should show a
notice so the user knows there is more content and a way to view it on Discord. The
[`MessageHandle::AdditionalContent`] method will contain data about the non-text content in this
message.

You can use this metadata to render a placeholder message for players and can link out to Discord
using [`Client::CanOpenMessageInDiscord`] and [`Client::OpenMessageInDiscord`].

Upstream also points to the Discord API message resource documentation for more information about
messages.

[`MessageHandle::AdditionalContent`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1MessageHandle.html#af4497491a95fda65402b6acf7a8b42e5
[`Client::CanOpenMessageInDiscord`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#ae2aac143a691091691c5cc75aa07dace
[`Client::OpenMessageInDiscord`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a66b8f85b14403a5d5ea125f39aa6e1b1

## Getting direct message history

The SDK provides two methods to retrieve direct message conversation history, allowing you to display
past conversations when users open a DM or browse their message list.

### Retrieving all conversation summaries

Use [`Client::GetUserMessageSummaries`] to get a list of all users the current user has DM
conversations with, along with the most recent message ID for each conversation:

```cpp
client->GetUserMessageSummaries([](const discordpp::ClientResult &result,
                                  const std::vector<discordpp::UserMessageSummary> &summaries) {
    if (result.Successful()) {
        std::cout << "📋 Retrieved " << summaries.size() << " conversations\n";

        for (const auto &summary : summaries) {
            std::cout << "User ID: " << summary.UserId()
                     << ", Last Message ID: " << summary.LastMessageId() << "\n";
        }
    } else {
        std::cerr << "❌ Failed to retrieve conversation summaries\n";
    }
});
```

Each `discordpp::UserMessageSummary` exposes `UserId()` and `LastMessageId()`.

This is particularly useful for:

- Building a conversation list UI
- Determining which users have active conversations
- Finding the most recent activity in each conversation

[`Client::GetUserMessageSummaries`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a32dafc20ff1f99b019e40bdc81f46dde

### Retrieving messages from a specific conversation

Use [`Client::GetUserMessagesWithLimit`] to fetch message history from a specific DM conversation:

```cpp
const uint64_t recipientId = 1234567890; // The other user's Discord ID
const int32_t messageLimit = 50; // Number of recent messages to retrieve (max 200)

client->GetUserMessagesWithLimit(
    recipientId, messageLimit,
    [](const discordpp::ClientResult &result,
       const std::vector<discordpp::MessageHandle> &messages) {
        if (result.Successful()) {
            std::cout << "💬 Retrieved " << messages.size()
                     << " messages from conversation\n";

            // Messages are returned in reverse chronological order (newest first)
            for (const auto &message : messages) {
                std::cout << "Message: " << message.Content()
                         << " from " << message.AuthorId() << std::endl;
            }
        } else {
            std::cerr << "❌ Failed to retrieve message history\n";
        }
    }
);
```

**Important limitations (upstream):**

- Only a maximum of **200 messages** and up to **72 hours** of history can be retrieved
- Both players must have played the game for DM history to be accessible
- If either user has not played the game, the system cannot find a channel between them and may return
  a **404** `discordpp::ErrorType::HTTPError` error

Key points about [`Client::GetUserMessagesWithLimit`]:

- Messages are returned in reverse chronological order (newest first)
- The function checks the local cache first and only makes an HTTP request if needed
- Pass `0` or a negative value for `limit` to retrieve all available messages (up to the 200 message
  maximum)

This functionality is useful for:

- Displaying conversation history when a user opens a DM
- Implementing message scrollback features
- Preserving conversation context across game sessions
- Building a full-featured in-game messaging interface

[`Client::GetUserMessagesWithLimit`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a054a758a76c5873b38a4d79651a5f26c

## In-game direct message settings

The Discord client provides a settings screen for users to control who can DM them in-game via the
Social SDK.

*Image caption (upstream): Discord content and social — Connected game settings (994 × 684).*

You cannot control these settings directly with the Social SDK. However, you can call
[`Client::OpenConnectedGamesSettingsInDiscord`], which opens the Connected Games settings in the
Discord client, where users can manage their direct messaging settings related to games using the
Discord Social SDK.

If the client is not connected or the user is a provisional account, this function does nothing. **It
is always a no-op for console platforms.**

[`Client::OpenConnectedGamesSettingsInDiscord`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a24f268f5eebe9919a3f774354eb577e0

## Development rate limits

Prior to being approved for increased rate limits (see the communication features section of
`CORE-CONCEPTS.md`), sending direct messages is limited to **100 per 2 hours** per application.

These limitations are designed to provide sufficient capacity for development, testing, and
small-scale demos while ensuring system stability.

For guidance on detecting and retrying rate limited requests in the SDK, see the Social SDK
*Handle Rate Limits* how-to guide.

## Change log — sending direct messages

| Date            | Changes                          |
| --------------- | -------------------------------- |
| August 29, 2025 | Add DM history                   |
| June 30, 2025   | Add communications scope warning |
| May 06, 2025    | link to DM Settings              |
| March 17, 2025  | initial release                  |

---

# Linked Channels

## Access status and scopes

**Note (upstream).** This feature is currently available with **limited access**. To apply for full
access to closed beta features, or to reach out to Discord directly to discuss your game, fill out
[this form](https://discord.com/developers/social-sdk-closed-beta-access-request-form). See the
limited access section of the communication features guide in `CORE-CONCEPTS.md`.

**Warning (upstream).** To utilize this communication feature, you must enable
[`Client::GetDefaultCommunicationScopes`] in your OAuth Scope configuration. See the OAuth Scopes core
concepts guide (`CORE-CONCEPTS.md`) for more details.

**Prerequisites stated upstream**: set up the Discord Social SDK, and understand creating and managing
lobbies (see `LOBBIES.md`).

## What linking does

Linked Channels let players connect in-game lobbies with Discord text channels, enabling chat between
your game and Discord servers. When linked:

- In-game messages appear in the Discord channel
- Discord messages appear in your game
- Messages from your game show your game's name and icon in Discord

## Linked channel requirements

### Channel type and settings

| Requirement     | Description                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------- |
| Channel Type    | Must be a Discord text channel in a server                                                        |
| Age Restriction | Cannot be an [age-restricted channel](https://support.discord.com/hc/en-us/articles/115000084051) |
| Link Status     | Cannot be currently linked to another lobby                                                       |

### Required permissions

The user linking the channel must have these Discord permissions:

| Permission      | Description                      |
| --------------- | -------------------------------- |
| Manage Channels | Ability to edit channel settings |
| View Channel    | Can see and read the channel     |
| Send Messages   | Can post messages in the channel |

## Private channels

Discord allows all channels the user can access in a server to be linked in game, even if that channel
is private to other server members. This means a user could choose to link a private "admins chat"
channel (assuming they are an admin) in the game if they wanted.

It is not possible for the game to know which users should have access to that channel. **Every lobby
member can view and reply to all messages sent in the linked channel.**

**Warning (upstream).** If you are going to allow private channels to be linked in-game, you must make
sure that users are aware that their private channel will be viewable by everyone in the lobby.

To help you identify which channels are public or private, Discord added an
`isViewableAndWriteableByAllMembers` boolean. You can use that boolean to prevent private channels
from being linked or to know when to show a clear warning; it is up to you.

## User requirements

### Linking a lobby

The lobby member must have the `CanLinkLobby` flag set to link a channel to a lobby. This flag is
**disabled by default** and must be explicitly set using the Lobby API (the Discord API lobby resource)
for users you want to have elevated permissions. Discord recommends only toggling this on for the
equivalent of the administrator/owner of a lobby.

This allows you, as the game developer, to say, "Only the admins of this guild are allowed to configure
the linked channel."

### Unlinking a lobby

To unlink a channel from a lobby, lobby members only require the `CanLinkLobby` flag to be set for
them. They **do not** need to have any permissions on the Discord side.

## Lobby requirements

Discord recommends only using channel linking for **persistent** lobbies. Ephemeral lobbies such as
match-chat are not good candidates for linking.

Lobbies created on the client side with secrets are also **not eligible** for channel linking.

## Creating a linked channel

Channel linking happens entirely in the game. The user is never kicked out of the game to go to
Discord to set it up. At a high level you fetch the list of servers (also known as guilds) and
channels the user can access, show them some UI to pick a channel, and then save that selection back
to Discord.

### Fetch available servers (guilds) and channels

[`Client::GetUserGuilds`] fetches the user's Discord servers from the Discord API. A list of
`GuildMinimal` structs, including the guild ID and name, is returned on success.

[`Client::GetGuildChannels`] takes a `guildId` and fetches all the channels in a single guild that the
user can access. On success it returns a list of `GuildChannel` objects:

```cpp
struct GuildChannel {
    struct LinkedLobby {
        uint64_t applicationId;
        uint64_t lobbyId;
    };
    uint64_t id;
    std::string name;
    bool isLinkable;
    bool isViewableAndWriteableByAllMembers;
    std::optional<LinkedLobby> linkedLobby;
};
```

- `isLinkable` indicates whether the user can link the given guild channel. This includes checking for
  channel validity (Is it a text channel? Is it age-restricted? Is it already linked to another
  lobby?) and validating the user's channel permissions. (Check the **Edit Lobby/Channel Link**
  endpoint docs for a full list of requirements.)
- `isViewableAndWriteableByAllMembers` indicates if the channel in Discord has restrictions on any
  members' or roles' ability to read or write to it (e.g. the channel may be considered private in
  some way). These read/write permissions are **only enforced in the Discord client**. A player who
  may not be able to view the channel in-Discord can read/write to it in-game as long as they are a
  lobby member. **It is important to notify the player performing the link that the channel contents
  may become exposed to players in-game who do not have access to the channel in Discord.**

[`Client::GetUserGuilds`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#aac1ec02df6074ed9213ce230e6a42fe1
[`Client::GetGuildChannels`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#adba1e5a83c219a9c4f6dab1657778017

### Saving a channel link selection

Once the user has chosen a channel to link to, call [`Client::LinkChannelToLobby`] to set or change
the channel a lobby is linked to. Use [`Client::UnlinkChannelFromLobby`] to remove the link. The
conditions in [Linked channel requirements](#linked-channel-requirements) must be met for the given
lobby, channel, and user.

[`Client::LinkChannelToLobby`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a3114d58d50d4d2cb5752d95e121315d4
[`Client::UnlinkChannelFromLobby`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a28f78a6fe46eb11eb54ee9b53fa94ffe

## Try it out with the Discord API

To test Linked Channels before building out a player interface, follow these steps to get things
working in a prototype using the Discord API:

1. Create a lobby using the **Create Lobby** endpoint (`POST /lobbies` in the Discord API lobby
   resource).
2. Enable the `CanLinkLobby` flag (`1 << 0`) on your lobby member by either sending a request to the
   `/lobbies/<lobby_id>/members/<user_id>` endpoint or by including the member data in the body of the
   **Create Lobby** request.
3. Identify a Discord server text channel that your `lobby_member` has the specified permissions
   enabled for (again, read/write and manage channels) and grab the channel's id.
4. Send a request to the `/lobbies/<lobby_id>/channel-linking` endpoint described above with the
   channel id.

Your lobby and channel should now be linked, and if you send a message in the lobby you should see it
appear in the channel and vice versa.

Upstream gives HTTP methods for none of these three routes beyond naming the **Create Lobby** endpoint
and the **Edit Lobby/Channel Link** endpoint by title; it defers to the Discord API lobby resource
documentation for methods and parameters.

## Example implementation

### Step 1: set up message handling

```cpp
// filepath: your_game/channel_linking.cpp
void HandleDiscordMessage(const std::string& message) {
    std::cout << "📱 Game received: " << message << "\n";
    // Check if message is from the lobby
    // Display in your game UI
}

void SetupMessageHandlers(std::shared_ptr<discordpp::Client> client) {
    client->SetMessageCreatedCallback([](uint64_t messageId) {
        discordpp::MessageHandle message = client->GetMessageHandle(messageId);
        HandleDiscordMessage(message);
    });
}
```

### Step 2: fetch available servers

```cpp
void FetchDiscordServers(std::shared_ptr<discordpp::Client> client) {
    client->GetUserGuilds([](auto result, const auto& guilds) {
        if (!result.Successful()) {
            std::cout << "❌ Failed to fetch guilds\n";
            return;
        }

        for (const auto& guild : guilds) {
            std::cout << "📁 Guild: " << guild.name << "\n";
            // Store guild IDs for later use
            SaveGuildId(guild.id);
        }
    });
}

void FetchChannelsForGuild(
    std::shared_ptr<discordpp::Client> client,
    uint64_t guildId
) {
    client->GetGuildChannels(guildId, [](auto result, const auto& channels) {
        if (!result.Successful()) return;

        for (const auto& channel : channels) {
            if (channel.isLinkable) {
                std::cout << "  📝 Channel: " << channel.name;
                if (!channel.isViewableAndWriteableByAllMembers) {
                    std::cout << " (Private)";
                }
                std::cout << "\n";
            }
        }
    });
}
```

### Step 3: link channel to lobby

```cpp
void ShowPrivateChannelWarning() {
    std::cout << "⚠️ Warning: This is a private channel.\n";
    std::cout << "All lobby members will be able to see messages.\n";
    std::cout << "Do you want to continue? (y/n)\n";
    
    char response;
    std::cin >> response;
    return (response == 'y' || response == 'Y');
}

void LinkChannelToLobby(
    std::shared_ptr<discordpp::Client> client,
    uint64_t lobbyId,
    uint64_t channelId,
    bool isPrivate
) {
    if (isPrivate && !ShowPrivateChannelWarning()) {
        std::cout << "❌ Channel linking cancelled\n";
        return;
    }

    client->LinkChannelToLobby(
        lobbyId,
        channelId,
        [](auto result) {
            if (result.Successful()) {
                std::cout << "✅ Channel linked successfully!\n";
            } else {
                std::cout << "❌ Failed to link channel\n";
            }
        }
    );
}
```

### Step 4: send and receive messages

```cpp
void SendLobbyMessage(
    std::shared_ptr<discordpp::Client> client,
    uint64_t lobbyId,
    const std::string& message
) {
    client->SendLobbyMessage(lobbyId, message, [](auto result) {
        if (!result.Successful()) {
            std::cout << "❌ Failed to send message\n";
        }
    });
}

void UnlinkChannel(
    std::shared_ptr<discordpp::Client> client,
    uint64_t lobbyId
) {
    client->UnlinkChannelFromLobby(lobbyId, [](auto result) {
        if (result.Successful()) {
            std::cout << "✅ Channel unlinked\n";
        }
    });
}
```

### Step 5: putting it all together

```cpp
// filepath: your_game/main.cpp
int main() {
    auto client = std::make_shared<discordpp::Client>();
    
    // Set up handlers
    SetupMessageHandlers(client);
    
    // When user wants to link a channel:
    FetchDiscordServers(client);
    
    // After user selects a guild:
    FetchChannelsForGuild(client, selectedGuildId);
    
    // After user selects a channel:
    LinkChannelToLobby(
        client,
        currentLobbyId,
        selectedChannelId,
        isPrivateChannel
    );
    
    // When sending a message:
    SendLobbyMessage(client, currentLobbyId, "Hello from the game!");
    
    // When done with the channel:
    UnlinkChannel(client, currentLobbyId);
    
    return 0;
}
```

## Joining Discord servers via linked lobbies

Once a lobby is linked to a Discord channel, players can join the associated Discord server directly
from your game. This simplifies getting players into your Discord community by generating invites
on-demand, eliminating the need to manually share invite links.

The [`Client::JoinLinkedLobbyGuild`] function generates a **one-time-use invite** for the current user
and, on supported platforms, automatically navigates them to Discord to accept it.

An in-game player flow could look like:

1. A Discord server admin links a channel to your game's lobby
2. Players in the lobby see an option to "Join Discord Server" in your game
3. When clicked, the SDK generates a unique invite and opens Discord
4. The player accepts the invite and becomes a Discord server member

**Info (upstream).** Only players with linked Discord accounts can join the server. If a player is
using a provisional account, you should prompt them to link their Discord account first (see
`PROVISIONAL-ACCOUNTS.md` and `ACCOUNT-LINKING.md`).

```cpp
const uint64_t lobbyId = 1234567890;

// Invite the user to join the Discord guild associated with the linked lobby
client->JoinLinkedLobbyGuild(
    lobbyId,
    // This is triggered when the user is using a provisional account, since
    // the user needs a real Discord account to join the Discord server, so you don't need
    // to implement a provisional user check on implementation.
    [] {
        // Show a message in your UI explaining that they need to link their Discord account
        // and/or step them through the process
        std::cout << "📝 User needs to link their Discord account\n";
    },
    // Called after the invite generation attempt completes, providing either a
    // successful result with the invite URL or an error if the operation failed.
    [](const discordpp::ClientResult &result, const std::string& inviteUrl) {
        if(result.Successful()) {
            std::cout << "✅ Discord invite generated successfully!\n";

            // On console platforms, you'll need to display the invite URL
            // for users to manually navigate to
            #ifdef CONSOLE_PLATFORM
            std::cout << "Join the Discord server at: " << inviteUrl << "\n";
            // Display this URL in your game's UI for the player to use
            #endif
        } else {
            std::cerr << "❌ Failed to generate Discord invite\n";
        }
    }
);
```

[`Client::JoinLinkedLobbyGuild`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a54ec764e72e168de419ac14e24e8fc60

### Platform considerations

- **Desktop**: the SDK automatically opens the Discord client or web browser with the invite
- **Console**: since console platforms cannot navigate to Discord directly, you should display the
  invite URL in your game's UI so players can use it on another device

**Warning (upstream).** Discord server admins cannot restrict who can join the server via this method.
Any player in a linked lobby can generate an invitation to the server, regardless of their lobby
permissions. Make sure to make your players aware to only link channels in servers you trust your
players to join, and/or provide in-game options to disable this feature for certain lobbies.

## Change log — linked channels

| Date           | Changes                          |
| -------------- | -------------------------------- |
| June 30, 2025  | Add communications scope warning |
| March 17, 2025 | initial release                  |

---

# Support and bug reports

Both pages close with the same note: join the [Discord Developers
Server](https://discord.gg/discord-developers) and share questions in the `#social-sdk-dev-help`
channel for support from the community. Report Social SDK bugs at
[https://dis.gd/social-sdk-bug-report](https://dis.gd/social-sdk-bug-report).

# What upstream leaves undocumented on these pages

- **No signatures.** Neither page gives a declared signature for any `Client::` method. The parameter
  order and types are only visible in the code examples reproduced above; both pages defer to the C++
  reference at `discord.com/developers/docs/social-sdk/`.
- **HTTP methods for the three linked-channel routes are not stated.** `/lobbies/<lobby_id>/members/<user_id>`
  and `/lobbies/<lobby_id>/channel-linking` appear without a method; the page defers to the Discord
  API lobby resource and to the **Edit Lobby/Channel Link** endpoint docs.
- **Channel type enum values are not given.** The DM page names three channel types in prose ("DM",
  "Ephemeral DM", "Lobby") with no SDK enum name or numeric values.
- **`MessageHandle::DisclosureType` values are not enumerated**, nor is the exact disclosure text.
- **`MessageHandle::AdditionalContent` shape is not documented** — only that it "will contain data
  about the non-text content".
- **No rate limit figures for lobby messages or linked-channel operations.** The 100-per-2-hours
  figure is stated for direct messages only.
- **No error enum listing.** Only `discordpp::ErrorType::HTTPError` with status 404 is named.
- **The complete `CanLinkLobby` flag set is not given** — only that flag and its bit value `1 << 0`.
- **`GuildMinimal` is not shown as a struct**; the page states only that it carries the guild ID and
  name.
- The linked-channels example code contains upstream defects reproduced verbatim:
  `ShowPrivateChannelWarning` is declared `void` yet returns a `bool`, and `SetupMessageHandlers`
  passes a `MessageHandle` to a `const std::string&` parameter.
