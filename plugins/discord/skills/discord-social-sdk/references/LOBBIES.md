# Discord Social SDK — Lobbies

Distilled from `docs.discord.com/developers/discord-social-sdk/development-guides/managing-lobbies`
and `docs.discord.com/developers/resources/lobby` (the REST Lobby resource), retrieved 2026-08-26.

## Contents

- [Overview and prerequisites](#overview-and-prerequisites)
- [Lobby Features and limits](#lobby-features-and-limits)
- [Managing Lobbies (SDK)](#managing-lobbies-sdk)
- [Lobby Lifecycle](#lobby-lifecycle)
- [Sending Messages to a Lobby](#sending-messages-to-a-lobby)
- [Receiving Lobby Messages](#receiving-lobby-messages)
- [Getting Lobby Chat History](#getting-lobby-chat-history)
- [Linked channels, voice and invites](#linked-channels-voice-and-invites)
- [SDK Development Rate Limits](#sdk-development-rate-limits)
- [Lobby REST resource](#lobby-rest-resource)
  - [Lobby Object](#lobby-object)
  - [Lobby Member Object](#lobby-member-object)
  - [Endpoints](#endpoints)
  - [Lobby Message Object](#lobby-message-object)
  - [Lobby Invite Object](#lobby-invite-object)
  - [REST Development Rate Limits](#rest-development-rate-limits)
- [Symbols and change log](#symbols-and-change-log)

---

## Overview and prerequisites

**Warning: this feature is currently available with rate limits.** To increase the rate limits for
your game, follow CORE-CONCEPTS.md → Applying for Increased Rate Limits.

Lobbies are **groups of users that can communicate via text and voice**.

Prerequisites: set up the Discord Social SDK with a Getting Started guide.

**Warning: to utilize this communication feature, you must enable
`Client::GetDefaultCommunicationScopes` in your OAuth Scope configuration** (i.e. the
`sdk.social_layer` scope). See CORE-CONCEPTS.md → OAuth2 Scopes.

---

## Lobby Features and limits

Users can be **in multiple lobbies at once**. A lobby can also have **metadata (an arbitrary JSON
blob)** associated with the lobby and each user.

### Lobby Members

- **Lobbies may have a maximum of 1,000 members.**
- **Each user may have a maximum of 100 lobbies per game.**
- If your game needs more than 1,000 members in a lobby, contact Discord to discuss your use case.

### Text Chat

Lobbies have a text chat channel that all members can use to communicate. Messages are sent to all
members of the lobby.

### Voice Chat

Lobbies support voice calls. **Although a lobby is allowed to have 1,000 members, you should not start
voice calls in lobbies that large.** Discord recommends **around 25 members or fewer for voice
calls**; contact Developer Support if you need more than 25-member calls.

---

## Managing Lobbies (SDK)

There are two ways to manage lobbies:

1. From your server using the Discord API.
2. From the client using the `Client::CreateOrJoinLobby` function.

### Server-Side Lobby Management

You can use the Discord HTTP API to create, update, and delete lobbies and manage lobby membership.
See [Lobby REST resource](#lobby-rest-resource) below for the endpoints, and HOW-TO-GUIDES.md → Use
with Discord APIs for how to authenticate your requests.

**Warning: clients will not be able to use `Client::CreateOrJoinLobby`,
`Client::CreateOrJoinLobbyWithMetadata`, or `Client::LeaveLobby` with lobbies created using the
API.**

### Client-Side Lobby Management

The SDK client can also create and join lobbies. **This works by associating a secret value with the
lobby.** You can distribute this secret as necessary, and holders can then join the lobby using that
secret. **If the lobby does not exist, it will be created on demand.**

- The relevant SDK functions are `Client::CreateOrJoinLobby` and `Client::LeaveLobby`.
- **Lobby secrets are unique per game (i.e. application).** For example, use a new secret if you want
  to generate a new lobby at the end of the match. Calling `Client::LeaveLobby` and then
  `Client::CreateOrJoinLobby` with the same secret value will just re-add you to the same lobby.
- **Calling `Client::CreateOrJoinLobby` while the user is already in the lobby will update their
  metadata (if included) instead.**
- **Discord's Rich Presence system supports syncing this secret**, too. Using this flow, clients can
  request to join another user's activity. When approved, the SDK will be given the secret, which you
  can access and join the associated lobby if you choose to do so. See
  [Creating Lobby Invites](#linked-channels-voice-and-invites).
- To keep track of metadata for the lobby or the lobby members, use
  `Client::CreateOrJoinLobbyWithMetadata`. This function takes a JSON object as an argument, which
  will be stored with the lobby and the lobby members. **This metadata can be retrieved using the
  `discordpp::Client::GetLobbyHandle` function.**

```cpp
// Create or join a lobby from the client
client->CreateOrJoinLobby("your-unique-lobby-secret",[client](discordpp::ClientResult result, uint64_t lobbyId) {
  if(result.Successful()) {
    std::cout << "🎮 Lobby created or joined successfully! Lobby Id: " << lobbyId << std::endl;
  } else {
    std::cerr << "❌ Lobby creation/join failed\n";
  }
});
```

### Leaving a Lobby

To remove a user from a lobby, use `Client::LeaveLobby`. **Only lobbies created with
`Client::CreateOrJoinLobby` can be left using `Client::LeaveLobby`.**

```cpp
uint64_t lobbyId = 01234567890;

// Leaving a lobby from the client
client->LeaveLobby(lobbyId, [&](discordpp::ClientResult result) {
  if(result.Successful()) {
    std::cout << "🎮 Left lobby successfully! Lobby Id: " << lobbyId << std::endl;
  } else {
    std::cerr << "❌ Leaving lobby failed\n";
  }
}
```

(The closing `);` is missing in upstream's snippet; reproduced verbatim.)

---

## Lobby Lifecycle

Lobbies are **intended to be ephemeral** and should be cleaned up when the game/match/area/world is no
longer needed. To support this, you can set a **"max idle time"**: if a lobby sits idle, with no one
connected to it at all, for more than that time, Discord automatically deletes the lobby. As long as
one person is connected, the lobby won't be deleted (and the timer resets too).

- **This value defaults to 5 minutes.**
- **The maximum value for this "idle time" will likely be 7 days** — the lobby only gets deleted if no
  one connects to it for an entire week. This gives a good amount of permanence to lobbies when needed,
  but there may be rare cases where a lobby does need to be "rebuilt" if everyone is offline for an
  extended period. (The REST API expresses this as `idle_timeout_seconds`, valid **5 to 604800**.)

**Additional limitation for client-created lobbies:** lobbies created by the SDK client using
`Client::CreateOrJoinLobby` have the **"secret" value expire after 30 days** — the lobby will still
exist, but new users won't be able to join the lobby after that.

---

## Sending Messages to a Lobby

Once you have a lobby created, lobby members can send messages using `Client::SendLobbyMessage`.
**Clients can send messages to lobbies they are members of regardless of whether they joined the lobby
using the client or server-side method.**

```cpp
uint64_t lobbyId = 01234567890;

client->SendLobbyMessage(lobbyId, "Hello", [](discordpp::ClientResult result, uint64_t messageId) {
  if(result.Successful()) {
    std::cout << "📨 Message sent successfully!\n";
  } else {
    std::cerr << "❌ Message sending failed\n";
  }
});
```

---

## Receiving Lobby Messages

Use `Client::SetMessageCreatedCallback`. **This callback fires whenever a new message is received in a
lobby or a DM.** From the `messageId`, you can fetch the `MessageHandle` and then the `ChannelHandle`
to determine the location to which the message was sent.

```cpp
client->SetMessageCreatedCallback([&client](uint64_t messageId) {
  discordpp::MessageHandle message = client->GetMessageHandle(messageId);
  std::cout << "📨 New message received: " << message->Content() << "\n";
});
```

---

## Getting Lobby Chat History

Retrieve previous messages with `Client::GetLobbyMessagesWithLimit`. The function takes a lobby ID and
a limit parameter.

**Important limitations:**

- **Only a maximum of 200 messages and up to 72 hours of history can be retrieved.**
- **Only messages from lobbies the user is currently a member of can be retrieved.**

```cpp
const uint64_t lobbyId = 01234567890;
const uint32_t messageLimit = 50; // Number of recent messages to retrieve (max 200)

client->GetLobbyMessagesWithLimit(
  lobbyId, messageLimit,
  [](const discordpp::ClientResult &result, const std::vector<discordpp::MessageHandle> &messages) {
    if (result.Successful()) {
      std::cout << "? Retrieved " << messages.size()
                << " messages from lobby chat history!\n";

      // Process the messages (they are returned in chronological order)
      for (const auto &message : messages) {
        std::cout << "Message: " << message.Content() << std::endl;
      }
    } else {
      std::cerr << "? Failed to retrieve lobby chat history\n";
    }
  });
```

The messages are returned as a list of `MessageHandle` objects, **ordered chronologically from oldest
to newest**. Each `MessageHandle` contains the message content, author information, and timestamp.

Particularly useful for:

- Displaying recent chat when a user joins a lobby
- Implementing chat history scrollback features
- Preserving conversation context across game sessions

---

## Linked channels, voice and invites

- **Linking a Channel to Lobby.** You can connect a lobby to a Discord text channel with Linked
  Channels, letting users chat with the lobby using Discord even if they are not in the game. See
  MESSAGING.md → Linked Channels.
- **Managing Voice Chat.** See VOICE-CHAT.md for how to start a voice call in a lobby.
- **Creating Lobby Invites.** Your game can use lobbies and game invites to allow users to invite
  friends to join an existing lobby. See RELATIONSHIPS-AND-FRIENDS.md → Using Game Invites with
  Lobbies.
- **Voice Muting Based on Player Blocks.** Locally mute players in lobby voice calls based on block
  relationships — see VOICE-CHAT.md.

---

## SDK Development Rate Limits

Applications without increased rate limits for production releases are subject to the following
**application-wide** limits:

| Operation | Limit |
| --- | --- |
| `Client::CreateOrJoinLobby` | 100 per 2 hours |
| `Client::LinkChannelToLobby` | 20 per 2 hours |
| `Client::UnlinkChannelFromLobby` | 20 per 2 hours |
| `Client::SendLobbyMessage` | 100 per 2 hours |

**These are per-application rate limits, not per-user.** For detecting and retrying rate-limited
requests in the SDK, see HOW-TO-GUIDES.md → Handle Rate Limits.

---

## Lobby REST resource

Source: `docs.discord.com/developers/resources/lobby`. API base `https://discord.com/api/v10`.

### Lobby Object

Represents a lobby within Discord.

**Lobby Structure**

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | the id of this channel |
| application_id | snowflake | application that created the lobby |
| metadata | ?dict\<string, string> | dictionary of string key/value pairs. The max total length is 1000. |
| members | array of lobby member objects | members of the lobby |
| linked_channel? | channel object | the guild channel linked to the lobby |

### Lobby Member Object

Represents a member of a lobby, including optional metadata and flags.

**Lobby Member Structure**

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | the id of the user |
| metadata? | ?dict\<string, string> | dictionary of string key/value pairs. The max total length is 1000. |
| flags? | integer | lobby member flags combined as a bitfield |
| additional_name? | string | an additional 1-80 character display name for the member, such as an in-game character name. Can only be set via *Add a Member to a Lobby* or *Bulk Update Lobby Members*. Accessible via the Social SDK with `MessageHandle::AdditionalName` |

**Lobby Member Flags**

| Flag | Value | Description |
| --- | --- | --- |
| CanLinkLobby | `1<<0` | user can link a text channel to a lobby |

**Example Lobby Object**

```json
{
  "id": "96008815106887111",
  "application_id": "41771983429993937",
  "metadata": {
    "topic": "we need more redstone"
  },
  "members": [
    {
      "id": "41771983429993000",
      "metadata": null,
      "flags": 1,
      "additional_name": "Twindly Shimmerleaf"
    }
  ]
}
```

### Endpoints

#### POST /lobbies

**Create Lobby.** Creates a new lobby, adding any of the specified members to it, if provided. Returns
a lobby object.

**Discord Social SDK clients will not be able to join or leave a lobby created using this API**, such
as with `Client::CreateOrJoinLobby`.

JSON Params:

| Field | Type | Description |
| --- | --- | --- |
| metadata? | ?dict\<string, string> | optional dictionary of string key/value pairs. The max total length is 1000. |
| members? | array of lobby member objects | optional array of up to 25 users to be added to the lobby |
| idle_timeout_seconds? | integer | seconds to wait before shutting down a lobby after it becomes idle. Value can be between 5 and 604800 (7 days). See `LobbyHandle` for more details on this behavior. |

Lobby Member JSON Params:

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | Discord user id of the user to add to the lobby |
| metadata? | ?dict\<string, string> | optional dictionary of string key/value pairs. The max total length is 1000. |
| flags? | integer | lobby member flags combined as a bitfield |

#### PUT /lobbies

**Create or Join Lobby.** Creates a new lobby for the application identified by a `secret`, or joins
the calling user to the existing lobby with that secret if one already exists. Updates lobby metadata
and the calling member's metadata on join.

**Uses `Bearer` token for authorization with the `sdk.social_layer` scope.** Returns a lobby object.

JSON Params:

| Field | Type | Description |
| --- | --- | --- |
| secret | string | secret used to identify the lobby. If a lobby for this application already exists with this secret, the caller joins it; otherwise a new lobby is created. **Max 250 characters.** |
| idle_timeout_seconds? | integer | seconds to wait before shutting down a lobby after it becomes idle. Value can be between 5 and 604800 (7 days). See `LobbyHandle` for more details on this behavior. |
| lobby_metadata? | ?dict\<string, string> | optional dictionary of string key/value pairs to set on the lobby. The max total length is 1000. **Overwrites any existing lobby metadata.** |
| member_metadata? | ?dict\<string, string> | optional dictionary of string key/value pairs to set on the calling user's lobby member. The max total length is 1000. |

#### GET /lobbies/{lobby.id}

**Get Lobby.** Returns a lobby object for the specified lobby id, if it exists.

#### PATCH /lobbies/{lobby.id}

**Modify Lobby.** Modifies the specified lobby with new values, if provided. Returns the updated lobby
object.

JSON Params:

| Field | Type | Description |
| --- | --- | --- |
| metadata? | ?dict\<string, string> | optional dictionary of string key/value pairs. The max total length is 1000. **Overwrites any existing metadata.** |
| members? | array of lobby member objects | optional array of up to 25 users to replace the lobby members with. **If provided, lobby members not in this list will be removed from the lobby.** |
| idle_timeout_seconds? | integer | seconds to wait before shutting down a lobby after it becomes idle. Value can be between 5 and 604800 (7 days). See `LobbyHandle` for more details on this behavior. |

#### DELETE /lobbies/{lobby.id}

**Delete Lobby.** Deletes the specified lobby if it exists. **It is safe to call even if the lobby is
already deleted.** Returns nothing.

#### PUT /lobbies/{lobby.id}/members/{user.id}

**Add a Member to a Lobby.** Adds the provided user to the specified lobby. **If called when the user
is already a member of the lobby, it will update fields such as metadata on that user instead.**
Returns the lobby member object.

JSON Params:

| Field | Type | Description |
| --- | --- | --- |
| metadata? | ?dict\<string, string> | optional dictionary of string key/value pairs. The max total length is 1000. |
| flags? | integer | lobby member flags combined as a bitfield |
| additional_name? | ?string | an additional display name for the member, such as an in-game character name. 1-80 characters. **Omit the field to preserve the member's current value, or send `null` to clear it.** |

#### POST /lobbies/{lobby.id}/members/bulk

**Bulk Update Lobby Members.** Adds, updates, or removes **up to 25 members** from the specified lobby
in a single request. Members with `remove_member: false` (the default) are **upserted** — added if not
present, or updated with the provided metadata and flags if already a member. Members with
`remove_member: true` are removed.

Returns an array of lobby member objects **for the upserted members. Removed members are not included
in the response.**

**Users unknown to Discord will return a 404 `UNKNOWN_USER` error. Users that fail permission checks
or who have already reached the maximum number of lobbies per application (and are not already a
member of this lobby) are silently dropped from the upsert set.**

JSON Params: an array of member objects, **minimum 1, maximum 25**.

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | Discord user id of the user to add, update, or remove |
| metadata? | ?dict\<string, string> | optional dictionary of string key/value pairs. The max total length is 1000. |
| flags? | integer | lobby member flags combined as a bitfield |
| additional_name? | ?string | an additional display name for the member, such as an in-game character name. 1-80 characters. Omit the field to preserve the member's current value, or send `null` to clear it. |
| remove_member? | boolean | if `true`, the user is removed from the lobby instead of upserted. Default `false`. |

#### DELETE /lobbies/{lobby.id}/members/{user.id}

**Remove a Member from a Lobby.** Removes the provided user from the specified lobby. **Safe to call
even if the user is no longer a member of the lobby, but will fail if the lobby does not exist.**
Returns nothing.

#### DELETE /lobbies/{lobby.id}/members/@me

**Leave Lobby.** Removes the current user from the specified lobby. Safe to call even if the user is
no longer a member, but fails if the lobby does not exist. **Uses `Bearer` token for authorization.**
Returns nothing.

#### PATCH /lobbies/{lobby.id}/channel-linking (link)

**Link Channel to Lobby.** Links an existing text channel to a lobby.

**Uses `Bearer` token for authorization and user must be a lobby member with the `CanLinkLobby` lobby
member flag.** Returns a lobby object with a linked channel.

JSON Params:

| Field | Type | Description |
| --- | --- | --- |
| channel_id? | snowflake | the id of the channel to link to the lobby. **If not provided, will unlink any currently linked channels from the lobby.** |

#### PATCH /lobbies/{lobby.id}/channel-linking (unlink)

**Unlink Channel from Lobby.** Unlinks any currently linked channels from the specified lobby. **Send
a request to this endpoint with an empty body.**

Uses `Bearer` token for authorization and user must be a lobby member with the `CanLinkLobby` lobby
member flag. Returns a lobby object without a linked channel.

(Same path and method as the link operation — the distinction is the presence of `channel_id`.)

#### POST /lobbies/{lobby.id}/messages

**Send Lobby Message.** Sends a message to the specified lobby. **The calling user must be a member of
the lobby.**

**Uses `Bearer` token for authorization with the `sdk.social_layer` scope.** Returns the created lobby
message object.

**If the lobby has a linked channel, the message is also forwarded to that channel. If forwarding
fails (for example, due to AutoMod), the lobby message is still delivered to other lobby members.**

JSON Params:

| Field | Type | Description |
| --- | --- | --- |
| content | string | message content. **Must be non-empty.** |
| metadata? | ?dict\<string, string> | optional dictionary of string key/value pairs delivered alongside the message to active clients via the Social SDK. **Not persisted on the linked channel message.** |
| flags? | integer | optional message flags combined as a bitfield. **Only flags creatable by the Social SDK are accepted.** |

#### GET /lobbies/{lobby.id}/messages

**Get Lobby Messages.** Returns the most recent messages in the specified lobby. The calling user must
be a member of the lobby.

Uses `Bearer` token for authorization with the `sdk.social_layer` scope. Returns an array of lobby
message objects.

Query Params:

| Field | Type | Description |
| --- | --- | --- |
| limit? | integer | max number of messages to return (**1-200**). **Defaults to 50.** |

#### PUT /lobbies/{lobby.id}/messages/{message.id}/moderation-metadata

**Update Lobby Message Moderation Metadata.** Sets the moderation metadata for a lobby message. **The
metadata is app-scoped and delivered to active game clients via the Social SDK as a realtime message
update.** See HOW-TO-GUIDES.md → Integrate Moderation for the full moderation flow.

**Uses `Bot` token for authorization.** Returns `HTTP 204: No Content` on success.

JSON Params:

| Field | Type | Description |
| --- | --- | --- |
| `*` | string | Free-form key–value pairs describing the moderation decision. **Up to 5 keys; key length ≤ 1024 characters; value length ≤ 2000 characters.** |

#### POST /lobbies/{lobby.id}/members/@me/invites

**Create Lobby Channel Invite for Self.** Creates a **single-use** guild invite to the lobby's linked
channel, targeted at the calling user. **The lobby must have a linked channel and the caller must be a
member of the lobby. The invite expires after one hour.**

Uses `Bearer` token for authorization with the `sdk.social_layer` scope. Returns a lobby invite
object.

#### POST /lobbies/{lobby.id}/members/{user.id}/invites

**Create Lobby Channel Invite for User.** Creates a **single-use** guild invite to the lobby's linked
channel on behalf of an application, targeted at the specified user. **The lobby must have a linked
channel. The invite expires after one hour.**

**Uses `Bot` token for authorization.** Returns a lobby invite object.

### Lobby Message Object

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | id of the message |
| type | integer | message type (see the Message resource's message types) |
| content | string | message content |
| lobby_id | snowflake | id of the lobby this message was sent to |
| channel_id | snowflake | included for compatibility with the messages interface; **equal to `lobby_id`** |
| author | user object | the user who sent the message |
| lobby_member? | object | contains a single `additional_name` string — the author's lobby member additional display name, **captured when the message was sent**. Omitted if the author had no `additional_name` set. |
| metadata? | ?dict\<string, string> | dispatch-only metadata sent with the message |
| moderation_metadata? | ?dict\<string, string> | moderation metadata set via *Update Lobby Message Moderation Metadata* |
| flags | integer | message flags bitfield |
| application_id | snowflake | the application that sent the message |

### Lobby Invite Object

| Field | Type | Description |
| --- | --- | --- |
| code | string | the invite code for the lobby's linked channel |

### REST Development Rate Limits

Applications without increased rate limits for production releases are subject to the following
**application-wide development limits**:

| Endpoint | Limit |
| --- | --- |
| `POST /lobbies` | 100 per 2 hours |
| `PUT /lobbies` | 100 per 2 hours |
| `PATCH /lobbies/{lobby.id}` | 100 per 2 hours |
| `PUT /lobbies/{lobby.id}/members/{user.id}` | 100 per 2 hours |
| `DELETE /lobbies/{lobby.id}/members/{user.id}` | 100 per 2 hours |
| `POST /lobbies/{lobby.id}/members/bulk` | 100 per 2 hours |
| `POST /lobbies/{lobby.id}/members/@me/invites` | 100 per 2 hours |
| `POST /lobbies/{lobby.id}/members/{user.id}/invites` | 100 per 2 hours |
| `PATCH /lobbies/{lobby.id}/channel-linking` | 20 per 2 hours |
| `POST /lobbies/{lobby.id}/messages` | 100 per 2 hours |

**These are per-application rate limits, not per-user.**

---

## Symbols and change log

Doxygen anchors, base `https://discord.com/developers/docs/social-sdk/`:

| Symbol | Anchor |
| --- | --- |
| `ChannelHandle` | `classdiscordpp_1_1ChannelHandle.html#ac32096b2ef15c5c220e9b7b92253cc46` |
| `Client::CreateOrJoinLobby` | `classdiscordpp_1_1Client.html#a8b4e195555ecaa89ccdfc0acd28d3512` |
| `Client::CreateOrJoinLobbyWithMetadata` | `classdiscordpp_1_1Client.html#a5c84fa76c73cf3c0bfd68794ca5595c1` |
| `Client::GetLobbyMessagesWithLimit` | `classdiscordpp_1_1Client.html#a0586192e85caf548b8b321f1cb21301f` |
| `Client::LeaveLobby` | `classdiscordpp_1_1Client.html#a8c78f797240b35d721383461a2e62926` |
| `Client::LinkChannelToLobby` | `classdiscordpp_1_1Client.html#a3114d58d50d4d2cb5752d95e121315d4` |
| `Client::SendLobbyMessage` | `classdiscordpp_1_1Client.html#a779e0483f51dc99f0db3dd761d22ab6f` |
| `Client::SetMessageCreatedCallback` | `classdiscordpp_1_1Client.html#a28325a8e8c688a84ac851da4bc86e148` |
| `Client::UnlinkChannelFromLobby` | `classdiscordpp_1_1Client.html#a28f78a6fe46eb11eb54ee9b53fa94ffe` |
| `MessageHandle` | `classdiscordpp_1_1MessageHandle.html#ae25595b43bc74b0c4c92c5165d16382f` |
| `MessageHandle::AdditionalName` | `classdiscordpp_1_1MessageHandle.html#aed26c7506b01e735710530dac5eddb6e` |
| `LobbyHandle` | `classdiscordpp_1_1LobbyHandle.html#a04cebab69ab0e7fb930346a14a87e843` |
| `Client::GetDefaultCommunicationScopes` | `classdiscordpp_1_1Client.html#a71499da752fbdc2d4326ae0fd36c0dd1` |

Also referenced without a linked anchor: `Client::GetLobbyHandle`, `Client::GetMessageHandle`,
`MessageHandle::Content`, `ClientResult`.

**Change Log (Creating and Managing Lobbies):**

| Date           | Changes                          |
| -------------- | -------------------------------- |
| June 30, 2025  | Add communications scope warning |
| March 17, 2025 | initial release                  |

The `resources/lobby` page carries no change log.
