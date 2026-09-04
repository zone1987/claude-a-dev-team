#!/usr/bin/env python3
"""Catch a ReUI MCP outage and hand the session its local fallback.

Fires on PostToolUseFailure for mcp__reui__* calls. The free plan allows 100 MCP
requests per day; once that is spent every further call returns 429 and the agent
would otherwise keep retrying a tool that cannot answer today. This marks the
session and points at the distilled reference files instead.

Never blocks (exit 0 on every path).
"""
import json
import os
import re
import sys

STATE_DIR = os.path.join(os.path.expanduser('~'), '.cache', 'reui-plugin')

# what the ReUI MCP answers, and what each means for the rest of the session
QUOTA = 'quota'
AUTH = 'auth'
LICENCE = 'licence'
REACH = 'reach'

FALLBACK = (
    'Fall back to the plugin\'s own reference files for the rest of this session: '
    'skills/reui-registry/references/ (FREE-VS-PREMIUM, PRIMITIVES, EXAMPLES-FREE), '
    'skills/reui-blocks/references/ (the 533 premium blocks by group), '
    'skills/reui-data|reui-forms|reui-layout/references/ (component APIs), '
    'skills/reui-setup/references/ (install, registry config, licence). '
    'They carry the registry and the component APIs offline. '
    'The shadcn CLI is unaffected: `npx shadcn@latest add @reui/<name> --yes` keeps working, '
    'and `npx shadcn@latest search @reui -q "..."` still searches the registry without the MCP.'
)

DIAGNOSIS = {
    QUOTA: (
        'ReUI MCP daily quota reached (free plan: 100 tool calls/day). '
        'Stop calling mcp__reui__* tools — every further call this session returns 429. '
        'The allowance resets the next day; a Pro or Ultimate licence removes the limit.'
    ),
    AUTH: (
        'ReUI MCP rejected the credential (401). Either the browser sign-in expired — run `/mcp` '
        'and re-authenticate `reui` — or, on the headless path, the `reui_pat_*` token in the '
        'Authorization header expired or was revoked, and re-authenticating cannot fix that: '
        'create a new token and update the header. A configured Authorization header always '
        'overrides the OAuth credential.'
    ),
    LICENCE: (
        'ReUI MCP refused this item as out of plan: the account is valid but the tier does not '
        'cover it. '
        'Premium blocks need Pro, icons and templates need Ultimate. '
        'Free primitives and every c-* example stay available.'
    ),
    REACH: (
        'The ReUI MCP server could not be reached or did not answer usably.'
    ),
}


def classify(text):
    low = text.lower()
    if '429' in low or 'rate limit' in low or 'daily limit' in low or 'quota' in low:
        return QUOTA
    if '403' in low or 'requiredplan' in low or 'licence' in low or 'license required' in low:
        return LICENCE
    if '401' in low or 'unauthorized' in low or 'unauthenticated' in low or 'www-authenticate' in low:
        return AUTH
    return REACH


def note_state(session, kind):
    """Remember a spent quota so a later failure in the same session stays quiet."""
    if kind != QUOTA or not session:
        return False
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        marker = os.path.join(STATE_DIR, re.sub(r'[^A-Za-z0-9_-]', '', str(session))[:64] + '.quota')
        if os.path.exists(marker):
            return True
        with open(marker, 'w') as fh:
            fh.write('1')
    except OSError:
        pass
    return False


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool = payload.get('tool_name') or ''
    if not isinstance(tool, str) or not tool.startswith('mcp__reui__'):
        return 0

    blob = json.dumps({
        k: payload.get(k) for k in ('tool_response', 'error', 'result', 'message', 'stderr')
    }, default=str)

    kind = classify(blob)
    already = note_state(payload.get('session_id'), kind)
    if already:
        return 0

    print(json.dumps({
        'additionalContext': '[reui] ' + DIAGNOSIS[kind] + ' ' + FALLBACK
    }))
    return 0


if __name__ == '__main__':
    sys.exit(main())
