#!/usr/bin/env python3
"""UserPromptSubmit: point Claude at the octo-api skills, but only on brand anchors.

The API's domain vocabulary — product, booking, availability, pricing, cart, unit, option — is
everyday language in e-commerce work, so matching on it would fire this plugin while someone edits
a Shopware entity or a Symfony service. Only brand and protocol tokens match here.

Never blocks. Exits 0 on every path.
"""
from __future__ import annotations

import json
import re
import sys

# Each alternative below is unambiguous: it cannot plausibly appear in a Shopware, Symfony,
# Vue or React prompt that has nothing to do with OCTO.
ANCHOR = re.compile(
    r"""(?xi)
    \bocto\b                  # OCTO / octo as a whole word
  | \bocto[-/][a-z]           # octo/pricing, octo-core, Octo-Capabilities, Octo-Env
  | \bventrata\b              # the reference implementation
  | \bgo[\s-]?city\b          # Go City / go-city / gocity
  | /octo/                    # the base path
  | \bavailabilityid\b        # protocol-specific identifier, no generic collision
  | \bx-capabilities\b        # legacy header alias
    """
)

HINT = (
    "OCTO/Ventrata context detected. Treat the octo-api plugin as the source of truth instead of "
    "recalling API details: its references are generated from the Ventrata OpenAPI specification "
    "and every field is verifiable. Load the skill that fits — octo-protocol (auth, the mandatory "
    "Octo-Capabilities header, error codes), octo-products, octo-availability, octo-bookings, "
    "octo-capabilities-commerce, octo-capabilities-fulfilment, octo-capabilities-platform, "
    "octo-gocity — or delegate to the octo-integrator agent. Check any field name against the "
    "skill's FIELD-INDEX.json before using it."
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    prompt = payload.get("prompt")
    if not isinstance(prompt, str) or not ANCHOR.search(prompt):
        return 0

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": HINT,
            }
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
