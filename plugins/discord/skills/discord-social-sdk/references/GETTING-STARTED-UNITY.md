# Getting Started with Unity and the Discord Social SDK

Distilled from `docs.discord.com/developers/discord-social-sdk/getting-started/using-unity`,
retrieved 2026-08-26.

## Contents

- [Overview and prerequisites](#overview-and-prerequisites)
- [Step 1: Create a Discord Developer Team](#step-1-create-a-discord-developer-team)
- [Step 2: Create a Discord Application](#step-2-create-a-discord-application)
- [Step 3: Enable Discord Social SDK for Your App](#step-3-enable-discord-social-sdk-for-your-app)
- [Step 4: Download the Social SDK for Unity](#step-4-download-the-social-sdk-for-unity)
- [Step 5: Project Setup](#step-5-project-setup)
- [Step 6: Setting Up SDK Event Handling](#step-6-setting-up-sdk-event-handling)
- [Step 7: Account Linking with Discord](#step-7-account-linking-with-discord)
- [Step 8: Connect the SDK to Discord](#step-8-connect-the-sdk-to-discord)
- [Step 9: Access Discord Relationships](#step-9-access-discord-relationships)
- [Step 10: Set Rich Presence](#step-10-set-rich-presence)
- [The full DiscordManager.cs](#the-full-discordmanagercs)
- [Conclusion and next steps](#conclusion-and-next-steps)
- [Symbols used in this guide](#symbols-used-in-this-guide)
- [Change Log](#change-log)

---

## Overview and prerequisites

This guide walks through integrating the Discord Social SDK into a **Unity project**. By the end you
have a project that can:

- Authenticate users with Discord
- Set up logging and status monitoring
- Start the SDK and establish a connection
- Request the number of Discord friends the player has
- Set the player's rich presence for your game

### Prerequisites

- **Unity 2021.3 or later**

The C# namespace is `Discord.Sdk`.

---

## Step 1: Create a Discord Developer Team

Create a developer team on the Discord Developer Portal (`https://discord.com/developers/teams`). This
team is used to manage your Discord applications and SDK integrations. Skip this step if you already
have a team configured.

Later, you can invite your team members to your new team to collaborate on your integration.

---

## Step 2: Create a Discord Application

1. Create a new application on the Discord Developer Portal
   (`https://discord.com/developers/applications`) and assign it to your team.
2. Add a redirect URL in the OAuth2 tab
   (`https://discord.com/developers/applications/select/oauth2`):
   - For desktop applications: `http://127.0.0.1/callback` (this can be changed later).
   - See `discordpp::Client::Authorize` for more details on setting up more advanced redirect URIs.
3. Enable the `Public Client` toggle in the OAuth2 tab.

**Warning:** this guide requires enabling **Public Client** to get started quickly. **Most games will
not want to ship as a public client.** Have your team review this setting before releasing your game.
See CORE-CONCEPTS.md → OAuth2 Client Types.

---

## Step 3: Enable Discord Social SDK for Your App

1. From the Discord Developer Portal, select your newly created application from Step 2.
2. In the left sidebar for your app, locate and click the **Getting Started** link under
   `Discord Social SDK`.
3. Fill out the form to share details about your game.
4. Click `Submit` and the Social SDK will be enabled for your application.
5. Once enabled, you'll find binaries for the Social SDK under **Downloads**
   (`https://discord.com/developers/applications/select/social-sdk/downloads`).

---

## Step 4: Download the Social SDK for Unity

1. Click on the **Downloads** link under the Discord Social SDK section of the sidebar.
2. Select the latest version from the version dropdown and download the SDK for Unity.

A Unity sample project is available for download on that page; the upstream guide does not cover it
(see [Next steps](#conclusion-and-next-steps) for the GitHub sample).

---

## Step 5: Project Setup

Set up the Unity project to include the Social SDK package and add the necessary objects and scripts.

1. Create a **new 2D project** in Unity Hub using Unity version 2021.3 or later.
2. Either:
   1. Unzip the zip file in the Unity `Packages` folder, **or**
   2. Unzip the zip file and **Install Package from Disk**
      (`https://docs.unity3d.com/Manual/upm-ui-local.html`). Make sure the folder is in a directory
      that won't get moved or deleted, as your Unity project will load it from that location.
3. In your project add a `Scripts` folder and create a `DiscordManager.cs` script.
4. Add the following code to `DiscordManager.cs`:

```cs
using UnityEngine;
using UnityEngine.UI;
using Discord.Sdk;
using System.Linq;

public class DiscordManager : MonoBehaviour
{
    [SerializeField] 
    private ulong clientId; // Set this in the Unity Inspector from the dev portal
    
    [SerializeField]
    private Button loginButton; 
    
    [SerializeField] 
    private Text statusText;

    private Client client;
    private string codeVerifier;
}
```

(Upstream numbering jumps from 4 to 6 here — there is no step 5 in the list.)

6. Add an empty object to the scene (**GameObject > Create Empty**) called **DiscordManager** and
   attach the `DiscordManager.cs` script to it.
7. Add a button to the scene: **GameObject > UI > Legacy > Button**.
8. Add text to the scene: **GameObject > UI > Legacy > Text**.
9. Position the button and text somewhere visible on the screen.
10. Attach the button and text to the **DiscordManager** in the inspector.
11. Run it!

Nothing should happen yet.

### Troubleshooting

- Make sure the Social SDK package was successfully added to Unity.

**Mac libdiscord_partner_sdk.dylib Not Opened.** On Mac you may get the error
"libdiscord_partner_sdk.dylib" Not Opened because Apple couldn't verify it. If this happens press
**Done** on the popup. [Image: Error]

Open your **System Settings > Privacy & Security** and scroll down to the **Security** section. It will
tell you "libdiscord_partner_sdk.dylib" was blocked to protect your Mac. Press **Open Anyway** and try
running again. [Image: Settings]

Now when you get the pop up you'll have the option to select **Open Anyway** and it will be able to
use it successfully. [Image: Open]

---

## Step 6: Setting Up SDK Event Handling

Two important callbacks:

- A logging callback to see what the SDK is doing
- A status callback to know when you can start using Discord features

Add the following to `DiscordManager.cs`:

```cs
void Start()
{
    client = new Client();

    // Modifying LoggingSeverity will show you more or less logging information
    client.AddLogCallback(OnLog, LoggingSeverity.Error);
    client.SetStatusChangedCallback(OnStatusChanged);

    // Make sure the button has a listener
    if (loginButton != null)
    {
        //loginButton.onClick.AddListener(StartOAuthFlow);
    }
    else
    {
        Debug.LogError("Login button reference is missing, connect it in the inspector!");
    }

    // Set initial status text
    if (statusText != null)
    {
        statusText.text = "Ready to login";
    }
    else
    {
        Debug.LogError("Status text reference is missing, connect it in the inspector!");
    }
}

private void OnLog(string message, LoggingSeverity severity)
{
    Debug.Log($"Log: {severity} - {message}");
}

private void OnStatusChanged(Client.Status status, Client.Error error, int errorCode)
{
    Debug.Log($"Status changed: {status}");
    statusText.text = status.ToString();
    if(error != Client.Error.None)
    {
        Debug.LogError($"Error: {error}, code: {errorCode}");
    }
}
```

This hooks up the API status changes to your text in the game. Then get your Client ID from the OAuth2
tab in the developer portal and paste it into the `ClientID` on the **DiscordManager** in the
inspector.

### What These Callbacks Do

- The **logging callback** shows you what's happening behind the scenes and is a powerful tool for
  debugging.
- The **status callback** tells you when you're connected and ready to use Discord features.

**The Unity plugin handles running the SDK callbacks for you in Unity** — no need to use
`RunCallbacks` as in the C++ guide.

Most Discord features won't work until the status is `Ready`.

---

## Step 7: Account Linking with Discord

Implement OAuth2 authentication to support account linking with Discord. This process will:

1. Open the Discord app or a browser window for Discord login
2. Get an authorization code
3. Exchange it for an access token
4. Connect to Discord

**Building for mobile?** Account linking on iOS and Android works differently. See ACCOUNT-LINKING.md
→ Account Linking on Mobile, then return here.

**Choosing your OAuth2 scopes:** this guide uses `Client.GetDefaultPresenceScopes()`, which requests
the `openid` and `sdk.social_layer_presence` scopes. These enable core features like account linking,
friends list, and rich presence. If your game also needs lobbies, voice chat, or direct messaging, use
`Client.GetDefaultCommunicationScopes()` instead. See CORE-CONCEPTS.md → OAuth2 Scopes.

Add this code to `DiscordManager.cs`:

```cs
private void StartOAuthFlow() {
    var authorizationVerifier = client.CreateAuthorizationCodeVerifier();
    codeVerifier = authorizationVerifier.Verifier();

    var args = new AuthorizationArgs();
    args.SetClientId(clientId);
    args.SetScopes(Client.GetDefaultPresenceScopes());
    args.SetCodeChallenge(authorizationVerifier.Challenge());
    client.Authorize(args, OnAuthorizeResult);
}

private void OnAuthorizeResult(ClientResult result, string code, string redirectUri) {
    Debug.Log($"Authorization result: [{result.Error()}] [{code}] [{redirectUri}]");
    if (!result.Successful()) {
        return;
    }
    GetTokenFromCode(code, redirectUri);
}

private void GetTokenFromCode(string code, string redirectUri) {
    client.GetToken(clientId,
                    code,
                    codeVerifier,
                    redirectUri,
                    (result, token, refreshToken, tokenType, expiresIn, scope) => {});
}
```

Then uncomment `loginButton.onClick.AddListener(StartOAuthFlow);` in your `Start()` method:

```cs
if (loginButton != null)
{
    loginButton.onClick.AddListener(StartOAuthFlow);
}
```

### What's Happening Here?

1. Create a code verifier for OAuth2 PKCE security.
2. Set up authorization arguments with your app ID and required scopes.
3. Start the auth flow with `Client::Authorize`, which opens a browser.
4. When authorized, exchange the code for an access token.

**Warning: never log or store access tokens insecurely!** Treat them as sensitive credentials.

### Testing It Out

Press play and click the button — it should start the OAuth flow. You'll be redirected to your browser
to log in and authorize the game. There will be some logging to the console, but the status won't
change yet.

### Troubleshooting

- Make sure you've uncommented `loginButton.onClick.AddListener(StartOAuthFlow);` if the button
  doesn't seem to do anything.
- Double check your `ClientId` is correct.
- Ensure you've added the redirect URL in your Discord Developer Portal.
- Check the console for specific error messages.

---

## Step 8: Connect the SDK to Discord

Add this code to `DiscordManager.cs`:

```cs
private void OnReceivedToken(string token) {
    Debug.Log("Token received: " + token);
    client.UpdateToken(AuthorizationTokenType.Bearer, token, (ClientResult result) => { client.Connect(); });
}

private void OnRetrieveTokenFailed() { statusText.text = "Failed to retrieve token"; }
```

Then update `GetTokenFromCode` to call these functions when it completes:

```cs
private void GetTokenFromCode(string code, string redirectUri) {
    client.GetToken(clientId,
                    code,
                    codeVerifier,
                    redirectUri,
                    (result, token, refreshToken, tokenType, expiresIn, scope) => {
                        if (token != "") {
                            OnReceivedToken(token);
                        } else {
                            OnRetrieveTokenFailed();
                        }
                    });
}
```

### What's Happening Here?

1. `Client::UpdateToken` tells the SDK to use your access token for Discord API calls.
2. Once the token is updated, `Client::Connect` is called in the callback.
3. The SDK will begin connecting asynchronously.
4. Your status text will tell you when the SDK is ready.

### Testing the Connection

Press play and click the button again to log in and authorize the game. This time the status text
should change as it goes through the OAuth flow, and it should end up `Ready`.

### Troubleshooting

If you don't see `Ready` status:

- Check that your access token is valid.
- Ensure you have internet connectivity.
- Look for error messages from the SDK in the console.
- Verify your `ClientID` set in the inspector is correct.

---

## Step 9: Access Discord Relationships

Add:

```cs
private void ClientReady()
{
    Debug.Log($"Friend Count: {client.GetRelationships().Count()}");
}
```

Call this when the client is ready, from `OnStatusChanged`:

```cs
private void OnStatusChanged(Client.Status status, Client.Error error, int errorCode)
{
    Debug.Log($"Status changed: {status}");
    statusText.text = status.ToString();
    if(error != Client.Error.None)
    {
        Debug.LogError($"Error: {error}, code: {errorCode}");
    }

    if (status == Client.Status.Ready)
    {
        ClientReady();
    }
}
```

### What This Code Does

When the client status is `Ready`, it calls `ClientReady`, which calls `Client::GetRelationships`,
returning a list of all the player's friends. The number of friends is logged directly to the console.
Note the `System.Linq` using — `Count()` is a LINQ extension.

### Example Output

```
Friend Count: 42
```

### Troubleshooting

- Verify your OAuth2 scopes include relationships access.
- Ensure you're connected (status is `Ready`).
- Check that you have friends on Discord.
- Look for errors in the logging callback.

---

## Step 10: Set Rich Presence

Update `ClientReady`:

```cs
private void ClientReady()
{
    Debug.Log($"Friend Count: {client.GetRelationships().Count()}");

    Activity activity = new Activity();
    activity.SetType(ActivityTypes.Playing);
    activity.SetState("In Competitive Match");
    activity.SetDetails("Rank: Diamond II");
    client.UpdateRichPresence(activity, (ClientResult result) => {
        if (result.Successful()) {
            Debug.Log("Rich presence updated!");
        } else {
            Debug.LogError("Failed to update rich presence");
        }
    });
}
```

### What This Code Does

1. Creates an `Activity` object to represent what the player is doing.
2. Sets basic information like:
   - The activity type (Playing)
   - Current state ("In Competitive Match")
   - Additional details ("Rank: Diamond II")
3. Updates your rich presence on Discord.

### Testing It Out

Hit play and click the button. Once the OAuth flow is complete, the status will hit `Ready`. The
console will tell you if setting rich presence was successful, and you can check your Discord profile
to see it.

### Troubleshooting

If you don't see your presence:

- Ensure you're connected (status is `Ready`).
- Check the console for error messages.
- Verify your activity settings are valid.
- Make sure you're not invisible on Discord.

---

## The full DiscordManager.cs

Verbatim from upstream (indentation quirks included — `void Start()` is over-indented in the source):

```cs
using UnityEngine;
using UnityEngine.UI;
using Discord.Sdk;
using System.Linq;

public class DiscordManager : MonoBehaviour
{
    [SerializeField] 
    private ulong clientId; // Set this in the Unity Inspector from the dev portal
    
    [SerializeField]
    private Button loginButton; 
    
    [SerializeField] 
    private Text statusText;

    private Client client;
    private string codeVerifier;

        void Start()
    {
        client = new Client();

        // Modifying LoggingSeverity will show you more or less logging information
        client.AddLogCallback(OnLog, LoggingSeverity.Error);
        client.SetStatusChangedCallback(OnStatusChanged);

        // Make sure the button has a listener
        if (loginButton != null)
        {
            loginButton.onClick.AddListener(StartOAuthFlow);
        }
        else
        {
            Debug.LogError("Login button reference is missing, connect it in the inspector!");
        }

        // Set initial status text
        if (statusText != null)
        {
            statusText.text = "Ready to login";
        }
        else
        {
            Debug.LogError("Status text reference is missing, connect it in the inspector!");
        }
    }

    private void OnLog(string message, LoggingSeverity severity)
    {
        Debug.Log($"Log: {severity} - {message}");
    }

    private void OnStatusChanged(Client.Status status, Client.Error error, int errorCode)
    {
        Debug.Log($"Status changed: {status}");
        statusText.text = status.ToString();
        if(error != Client.Error.None)
        {
            Debug.LogError($"Error: {error}, code: {errorCode}");
        }

        if (status == Client.Status.Ready)
        {
            ClientReady();
        }
    }

    private void ClientReady()
    {
            Debug.Log($"Friend Count: {client.GetRelationships().Count()}");

            Activity activity = new Activity();
            activity.SetType(ActivityTypes.Playing);
            activity.SetState("In Competitive Match");
            activity.SetDetails("Rank: Diamond II");
            client.UpdateRichPresence(activity, (ClientResult result) => {
                if (result.Successful()) {
                    Debug.Log("Rich presence updated!");
                } else {
                    Debug.LogError("Failed to update rich presence");
                }
            });
    }

    private void StartOAuthFlow() {
        var authorizationVerifier = client.CreateAuthorizationCodeVerifier();
        codeVerifier = authorizationVerifier.Verifier();
        
        var args = new AuthorizationArgs();
        args.SetClientId(clientId);
        args.SetScopes(Client.GetDefaultPresenceScopes());
        args.SetCodeChallenge(authorizationVerifier.Challenge());
        client.Authorize(args, OnAuthorizeResult);
    }

    private void OnAuthorizeResult(ClientResult result, string code, string redirectUri) {
        Debug.Log($"Authorization result: [{result.Error()}] [{code}] [{redirectUri}]");
        if (!result.Successful()) {
            return;
        }
        GetTokenFromCode(code, redirectUri);
    }

    private void GetTokenFromCode(string code, string redirectUri) {
        client.GetToken(clientId,
                        code,
                        codeVerifier,
                        redirectUri,
                        (result, token, refreshToken, tokenType, expiresIn, scope) => {
                            if (token != "") {
                                OnReceivedToken(token);
                            } else {
                                OnRetrieveTokenFailed();
                            }
                        });
    }

    private void OnReceivedToken(string token) {
        Debug.Log("Token received: " + token);
        client.UpdateToken(AuthorizationTokenType.Bearer, token, (ClientResult result) => { client.Connect(); });
    }

    private void OnRetrieveTokenFailed() { statusText.text = "Failed to retrieve token"; }
}
```

---

## Conclusion and next steps

### What You've Built

- Created a Discord application and configured OAuth2
- Set up SDK logging and status monitoring
- Implemented user authentication flow
- Retrieved Discord relationships data
- Added Rich Presence support

### Key Concepts Learned

- How to initialize and configure the Discord SDK
- Managing authentication and connections
- Working with Discord's social features
- Handling asynchronous callbacks
- Monitoring SDK status and events

### Social SDK Unity sample

An in-depth sample for using the Social SDK in Unity following the best practices in these guides:
`https://github.com/discord/social-sdk-unity-sample`. It contains easy to drop in prefabs with both
code and UI to quickly integrate Discord's social features into your game.
[Image: Video showing off the Unity sample with the Discord Social SDK]

(For the mobile scene in that sample, see CORE-CONCEPTS.md → Discord Social SDK on Mobile.)

### Next Steps

- **Creating a Unified Friends List** — see RELATIONSHIPS-AND-FRIENDS.md.
- **Setting Rich Presence** — see RICH-PRESENCE.md.
- **Managing Game Invites** — see RELATIONSHIPS-AND-FRIENDS.md.

Need help? Join the Discord Developers Server (`https://discord.gg/discord-developers`),
`#social-sdk-dev-help` channel. Bug reports: `https://dis.gd/social-sdk-bug-report`.

---

## Symbols used in this guide

| Symbol | Reference doc anchor (base `https://discord.com/developers/docs/social-sdk/`) |
| --- | --- |
| `Activity` | `classdiscordpp_1_1Activity.html#ae793d9adbe16fef402b859ba02bee682` |
| `Client::Authorize` | `classdiscordpp_1_1Client.html#ace94a58e27545a933d79db32b387a468` |
| `Client::Connect` | `classdiscordpp_1_1Client.html#a873a844c7c4c72e9e693419bb3e290aa` |
| `Client::GetRelationships` | `classdiscordpp_1_1Client.html#ad481849835cd570f0e03adafcf90125d` |
| `Client::UpdateToken` | `classdiscordpp_1_1Client.html#a606b32cef7796f7fb91c2497bc31afc4` |
| `RunCallbacks` | `namespacediscordpp.html#ab5dd8cf274f581ee1885de5816be3c29` |

C# API surface used, unlinked upstream: `Client` (constructor `new Client()`),
`Client.AddLogCallback(callback, LoggingSeverity)`, `Client.SetStatusChangedCallback(callback)`,
`Client.CreateAuthorizationCodeVerifier()` returning an object with `Verifier()` and `Challenge()`,
`AuthorizationArgs` with `SetClientId(ulong)`, `SetScopes(string)`, `SetCodeChallenge(...)`,
`Client.GetDefaultPresenceScopes()`, `Client.GetDefaultCommunicationScopes()`,
`Client.Authorize(args, callback)`,
`Client.GetToken(clientId, code, codeVerifier, redirectUri, (result, token, refreshToken, tokenType, expiresIn, scope) => …)`,
`Client.UpdateToken(AuthorizationTokenType.Bearer, token, callback)`, `Client.Connect()`,
`Client.GetRelationships()`, `Client.UpdateRichPresence(activity, callback)`,
`ClientResult.Successful()`, `ClientResult.Error()`, `Client.Status.Ready`, `Client.Error.None`,
`LoggingSeverity.Error`, `ActivityTypes.Playing`, `Activity.SetType/SetState/SetDetails`.

---

## Change Log

| Date           | Changes         |
| -------------- | --------------- |
| March 17, 2025 | Initial release |
