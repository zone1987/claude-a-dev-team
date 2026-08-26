# Webhook Events

HTTP-based outgoing webhook events: subscribing, endpoint setup, the PING handshake, signature
validation, the payload envelope, every event type with its structure and example, and the Social SDK
message objects.

Source: [Webhook Events](https://docs.discord.com/developers/events/webhook-events), retrieved
2026-08-26.

## Contents

- [What webhook events are](#what-webhook-events-are)
- [Subscribing to events](#subscribing-to-events)
- [Preparing for events](#preparing-for-events)
- [Acknowledging PING requests](#acknowledging-ping-requests)
- [Validating security request headers](#validating-security-request-headers)
- [Adding a Webhook Events endpoint URL](#adding-a-webhook-events-endpoint-url)
- [Responding to events](#responding-to-events)
- [Payload structure](#payload-structure)
- [Webhook types](#webhook-types)
- [Event body object](#event-body-object)
- [Event types](#event-types)
- [Application Authorized](#application-authorized)
- [Application Deauthorized](#application-deauthorized)
- [Entitlement Create](#entitlement-create)
- [Entitlement Update](#entitlement-update)
- [Entitlement Delete](#entitlement-delete)
- [Quest User Enrollment](#quest-user-enrollment)
- [Lobby Message Create](#lobby-message-create)
- [Lobby Message Update](#lobby-message-update)
- [Lobby Message Delete](#lobby-message-delete)
- [Game Direct Message Create](#game-direct-message-create)
- [Game Direct Message Update](#game-direct-message-update)
- [Game Direct Message Delete](#game-direct-message-delete)
- [Social SDK message objects](#social-sdk-message-objects)

## What webhook events are

Webhook events are one-way events sent to your app over HTTP to notify you when an event occurred.
Unlike events that are sent over Gateway connections, events sent over webhooks are **not realtime or
guaranteed to be in order**.

While incoming webhooks are triggered by an external service, webhook events (i.e. outgoing webhooks)
are triggered by events happening in Discord. This means your app will need to set up a public URL
where you can receive HTTP events.

## Subscribing to events

To configure webhook events, you'll need to configure your URL and select the events you want your app
to receive.

Info: the steps below walk through subscribing using the developer portal. If you prefer to use the
API, you can call Edit Current Application.

In your app's settings (`https://discord.com/developers/applications`), navigate to the **Webhooks**
page (`https://discord.com/developers/applications/select/webhooks`) from the left-hand sidebar then
complete the following:

1. Under **Endpoint**, add a public URL that is set up to receive and acknowledge webhook events.
2. Enable Events by clicking the toggle in the **Events** section.
3. Select the webhook events you want your app to receive.
4. Click **Save Changes**.

If your URL is successfully verified, your app should begin receiving the events you selected.

## Preparing for events

To receive webhook events, you'll need to configure your app's **Webhook Event URL** in your app's
settings.

A **Webhook Events URL** is a public endpoint for your app where Discord can send your app HTTP-based
events. If your app is using Gateway events, you don't need to configure a Webhook Events URL.

Before you can add a Webhook Events URL to your app, your endpoint must be prepared for two things
ahead of time:

1. Acknowledging `PING` events from Discord
2. Validating security-related request headers (`X-Signature-Ed25519` and `X-Signature-Timestamp`)

If either of these are not complete, your Webhook Events URL will not be validated.

## Acknowledging PING requests

When adding your Webhook Events URL, Discord will send a `POST` request with a `PING` payload with a
`type: 0` to your endpoint. Your app is expected to acknowledge the request by returning a `204`
response with an empty body.

Info: you must provide a valid `Content-Type` when responding to `PING`s.

To properly acknowledge a `PING` payload, return a `204` response with no body:

```py
@app.route('/', methods=['POST'])
def my_command():
    if request.json["type"] == 0:
        return Response(status=204)
```

## Validating security request headers

To receive events via HTTP, there are some security steps you **must** take before your app is eligible
to receive requests.

Each webhook is sent with the following headers:

* `X-Signature-Ed25519` as a signature
* `X-Signature-Timestamp` as a timestamp

Using your favorite security library, you **must validate the request each time you receive an event**.
If the signature fails validation, your app should respond with a `401` error code. Code examples of
validating security headers are in the Interactions documentation; call the Skill tool with
"discord-interactions".

In addition to ensuring your app validates security-related request headers at the time of saving your
endpoint, Discord will also perform automated, routine security checks against your endpoint, including
purposefully sending you invalid signatures. If you fail the validation, Discord will remove your
Webhook Events URL and alert you via email and System DM.

## Adding a Webhook Events endpoint URL

After you have a public endpoint to use as your app's Event Webhooks URL, you can add it to your app by
going to your app's settings.

On the **Webhooks** page, look for the **Endpoint URL** field. Paste your public URL that is set up to
acknowledge `PING` messages and correctly handles security-related signature headers.

After you configure your Webhook Events URL, you can enable and subscribe to events on the same page.

## Responding to events

When your Webhook Event URL receives a webhook event, your app should respond with a `204` status code
with no body **within 3 seconds** to acknowledge that your app successfully received it. If your app
doesn't respond to the webhook event, Discord will retry sending it several times using exponential
backoff for up to 10 minutes.

If your app fails to respond too often, Discord will stop sending you webhook events and notify you via
email.

## Payload structure

Webhook events are wrapped in an outer payload, with an inner `event` object. Structure of the outer
webhook payload:

| Field          | Type              | Description                                                    |
| -------------- | ----------------- | -------------------------------------------------------------- |
| version        | integer           | Version scheme for the webhook event. Currently always `1`     |
| application_id | snowflake         | ID of your app                                                 |
| type           | webhook type      | Type of webhook, either `0` for PING or `1` for webhook events |
| event?         | event body object | Event data payload                                             |

## Webhook types

| Type  | Value | Description                                                       |
| ----- | ----- | ----------------------------------------------------------------- |
| PING  | `0`   | PING event sent to verify your Webhook Event URL is active        |
| Event | `1`   | Webhook event (details for event in event body object)             |

## Event body object

The event body contains high-level data about the event, like the type and time it was triggered. The
inner `data` object contains information specific to the event type.

| Field     | Type   | Description                                                          |
| --------- | ------ | -------------------------------------------------------------------- |
| type      | string | Event type                                                           |
| timestamp | string | Timestamp of when the event occurred in ISO8601 format               |
| data?     | object | Data for the event. The shape depends on the event type              |

## Event types

The table below includes the different webhook event types your app can subscribe to. The "Value"
column corresponds to the event's `type` field value in the event body object.

| Name                       | Value                        | Description                                                               |
| -------------------------- | ---------------------------- | ------------------------------------------------------------------------- |
| Application Authorized     | `APPLICATION_AUTHORIZED`     | Sent when an app was authorized by a user to a server or their account    |
| Application Deauthorized   | `APPLICATION_DEAUTHORIZED`   | Sent when an app was deauthorized by a user                               |
| Entitlement Create         | `ENTITLEMENT_CREATE`         | Entitlement was created                                                   |
| Entitlement Update         | `ENTITLEMENT_UPDATE`         | Entitlement was updated                                                   |
| Entitlement Delete         | `ENTITLEMENT_DELETE`         | Entitlement was deleted                                                   |
| Quest User Enrollment      | `QUEST_USER_ENROLLMENT`      | User was added to a Quest (currently unavailable)                         |
| Lobby Message Create       | `LOBBY_MESSAGE_CREATE`       | Sent when a message is created in a lobby                                 |
| Lobby Message Update       | `LOBBY_MESSAGE_UPDATE`       | Sent when a message is updated in a lobby                                 |
| Lobby Message Delete       | `LOBBY_MESSAGE_DELETE`       | Sent when a message is deleted from a lobby                               |
| Game Direct Message Create | `GAME_DIRECT_MESSAGE_CREATE` | Sent when a direct message is created during an active Social SDK session |
| Game Direct Message Update | `GAME_DIRECT_MESSAGE_UPDATE` | Sent when a direct message is updated during an active Social SDK session |
| Game Direct Message Delete | `GAME_DIRECT_MESSAGE_DELETE` | Sent when a direct message is deleted during an active Social SDK session |

## Application Authorized

`APPLICATION_AUTHORIZED` is sent when the app is added to a server or user account.

###### Application Authorized Structure

| Field             | Type             | Description                                                                                                                                    |
| ----------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| integration_type? | integer          | Installation context for the authorization. Either guild (`0`) if installed to a server or user (`1`) if installed to a user's account          |
| user              | user object      | User who authorized the app                                                                                                                    |
| scopes            | array of strings | List of scopes the user authorized                                                                                                             |
| guild?            | guild object     | Server which app was authorized for (when integration type is `0`)                                                                             |

###### Application Authorized Example

```json
{
  "version": 1,
  "application_id": "1234560123453231555",
  "type": 1,
  "event": {
    "type": "APPLICATION_AUTHORIZED",
    "timestamp": "2024-10-18T14:42:53.064834",
    "data": {
      "integration_type": 1,
      "scopes": [
        "applications.commands"
      ],
      "user": {
        // user data
      }
    }
  }
}
```

## Application Deauthorized

`APPLICATION_DEAUTHORIZED` is sent when the app is deauthorized by a user.

###### Application Deauthorized Structure

| Field | Type        | Description                   |
| ----- | ----------- | ----------------------------- |
| user  | user object | User who deauthorized the app |

###### Application Deauthorized Example

```json
{
  "version": 1,
  "application_id": "1234560123453231555",
  "type": 1,
  "event": {
    "type": "APPLICATION_DEAUTHORIZED",
    "timestamp": "2024-10-18T14:42:53.064834",
    "data": {
      "user": {
        // user data
      }
    }
  }
}
```

###### Discord Social SDK

For Discord Social SDK apps, `APPLICATION_DEAUTHORIZED` is the **only out-of-game signal that a user's
link state has changed**. Listening for it is required to keep your application state in sync — if you
miss the webhook, the next token use will fail and the game should fall back to the provisional account
flow.

Every revocation that fires this event is mechanically an unmerge — the merged Discord account reverts
to a new provisional account, and the OAuth2 tokens for the Discord user become invalid. The triggers
include:

* Token revocations via `/oauth2/token/revoke` or `Client::RevokeToken`.
* The user removing your app from *User Settings → Authorized Apps* in Discord.
* The Social SDK unmerge endpoints.
* The user's Discord account being banned.

Call the Skill tool with "discord-social-sdk" for the account linking and provisional account flows.

## Entitlement Create

`ENTITLEMENT_CREATE` is sent when an entitlement is created when a user purchases or is otherwise
granted one of your app's SKUs. Refer to the Monetization documentation for details; call the Skill tool
with "discord-monetization".

###### Entitlement Create Structure

The inner payload is an entitlement object.

###### Entitlement Create Example

```json
{
  "version": 1,
  "application_id": "1234560123453231555",
  "type": 1,
  "event": {
    "type": "ENTITLEMENT_CREATE",
    "timestamp": "2024-10-18T18:41:21.109604",
    "data": {
      "application_id": "1234560123453231555",
      "consumed": false,
      "deleted": false,
      "gift_code_flags": 0,
      "id": "1234505980407808808",
      "promotion_id": null,
      "sku_id": "123489045643835123",
      "type": 4,
      "user_id": "111178765189277770"
    }
  }
}
```

## Entitlement Update

`ENTITLEMENT_UPDATE` is sent when an entitlement is updated.

###### Entitlement Update Structure

The inner payload is an entitlement object.

###### Entitlement Update Example

```json
{
  "version": 1,
  "application_id": "1234560123453231555",
  "type": 1,
  "event": {
    "type": "ENTITLEMENT_UPDATE",
    "timestamp": "2024-10-18T18:41:21.109604",
    "data": {
      "application_id": "1234560123453231555",
      "consumed": false,
      "deleted": false,
      "gift_code_flags": 0,
      "id": "1234505980407808808",
      "promotion_id": null,
      "sku_id": "123489045643835123",
      "type": 4,
      "user_id": "111178765189277770"
    }
  }
}
```

## Entitlement Delete

`ENTITLEMENT_DELETE` is sent when an entitlement is deleted.

###### Entitlement Delete Structure

The inner payload is an entitlement object.

###### Entitlement Delete Example

```json
{
  "version": 1,
  "application_id": "1234560123453231555",
  "type": 1,
  "event": {
    "type": "ENTITLEMENT_DELETE",
    "timestamp": "2024-10-18T18:41:21.109604",
    "data": {
      "application_id": "1234560123453231555",
      "consumed": false,
      "deleted": true,
      "gift_code_flags": 0,
      "id": "1234505980407808808",
      "promotion_id": null,
      "sku_id": "123489045643835123",
      "type": 4,
      "user_id": "111178765189277770"
    }
  }
}
```

## Quest User Enrollment

Warning: this event cannot be received by apps at this time. It's documented because it appears on the
Webhooks settings page.

`QUEST_USER_ENROLLMENT` is sent when a user is added to a Quest on Discord. The upstream documents no
payload structure or example for it.

## Lobby Message Create

`LOBBY_MESSAGE_CREATE` is sent when a message is created in a lobby.

###### Lobby Message Create Structure

The inner payload is a lobby message object (see below).

###### Lobby Message Create Example

```json
{
  "version": 1,
  "application_id": "1234567765431056709",
  "type": 1,
  "event": {
    "type": "LOBBY_MESSAGE_CREATE",
    "timestamp": "2024-10-18T18:41:21.109604",
    "data": {
      "id": "1397729799727878254",
      "type": 0,
      "content": "welcome to the party!",
      "lobby_id": "1397729744753266719",
      "channel_id": "1397729744753266719",
      "author": {
        // user data
      },
      "flags": 65536,
      "application_id": "1234567765431056709"
    }
  }
}
```

## Lobby Message Update

`LOBBY_MESSAGE_UPDATE` is sent when a message is updated in a lobby.

###### Lobby Message Update Structure

The inner payload is a lobby message object with additional fields for message updates.

###### Lobby Message Update Example

```json
{
  "version": 1,
  "application_id": "1234567765431056709",
  "type": 1,
  "event": {
    "type": "LOBBY_MESSAGE_UPDATE",
    "timestamp": "2025-08-05T20:39:19.587872",
    "data": {
      "id": "1402390388030832792",
      "type": 0,
      "content": "noice",
      "lobby_id": "1402385687281537066",
      "channel_id": "1402389638311841883",
      "author": {
        // user data
      },
      "edited_timestamp": "2025-08-05T20:39:19.557970+00:00",
      "flags": 0,
      "timestamp": "2025-08-05T20:38:43.660000+00:00"
    }
  }
}
```

## Lobby Message Delete

`LOBBY_MESSAGE_DELETE` is sent when a message is deleted from a lobby.

###### Lobby Message Delete Structure

| Field    | Type      | Description                                   |
| -------- | --------- | --------------------------------------------- |
| id       | snowflake | ID of the deleted message                     |
| lobby_id | snowflake | ID of the lobby where the message was deleted |

###### Lobby Message Delete Example

```json
{
  "version": 1,
  "application_id": "1234567765431056709",
  "type": 1,
  "event": {
    "type": "LOBBY_MESSAGE_DELETE",
    "timestamp": "2025-08-05T21:44:09.412957",
    "data": {
      "id": "1402406637632884857",
      "lobby_id": "1402399883394285659"
    }
  }
}
```

## Game Direct Message Create

`GAME_DIRECT_MESSAGE_CREATE` is sent when a direct message is created while at least one user has an
active Social SDK session.

###### Game Direct Message Create Structure

The inner payload is a message object or SDK DM message object (see below).

###### Game Direct Message Create Example

```json
{
  "version": 1,
  "application_id": "1234567765431056709",
  "type": 1,
  "event": {
    "type": "GAME_DIRECT_MESSAGE_CREATE",
    "timestamp": "2025-08-14T18:09:38.063234",
    "data": {
      "id": "1405614357781545021",
      "type": 0,
      "content": "get in friend, we're going raiding",
      "channel_id": "1405604229820715098",
      "author": {
        // user data
      },
      "timestamp": "2025-08-14T18:09:37.947000+00:00",
      "application_id": "1234567765431056709",
      "attachments": []
    }
  }
}
```

## Game Direct Message Update

`GAME_DIRECT_MESSAGE_UPDATE` is sent when a direct message is updated while at least one user has an
active Social SDK session.

###### Game Direct Message Update Structure

The inner payload is a message object or SDK DM message object.

###### Game Direct Message Update Example

```json
{
  "version": 1,
  "application_id": "1234567765431056709",
  "type": 1,
  "event": {
    "type": "GAME_DIRECT_MESSAGE_UPDATE",
    "timestamp": "2025-08-14T16:44:31.847073",
    "data": {
      "id": "1405591838810706081",
      "content": "almost ready to queue?",
      "channel_id": "1404960877324533784",
      "author": {
        // user data
      },
      "recipient_id": "1404960877324533784"
    }
  }
}
```

## Game Direct Message Delete

`GAME_DIRECT_MESSAGE_DELETE` is sent when a direct message is deleted while at least one user has an
active Social SDK session.

###### Game Direct Message Delete Structure

The inner payload is a message object or SDK DM message object.

###### Game Direct Message Delete Example

```json
{
  "version": 1,
  "application_id": "1234567765431056709",
  "type": 1,
  "event": {
    "type": "GAME_DIRECT_MESSAGE_DELETE",
    "timestamp": "2025-08-20T17:01:50.099204",
    "data": {
      "id": "1407771600643686503",
      "type": 0,
      "content": "cant make it in time",
      "channel_id": "1405604229820715098",
      "author": {
        // user data
      },
      "timestamp": "2025-08-20T17:01:44.725000+00:00",
      "flags": 0,
      "attachments": [],
      "components": []
    }
  }
}
```

## Social SDK message objects

Discord Social SDK utilizes specialized message objects for lobby and direct message events that occur
during active game sessions. These objects extend or modify the standard Discord message structure to
support communication features.

* Lobby messages include lobby-specific fields like `lobby_id`
* Standard Discord messages in SDK contexts may include additional fields
* SDK DM messages are used for communication between provisional accounts

These objects are used in the webhook events `LOBBY_MESSAGE_*` and `GAME_DIRECT_MESSAGE_*` depending on
the messaging context.

### Lobby Message Object

Represents a message sent in a lobby or Linked Channel.

###### Lobby Message Structure

| Field           | Type        | Description                                                            |
| --------------- | ----------- | ---------------------------------------------------------------------- |
| id              | snowflake   | ID of the message                                                      |
| type            | integer     | Type of message                                                        |
| content         | string      | Contents of the message                                                |
| lobby_id        | snowflake   | ID of the lobby where the message was sent                             |
| channel_id      | snowflake   | ID of the channel the message was sent in                              |
| author          | user object | Author of the message                                                  |
| metadata?       | object      | Additional metadata for the message (key-value pairs)                  |
| flags           | integer     | Message flags combined as a bitfield                                   |
| application_id? | snowflake   | ID of the application (only present during active Social SDK sessions) |

### Message Object

Standard Message Object with additional fields.

###### Additional Fields

| Field      | Type           | Description                                                                             |
| ---------- | -------------- | --------------------------------------------------------------------------------------- |
| lobby_id?  | snowflake      | ID of the lobby where the message was created (only present in Linked Channel messages) |
| channel    | channel object | Channel object with recipient information                                               |

### SDK DM Message Object

Represents a message between provisional users that exists only in-game.

###### SDK DM Message Structure

| Field          | Type                     | Description                                    |
| -------------- | ------------------------ | ---------------------------------------------- |
| id             | snowflake                | ID of the message                              |
| type           | integer                  | Type of message                                |
| content        | string                   | Contents of the message                        |
| author         | user object              | Author of the message                          |
| flags          | integer                  | Message flags combined as a bitfield           |
| application_id | snowflake                | ID of the application that created the message |
| channel        | channel object           | Channel object with recipient information      |
| activity?      | message activity object   | Sent with Rich Presence-related chat embeds    |
| application?   | partial application object| Sent with Rich Presence-related chat embeds    |

Info: when both users in a direct message are provisional accounts, messages become "SDK DM messages"
that are only visible in-game and use this specialized structure.

## Source

Discord Developer Documentation,
[Webhook Events](https://docs.discord.com/developers/events/webhook-events), retrieved 2026-08-26.
