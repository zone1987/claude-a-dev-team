# Embedded App SDK — Installation, Methods and Commands

Complete reference for `@discord/embedded-app-sdk`: installation, the four SDK methods, and all 21
SDK commands with signatures, supported platforms, required scopes and usage examples. Events, types
and enums are in `EMBEDDED-APP-SDK-EVENTS.md`.

Source: `https://docs.discord.com/developers/developer-tools/embedded-app-sdk`, retrieved 2026-08-26.

## Contents

- [Install the SDK](#install-the-sdk)
- [SDK Methods](#sdk-methods) — `ready`, `subscribe`, `unsubscribe`, `close`
- [Additional SDK members documented on other pages](#additional-sdk-members-documented-on-other-pages)
- [SDK Commands](#sdk-commands) — the 21-command table
- [authenticate()](#authenticate) · [authorize()](#authorize) · [captureLog()](#capturelog)
- [encourageHardwareAcceleration()](#encouragehardwareacceleration) · [getChannel()](#getchannel)
- [getChannelPermissions()](#getchannelpermissions) · [getEntitlements()](#getentitlements)
- [getInstanceConnectedParticipants()](#getinstanceconnectedparticipants)
- [getPlatformBehaviors()](#getplatformbehaviors) · [getRelationships()](#getrelationships)
- [getSkus()](#getskus) · [initiateImageUpload()](#initiateimageupload)
- [openExternalLink()](#openexternallink) · [openInviteDialog()](#openinvitedialog)
- [openShareMomentDialog()](#opensharemomentdialog) · [setActivity()](#setactivity)
- [setConfig()](#setconfig) · [setOrientationLockState()](#setorientationlockstate)
- [shareLink()](#sharelink) · [startPurchase()](#startpurchase)
- [userSettingsGetLocale()](#usersettingsgetlocale)

## What the SDK is

The Embedded App SDK handles making RPC calls between your application and Discord. It is designed to
assist developers in developing interactive Activities like games.

The events and commands available in the Embedded App SDK are a subset of the RPC API ones, so
referencing the RPC documentation can be helpful to understand what is happening under the hood when
developing Activities.

## Install the SDK

The Embedded App SDK is available via **npm** (`https://www.npmjs.com/package/@discord/embedded-app-sdk`)
and **GitHub** (`https://github.com/discord/embedded-app-sdk`).

In your frontend JavaScript project directory, install using your package manager of choice.

```
npm install @discord/embedded-app-sdk
```

After installing, you can import and instantiate the SDK in your project.

```javascript
import { DiscordSDK } from "@discord/embedded-app-sdk";

const discordSdk = new DiscordSDK(DISCORD_CLIENT_ID);
```

## SDK Methods

| Name | Description |
| --- | --- |
| ready | Resolves when your app has successfully connected to the Discord client |
| subscribe | Subscribe to an Embedded App SDK Event |
| unsubscribe | Unsubscribe to an Embedded App SDK Event |
| close | Close an Embedded App |

### ready()

Resolves when your app has successfully connected to the Discord client.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`ready(): Promise<void>`

#### SDK Usage

```js
async function setup() {
  await discordSdk.ready();
  // The rest of your app logic
}
```

### subscribe()

Used to subscribe to a specific event from the list of SDK Events (see
`EMBEDDED-APP-SDK-EVENTS.md`).

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

Depends on the event. Refer to the Required Scopes for the specific event you are subscribing to.

#### Signature

`subscribe<Event>(event: Event, listener: (data: EventPayloadData<Event>) => void, ...subscribeArgs: Partial<EventPayloadData<Event>>): Promise<EventEmitter>`

`EventEmitter` is Node's `events.EventEmitter` (`https://nodejs.org/docs/latest/api/events.html`).

#### Usage

```js
await discordSdk.subscribe("SDK_EVENT_NAME", eventHandler, args);
```

### unsubscribe()

Used to unsubscribe to SDK Events that your app has already subscribed to.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

*The `EventPayloadData` will vary based on the event you are unsubscribing from. See the specific
event for details.*

`unsubscribe<Event>(event: Event, listener: (data: EventPayloadData<Event>) => void, ...subscribeArgs: Partial<EventPayloadData<Event>>): Promise<EventEmitter>`

#### Usage

```js
await discordSdk.unsubscribe("SDK_EVENT_NAME");
```

### close()

Used to close your app with a specified code and reason.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`close(code: RPCCloseCodes, message: string): void`

#### SDK Usage

```js
discordSdk.close(RPCCloseCodes.CLOSE_NORMAL, "You exited from app");
```

## Additional SDK members documented on other pages

The SDK reference page lists only the four methods above. These further members are documented on the
development-guide pages and are reproduced here so the SDK surface is complete in one place. Their
formal signatures are **not** stated upstream.

- **`discordSdk.instanceId`** — the current activity instance ID. Available as soon as the SDK is
  constructed; does not require the `ready` payload. (Multiplayer Experience guide.)
- **`discordSdk.channelId`** — the channel the Activity runs in; may be `null`. Used as
  `getChannel({channel_id: discordSdk.channelId})`. (Building an Activity, Step 6.)
- **`discordSdk.guildId`** — the guild the Activity runs in; `null` in GDMs. (Building an Activity.)
- **`discordSdk.customId`** — the `custom_id` query parameter of the incentivized link the user
  launched from. (Growth and Referrals guide.)
- **`discordSdk.referrerId`** — the `referrer_id` query parameter, a Discord snowflake user ID.
  (Growth and Referrals guide.)
- **`discordSdk.subscribeToLayoutModeUpdatesCompat(handler)`** — subscribes to both
  `ACTIVITY_PIP_MODE_UPDATE` and `ACTIVITY_LAYOUT_MODE_UPDATE`, giving backward compatibility with
  old Discord clients that only support `ACTIVITY_PIP_MODE_UPDATE`. (Layout guide.)
- **`discordSdk.unsubscribeFromLayoutModeUpdatesCompat(handler)`** — the matching unsubscribe.
  (Layout guide.)
- **`patchUrlMappings(mappings)`** — a top-level export, not a method on the instance:
  `import {patchUrlMappings} from '@discord/embedded-app-sdk'`. Takes an array of
  `{prefix, target}` mappings. (Networking guide.)
- **`Permissions`, `PermissionUtils`** — top-level exports used as
  `PermissionUtils.can(Permissions.CREATE_INSTANT_INVITE, permissions)`. (User Actions guide.)
- **`Common`** — namespace holding the enum objects, e.g.
  `Common.OrientationLockStateTypeObject.LANDSCAPE`, `Common.ThermalStateTypeObject.NOMINAL`,
  `Common.OrientationTypeObject.PORTRAIT`.
- **`Events`, `Types`** — top-level exports: `Events.ACTIVITY_INSTANCE_PARTICIPANTS_UPDATE`,
  `Types.GetActivityInstanceConnectedParticipantsResponse`.
- **Constructor options object** — second argument to `new DiscordSDK(clientId, options)`. The only
  documented key is `disableConsoleLogOverride: boolean`, which stops the SDK forwarding console
  logs to Discord. (Local Development guide.)

## SDK Commands

Developers can use these commands to interact with the Discord client. The following SDK commands are
prefixed with `.commands`, such as, `discordSDK.commands.authenticate`.

| Name | Description |
| --- | --- |
| authenticate | Authenticate an existing client with your app |
| authorize | Authorize a new client with your app |
| captureLog | Forward logs to your own logger |
| encourageHardwareAcceleration | Presents a modal dialog to allow enabling of hardware acceleration |
| getChannel | Returns information about the channel, per the channel_id |
| getChannelPermissions | Returns permissions for the current user in the currently connected channel |
| getEntitlements | Returns a list of entitlements for the current user |
| getInstanceConnectedParticipants | Returns all participants connected to the instance |
| getPlatformBehaviors | Returns information about supported platform behaviors |
| getRelationships | Allows your app to access a user's Discord Friends list, their pending requests, and blocked users. This scope is part of our Social SDK — submit for access at `https://discord.com/developers/applications/select/social-sdk/getting-started`. Social SDK Terms apply (`https://support-dev.discord.com/hc/en-us/articles/30225844245271-Discord-Social-SDK-Terms`), including Section 5(a)(ii) to the data you obtain |
| getSkus | Returns a list of your app's SKUs |
| initiateImageUpload | Presents the file upload flow in the Discord client |
| openExternalLink | Allows for opening an external link from within the Discord client |
| openInviteDialog | Presents a modal dialog with Channel Invite UI without requiring additional OAuth scopes |
| openShareMomentDialog | Presents a modal dialog to share media to a channel or DM |
| setActivity | Modifies how your activity's rich presence is displayed in the Discord client |
| setConfig | Set whether or not the PIP (picture-in-picture) is interactive |
| setOrientationLockState | Set options for orientation and picture-in-picture (PIP) modes |
| shareLink | Presents a modal for the user to share a link to your activity with custom query params |
| startPurchase | Launches the purchase flow for a specific SKU, per the sku_id |
| userSettingsGetLocale | Returns the current user's locale |

### authenticate()

Authenticate an existing client with your app.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`authenticate(args: AuthenticateRequest): Promise<AuthenticateResponse>`

#### Usage

```js
await discordSdk.commands.authenticate({
  access_token: 'ACCESS_TOKEN_STRING'
});
```

### authorize()

Authorize a new client with your app.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`authorize(args: AuthorizeRequest): Promise<AuthorizeResponse>`

#### Usage

The upstream example keeps the unused scopes as comments; they are preserved here because they
enumerate what may be requested.

```js
await discordSdk.commands.authorize({
  client_id: DISCORD_CLIENT_ID,
  response_type: "code",
  state: "",
  prompt: "none",
  scope: [
    // "applications.builds.upload",
    // "applications.builds.read",
    // "applications.store.update",
    // "applications.entitlements",
    // "bot",
    "identify",
    // "connections",
    // "email",
    // "gdm.join",
    "guilds",
    // "guilds.join",
    // "guilds.members.read",
    // "messages.read",
    // "relationships.read",
    // 'rpc.activities.write',
    // "rpc.notifications.read",
    // "rpc.voice.write",
    // "rpc.voice.read",
    // "webhook.incoming",
  ],
});
```

### captureLog()

Forward logs to your own logger.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`captureLog(args: CaptureLogRequest): Promise<void>`

#### Usage

```js
await discordSdk.commands.captureLog({
  level: 'log',
  message: 'This is my log message!'
});
```

### encourageHardwareAcceleration()

Presents a modal dialog to allow enabling of hardware acceleration.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ⛔️ | ⛔️ |

#### Required Scopes

No scopes required

#### Signature

`encourageHardwareAcceleration(): Promise<EncourageHardwareAccelerationResponse>`

#### Usage

```js
await discordSdk.commands.encourageHardwareAcceleration();
```

### getChannel()

Returns information about the channel for a provided channel ID.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

- `[guilds]` for guild channels
- `[guilds, dm_channels.read]` for GDM channels. `dm_channels.read` requires approval from Discord.

#### Signature

`getChannel(args: GetChannelRequest): Promise<GetChannelResponse>`

#### Usage

```js
await discordSdk.commands.getChannel({
  channel_id: discordSdk.channelId,
});
```

### getChannelPermissions()

Returns permissions for the current user in the currently connected channel.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

- `guilds.members.read`

#### Signature

`getChannelPermissions(): Promise<GetChannelPermissionsResponse>`

#### Usage

```js
await discordSdk.commands.getChannelPermissions();
```

### getEntitlements()

Returns a list of entitlements for the current user.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`getEntitlements(): Promise<GetEntitlementsResponse>`

#### Usage

```js
await discordSdk.commands.getEntitlements();
```

### getInstanceConnectedParticipants()

Returns all participants connected to the instance.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`getInstanceConnectedParticipants(): Promise<GetInstanceConnectedParticipantsResponse>`

#### Usage

```js
await discordSdk.commands.getInstanceConnectedParticipants();
```

### getPlatformBehaviors()

Returns information about supported platform behaviors.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`getPlatformBehaviors(): Promise<GetPlatformBehaviorsResponse>`

#### Usage

```js
await discordSdk.commands.getPlatformBehaviors();
```

### getRelationships()

Returns the current user's relationships.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

- `relationships.read`

This scope is part of Discord's Social SDK — submit for access at
`https://discord.com/developers/applications/select/social-sdk/getting-started`. Social SDK Terms
apply (`https://support-dev.discord.com/hc/en-us/articles/30225844245271-Discord-Social-SDK-Terms`),
including Section 5(a)(ii) to the data you obtain.

#### Signature

`getRelationships(): Promise<GetRelationshipsResponse>`

#### Usage

```js
await discordSdk.commands.getRelationships();
```

### getSkus()

Returns a list of SKU objects. SKUs without prices are automatically filtered out.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`getSkus(): Promise<GetSkusResponse>`

#### Usage

```js
await discordSdk.commands.getSkus();
```

### initiateImageUpload()

Presents the file upload flow in the Discord client.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`initiateImageUpload(): Promise<InitiateImageUploadResponse>`

#### Usage

```js
await discordSdk.commands.initiateImageUpload();
```

### openExternalLink()

Allows for opening an external link from within the Discord client.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`openExternalLink(args: OpenExternalLinkRequest): Promise<OpenExternalLinkResponse>`

#### Usage

```js
await discordSdk.commands.openExternalLink({
  url: 'string url'
});
```

### openInviteDialog()

Presents a modal dialog with Channel Invite UI without requiring additional OAuth scopes.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`openInviteDialog(): Promise<void>`

#### Usage

```js
await discordSdk.commands.openInviteDialog();
```

### openShareMomentDialog()

Presents a modal dialog to share media to a channel or direct message.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ⛔️ | ⛔️ |

#### Required Scopes

No scopes required

#### Signature

`openShareMomentDialog(args: OpenShareMomentDialogRequest) Promise<void>`

(The missing `:` is as printed upstream.)

#### Usage

```js
await discordSdk.commands.openShareMomentDialog({
  mediaUrl: 'DISCORD_CDN_URL'
});
```

### setActivity()

Modifies how your Activity's Rich Presence data is displayed in the Discord client. The inner
`activity` field is a partial Activity object (the Gateway activity structure).

Read `RICH-PRESENCE-IN-ACTIVITIES.md` for more usage details.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

- `rpc.activities.write`

#### Signature

`setActivity(args: SetActivityRequest): Promise<Activity>`

#### Usage

```js
await discordSdk.commands.setActivity({
  activity: {
    type: 0,
    details: 'Details',
    state: 'Playing'
  }
});
```

### setConfig()

Set whether or not the PIP (picture-in-picture) is interactive.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ⛔️ | ⛔️ |

#### Required Scopes

No scopes required

#### Signature

`setConfig(args: SetConfigRequest): Promise<SetConfigResponse>`

#### Usage

```js
await discordSdk.commands.setConfig({
  use_interactive_pip: true
})
```

### setOrientationLockState()

Locks the application to specific orientations in each of the supported layout modes.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ⛔️ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`setOrientationLockState(args: SetOrientationLockStateRequest): Promise<void>`

#### Usage

```js
import {Common} from '@discord/embedded-app-sdk';

await discordSdk.commands.setOrientationLockState({
  lock_state: Common.OrientationLockStateTypeObject.LANDSCAPE,
  picture_in_picture_lock_state: Common.OrientationLockStateTypeObject.LANDSCAPE,
  grid_lock_state: Common.OrientationLockStateTypeObject.UNLOCKED
});
```

Fallback and null semantics are in `DEVELOPMENT-GUIDES.md` under Layout.

### shareLink()

Presents the user with a modal to share a link.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

No scopes required

#### Signature

`shareLink(args: ShareLinkRequest): Promise<ShareLinkResponse><void>`

(The trailing `<void>` is as printed upstream.)

#### Usage

```js
const { success } = await discordSdk.commands.shareLink({
  message: 'This message is shared alongside the link!',
  custom_id: 'some_custom_id',
});
success ? console.log('User shared link!') : console.log('User did not share link!');
```

**Undocumented argument, observed in an upstream example.** The `ShareLinkRequest` interface lists
only `custom_id?` and `message`, but the Growth and Referrals guide passes `link_id` instead of
`custom_id` when sharing a generated quick link:
`discordSdk.commands.shareLink({message: '...', link_id})`. The interface table does not mention
`link_id`; the discrepancy is upstream's.

### startPurchase()

Launches the purchase flow for a specific SKU ID.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ⛔️ | ⛔️ |

#### Required Scopes

No scopes required

#### Signature

`startPurchase(args: StartPurchaseRequest): Promise<StartPurchaseResponse>`

#### Usage

```js
await discordSdk.commands.startPurchase({sku_id: skuId});
```

### userSettingsGetLocale()

Returns the current user's locale.

#### Supported Platforms

| Web | iOS | Android |
| --- | --- | ------- |
| ✅ | ✅ | ✅ |

#### Required Scopes

- `identify`

#### Signature

`userSettingsGetLocale(): Promise<UserSettingsGetLocaleResponse>`

#### Usage

```js
await discordSdk.commands.userSettingsGetLocale();
```

## Source

Discord Developer Documentation, `https://docs.discord.com/developers/developer-tools/embedded-app-sdk`,
retrieved 2026-08-26. SDK members listed under "Additional SDK members" come from the pages cited on
each line.
