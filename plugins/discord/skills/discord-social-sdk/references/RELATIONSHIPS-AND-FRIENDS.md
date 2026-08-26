# Relationships, Friends List and Game Invites

Distilled from three Discord Social SDK development guides:

- [Managing Relationships in Your Game](https://docs.discord.com/developers/discord-social-sdk/development-guides/managing-relationships) — change log last entry March 17, 2025
- [Creating a Unified Friends List](https://docs.discord.com/developers/discord-social-sdk/development-guides/creating-a-unified-friends-list) — change log last entry July 17, 2025
- [Managing Game Invites](https://docs.discord.com/developers/discord-social-sdk/development-guides/managing-game-invites) — change log last entry June 10, 2026

Read from a local mirror on 2026-08-26.

## Contents

- [Managing Relationships](#managing-relationships)
  - [Relationship scopes and consent](#relationship-scopes-and-consent)
  - [Relationship types: Discord versus game](#relationship-types-discord-versus-game)
  - [Discord friend relationships](#discord-friend-relationships)
  - [Game friend relationships](#game-friend-relationships)
  - [Sending game friend requests](#sending-game-friend-requests)
  - [Sending Discord friend requests](#sending-discord-friend-requests)
  - [Accept incoming friend requests](#accept-incoming-friend-requests)
  - [Reject incoming friend requests](#reject-incoming-friend-requests)
  - [Cancel outgoing friend requests](#cancel-outgoing-friend-requests)
  - [Managing existing relationships](#managing-existing-relationships)
  - [Blocking users](#blocking-users)
  - [Unblocking users](#unblocking-users)
  - [Change log — managing relationships](#change-log--managing-relationships)
- [Creating a Unified Friends List](#creating-a-unified-friends-list)
  - [Prerequisites and the two entities](#prerequisites-and-the-two-entities)
  - [User status and rich presence](#user-status-and-rich-presence)
  - [Approach 1: SDK unified friends list helper functions](#approach-1-sdk-unified-friends-list-helper-functions)
  - [Approach 2: manually fetching relationships and users](#approach-2-manually-fetching-relationships-and-users)
  - [Change log — unified friends list](#change-log--unified-friends-list)
- [Managing Game Invites](#managing-game-invites)
  - [Game invites are powered entirely by rich presence](#game-invites-are-powered-entirely-by-rich-presence)
  - [Configuring rich presence to enable game invites](#configuring-rich-presence-to-enable-game-invites)
  - [Registering a launch command](#registering-a-launch-command)
  - [Sending game invites](#sending-game-invites)
  - [Receiving game invites](#receiving-game-invites)
  - [Accepting game invites](#accepting-game-invites)
  - [Using game invites with lobbies](#using-game-invites-with-lobbies)
  - [Supporting mobile game invites](#supporting-mobile-game-invites)
  - [Setting a cover image for the invite (optional)](#setting-a-cover-image-for-the-invite-optional)
  - [Change log — managing game invites](#change-log--managing-game-invites)
- [Support and bug reports](#support-and-bug-reports)

---

# Managing Relationships

The SDK lets you manage relationships between players in your game: send and accept friend requests,
handle different types of relationships, block and unblock users, and work with both Discord-wide and
game-specific friendships.

**Prerequisites stated upstream**: complete the Getting Started guide (see `GETTING-STARTED-CPP.md`,
`GETTING-STARTED-UNITY.md`, `GETTING-STARTED-UNREAL.md`) and the Creating a Unified Friends List
guide (below in this file).

## Relationship scopes and consent

This feature requires the **Default Presence Scopes** (`openid` and `sdk.social_layer_presence`). Use
[`Client::GetDefaultPresenceScopes`] when configuring your OAuth2 flow. See the OAuth2 Scopes guide
(`CORE-CONCEPTS.md`) for details on all available scopes.

[`Client::GetDefaultPresenceScopes`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a7648bd1d2f7d9a86ebd0edb8bef12b5c

**Warning (upstream).** While the SDK allows you to manage a user's relationships, you should never
act without their explicit consent. You should not automatically send or accept friend requests. Only
invoke APIs to manage relationships in response to a user action such as clicking a "Send Friend
Request" button.

Discord models the relationship between two users using the Relationship entity in the SDK.
Relationships are not just for friends — they are also used to send and receive friend requests and
block other users.

## Relationship types: Discord versus game

Sometimes users want to be friends across all their games, so starting a new game does not start from
scratch. Sometimes they do not want to give out that access and only want to be friends in the
current game. The SDK therefore supports two types of relationship:

- **Discord relationships**: persist across games and on the Discord client. Both users can see
  whether each other is online, regardless of whether they are in the same game. Discord
  relationships are the same as becoming a friend in the Discord client.
- **Game relationships**: per-game relationships that do not carry over to other games. The two users
  can only see if the other is online if they are playing a game in which they are friends. Game
  friends can DM each other, and those DMs show up in Discord, but they can disable that behavior and
  keep their game conversations restricted to just the game. That option is located in the
  **"Content & Social"** user settings, under the **"Connected Games"** tab at the top of the page.

[`RelationshipHandle`] determines the type of friendship between the player and another user. It has
two fields:

- [`RelationshipHandle::DiscordRelationshipType`] for the **Discord friendship**
- [`RelationshipHandle::GameRelationshipType`] for the **game friendship**

Having both friend types matters because a pair of users might start out as game friends and later
choose to "upgrade" to full Discord friends. In that case their
[`RelationshipHandle::DiscordRelationshipType`] would be set to `RelationshipType::PendingIncoming`
or `RelationshipType::PendingOutgoing` (based on whether they are receiving or sending the request
respectively), while their [`RelationshipHandle::GameRelationshipType`] would remain
`RelationshipType::Friend`.

While the API technically supports users being both types of friends, you do not have to ensure that
every Discord friend is a game friend or vice versa. When adding friends, offer users a choice of
friend type and explain the difference. See the design guidelines for more.

[`RelationshipHandle`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1RelationshipHandle.html#a7da36b15ad0b7d38ba658a622e9ded77
[`RelationshipHandle::DiscordRelationshipType`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1RelationshipHandle.html#a5fecfb79a4a2b6f3dc5f73b09d0c3881
[`RelationshipHandle::GameRelationshipType`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1RelationshipHandle.html#aa60146eb72ede07e3e615565f61f97eb

## Discord friend relationships

- Persist across all games and Discord
- Limited to **1,000 friends**
- Online status visible everywhere
- Full Discord chat functionality

## Game friend relationships

- Only exist within your game
- **No current friend limit**
- Online status is only visible in-game

---

Once you have created a unified friends list, you can start managing relationships between players.

## Sending game friend requests

Sends (or accepts) a game friend request to the target user. You can send game friend requests using
the target's Discord unique username or user ID.

After the request is sent, each user has a new game relationship. For the current user
[`RelationshipHandle::GameRelationshipType`] will be `RelationshipType::PendingOutgoing`, and for the
target user it will be `RelationshipType::PendingIncoming`.

If the current user has already received a game friend request from the target user (meaning
[`RelationshipHandle::GameRelationshipType`] is `RelationshipType::PendingIncoming`), the two users
become game friends.

```cpp
client->SendGameFriendRequest("username", [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Game friend request sent successfully!\n";
  }
});

client->SendGameFriendRequestById(123456789, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Game friend request sent successfully!\n";
  }
});
```

## Sending Discord friend requests

Sends (or accepts) a Discord friend request to the target user, by Discord unique username or user ID.

After the request is sent, each user has a new Discord relationship. For the current user
[`RelationshipHandle::DiscordRelationshipType`] will be `RelationshipType::PendingOutgoing`, and for
the target user it will be `RelationshipType::PendingIncoming`.

If the current user has already received a Discord friend request from the target user (meaning
[`RelationshipHandle::DiscordRelationshipType`] is `RelationshipType::PendingIncoming`), the two users
become Discord friends.

```cpp
client->SendDiscordFriendRequest("username", [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Discord friend request sent successfully!\n";
  }
});

client->SendDiscordFriendRequestById(123456789, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Discord friend request sent successfully!\n";
  }
});
```

## Accept incoming friend requests

Allow your players to accept incoming friend requests, which `RelationshipType::PendingIncoming`
represents.

```cpp
// RelationshipHandle::DiscordRelationshipType == RelationshipType::PendingIncoming
client->AcceptDiscordFriendRequest(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Discord friend request accepted!\n";
  }
});

// RelationshipHandle::GameRelationshipType == RelationshipType::PendingIncoming
client->AcceptGameFriendRequest(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Game friend request accepted!\n";
  }
});
```

## Reject incoming friend requests

Allow your players to reject incoming friend requests, which `RelationshipType::PendingIncoming`
represents.

```cpp
// Reject Incoming Friend Requests
// RelationshipHandle::DiscordRelationshipType == RelationshipType::PendingIncoming
client->RejectDiscordFriendRequest(userId,[](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Discord friend request rejected!\n";
  }
});

// RelationshipHandle::GameRelationshipType == RelationshipType::PendingIncoming
client->RejectGameFriendRequest(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Game friend request rejected!\n";
  }
});
```

## Cancel outgoing friend requests

Allow your players to cancel outgoing friend requests, which `RelationshipType::PendingOutgoing`
represents. The upstream comment on the Discord variant reads `PendingIncoming`; that is how the page
states it.

```cpp
// Cancel Outgoing Friend Requests
// RelationshipHandle::DiscordRelationshipType == RelationshipType::PendingIncoming
client->CancelDiscordFriendRequest(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Discord friend request canceled!\n";
  }
});

// RelationshipHandle::GameRelationshipType == RelationshipType::PendingOutgoing
client->CancelGameFriendRequest(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Game friend request canceled!\n";
  }
});
```

## Managing existing relationships

Allow your players to remove existing relationships with other users. This removes the relationship
from both users, and they will no longer be able to see each other's online status or send messages.

```cpp
// Removes any friendship between the current user and the target user. 
// This function will remove BOTH any Discord friendship and any game friendship between the users.
client->RemoveDiscordAndGameFriend(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Discord and Game friendships removed!\n";
  }
});

// Removes any game friendship between the current user and the target user.
client->RemoveGameFriend(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 Game friendship removed!\n";
  }
});
```

## Blocking users

Allow your players to block another user so they cannot send friend or activity invites and cannot
message them anymore.

Blocking a user also removes any existing relationship between the two users and persists across
games, so blocking a user in one game or on Discord blocks them in all other games and on Discord.

```cpp
client->BlockUser(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 User blocked successfully!\n";
  }
});
```

## Unblocking users

Allow your players to unblock another user if they have been blocked. Unblocking a user does **not**
restore any previous relationships between the users.

```cpp
client->UnblockUser(userId, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "🎮 User unblocked successfully!\n";
  }
});
```

## Change log — managing relationships

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | Initial release |

---

# Creating a Unified Friends List

A unified friends list combines both Discord and game-specific relationships in one view. The guide
covers fetching all relationship data, filtering and organising relationships, displaying online
status, and handling different relationship types.

**Prerequisites stated upstream**: set up the SDK (Getting Started), authenticate users (see
`ACCOUNT-LINKING.md`), and understand relationship types (see [Managing
Relationships](#managing-relationships) above).

This feature requires the **Default Presence Scopes** (`openid` and `sdk.social_layer_presence`). Use
[`Client::GetDefaultPresenceScopes`] when configuring your OAuth2 flow; see `CORE-CONCEPTS.md` for
all available scopes.

## Prerequisites and the two entities

The Discord friend list is ultimately constructed from two entities: **Relationships** and **Users**.
Query the Relationships API to find everyone a user is a friend with, and the Users API to find the
extra information for rendering the list, such as whether they are online.

**Relationships** are how Discord models friends, friend requests, and more. All relationships for
the current user are loaded when the Client connects. Each relationship has a target user id and a
type, such as `Friend`, `PendingOutgoing`, or `Blocked`. To allow users to manage their relationships
in your game, provide a way to accept or reject friend requests, block users, and manage pending
requests — see [Managing Relationships](#managing-relationships) above for implementation details.

**Users** are the Discord users that are part of the relationships. The SDK provides a way to fetch a
user by their ID, and the user object contains information such as their username, display name,
avatar, and more.

## User status and rich presence

Presence is how Discord stores whether a user is currently online, as well as what activities they
are currently doing (such as playing a game). The SDK gives you access to two types of status:

- **Online Status**: Online, Offline, Idle, etc.
- **Rich Presence**: any activities associated with the current game (or *application* in Discord
  parlance).

**Info (upstream).** The SDK will only display activities associated with the current game, meaning
you will not be able to see other game activities in Rich Presence, even if you can see them in the
Discord client.

See the design guidelines for Status & Rich Presence for best practices on displaying presence
information, and `RICH-PRESENCE.md` for the Rich Presence API itself.

There are two ways to create a unified friends list in your game:

1. Using the SDK Unified Friends List helper functions, which automatically group and sort
   relationships and users for you.
2. Directly retrieving relationships and users from the SDK, and sorting manually.

## Approach 1: SDK unified friends list helper functions

**Info (upstream).** This approach is recommended as it significantly reduces the amount of code you
need to write and maintain compared to manually fetching and organizing relationships, while ensuring
your friends list follows Discord's best practices.

The SDK provides built-in helper functions that automatically group and sort your friends list
according to Discord's recommended design guidelines for a unified friends list.

The SDK automatically organizes friends into the three groups found via [`RelationshipGroupType`]:

- `OnlinePlayingGame`: friends who are online and currently playing your game
- `OnlineElsewhere`: friends who are online but not playing your game
- `Offline`: friends who are offline

[`RelationshipGroupType`]: https://discord.com/developers/docs/social-sdk/namespacediscordpp.html#a503ed2f7b0bfbd435321a0e8b1dfba35

### Step 1: display the unified friends list

The [`Client::GetRelationshipsByGroup`] method returns a pre-sorted list of relationships for a
specific group type. This eliminates the need to manually filter, categorize, and sort friends
yourself. The SDK handles all the logic for determining which group each friend belongs to based on
their online status and game activity, and automatically sorts users within each group (for example,
users who have played your game are moved to the top of the `OnlineElsewhere` group).

```cpp
void DisplayUnifiedFriendsList(const std::shared_ptr<discordpp::Client> &client) {
    // Get friends playing the game
  const auto onlineInGame = client->GetRelationshipsByGroup(
        discordpp::RelationshipGroupType::OnlinePlayingGame
    );

    // Get friends online elsewhere
    const auto onlineElsewhere = client->GetRelationshipsByGroup(
        discordpp::RelationshipGroupType::OnlineElsewhere
    );

    // Get offline friends
    const auto offline = client->GetRelationshipsByGroup(
        discordpp::RelationshipGroupType::Offline
    );

    // Display "Online - GameTitle" Friends
    std::cout << "\n=== Online - GameTitle (" << onlineInGame.size() << ") ===\n";
    for (const auto& relationship : onlineInGame) {
        auto user = relationship.User();
        if (user) {
            std::string displayStr = "🟣 " + user->DisplayName();

            // Add Discord friend indicator
            if (relationship.DiscordRelationshipType() == discordpp::RelationshipType::Friend) {
                displayStr += " 👾";
            }

            // Add game friend indicator
            if (relationship.GameRelationshipType() == discordpp::RelationshipType::Friend) {
                displayStr += " 🎮";
            }

            std::cout << displayStr << "\n";
        }
    }

    // Display "Online - Elsewhere" Friends
    std::cout << "\n=== Online - Elsewhere (" << onlineElsewhere.size() << ") ===\n";
    for (const auto& relationship : onlineElsewhere) {
        auto user = relationship.User();
        if (user) {
            std::string displayStr = "🟢 " + user->DisplayName();

            // Add Discord friend indicator
            if (relationship.DiscordRelationshipType() == discordpp::RelationshipType::Friend) {
                displayStr += " 👾";
            }

            // Add game friend indicator
            if (relationship.GameRelationshipType() == discordpp::RelationshipType::Friend) {
                displayStr += " 🎮";
            }

            std::cout << displayStr << "\n";
        }
    }

    // Display "Offline" Friends
    std::cout << "\n=== Offline (" << offline.size() << ") ===\n";
    for (const auto& relationship : offline) {
        auto user = relationship.User();
        if (user) {
            std::string displayStr = "⚫ " + user->DisplayName();

            // Add Discord friend indicator
            if (relationship.DiscordRelationshipType() == discordpp::RelationshipType::Friend) {
                displayStr += " 👾";
            }

            // Add game friend indicator
            if (relationship.GameRelationshipType() == discordpp::RelationshipType::Friend) {
                displayStr += " 🎮";
            }

            std::cout << displayStr << "\n";
        }
    }
}
```

[`Client::GetRelationshipsByGroup`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a9f7898d3f3d1ec92b06c662df70746d5

### Step 2: set up automatic updates

To keep your friends list up-to-date automatically, use
[`Client::SetRelationshipGroupsUpdatedCallback`]. This callback is triggered whenever any change
occurs that might affect the friends list grouping, such as a friend going online or offline, or when
a relationship changes, such as when you accept a friend request or block a user.

```cpp
// Set up the unified friends list update callback
client->SetRelationshipGroupsUpdatedCallback([&client](const uint64_t userId) {
    std::cout << "👥 Friends list updated for user: " << userId << std::endl;
    DisplayUnifiedFriendsList(client);
});
```

[`Client::SetRelationshipGroupsUpdatedCallback`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#af12441ef091298f968075b7190851098

## Approach 2: manually fetching relationships and users

This gives you more control over how the friends list is displayed in your game.

### Step 1: fetch relationships

A function using [`Client::GetRelationships`] to query all the relationships and user information for
the account:

```cpp
void DisplayFriendsList(discordpp::Client& client) {
    std::vector<std::string> relationships{};
    for (auto& relationship: client->GetRelationships()) {
        auto user = relationship.User();
        if (!user) {
            continue;
        }
    
        std::string str{};
        // Identifying information about the user:
        str += " DiscordName: " + user->DisplayName();
        str += " DiscordId: " + std::to_string(user->Id());
        // Provisional users don't have a Discord icon shown next to them:
        str += " IsProvisional: " + std::to_string(user->IsProvisional());
        // Whether the relationship is for a friend, a friend request, or because the user is blocked:
        // For a friends list you'll want to filter out blocked users
        // And likely display friend requests in a different section
        str += " DiscordRelationshipType: " + std::string(discordpp::EnumToString(relationship.DiscordRelationshipType()));
        str += " GameRelationshipType: " + std::string(discordpp::EnumToString(relationship.GameRelationshipType()));
        // Whether the user is online/offline/etc:
        str += " IsOnlineAnywhere: " + std::to_string(user->Status() != discordpp::StatusType::Offline);
        str += " IsOnlineInGame: " + std::to_string(user->GameActivity() != std::nullopt);
        relationships.push_back(str);
    }
    
    std::sort(relationships.begin(), relationships.end());
    for (auto str : relationships) {
        printf("%s\n", str.c_str());
    }
}
```

[`Client::GetRelationships`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#ad481849835cd570f0e03adafcf90125d

**Info (upstream).** The `relationship.User()` function returns a [`UserHandle`] object that
represents a user that the Discord Social SDK knows about. Handle objects maintain references to both
the underlying data and the SDK instance, which means that when their data changes, existing handle
objects automatically reflect these changes without needing to be recreated.

[`UserHandle`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1UserHandle.html#a587bcc838e42dc5c56f840a350070707

Call this function when the client is ready, so add it to the ready callback:

```cpp
// Set up status callback to monitor client connection
client->SetStatusChangedCallback([client](discordpp::Client::Status status, discordpp::Client::Error error, int32_t errorDetail) {
    std::cout << "🔄 Status changed: " << discordpp::Client::StatusToString(status) << std::endl;

    if (status == discordpp::Client::Status::Ready) {
        std::cout << "✅ Client is ready! You can now call SDK functions.\n";
        std::cout << "👥 Friends Count: " << client->GetRelationships().size() << std::endl;
        
        SetRichPresence(client);
        DisplayFriendsList(client);

    } else if (error != discordpp::Client::Error::None) {
        std::cerr << "❌ Connection Error: " << discordpp::Client::ErrorToString(error) << " - Details: " << errorDetail << std::endl;
    }
});
```

This outputs the raw relationship data to the console, which you can use to filter, organize and
build a friends list that fits your game's design aesthetic.

### Step 2: organize relationships

Based on the design guidelines for a Unified Friends List, separate the player's friends list into
three sections: `Online - GameTitle`, `Online - Elsewhere`, and `Offline`.

Because the example is a text console application it uses emojis to represent the status of each
friend, but you can use your own design elements to convey status and presence in your game.

The updated `DisplayFriendsList` function:

- creates three vectors to store the friends in each category;
- filters out pending friends and blocked users;
- adds indicators for Discord friends, game friends, and provisional users;
- categorizes friends based on their game and presence status;
- sorts each category alphabetically;
- displays each category separately.

**Info (upstream).** This example is for reference only. Please make sure you use efficient data
structures and cache data when appropriate to avoid performance issues in your game.

```cpp
void DisplayFriendsList(std::shared_ptr<discordpp::Client> client) {
    // Create vectors for each section
    std::vector<std::string> inGame;
    std::vector<std::string> online;
    std::vector<std::string> offline;
    
    for (auto& relationship : client->GetRelationships()) {
        auto user = relationship.User();
        if (!user) {
            continue;
        }

        // Filter out pending friends and blocked users
        // You can display friend requests and blocked users in a different view to allow players to manage them in your game
        if (relationship.DiscordRelationshipType() != discordpp::RelationshipType::Friend) {
            continue;
        }
 
        std::string str;
        str += user->DisplayName();

        // Add Discord friend indicator
        // In a real game, please use the official Discord logo available in our design guidelines
        if (relationship.DiscordRelationshipType() == discordpp::RelationshipType::Friend) {
            str += " 👾";
        }

        // Add game friend indicator
        if (relationship.GameRelationshipType() == discordpp::RelationshipType::Friend) {
            str += " 🎮";
        }

        // Add provisional indicator
        if (user->IsProvisional()) {
            str += " (Provisional)";
        }

        // Categorize based on status
        if (user->GameActivity()) {
            // in game
            inGame.push_back("🟣 " + str);
        } else if (user->Status() != discordpp::StatusType::Offline) {
            // online
            online.push_back("🟢 " + str);
        } else {
            // offline
            offline.push_back("⚫ " + str);
        } 
    }
    
    // Sort each category
    std::sort(inGame.begin(), inGame.end());
    std::sort(online.begin(), online.end());
    std::sort(offline.begin(), offline.end());
    
    // Display "Online - GameTitle" Friends
    std::cout << "\n=== Online - GameTitle (" << inGame.size() << ") ===\n";
    for (const auto& str : inGame) {
        std::cout << str << "\n";
    }
    
    // Display "Online - Elsewhere" Friends
    std::cout << "\n=== Online - Elsewhere (" << online.size() << ") ===\n";
    for (const auto& str : online) {
        std::cout << str << "\n";
    }
    
    // Display "Offline" Friends
    std::cout << "\n=== Offline (" << offline.size() << ") ===\n";
    for (const auto& str : offline) {
        std::cout << str << "\n";
    }
}
```

Building and running the application now shows a list of friends separated into three categories:
`Online - GameTitle`, `Online - Elsewhere`, and `Offline`.

### Step 3: monitor changes to users

To monitor for user changes, use [`Client::SetUserUpdatedCallback`]. This callback is triggered
whenever a user's info is updated, such as name or presence changes (when they go online, offline, or
start playing your game).

```cpp
client->SetUserUpdatedCallback([&client](uint64_t userId) {
    std::cout << "👤 User updated: " << userId << std::endl;
    DisplayFriendsList(*client);
});
```

Now the friends list automatically updates when a friend's presence changes.

**Info (upstream).** The automatic updates of the [`UserHandle`] object to the latest user
information should be sufficient for retrieving the most up-to-date user information.
[`Client::SetUserUpdatedCallback`] may be more useful to identify times when you wish to re-sort your
user list, or similar operations.

[`Client::SetUserUpdatedCallback`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a3559f375165acedc6d6677ef599b3a4a

### Step 4: monitor changes in relationships

Two callbacks handle relationship updates.

**Warning (upstream).** These examples rebuild the friends list from scratch every time a
relationship changes. For performance reasons, Discord recommends maintaining a collection of
[`UserHandle`] objects and adding and removing them appropriately.

#### Relationship created callback

This can happen when a user sends or accepts a friend invite, or blocks a user.

```cpp
client->SetRelationshipCreatedCallback([&client](uint64_t userId, bool isDiscordRelationshipUpdate) {
    std::optional<discordpp::UserHandle> user = client->GetUser(userId);
    // if the userid is valid (which it should be), we can display the user's display name
    if(user) {
        std::cout << "🤝 Relationship created: " << user->DisplayName() << std::endl;
        DisplayFriendsList(*client);
    }
});
```

#### Relationship deleted callback

This can happen when a user rejects a friend request or removes a friend.

```cpp
client->SetRelationshipDeletedCallback([&client](uint64_t userId, bool isDiscordRelationshipUpdate) {
    std::cout << "🔥 Relationship deleted: " << userId << std::endl;
    DisplayFriendsList(*client);
});
```

## Change log — unified friends list

| Date           | Changes                |
| -------------- | ---------------------- |
| March 17, 2025 | Initial release        |
| July 17, 2025  | Add UFL helper methods |

---

# Managing Game Invites

Game Invites allow users to invite others to join their game session or party. This feature is
available on the Discord client and the Social SDK.

## Game invites are powered entirely by rich presence

**Info (upstream). Game Invites are not a standalone feature** — they are **powered entirely by Rich
Presence**. When you configure Rich Presence with party information, a join secret, and/or supported
platforms, Discord automatically enables invite functionality. This guide shows you how to configure
Rich Presence to unlock game invites.

**Prerequisites stated upstream**:

- Complete the Setting Rich Presence guide (`RICH-PRESENCE.md`)
- Understand that without an active Rich Presence with party data, invites will not work
- Set up the SDK with the Getting Started guide

**Warning (upstream).** To utilize this communication feature, you must enable
[`Client::GetDefaultCommunicationScopes`] in your OAuth Scope configuration. See the OAuth Scopes
core concepts guide (`CORE-CONCEPTS.md`) for more details.

[`Client::GetDefaultCommunicationScopes`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a71499da752fbdc2d4326ae0fd36c0dd1

**Info (upstream) on naming.** Rich Presence, aka "Activity", can be thought of as the "current
activity of a user" and is represented by the [`Activity`] class in the SDK and in Discord's gateway
events (the activity object under gateway events in the Discord API docs). This is not to be confused
with Discord Activities, which are embedded games that can also set and display rich presence.

[`Activity`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Activity.html#ae793d9adbe16fef402b859ba02bee682

## Configuring rich presence to enable game invites

### Setting up rich presence

```cpp
// Create discordpp::Activity - This Rich Presence Activity is your invite configuration
discordpp::Activity activity;
activity.SetType(discordpp::ActivityTypes::Playing);

// Set the game state and details
activity.SetState("In Competitive Match");
activity.SetDetails("Valhalla");

// Update Rich Presence presence
client->UpdateRichPresence(activity, [](discordpp::ClientResult result) {
    if(result.Successful()) {
        std::cout << "🎮 Rich Presence updated successfully!\n";
        // Note: Invites are NOT yet enabled - we need party info and join secret
    } else {
        std::cerr << "❌ Rich Presence update failed";
    }
});
```

Running the game now, the Discord client shows we are "In Competitive Match" on "Valhalla". You must
set up your rich presence [`Activity`] with party information **and** a join secret to send game
invites.

### Adding an activity party

```cpp
// rest of the code

// Create discordpp::ActivityParty
discordpp::ActivityParty party;
party.SetId("party1234");
// current party size
party.SetCurrentSize(1);
// max party size
party.SetMaxSize(5);
// Set the party information in the Activity, to inform the invite about the party size and how many players can join
activity.SetParty(party);

// Update Rich Presence
// Still not enough for invites - we need the join secret!
```

Running the game now, the Discord client shows we are "In Competitive Match" on "Valhalla" with more
information about the party.

### Adding join secret and supported platforms

The last step is to add a join secret to your rich presence activity.

The `Join Secret` is a generic secret that you can use to join a Discord lobby (see `LOBBIES.md`), a
game session, or something else. The game invite system is a way for players to share this secret
value with other players — how you use it is up to you.

You also need to set the supported platforms for joining the game so that the Discord client can
display the correct invite button for the user's platform.

```cpp
// Create discordpp::Activity

// Create ActivitySecrets
discordpp::ActivitySecrets secrets;
secrets.SetJoin("joinsecret1234");    // Rich Presence secret will be in the invite payload
activity.SetSecrets(secrets);

// Set supported platforms that can join the game
// See discordpp::ActivityGamePlatforms for available platforms
activity.SetSupportedPlatforms(discordpp::ActivityGamePlatforms::Desktop);

// Update Rich Presence
// ✅ NOW invites are enabled through Rich Presence!
```

### Putting it all together

```cpp
// Create discordpp::Activity - This Rich Presence Activity is your invite configuration
discordpp::Activity activity;
activity.SetType(discordpp::ActivityTypes::Playing);

// Set the game state and details
activity.SetState("In Competitive Match");
activity.SetDetails("Valhalla");

// Set the party information
discordpp::ActivityParty party;
party.SetId("party1234");
party.SetCurrentSize(1);          // current party size
party.SetMaxSize(5);              // max party size
// Set the party information in the Activity, to inform the invite about the party size and how many players can join
activity.SetParty(party);

// Create ActivitySecrets
discordpp::ActivitySecrets secrets;
secrets.SetJoin("joinsecret1234");    // Rich Presence secret will be in the invite payload
activity.SetSecrets(secrets);

// Set supported platforms that can join the game
// See discordpp::ActivityGamePlatforms for available platforms
activity.SetSupportedPlatforms(discordpp::ActivityGamePlatforms::Desktop);

// Update Rich Presence presence
client->UpdateRichPresence(activity, [](discordpp::ClientResult result) {
    if(result.Successful()) {
        std::cout << "🎮 Rich Presence updated successfully!\n";
        // ✅ Rich Presence updated = Game invites now available!
    } else {
        std::cerr << "❌ Rich Presence update failed";
        // ❌ No Rich Presence = No invites possible
    }
});
```

The Discord client shows an invite button to your friends when they see your rich presence.

## Registering a launch command

Before sending a game invite, make sure Discord knows how to launch your game when someone opens an
invite.

**Launch registration is local**, as in it only affects the machine that calls it. Therefore, each
time the SDK starts up within your game client, register how your game should be launched on that
machine, so that if the player opens an invite from Discord, your game can be launched for them if
not already running.

There are two ways to register, depending on how your game is distributed: register a launch command
for your game, or register a Steam Game ID.

### Registering a launch command

[`Client::RegisterLaunchCommand`] registers a command that Discord will run on this machine to launch
your game. Run this when the SDK starts up so that if the user opens an invite from Discord the game
can be launched for them.

```cpp
client->RegisterLaunchCommand(YOUR_APP_ID, "yourgame://");
```

[`Client::RegisterLaunchCommand`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a024d7222931fdcb7d09c2b107642ecab

### Registering a Steam game

For Steam games, [`Client::RegisterLaunchSteamApplication`] registers your Steam game ID on this
machine. As with the launch command, run this when the SDK starts up so that if the user opens an
invite from Discord the game can be launched for them.

```cpp
client->RegisterLaunchSteamApplication(YOUR_APP_ID, STEAM_GAME_ID);
```

[`Client::RegisterLaunchSteamApplication`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a45b2c791c5b06f77d457dacb53dfba40

## Sending game invites

**Warning (upstream). Testing invites requires a second account.** A user cannot see their own Rich
Presence Invite — you will not receive invites you send to yourself. To test the full invite flow, use
a separate test account.

Game invites can be sent in two ways:

1. Users can send game invites directly through the Discord client.
2. You can programmatically send game invites on a user's behalf through the SDK.

### Sending game invites in the Discord client

Users can send game invites directly through the Discord client. This feature is described in detail
in the [Game Invites help center
article](https://support.discord.com/hc/en-us/articles/115001557452-Game-Invites).

### Sending game invites in the SDK

If a player has the required party, join secret, and supported platforms set in their rich presence,
your game can send game invites programmatically through the SDK using [`Client::SendActivityInvite`].

**Warning (upstream).** [`Client::SendActivityInvite`] only works if Rich Presence is active with
proper configuration.

**Tip (upstream). Invite messages require communication scopes** (see the prerequisites above). The
invite and join flow itself is powered by Rich Presence and works with only the default presence
scopes. However, the invite **message** (e.g. `"Join my game!"`) is a Discord message. If the sender
is authorized with only presence scopes, the invite still sends and can be accepted, but its message
content will be empty.

```cpp
uint64_t targetUserId = 1111785262289277050; 
std::string inviteMessage = "Join my game!";
client->SendActivityInvite(targetUserId, inviteMessage, [](discordpp::ClientResult result) {
  if(result.Successful()) {
    std::cout << "Activity Invite sent to user" << std::endl;
  } else {
    std::cerr << "Failed - check if Rich Presence has party, secret, and platforms set" << std::endl;
  }
});
```

*Image caption (upstream): Example of a sent game invite in the Discord client (436 × 251).*

[`Client::SendActivityInvite`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#afc14e98fc070399895739da6d53efa60

## Receiving game invites

Game invites can also be received in two ways:

1. Users can receive game invites directly through the Discord client, in their DMs. This feature is
   described in detail in the Game Invites help center article linked above.
2. Your game can receive game invites for a user programmatically through the SDK.

Use [`Client::SetActivityInviteCreatedCallback`] to detect new invites and
[`Client::AcceptActivityInvite`] to accept them. The callback you specify for
[`Client::AcceptActivityInvite`] will be invoked with the join secret you set in Rich Presence.

```cpp
client->SetActivityInviteCreatedCallback([&client](discordpp::ActivityInvite invite) {
  std::cout << "Activity Invite received from user: " << invite.SenderId() << std::endl;
  if(auto message = client->GetMessageHandle(invite.MessageId())){
    std::cout << "Invite Message: " << message->Content() << std::endl;
  }
  client->AcceptActivityInvite(invite, [](discordpp::ClientResult result, std::string joinSecret) {
    if(result.Successful()) {
      std::cout << "Activity Invite accepted successfully!\n";
      // joinSecret comes from the sender's Rich Presence configuration
      // Use the joinSecret to connect the two players in your game
    } else {
      std::cerr << "❌ Activity Invite accept failed";
    }
  });
});
```

[`Client::AcceptActivityInvite`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#ad12cf35065e4d2b303ee470af7c6ef37
[`Client::SetActivityInviteCreatedCallback`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a3b4e37a222a8662506d763514774bedc

## Accepting game invites

Use [`Client::SetActivityJoinCallback`] to monitor for a user accepting a game invite, either in-game
or in Discord. Use the join secret to connect the players in your game.

```cpp
// This fires when a user clicks "Join" on someone's Rich Presence
client->SetActivityJoinCallback([&client](std::string joinSecret) {
  // joinSecret is pulled from the host's Rich Presence ActivitySecrets
  // Use the joinSecret to connect the players in your game
});
```

[`Client::SetActivityJoinCallback`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a587d1c6d0352eba397c888987aa58418

## Using game invites with lobbies

Game invites can be used together with Lobbies (see `LOBBIES.md`) to create a seamless experience for
players joining a game session or party. When a player accepts a game invite, use the join secret to
connect the two players.

An example flow:

- When a user starts playing the game, they create a lobby with a random secret string, using
  [`Client::CreateOrJoinLobby`]
- That user publishes their Rich Presence with the join secret set to the lobby secret, along with
  party size information
- Another user can then see that Rich Presence on Discord and request to join
- Once accepted, the new user receives the join secret, and their client can call
  `CreateOrJoinLobby(joinSecret)` to join the lobby
- Finally, the original user can notice that the lobby membership has changed, so they publish a new
  Rich Presence update containing the updated party size information

**Info (upstream).** These examples use client-side lobby management but can also be adapted for
lobbies created on the server side.

[`Client::CreateOrJoinLobby`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a8b4e195555ecaa89ccdfc0acd28d3512

### Game invite with lobby example

```cpp
// User A
// 1. Create a lobby with secret
std::string lobbySecret = "foo"
uint64_t USER_B_ID = 01234567890;
client->CreateOrJoinLobby(lobbySecret, [&client](discordpp::ClientResult result, uint64_t lobbyId) {
  // 2. Update Rich Presence with a party and join secret to enable invites
  discordpp::Activity activity{};
  activity.SetType(discordpp::ActivityTypes::Playing);
  activity.SetState("In Lobby");

  // Rich Presence party configuration for how many players can join
  discordpp::ActivityParty party{};
  party.SetId("party1234");
  party.SetCurrentSize(1);
  party.SetMaxSize(4);
  activity.SetParty(party);

  // Rich Presence secret is what is shared via invites
  discordpp::ActivitySecrets secrets{};
  secrets.SetJoin(lobbySecret);  // This connects Rich Presence to your lobby
  activity.SetSecrets(secrets);

  // Don't forget to set this Rich Presence update, otherwise SendActivityInvite won't work!
  client->UpdateRichPresence(std::move(activity), [&client](discordpp::ClientResult result) {
    // 3. NOW we can send invites because Rich Presence is configured
    client->SendActivityInvite(USER_B_ID, "come play with me", [](discordpp::ClientResult result) {
        if(result.Successful()) {
            std::cout << "💌 Invite sent successfully!\n";
        } else {
            std::cerr << "❌ Invite failed - check Rich Presence configuration\n";
        }
    });
  });
});

// User B
// 4. Monitor for new invites
client->SetActivityInviteCreatedCallback([&client](discordpp::ActivityInvite invite) {
  std::cout << "💌 New invite received: " << invite.SenderId() << "\n";
  // 5. When an invite is received, ask the user if they want to accept it.

  // If they choose to do so then go ahead and invoke AcceptActivityInvite
  client->AcceptActivityInvite(invite, [&client](discordpp::ClientResult result, std::string joinSecret) {
    if (result.Successful()) {
      std::cout << "🎮 Invite accepted! Joining lobby...\n";
      // joinSecret came from User A's Rich Presence configuration

      // 6. Join the lobby using the joinSecret
      client->CreateOrJoinLobby(joinSecret, [=](discordpp::ClientResult result, uint64_t lobbyId) {
        // Successfully joined lobby!
        if (result.Successful()) {
          std::cout << "🎮 Lobby joined successfully! " << lobbyId << std::endl;
        } else {
          std::cerr << "❌ Lobby join failed\n";
        }
      });
    }
  });
});
```

### Lobby join request example

Users can also request to join each other's parties. Use [`Client::SendActivityJoinRequest`] to ask to
join another player's game, and [`Client::SendActivityJoinRequestReply`] to let that player accept the
request.

```cpp
// User A
// 1. Create a lobby with secret
std::string lobbySecret = "foo";
uint64_t USER_A_ID = 286438705638408203;
client->CreateOrJoinLobby(lobbySecret, [&client](discordpp::ClientResult result, uint64_t lobbyId) {
  // 2. Update Rich Presence with a party and join secret to enable invites
  discordpp::Activity activity{};
  activity.SetType(discordpp::ActivityTypes::Playing);
  activity.SetState("In Lobby");

  // Rich Presence party configuration for how many players can join
  discordpp::ActivityParty party{};
  party.SetId("party1234");
  party.SetCurrentSize(1);
  party.SetMaxSize(4);
  activity.SetParty(party);

  // Rich Presence secret is what is shared via invites
  discordpp::ActivitySecrets secrets{};
  secrets.SetJoin(lobbySecret);
  activity.SetSecrets(secrets);

  // This Rich Presence update is what enables the "Ask to Join" button in Discord
  client->UpdateRichPresence(std::move(activity), [&client](discordpp::ClientResult result) {});
});

// User B
// 3. Request to join User A's party
client->SendActivityJoinRequest(USER_A_ID, [](discordpp::ClientResult result) {});

// User A
// 4. Monitor for new invites:
client->SetActivityInviteCreatedCallback([&client](discordpp::ActivityInvite invite) {
  // 5. The game can now show that User A has received a request to join their party
  // If User A is ok with that, they can reply back:
  // Note: invite.type will be ActivityActionTypes::JoinRequest in this example
  client->SendActivityJoinRequestReply(invite, [](discordpp::ClientResult result) {});
});

// User B
// 6. Same as before, user B can monitor for invites
client->SetActivityInviteCreatedCallback([&client](discordpp::ActivityInvite invite) {
  std::cout << "💌 New invite received: " << invite.SenderId() << "\n";
  // 7. When an invite is received, ask the user if they want to accept it.
  // If they choose to do so then go ahead and invoke AcceptActivityInvite
  client->AcceptActivityInvite(invite, [&client](discordpp::ClientResult result, std::string joinSecret) {
    if (result.Successful()) {
      std::cout << "🎮 Invite accepted! Joining lobby...\n";
      // joinSecret came from User A's Rich Presence
      // 5. Join the lobby using the joinSecret
      client->CreateOrJoinLobby(joinSecret, [=](discordpp::ClientResult result, uint64_t lobbyId) {
        // Successfully joined lobby!
        if (result.Successful()) {
          std::cout << "🎮 Lobby joined successfully! " << lobbyId << std::endl;
        } else {
          std::cerr << "❌ Lobby join failed\n";
        }
      });
    }
  });
});
```

[`Client::SendActivityJoinRequest`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#a6c16b1cd68b4a3ce198575a7efb3a87b
[`Client::SendActivityJoinRequestReply`]: https://discord.com/developers/docs/social-sdk/classdiscordpp_1_1Client.html#adb88f1aa7976f4e9bafa8db4e533df07

## Supporting mobile game invites

When a player receives a game invite on mobile, Discord must know how to launch your game. Game
launching is handled through deep linking, which allows Discord to pass the join information to your
game.

### Setting up mobile deep links

1. Configure your deep link URL in the Discord Developer Portal:

- Go to your application's `General` tab
- Enter your game's URL scheme. Any `https://` URL will work here, but for maximum flexibility it
  should be a [Universal Link for
  iOS](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) or an
  [Android App Link](https://developer.android.com/training/app-links).
- Discord will append `/_discord/join?secret=SECRETHERE` to your URL

2. Tell Discord which platforms can accept invites:

```cpp
activity.SetSupportedPlatforms(
    ActivityGamePlatforms.Desktop |  // Enable PC/Mac invites
    ActivityGamePlatforms.IOS |      // Enable iOS invites
    ActivityGamePlatforms.Android    // Enable Android invites
);
```

### How mobile deep links work

1. The user receives and accepts an invite in Discord
2. Discord launches your game using your URL scheme:
   ```
   https://your-universal-app-link.com/_discord/join?secret=the_join_secret_you_set
   ```
3. Your game receives the URL and extracts the join secret
4. Use the secret to connect the player to the session

## Setting a cover image for the invite (optional)

You can set a cover image for an invite via rich presence activity. This image displays as the banner
on the invite and helps draw attention to it. Setting a cover image via rich presence allows you to
dynamically customize invites per rich presence activity; for example, showing different images based
on game mode, map, etc. rather than using the same static image for all invites. If not set, the
banner falls back to the **"Rich Presence Invite Image"** configured in the Developer Portal under the
**"Rich Presence"** tab. Setting an invite cover image is entirely optional.

```cpp
discordpp::ActivityAssets assets;
assets.SetInviteCoverImage("invite-cover-image"); // This example uses an asset key, but you can use an external URL asset for more dynamic cover images.
activity.SetAssets(assets);
```

## Change log — managing game invites

| Date           | Changes                                                               |
| -------------- | --------------------------------------------------------------------- |
| June 10, 2026  | Clarify that launch command registration is local to each machine     |
| June 8, 2026   | Recommend communication scopes; clarify empty invite message behavior |
| March 17, 2025 | initial release                                                       |

---

# Support and bug reports

All three pages close with the same note: join the [Discord Developers
Server](https://discord.gg/discord-developers) and share questions in the `#social-sdk-dev-help`
channel for support from the community. Report Social SDK bugs at
[https://dis.gd/social-sdk-bug-report](https://dis.gd/social-sdk-bug-report).

## What upstream leaves undocumented on these pages

- The full `RelationshipType` enum is never enumerated. The pages name only `Friend`,
  `PendingIncoming`, `PendingOutgoing` and `Blocked`; no complete value list, no numeric values.
- `StatusType` is likewise partial: `Offline` is the only value used in code, with "Online, Offline,
  Idle, etc." in prose.
- The full `ActivityGamePlatforms` enum is not listed. The page says "See the
  `ActivityGamePlatforms` enum for all supported platforms" and shows only `Desktop`, `IOS`,
  `Android`.
- `ActivityActionTypes` is mentioned only through `ActivityActionTypes::JoinRequest` in a code
  comment; the other values are not stated.
- No signatures are given for the relationship methods (`SendGameFriendRequest`,
  `SendGameFriendRequestById`, `AcceptDiscordFriendRequest`, `BlockUser`, and so on) — only the call
  forms shown in the code examples, all of which are reproduced above. The pages link to the C++
  reference on `discord.com/developers/docs/social-sdk/` for signatures.
- No rate limits are stated for relationship or invite operations on these pages.
- `Client::GetRelationshipsByGroup` return type is described only as "a pre-sorted list of
  relationships".
- The invite cover image dimensions and the join secret length limit are not stated.
