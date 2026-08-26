# Gateway Receive Events — Voice, Webhooks, Interactions, Stages, Subscriptions

Every field of every receive event in the voice, webhook, interaction, stage instance, subscription
and application-command-permission domains.

Source: [Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved
2026-08-26.

## Contents

- [Application Command Permissions Update](#application-command-permissions-update)
- [Voice Channel Effect Send](#voice-channel-effect-send)
- [Voice State Update](#voice-state-update)
- [Voice Server Update](#voice-server-update)
- [Webhooks Update](#webhooks-update)
- [Interaction Create](#interaction-create)
- [Stage Instances](#stage-instances)
- [Subscriptions](#subscriptions)

Voice Channel Status Update and Voice Channel Start Time Update are documented in
`GATEWAY-EVENTS-GUILDS.md`, because upstream places them in the Channels section.

## Application Command Permissions Update

`APPLICATION_COMMAND_PERMISSIONS_UPDATE` event, sent when an application command's permissions are
updated. The inner payload is an application command permissions object (the Guild Application Command
Permissions structure). Call the Skill tool with "discord-interactions" for that object.

## Voice Channel Effect Send

Sent when someone sends an effect, such as an emoji reaction or a soundboard sound, in a voice channel
the current user is connected to.

###### Voice Channel Effect Send Event Fields

| Field           | Type                 | Description                                                                       |
| --------------- | -------------------- | --------------------------------------------------------------------------------- |
| channel_id      | snowflake            | ID of the channel the effect was sent in                                          |
| guild_id        | snowflake            | ID of the guild the effect was sent in                                            |
| user_id         | snowflake            | ID of the user who sent the effect                                                |
| emoji?          | ?emoji object        | The emoji sent, for emoji reaction and soundboard effects                         |
| animation_type? | ?integer             | The type of emoji animation, for emoji reaction and soundboard effects            |
| animation_id?   | integer              | The ID of the emoji animation, for emoji reaction and soundboard effects          |
| sound_id?       | snowflake or integer | The ID of the soundboard sound, for soundboard effects                            |
| sound_volume?   | double               | The volume of the soundboard sound, from 0 to 1, for soundboard effects           |

###### Animation Types

| Type    | Value | Description                                 |
| ------- | ----- | ------------------------------------------- |
| PREMIUM | 0     | A fun animation, sent by a Nitro subscriber |
| BASIC   | 1     | The standard animation                      |

## Voice State Update

Sent when someone joins/leaves/moves voice channels. Inner payload is a voice state object. Call the
Skill tool with "discord-rest" for the voice state object.

## Voice Server Update

Sent when a guild's voice server is updated. This is sent when initially connecting to voice, and when
the current voice instance fails over to a new server.

Warning: a null endpoint means that the voice server allocated has gone away and is trying to be
reallocated. You should attempt to disconnect from the currently connected voice server, and not
attempt to reconnect until a new voice server is allocated.

###### Voice Server Update Event Fields

| Field    | Type      | Description                           |
| -------- | --------- | ------------------------------------- |
| token    | string    | Voice connection token                |
| guild_id | snowflake | Guild this voice server update is for |
| endpoint | ?string   | Voice server host                     |

###### Example Voice Server Update Payload

```json
{
  "token": "my_token",
  "guild_id": "41771983423143937",
  "endpoint": "sweetwater-12345.discord.media:2048"
}
```

## Webhooks Update

Sent when a guild channel's webhook is created, updated, or deleted.

###### Webhooks Update Event Fields

| Field      | Type      | Description       |
| ---------- | --------- | ----------------- |
| guild_id   | snowflake | ID of the guild   |
| channel_id | snowflake | ID of the channel |

## Interaction Create

`INTERACTION_CREATE` on the wire. Sent when a user uses an Application Command or Message Component. Inner payload is an Interaction
object (the Interaction structure). Call the Skill tool with "discord-interactions".

## Stage Instances

### Stage Instance Create

Sent when a Stage instance is created (i.e. the Stage is now "live"). Inner payload is a Stage
instance.

### Stage Instance Update

Sent when a Stage instance has been updated. Inner payload is a Stage instance.

### Stage Instance Delete

Sent when a Stage instance has been deleted (i.e. the Stage has been closed). Inner payload is a Stage
instance.

## Subscriptions

### Subscription Create

Info: subscription status should not be used to grant perks. Use entitlements as an indication of
whether a user should have access to a specific SKU. See the guide on Implementing App Subscriptions
for more information — call the Skill tool with "discord-monetization".

Sent when a Subscription for a Premium App is created. Inner payload is a Subscription object.

A Subscription's `status` can be either **inactive** or **active** when this event is received. You
will receive subsequent `SUBSCRIPTION_UPDATE` events if the `status` is updated to **active**. As a
best practice, you should not grant any perks to users until the entitlements are created.

### Subscription Update

Sent when a Subscription for a Premium App has been updated. Inner payload is a Subscription object.

### Subscription Delete

Sent when a Subscription for a Premium App has been deleted. Inner payload is a Subscription object.

## Source

Discord Developer Documentation,
[Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved 2026-08-26.
