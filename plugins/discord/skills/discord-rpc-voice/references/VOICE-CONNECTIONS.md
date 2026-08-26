# Discord Voice Connections

The complete voice connection protocol: gateway voice state, voice server update, the voice WebSocket,
every voice opcode, heartbeating, the UDP connection, IP discovery, transport encryption modes, the
RTP voice packet structure, speaking, resuming, the DAVE end-to-end encryption protocol, and every
voice close event code.

Voice connections operate in a similar fashion to the Gateway connection. However, they use a
different set of payloads and a **separate UDP-based connection** for voice data transmission. Because
UDP is used for both receiving and transmitting voice data, your client *must* be able to receive UDP
packets, even through a firewall or NAT (see UDP hole punching). The Discord Voice servers implement
functionality (see [IP Discovery](#ip-discovery)) for discovering the local machine's remote UDP
IP/Port, which can assist in some network configurations.

## Contents

- [Voice gateway versioning](#voice-gateway-versioning)
- [Voice opcodes](#voice-opcodes)
- [Voice close event codes](#voice-close-event-codes)
- [Connecting to voice: retrieving voice server information](#connecting-to-voice-retrieving-voice-server-information)
- [Establishing a voice WebSocket connection](#establishing-a-voice-websocket-connection)
- [Heartbeating](#heartbeating)
- [Establishing a voice UDP connection](#establishing-a-voice-udp-connection)
- [Transport encryption and sending voice](#transport-encryption-and-sending-voice)
- [Transport encryption modes](#transport-encryption-modes)
- [Voice packet structure](#voice-packet-structure)
- [Speaking](#speaking)
- [Voice data interpolation](#voice-data-interpolation)
- [Resuming a voice connection](#resuming-a-voice-connection)
- [Buffered resume](#buffered-resume)
- [IP discovery](#ip-discovery)
- [End-to-end encryption (DAVE protocol)](#end-to-end-encryption-dave-protocol)

## Voice gateway versioning

To ensure that you have the most up-to-date information, use **version 8**. Otherwise Discord cannot
guarantee that the opcodes documented here will reflect what you receive over the socket.

Previously, if the version query string `v` was omitted the voice gateway would default to version 1.
That behavior is being deprecated; in the future you must present a voice gateway version or your
voice connection will be rejected.

Upstream warning: "Versions below 4 as well as the default version behavior will be discontinued as of
November 18th, 2024. Connections without a version or with a version less than version 4 will be
rejected as of this date."

###### Gateway Versions

| Version | Status      | WebSocket URL Append | Change                                                                 |
| ------- | ----------- | -------------------- | ---------------------------------------------------------------------- |
| 8       | recommended | ?v=8                 | Added server message buffering, missed messages re-delivered on resume |
| 7       | available   | ?v=7                 | Added channel options opcode                                           |
| 6       | available   | ?v=6                 | Added code version opcode                                              |
| 5       | available   | ?v=5                 | Added video sink wants opcode                                          |
| 4       | available   | ?v=4                 | Changed speaking status to bitmask from boolean                        |
| 3       | deprecated  | ?v=3                 | Added video                                                            |
| 2       | deprecated  | ?v=2                 | Changed heartbeat reply from server to heartbeat ACK opcode            |
| 1       | deprecated  | ?v=1                 | Initial version                                                        |

## Voice opcodes

The `Binary` column marks opcodes sent as binary WebSocket messages instead of JSON text; see
[Binary WebSocket messages](#binary-websocket-messages).

| Code | Name                                | Sent By           | Description                                              | Binary |
| ---- | ----------------------------------- | ----------------- | -------------------------------------------------------- | ------ |
| 0    | Identify                            | client            | Begin a voice websocket connection.                      |        |
| 1    | Select Protocol                     | client            | Select the voice protocol.                               |        |
| 2    | Ready                               | server            | Complete the websocket handshake.                        |        |
| 3    | Heartbeat                           | client            | Keep the websocket connection alive.                     |        |
| 4    | Session Description                 | server            | Describe the session.                                    |        |
| 5    | Speaking                            | client and server | Indicate which users are speaking.                       |        |
| 6    | Heartbeat ACK                       | server            | Sent to acknowledge a received client heartbeat.         |        |
| 7    | Resume                              | client            | Resume a connection.                                     |        |
| 8    | Hello                               | server            | Time to wait between sending heartbeats in milliseconds. |        |
| 9    | Resumed                             | server            | Acknowledge a successful session resume.                 |        |
| 11   | Clients Connect                     | server            | One or more clients have connected to the voice channel  |        |
| 13   | Client Disconnect                   | server            | A client has disconnected from the voice channel         |        |
| 21   | DAVE Prepare Transition             | server            | A downgrade from the DAVE protocol is upcoming           |        |
| 22   | DAVE Execute Transition             | server            | Execute a previously announced protocol transition       |        |
| 23   | DAVE Transition Ready               | client            | Acknowledge readiness previously announced transition    |        |
| 24   | DAVE Prepare Epoch                  | server            | A DAVE protocol version or group change is upcoming      |        |
| 25   | DAVE MLS External Sender            | server            | Credential and public key for MLS external sender        | X      |
| 26   | DAVE MLS Key Package                | client            | MLS Key Package for pending group member                 | X      |
| 27   | DAVE MLS Proposals                  | server            | MLS Proposals to be appended or revoked                  | X      |
| 28   | DAVE MLS Commit Welcome             | client            | MLS Commit with optional MLS Welcome messages            | X      |
| 29   | DAVE MLS Announce Commit Transition | server            | MLS Commit to be processed for upcoming transition       | X      |
| 30   | DAVE MLS Welcome                    | server            | MLS Welcome to group for upcoming transition             | X      |
| 31   | DAVE MLS Invalid Commit Welcome     | client            | Flag invalid commit or welcome, request re-add           |        |

Codes 10, 12, and 14 through 20 are not documented upstream. Opcodes named only in the version-change
table (channel options, code version, video sink wants) have no assigned number on either upstream
page.

## Voice close event codes

| Code | Description                   | Explanation                                                                                                       |
| ---- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 4001 | Unknown opcode                | You sent an invalid opcode.                                                                                       |
| 4002 | Failed to decode payload      | You sent an invalid payload in your identifying to the Gateway.                                                    |
| 4003 | Not authenticated             | You sent a payload before identifying with the Gateway.                                                            |
| 4004 | Authentication failed         | The token you sent in your identify payload is incorrect.                                                          |
| 4005 | Already authenticated         | You sent more than one identify payload. Stahp.                                                                    |
| 4006 | Session no longer valid       | Your session is no longer valid.                                                                                   |
| 4009 | Session timeout               | Your session has timed out.                                                                                       |
| 4011 | Server not found              | We can't find the server you're trying to connect to.                                                              |
| 4012 | Unknown protocol              | We didn't recognize the protocol you sent.                                                                         |
| 4014 | Disconnected                  | Disconnect individual client (you were kicked, the main gateway session was dropped, etc.). Should not reconnect.   |
| 4015 | Voice server crashed          | The server crashed. Our bad! Try resuming.                                                                         |
| 4016 | Unknown encryption mode       | We didn't recognize your encryption.                                                                               |
| 4017 | E2EE/DAVE protocol required   | This channel requires a client supporting E2EE via the DAVE Protocol.                                              |
| 4020 | Bad request                   | You sent a malformed request                                                                                       |
| 4021 | Disconnected: Rate Limited    | Disconnect due to rate limit exceeded. Should not reconnect.                                                       |
| 4022 | Disconnected: Call Terminated | Disconnect all clients due to call terminated (channel deleted, voice server changed, etc.). Should not reconnect. |

Codes 4007, 4008, 4010, 4013, 4018 and 4019 are not documented upstream.

## Connecting to voice: retrieving voice server information

The first step in connecting to a voice server (and in turn, a guild's voice channel) is formulating a
request that can be sent to the Gateway, which will return information about the voice server to
connect to. Because Discord's voice platform is widely distributed, **users should never cache or save
the results of this call.** To inform the gateway of your intent to establish voice connectivity, first
send an **Opcode 4 Gateway Voice State Update** (a Gateway opcode, not a voice opcode — call the Skill
tool with `"discord-gateway"`).

###### Gateway Voice State Update Example

```json
{
  "op": 4,
  "d": {
    "guild_id": "41771983423143937",
    "channel_id": "127121515262115840",
    "self_mute": false,
    "self_deaf": false
  }
}
```

If the request succeeded, the gateway will respond with **two** events — a `VOICE_STATE_UPDATE` event
and a `VOICE_SERVER_UPDATE` event — meaning your library must properly wait for **both** events before
continuing. The first will contain a new key, `session_id`, and the second will provide voice server
information used to establish a new voice connection:

###### Example Voice Server Update Payload

```json
{
  "t": "VOICE_SERVER_UPDATE",
  "s": 2,
  "op": 0,
  "d": {
    "token": "my_token",
    "guild_id": "41771983423143937",
    "endpoint": "sweetwater-12345.discord.media:2048"
  }
}
```

With this information, you can move on to establishing a voice WebSocket connection.

When sending a voice state update to change channels within the same guild, it is possible to receive
a `VOICE_SERVER_UPDATE` with the **same `endpoint`** as the previous `VOICE_SERVER_UPDATE`. The `token`
will be changed and **you cannot re-use the previous session during a channel change, even if the
endpoint remains the same.**

Upstream note: "Bot users respect the voice channel's user limit, if set. When the voice channel is
full, you will not receive the Voice State Update or Voice Server Update events in response to your own
Voice State Update. Having `MOVE_MEMBERS` permission bypasses this limit and allows you to join
regardless of the channel being full or not."

## Establishing a voice WebSocket connection

Once you retrieve a `session_id`, `token`, and `endpoint`, you can connect and handshake with the voice
server over another secure WebSocket. Unlike the gateway endpoint received in an HTTP Get Gateway
request, **the endpoint received from the Voice Server Update payload does not contain a URL protocol**,
so some libraries may require manually prepending it with `wss://` before connecting.

Once connected to the voice WebSocket endpoint, send an **Opcode 0 Identify** payload with
`server_id`, `user_id`, `session_id`, and `token`:

###### Example Voice Identify Payload

```json
{
  "op": 0,
  "d": {
    "server_id": "41771983423143937",
    "user_id": "104694319306248192",
    "session_id": "my_session_id",
    "token": "my_token",
    "max_dave_protocol_version": 1
  }
}
```

The voice server should respond with an **Opcode 2 Ready** payload, which informs you of the `SSRC`,
UDP IP/port, and supported encryption modes the voice server expects:

###### Example Voice Ready Payload

```json
{
  "op": 2,
  "d": {
    "ssrc": 1,
    "ip": "127.0.0.1",
    "port": 1234,
    "modes": ["xsalsa20_poly1305", "xsalsa20_poly1305_suffix", "xsalsa20_poly1305_lite"],
    "heartbeat_interval": 1
  }
}
```

**`heartbeat_interval` here is an erroneous field and should be ignored.** The correct
`heartbeat_interval` value comes from the Hello payload.

The `modes` array in this particular upstream example lists three now-deprecated modes; see
[Transport encryption modes](#transport-encryption-modes) for the currently available set.

## Heartbeating

In order to maintain your WebSocket connection, you need to continuously send heartbeats at the
interval determined in **Opcode 8 Hello**:

###### Example Hello Payload

```json
{
  "op": 8,
  "d": {
    "heartbeat_interval": 41250,
  }
}
```

After receiving Opcode 8 Hello, send **Opcode 3 Heartbeat** — which contains an integer nonce — every
elapsed interval:

###### Example Heartbeat Payload since V8

```json
{
  "op": 3,
  "d": {
    "t": 1501184119561,
    "seq_ack": 10
  }
}
```

Since voice gateway version 8, heartbeat messages **must** include `seq_ack`, which contains the
sequence number of the last numbered message received from the gateway. See
[Buffered resume](#buffered-resume).

###### Example Heartbeat Payload below V8

```json
{
  "op": 3,
  "d": 1501184119561
}
```

In return, you will be sent back an **Opcode 6 Heartbeat ACK** that contains the previously sent nonce:

###### Example Heartbeat ACK Payload since V8

```json
{
  "op": 6,
  "d": {
    "t": 1501184119561
  }
}
```

###### Example Heartbeat ACK Payload below V8

```json
{
  "op": 6,
  "d": 1501184119561
}
```

## Establishing a voice UDP connection

Once you receive the properties of a UDP voice server from the Opcode 2 Ready payload, you can proceed
to the final step of voice connections: establishing and handshaking a UDP connection for voice data.

###### Example Ready Payload

```json
{
  "op": 2,
  "d": {
    ...,
    "modes": ["aead_aes256_gcm_rtpsize", "aead_xchacha20_poly1305_rtpsize", "xsalsa20_poly1305_lite_rtpsize"]
  }
}
```

First, open a UDP connection to the IP and port provided in the Ready payload. If required, you can now
perform an [IP Discovery](#ip-discovery) using this connection. Once you have fully discovered your
external IP and UDP port, tell the voice WebSocket what it is, and start receiving/sending data. Do
this using **Opcode 1 Select Protocol**:

###### Example Select Protocol Payload

```json
{
  "op": 1,
  "d": {
    "protocol": "udp",
    "data": {
      "address": "127.0.0.1",
      "port": 1337,
      "mode": "aead_aes256_gcm_rtpsize"
    }
  }
}
```

An unrecognized `protocol` closes the socket with `4012`; an unrecognized `mode` with `4016`.

## Transport encryption and sending voice

Transport encryption between the client and the selective forwarding unit (SFU) is still used **even in
E2EE calls**.

Voice data sent to Discord should be encoded with **Opus**, using **two channels (stereo)** and a
sample rate of **48kHz**. Voice data is sent using an **RTP header** (RFC 3550), followed by encrypted
Opus audio data. Voice encryption uses the key passed in Opcode 4 Session Description and the nonce
formed with the 12 byte header appended with 12 null bytes to achieve the 24 required by
`xsalsa20_poly1305`. Discord encrypts with the **libsodium** encryption library.

## Transport encryption modes

| Mode                               | Key                              | Nonce                                                 | Status                |
| ---------------------------------- | -------------------------------- | ----------------------------------------------------- | --------------------- |
| AEAD AES256-GCM (RTP Size)         | aead_aes256_gcm_rtpsize          | 32-bit incremental integer value, appended to payload | Available (Preferred) |
| AEAD XChaCha20 Poly1305 (RTP Size) | aead_xchacha20_poly1305_rtpsize  | 32-bit incremental integer value, appended to payload | Available (Required)  |
| XSalsa20 Poly1305 Lite (RTP Size)  | xsalsa20_poly1305_lite_rtpsize   | 32-bit incremental integer value, appended to payload | Deprecated            |
| AEAD AES256-GCM                    | aead_aes256_gcm                  | 32-bit incremental integer value, appended to payload | Deprecated            |
| XSalsa20 Poly1305                  | xsalsa20_poly1305                | Copy of RTP header                                    | Deprecated            |
| XSalsa20 Poly1305 Suffix           | xsalsa20_poly1305_suffix         | 24 random bytes                                       | Deprecated            |
| XSalsa20 Poly1305 Lite             | xsalsa20_poly1305_lite           | 32-bit incremental integer value, appended to payload | Deprecated            |

Upstream warnings:

> The deprecated encryption modes above will be discontinued as of November 18th, 2024. As of this
> date the voice gateway will not allow you to connect with one of the deprecated encryption modes.

> The nonce has to be stripped from the payload before encrypting and before decrypting the audio data.

The **RTP size** variants determine the unencrypted size of the RTP header in the same way as SRTP
(RFC 3711 §3.1), which considers CSRCs and (optionally) the extension preamble to be part of the
unencrypted header. The deprecated variants use a **fixed size** unencrypted header for RTP.

The voice gateway will report what encryption modes are available in Opcode 2 Ready.

Voice gateway compatible modes will **always** include `aead_xchacha20_poly1305_rtpsize` but **may not**
include `aead_aes256_gcm_rtpsize` depending on the underlying hardware. **You must support
`aead_xchacha20_poly1305_rtpsize`. You should prefer to use `aead_aes256_gcm_rtpsize` when it is
available.**

Include your selected mode in Opcode 1 Select Protocol.

Finally, the voice server will respond with an **Opcode 4 Session Description** that includes the
`mode` and `secret_key`, a **32 byte array** used for transport encryption and sending voice data:

###### Example Session Description Payload

```json
{
  "op": 4,
  "d": {
      "mode": "aead_aes256_gcm_rtpsize",
      "secret_key": [ ...251, 100, 11...],
      "dave_protocol_version": 1
  }
}
```

You can now start encrypting and sending voice data over the previously established UDP connection.

## Voice packet structure

| Field           | Type                          | Size    |
| --------------- | ----------------------------- | ------- |
| Version + Flags | Single byte value of `0x80`   | 1 byte  |
| Payload Type    | Single byte value of `0x78`   | 1 byte  |
| Sequence        | Unsigned short (big endian)   | 2 bytes |
| Timestamp       | Unsigned integer (big endian) | 4 bytes |
| SSRC            | Unsigned integer (big endian) | 4 bytes |
| Encrypted audio | Binary data                   | n bytes |

The fixed part is therefore 12 bytes (offsets 0, 1, 2–3, 4–7, 8–11), followed by the encrypted audio at
offset 12. This is the "12 byte header" referenced by the `xsalsa20_poly1305` nonce construction above.

## Speaking

Speaking updates are used to update the **speaking modes** used by the client. This speaking mode is
set using an **Opcode 5 Speaking** payload. **The client must send this at least once before sending
audio** to update the SSRC and set the initial speaking mode.

The following flags can be used as a bitwise mask. For example `5` would be priority and voice. **The
speaking mode should not be 0 to allow sending audio.**

| Flag       | Meaning                                                        | Value    |
| ---------- | -------------------------------------------------------------- | -------- |
| Microphone | Normal transmission of voice audio                             | `1 << 0` |
| Soundshare | Transmission of context audio for video, no speaking indicator | `1 << 1` |
| Priority   | Priority speaker, lowering audio of other speakers             | `1 << 2` |

###### Example Speaking Payload

```json
{
  "op": 5,
  "d": {
    "speaking": 5,
    "delay": 0,
    "ssrc": 1
  }
}
```

Upstream warning: "You must send at least one Opcode 5 Speaking payload before sending voice data, or
you will be disconnected with an invalid SSRC error."

Upstream note: "The `delay` property should be set to `0` for bots that use the voice gateway."

## Voice data interpolation

When there's a break in the sent data, the packet transmission shouldn't simply stop. Instead, **send
five frames of silence (`0xF8, 0xFF, 0xFE`)** before stopping, to avoid unintended Opus interpolation
with subsequent transmissions.

## Resuming a voice connection

When your client detects that its connection has been severed, it should open a **new** WebSocket
connection. Once the new connection has been opened, send an **Opcode 7 Resume** payload:

###### Example Resume Connection Payload Since V8

```json
{
  "op": 7,
  "d": {
    "server_id": "41771983423143937",
    "session_id": "my_session_id",
    "token": "my_token",
    "seq_ack": 10
  }
}
```

###### Example Resume Connection Payload Before V8

```json
{
  "op": 7,
  "d": {
    "server_id": "41771983423143937",
    "session_id": "my_session_id",
    "token": "my_token"
  }
}
```

If successful, the voice server will respond with an **Opcode 9 Resumed** to signal that your client is
now resumed:

###### Example Resumed Payload

```json
{
  "op": 9,
  "d": null
}
```

If the resume is unsuccessful — for example, due to an invalid session — the WebSocket connection will
close with the appropriate [voice close event code](#voice-close-event-codes). You should then follow
the connecting flow to reconnect.

## Buffered resume

Since voice gateway version 8, the gateway can **resend buffered messages that have been lost upon
resume**. To support this, the gateway includes a sequence number with all messages that may need to be
re-sent.

###### Example Message With Sequence Number

```json
{
  "op": 5,
  "d": {
    "speaking": 0,
    "delay": 0,
    "ssrc": 110
  },
  "seq": 10
}
```

A client using voice gateway version 8 **must** include the last sequence number they received under
the data `d` key as `seq_ack` in **both** the Opcode 3 Heartbeat and Opcode 7 Resume payloads.

If no sequence numbered messages have been received, `seq_ack` can be **omitted or included with a
value of `-1`**.

The gateway server uses a fixed bit length sequence number and handles wrapping the sequence number
around. Since voice gateway messages will always arrive in order, a client only needs to retain the
last sequence number it has seen.

If the session is successfully resumed the voice gateway will respond with an Opcode 9 Resumed and will
re-send any messages that the client did not receive.

The resume **may be unsuccessful** if the voice gateway buffer for the session no longer contains a
message that has been missed. In this case the session will be closed and you should then follow the
connecting flow to reconnect.

## IP discovery

Generally routers on the Internet mask or obfuscate UDP ports through a process called NAT. Most users
who implement voice will want to utilize IP discovery to find their external IP and port, which will
then be used for receiving voice communications. To retrieve your external IP and port, send the
following UDP packet to your voice port (**all numeric are big endian**):

| Field   | Description                                                    | Size     |
| ------- | -------------------------------------------------------------- | -------- |
| Type    | Values 0x1 and 0x2 indicate request and response, respectively | 2 bytes  |
| Length  | Message length excluding Type and Length fields (value 70)     | 2 bytes  |
| SSRC    | Unsigned integer                                               | 4 bytes  |
| Address | Null-terminated string in response                             | 64 bytes |
| Port    | Unsigned short                                                 | 2 bytes  |

Total packet size is 74 bytes: 2 + 2 + 4 + 64 + 2, with the `Length` value of 70 covering everything
after the Type and Length fields. Send with `Type = 0x1` and read the reply with `Type = 0x2`; the
discovered external address is the null-terminated string in the 64-byte `Address` field and the
external port is the trailing unsigned short. The `SSRC` is the one received in Opcode 2 Ready.

## End-to-end encryption (DAVE protocol)

Since September 2024, Discord is migrating voice and video in DMs, Group DMs, voice channels, and Go
Live streams to use end-to-end encryption (E2EE).

Upstream warning: "To support our long-term privacy goals, we will **only support E2EE calls starting
on March 1st, 2026** for all audio and video conversations in direct messages (DMs), group messages
(GDMs), voice channels, and Go Live streams on Discord. We highly recommend you implement DAVE support
as soon as possible to ensure a smooth transition."

**The upstream page is explicit that this section is a high-level overview only**, centered around the
voice gateway opcodes necessary for the protocol. The most thorough documentation on the DAVE protocol
is the Protocol Whitepaper at <https://daveprotocol.com>. Discord's open-source library
<https://github.com/discord/libdave> may be leveraged or referred to. **The exact format of the DAVE
protocol opcodes is detailed in the Voice Gateway Opcodes section of the protocol whitepaper**
(<https://daveprotocol.com/#voice-gateway-opcodes>) and is not reproduced on the Discord docs page.

When a call is E2EE, all members of the call exchange keys via a **Messaging Layer Security** (MLS,
RFC 9420) group. This group is used to derive per-sender ratcheted media keys (known only to the
participants of the group) to encrypt/decrypt media frames sent in the call.

### Binary WebSocket messages

To reduce overhead, some of the new DAVE protocol opcodes are sent as **binary** instead of JSON text.
See the `Binary` column in [Voice opcodes](#voice-opcodes) to identify these opcodes. Binary WebSocket
messages have the following format:

| Field           | Description                                                        | Size           |
| --------------- | ------------------------------------------------------------------ | -------------- |
| Sequence Number | OPTIONAL (server -> client only) big-endian uint16 sequence number | 2 bytes        |
| Opcode          | Unsigned integer opcode value                                      | 1 bytes        |
| Payload         | Binary message payload (format defined by opcode)                  | Variable bytes |

Sequence numbers are only sent from the server to the client, and **all server-sent binary opcodes
require the sequence number**. See [Buffered resume](#buffered-resume) for how sequence numbers are
used when present.

### Indicating DAVE protocol support

Include the highest DAVE protocol version you support in **Opcode 0 Identify** as
`max_dave_protocol_version`. **Sending version 0, or omitting the `max_dave_protocol_version` field,
indicates no DAVE protocol support.**

The voice gateway specifies the initial protocol version in **Opcode 4 Session Description** under
`dave_protocol_version`. This may be any non-discontinued protocol version equal to or less than your
supported protocol version.

Upstream warning: "Clients must retain backwards-compatibility of any non-discontinued DAVE protocol
versions. The voice gateway selects the lowest shared protocol version for the call."

### Protocol transitions

The voice gateway negotiates protocol version and MLS group transitions, to ensure the continuity of
media being sent for the call. This can occur when the call is upgrading/downgrading to/from E2EE (in
the initial transition phase), changing protocol versions, or when the MLS group is changing.

Some opcodes include a **transition ID**. After preparing local state necessary to perform the
transition, send **Opcode 23 DAVE Protocol Transition Ready** to indicate to the voice gateway that you
are ready to execute the transition. When all participants are ready or when a timeout has been
reached, the voice gateway dispatches **Opcode 22 DAVE Protocol Execute Transition** to confirm
execution of the transition. The transition execution is what indicates to media senders that they can
begin sending media with the new protocol context (e.g. without E2EE after a downgrade, with a new
protocol version after a protocol version change, or using a new key ratchet after a group participant
change).

#### Downgrade

Downgrades to protocol version 0 are announced via **Opcode 21 DAVE Protocol Prepare Transition**. This
can occur during the transition phase when a client that does not support the protocol joins the call.
When this transition is executed, senders should **stop** sending media using the protocol format.

#### Protocol version change and upgrade

Protocol version transitions (including upgrades from protocol version 0) are announced via **Opcode 24
DAVE Protocol Prepare Epoch**. In addition to the `transition_id`, this opcode includes the `epoch` for
the upcoming MLS epoch.

Receiving Opcode 24 with `epoch = 1` indicates that a **new MLS group is being created**. Participants
must:

- prepare a local MLS group with the parameters appropriate for the DAVE protocol version
- generate and send **Opcode 26 DAVE MLS Key Package** to deliver a new MLS key package to the voice
  gateway

When the `epoch` is greater than 1, the protocol version of the existing MLS group is changing.

When the transition is executed, senders must start sending media using the new protocol context (e.g.
formatted for the new protocol version or using a new key ratchet).

#### MLS group changes

When the participants of the MLS group must change, **existing** participants receive an **Opcode 29
DAVE MLS Announce Commit Transition**, whereas **new** members being added to the group receive
**Opcode 30 DAVE MLS Welcome**. Both opcodes include the transition ID and binary MLS Commit or MLS
Welcome message.

To prepare for the protocol transition, existing group members must apply the commit to progress their
local MLS group to the correct next state. Opcode 23 DAVE Protocol Transition Ready is sent when the MLS
commit has been processed.

Welcomed members send Opcode 23 DAVE Protocol Transition Ready after successfully joining the group
received in the MLS Welcome message.

### External sender

The voice gateway **must be an external sender** of the MLS group, so that it can send external MLS
proposals to add and remove call participants when appropriate (i.e. proposing the addition of new
members when they connect and the removal of previous members when they disconnect).

DAVE protocol participants **only** process proposals which arrive from the external sender, and not
from any other group members. The external sender **only sends Add or Remove proposals**.

The voice gateway uses **Opcode 25 DAVE MLS External Sender Package** to provide the external sender
public key and credential to MLS group participants. This message may be sent immediately on voice
gateway connection or at a later time when the call is upgrading to use the DAVE protocol.

Group creators must include the external sender they receive from the voice gateway in their MLS group
extensions when creating the group. Welcomed group members ensure that the expected external sender
extension is present in the group they are about to join.

### Joining the MLS group

Except for the initial creation of the first group for the call, joining the MLS group always occurs
after receiving Opcode 30 DAVE MLS Welcome.

#### Key packages

To be proposed to be added to the MLS group, pending members must send an MLS key package via **Opcode
26 DAVE MLS Key Package**. **Key packages are only used one time**, and a new key package must be
generated each time a pending member is waiting to be added or re-added to the group.

##### Identity public key

MLS participants use an asymmetric keypair for MLS message signatures and authentication. The public
key of this keypair is included in the key package and MLS tree. It is known to other participants in
the call and is leveraged for out-of-band identity verification.

You can choose to generate a new ephemeral keypair for every protocol call or use the same persistent
keypair at all times.

#### Initial group

When there is not yet an MLS group (e.g. a transport-only encrypted call is upgrading, or two members
have just joined a new call) all pending group members create a local group using the MLS parameters
defined by the DAVE protocol version and including the voice gateway external sender received via
Opcode 25 DAVE MLS External Sender Package. **Every pending member of the group has the chance to
produce the initial commit** that creates the MLS group with `epoch = 1`.

Pending group members receive add proposals for every other pending group member from the voice
gateway. If an additional pending member joins while there is not yet an MLS group, they receive all
in-flight proposal messages.

Proposal and commit handling follows the same process whether or not there is an established group; see
[Proposals and commits](#proposals-and-commits).

#### Welcome

Pending group members receive a welcome message from another group member which adds them to the MLS
group. This is dispatched from the voice gateway via Opcode 30 DAVE MLS Welcome.

#### Invalid group

If the group received in an Opcode 30 DAVE MLS Welcome or Opcode 29 DAVE MLS Announce Commit Transition
is unprocessable, the member receiving the unprocessable message sends **Opcode 31 DAVE MLS Invalid
Commit Welcome** to the voice gateway. Additionally, the local group state is reset and a new key
package is generated and sent to the voice gateway via Opcode 26 DAVE MLS Key Package.

This causes the voice gateway to propose the removal and re-addition of the requesting member.

### Proposals and commits

The voice gateway dispatches proposals which must be appended or revoked via **Opcode 27 DAVE MLS
Proposals**. All members of the established or pending MLS group must append or revoke the proposals
they receive, and then produce an MLS commit message and optionally an MLS welcome message (when
committing add proposals which add new members) which they send to the voice gateway via **Opcode 28
DAVE MLS Commit Welcome**.

In each epoch, the voice gateway dispatches the "winning" commit via Opcode 29 DAVE MLS Announce Commit
Transition and optionally the associated welcome messages via Opcode 30 DAVE MLS Welcome. The voice
gateway broadcasts the **first valid** commit and welcome(s) it sees in the given epoch, and **drops**
any commits later received for the out-of-date epoch. **All dispatched unrevoked proposals in the epoch
must be included in the commit for it to be valid. All members added in the epoch must be welcomed for
the welcome to be valid.**

### Audio frame E2EE

While transport encryption operates at the **packet** level, E2EE enabled by the DAVE protocol operates
at the **frame** level.

When any DAVE protocol is enabled for a call, the **full contents of OPUS frames** sent and received by
call participants are end-to-end encrypted.

#### ULEB128 encoding

Some fields in the protocol frame payload use **ULEB128 encoding** (unsigned LEB128). This is a
variable-length code compression to represent arbitrarily large unsigned integers in a small number of
bytes.

#### Payload format

| Field                      | Description                                                | Size           |
| -------------------------- | ---------------------------------------------------------- | -------------- |
| E2EE OPUS Frame            | Ciphertext for E2EE OPUS frame                             | Variable bytes |
| AES-GCM Auth. Tag          | Truncated AES128-GCM AEAD Authentication Tag               | 8 bytes        |
| ULEB128 Nonce              | ULEB128 synchronization nonce                              | Variable bytes |
| ULEB128 Unencrypted Ranges | ULEB128 offset/length pairs of E2EE frame unencrypted data | Variable bytes |
| Supplemental Data Size     | Unsigned integer bytes size of supplemental data           | 1 byte         |
| Magic Marker               | 0xFAFA marker to assist with protocol frame identification | 2 bytes        |

The E2EE OPUS frame is the full ciphertext resulting from the AES128-GCM AEAD encryption described
below. The authentication tag is an 8-byte truncated version of the authentication tag resulting from
the AEAD encryption.

The ULEB128 nonce is a variable length representation of the nonce used for encryption/decryption.

The ULEB128 unencrypted ranges field is **empty (0 bytes) for OPUS frames**, because the full contents
of the frame are encrypted.

The supplemental data size is the sum of bytes required for:

- 8-byte authentication tag
- Variable length ULEB128 nonce
- Variable length ULEB128 unencrypted ranges
- 1 byte supplemental data size
- 2 byte magic marker

The magic marker is a constant 2-byte value **0xFAFA**. This is used by media receivers to detect
protocol frames as well as by the SFU to avoid sending protocol frames to non-protocol-supporting
receivers during transition periods.

#### Frame encryption

Media frames are encrypted for E2EE using **AES128-GCM**.

##### Sender key derivation

Each media sender has a **ratcheted per-sender key**. There is a new per-sender ratchet created in each
MLS group epoch. The initial secret for each sender's ratchet is an exported **16-byte** secret from the
MLS group. Keys are retrieved from the ratchet via a generation counter derived from the
**most-significant byte of the 4-byte nonce**.

For very long lived epochs, the **nonce wrap-around must be handled** so the generation does not also
wrap back around to 0.

See the Sender Key Derivation section of the Protocol Whitepaper
(<https://daveprotocol.com/#sender-key-derivation>) for the detailed process — the Discord docs page
does not state it.

##### Nonce

The nonce passed to the AES128-GCM encryption and decryption functions is a **full 12-byte nonce**, but
the protocol only uses at most 4 bytes. The 12-byte nonce can be expanded from a 4-byte truncated nonce
by setting the **8 most significant bytes of the nonce to zero**, with the 4 least significant bytes
carrying the value of the truncated nonce.

The generation used for the sender's key ratchet is retrieved from the most-significant byte of the
4-byte nonce (i.e. the 4th least significant byte of the full 12-byte nonce).

##### Authentication tag

The authentication tag resulting from the AES128-GCM encryption is **truncated to 8 bytes**. Some
implementations may provide the desired tag length as a parameter, whereas some may always return the
full 12-byte tag from which the 4 least significant bytes should be removed.

##### AEAD additional data

**OPUS frames are fully encrypted and no additional data is passed to the AEAD.**

## Source

Discord Developer Documentation:
- <https://docs.discord.com/developers/topics/voice-connections>
- <https://docs.discord.com/developers/topics/opcodes-and-status-codes> (voice opcodes, voice close event codes)

Retrieved 2026-08-26.
