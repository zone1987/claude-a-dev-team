# Discord Social SDK — Setting Rich Presence

Distilled from
`docs.discord.com/developers/discord-social-sdk/development-guides/setting-rich-presence`,
retrieved 2026-08-26.

## Contents

- [Overview and prerequisites](#overview-and-prerequisites)
- [Understanding Rich Presence](#understanding-rich-presence)
- [Customizing Rich Presence](#customizing-rich-presence)
- [Setting an Invite Image](#setting-an-invite-image)
- [Uploading Assets](#uploading-assets)
- [Setting Details and State](#setting-details-and-state)
- [Setting the Application Name](#setting-the-application-name)
- [Setting Timestamps](#setting-timestamps)
- [Setting Assets](#setting-assets)
- [Setting Field URLs](#setting-field-urls)
- [Setting Buttons](#setting-buttons)
- [Configuring Status Text](#configuring-status-text)
- [Setting Party and Join Secret](#setting-party-and-join-secret)
- [Setting Supported Platforms](#setting-supported-platforms)
- [Rich Presence Without Authentication](#rich-presence-without-authentication)
- [Symbols and change log](#symbols-and-change-log)

---

## Overview and prerequisites

Rich Presence allows you to display detailed information about what players are doing in your game.
**Users can see this information in their Discord profile and friends list and use it to join their
friends' games with Game Invites.**

Prerequisites:

- Set up the Discord Social SDK.
- Connected to Discord with a valid client instance.

**This feature requires the Default Presence Scopes** (`openid` and `sdk.social_layer_presence`). Use
`Client::GetDefaultPresenceScopes` when configuring your OAuth2 flow.

---

## Understanding Rich Presence

Users can see Rich Presence information in various places in Discord:

- User profiles
- Friend lists
- Server member lists

**Naming note:** Rich Presence, aka "Activity", can be thought of as the "current activity of a user"
and is represented by the `Activity` class in the SDK and in the gateway events
(`/developers/events/gateway-events#activity-object`). **This is not to be confused with Discord
Activities** (`/developers/activities/overview`), which are embedded games that can also set and
display rich presence.

Each `Activity` contains fields that describe the following:

| Field | Description | Purpose |
| --- | --- | --- |
| `name` | Game or app name | Displayed in the user's profile |
| `type` | Activity type | What the player is doing (e.g., "Playing", "Watching", "Listening") |
| `details` | What the player is doing | Main activity description (e.g., "Playing Capture the Flag") |
| `state` | Their current status | Secondary status (e.g., "In Queue", "In Match, "In a group") |
| `party` | Party information | Shows party size and capacity (e.g., "2 of 4") |
| `timestamps` | Activity duration | Shows elapsed or remaining time |
| `assets` | Custom artwork | Game/map thumbnails and character icons |
| `secrets` | Join/spectate tokens | Enable Game Invite functionality |
| `supportedPlatforms` | Platform flags | Control where join buttons appear |

**While the SDK supports multiple `ActivityTypes`, games should use `ActivityTypes::Playing` for
`type`.** The SDK automatically associates the activity with your game, so by default fields like
`name` show your game's name. To customize the displayed name, see
[Setting the Application Name](#setting-the-application-name).

---

## Customizing Rich Presence

When displayed in Discord, Rich Presence has **three main components**:

```
Playing "Your Game Name"          <- Line 1: Game name (automatic)
Capture the Flag | 2 - 1          <- Line 2: Details field
In a group (2 of 3)               <- Line 3: State + Party info
```

You control how lines 2 and 3 are rendered:

- **Line 1**, `Playing "game name"`, is powered by the name of your game (or application) on Discord.
- **Line 2**, `Capture the flag | 2 - 1`, is powered by the **`details`** field in the activity, and
  should generally try to describe what **the player** is currently doing. **You can even include
  dynamic data such as a match score here.**
- **Line 3**, `In a group (2 of 3)`, describes the **party** the player is in. "Party" refers to a group
  of players in a shared context, such as a lobby, server, team, etc. The first half, `In a group`, is
  powered by the **`state`** field; the second half, `(2 of 3)`, is powered by the **`party`** field and
  describes how many people are in the current party and how big the party can get.

[Image: Graphical representation of the legend for rich presence details]

For tips on designing Rich Presence, see the Rich Presence best practices guide
(`/developers/rich-presence/best-practices`).

---

## Setting an Invite Image

**The Rich Presence invite image appears when invites are sent for a 3rd party game or app using the
Discord Social SDK.** After uploading an invite image for your app, you can see a preview of it to the
right (under "IRL Invite Image Example"). [Image: Rich Presence invite image in app settings]

---

## Uploading Assets

While integrating Rich Presence, you'll likely want to upload custom art assets for your app. **For all
Rich Presence assets, it's highly recommended to make them 1024 x 1024.**

To add custom assets, navigate to your app's settings and click **Rich Presence** on the left-hand
sidebar. On the Art Assets page
(`https://discord.com/developers/applications/select/rich-presence/assets`), you can upload **two
different types of assets**. [Image: Rich Presence invite image in app settings]

**Up to 300 custom assets can be added to your app** for later use when setting Rich Presence for a
Discord user. These assets can be anything that help orient others to what a user is doing inside of
your Activity or 3rd party game.

**If you need more than 300 custom assets or want to use images stored somewhere else, you can also
specify an external URL** (`/developers/events/gateway-events#activity-object-activity-asset-image`) as
long as it still has the proper dimensions and size. **Unlike uploaded assets, external URLs also
support GIF, animated WebP, and AVIF.**

For tips on choosing assets, see the Rich Presence best practices guide
(`/developers/rich-presence/best-practices#have-interesting-expressive-art`).

**When uploading Rich Presence assets, the asset keys will automatically be changed to lowercase.** You
can see this reflected in your app's settings after saving a newly uploaded asset, and you should keep
it in mind when referencing any asset keys in your code. [Image: Rich Presence assets in app settings]

---

## Setting Details and State

```cpp
// Create a new activity
discordpp::Activity activity;
activity.SetType(discordpp::ActivityTypes::Playing);
activity.SetDetails("Battle Creek");
activity.SetState("In Competitive Match");

// Update the presence
client->UpdateRichPresence(activity, [](discordpp::ClientResult result) {
  if (result.Successful()) {
    std::cout << "✅ Rich presence updated!\n";
  }
});
```

---

## Setting the Application Name

By default, Rich Presence displays your application's name as it's registered on Discord (the top line,
e.g. `Playing "My Game: Chapter Two"`). **You can override this displayed name by setting the `name`
field on the activity with `Activity::SetName` before calling `Client::UpdateRichPresence`:**

```cpp
// Override the displayed application name (top line of Rich Presence)
activity.SetName("My Game: Chapter Two");
```

**Registered application names are restricted to a limited character set. Using `Activity::SetName`
gives you more flexibility over exactly what text is displayed, including characters that aren't
permitted in your registered application name.**

---

## Setting Timestamps

You can include timestamps to display a **live timer**, such as how long a player has been in their
current activity or how much time is left in a timed match. **Timestamps are `ActivityTimestamps` set
as Unix timestamps in seconds.**

**The direction of the timer is determined by which field you set:**

- Set the **start** time only to count **up** and show elapsed time (e.g. `12:34 elapsed`).
- Set the **end** time to count **down** and show the remaining time (e.g. `12:34 left`).

### Count up (elapsed time)

Set `ActivityTimestamps::SetStart` to a time in the past, such as the current time. The timer counts up
from that point.

```cpp
// Counting up: elapsed time since the activity started
discordpp::ActivityTimestamps timestamps;
// time(nullptr) returns the current Unix time in seconds, so the timer starts now
timestamps.SetStart(time(nullptr));
activity.SetTimestamps(timestamps);
```

### Count down (time remaining)

Set `ActivityTimestamps::SetEnd` to a time in the future. The timer counts down to that point.

```cpp
// Counting down: time remaining until the activity ends (one hour from now)
discordpp::ActivityTimestamps timestamps;
// time(nullptr) is the current Unix time in seconds; + 3600 sets the end one hour from now
timestamps.SetEnd(time(nullptr) + 3600);
activity.SetTimestamps(timestamps);
```

**Setting the end time is what makes the timer count down.** If you only set the start time, the timer
counts up instead. **You can set both** — `start` still controls the elapsed reference point, but as
long as `end` is set the timer displays the remaining time.

---

## Setting Assets

Once you've uploaded assets to your app, reference them using their **asset key**. Example with assets
keyed "map-mainframe", "tank-avatar", and "invite-cover-image":

```cpp
// Setting Activity Assets
discordpp::ActivityAssets assets;
assets.SetLargeImage("map-mainframe");
assets.SetLargeText("Mainframe");
assets.SetSmallImage("tank-avatar");
assets.SetSmallText("Tank");
assets.SetInviteCoverImage("invite-cover-image"); // Used for Game Invites
activity.SetAssets(assets);
```

If you need more than 300 custom assets or want to use images stored somewhere else, you can specify an
external URL as long as it has the proper dimensions and size. **Unlike uploaded assets, external URLs
also support GIF, animated WebP, and AVIF.**

---

## Setting Field URLs

**You can set URLs for `details`, `state`, `assets.large_image` and `assets.small_image`.** When
present, **these URLs make the corresponding image/text into clickable links.**

```cpp
activity.SetState("Playing on Mainframe");
activity.SetStateUrl("https://example.com/maps/mainframe");
activity.SetDetails("Rank #1337 in global leaderboard");
activity.SetDetailsUrl("https://example.com/leaderboard/global");

discordpp::ActivityAssets assets;
assets.SetLargeImage("map-mainframe");
assets.SetLargeText("Mainframe");
assets.SetLargeUrl("https://example.com/maps/mainframe");
assets.SetSmallImage("tank-avatar");
assets.SetSmallText("Tank");
assets.SetSmallUrl("https://example.com/classes/tank");

activity.SetAssets(assets);
```

So the URL setters are `Activity::SetStateUrl`, `Activity::SetDetailsUrl`,
`ActivityAssets::SetLargeUrl` and `ActivityAssets::SetSmallUrl`.

---

## Setting Buttons

**You can add up to two custom buttons** to a player's Rich Presence. **Each button has a label and a
URL**, making them a direct call to action for anyone viewing the presence — link out to your game's
store page, website, or community server.

C++:

```cpp
discordpp::ActivityButton buyButton;
buyButton.SetLabel("Buy On Steam!");
buyButton.SetUrl("https://store.steampowered.com/app/AppID/GameName/");

discordpp::ActivityButton communityButton;
communityButton.SetLabel("Join the Community!");
communityButton.SetUrl("https://discord.gg/your-discord-url-or-id");

activity.AddButton(buyButton);
activity.AddButton(communityButton);
```

Unity (C#):

```csharp
ActivityButton buyButton = new ActivityButton();
buyButton.SetLabel("Buy On Steam!");
buyButton.SetUrl("https://store.steampowered.com/app/AppID/GameName/");

ActivityButton communityButton = new ActivityButton();
communityButton.SetLabel("Join the Community!");
communityButton.SetUrl("https://discord.gg/your-discord-url-or-id");

activity.AddButton(buyButton);
activity.AddButton(communityButton);
```

Unreal:

```cpp
UDiscordActivityButton* BuyButton = NewObject<UDiscordActivityButton>();
BuyButton->Init();
BuyButton->SetLabel("Buy On Steam!");
BuyButton->SetUrl("https://store.steampowered.com/app/AppID/GameName/");

UDiscordActivityButton* CommunityButton = NewObject<UDiscordActivityButton>();
CommunityButton->Init();
CommunityButton->SetLabel("Join the Community!");
CommunityButton->SetUrl("https://discord.gg/your-discord-url-or-id");

Activity->AddButton(BuyButton);
Activity->AddButton(CommunityButton);
```

**Buttons are only visible to other users — you cannot see buttons on your own Rich Presence.** To test
that your buttons are working, use a second account or ask a friend to view your profile.

---

## Configuring Status Text

**By default, Rich Presence displays the game's name in the user's status text.** You can override this
behavior by setting a status display type.

```cpp
// uses the game's name in the status text (default)
activity.SetStatusDisplayType(discordpp::StatusDisplayTypes::Name);

// uses the activity's state field in the status text
activity.SetStatusDisplayType(discordpp::StatusDisplayTypes::State);

// uses the activity's details field in the status text
activity.SetStatusDisplayType(discordpp::StatusDisplayTypes::Details);
```

So `StatusDisplayTypes` has the values **`Name` (default), `State` and `Details`**.

---

## Setting Party and Join Secret

You can include party details and a join secret to power Game Invites (see
RELATIONSHIPS-AND-FRIENDS.md → Managing Game Invites).

```cpp

// Setting Party Details
discordpp::ActivityParty party;
party.SetId("party1234");
party.SetCurrentSize(1);
party.SetMaxSize(5);
activity.SetParty(party);

// Setting Join Secret details
discordpp::ActivitySecrets secrets;
secrets.SetJoin("your-join-secret");
activity.SetSecrets(secrets);
```

---

## Setting Supported Platforms

You can set the supported platforms for your game in Rich Presence. **This controls where the join
buttons appear in Discord.** If you only want the join button to appear on desktop:

```cpp
activity.SetSupportedPlatforms(discordpp::ActivityGamePlatforms::Desktop);
```

See the `ActivityGamePlatforms` enum for all supported platforms. (This page does not enumerate them;
the game-invites page names `Desktop`, `IOS` and `Android` and shows them combined with `|`.)

---

## Rich Presence Without Authentication

**Warning: Rich Presence via RPC (Remote Procedure Call) is supported on desktop, and on Android (from
Social SDK 1.10+). It does not support iOS, console, or web clients.**

**Unlike most other features of the Discord Social SDK, Rich Presence can be set without
authentication.** Instead of using `Client::Connect` to authenticate with Discord, you can use Rich
Presence functionality by directly communicating with a running Discord client through RPC.

### Requirements

- **The Discord desktop client must be running on the user's machine**, or — on Android — **the Discord
  app must be installed and signed in**.
- **Your application must be registered with Discord and have a valid Application ID.**

This direct approach makes Rich Presence integration much simpler for developers who only need basic
presence functionality while a Discord client is available.

### Setting Up Direct Rich Presence

1. Set your application ID using `Client::SetApplicationId`
2. Configure your activity details
3. Call `Client::UpdateRichPresence`

```cpp
auto client = std::make_shared<discordpp::Client>();

// Set the application ID (no Connect() call needed)
client->SetApplicationId(APPLICATION_ID);

// Configure rich presence details
discordpp::Activity activity;
activity.SetType(discordpp::ActivityTypes::Playing);
activity.SetState("In Competitive Match");
activity.SetDetails("Rank: Diamond II");

// Update rich presence
client->UpdateRichPresence(
    activity, [](const discordpp::ClientResult &result) {
      if (result.Successful()) {
        std::cout << "🎮 Rich Presence updated successfully!\n";
      } else {
        std::cerr << "❌ Rich Presence update failed";
      }
    });
```

For the RPC protocol itself, call the Skill tool with "discord-rpc-voice".

---

## Symbols and change log

### Doxygen anchors

Base `https://discord.com/developers/docs/social-sdk/`.

| Symbol | Anchor |
| --- | --- |
| `Activity` | `classdiscordpp_1_1Activity.html#ae793d9adbe16fef402b859ba02bee682` |
| `Activity::SetName` | `classdiscordpp_1_1Activity.html#a59f9a63a8b105946d0c9838f3e643ae2` |
| `ActivityTimestamps` | `classdiscordpp_1_1ActivityTimestamps.html#a0ff108aac69639c18f1669994e459ee2` |
| `ActivityTimestamps::SetEnd` | `classdiscordpp_1_1ActivityTimestamps.html#ab6478ec46860feb64174da3eb1063aaa` |
| `ActivityTimestamps::SetStart` | `classdiscordpp_1_1ActivityTimestamps.html#a5bb6a6bc243fedb954ae82d6c4ef3542` |
| `ActivityTypes` | `namespacediscordpp.html#a6c76a8cbbc9270f025fd6854d5558660` |
| `Client::Connect` | `classdiscordpp_1_1Client.html#a873a844c7c4c72e9e693419bb3e290aa` |
| `Client::SetApplicationId` | `classdiscordpp_1_1Client.html#ad452335c06b28be0406dab824acccc49` |
| `Client::UpdateRichPresence` | `classdiscordpp_1_1Client.html#af0a85e30f2b3d8a0b502fd23744ee58e` |
| `Client::GetDefaultPresenceScopes` | `classdiscordpp_1_1Client.html#a7648bd1d2f7d9a86ebd0edb8bef12b5c` |

Types and members used without a linked anchor: `Activity::SetType`, `Activity::SetState`,
`Activity::SetStateUrl`, `Activity::SetDetails`, `Activity::SetDetailsUrl`,
`Activity::SetTimestamps`, `Activity::SetAssets`, `Activity::SetParty`, `Activity::SetSecrets`,
`Activity::SetSupportedPlatforms`, `Activity::SetStatusDisplayType`, `Activity::AddButton`,
`ActivityAssets` (`SetLargeImage`, `SetLargeText`, `SetLargeUrl`, `SetSmallImage`, `SetSmallText`,
`SetSmallUrl`, `SetInviteCoverImage`), `ActivityButton` (`SetLabel`, `SetUrl`),
`UDiscordActivityButton` (Unreal, with `Init()`), `ActivityParty` (`SetId`, `SetCurrentSize`,
`SetMaxSize`), `ActivitySecrets` (`SetJoin`), `ActivityGamePlatforms::Desktop`,
`ActivityTypes::Playing`, `StatusDisplayTypes` (`Name`, `State`, `Details`), `ClientResult`.

### Change Log

| Date           | Changes                                                        |
| -------------- | -------------------------------------------------------------- |
| August 3, 2026 | Added Android support for Rich Presence without authentication |
| June 24, 2026  | Clarified count-up vs count-down timestamps                    |
| June 5, 2026   | Added Setting the Application Name section                     |
| March 31, 2026 | Added Setting Buttons section                                  |
| March 17, 2025 | Initial release                                                |
