---
name: discord-rpc-voice
description: "Discord local RPC and the voice protocol: RPC commands and events, voice opcodes, encryption. Use when the request names Discord RPC or a Discord voice connection."
---

# Discord RPC and Voice

Two local/real-time protocols that are **not** the Gateway: the **RPC server** running on the user's own
machine, and the **voice connection** a bot opens to a Discord voice server. Both are documented here to
the field.

## How these differ from the Gateway

| | Gateway | RPC | Voice |
|---|---|---|---|
| Endpoint | Discord's remote WSS gateway | `localhost` IPC pipe or `ws://127.0.0.1:PORT` | a per-call voice server (`wss://`) plus a UDP socket |
| Who runs it | Discord | the user's own Discord desktop client | Discord |
| Auth | bot token in Identify | OAuth2 `AUTHORIZE` then `AUTHENTICATE` (code `4006` until authenticated) | `session_id` + `token` from the Gateway |
| Envelope | `op`/`d`/`s`/`t` | `cmd`/`nonce`/`evt`/`data`/`args` | `op`/`d`, plus `seq` since v8 |
| Media | none | none | Opus over UDP in RTP packets |
| Access | any bot | **approved apps only**, or up to 50 listed testers | any bot in a voice channel |

**RPC is gated.** Unapproved apps reach RPC only through a 50-slot tester list, and are capped at 10
guilds and 10 channels. RPC over WebSocket is deprecated and open only to old private-beta participants;
new native integrations use IPC. Discord recommends the Social SDK for new social integrations.

**A voice connection always starts on the Gateway.** Send Gateway Opcode 4 Voice State Update, wait for
**both** `VOICE_STATE_UPDATE` (for `session_id`) and `VOICE_SERVER_UPDATE` (for `token` and `endpoint`),
then open the voice WebSocket with `?v=8`. Never cache the endpoint. On a channel change within one guild
the endpoint may repeat, but the token changes and the old session cannot be reused.

## Load-bearing facts

- **Voice gateway version 8 is the one to use.** Versions below 4 and the no-version default were
  discontinued on 2024-11-18. v8 adds message buffering: `seq_ack` is mandatory in Heartbeat and Resume.
- **`aead_xchacha20_poly1305_rtpsize` is mandatory to support**, `aead_aes256_gcm_rtpsize` is preferred
  when the gateway offers it. Every other named mode is deprecated and rejected since 2024-11-18.
- **Send at least one Opcode 5 Speaking before any audio**, with a non-zero mask, or you are disconnected
  for an invalid SSRC. Send five frames of silence (`0xF8, 0xFF, 0xFE`) when a transmission ends.
- **The `heartbeat_interval` in Opcode 2 Ready is erroneous.** Use the one from Opcode 8 Hello.
- **E2EE becomes mandatory on 2026-03-01** for DMs, GDMs, voice channels and Go Live. Declare support
  with `max_dave_protocol_version` in Identify; omitting it or sending 0 means no support.
- **RPC voice settings are single-writer.** The first app to change them locks out every other connected
  app until it disconnects.

## Reference map

- **[RPC-PROTOCOL.md](references/RPC-PROTOCOL.md)**: IPC paths per platform, the handshake frame with its byte
  layout, the 5 IPC opcodes, the deprecated WebSocket transport with origin checking and the
  `[6463, 6472]` port scan, RPC versions, the tester/guild/channel restrictions, the payload envelope,
  `AUTHORIZE`/`AUTHENTICATE` flow, the `rpc_token` bypass, all 16 RPC error codes and all 6 RPC close
  event codes.
- **[RPC-COMMANDS.md](references/RPC-COMMANDS.md)**: all 19 entries of the RPC command table, and every documented
  command with its argument structure, response structure and verbatim example payloads — including the
  full voice-settings object tree (input, output, mode, shortcut key combo, the 4 key types) and the
  certified-device argument shape.
- **[RPC-EVENTS.md](references/RPC-EVENTS.md)**: all 25 RPC events with subscription arguments, dispatch data
  structures and verbatim examples — `READY`, `ERROR`, the voice-state and voice-connection events with
  all 10 connection states, the 6 relationship types, the 8 entitlement types, and which events need the
  `rpc.notifications.read`, `relationships_read` or `identify.premium` scope.
- **[VOICE-CONNECTIONS.md](references/VOICE-CONNECTIONS.md)**: the whole voice lifecycle — the 8 gateway versions,
  all 23 voice opcodes with their numbers and binary flag, all 16 voice close event codes, the WebSocket
  and UDP handshakes, heartbeating in both pre-v8 and v8 shapes, all 7 transport encryption modes, the
  6-field RTP voice packet structure, the 3 speaking flags, resuming and buffered resume, the 5-field IP
  discovery packet, and the complete DAVE/MLS section with the E2EE frame payload format.
- **[CERTIFIED-DEVICES.md](references/CERTIFIED-DEVICES.md)**: the certification program, HTTP and WebSocket
  transports with query params, the `6463`–`6473` port scan, Windows/macOS device UUID retrieval with the
  `waveInMessage`/`waveOutMessage` examples, update cadence, priority ordering, and the Device, Vendor,
  Model and Device Type models.

## Related

Call the Skill tool with "discord-gateway" for the Voice State Update opcode that starts a voice
connection and for the activity object used by `SET_ACTIVITY`.
Call the Skill tool with "discord-oauth2" for the RPC scopes (`rpc`, `rpc.notifications.read`,
`relationships_read`, `identify.premium`, `messages.read`) and the token exchange.
Call the Skill tool with "discord-social-sdk" for the integration path Discord recommends over RPC for
new games.
Call the Skill tool with "discord-activities" for embedded activities inside a voice channel.
Call the Skill tool with "discord-rest" for the user, guild, channel, message and voice state objects
that RPC responses embed.
Call the Skill tool with "discord-monetization" for SKUs and entitlements behind `ENTITLEMENT_CREATE`.

## Source

Distilled from the Discord Developer Documentation:

- <https://docs.discord.com/developers/topics/rpc>
- <https://docs.discord.com/developers/topics/voice-connections>
- <https://docs.discord.com/developers/topics/certified-devices>
- <https://docs.discord.com/developers/topics/opcodes-and-status-codes> — voice opcodes, voice close
  event codes, RPC error codes and RPC close event codes, which the three pages above reference but do
  not contain.

Retrieved 2026-08-26. Rights holder of the original documentation: Discord Inc.
