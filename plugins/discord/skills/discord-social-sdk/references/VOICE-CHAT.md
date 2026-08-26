# Discord Social SDK — Voice Chat

Distilled from `docs.discord.com/developers/discord-social-sdk/development-guides/managing-voice-chat`
and `.../how-to/voice-muting-for-blocked-players`, retrieved 2026-08-26.

## Contents

- [Managing Voice Chat](#managing-voice-chat)
  - [Prerequisites](#prerequisites)
  - [Starting and Joining Voice Calls](#starting-and-joining-voice-calls)
  - [Controlling Voice Features](#controlling-voice-features)
  - [Detecting No Audio Input](#detecting-no-audio-input)
  - [Noise Suppression & Cancellation](#noise-suppression--cancellation)
  - [Advanced Audio Processing](#advanced-audio-processing)
  - [Ending Voice Calls](#ending-voice-calls)
  - [Checking Lobby Voice Call Status](#checking-lobby-voice-call-status)
  - [Diagnosing Audio Issues](#diagnosing-audio-issues)
- [Voice Muting Based on Player Blocks](#voice-muting-based-on-player-blocks)
  - [Why Voice Muting Must Be Handled Explicitly](#why-voice-muting-must-be-handled-explicitly)
  - [Step 1: Populate the Mute List](#step-1-populate-the-mute-list)
  - [Step 2: Apply the Mute List](#step-2-apply-the-mute-list)
  - [Best Practices](#best-practices)
- [Symbols and change logs](#symbols-and-change-logs)

---

## Managing Voice Chat

Source: `/development-guides/managing-voice-chat`.

**Warning: this feature is currently available with rate limits.** To increase the rate limits for your
game, follow CORE-CONCEPTS.md → Applying for Increased Rate Limits.

Voice calls are a core feature of the Discord Social SDK that enable **real-time voice communication
between players in your game within lobbies**. This guide covers:

- Start and join voice calls in lobbies
- Control voice settings like mute, deafen, and volume
- Process audio data with custom callbacks
- Integrate with external audio systems
- Check voice call status and participant states

### Prerequisites

**Warning: to utilize this communication feature, you must enable
`Client::GetDefaultCommunicationScopes` in your OAuth Scope configuration.**

**1. Lobby Management. Voice calls require an active lobby with participants.** You must:

1. **Create or join a lobby** using the Discord Social SDK
2. **Add players to the lobby** — voice calls only work with lobby members

See LOBBIES.md for creating lobbies, joining lobbies, and managing lobby members.

**2. Lobby Size Limitations.** While Discord lobbies technically support up to **1,000 members**,
**voice calls should be limited to much smaller groups**. Discord **strongly recommends keeping voice
calls to 25 members or fewer** for optimal performance and user experience.

### Starting and Joining Voice Calls

**Both operations use the same functions whether you're creating something new or joining something
that already exists.**

```cpp
// First, create or join a lobby using a shared secret
const std::string lobbySecret = "my-game-lobby-secret";

client->CreateOrJoinLobby(lobbySecret, [client](const discordpp::ClientResult& result, uint64_t lobbyId) {
    if (result.Successful()) {
        std::cout << "🎮 Successfully joined lobby!" << std::endl;

        // Now start or join the voice call in this lobby
        // StartCall returns a Call object but has no callback
        const auto call = client->StartCall(lobbyId);

        // StartCall returns null if user is already in this voice channel
        if (call) {
          std::cout << "🎤 Voice call operation initiated..." << std::endl;
        } else {
          std::cout << "ℹ️ Already in this voice channel" << std::endl;
        }

    } else {
        std::cerr << "❌ Failed to join lobby: " << result.Error() << std::endl;
    }
});
```

#### How It Works

Both `Client::CreateOrJoinLobby` and `Client::StartCall` handle existing and new scenarios
automatically:

- **`Client::CreateOrJoinLobby`**: if a lobby with the given secret already exists, you'll join it. If
  not, a new lobby is created with that secret.
- **`Client::StartCall`**: if a voice call is already active in the lobby, you'll join it. If not, a new
  voice call is started. **It returns a `Call` object but has no callback, and returns null if the user
  is already in this voice channel.**

**You don't need to check if a lobby exists or if a call is already ongoing.** The SDK handles both
scenarios seamlessly.

### Controlling Voice Features

The SDK provides voice control options **at both the individual call level and globally across all
calls**.

#### Global Voice Controls

These methods control voice settings across **all active calls** using the `Client` object:

- **`Client::SetSelfMuteAll`** — mutes your microphone across all active calls
- **`Client::SetSelfDeafAll`** — deafens you across all active calls
- **`Client::SetInputVolume`** — sets microphone volume
- **`Client::SetOutputVolume`** — sets speaker volume

#### Per-Call Voice Controls

These methods control voice settings for a **specific call** using the `Call` object:

- **`Call::SetSelfMute`** — mutes your microphone so other participants in this call cannot hear you
- **`Call::SetSelfDeaf`** — mutes all audio from this call so you cannot hear other participants, **and
  they cannot hear you either**
- **`Call::SetParticipantVolume`** — adjusts the volume of a specific participant

#### Voice Activity Detection

Use **`Call::SetVADThreshold`** to control voice activation detection sensitivity. This allows optional
fine-tuning of when the system considers someone to be speaking.

```cpp
// Per-call controls (assuming you have a Call object)
uint64_t lobbyId = 123456789;  // Your lobby ID
auto call = client->GetCall(lobbyId);
if (call) {
    call.SetSelfMute(true);           // Mute in this call only
    call.SetSelfDeaf(false);          // Unmute audio in this call
    call.SetParticipantVolume(userId, 150.0f);  // Increase participant volume
    call.SetVADThreshold(false, -30.0f);       // Set custom voice detection threshold
}

// Global controls
client->SetSelfMuteAll(true);          // Mute across all calls
client->SetInputVolume(75.0f);         // Set microphone to 75%
client->SetOutputVolume(120.0f);       // Increase speaker volume to 120%
```

Note the observed shapes: volumes are floats on a 100-based percentage scale (values above 100 are
allowed, e.g. `120.0f`), `SetVADThreshold` takes `(bool, float)`, and `Client::GetCall(lobbyId)`
retrieves an existing call.

### Detecting No Audio Input

**The SDK can notify you when no audio is reaching the microphone** — for example, when a user's mic is
broken, muted at the OS level, or the wrong input device is selected. This lets your game surface a
"your mic appears silent" hint instead of leaving the user to wonder why nobody can hear them.

- **`Client::SetNoAudioInputThreshold`** — dBFS threshold for what counts as "no input". **Range
  `[-100.0, 100.0]`, defaults to `-100.0` (detection disabled).** Set to something like `-60.0` to
  enable.
- **`Client::SetNoAudioInputCallback`** — receives a **`bool inputDetected`** whenever the mic crosses
  the threshold (silent → active or active → silent).

```cpp
// Enable detection at -60 dBFS
client->SetNoAudioInputThreshold(-60.0f);

client->SetNoAudioInputCallback([](bool inputDetected) {
    if (!inputDetected) {
        // Show a UI hint: "Your mic appears silent — check your device settings."
    } else {
        // Mic is receiving audio again; clear the hint.
    }
});
```

### Noise Suppression & Cancellation

The SDK provides **two tiers of microphone audio processing**: a set of WebRTC-based defaults that are
always on, and an optional **Krisp**-powered noise cancellation for higher-quality results.

**Krisp delivers higher-quality noise cancellation, but ships extra libraries and model files that
increase your installation size.** If size is a constraint — for example on mobile — see
[Excluding Krisp](#excluding-krisp-to-reduce-installation-size) for how to ship with only the WebRTC
defaults.

#### Default Audio Processing (WebRTC)

**These three processors ship with every build and default to on.** They use the WebRTC library's
standard audio pipeline:

- **`Client::SetNoiseSuppression`** — suppresses steady background noise (e.g. fans, keyboards, room
  tone). **Defaults to on.**
- **`Client::SetEchoCancellation`** — removes echo from speakers being picked up by the mic. **Defaults
  to on.**
- **`Client::SetAutomaticGainControl`** — automatically normalizes microphone volume for clarity and
  consistency. **Defaults to on.**

```cpp
// Toggle individual WebRTC processors from a voice settings UI
client->SetNoiseSuppression(true);
client->SetEchoCancellation(true);
client->SetAutomaticGainControl(true);
```

#### Advanced Noise Cancellation (Krisp)

**`Client::SetNoiseCancellation`** enables **Krisp**, a noise cancellation technology that removes a
much wider range of background sounds (e.g. typing, dogs barking, traffic) than the WebRTC
suppression. **It defaults to off.**

**Krisp and WebRTC noise suppression are mutually exclusive. Enabling
`Client::SetNoiseCancellation` automatically disables `Client::SetNoiseSuppression`** — you don't need
to turn it off yourself.

```cpp
// Enable Krisp noise cancellation
client->SetNoiseCancellation(true);
```

#### Excluding Krisp to Reduce Installation Size

Krisp ships as additional libraries and model files alongside the core SDK, which adds to your
installation size. If you're optimizing for size — for example on mobile — you can ship without Krisp
and rely on the WebRTC noise suppression instead.

**To exclude Krisp from your distribution, remove all `.kef` and `.kw` files along with any file or
directory whose name contains `krisp`** (for example `discord_krisp.dll`,
`libdiscord_krisp.dylib`, `discord_partner_sdk_krisp.aar`, and
`discord_partner_sdk_krisp.xcframework`).

### Advanced Audio Processing

#### Manipulating Voice Data with Callbacks

For advanced audio processing needs, use **`Client::StartCallWithAudioCallbacks`** to access raw audio
data. This enables real-time audio manipulation and integration with external audio processing
systems.

#### In-Place Audio Modification

To directly modify incoming audio samples (e.g., volume dampening):

```cpp
const auto call = client->StartCallWithAudioCallbacks(
    lobbyId,
    [](uint64_t userId, int16_t *data, const size_t samplesPerChannel,
       int sampleRate, const size_t channels,
       bool &outShouldMuteData) {
      // Dampen volume of incoming audio by modifying data's samples
      // in-place
      for (int i = 0; i < samplesPerChannel * channels; i++) {
        data[i] *= 0.5; // Reduce volume by 50%
      }
    },
    [](int16_t *data, uint64_t samplesPerChannel, int32_t sampleRate,
       uint64_t channels) {});

```

So the signature is `StartCallWithAudioCallbacks(lobbyId, receivedCallback, capturedCallback)` where
the received callback is
`(uint64_t userId, int16_t* data, size_t samplesPerChannel, int sampleRate, size_t channels, bool& outShouldMuteData)`
and the second callback is
`(int16_t* data, uint64_t samplesPerChannel, int32_t sampleRate, uint64_t channels)`.

#### External Audio Pipeline Integration

To route audio to external processing systems such as **FMOD** (`https://www.fmod.com/`) or **Wwise**
(`https://www.audiokinetic.com/en/wwise/overview/`):

```cpp
const auto call = client->StartCallWithAudioCallbacks(lobbyId,
    [](uint64_t userId, int16_t* data, size_t samplesPerChannel,
       int sampleRate, size_t channels, bool& outShouldMuteData) {
        // Prevent Discord from playing the audio directly
        outShouldMuteData = true;

        const int totalNumSamples = samplesPerChannel * channels;
        // Send audio data to your external audio system
        SendAudioToExternalAudioSystem(data, totalNumSamples);
    },
    [](int16_t *data, uint64_t samplesPerChannel, int32_t sampleRate,
       uint64_t channels) {});
```

#### Key Audio Processing Points

1. **Direct Manipulation**: the `data` parameter in `Client::UserAudioReceivedCallback` can be modified
   in-place to alter incoming audio samples.
2. **External Processing**: set **`outShouldMuteData = true`** to prevent Discord from playing audio
   directly, allowing you to handle it through your own audio pipeline.
3. **No Encoding Required**: the SDK handles all voice encoding/decoding automatically — you work with
   raw audio samples.

### Ending Voice Calls

**End a Call For a Specific Lobby:**

```cpp
uint64_t lobbyId = 123456789;  // Your lobby ID
client->EndCall(lobbyId, []() {
    std::cout << "🔇 Call ended successfully" << std::endl;
});
```

**End All Calls:**

```cpp
client->EndCalls([]() {
    std::cout << "🔇 All calls ended successfully" << std::endl;
});
```

Both `Client::EndCall` and `Client::EndCalls` take a completion callback with no arguments.

### Checking Lobby Voice Call Status

You may want to check the voice call status for your lobby to display UI indicators, monitor
participant activity, or provide information to players.

#### Checking if a Call is Active

Use **`LobbyHandle::GetCallInfoHandle()`**:

```cpp
// Check if there's an active call in the lobby
const auto callInfoHandle = lobby->GetCallInfoHandle();
if (callInfoHandle) {
  // There's an active call - you can join it or get participant
  // info
  const auto participants = callInfoHandle->GetParticipants();
  std::cout << "Active call with " << participants.size()
            << " participants" << std::endl;
} else {
  // No active call in this lobby
  std::cout << "No active voice call in this lobby" << std::endl;
}

```

#### Checking Individual Participant Status

For each participant in a voice call, check their voice state using **`VoiceStateHandle`**:

```cpp
// Get voice state information for participants
const auto callInfo = lobby->GetCallInfoHandle();
if (callInfo) {
  const auto participants = callInfo->GetParticipants();

  for (const auto &participantId : participants) {
    const auto voiceState = callInfo->GetVoiceStateHandle(participantId);
    if (voiceState) {
      const bool isMuted = voiceState->SelfMute();
      const bool isDeafened = voiceState->SelfDeaf();

      std::cout << "Participant " << participantId
                << " - Muted: " << (isMuted ? "Yes" : "No")
                << ", Deafened: " << (isDeafened ? "Yes" : "No")
                << std::endl;
    }
  }
}

```

#### Voice State Information Available

`VoiceStateHandle` provides these key details about each participant:

- **`VoiceStateHandle::SelfMute`**: returns `true` if the user has muted themselves (others cannot hear
  them)
- **`VoiceStateHandle::SelfDeaf`**: returns `true` if the user has deafened themselves (they cannot hear
  others **and others cannot hear them**)

Particularly useful for:

- Displaying voice indicators in your UI
- Implementing voice-related features or debugging audio issues

The call-info type also exposes `GetParticipants()` and `GetVoiceStateHandle(participantId)`.

### Diagnosing Audio Issues

If users report echo, feedback, or other audio quality problems, the SDK offers dedicated tooling for
capturing voice and audio diagnostics. See HOW-TO-GUIDES.md → Debug & Log:

- **Voice Logging** — capture logs from the voice subsystem and underlying WebRTC layer.
- **Audio Logging** — record input/output waveforms to disk for offline analysis.

---

## Voice Muting Based on Player Blocks

Source: `/how-to/voice-muting-for-blocked-players`.

This guide explains how to mute players in a lobby voice call based on block relationships — whether
those blocks come from Discord's own relationship system or from an external source such as your game
or platform backend. It helps you:

- Understand why blocking a user does not automatically silence them in voice
- Populate a per-player mute list using Discord block relationships (client-side) or your game server
  (server-side)
- Apply that mute list using a shared implementation that works for both approaches
- Satisfy **bi-directional mute** requirements (if A blocks B, neither can hear the other)

Prerequisites: the Getting Started guide; a working lobby from Managing Lobbies; familiarity with
Managing Voice Chat and Managing Relationships.

### Why Voice Muting Must Be Handled Explicitly

**Discord Blocking Does Not Silence Voice.** Calling `Client::BlockUser` prevents a user from sending
friend requests or messages, but it does **not** mute them in a lobby voice call. **If you want a
blocked player to be inaudible, your game must explicitly call `Call::SetLocalMute`.**

**Block Signals May Come From Outside Discord.** Your game may receive block information from sources
other than Discord — for example, from a platform-level or game-level block list. In these cases there
is no Discord relationship to query on the client. **Your server needs to supply this information to
clients through another mechanism, such as lobby member metadata.**

**Bi-Directional Muting.** `Call::SetLocalMute` is **one-directional**: calling it on A's client only
stops A from hearing B — it has no effect on what B hears. **To silence audio in both directions, both
clients must independently call `SetLocalMute` on each other.**

The challenge is that both players need to independently know to mute each other. **The approaches in
this guide address this through lobby member metadata: each player writes their `mute_list` to their
own member metadata, which is visible to all lobby members.** This lets players detect when someone
else has listed them and mute that person in return, regardless of the original source of the block
signal.

### Step 1: Populate the Mute List

Both approaches work by writing a **`mute_list`** key to each lobby member's metadata. **The value is a
comma-separated list of Discord user IDs** that player should mute in the voice call.

#### Client-Side

Use this approach when the block information your game needs is available directly on the client — for
example, from Discord's relationship system, your own in-game friend/block system, or any other
client-accessible data source.

When joining the lobby, build the mute list from whatever client-side data you have and write those IDs
to your own member metadata using **`Client::CreateOrJoinLobbyWithMetadata`**. This makes your mute
list visible to other lobby members so they can mute you in return.

```cpp
const auto lobbySecret = "my-lobby-secret";

// Example: build the mute list from Discord block relationships.
// Replace this with your own logic if using a different data source.
std::string myMuteList;
for (const auto& rel : client->GetRelationships()) {
    if (rel.DiscordRelationshipType() == discordpp::RelationshipType::Blocked) {
        if (!myMuteList.empty()) myMuteList += ",";
        myMuteList += std::to_string(rel.Id());
    }
}

// Join the lobby with your mute list in your member metadata
client->CreateOrJoinLobbyWithMetadata(
  lobbySecret,
  {},  // no lobby-level metadata needed
  {{"mute_list", myMuteList}},
  [](const discordpp::ClientResult &result, uint64_t lobbyId) {
      if (!result.Successful()) {
          std::cerr << "Failed to join lobby\n";
      }
  }
);
```

So `Client::CreateOrJoinLobbyWithMetadata(secret, lobbyMetadata, memberMetadata, callback)`.

**Member metadata has a maximum total length of 1,000 characters.** At ~19 characters per Discord
snowflake ID plus a comma separator, **this comfortably fits around 50 blocked users.** Look at the
server-side integration if your needs exceed this limitation.

#### Server-Side

Use this approach when block information comes from an external source — such as a platform-level
blocklist, when you want to **guarantee bi-directional muting without relying on clients** to populate
their own metadata, or when you need to **filter lobby blocklists to only those in the lobby** to
support players who have very large potential blocklists.

Your server code can filter each player's block list down to only the other members in the session and
write it to their metadata when creating the lobby. **Since you know exactly who is joining, you only
need to consider block relationships between those specific players — not each player's entire block
list.** The client-side code in Step 2 handles the reverse direction: each client also checks whether
any other participant has listed them.

```python
import requests

API_ENDPOINT = 'https://discord.com/api/v10'
BOT_TOKEN = 'YOUR_BOT_TOKEN'

def create_lobby_with_mute_metadata(session_members, block_relationships):
    """
    session_members: list of Discord user ID strings for this lobby
    block_relationships: dict mapping user ID to list of user IDs they have blocked

    Each player's mute_list contains only the session members they have blocked.
    The client handles the reverse direction by checking whether others have listed them.
    """
    mute_map = {user_id: set() for user_id in session_members}

    # Only include blocks where both users are in this session
    for blocker_id, blocked_ids in block_relationships.items():
        if blocker_id in mute_map:
            for blocked_id in blocked_ids:
                if blocked_id in mute_map:
                    mute_map[blocker_id].add(blocked_id)

    members = []
    for user_id in session_members:
        mute_list = mute_map.get(user_id, set())
        members.append({
            "id": user_id,
            "metadata": {"mute_list": ",".join(mute_list)} if mute_list else None,
        })

    response = requests.post(
        f'{API_ENDPOINT}/lobbies',
        headers={
            'Authorization': f'Bot {BOT_TOKEN}',
            'Content-Type': 'application/json',
        },
        json={"members": members},
    )
    response.raise_for_status()
    return response.json()

# Example: Player A has blocked Player B.
# Only A's mute_list contains B. B's mute_list is empty (B has not blocked anyone).
# The client-side code in Step 2 handles the reverse: B will detect A has listed them and mute A.
lobby = create_lobby_with_mute_metadata(
    session_members=[
        "111111111111111111",  # Player A
        "222222222222222222",  # Player B
        "333333333333333333",  # Player C (no blocks)
    ],
    block_relationships={
        "111111111111111111": ["222222222222222222"],  # A has blocked B
    },
)
print(f"Lobby created: {lobby['id']}")
```

**If players join the lobby after the initial creation, you may need to update their metadata with the
relevant blocklists.** Use `POST /lobbies/{lobby.id}/members/bulk` to add or update **up to 25 members
in a single request**, or `PUT /lobbies/{lobby.id}/members/{user.id}` to update a single member (see
LOBBIES.md).

### Step 2: Apply the Mute List

Once the `mute_list` metadata is populated — by either approach — **the client code that reads it and
applies mutes is the same**.

#### On Lobby Join

After joining the lobby and starting the voice call, run `ApplyMuteChecks` against every other lobby
member.

```cpp
const auto currentUser = client->GetCurrentUserV2();
if (!currentUser) return;
const auto myUserId = currentUser->Id();
const auto lobby = client->GetLobbyHandle(lobbyId);
auto call = client->StartCall(lobbyId);

if (lobby && call) {
    for (auto memberId : lobby->LobbyMemberIds()) {
        if (memberId != myUserId) {
            ApplyMuteChecks(call, *lobby, myUserId, memberId);
        }
    }
}

// Mutes lobbyUserId locally if either myUserId or lobbyUserId has listed the other in their mute_list.
void ApplyMuteChecks(discordpp::Call& call, const discordpp::LobbyHandle& lobby,
                     const uint64_t myUserId, const uint64_t lobbyUserId) {

  auto isListed = [&](const uint64_t ownerId, const uint64_t searchId) -> bool {
    const auto member = lobby.GetLobbyMemberHandle(ownerId);
    if (!member) return false;
    auto metadata = member->Metadata();
    const auto it = metadata.find("mute_list");
    if (it == metadata.end()) return false;
    std::stringstream ss(it->second);
    std::string idStr;
    while (std::getline(ss, idStr, ',')) {
      if (std::stoull(idStr) == searchId) return true;
    }
    return false;
  };

  if (isListed(myUserId, lobbyUserId) || isListed(lobbyUserId, myUserId)) {
    call.SetLocalMute(lobbyUserId, true);
  }
}
```

API surface this reveals: `Client::GetCurrentUserV2()` (with `Id()`), `Client::GetLobbyHandle(lobbyId)`,
`LobbyHandle::LobbyMemberIds()`, `LobbyHandle::GetLobbyMemberHandle(userId)` and the member handle's
`Metadata()` map.

#### Handling Participants Who Join Later

Register **`Call::SetParticipantChangedCallback`** to apply mutes when new participants join the voice
call mid-session. **This fires with `added = true` when someone joins and `added = false` when they
leave.**

```cpp
call.SetParticipantChangedCallback(
    [client, lobbyId, myUserId, call](uint64_t userId, const bool added) mutable {
      if (!added) return;
      auto lobby = client->GetLobbyHandle(lobbyId);
      if (!lobby) return;
      ApplyMuteChecks(call, *lobby, myUserId, userId);
    }
);
```

### Best Practices

- **Consider filtering at matchmaking time.** The cleanest experience is to avoid placing blocked
  players in the same lobby at all. Voice muting handles the audio side, but blocked players may still
  see each other in the game UI.
- **Update mutes when relationships change.** If a player blocks someone during an active session, call
  `Call::SetLocalMute` immediately and update your `mute_list` member metadata by re-calling
  `Client::CreateOrJoinLobbyWithMetadata` with the new list. For the server-side approach, update the
  member's metadata via `PUT /lobbies/{lobby.id}/members/{user.id}`.
- **Keep metadata compact.** Lobby member metadata has a **1,000-character limit**. Comma-separated ID
  strings are more efficient than JSON objects.

---

## Symbols and change logs

### Doxygen anchors

Base `https://discord.com/developers/docs/social-sdk/`.

| Symbol | Anchor |
| --- | --- |
| `Call` | `classdiscordpp_1_1Call.html#a1cc8a7f73c15a960bc409d734b5edbd1` |
| `Call::SetParticipantVolume` | `classdiscordpp_1_1Call.html#ad974fadbe89c453e4d8a3f9824e21ceb` |
| `Call::SetSelfDeaf` | `classdiscordpp_1_1Call.html#a07d67c210f2a4655c6f1d2899c6d32d6` |
| `Call::SetSelfMute` | `classdiscordpp_1_1Call.html#afa35a5d6a4564df97452df58bb74f617` |
| `Call::SetVADThreshold` | `classdiscordpp_1_1Call.html#a7c3fd83c5dfe37d796e30c5e28c93b6e` |
| `Call::SetLocalMute` | `classdiscordpp_1_1Call.html#aaf8e7728b15da5d1be8d8b4258225171` |
| `Call::SetParticipantChangedCallback` | `classdiscordpp_1_1Call.html#acb20d338a04abec2369217f41c22c0e5` |
| `Client` | `classdiscordpp_1_1Client.html#a91716140c699d8ef0bdf6bfd7ee0ae13` |
| `Client::CreateOrJoinLobby` | `classdiscordpp_1_1Client.html#a8b4e195555ecaa89ccdfc0acd28d3512` |
| `Client::CreateOrJoinLobbyWithMetadata` | `classdiscordpp_1_1Client.html#a5c84fa76c73cf3c0bfd68794ca5595c1` |
| `Client::BlockUser` | `classdiscordpp_1_1Client.html#add4a917c8382e411d5a55737c9edc8ad` |
| `Client::SetAutomaticGainControl` | `classdiscordpp_1_1Client.html#a818ae7f46b5bd3873dcd51dd3d9fa64d` |
| `Client::SetEchoCancellation` | `classdiscordpp_1_1Client.html#a1def244b7ecd388902ba5256ce506ca3` |
| `Client::SetInputVolume` | `classdiscordpp_1_1Client.html#ad4358f5baffd9a5f2a6fa74d62459313` |
| `Client::SetNoAudioInputCallback` | `classdiscordpp_1_1Client.html#a479e60724bf6b0b39b555c1ff8489b9e` |
| `Client::SetNoAudioInputThreshold` | `classdiscordpp_1_1Client.html#ab33f5d70461ee7590b6f3cfccaeb6df4` |
| `Client::SetNoiseCancellation` | `classdiscordpp_1_1Client.html#a54aad09e8e06dc327695209b733d3f4c` |
| `Client::SetNoiseSuppression` | `classdiscordpp_1_1Client.html#ae3f6e33b956964525adfa4536bd1fe73` |
| `Client::SetOutputVolume` | `classdiscordpp_1_1Client.html#a61a9321a79479c8b1be1559e2bbdd934` |
| `Client::SetSelfDeafAll` | `classdiscordpp_1_1Client.html#a59be56ae5752e9f2f0f299bc552282b2` |
| `Client::SetSelfMuteAll` | `classdiscordpp_1_1Client.html#a9c6ef96590533d103a866cb8a99d2669` |
| `Client::StartCall` | `classdiscordpp_1_1Client.html#aef4f25d761fe198fbe9bc721fc24d83f` |
| `Client::StartCallWithAudioCallbacks` | `classdiscordpp_1_1Client.html#abcaa891769f9e912bfa0e06ff7221b05` |
| `VoiceStateHandle` | `classdiscordpp_1_1VoiceStateHandle.html#aad2d4454b6677d82721128b0cd98a2d8` |
| `VoiceStateHandle::SelfDeaf` | `classdiscordpp_1_1VoiceStateHandle.html#a9fd4ac5fb813b926d1336fc65b440f42` |
| `VoiceStateHandle::SelfMute` | `classdiscordpp_1_1VoiceStateHandle.html#a5476a6e8d5e9092a153b4646371a9f3f` |
| `Client::GetDefaultCommunicationScopes` | `classdiscordpp_1_1Client.html#a71499da752fbdc2d4326ae0fd36c0dd1` |

Used without a linked anchor: `Client::GetCall`, `Client::EndCall`, `Client::EndCalls`,
`Client::UserAudioReceivedCallback`, `Client::GetCurrentUserV2`, `Client::GetLobbyHandle`,
`Client::GetRelationships`, `LobbyHandle::GetCallInfoHandle`, `LobbyHandle::LobbyMemberIds`,
`LobbyHandle::GetLobbyMemberHandle`, the call-info handle's `GetParticipants` and
`GetVoiceStateHandle`, the lobby member handle's `Metadata`, `RelationshipType::Blocked`, and
`ClientResult`.

### Change logs

**Managing Voice Chat:**

| Date           | Changes                                                           |
| -------------- | ----------------------------------------------------------------- |
| May 13, 2026   | Add noise suppression, cancellation, and no-audio-input detection |
| June 30, 2025  | Add communications scope warning                                  |
| June 19, 2025  | released guide                                                    |
| March 17, 2025 | initial release                                                   |

**Voice Muting Based on Player Blocks:**

| Date           | Changes         |
| -------------- | --------------- |
| April 22, 2026 | Initial release |
