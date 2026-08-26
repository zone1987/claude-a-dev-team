# Discord RPC — Transport, Handshake, Authorization, Error Codes

The local RPC server protocol: how to find it, how to open a session, how to authenticate, the
payload envelope every message uses, and every numeric error and close code.

## Contents

- [RPC over IPC](#rpc-over-ipc)
- [IPC path](#ipc-path)
- [Connecting to IPC](#connecting-to-ipc)
- [IPC opcodes](#ipc-opcodes)
- [RPC over WebSocket (deprecated)](#rpc-over-websocket-deprecated)
- [RPC server ports](#rpc-server-ports)
- [RPC versions](#rpc-versions)
- [Restrictions](#restrictions)
- [Payload structure](#payload-structure)
- [Authenticating](#authenticating)
- [The RPC token system](#the-rpc-token-system)
- [Voice settings single-modifier lock](#voice-settings-single-modifier-lock)
- [RPC error codes](#rpc-error-codes)
- [RPC close event codes](#rpc-close-event-codes)

## RPC over IPC

Discord's RPC server supports IPC (Inter-Process Communication) as transport for native applications
and games. This allows high-performance, local communication with the Discord client without
requiring network-level overhead.

Upstream warning: Discord recommends using the Discord Social SDK for new projects that are looking
to integrate Discord's social features into their game. (Call the Skill tool with
`"discord-social-sdk"`.)

## IPC path

| Platform    | Path Format                                                                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows     | `\\?\pipe\discord-ipc-{n}`                                                                                                                        |
| Linux/macOS | `${XDG_RUNTIME_DIR}/discord-ipc-{n}`, `${TMPDIR}/discord-ipc-{n}`, `${TMP}/discord-ipc-{n}`, `${TEMP}/discord-ipc-{n}`, or `/tmp/discord-ipc-{n}` |

On Linux/macOS, Discord resolves the IPC prefix in this order: `XDG_RUNTIME_DIR`, `TMPDIR`, `TMP`,
`TEMP`, then `/tmp` as a final fallback.

## Connecting to IPC

To begin a session, the application must open the IPC socket and send a `HANDSHAKE` opcode.

### Handshake payload

The payload is a JSON object containing the RPC version and your application's client ID.

| Field       | Type      | Description                  |
| ----------- | --------- | ---------------------------- |
| `v`         | `integer` | RPC version                  |
| `client_id` | `string`  | Your application's client ID |

###### Example Handshake

```
[00 00 00 00] // Opcode 0 (Handshake)
[2D 00 00 00] // Length 45
{"v":1,"client_id":"123456789012345678"}
```

Upon success, Discord will respond with a `FRAME` (Opcode `1`) containing the `READY` event.

Once the handshake is complete, all subsequent requests and responses use the `FRAME` opcode. The
internal structure of these frames follows the standard RPC Payload structure — see
[Payload structure](#payload-structure) below.

Note on the frame layout implied by the example: each IPC frame is preceded by a 4-byte little-endian
opcode followed by a 4-byte little-endian payload length, then the JSON body. The upstream page shows
this only through the example above and does not describe the framing in prose.

## IPC opcodes

| Opcode | Name        | Description                                   |
| ------ | ----------- | --------------------------------------------- |
| `0`    | `HANDSHAKE` | Sent by the client to initiate the connection |
| `1`    | `FRAME`     | Used for all standard RPC commands and events |
| `2`    | `CLOSE`     | Sent by either side to close the connection   |
| `3`    | `PING`      | Sent to check if the connection is alive      |
| `4`    | `PONG`      | Response to a `PING`                          |

## RPC over WebSocket (deprecated)

Upstream marks this section as deprecated and gated: "This is a deprecated way, which is only
available for old participants of private beta. It is preferable to use RPC that uses IPC."

All Discord clients have an RPC server running on localhost that allows control over local Discord
clients.

### Connecting to WebSocket

The local RPC server runs on localhost (`127.0.0.1`) and is set up to process WebSocket connections
and proxy API requests.

For WebSocket connections, the connection is always
`ws://127.0.0.1:PORT/?v=VERSION&client_id=CLIENT_ID&encoding=ENCODING`:

- `CLIENT_ID` is the client ID of the application accessing the RPC Server.
- `VERSION` is the version of the RPC Server.
- `PORT` is the port of the RPC Server.
- `ENCODING` is the type of encoding for this connection to use. `json` and `etf` are supported.

To begin, you'll need to create an app at `https://discord.com/developers/applications` and click the
big plus button. When you create an app on the Developers site, you must specify an "RPC Origin" and
"Redirect URI" from which to permit connections and authorizations. **The origin you send when
connecting and the redirect uri you send when exchanging an authorization code for an access token
must match one of the ones entered on the Developers site.**

When establishing a WebSocket connection, Discord verifies the `Origin` header on connection to
prevent client ID spoofing. You will be instantly disconnected if the Origin does not match.

If you're connecting to the RPC server from within a browser, RPC origins are usually in the form
`SCHEME://HOST[:PORT]`, where `SCHEME` is typically https or http, `HOST` is your domain or ip, and
`PORT` is the port of the webserver from which the user will be connecting (omitted for ports 80 and
443). For example, `https://discord.com` would be used if the user were connecting from
`https://discord.com/some/page/url`.

If you're connecting to the RPC server from within a non-browser application (like a game), you just
need to make sure that the origin is sent with the upgrade request when connecting to the WebSocket.
For local testing, Discord recommends testing with an origin like `https://localhost`. For production
apps, Discord recommends setting the origin to your company/game's domain, for example
`https://discord.com`.

## RPC server ports

The port range for Discord's local RPC server is [6463, 6472]. Since the RPC server runs locally,
there's a chance it might not be able to obtain its preferred port when it tries to bind to one. For
this reason, the local RPC server will pick one port out of a range of these 10 ports, trying
sequentially until it can bind to one. When implementing your client, you should perform the same
sequential checking to find the correct port to connect to.

Note the asymmetry with certified devices: the certified-devices page states the range as `6463` to
`6473` (11 ports), while this page states `[6463, 6472]` (10 ports). Both are reproduced as upstream
writes them. See CERTIFIED-DEVICES.md.

## RPC versions

| Version | Out of Service |
| ------- | -------------- |
| 1       | no             |

## Restrictions

For connections to the RPC server, a list of approved testers (see the `AUTHORIZE` command in
RPC-COMMANDS.md) is used to restrict access while you're still developing. You can invite up to 50
people.

For applications/games not approved, Discord limits you to creating 10 guilds and 10 channels. This
limit is raised to virtually unlimited after approval.

## Payload structure

| Field | Type   | Description                    | Present                                                  |
| ----- | ------ | ------------------------------ | -------------------------------------------------------- |
| cmd   | enum   | payload command (RPC command)  | Always                                                   |
| nonce | string | unique string used once for replies from the server | In responses to commands (not subscribed events)         |
| evt   | enum   | subscription event (RPC event) | In subscribed events, errors, and (un)subscribing events |
| data  | object | event data                     | In responses from the server                             |
| args  | object | command arguments              | In commands sent to the server                           |

The command enum is the RPC Commands table in RPC-COMMANDS.md; the event enum is the RPC Events table
in RPC-EVENTS.md.

## Authenticating

In order to call any commands over RPC, you must be authenticated or you will receive a code `4006`
error response. To begin, call `AUTHORIZE`:

###### RPC Authorize Example

```json
{
  "nonce": "f48f6176-4afb-4c03-b1b8-d960861f5216",
  "args": {
    "client_id": "192741864418312192",
    "scopes": ["rpc", "identify"]
  },
  "cmd": "AUTHORIZE"
}
```

The user will then be prompted to authorize your app to access RPC on Discord. The `AUTHORIZE`
command returns a `code` that you can exchange with a POST to
`https://discord.com/api/oauth2/token` containing the standard OAuth2 body parameters
(RFC 6749 §4.1.3) for the token exchange. The token endpoint on Discord's API will return an
`access_token` that can be sent with `AUTHENTICATE`:

###### RPC Authenticate Example

```json
{
  "nonce": "5bb10a43-1fdc-4391-9512-0c8f4aa203d4",
  "args": {
    "access_token": "EXAMPLE_BEARER_TOKEN_REDACTED"
  },
  "cmd": "AUTHENTICATE"
}
```

You can now call RPC commands on behalf of the authorized user.

## The RPC token system

**Discord currently does not allow access to RPC for unapproved apps without being on the game's list
of testers.** Discord grants 50 testing spots, which should be ample for development. After approval,
this restriction is removed and the app will be accessible to anyone.

Discord also has an RPC token system to bypass the user authorization modal. This is usable by
approved games as well as by users on a game's list of testers, and **also disallows use of the
`messages.read` scope**. If you have been granted access, you can send a POST request to
`https://discord.com/api/oauth2/token/rpc` with your application's `client_id` and `client_secret` in
the body (sent as a url-encoded body, **not JSON**). You can then pass the returned `rpc_token` value
to the `rpc_token` field in your RPC authorize request (see `AUTHORIZE` in RPC-COMMANDS.md).

## Voice settings single-modifier lock

Upstream states this on both `SET_USER_VOICE_SETTINGS` and `SET_VOICE_SETTINGS`, verbatim:

> In the current release, we only support a single modifier of voice settings at a time over RPC. If
> an app changes voice settings, it will lock voice settings so that other apps connected
> simultaneously lose the ability to change voice settings. Settings reset to what they were before
> being changed after the controlling app disconnects. When an app that has previously set voice
> settings connects, the client will swap to that app's configured voice settings and lock voice
> settings again. This is a temporary situation that will be changed in the future.

## RPC error codes

Sent as the `data` of an `ERROR` event. Access to the RPC server requires approval from Discord.

| Code | Name                               | Description                                                                           |
| ---- | ---------------------------------- | ------------------------------------------------------------------------------------- |
| 1000 | Unknown error                      | An unknown error occurred.                                                            |
| 4000 | Invalid payload                    | You sent an invalid payload.                                                          |
| 4002 | Invalid command                    | Invalid command name specified.                                                       |
| 4003 | Invalid guild                      | Invalid guild ID specified.                                                           |
| 4004 | Invalid event                      | Invalid event name specified.                                                         |
| 4005 | Invalid channel                    | Invalid channel ID specified.                                                         |
| 4006 | Invalid permissions                | You lack permissions to access the given resource.                                    |
| 4007 | Invalid client ID                  | An invalid OAuth2 application ID was used to authorize or authenticate with.           |
| 4008 | Invalid origin                     | An invalid OAuth2 application origin was used to authorize or authenticate with.       |
| 4009 | Invalid token                      | An invalid OAuth2 token was used to authorize or authenticate with.                    |
| 4010 | Invalid user                       | The specified user ID was invalid.                                                    |
| 5000 | OAuth2 error                       | A standard OAuth2 error occurred; check the data object for the OAuth2 error details.  |
| 5001 | Select channel timed out           | An asynchronous `SELECT_TEXT_CHANNEL`/`SELECT_VOICE_CHANNEL` command timed out.        |
| 5002 | `GET_GUILD` timed out              | An asynchronous `GET_GUILD` command timed out.                                        |
| 5003 | Select voice force required        | You tried to join a user to a voice channel but the user was already in one.           |
| 5004 | Capture shortcut already listening | You tried to capture more than one shortcut key at once.                              |

Note: code `4006` is documented twice with different meanings depending on context. The
`Authenticating` section of the RPC page says an unauthenticated command yields "a code `4006` error
response"; the error-code table names `4006` "Invalid permissions — You lack permissions to access
the given resource." Both statements are upstream.

## RPC close event codes

| Code | Name              | Description                                                               |
| ---- | ----------------- | ------------------------------------------------------------------------- |
| 4000 | Invalid client ID | You connected to the RPC server with an invalid client ID.                |
| 4001 | Invalid origin    | You connected to the RPC server with an invalid origin.                   |
| 4002 | Rate limited      | You are being rate limited.                                               |
| 4003 | Token revoked     | The OAuth2 token associated with a connection was revoked, get a new one! |
| 4004 | Invalid version   | The RPC Server version specified in the connection string was not valid.  |
| 4005 | Invalid encoding  | The encoding specified in the connection string was not valid.            |

## Source

Discord Developer Documentation:
- <https://docs.discord.com/developers/topics/rpc>
- <https://docs.discord.com/developers/topics/opcodes-and-status-codes> (RPC error codes, RPC close event codes)

Retrieved 2026-08-26.
