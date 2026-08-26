#!/usr/bin/env python3
"""Inject a routing hint when a prompt names an exact Discord identifier.

A hook cannot make a skill load — no such mechanism exists. What it can do is put the name of the
right skill in front of the model at the moment the prompt arrives, which is cheaper and more
reliable than hoping a description matched.

Deliberately narrow: it fires on exact Discord API vocabulary, never on the bare word "discord".
A prompt that merely mentions Discord in passing gets nothing, because a hint on every such prompt
would be noise, and noise is what makes a hint ignored.

Contract, and each line of it is load-bearing:
  - additionalContext sits at the TOP level of the JSON, never inside hookSpecificOutput. Nested,
    the hook exits 0, prints valid JSON, and the context silently never arrives.
  - UserPromptSubmit supports no matcher, so the match happens here, with the cheap test first.
  - Exit 0 on every path. A non-zero exit on this event only produces noise for the user.
"""
from __future__ import annotations

import json
import re
import sys

# Exact API vocabulary, mapped to the skill that owns it. A term earns a place here only if it
# belongs to Discord and to no other plugin in this marketplace.
ROUTES: list[tuple[str, str, str]] = [
    (
        "discord-gateway",
        r"\b(GUILD_MEMBERS|MESSAGE_CONTENT|GUILD_PRESENCES|privileged intent|gateway intent"
        r"|IDENTIFY|RESUMED|HELLO|INVALID_SESSION|op\s*code|opcode|GUILD_CREATE|MESSAGE_CREATE"
        r"|INTERACTION_CREATE|GUILD_MEMBER_ADD|PRESENCE_UPDATE|VOICE_STATE_UPDATE"
        r"|gateway\s+close\s+code|4014|shard(ing)?)\b",
        "intents, event payloads, opcodes and close codes",
    ),
    (
        "discord-interactions",
        r"\b(slash\s+command|application\s+command|APPLICATION_COMMAND|CHAT_INPUT"
        r"|interaction\s+token|action\s+row|select\s+menu|button\s+component|modal"
        r"|DEFERRED_CHANNEL_MESSAGE|InteractionCallbackType|autocomplete|components\s+v2"
        r"|ephemeral)\b",
        "command registration, callback types and every component type",
    ),
    (
        "discord-oauth2",
        r"\b(applications\.commands|identify\s+scope|guilds\.join|oauth2/authorize"
        r"|bot\s+invite|permissions\s+integer|permission\s+bit|linked\s+role"
        r"|role\s+connection|MANAGE_GUILD|ADMINISTRATOR|SEND_MESSAGES)\b",
        "scopes, the permission bitfield and linked roles",
    ),
    (
        "discord-rest",
        r"\b(snowflake|/channels/|/guilds/|/webhooks/|allowed_mentions|message_reference"
        r"|guild\s+member|audit\s+log|auto\s*mod(eration)?|forum\s+channel|MESSAGE_REFERENCE)\b",
        "resource objects, their fields and endpoints",
    ),
    (
        "discord-platform",
        r"\b(X-RateLimit|rate\s*limit\s+bucket|Retry-After|429|invalid\s+request\s+limit"
        r"|thread\s+metadata|archived\s+thread|app\s+discovery)\b",
        "the rate limit model, threads and discovery",
    ),
    (
        "discord-activities",
        r"\b(embedded\s+app\s+sdk|discordSdk|@discord/embedded-app-sdk|activity\s+iframe"
        r"|url\s+mapping|discord\s+activity)\b",
        "the Embedded App SDK and Activity constraints",
    ),
    (
        "discord-social-sdk",
        r"\b(social\s+sdk|provisional\s+account|discordpp|Client::|unified\s+friends"
        r"|linked\s+channel|game\s+invite)\b",
        "the game SDK, provisional accounts and lobbies",
    ),
    (
        "discord-monetization",
        r"\b(entitlement|SKU|app\s+subscription|one-time\s+purchase|ENTITLEMENT_CREATE"
        r"|iap\s+for\s+activities)\b",
        "SKUs, entitlements and subscriptions",
    ),
    (
        "discord-rpc-voice",
        r"\b(voice\s+opcode|xsalsa20|aead_|ip\s+discovery|rtp\s+header|discord\s+rpc"
        r"|SET_ACTIVITY|certified\s+device)\b",
        "the RPC and voice protocols",
    ),
    (
        "discord-bots",
        r"\b(discord\.com/api|Bot\s+token|API\s+v10|cdn\.discordapp\.com|discord\s+bot"
        r"|discord\s+app)\b",
        "base URL, auth, versioning, snowflakes and the CDN",
    ),
]

MAX_HINTS = 3


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    prompt = payload.get("prompt") or ""
    if not prompt:
        return 0

    # The cheap gate: no Discord vocabulary at all, no work and no output.
    if not re.search(r"discord|slash\s+command|snowflake|entitlement|gateway\s+intent", prompt, re.I):
        return 0

    hits: list[str] = []
    for skill, pattern, covers in ROUTES:
        if re.search(pattern, prompt, re.IGNORECASE):
            hits.append(f'- Call the Skill tool with "{skill}" for {covers}.')
        if len(hits) == MAX_HINTS:
            break

    if not hits:
        return 0

    lines = [
        "The `discord` plugin carries the Discord developer documentation in full, extracted from",
        "docs.discord.com. Exact values — field names, intent bits, component type numbers,",
        "permission bits, opcodes — come from its reference files, not from recall:",
        *hits,
        'For a task spanning several of these, delegate to the `discord:discord-dev` agent.',
    ]

    json.dump({"additionalContext": "\n".join(lines)}, sys.stdout)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # A hook that fails must never interrupt the user's prompt.
        sys.exit(0)
