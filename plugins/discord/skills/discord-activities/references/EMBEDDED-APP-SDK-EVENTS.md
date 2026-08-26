# Embedded App SDK — Events, Interfaces and Enums

All 13 SDK events with their required scopes and sample payloads, all 58 SDK interfaces with every
property and type, and all 10 SDK enums with every value. Commands and installation are in
`EMBEDDED-APP-SDK-COMMANDS.md`.

Source: `https://docs.discord.com/developers/developer-tools/embedded-app-sdk`, retrieved 2026-08-26.

## Contents

- [SDK Events](#sdk-events) — the 13-event table, then one section per event
- [SDK Interfaces](#sdk-interfaces) — 58 interfaces, alphabetical as upstream
- [SDK Enums](#sdk-enums) — `ChannelTypesObject`, `ConsoleLevel`,
  `OrientationLockStateTypeObject`, `ThermalStateTypeObject`, `OrientationTypeObject`,
  `LayoutModeTypeObject`, `OAuthScopes`, `RPCCloseCodes`, `SkuTypeObject`, `Relationship Types`

## SDK Events

Developers may use the following events alongside the `subscribe()` SDK method to subscribe to events
from Discord and supported devices.

| Name | Description |
| --- | --- |
| READY | non-subscription event sent immediately after connecting, contains server information |
| ERROR | non-subscription event sent when there is an error, including command responses |
| VOICE_STATE_UPDATE | sent when a user's voice state changes in a subscribed voice channel (mute, volume, etc.) |
| SPEAKING_START | sent when a user in a subscribed voice channel speaks |
| SPEAKING_STOP | sent when a user in a subscribed voice channel stops speaking |
| ACTIVITY_LAYOUT_MODE_UPDATE | Received when a user changes the layout mode in the Discord client |
| ORIENTATION_UPDATE | Received when screen orientation changes |
| CURRENT_USER_UPDATE | Received when the current user object changes |
| CURRENT_GUILD_MEMBER_UPDATE | Received when the current guild member object changes |
| THERMAL_STATE_UPDATE | Received when Android or iOS thermal states are surfaced to the Discord app |
| ACTIVITY_INSTANCE_PARTICIPANTS_UPDATE | Received when the number of instance participants changes |
| RELATIONSHIP_UPDATE | Received when a relationship of the current user is updated |
| ENTITLEMENT_CREATE | Received when an entitlement is created for a SKU |

A fourteenth event, `ACTIVITY_PIP_MODE_UPDATE`, is **not** in this table but is named in the Layout
development guide: old Discord clients only support `ACTIVITY_PIP_MODE_UPDATE`, while new clients
support both it and `ACTIVITY_LAYOUT_MODE_UPDATE`. Use `subscribeToLayoutModeUpdatesCompat` /
`unsubscribeFromLayoutModeUpdatesCompat` to cover both. Upstream states no payload for it.

### READY

Non-subscription event sent immediately after connecting, contains server information.

#### Required Scopes

No scopes required

#### Sample Event Payload

```javascript
{
  "v": 1,
  "config": {
      "cdn_host": "cdn.discordapp.com",
      "api_endpoint": "//discord.com/api",
      "environment": "production"
  }
}
```

### ERROR

Non-subscription event sent when there is an error, including command responses.

#### Required Scopes

No scopes required

#### Sample Event Payload

```javascript
{
  "code": 4006,
  "message": "Not authenticated or invalid scope"
}
```

### VOICE_STATE_UPDATE

Received when a user's voice state changes in a subscribed voice channel (mute, volume, etc).

#### Required Scopes

- `rpc.voice.read`

#### Sample Event Payload

```javascript
{
  "voice_state": {
    "mute": false,
    "deaf": false,
    "self_mute": false,
    "self_deaf": false,
    "suppress": false
  },
  "user": {
    "id": "190320984123768832",
    "username": "test 2",
    "discriminator": "7479",
    "avatar": "b004ec1740a63ca06ae2e14c5cee11f3",
    "bot": false
  },
  "nick": "test user 2",
  "volume": 110,
  "mute": false,
  "pan": {
    "left": 1.0,
    "right": 1.0
  }
}
```

### SPEAKING_START

Received when a user in a subscribed voice channel speaks.

#### Required Scopes

- `rpc.voice.read`

#### Sample Event Payload

```javascript
{
  "channel_id": "7173758092142710784",
  "user_id": "7173758143913005056"
}
```

### SPEAKING_STOP

Received when a user in a subscribed voice channel stops speaking.

#### Required Scopes

- `rpc.voice.read`

#### Sample Event Payload

```javascript
{
  "channel_id": "7173758211307081728",
  "user_id": "7173758261412237312"
}
```

### ACTIVITY_LAYOUT_MODE_UPDATE

Received when a user changes the layout mode in the Discord client.

#### Required Scopes

No scopes required

#### Sample Event Payload

```javascript
{
  "layout_mode": 1
}
```

Values are `LayoutModeTypeObject`: `-1` UNHANDLED, `0` FOCUSED, `1` PIP, `2` GRID.

### ORIENTATION_UPDATE

Received when screen orientation changes.

#### Required Scopes

No scopes required

#### Sample Event Payload

```javascript
{
  "screen_orientation": 1
}
```

Values are `OrientationTypeObject`: `-1` UNHANDLED, `0` PORTRAIT, `1` LANDSCAPE. Discord publishes
the current orientation upon event subscription, and also publishes later changes.

### CURRENT_USER_UPDATE

Received when the current user object changes.

#### Required Scopes

- `identify`

#### Sample Event Payload

```javascript
{
  "id": "7173771622812225536",
  "username": "beef_supreme",
  "discriminator": "0",
  "global_name": "Dis Cord",
  "avatar": "abcdefg",
  "avatar_decoration_data": {
    "asset": "abcdefg",
    "sku_id": "123456789"
  },
  "bot": false,
  "flags": 1,
  "premium_type": 2
}
```

### CURRENT_GUILD_MEMBER_UPDATE

Received when the current guild member object changes.

#### Required Scopes

- `identify`
- `guilds.members.read`

#### Sample Event Payload

The missing comma after `guild_id` is as printed upstream.

```javascript
{
  "user_id": "7173771622812225536",
  "nick": "beef_supreme",
  "guild_id": "613425648685547541"
  "avatar": "abcdefg",
  "avatar_decoration_data": {
    "asset": "abcdefg",
    "sku_id": "123456789"
  },
  "color_string": "#ffff00"
}
```

### THERMAL_STATE_UPDATE

Received when Android or iOS thermal states are surfaced to the Discord mobile app.

#### Required Scopes

No scopes required

#### Sample Event Payload

```javascript
{
  thermal_state: 0
}
```

Values are `ThermalStateTypeObject`. Platform mapping and the subscription example are in
`DEVELOPMENT-GUIDES.md` under Mobile.

### ACTIVITY_INSTANCE_PARTICIPANTS_UPDATE

Received when the number of instance participants changes.

#### Required Scopes

No scopes required

#### Sample Event Payload

```javascript
{
  "participants": [
    {
      "id": "7173771622812225536",
      "username": "beef_supreme",
      "discriminator": "0",
      "global_name": "Dis Cord",
      "avatar": "abcdefg",
      "avatar_decoration_data": {
        "asset": "abcdefg",
        "sku_id": "123456789"
      },
      "bot": false,
      "flags": 1,
      "premium_type": 2
    }
  ]
}
```

### RELATIONSHIP_UPDATE

Received when a relationship of the current user is updated.

#### Required Scopes

- `relationships.read`

This scope is part of Discord's Social SDK — submit for access at
`https://discord.com/developers/applications/select/social-sdk/getting-started`. Social SDK Terms
apply (`https://support-dev.discord.com/hc/en-us/articles/30225844245271-Discord-Social-SDK-Terms`),
including Section 5(a)(ii) to the data you obtain.

#### Sample Event Payload

```javascript
{
  "type": 1,
  "user": {
      "id": "7173771622812225536",
      "username": "beef_supreme",
      "discriminator": "0",
      "global_name": "Dis Cord",
      "avatar": "abcdefg",
      "avatar_decoration_data": {
        "asset": "abcdefg",
        "sku_id": "123456789"
      },
      "bot": false,
      "flags": 1,
      "premium_type": 2
  }
}
```

### ENTITLEMENT_CREATE

Upstream states only: "Coming soon! Not available during Developer Preview". No required scopes and no
sample payload are given.

## SDK Interfaces

Types are reproduced exactly as upstream, including optional markers (`?`) and nullability.

#### Activity

| Property | Type |
| --- | --- |
| name | string |
| type | number |
| url? | string \| null |
| created_at? | number \| null |
| timestamps? | Timestamp \| null |
| application_id? | string \| null |
| details? | string \| null |
| details_url? | string \| null |
| state? | string \| null |
| state_url? | string \| null |
| emoji? | Emoji \| null |
| party? | Party \| null |
| assets? | Assets \| null |
| secrets? | Secrets \| null |
| instance? | boolean \| null |
| flags? | number \| null |

#### Assets

| Property | Type |
| --- | --- |
| large_image? | string \| null |
| large_text? | string \| null |
| large_url? | string \| null |
| small_image? | string \| null |
| small_text? | string \| null |
| small_url? | string \| null |

#### Application

| Property | Type |
| --- | --- |
| description | string |
| icon? | string \| null |
| id | string |
| rpc_origins? | string[] |
| name | string |

#### Attachment

| Property | Type |
| --- | --- |
| id | string |
| filename | string |
| size | number |
| url | string |
| proxy_url | string |
| height? | number \| null |
| width? | number \| null |

#### AuthenticateRequest

| Property | Type |
| --- | --- |
| access_token? | string \| null |

#### AuthenticateResponse

| Property | Type |
| --- | --- |
| access_token | string |
| user | User |
| scopes | string[] |
| expires | string |
| application | Application |

#### AuthorizeRequest

| Property | Type |
| --- | --- |
| client_id | string |
| scope | OAuthScopes[] |
| response_type? | 'code' |
| code_challenge? | string |
| state? | string |
| prompt? | 'none' |
| code_challenge_method? | 'S256' |

#### AuthorizeResponse

| Property | Type |
| --- | --- |
| code | string |

#### AvatarDecorationData

| Property | Type |
| --- | --- |
| asset | string |
| sku_id? | string \| null |

#### CaptureLogRequest

| Property | Type |
| --- | --- |
| level | ConsoleLevel |
| message | string |

#### ChannelMention

| Property | Type |
| --- | --- |
| id | string |
| guild_id | string |
| type | number |
| name | string |

#### Embed

| Property | Type |
| --- | --- |
| title? | string \| null |
| type? | string \| null |
| description? | string \| null |
| url? | string \| null |
| timestamp? | string \| null |
| color? | number \| null |
| footer? | EmbedFooter \| null |
| image? | Image \| null |
| thumbnail? | Image \| null |
| video? | Video \| null |
| provider? | EmbedProvider \| null |
| author? | EmbedAuthor \| null |
| fields? | EmbedField[] \| null |

#### EmbedAuthor

| Property | Type |
| --- | --- |
| name? | string \| null |
| url? | string \| null |
| icon_url? | string \| null |
| proxy_icon_url? | string \| null |

#### EmbedField

| Property | Type |
| --- | --- |
| name | string |
| value | string |
| inline | boolean |

#### EmbedFooter

| Property | Type |
| --- | --- |
| text | string |
| icon_url? | string \| null |
| proxy_icon_url? | string \| null |

#### EmbedProvider

| Property | Type |
| --- | --- |
| name? | string \| null |
| url? | string \| null |

#### Emoji

| Property | Type |
| --- | --- |
| id | string |
| name? | string \| null |
| roles? | string[] \| null |
| user? | User \| null |
| require_colons? | boolean \| null |
| managed? | boolean \| null |
| animated? | boolean \| null |
| available? | boolean \| null |

#### EncourageHardwareAccelerationResponse

| Property | Type |
| --- | --- |
| enabled | boolean |

#### Entitlement

| Property | Type |
| --- | --- |
| id | string |
| sku_id | string |
| application_id | string |
| user_id | string |
| gift_code_flags | number |
| type | string \| number |
| gifter_user_id? | string \| null |
| branches? | string[] \| null |
| starts_at? | string \| null |
| ends_at? | string \| null |
| parent_id? | string \| null |
| consumed? | boolean \| null |
| deleted? | boolean \| null |
| gift_code_batch_id? | string \| null |

#### GetChannelPermissionsResponse

| Property | Type |
| --- | --- |
| permissions | bigint \| string |

#### GetChannelRequest

| Property | Type |
| --- | --- |
| channel_id | string |

#### GetChannelResponse

| Property | Type |
| --- | --- |
| id | string |
| type | ChannelTypesObject |
| guild_id? | string \| null |
| name? | string \| null |
| topic? | string \| null |
| bitrate? | number \| null |
| user_limit? | number \| null |
| position? | number \| null |
| voice_states | UserVoiceState[] |
| messages | Message[] |

#### GetEntitlementsResponse

| Property | Type |
| --- | --- |
| entitlements | Entitlement[] |

#### GetInstanceConnectedParticipantsResponse

| Property | Type |
| --- | --- |
| participants | User[] |

The Multiplayer Experience guide refers to the same shape by the type name
`Types.GetActivityInstanceConnectedParticipantsResponse`.

#### GetPlatformBehaviorsResponse

| Property | Type |
| --- | --- |
| iosKeyboardResizesView? | boolean |

#### GetRelationshipsResponse

| Property | Type |
| --- | --- |
| relationships | Relationship[] |

#### GetSkusResponse

| Property | Type |
| --- | --- |
| skus | Sku[] |

#### GuildMember

| Property | Type |
| --- | --- |
| user | User |
| nick? | string \| null |
| roles | string[] |
| joined_at | string |
| deaf | boolean |
| mute | boolean |

#### GuildMemberRPC

| Property | Type |
| --- | --- |
| user_id | string |
| nick? | string \| null |
| guild_id | string |
| avatar? | string \| null |
| avatar_decoration_data? | AvatarDecorationData \| null |
| color_string? | string \| null |

#### Image

| Property | Type |
| --- | --- |
| url? | string \| null |
| proxy_url? | string \| null |
| height? | number \| null |
| width? | number \| null |

#### InitiateImageUploadResponse

| Property | Type |
| --- | --- |
| image_url | string |

#### Message

Upstream renders this table with a stray third column; the `nonce` row's type is split across it as
`string` / `number | null`, i.e. `string | number | null`.

| Property | Type |
| --- | --- |
| id | string |
| channel_id | string |
| guild_id? | string \| null |
| author? | User \| null |
| member? | GuildMember \| null |
| content | string |
| timestamp | string |
| edited_timestamp? | string \| null |
| tts | boolean |
| mention_everyone | boolean |
| mentions | User[] |
| mention_roles | string[] |
| mention_channels | ChannelMention[] |
| attachments | Attachment[] |
| embeds | Embed[] |
| reactions? | Reaction[] \| null |
| nonce? | string \| number \| null |
| pinned | boolean |
| webhook_id? | string \| null |
| type | number |
| activity? | MessageActivity \| null |
| application? | MessageApplication \| null |
| message_reference? | MessageReference \| null |
| flags? | number |
| stickers? | Sticker[] \| null |
| referenced_message? | Message \| null |

`Sticker` is referenced but has no interface table of its own upstream.

#### MessageActivity

| Property | Type |
| --- | --- |
| type | number |
| party_id? | string \| null |

#### MessageApplication

| Property | Type |
| --- | --- |
| id | string |
| cover_image? | string \| null |
| description | string |
| icon? | string \| null |
| name | string |

#### MessageReference

| Property | Type |
| --- | --- |
| message_id? | string \| null |
| channel_id? | string \| null |
| guild_id? | string \| null |

#### OpenExternalLinkRequest

| Property | Type |
| --- | --- |
| url | string |

#### OpenExternalLinkResponse

**Warning (upstream):** `{ opened: null }` is returned on Discord clients before December 2024 that
do not report the open link result.

| Property | Type |
| --- | --- |
| opened | boolean \| null |

#### OpenShareMomentDialogRequest

| Property | Type |
| --- | --- |
| mediaUrl | string |

#### Party

| Property | Type |
| --- | --- |
| id? | string \| null |
| size? | number[] \| null |

#### Reaction

| Property | Type |
| --- | --- |
| count | number |
| me | boolean |
| emoji | Emoji |

#### Relationship

| Property | Type |
| --- | --- |
| type | number (see Relationship Types) |
| user | User |

#### Secrets

| Property | Type |
| --- | --- |
| join? | string |
| match? | string |

#### SetActivityRequest

| Property | Type |
| --- | --- |
| activity | Activity |

#### SetConfigRequest

| Property | Type |
| --- | --- |
| use_interactive_pip | boolean |

#### SetConfigResponse

| Property | Type |
| --- | --- |
| use_interactive_pip | boolean |

#### SetOrientationLockStateRequest

| Property | Type |
| --- | --- |
| lock_state | OrientationLockState (see OrientationLockStateTypeObject) |
| picture_in_picture_lock_state | OrientationLockState |
| grid_lock_state | OrientationLockState |

#### ShareLinkRequest

| Property | Type |
| --- | --- |
| custom_id? | string |
| message | string |

See the `shareLink()` note in `EMBEDDED-APP-SDK-COMMANDS.md`: an upstream example also passes
`link_id`, which this table does not list.

#### ShareLinkResponse

| Property | Type |
| --- | --- |
| success | boolean |

#### Sku

| Property | Type |
| --- | --- |
| id | string |
| name | string |
| type | SkuTypeObject |
| price | SkuPrice |
| application_id | string |
| flags | number |
| release_date | string \| null |

#### SkuPrice

| Property | Type |
| --- | --- |
| amount | number |
| currency | string |

#### StartPurchaseRequest

| Property | Type |
| --- | --- |
| sku_id | string |

#### StartPurchaseResponse

| Value |
| --- |
| Entitlement[] \| null |

#### Timestamp

| Property | Type |
| --- | --- |
| start? | number |
| end? | number |

#### User

| Property | Type |
| --- | --- |
| id | string |
| username | string |
| discriminator | string |
| global_name? | string \| null |
| avatar? | string \| null |
| avatar_decoration_data | AvatarDecorationData \| null |
| bot | boolean |
| flags? | number \| null |
| premium_type? | number \| null |

#### UserSettingsGetLocaleResponse

| Property | Type |
| --- | --- |
| locale | string |

#### UserVoiceState

| Property | Type |
| --- | --- |
| mute | boolean |
| nick | string |
| user | User |
| voice_state | VoiceState |
| volume | number |

#### Video

| Property | Type |
| --- | --- |
| url? | string \| null |
| height? | number \| null |
| width? | number \| null |

#### VoiceState

| Property | Type |
| --- | --- |
| mute | boolean |
| deaf | boolean |
| self_mute | boolean |
| self_deaf | boolean |
| suppress | boolean |

## SDK Enums

#### ChannelTypesObject

Values are listed in upstream's order, which is not numeric.

| Name | Value |
| --- | --- |
| UNHANDLED | -1 |
| DM | 1 |
| GROUP_DM | 3 |
| GUILD_TEXT | 0 |
| GUILD_VOICE | 2 |
| GUILD_CATEGORY | 4 |
| GUILD_ANNOUNCEMENT | 5 |
| GUILD_STORE | 6 |
| ANNOUNCEMENT_THREAD | 10 |
| PUBLIC_THREAD | 11 |
| PRIVATE_THREAD | 12 |
| GUILD_STAGE_VOICE | 13 |
| GUILD_DIRECTORY | 14 |
| GUILD_FORUM | 15 |

#### ConsoleLevel

| Value |
| --- |
| 'error' |
| 'log' |
| 'warn' |
| 'debug' |
| 'info' |

#### OrientationLockStateTypeObject

| Name | Value |
| --- | --- |
| UNHANDLED | -1 |
| UNLOCKED | 1 |
| PORTRAIT | 2 |
| LANDSCAPE | 3 |

#### ThermalStateTypeObject

| Name | Value |
| --- | --- |
| UNHANDLED | -1 |
| NOMINAL | 0 |
| FAIR | 1 |
| SERIOUS | 2 |
| CRITICAL | 3 |

#### OrientationTypeObject

| Name | Value |
| --- | --- |
| UNHANDLED | -1 |
| PORTRAIT | 0 |
| LANDSCAPE | 1 |

#### LayoutModeTypeObject

| Name | Value |
| --- | --- |
| UNHANDLED | -1 |
| FOCUSED | 0 |
| PIP | 1 |
| GRID | 2 |

#### OAuthScopes

| Value |
| --- |
| 'bot' |
| 'rpc' |
| 'identify' |
| 'connections' |
| 'email' |
| 'guilds' |
| 'guilds.join' |
| 'guilds.members.read' |
| 'gdm.join' |
| 'messages.read' |
| 'rpc.notifications.read' |
| 'rpc.voice.write' |
| 'rpc.voice.read' |
| 'rpc.activities.write' |
| 'webhook.incoming' |
| 'applications.commands' |
| 'applications.builds.upload' |
| 'applications.builds.read' |
| 'applications.store.update' |
| 'applications.entitlements' |
| 'relationships.read' |
| 'activities.read' |
| 'activities.write' |
| 'dm_channels.read' |

#### RPCCloseCodes

| Name | Code |
| --- | --- |
| CLOSE_NORMAL | 1000 |
| CLOSE_UNSUPPORTED | 1003 |
| CLOSE_ABNORMAL | 1006 |
| INVALID_CLIENTID | 4000 |
| INVALID_ORIGIN | 4001 |
| RATELIMITED | 4002 |
| TOKEN_REVOKED | 4003 |
| INVALID_VERSION | 4004 |
| INVALID_ENCODING | 4005 |

The Production Readiness guide additionally names `RPCErrorCodes.INVALID_COMMAND`, returned when a
Discord client is too old to support a command. Upstream lists no numeric value for it on these pages.
The `ERROR` event sample shows code `4006` with message "Not authenticated or invalid scope", which is
also absent from this table.

#### SkuTypeObject

| Name | Value |
| --- | --- |
| UNHANDLED | -1 |
| APPLICATION | 1 |
| DLC | 2 |
| CONSUMABLE | 3 |
| BUNDLE | 4 |
| SUBSCRIPTION | 5 |

#### Relationship Types

| Value | Name | Description |
| --- | --- | --- |
| 0 | None | The user has no relationship with the other user. |
| 1 | Friend | The user is friends with the other user. |
| 2 | Blocked | The current user has blocked the target user. |
| 3 | Pending Incoming | The current user has received a friend request from the target user, but it is not yet accepted. |
| 4 | Pending Outgoing | The current user has sent a friend request to the target user, but it is not yet accepted. |
| 5 | Implicit | The Implicit type is documented for visibility, but should be unused in the SDK. |
| 6 | Suggestion | The Suggestion type is documented for visibility, but should be unused in the SDK. |

## Source

Discord Developer Documentation, `https://docs.discord.com/developers/developer-tools/embedded-app-sdk`,
retrieved 2026-08-26. `ACTIVITY_PIP_MODE_UPDATE` and `RPCErrorCodes.INVALID_COMMAND` come from
`https://docs.discord.com/developers/activities/development-guides/layout` and
`https://docs.discord.com/developers/activities/development-guides/production-readiness`.
