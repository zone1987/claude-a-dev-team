---
name: discord-interactions
description: "Discord slash commands, interaction responses and the component system. Use when the request names a Discord slash command, a Discord interaction, or a modal."
---

# Discord Interactions, Commands and Components

Register application commands, receive interactions, respond inside the deadline, and build message and
modal UI from components. The references below carry all 20 component types with their integer IDs, 5
interaction types, 9 interaction callback types, 4 command types, 11 command option types and 24
endpoints, with every field, enum value, default and limit the upstream states.

## The interaction request/response cycle

1. **Register** a command over HTTP — `POST /applications/{application.id}/commands` global, or
   `.../guilds/{guild.id}/commands` per guild. Guild commands update instantly; global commands
   read-repair. A `POST` with an existing name is an upsert. 200 creates per day per guild.
2. **Receive** it one of two mutually exclusive ways: the `INTERACTION_CREATE` Gateway event, or HTTP to
   your Interactions Endpoint URL. HTTP requires acknowledging `PING` (`type: 1`) with `PONG`
   (`type: 1`) and verifying `X-Signature-Ed25519` over `X-Signature-Timestamp + rawBody` against the
   app's public key, answering `401` on failure. Discord probes the endpoint with deliberately invalid
   signatures and removes the URL if it passes them.
3. **Acknowledge within 3 seconds** via `POST /interactions/{interaction.id}/{interaction.token}/callback`,
   even when the interaction arrived over the Gateway — responses never go back over the Gateway.
   **Blowing the 3-second deadline invalidates the token** and the interaction is dead.
   - `4` `CHANNEL_MESSAGE_WITH_SOURCE` reply now · `5` `DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE` show a
     loading state and answer later
   - `6` `DEFERRED_UPDATE_MESSAGE` · `7` `UPDATE_MESSAGE` — components only
   - `8` `APPLICATION_COMMAND_AUTOCOMPLETE_RESULT` max 25 choices · `9` `MODAL` (never for
     `MODAL_SUBMIT` or `PING`) · `12` `LAUNCH_ACTIVITY` · `1` `PONG` · `10` `PREMIUM_REQUIRED`
     (deprecated)
4. **Follow up for 15 minutes**, the token's whole lifetime: `PATCH`/`DELETE`
   `/webhooks/{application.id}/{interaction.token}/messages/@original`, or `POST`
   `/webhooks/{application.id}/{interaction.token}` for a new message. `EPHEMERAL` is `1 << 6` (64) and
   an existing message's ephemeral state can never be changed, so choose it on the first response.
5. **Components** need the message flag `IS_COMPONENTS_V2` = `1 << 15` (32768). It is irreversible per
   message and disables `content`, `embeds`, `poll` and `stickers`; up to 40 components per message.

Interactive components carry a `custom_id` (1-100 characters, unique within the message) that returns in
the interaction payload. In messages, buttons and selects sit in an Action Row — 5 buttons **or** 1
select. In modals, each input sits in a Label (type 18); a modal holds 1 to 5 components.

## Reference map

- **[references/APPLICATION-COMMANDS.md](references/APPLICATION-COMMANDS.md)**: the 4 command types, the
  full command object, the option object with all 11 option types, choices, autocomplete, subcommands
  and groups with the one-level nesting rule, installation and interaction contexts, the permissions
  object with its 3 permission types and 2 constants, localization with its 3 locale fallbacks,
  age-restricted commands, all 16 command endpoints with every JSON and query parameter, and a 23-row
  table of every limit.
- **[references/RECEIVING-AND-RESPONDING.md](references/RECEIVING-AND-RESPONDING.md)**: the Interaction
  object's 21 fields, the 5 interaction types, 3 interaction context types,
  `authorizing_integration_owners`, the 4 `data` shapes, resolved data, the Ed25519 signature procedure
  in JavaScript, Python and Java verbatim, all 9 callback types, callback data for
  messages/autocomplete/modals, the 3 callback response objects, the 8 callback and followup endpoints,
  an assembled deferred-then-followup walkthrough, and every timing constraint.
- **[references/COMPONENTS-REFERENCE-INTERACTIVE.md](references/COMPONENTS-REFERENCE-INTERACTIVE.md)**:
  the 11 interactive components — Button (2) with 6 styles and its design guidelines, String Select (3),
  Text Input (4) with 2 styles, User (5), Role (6), Mentionable (7) and Channel (8) Select, File Upload
  (19), Radio Group (21), Checkbox Group (22), Checkbox (23) — each with its structure, its interaction
  response structure and both the send and submit payload examples.
- **[references/COMPONENTS-REFERENCE-LAYOUT-AND-CONTENT.md](references/COMPONENTS-REFERENCE-LAYOUT-AND-CONTENT.md)**:
  the complete 20-row component type table, component anatomy and `custom_id`, the 9 layout and content
  components — Action Row (1), Section (9), Text Display (10), Thumbnail (11), Media Gallery (12), File
  (13), Separator (14), Container (17), Label (18) — the Unfurled Media Item and its flag, file
  uploading, legacy behavior, an 8-row nesting matrix and a 31-row table of every component limit.
- **[references/USING-COMPONENTS.md](references/USING-COMPONENTS.md)**: the message-component walkthrough
  with its 3 payloads and the `?with_components=true` webhook query parameter, plus the modal walkthrough
  with the Label-wrapped String Select and Text Input payload.

## Related

Call the Skill tool with "discord-rest" for the message, channel, emoji and attachment objects an
interaction response targets, and for channel type integers. Call the Skill tool with "discord-gateway"
for the `INTERACTION_CREATE` event and the Application Command Permissions Update event. Call the Skill
tool with "discord-bots" for bot tokens, the `applications.commands` scope and app setup.

## Source

Distilled from the Discord Developer Documentation, retrieved 2026-08-26:

- `https://docs.discord.com/developers/interactions/overview`
- `https://docs.discord.com/developers/interactions/application-commands`
- `https://docs.discord.com/developers/interactions/receiving-and-responding`
- `https://docs.discord.com/developers/components/overview`
- `https://docs.discord.com/developers/components/reference`
- `https://docs.discord.com/developers/components/using-message-components`
- `https://docs.discord.com/developers/components/using-modal-components`
