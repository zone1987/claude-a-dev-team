# Gateway Receive Events — Guilds, Channels, Threads, Entitlements

Every field of every receive event in the auto moderation, channel, thread, entitlement, guild,
integration and invite domains.

Source: [Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved
2026-08-26.

## Contents

- [Auto Moderation](#auto-moderation)
- [Channels](#channels)
- [Threads](#threads)
- [Channel Pins Update](#channel-pins-update)
- [Entitlements](#entitlements)
- [Guilds](#guilds)
- [Guild members](#guild-members)
- [Guild roles](#guild-roles)
- [Guild scheduled events](#guild-scheduled-events)
- [Guild soundboard sounds](#guild-soundboard-sounds)
- [Integrations](#integrations)
- [Invites](#invites)

## Auto Moderation

All Auto Moderation related events are only sent to bot users which have the `MANAGE_GUILD`
permission.

### Auto Moderation Rule Create

Sent when a rule is created. The inner payload is an auto moderation rule object.

### Auto Moderation Rule Update

Sent when a rule is updated. The inner payload is an auto moderation rule object.

### Auto Moderation Rule Delete

Sent when a rule is deleted. The inner payload is an auto moderation rule object.

### Auto Moderation Action Execution

Sent when a rule is triggered and an action is executed (e.g. when a message is blocked).

###### Auto Moderation Action Execution Event Fields

| Field                      | Type                          | Description                                                                      |
| -------------------------- | ----------------------------- | -------------------------------------------------------------------------------- |
| guild_id                   | snowflake                     | ID of the guild in which action was executed                                     |
| action                     | auto moderation action object | Action which was executed                                                        |
| rule_id                    | snowflake                     | ID of the rule which action belongs to                                           |
| rule_trigger_type          | trigger_type                  | Trigger type of rule which was triggered                                         |
| user_id                    | snowflake                     | ID of the user which generated the content which triggered the rule              |
| channel_id?                | snowflake                     | ID of the channel in which user content was posted                               |
| message_id?                | snowflake                     | ID of any user message which content belongs to *                                |
| alert_system_message_id?   | snowflake                     | ID of any system auto moderation messages posted as a result of this action **   |
| content ***                | string                        | User-generated text content                                                      |
| matched_keyword            | ?string                       | Word or phrase configured in the rule that triggered the rule                    |
| matched_content ***        | ?string                       | Substring in content that triggered the rule                                     |

\* `message_id` will not exist if message was blocked by Auto Moderation or content was not part of
any message

\*\* `alert_system_message_id` will not exist if this event does not correspond to an action with type
`SEND_ALERT_MESSAGE`

\*\*\* `MESSAGE_CONTENT` (`1 << 15`) gateway intent is required to receive the `content` and
`matched_content` fields

The auto moderation rule, action and trigger_type objects are REST resources; call the Skill tool with
"discord-rest".

## Channels

### Channel Create

Sent when a new guild channel is created, relevant to the current user. The inner payload is a
channel object.

### Channel Update

Sent when a channel is updated. The inner payload is a channel object. This is not sent when the field
`last_message_id` is altered. To keep track of the `last_message_id` changes, you must listen for
Message Create events (or Thread Create events for `GUILD_FORUM` and `GUILD_MEDIA` channels).

This event may reference roles or guild members that no longer exist in the guild.

### Channel Delete

Sent when a channel relevant to the current user is deleted. The inner payload is a channel object.

### Channel Info

Includes ephemeral data for channels in a guild. Sent in response to Request Channel Info.

###### Channel Info Structure

| Field    | Type                             | Description                              |
| -------- | -------------------------------- | ---------------------------------------- |
| guild_id | snowflake                        | The guild id                             |
| channels | array of channel info objects    | Ephemeral data for channels in the guild |

###### Channel Info Channel Structure

| Field              | Type      | Description                                                   |
| ------------------ | --------- | ------------------------------------------------------------- |
| id                 | snowflake | The channel id                                                |
| status?            | ?string   | The voice channel status                                      |
| voice_start_time?  | ?integer  | Unix timestamp (in seconds) of when the voice session started |

### Voice Channel Status Update

Sent when the voice channel status changes.

| Field    | Type      | Description                  |
| -------- | --------- | ---------------------------- |
| id       | snowflake | The channel id               |
| guild_id | snowflake | The guild id                 |
| status   | ?string   | The new voice channel status |

### Voice Channel Start Time Update

Sent when the voice channel start time changes.

| Field              | Type      | Description                                                   |
| ------------------ | --------- | ------------------------------------------------------------- |
| id                 | snowflake | The channel id                                                |
| guild_id           | snowflake | The guild id                                                  |
| voice_start_time?  | ?integer  | Unix timestamp (in seconds) of when the voice session started |

## Threads

### Thread Create

Sent when a thread is created, relevant to the current user, or when the current user is added to a
thread. The inner payload is a channel object.

* When a thread is created, includes an additional `newly_created` boolean field.
* When being added to an existing private thread, includes a thread member object.

### Thread Update

Sent when a thread is updated. The inner payload is a channel object. This is not sent when the field
`last_message_id` is altered. To keep track of the `last_message_id` changes, you must listen for
Message Create events.

### Thread Delete

Sent when a thread relevant to the current user is deleted. The inner payload is a subset of the
channel object, containing just the `id`, `guild_id`, `parent_id`, and `type` fields.

### Thread List Sync

Sent when the current user *gains* access to a channel.

###### Thread List Sync Event Fields

| Field        | Type                          | Description                                                                                                                                                                                                            |
| ------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| guild_id     | snowflake                     | ID of the guild                                                                                                                                                                                                        |
| channel_ids? | array of snowflakes           | Parent channel IDs whose threads are being synced. If omitted, then threads were synced for the entire guild. This array may contain channel_ids that have no active threads as well, so you know to clear that data.   |
| threads      | array of channel objects      | All active threads in the given channels that the current user can access                                                                                                                                              |
| members      | array of thread member objects| All thread member objects from the synced threads for the current user, indicating which threads the current user has been added to                                                                                     |

### Thread Member Update

Sent when the thread member object for the current user is updated. The inner payload is a thread
member object with an extra `guild_id` field. This event is documented for completeness, but unlikely
to be used by most bots. For bots, this event largely is just a signal that you are a member of the
thread.

###### Thread Member Update Event Extra Fields

| Field    | Type      | Description     |
| -------- | --------- | --------------- |
| guild_id | snowflake | ID of the guild |

### Thread Members Update

Sent when anyone is added to or removed from a thread. If the current user does not have the
`GUILD_MEMBERS` Gateway Intent, then this event will only be sent if the current user was added to or
removed from the thread.

###### Thread Members Update Event Fields

| Field               | Type                           | Description                                               |
| ------------------- | ------------------------------ | --------------------------------------------------------- |
| id                  | snowflake                      | ID of the thread                                          |
| guild_id            | snowflake                      | ID of the guild                                           |
| member_count        | integer                        | Approximate number of members in the thread, capped at 50 |
| added_members?*     | array of thread member objects | Users who were added to the thread                        |
| removed_member_ids? | array of snowflakes            | ID of the users who were removed from the thread          |

\* In this gateway event, the thread member objects will also include the guild member and nullable
presence objects for each added thread member.

## Channel Pins Update

Sent when a message is pinned or unpinned in a text channel. This is not sent when a pinned message is
deleted.

###### Channel Pins Update Event Fields

| Field               | Type               | Description                                             |
| ------------------- | ------------------ | ------------------------------------------------------- |
| guild_id?           | snowflake          | ID of the guild                                         |
| channel_id          | snowflake          | ID of the channel                                       |
| last_pin_timestamp? | ?ISO8601 timestamp | Time at which the most recent pinned message was pinned |

## Entitlements

### Entitlement Create

Warning: the `ENTITLEMENT_CREATE` event behavior changed on October 1, 2024. See the Change Log and
Entitlement Migration Guide for more information on what changed.

Sent when an entitlement is created. The inner payload is an entitlement object.

### Entitlement Update

Warning: the `ENTITLEMENT_UPDATE` event behavior changed on October 1, 2024. See the Change Log and
Entitlement Migration Guide for more information on what changed.

Sent when an entitlement is updated. The inner payload is an entitlement object.

For subscription entitlements, this event is triggered only when a user's subscription ends, providing
an `ends_at` timestamp that indicates the end of the entitlement.

### Entitlement Delete

Sent when an entitlement is deleted. The inner payload is an entitlement object.

Entitlement deletions are infrequent, and occur when:

* Discord issues a refund for a subscription
* Discord removes an entitlement from a user via internal tooling
* Discord deletes an app-managed entitlement they created via the API

Entitlements are *not* deleted when they expire.

## Guilds

### Guild Create

This event can be sent in three different scenarios:

1. When a user is initially connecting, to lazily load and backfill information for all unavailable
   guilds sent in the Ready event. Guilds that are unavailable due to an outage will send a Guild
   Delete event.
2. When a Guild becomes available again to the client.
3. When the current user joins a new Guild.

Info: during an outage, the guild object in scenarios 1 and 3 may be marked as unavailable.

The inner payload can be:

* An available Guild: a guild object with extra fields, as noted below.
* An unavailable Guild: an unavailable guild object.

###### Guild Create Extra Fields

| Field                   | Type                                            | Description                                                                                                               |
| ----------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| joined_at               | ISO8601 timestamp                               | When this guild was joined at                                                                                             |
| large                   | boolean                                         | `true` if this is considered a large guild                                                                                |
| unavailable?            | boolean                                         | `true` if this guild is unavailable due to an outage                                                                      |
| member_count            | integer                                         | Total number of members in this guild                                                                                     |
| voice_states            | array of partial voice state objects            | States of members currently in voice channels; lacks the `guild_id` key                                                   |
| members                 | array of guild member objects                   | Users in the guild                                                                                                        |
| channels                | array of channel objects                        | Channels in the guild                                                                                                     |
| threads                 | array of channel objects                        | All active threads in the guild that current user has permission to view                                                  |
| presences               | array of partial presence update objects        | Presences of the members in the guild, will only include non-offline members if the size is greater than `large threshold` |
| stage_instances         | array of stage instance objects                 | Stage instances in the guild                                                                                              |
| guild_scheduled_events  | array of guild scheduled event objects          | Scheduled events in the guild                                                                                             |
| soundboard_sounds       | array of soundboard sound objects               | Soundboard sounds in the guild                                                                                            |

Warning: if your bot does not have the `GUILD_PRESENCES` Gateway Intent, or if the guild has over 75k
members, members and presences returned in this event will only contain your bot and users in voice
channels.

### Guild Update

Sent when a guild is updated. The inner payload is a guild object.

### Guild Delete

Sent when a guild becomes or was already unavailable due to an outage, or when the user leaves or is
removed from a guild. The inner payload is an unavailable guild object. If the `unavailable` field is
not set, the user was removed from the guild.

### Guild Audit Log Entry Create

Sent when a guild audit log entry is created. The inner payload is an Audit Log Entry object with an
extra `guild_id` key. This event is only sent to bots with the `VIEW_AUDIT_LOG` permission.

###### Guild Audit Log Entry Create Event Extra Fields

| Field    | Type      | Description     |
| -------- | --------- | --------------- |
| guild_id | snowflake | ID of the guild |

### Guild Ban Add

Sent when a user is banned from a guild. This event is only sent to bots with the `BAN_MEMBERS` or
`VIEW_AUDIT_LOG` permission.

###### Guild Ban Add Event Fields

| Field    | Type              | Description         |
| -------- | ----------------- | ------------------- |
| guild_id | snowflake         | ID of the guild     |
| user     | a user object     | User who was banned |

### Guild Ban Remove

Sent when a user is unbanned from a guild. This event is only sent to bots with the `BAN_MEMBERS` or
`VIEW_AUDIT_LOG` permission.

###### Guild Ban Remove Event Fields

| Field    | Type              | Description           |
| -------- | ----------------- | --------------------- |
| guild_id | snowflake         | ID of the guild       |
| user     | a user object     | User who was unbanned |

### Guild Emojis Update

Sent when a guild's emojis have been updated.

###### Guild Emojis Update Event Fields

| Field    | Type      | Description      |
| -------- | --------- | ---------------- |
| guild_id | snowflake | ID of the guild  |
| emojis   | array     | Array of emojis  |

### Guild Stickers Update

Sent when a guild's stickers have been updated.

###### Guild Stickers Update Event Fields

| Field    | Type      | Description        |
| -------- | --------- | ------------------ |
| guild_id | snowflake | ID of the guild    |
| stickers | array     | Array of stickers  |

### Guild Integrations Update

Sent when a guild integration is updated.

###### Guild Integrations Update Event Fields

| Field    | Type      | Description                                     |
| -------- | --------- | ----------------------------------------------- |
| guild_id | snowflake | ID of the guild whose integrations were updated |

## Guild members

### Guild Member Add

Warning: if using Gateway Intents, the `GUILD_MEMBERS` intent will be required to receive this event.

Sent when a user joins a guild. This event may also be sent for users who are already members of the
guild. The inner payload is a guild member object with an extra `guild_id` key:

###### Guild Member Add Extra Fields

| Field    | Type      | Description     |
| -------- | --------- | --------------- |
| guild_id | snowflake | ID of the guild |

### Guild Member Remove

Warning: if using Gateway Intents, the `GUILD_MEMBERS` intent will be required to receive this event.

Sent when a user is removed from a guild (leave/kick/ban).

###### Guild Member Remove Event Fields

| Field    | Type          | Description          |
| -------- | ------------- | -------------------- |
| guild_id | snowflake     | ID of the guild      |
| user     | a user object | User who was removed |

### Guild Member Update

Warning: if using Gateway Intents, the `GUILD_MEMBERS` intent will be required to receive this event.

Sent when a guild member is updated. This will also fire when the user object of a guild member
changes.

Caveat: Guild Member Update is sent for current-user updates regardless of whether the
`GUILD_MEMBERS` intent is set.

###### Guild Member Update Event Fields

| Field                        | Type                              | Description                                                                                                                                                                       |
| ---------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| guild_id                     | snowflake                         | ID of the guild                                                                                                                                                                   |
| roles                        | array of snowflakes               | User role ids                                                                                                                                                                     |
| user                         | a user object                     | User                                                                                                                                                                              |
| nick?                        | ?string                           | Nickname of the user in the guild                                                                                                                                                 |
| avatar                       | ?string                           | Member's guild avatar hash                                                                                                                                                        |
| banner                       | ?string                           | Member's guild banner hash                                                                                                                                                        |
| joined_at                    | ?ISO8601 timestamp                | When the user joined the guild                                                                                                                                                    |
| premium_since?               | ?ISO8601 timestamp                | When the user starting boosting the guild                                                                                                                                         |
| deaf?                        | boolean                           | Whether the user is deafened in voice channels                                                                                                                                    |
| mute?                        | boolean                           | Whether the user is muted in voice channels                                                                                                                                       |
| pending?                     | boolean                           | Whether the user has not yet passed the guild's Membership Screening requirements                                                                                                  |
| communication_disabled_until?| ?ISO8601 timestamp                | When the user's timeout will expire and the user will be able to communicate in the guild again, null or a time in the past if the user is not timed out                            |
| avatar_decoration_data?      | ?avatar decoration data           | Data for the member's guild avatar decoration                                                                                                                                     |
| collectibles?                | ?collectibles object              | data for the member's collectibles                                                                                                                                                |

### Guild Members Chunk

Sent in response to Guild Request Members (Request Guild Members, opcode 8). You can use the
`chunk_index` and `chunk_count` to calculate how many chunks are left for your request.

###### Guild Members Chunk Event Fields

| Field       | Type                          | Description                                                                                    |
| ----------- | ----------------------------- | ---------------------------------------------------------------------------------------------- |
| guild_id    | snowflake                     | ID of the guild                                                                                |
| members     | array of guild member objects | Set of guild members                                                                           |
| chunk_index | integer                       | Chunk index in the expected chunks for this response (`0 <= chunk_index < chunk_count`)        |
| chunk_count | integer                       | Total number of expected chunks for this response                                              |
| not_found?  | array                         | When passing an invalid ID to `REQUEST_GUILD_MEMBERS`, it will be returned here                |
| presences?  | array of presence objects     | When passing `true` to `REQUEST_GUILD_MEMBERS`, presences of the returned members will be here |
| nonce?      | string                        | Nonce used in the Guild Members Request                                                        |

## Guild roles

### Guild Role Create

Sent when a guild role is created.

###### Guild Role Create Event Fields

| Field    | Type          | Description           |
| -------- | ------------- | --------------------- |
| guild_id | snowflake     | ID of the guild       |
| role     | a role object | Role that was created |

### Guild Role Update

Sent when a guild role is updated.

###### Guild Role Update Event Fields

| Field    | Type          | Description           |
| -------- | ------------- | --------------------- |
| guild_id | snowflake     | ID of the guild       |
| role     | a role object | Role that was updated |

### Guild Role Delete

Sent when a guild role is deleted.

###### Guild Role Delete Event Fields

| Field    | Type      | Description     |
| -------- | --------- | --------------- |
| guild_id | snowflake | ID of the guild |
| role_id  | snowflake | ID of the role  |

## Guild scheduled events

### Guild Scheduled Event Create

Sent when a guild scheduled event is created. The inner payload is a guild scheduled event object.

### Guild Scheduled Event Update

Sent when a guild scheduled event is updated. The inner payload is a guild scheduled event object.

### Guild Scheduled Event Delete

Sent when a guild scheduled event is deleted. The inner payload is a guild scheduled event object.

### Guild Scheduled Event User Add

Sent when a user has subscribed to a guild scheduled event.

###### Guild Scheduled Event User Add Event Fields

| Field                    | Type      | Description                     |
| ------------------------ | --------- | ------------------------------- |
| guild_scheduled_event_id | snowflake | ID of the guild scheduled event |
| user_id                  | snowflake | ID of the user                  |
| guild_id                 | snowflake | ID of the guild                 |

### Guild Scheduled Event User Remove

Sent when a user has unsubscribed from a guild scheduled event.

###### Guild Scheduled Event User Remove Event Fields

| Field                    | Type      | Description                     |
| ------------------------ | --------- | ------------------------------- |
| guild_scheduled_event_id | snowflake | ID of the guild scheduled event |
| user_id                  | snowflake | ID of the user                  |
| guild_id                 | snowflake | ID of the guild                 |

## Guild soundboard sounds

### Guild Soundboard Sound Create

Sent when a guild soundboard sound is created. The inner payload is a soundboard sound object.

### Guild Soundboard Sound Update

Sent when a guild soundboard sound is updated. The inner payload is a soundboard sound object.

### Guild Soundboard Sound Delete

Sent when a guild soundboard sound is deleted.

###### Guild Soundboard Sound Delete Event Fields

| Field    | Type      | Description                      |
| -------- | --------- | -------------------------------- |
| sound_id | snowflake | ID of the sound that was deleted |
| guild_id | snowflake | ID of the guild the sound was in |

### Guild Soundboard Sounds Update

Sent when multiple guild soundboard sounds are updated.

###### Guild Soundboard Sounds Update Event Fields

| Field             | Type                              | Description                   |
| ----------------- | --------------------------------- | ----------------------------- |
| soundboard_sounds | array of soundboard sound objects | The guild's soundboard sounds |
| guild_id          | snowflake                         | ID of the guild               |

### Soundboard Sounds

Includes a guild's list of soundboard sounds. Sent in response to Request Soundboard Sounds
(opcode 31).

###### Soundboard Sounds Event Fields

| Field             | Type                              | Description                   |
| ----------------- | --------------------------------- | ----------------------------- |
| soundboard_sounds | array of soundboard sound objects | The guild's soundboard sounds |
| guild_id          | snowflake                         | ID of the guild               |

## Integrations

### Integration Create

Sent when an integration is created. The inner payload is an integration object with `user` omitted
and an additional `guild_id` key:

###### Integration Create Event Additional Fields

| Field    | Type      | Description     |
| -------- | --------- | --------------- |
| guild_id | snowflake | ID of the guild |

### Integration Update

Sent when an integration is updated. The inner payload is an integration object with `user` omitted
and an additional `guild_id` key:

###### Integration Update Event Additional Fields

| Field    | Type      | Description     |
| -------- | --------- | --------------- |
| guild_id | snowflake | ID of the guild |

### Integration Delete

Sent when an integration is deleted.

###### Integration Delete Event Fields

| Field           | Type      | Description                                                   |
| --------------- | --------- | ------------------------------------------------------------- |
| id              | snowflake | Integration ID                                                |
| guild_id        | snowflake | ID of the guild                                               |
| application_id? | snowflake | ID of the bot/OAuth2 application for this discord integration |

## Invites

All Invite related events are only sent to bot users with the `MANAGE_CHANNELS` permission on the
channel.

### Invite Create

Sent when a new invite to a channel is created.

###### Invite Create Event Fields

| Field               | Type                        | Description                                                                                                        |
| ------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| channel_id          | snowflake                   | Channel the invite is for                                                                                          |
| code                | string                      | Unique invite code                                                                                                 |
| created_at          | ISO8601 timestamp           | Time at which the invite was created                                                                               |
| guild_id?           | snowflake                   | Guild of the invite                                                                                                |
| inviter?            | user object                 | User that created the invite                                                                                       |
| max_age             | integer                     | How long the invite is valid for (in seconds)                                                                      |
| max_uses            | integer                     | Maximum number of times the invite can be used                                                                     |
| target_type?        | integer                     | Type of target for this voice channel invite                                                                       |
| target_user?        | user object                 | User whose stream to display for this voice channel stream invite                                                  |
| target_application? | partial application object  | Embedded application to open for this voice channel embedded application invite                                    |
| temporary           | boolean                     | Whether or not the invite is temporary (invited users will be kicked on disconnect unless they're assigned a role) |
| uses                | integer                     | How many times the invite has been used (always will be 0)                                                         |
| expires_at          | ?ISO8601 timestamp          | the expiration date of this invite                                                                                 |
| role_ids?           | array of snowflakes         | the role ID(s) for roles in the guild given to the users that accept this invite                                    |

### Invite Delete

Sent when an invite is deleted.

###### Invite Delete Event Fields

| Field      | Type      | Description           |
| ---------- | --------- | --------------------- |
| channel_id | snowflake | Channel of the invite |
| guild_id?  | snowflake | Guild of the invite   |
| code       | string    | Unique invite code    |

## Source

Discord Developer Documentation,
[Gateway Events](https://docs.discord.com/developers/events/gateway-events), retrieved 2026-08-26.
The guild, channel, thread member, role, entitlement, integration, invite, soundboard sound, stage
instance, audit log and auto moderation objects referenced above are REST resources; call the Skill
tool with "discord-rest".
