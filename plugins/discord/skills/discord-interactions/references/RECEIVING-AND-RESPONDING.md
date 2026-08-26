# Receiving and Responding to Interactions

Complete distillation of two pages, retrieved 2026-08-26:

- `https://docs.discord.com/developers/interactions/receiving-and-responding`
- `https://docs.discord.com/developers/interactions/overview` (the interaction types summary, the
  Interactions Endpoint URL setup and the full signature-verification procedure)

## Contents

- [Types of Interactions (overview page)](#types-of-interactions-overview-page)
- [Preparing for Interactions](#preparing-for-interactions)
  - [Configuring an Interactions Endpoint URL](#configuring-an-interactions-endpoint-url)
  - [Acknowledging PING requests](#acknowledging-ping-requests)
  - [Validating Security Request Headers](#validating-security-request-headers)
  - [Adding an Interactions Endpoint URL](#adding-an-interactions-endpoint-url)
- [Interaction Object](#interaction-object)
  - [Interaction Structure](#interaction-structure)
  - [Interaction Type](#interaction-type)
  - [Interaction Context Types](#interaction-context-types)
  - [Authorizing Integration Owners Object](#authorizing-integration-owners-object)
  - [Interaction Data](#interaction-data)
  - [Application Command Data Structure](#application-command-data-structure)
  - [Message Component Data Structure](#message-component-data-structure)
  - [Modal Submit Data Structure](#modal-submit-data-structure)
  - [Component Interaction Response Structures](#component-interaction-response-structures)
  - [Resolved Data Structure](#resolved-data-structure)
  - [Application Command Interaction Data Option Structure](#application-command-interaction-data-option-structure)
- [Message Interaction Object](#message-interaction-object)
- [Receiving an Interaction](#receiving-an-interaction)
- [Responding to an Interaction](#responding-to-an-interaction)
  - [Interaction Response Structure](#interaction-response-structure)
  - [Interaction Callback Type](#interaction-callback-type)
  - [Interaction Callback Data: Messages](#interaction-callback-data-messages)
  - [Interaction Callback Data: Autocomplete](#interaction-callback-data-autocomplete)
  - [Interaction Callback Data: Modal](#interaction-callback-data-modal)
- [Interaction Callback](#interaction-callback)
- [Followup Messages](#followup-messages)
  - [The deferred-then-followup flow, assembled](#the-deferred-then-followup-flow-assembled)
- [Endpoints](#endpoints)
- [All limits and timing constraints](#all-limits-and-timing-constraints)

---

## Types of Interactions (overview page)

Interactive features like commands and message components allow users to invoke an app natively within
Discord. When a user engages with one of your app's interactive features, your app will receive an
interaction.

### Commands

**Application commands** provide users a native way to invoke an app in Discord. They often map to an
app's core features or functionality.

*(Image: Command launcher in the Desktop client.)*

When an app creates a command it can choose the command's type, which determines where it appears in
the Discord client and the metadata the app will receive when the command is invoked. The overview page
says "There are three types for application commands" and then lists four:

- **Slash commands** are the most common type of command and are accessed by typing `/` in the chat
  input, or by opening the command picker.
- **Message commands** are commands related to a message or a message's content. They're accessed by
  clicking on the context menu (the three dots) at the top-right of a message (or right clicking on a
  message), then navigating to the "Apps" section.
- **User commands** are commands that relate to a user in Discord. They're accessed by right clicking
  on a user profile, then navigating to the "Apps" section.
- **Entry Point commands** are commands used as the primary way to launch Activities from the App
  Launcher.

Details in `APPLICATION-COMMANDS.md`.

### Message Components

**Message components** are interactive elements that can be included in the content of a message that
your app sends in Discord.

*(Image: Button message components in a message.)*

The main interactive components that apps can send in messages include:

- **Buttons** are clickable components that can be customized with different styles, texts, and emoji.
- **Static select menus** are components that a user can open to see a list of developer-defined select
  options with custom labels and descriptions.
- **Auto-populated select menus** are a set of four different select components that are populated with
  contextual Discord resources, like a list of users or channels in a server.

Full list and every field in `COMPONENTS-REFERENCE-LAYOUT-AND-CONTENT.md` and
`COMPONENTS-REFERENCE-INTERACTIVE.md`.

### Modals

**Modals** are single-user pop-up interfaces that allow apps to collect form-like data. Modals can only
be opened in response to a user invoking one of your app's commands or message components.

*(Image: Modals in the Discord client.)*

The overview page states that the only interactive component modals can contain are **text inputs**,
which allow users to fill out single-or-multi line form inputs. Note this statement is out of date
relative to the component reference, which documents String/User/Role/Mentionable/Channel Select, File
Upload, Radio Group, Checkbox Group and Checkbox as modal-capable as well.

---

## Preparing for Interactions

When a user interacts with your app, you have the option for your app to receive interactions in two
mutually-exclusive ways:

- WebSocket-based Gateway connection
- HTTP via outgoing webhooks

By default your app will receive interactions via a Gateway connection, but you can opt in to
HTTP-based interactions by adding an **Interactions Endpoint URL** to your app's settings.

### Configuring an Interactions Endpoint URL

An **Interactions Endpoint URL** is a public endpoint for your app where Discord can send your app
HTTP-based interactions. If your app is using Gateway-based interactions, you don't need to configure
an Interactions Endpoint URL.

Before you can add your Interactions Endpoint URL to your app, your endpoint must be prepared for two
things ahead of time:

1. Acknowledging `PING` requests from Discord
2. Validating security-related request headers (`X-Signature-Ed25519` and `X-Signature-Timestamp`)

If either of these is not complete, your Interactions Endpoint URL will not be validated.

### Acknowledging PING requests

When adding your Interactions Endpoint URL, Discord will send a `POST` request with a `PING` payload
with a `type: 1` to your endpoint. Your app is expected to acknowledge the request by returning a `200`
response with a `PONG` payload (which has the same `type: 1`).

**Info:** You must provide a valid `Content-Type` when responding to `PING`s. See the HTTP API section
of the API reference (`https://docs.discord.com/developers/reference#http-api`).

To properly acknowledge a `PING` payload, return a `200` response with a payload of `type: 1`:

```py
@app.route('/', methods=['POST'])
def my_command():
    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })
```

### Validating Security Request Headers

The internet is a scary place, especially for people hosting public, unauthenticated endpoints. To
receive interactions via HTTP, there are some security steps you **must** take before your app is
eligible to receive requests.

Each interaction is sent with the following headers:

- `X-Signature-Ed25519` as a signature
- `X-Signature-Timestamp` as a timestamp

Using your favorite security library, you **must validate the request each time you receive an
interaction**. If the signature fails validation, your app should respond with a `401` error code.

The message that is signed is the **concatenation of the timestamp header and the raw request body**,
in that order, verified against your application's public key (found on your application in the
Developer Portal) with Ed25519.

**JavaScript**

```js
const nacl = require("tweetnacl");

// Your public key can be found on your application in the Developer Portal
const PUBLIC_KEY = "APPLICATION_PUBLIC_KEY";

const signature = req.get("X-Signature-Ed25519");
const timestamp = req.get("X-Signature-Timestamp");
const body = req.rawBody; // rawBody is expected to be a string, not raw bytes

const isVerified = nacl.sign.detached.verify(
    Buffer.from(timestamp + body),
    Buffer.from(signature, "hex"),
    Buffer.from(PUBLIC_KEY, "hex")
);

if (!isVerified) {
    return res.status(401).end("invalid request signature");
}
```

**Python**

```py
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

# Your public key can be found on your application in the Developer Portal
PUBLIC_KEY = 'APPLICATION_PUBLIC_KEY'

verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

signature = request.headers["X-Signature-Ed25519"]
timestamp = request.headers["X-Signature-Timestamp"]
body = request.data.decode("utf-8")

try:
    verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
except BadSignatureError:
    abort(401, 'invalid request signature')
```

**Java**

Uses `tink-java` (`com.google.crypto.tink:tink:1.22.0`); the minimum Java version required is 11.

```java
import com.google.crypto.tink.subtle.Ed25519Verify;
import com.google.crypto.tink.subtle.Hex;

import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;

public class Ed25519WebhookVerifier {
    private final Ed25519Verify verifier;

    public Ed25519WebhookVerifier(String publicKey) {
        this.verifier = new Ed25519Verify(Hex.decode(publicKey));
    }

    public boolean verify(String signature, String timestamp, String body) {
        try {
            verifier.verify(Hex.decode(signature), (timestamp + body).getBytes(StandardCharsets.UTF_8));
            return true;
        } catch (GeneralSecurityException e) {
            return false;
        }
    }
}
```

Verify your interactions with:

```java
// Your public key can be found on your application in the Developer Portal
var verifier = new Ed25519WebhookVerifier("PUBLIC_KEY");

// Get those from your favorite web server library
// The "X-Signature-Ed25519" header
String signature;
// The "X-Signature-Timestamp" header
String timestamp;
// Request body
String body;
if (!verifier.verify(signature, timestamp, body)) {
    // Signature is invalid, return an HTTP 401 response
    throw new UnsupportedOperationException("Return a HTTP 401 response");
}
```

In addition to ensuring your app validates security-related request headers at the time of saving your
endpoint, Discord will also perform automated, routine security checks against your endpoint, including
purposefully sending you invalid signatures. If you fail the validation, Discord will remove your
interactions URL and alert you via email and System DM.

Discord recommends checking their Community Resources
(`https://docs.discord.com/developers/developer-tools/community-resources#interactions`) and the
libraries found there. They not only provide typing for Interactions data models, but also include
decorators for API frameworks like Flask and Express to make validation easy.

### Adding an Interactions Endpoint URL

After you have a public endpoint to use as your app's Interactions Endpoint URL, you can add it to your
app by going to your app's settings at `https://discord.com/developers/applications`.

On the **General Information** page (`https://discord.com/developers/applications/select/information`),
look for the **Interactive Endpoint URL** field. Paste your public URL that is set up to acknowledge
`PING` messages and correctly handles security-related signature headers.

---

## Interaction Object

An **Interaction** is the message that your application receives when a user uses an application
command or a message component.

- For **Slash Commands**, it includes the values that the user submitted.
- For **User Commands** and **Message Commands**, it includes the resolved user or message on which the
  action was taken.
- For **Message Components** it includes identifying information about the component that was used. It
  will also include some metadata about how the interaction was triggered: the `guild_id`, `channel`,
  `member` and other fields.

### Interaction Structure

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | ID of the interaction |
| application\_id | snowflake | ID of the application this interaction is for |
| type | interaction type | Type of interaction |
| data? \* | interaction data | Interaction data payload |
| guild? | partial guild object | Guild that the interaction was sent from |
| guild\_id? | snowflake | Guild that the interaction was sent from |
| channel? | partial channel object | Channel that the interaction was sent from |
| channel\_id? | snowflake | Channel that the interaction was sent from |
| member? \*\* | guild member object | Guild member data for the invoking user, including permissions |
| user? | user object | User object for the invoking user, if invoked in a DM |
| token | string | Continuation token for responding to the interaction |
| version | integer | Read-only property, always `1` |
| message? | message object | For components or modals triggered by components, the message they were attached to |
| app\_permissions \*\*\* | string | Bitwise set of permissions the app has in the source location of the interaction |
| locale? \*\*\*\* | string | Selected language of the invoking user |
| guild\_locale? | string | Guild's preferred locale, if invoked in a guild |
| entitlements | array of entitlement objects | For monetized apps, any entitlements for the invoking user, representing access to premium SKUs |
| authorizing\_integration\_owners | dictionary with keys of application integration types | Mapping of installation contexts that the interaction was authorized for to related user or guild IDs. See Authorizing Integration Owners Object for details |
| context? | interaction context type | Context where the interaction was triggered from |
| attachment\_size\_limit | integer | Attachment size limit in bytes |

\* This is always present on application command, message component, and modal submit interaction
types. It is optional for future-proofing against new interaction types.

\*\* `member` is sent when the interaction is invoked in a guild, and `user` is sent when invoked in a
DM.

\*\*\* `app_permissions` includes `ATTACH_FILES | EMBED_LINKS | MENTION_EVERYONE` permissions for
(G)DMs with other users, and additionally includes `USE_EXTERNAL_EMOJIS` for DMs with the app's bot
user.

\*\*\*\* This is available on all interaction types except PING.

### Interaction Type

| Name | Value |
| --- | --- |
| PING | 1 |
| APPLICATION\_COMMAND | 2 |
| MESSAGE\_COMPONENT | 3 |
| APPLICATION\_COMMAND\_AUTOCOMPLETE | 4 |
| MODAL\_SUBMIT | 5 |

### Interaction Context Types

Context in Discord where an interaction can be used, or where it was triggered from. Details about
using interaction contexts for application commands are in `APPLICATION-COMMANDS.md`.

| Name | Type | Description |
| --- | --- | --- |
| GUILD | 0 | Interaction can be used within servers |
| BOT\_DM | 1 | Interaction can be used within DMs with the app's bot user |
| PRIVATE\_CHANNEL | 2 | Interaction can be used within Group DMs and DMs other than the app's bot user |

### Authorizing Integration Owners Object

The `authorizing_integration_owners` field includes details about the authorizing user or server for
the installation(s) relevant to the interaction. For apps installed to a user, it can be used to tell
the difference between the authorizing user and the user that triggered an interaction (like a message
component).

A key will only be present if the following are true:

- The app has been authorized to the installation context corresponding to the key (`GUILD_INSTALL` or
  `USER_INSTALL`)
- The interaction is supported in the source interaction context (`GUILD`, `BOT_DM`, or
  `PRIVATE_CHANNEL`) for the installation context corresponding to the key
- And for command invocations, the command must be supported in the installation context (using
  `integration_types`)

The values in `authorizing_integration_owners` depend on the key:

- If the key is `GUILD_INSTALL` (`"0"`), the value depends on the source of the interaction:
  - The value will be the guild ID if the interaction is triggered from a server
  - The value will be `"0"` if the interaction is triggered from a DM with the app's bot user
- If the key is `USER_INSTALL` (`"1"`), the value will be the ID of the authorizing user

### Interaction Data

While the `data` field is guaranteed to be present for all interaction types besides `PING`, its
structure will vary. The following table maps each interaction type to its inner `data` payload.

| Interaction Type | Interaction Data |
| --- | --- |
| PING (`1`) | N / A |
| APPLICATION\_COMMAND (`2`) | Application Command Data Structure |
| MESSAGE\_COMPONENT (`3`) | Message Component Data Structure |
| APPLICATION\_COMMAND\_AUTOCOMPLETE (`4`) | Application Command Data Structure |
| MODAL\_SUBMIT (`5`) | Modal Submit Data Structure |

### Application Command Data Structure

**Info:** Sent in `APPLICATION_COMMAND` and `APPLICATION_COMMAND_AUTOCOMPLETE` interactions.

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | `ID` of the invoked command |
| name | string | `name` of the invoked command |
| type | integer | `type` of the invoked command |
| resolved? | resolved data | Converted users + roles + channels + attachments |
| options? \* | array of application command interaction data option | Params + values from the user |
| guild\_id? | snowflake | ID of the guild the command is registered to |
| target\_id? | snowflake | ID of the user or message targeted by a user or message command |

\* This can be partial when in response to `APPLICATION_COMMAND_AUTOCOMPLETE` (see Autocomplete in
`APPLICATION-COMMANDS.md`).

### Message Component Data Structure

| Field | Type | Description |
| --- | --- | --- |
| custom\_id | string | `custom_id` of the component |
| component\_type | integer | type of the component |
| values? \* | array of select option values | Values the user selected in a select menu component |
| resolved? | resolved data | Resolved entities from selected options |

\* This is always present for select menu components.

### Modal Submit Data Structure

| Field | Type | Description |
| --- | --- | --- |
| custom\_id | string | The custom ID provided for the modal |
| components | array of component interaction response | Values submitted by the user |
| resolved? | resolved data | Resolved entities from selected options |

### Component Interaction Response Structures

Response structures for both modal and message component interactions. Each of these per-component
structures is documented in `COMPONENTS-REFERENCE-INTERACTIVE.md` (interactive components) or
`COMPONENTS-REFERENCE-LAYOUT-AND-CONTENT.md` (Text Display, Label).

| Component |
| --- |
| String Select |
| Text Input |
| User Select |
| Role Select |
| Mentionable Select |
| Channel Select |
| Text Display |
| Label |
| File Upload |
| Radio Group |
| Checkbox Group |
| Checkbox |

### Resolved Data Structure

**Info:** If data for a Member is included, data for its corresponding User will also be included.

| Field | Type | Description |
| --- | --- | --- |
| users? | Map of Snowflakes to user objects | IDs and User objects |
| members? \* | Map of Snowflakes to partial member objects | IDs and partial Member objects |
| roles? | Map of Snowflakes to role objects | IDs and Role objects |
| channels? \*\* | Map of Snowflakes to partial channel objects | IDs and partial Channel objects |
| messages? | Map of Snowflakes to partial messages objects | IDs and partial Message objects |
| attachments? | Map of Snowflakes to attachment objects | IDs and attachment objects |

\* Partial `Member` objects are missing `user`, `deaf` and `mute` fields.

\*\* Partial `Channel` objects only have `id`, `name`, `type`, `permissions`, `app_permissions`,
`last_message_id`, `last_pin_timestamp`, `nsfw`, `parent_id`, `guild_id`, `flags`,
`rate_limit_per_user`, `topic` and `position` fields. Threads will also have the `thread_metadata`
field.

### Application Command Interaction Data Option Structure

All options have names, and an option can either be a parameter and input value — in which case `value`
will be set — or it can denote a subcommand or group — in which case it will contain a top-level key
and another array of `options`.

`value` and `options` are mutually exclusive.

| Field | Type | Description |
| --- | --- | --- |
| name | string | Name of the parameter |
| type | integer | Value of application command option type |
| value? | string, integer, double, or boolean | Value of the option resulting from user input |
| options? | array of application command interaction data option | Present if this option is a group or subcommand |
| focused? | boolean | `true` if this option is the currently focused option for autocomplete |

---

## Message Interaction Object

This is sent on the message object when the message is a response to an Interaction without an existing
message.

**Info:** This means responses to Message Components do not include this property, instead including a
message reference object as components *always* exist on preexisting messages.

### Message Interaction Structure

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | ID of the interaction |
| type | interaction type | Type of interaction |
| name | string | Name of the application command, including subcommands and subcommand groups |
| user | user object | User who invoked the interaction |
| member? | partial member object | Member who invoked the interaction in the guild |

---

## Receiving an Interaction

When a user interacts with your app, your app will receive an **Interaction**. Your app can receive an
interaction in one of two ways:

- Via `INTERACTION_CREATE` gateway event
- Via outgoing webhook

These two methods are **mutually exclusive**; you can *only* receive Interactions one of the two ways.
The `INTERACTION_CREATE` Gateway Event may be handled by connected clients, while the webhook method
does not require a connected client.

If you want to receive interactions via HTTP-based outgoing webhooks, you must configure an Interactions
Endpoint URL for your app — see [Preparing for Interactions](#preparing-for-interactions).

### Interaction Metadata

An Interaction includes metadata to aid your application in handling it as well as `data` specific to
the interaction type. Sample payloads per interaction type:

- Slash Commands — `APPLICATION-COMMANDS.md`, Example Interaction (Slash Command)
- User Commands — `APPLICATION-COMMANDS.md`, Example Interaction (User Command)
- Message Commands — `APPLICATION-COMMANDS.md`, Example Interaction (Message Command)
- Message Components — `USING-COMPONENTS.md` and `COMPONENTS-REFERENCE-INTERACTIVE.md`
- Modal Components — `USING-COMPONENTS.md` and `COMPONENTS-REFERENCE-INTERACTIVE.md`

---

## Responding to an Interaction

Interactions — both receiving and responding — are webhooks under the hood. So responding to an
Interaction is just like sending a webhook request.

**Info:** Interaction responses have the same header requirements as normal HTTP API requests
(`https://docs.discord.com/developers/reference#http-api`).

### Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type | interaction callback type | Type of response |
| data? | interaction callback data | An optional response message |

### Interaction Callback Type

| Name | Value | Description |
| --- | --- | --- |
| PONG | 1 | ACK a `Ping` |
| CHANNEL\_MESSAGE\_WITH\_SOURCE | 4 | Respond to an interaction with a message |
| DEFERRED\_CHANNEL\_MESSAGE\_WITH\_SOURCE | 5 | ACK an interaction and edit a response later, the user sees a loading state |
| DEFERRED\_UPDATE\_MESSAGE \* | 6 | For components, ACK an interaction and edit the original message later; the user does not see a loading state |
| UPDATE\_MESSAGE \* | 7 | For components, edit the message the component was attached to |
| APPLICATION\_COMMAND\_AUTOCOMPLETE\_RESULT | 8 | Respond to an autocomplete interaction with suggested choices |
| MODAL \*\* | 9 | Respond to an interaction with a popup modal |
| PREMIUM\_REQUIRED | 10 | **Deprecated**; respond to an interaction with an upgrade button, only available for apps with monetization enabled |
| LAUNCH\_ACTIVITY | 12 | Launch the Activity associated with the app. Only available for apps with Activities enabled |

\* Only valid for component-based interactions.

\*\* Not available for `MODAL_SUBMIT` and `PING` interactions.

Values `2`, `3` and `11` are not defined by the upstream table.

### Interaction Callback Data: Messages

Not all message fields are currently supported.

| Field | Type | Description |
| --- | --- | --- |
| tts? | boolean | Whether the response is TTS |
| content? | string | Message content |
| embeds? | array of embeds | Supports up to 10 embeds |
| allowed\_mentions? | allowed mentions | Allowed mentions object |
| flags? \* | integer | Message flags combined as a bitfield (only `SUPPRESS_EMBEDS`, `EPHEMERAL`, `IS_COMPONENTS_V2`, `IS_VOICE_MESSAGE`, and `SUPPRESS_NOTIFICATIONS` can be set) |
| components? | array of components | Message components |
| attachments? \*\* | array of partial attachment objects | Attachment objects with filename and description |
| poll? | poll request object | Details about the poll |

\* If you create a callback with the type `DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE` the only valid message
flag you may use is `EPHEMERAL`. If you'd like to create a component based message with
`IS_COMPONENTS_V2` you must do that with the Edit Original Interaction Response endpoint, not this one.

\*\* See Uploading Files in the API reference
(`https://docs.discord.com/developers/reference#uploading-files`) for details.

The `EPHEMERAL` message flag is `1 << 6` (64); `IS_COMPONENTS_V2` is `1 << 15` (32768).

### Interaction Callback Data: Autocomplete

| Field | Type | Description |
| --- | --- | --- |
| choices | array of choices | autocomplete choices (max of 25 choices) |

### Interaction Callback Data: Modal

| Field | Type | Description |
| --- | --- | --- |
| custom\_id | string | Developer-defined identifier for the modal, 1-100 characters |
| title | string | Title of the popup modal, max 45 characters |
| components | array of components | Between 1 and 5 (inclusive) components that make up the modal |

**Warning:** If your application responds with user data, you should use `allowed_mentions` to filter
which mentions in the content actually ping.

---

## Interaction Callback

When responding to an interaction received, you can make a `POST` request to
`/interactions/<interaction_id>/<interaction_token>/callback`. `interaction_id` is the unique id of that
individual Interaction from the received payload. `interaction_token` is the unique token for that
interaction from the received payload.

If you are receiving Interactions over the gateway, you **have to respond via HTTP**. Responses to
Interactions **are not sent as commands over the gateway**.

**If you send this request for an interaction received over HTTP, respond to the original HTTP request
with a 202 and no body.**

```py
import requests

url = "https://discord.com/api/v10/interactions/<interaction_id>/<interaction_token>/callback"

json = {
    "type": 4,
    "data": {
        "content": "Congrats on sending your command!"
    }
}
r = requests.post(url, json=json)
```

**Info:** Interaction `tokens` are valid for **15 minutes** and can be used to send followup messages
but you **must send an initial response within 3 seconds of receiving the event**. If the 3 second
deadline is exceeded, the token will be invalidated.

### Inline HTTP Response Behavior

If you receive interactions over HTTP, your server can also respond to the received `POST` request.
You'll want to respond with a `200` status code (if everything went well), as well as specifying a
`type` and `data`, which is an Interaction Response object:

```py
@app.route('/', methods=['POST'])
def my_command():
    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })

    else:
        return jsonify({
            "type": 4,
            "data": {
                "tts": False,
                "content": "Congrats on sending your command!",
                "embeds": [],
                "allowed_mentions": { "parse": [] }
            }
        })
```

### Interaction Callback Response Object

| Field | Type | Description |
| --- | --- | --- |
| interaction | interaction callback object | The interaction object associated with the interaction response. |
| resource? | interaction resource object | The resource that was created by the interaction response. |

### Interaction Callback Object

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | ID of the interaction |
| type | integer | Interaction type |
| activity\_instance\_id? | string | Instance ID of the Activity if one was launched or joined |
| response\_message\_id? | snowflake | ID of the message that was created by the interaction |
| response\_message\_loading? | boolean | Whether the message is in a loading state |
| response\_message\_ephemeral? | boolean | Whether the response message is ephemeral |

### Interaction Callback Resource Object

| Field | Type | Description |
| --- | --- | --- |
| type | integer | Interaction callback type |
| activity\_instance? \* | Activity instance resource | Represents the Activity launched by this interaction. |
| message? \*\* | message object | Message created by the interaction. |

\* Only present if type is `LAUNCH_ACTIVITY`.

\*\* Only present if type is either `CHANNEL_MESSAGE_WITH_SOURCE` or `UPDATE_MESSAGE`.

### Interaction Callback Activity Instance Resource

| Field | Type | Description |
| --- | --- | --- |
| id | string | Instance ID of the Activity if one was launched or joined. |

---

## Followup Messages

Sometimes, you want to send followup messages to a user after responding to an interaction. Or, you may
want to edit your original response. Whether you receive Interactions over the gateway or by outgoing
webhook, you can use the following endpoints to edit your initial response or send followup messages:

- `PATCH /webhooks/<application_id>/<interaction_token>/messages/@original` to edit your initial
  response to an Interaction
- `DELETE /webhooks/<application_id>/<interaction_token>/messages/@original` to delete your initial
  response to an Interaction
- `POST /webhooks/<application_id>/<interaction_token>` to send a new followup message
- `PATCH /webhooks/<application_id>/<interaction_token>/messages/<message_id>` to edit a message sent
  with that `token`

**Info:** Interactions webhooks share the same rate limit properties as normal webhooks.

Interaction tokens are valid for **15 minutes**, meaning you can respond to an interaction within that
amount of time.

### The deferred-then-followup flow, assembled

The upstream documents each step of this flow separately and gives no single worked example of it. The
shape below is assembled only from statements on this page — the callback type table, the message flag
footnote, the endpoint list and the token lifetimes — and adds nothing the page does not state.

Step 1, within **3 seconds** of receiving the interaction, acknowledge with
`DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE` (`5`) so the user sees a loading state. `EPHEMERAL` (`1 << 6`,
`64`) is the only message flag valid on this callback:

```
POST /interactions/{interaction.id}/{interaction.token}/callback
```

```json
{
  "type": 5,
  "data": {
    "flags": 64
  }
}
```

Step 2, any time within the token's **15 minutes**, replace the loading message by editing the original
response. This is also the endpoint the page requires for a component-based (`IS_COMPONENTS_V2`,
`1 << 15`, `32768`) message, since that flag cannot be set on the initial callback:

```
PATCH /webhooks/{application.id}/{interaction.token}/messages/@original
```

```json
{
  "content": "Done."
}
```

Step 3, additional messages on the same token use Create Followup Message. Note the deprecated
behavior the page calls out: calling this endpoint *directly* after a
`DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE` edits the loading message instead of creating a new one, ignores
the ephemeral flag you pass, and preserves the ephemeral state from the defer — use Edit Original
Interaction Response for that case instead:

```
POST /webhooks/{application.id}/{interaction.token}
```

```json
{
  "content": "And here is a second message."
}
```

The ephemeral state of an existing message cannot be changed, so decide it at step 1.

---

## Endpoints

**Info:** The endpoints below are not bound to the application's Global Rate Limit.

### POST /interactions/{interaction.id}/{interaction.token}/callback

Create Interaction Response.

Create a response to an Interaction. Body is an interaction response. Returns `204` unless
`with_response` is set to `true` which returns `200` with the body as interaction callback response.

This endpoint also supports file attachments similar to the webhook endpoints. Refer to Uploading Files
(`https://docs.discord.com/developers/reference#uploading-files`) for details on uploading files and
`multipart/form-data` requests.

#### Query String Params

| Field | Type | Description |
| --- | --- | --- |
| with\_response? | boolean | Whether to include an interaction callback object as the response |

### GET /webhooks/{application.id}/{interaction.token}/messages/@original

Get Original Interaction Response. Returns the initial Interaction response. Functions the same as Get
Webhook Message.

### PATCH /webhooks/{application.id}/{interaction.token}/messages/@original

Edit Original Interaction Response. Edits the initial Interaction response. Functions the same as Edit
Webhook Message.

### DELETE /webhooks/{application.id}/{interaction.token}/messages/@original

Delete Original Interaction Response. Deletes the initial Interaction response. Returns `204 No
Content` on success.

### POST /webhooks/{application.id}/{interaction.token}

Create Followup Message.

**Info:** Apps are limited to 5 followup messages per interaction if it was initiated from a
user-installed app and isn't installed in the server (meaning the authorizing integration owners object
only contains `USER_INSTALL`).

Create a followup message for an Interaction. Functions the same as Execute Webhook, but `wait` is
always true. The `thread_id`, `avatar_url`, and `username` parameters are not supported when using this
endpoint for interaction followups. You can use the `EPHEMERAL` message flag `1 << 6` (64) to send a
message that only the user can see. You can also use the `IS_COMPONENTS_V2` message flag `1 << 15`
(32768) to send a component-based message.

When using this endpoint directly after responding to an interaction with
`DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE`, this endpoint will function as Edit Original Interaction
Response for backwards compatibility. In this case, no new message will be created, and the loading
message will be edited instead. The ephemeral flag will be ignored, and the value you provided in the
initial defer response will be preserved, as an existing message's ephemeral state cannot be changed.
This behavior is deprecated, and you should use the Edit Original Interaction Response endpoint in this
case instead.

### GET /webhooks/{application.id}/{interaction.token}/messages/{message.id}

Get Followup Message. Returns a followup message for an Interaction. Functions the same as Get Webhook
Message.

### PATCH /webhooks/{application.id}/{interaction.token}/messages/{message.id}

Edit Followup Message. Edits a followup message for an Interaction. Functions the same as Edit Webhook
Message.

### DELETE /webhooks/{application.id}/{interaction.token}/messages/{message.id}

Delete Followup Message. Deletes a followup message for an Interaction. Returns `204 No Content` on
success.

---

## All limits and timing constraints

| Limit | Value |
| --- | --- |
| Initial response deadline | 3 seconds from receiving the event; exceeding it invalidates the token |
| Interaction token lifetime | 15 minutes |
| Embeds per message callback | up to 10 |
| Autocomplete choices per response | max 25 |
| Modal `custom_id` | 1-100 characters |
| Modal `title` | max 45 characters |
| Modal `components` | between 1 and 5 inclusive |
| Followup messages for a user-install-only interaction | max 5 per interaction |
| `version` on the interaction object | always `1` |
| Signature-failure response code | `401` |
| HTTP response when the callback was sent out-of-band | `202` with no body |
| `POST .../callback` success | `204`, or `200` with `with_response=true` |
| Rate limit scope of interaction endpoints | not bound to the application's Global Rate Limit; same rate limit properties as normal webhooks |

---

## Source

Discord Developer Documentation, retrieved 2026-08-26:

- `https://docs.discord.com/developers/interactions/receiving-and-responding`
- `https://docs.discord.com/developers/interactions/overview`
