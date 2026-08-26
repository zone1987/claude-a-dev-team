# Discord Threads

Complete extraction of `https://docs.discord.com/developers/topics/threads`, retrieved 2026-08-26.

Threads are temporary sub-channels inside an existing channel, to help better organize conversation
in a busy channel. They are designed to be **very similar to channel objects** — upstream states this
topic aggregates all thread information specifically to make migrating straightforward.

## Contents

- [Backwards compatibility](#backwards-compatibility)
- [Thread fields](#thread-fields)
- [Public and private threads](#public-and-private-threads)
- [Locked threads](#locked-threads)
- [Active and archived threads](#active-and-archived-threads)
- [Permissions](#permissions)
- [Gateway events](#gateway-events)
- [Thread membership](#thread-membership)
- [Editing and deleting threads](#editing-and-deleting-threads)
- [Age-restricted threads](#age-restricted-threads)
- [New message types](#new-message-types)
- [Enumerating threads](#enumerating-threads)
- [Webhooks in threads](#webhooks-in-threads)
- [Thread access and syncing in detail](#thread-access-and-syncing-in-detail)
- [Forum channels](#forum-channels)
- [Media channels](#media-channels)
- [Creating threads in forum and media channels](#creating-threads-in-forum-and-media-channels)
- [Forum and media channel fields](#forum-and-media-channel-fields)
- [Forum and media channel thread fields](#forum-and-media-channel-thread-fields)
- [Forum and media channel formatting](#forum-and-media-channel-formatting)

## Backwards compatibility

**Threads are only available in API v9 and above.** Bots that do not update to API v9 or above will
not receive most gateway events for threads, or things that happen in threads (such as
`MESSAGE_CREATE`). Bots on API v8 **will still receive gateway events for Interactions**.

The list of gateway events that may be dropped **includes, but is not limited to**, these 13:

- `MESSAGE_CREATE`
- `MESSAGE_DELETE`
- `MESSAGE_DELETE_BULK`
- `MESSAGE_REACTION_ADD`
- `MESSAGE_REACTION_REMOVE`
- `MESSAGE_REACTION_REMOVE_ALL`
- `MESSAGE_REACTION_REMOVE_EMOJI`
- `MESSAGE_UPDATE`
- `THREAD_CREATE`
- `THREAD_UPDATE`
- `THREAD_DELETE`
- `THREAD_MEMBER_UPDATE`
- `THREAD_MEMBERS_UPDATE`

## Thread fields

Threads share and repurpose a number of the existing fields from the channel object.

### Re-used unchanged

`id`, `guild_id`, `type`, `name`, `last_message_id`, `last_pin_timestamp`, `rate_limit_per_user`.

### Repurposed

| Field | Repurposed meaning on a thread |
| --- | --- |
| `owner_id` | The id of the **user that started the thread**. |
| `parent_id` | The id of the **`GUILD_TEXT` or `GUILD_ANNOUNCEMENT` channel the thread was created in**. |

### Thread-only fields

| Field | Semantics and caveats |
| --- | --- |
| `member_count` | An **approximate** member count, but **it stops counting at 50**. Upstream notes this is only used in Discord's UI, so it is not valuable to bots. |
| `message_count` | The number of messages in a thread. **Decremented when a message is deleted.** Threads created before **July 1, 2022** stop counting at 50. |
| `total_message_sent` | The number of messages in a thread. **Not** decremented when a message is deleted. Threads created before **July 1, 2022** stop counting at 50. |
| `thread_metadata` | Contains the thread-specific fields below. |

### `thread_metadata` fields

Four fields: `archived`, `archive_timestamp`, `auto_archive_duration`, `locked`.

`archive_timestamp` is changed **when creating, archiving, or unarchiving a thread, and when changing
the `auto_archive_duration` field**.

## Public and private threads

### Public threads

- Viewable by **everyone who can view the parent channel** of the thread.
- **Must be created from an existing message**, but can be "orphaned" if that message is deleted.
- The created thread and the message it was started from **share the same id**.
- The **type of thread created matches the type of the parent channel**:

| Parent channel type | Thread type created |
| --- | --- |
| `GUILD_TEXT` | `PUBLIC_THREAD` |
| `GUILD_ANNOUNCEMENT` | `ANNOUNCEMENT_THREAD` |

Created via the Start Thread from Message endpoint.

### Private threads

- Behave **similar to Group DMs, but in a Guild**.
- **Always** created with the `GUILD_PRIVATE_THREAD` type.
- **Can only be created in `GUILD_TEXT` channels.**
- Created via the Start Thread without Message endpoint.

## Locked threads

Users (**including bot users**) without the `MANAGE_THREADS` permission are more restricted in locked
threads:

- Users **cannot create or update messages** in locked threads.
- Users **cannot update properties** like the thread's title or tags.
- Some user activity — **deleting messages and adding or removing reactions** — will *only* be allowed
  in locked threads if that thread is **also active** (un-archived).

If a user or bot user **has** the `MANAGE_THREADS` permission, they will still be able to make changes
to the thread and messages.

## Active and archived threads

Every thread can be either **active** or **archived**. Changing a thread from archived to active is
referred to as **unarchiving** the thread. Threads that have `locked` set to `true` can only be
unarchived by a user with the `MANAGE_THREADS` permission.

### Why archiving exists

Besides helping to de-clutter the UI for users, archiving exists to **limit the working set of threads
that need to be kept around**. Since the number of archived threads can be quite large, keeping all of
them in memory may be quite prohibitive. Therefore:

- **Guilds are capped at a certain number of active threads**, and
- **only active threads can be manipulated.**

### What is forbidden in an archived thread

Users **cannot**:

- edit messages,
- add reactions,
- use application commands,
- join the thread.

**The only operation that should happen within an archived thread is messages being deleted.**

**Sending a message automatically unarchives the thread**, unless the thread has been locked by a
moderator.

Because of this constraint, the gateway protocol is designed to ensure that bots are able to have an
accurate view of the **full set of active threads**, but **archived threads are not synced up-front
via the gateway**.

### Limits

- **Threads do not count against the max-channels limit in a guild.**
- **There is a limit on the maximum number of active threads in a guild.** (Upstream does not state
  the numeric value on this page.)

### Auto-archiving behaviour

- Threads **automatically archive after a period of inactivity**.
- **As a server approaches the max thread limit this timer will automatically lower**, usually not
  below the `auto_archive_duration`.
- In very busy channels, threads set to a **7 day** auto archive may archive earlier to help avoid the
  server becoming "full".
- **"Activity" is defined as**: sending a message, unarchiving a thread, or changing the auto-archive
  time.
- The `auto_archive_duration` field **previously controlled how long a thread could stay active, but
  is now repurposed to control how long the thread stays in the channel list**.
- Channels can also set **`default_auto_archive_duration`**, which is used by Discord's clients to
  pre-select a different `auto_archive_duration` value when a user creates a thread.

## Permissions

Threads generally **inherit permissions from the parent channel** — for example, if you can add
reactions in the parent channel, you can do that in a thread as well.

### The three thread-specific permission bits

- `CREATE_PUBLIC_THREADS`
- `CREATE_PRIVATE_THREADS`
- `SEND_MESSAGES_IN_THREADS`

**The `SEND_MESSAGES` permission has no effect in threads; users must have
`SEND_MESSAGES_IN_THREADS` to talk in a thread.** (Upstream carries this as a `Warning`.)

### Private thread access

Private threads are similar to Group DMs, but in a guild: **you must be invited to the thread to be
able to view or participate in it, or be a moderator** (`MANAGE_THREADS` permission).

### Gateway visibility

Threads are treated slightly differently from channels in the gateway protocol: **clients will not be
informed of a thread through the gateway if they do not have permission to view that thread**.

## Gateway events

- **Guild Create** contains a field `threads`, which is an **array of channel objects**. This
  represents **all active threads in the guild that the current user is able to view**.
- When a thread is created, updated, or deleted, a **Thread Create**, **Thread Update**, or **Thread
  Delete** event is sent. Like their channel counterparts, **these just contain a thread**.
- Since the gateway only syncs active threads that the user can see, **if a user *gains* access to a
  channel**, the gateway may need to sync the active threads in that channel to the user. It sends a
  **Thread List Sync** event for this.

## Thread membership

Each thread **tracks explicit membership**. There are two primary use cases for this data:

1. **Clients use *their own* thread member object to calculate read states and notification
   settings.** Largely irrelevant for bots, but is the reason for some of the syncing complexity.
2. **Knowing everyone that is in a thread.**

Membership is tracked in an **array of thread member objects**. These have **four fields**:

| Field | Meaning |
| --- | --- |
| `id` | The **thread id**. |
| `user_id` | The user's id. |
| `join_timestamp` | When the user joined the thread. |
| `flags` | **Currently the only flags are for notification settings**, but others may be added in future updates. |

### Syncing for the current user

Six mechanisms, exactly as upstream lists them:

- A **Thread Members Update** gateway event is **always** sent when the current user is added to or
  removed from a thread.
- A **Thread Member Update** gateway event is sent whenever the current user's thread member object is
  updated.
- Certain API calls, such as **listing archived threads and search**, return an **array** of thread
  member objects for any returned threads the current user is a member of. Other API calls, such as
  **getting a channel**, return the thread member object for the current user **as a property on the
  channel**, if the current user is a member of the thread.
- The **Guild Create** gateway event contains a thread member object **as a property on any returned
  threads** the current user is a member of.
- The **Thread Create** gateway event contains a thread member object as a property of the thread if
  the current user is a member of it, **and the user has recently gained access to view the parent
  channel**.
- The **Thread List Sync** gateway event contains an **array** of thread member objects for any
  returned threads the current user is a member of.

### Syncing for other users

**These require the `GUILD_MEMBERS` gateway intent.** (Upstream carries this as an `Info` callout.)

- An API `GET` call to `/channels/<channel_id>/thread-members`, which returns an array of thread
  member objects.
- The **Thread Members Update** gateway event, which includes **all users who were added to or removed
  from a thread by an action**.

## Editing and deleting threads

Threads can be edited and deleted with the **existing `PATCH` and `DELETE` endpoints to edit a
channel**. The permission matrix upstream states:

| Operation | Requirement |
| --- | --- |
| **Deleting** a thread | `MANAGE_THREADS` permission. |
| Editing `archived` to `false` (unarchiving) | Only requires the current user has **already been added to the thread**. **If `locked` is true**, the user must have **created the thread** or have `MANAGE_THREADS`. |
| Editing `name`, `archived`, `auto_archive_duration` | `MANAGE_THREADS` **or** the current user is the **thread creator**. |
| Editing `rate_limit_per_user` or `locked` | `MANAGE_THREADS`. |

## Age-restricted threads

**Threads do not explicitly set the `nsfw` field.** All threads in an age-restricted channel
**inherit that setting** though.

## New message types

Threads introduce a few message types, and repurpose some others.

### Repurposed

| Message type | Repurposed behaviour |
| --- | --- |
| `RECIPIENT_ADD` | Also sent when a user **is added** to a thread by someone else. |
| `RECIPIENT_REMOVE` | Also sent when a user **is removed** from a thread by someone else. |
| `CHANNEL_NAME_CHANGE` | Sent when the **thread's name is changed**. |

### New

- **`THREAD_CREATED`** — a new message sent to the **parent `GUILD_TEXT` channel**, used to inform
  users that a thread has been created. It is currently **only sent in one case**: when a
  `PUBLIC_THREAD` is created from an **older message** (upstream: "older is still TBD, but is
  currently set to a very small value"). The message contains a **message reference** with the
  `guild_id` and `channel_id` of the thread. **The `content` of the message is the `name` of the
  thread.**
- **`THREAD_STARTER_MESSAGE`** — a new message sent as the **first message** in threads that are
  started from an existing message in the parent channel. It ***only*** contains a **message
  reference** field that points to the message from which the thread was started.

## Enumerating threads

**Four `GET` routes** for enumerating threads in a specific channel:

### GET /guilds/<guild_id>/threads/active

Returns **all active threads in a guild that the current user can access**; includes **public and
private** threads. (List Active Guild Threads.)

### GET /channels/<channel_id>/users/@me/threads/archived/private

Returns **all archived, private threads in a channel that the current user is a member of**, sorted by
**thread id descending**. (List Joined Private Archived Threads.)

### GET /channels/<channel_id>/threads/archived/public

Returns **all archived, public threads in a channel**, sorted by **archive timestamp descending**.
(List Public Archived Threads.)

### GET /channels/<channel_id>/threads/archived/private

Returns **all archived, private threads in a channel**, sorted by **archive timestamp descending**.
(List Private Archived Threads.)

## Webhooks in threads

Webhooks can send messages to threads by using the **`thread_id` query parameter**. See the Execute
Webhook documentation for more details.

## Thread access and syncing in detail

While the syncing of threads is similar to channels, there are **two important differences** relevant
for **Thread List Sync** and **Thread Create** events:

1. **The Gateway will only sync threads that the app has permission to view.**
2. **The Gateway will only sync threads once the app has "subscribed" to the guild.** For context, in
   Discord's official clients, a subscription happens when the user visits a channel in the guild.

### Gaining access to private threads

When an app is added to a private thread, it **likely doesn't have that thread in memory yet** since it
doesn't have permission to view it.

Private threads are **only synced to you if you are a member or a moderator**. Whenever a user is added
to a private thread, the Gateway **also sends a Thread Create event**. This ensures the client always
has a **non-null value** for that thread.

The `THREAD_CREATE` event is **also sent when the user is a moderator** (and thus would already have
the channel in memory).

### Gaining access to public threads

Upon connecting to the Gateway, **apps will be automatically subscribed to thread events and active
threads**.

However, when a **non-app** is added to a public thread but hasn't subscribed to threads, it may not
have that thread in memory yet (which is a requirement for Discord's clients). Because of this, the
Gateway will send a **Thread Create** event when a user is added to ***any*** thread, **even if the
event is not necessary for apps**.

### Gaining access to channels

When an app gains access to a channel — for example, it is given the moderator role — it likely
**won't have the threads in memory** for that channel, since the Gateway only syncs threads the client
has permission to view. To account for this, a **Thread List Sync** event is sent.

The Thread List Sync event contains a **`channel_ids` array**, which is the IDs of all channels whose
threads are being synced. The documented consumption pattern: **first clear out any active threads
whose `parent_id` is in the `channel_ids` array, then ingest any threads that were in the event.**

### Losing access to channels

When an app **loses** access to a channel, the Gateway does **not** send it a **Thread Delete** event
(or any equivalent thread-specific event). Instead, the app receives **the event that caused its
permissions on the channel to change**.

If an app wanted to track when it lost access to any thread, it's **possible but difficult**, as it
would need to handle all cases correctly. Usually, events that cause permission changes are a **Guild
Role Update**, **Guild Member Update** or **Channel Update** event.

Discord's clients **check their permissions *first*** when performing an action, so even if a client
has some stale data, it does not end up acting on it.

Additionally, when a user or app loses access to a channel, **they are not removed from the thread and
will continue to be reported as a member of that thread**. However, they will **not** receive any new
Gateway events unless they are removed from the thread, in which case they receive a **Thread Members
Update** event.

### Unarchiving a thread

When a thread is unarchived, **there is no guarantee that an app has the thread or its member status
in memory**. To account for this, the Gateway sends **two events, in this order**:

1. A **Thread Update** event, which contains the **full channel object**.
2. A **Thread Member Update** event, sent to **all members of the unarchived thread**. Discord's
   clients only load active threads into memory on start, so this event is sent even if it may not be
   relevant to most apps.

## Forum channels

A **`GUILD_FORUM` channel is type `15`**. It is similar to a `GUILD_TEXT` channel, except ***only***
threads can be created in them. Unless otherwise noted, threads in forum channels behave in the same
way as in text channels — meaning they use the **same endpoints** and receive the **same Gateway
events**.

**Messages cannot be sent directly in forum channels.**

More information about how forum channels appear in Discord is in Discord's Forum Channels FAQ help
centre article.

## Media channels

A **`GUILD_MEDIA` channel is type `16`**. It is similar to a `GUILD_FORUM` channel in that **only
threads can be created in them**. Unless otherwise noted, threads in media channels behave in the same
way as in forum channels — meaning they use the **same endpoints** and receive the **same Gateway
events**.

**`GUILD_MEDIA` channels are in beta and still being actively developed. The API and other technical
details are subject to change.** (Upstream carries this as a `Warning`.)

More information about media channels is in Discord's creator-support media channels help centre
article.

## Creating threads in forum and media channels

Within **thread-only channels**, threads appear as **posts**.

### POST /channels/<channel_id>/threads

Threads are created with this endpoint (Start Thread in Forum or Media Channel), with **slightly
different parameters** than threads in text channels. Upstream's example of why: when creating threads
in a threads-only channel, **a message is created that has the same ID as the thread**, which requires
you to **pass parameters for both a thread *and* a message**.

### Permission exception

Threads in thread-only channels have the **same permissions behavior** as threads in a text channel,
inheriting all permissions from the parent channel, **with one exception: creating a thread in a
thread-only channel only requires the `SEND_MESSAGES` permission.**

## Forum and media channel fields

Fields specific to thread-only channels that upstream calls out as important to keep in mind:

| Field | Detail |
| --- | --- |
| `last_message_id` | The **ID of the most recently created thread** in that channel. As with messages, your app will **not** receive a `CHANNEL_UPDATE` event when the field is changed. Instead clients should update the value when receiving **Thread Create** events. |
| `topic` | What is shown in the **"Guidelines" section** within the Discord client. |
| `rate_limit_per_user` | Limits **how frequently threads can be created**. |
| `default_thread_rate_limit_per_user` | A **new** field on thread-only channels, which limits **how often messages can be sent *in a thread***. **This field is copied into `rate_limit_per_user` on the thread at creation time.** |
| `available_tags` | Can be set when **creating or updating a channel**; determines **which tags can be set on individual threads** within the thread's `applied_tags` field. |
| `flags` | Indicates any **channel flags** set for a thread-only channel. **Currently only `REQUIRE_TAG` can be used**, which requires that a tag from `available_tags` be specified when creating a thread in that channel. |

All fields for channels, including thread-only channels, are in the Channel Object reference.

## Forum and media channel thread fields

- A thread can be **pinned** within a thread-only channel, represented as the **`PINNED` flag** in the
  `flags` field. A pinned thread has the **`(1 << 1)`** flag set, and **archiving that thread will
  unset the flag**. **A pinned thread will *not* auto-archive.**
- The `message_count` and `total_message_sent` fields on threads in thread-only channels **increment
  on `MESSAGE_CREATE`** events, and **decrement on `MESSAGE_DELETE` and `MESSAGE_DELETE_BULK`**
  events. There will be **no specific `CHANNEL_UPDATE` event** that notifies your app of changes to
  those fields — instead, apps should update those values when receiving corresponding events.

All fields for threads in thread-only channels are in the Start Thread in Forum or Media Channel
JSON/form params in the channel resource documentation.

## Forum and media channel formatting

In thread-only channels, **the first message in a thread and the channel topic can both contain
markdown for bulleted lists and headings** — unlike text channels.

## Source

Discord Developer Documentation, `https://docs.discord.com/developers/topics/threads`,
retrieved 2026-08-26.
