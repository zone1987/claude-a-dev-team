# Tracking drift

A plugin distilled from an upstream source is correct on the day it is written. The state file is how
anyone can tell whether it still is. Rules: `SRC-06`, `COV-05`.

## The state file

`.<name>-state.json` at the plugin root, holding what a refresh needs to know:

```json
{
  "source": "Ventrata OCTO API",
  "documentation": "https://docs.ventrata.com",
  "specUrl": "https://…/openapi.yaml?alt=media",
  "specSha256": "d7bec97a0a90927782559758929a0734c785c3054eacd76b3425acad972efa38",
  "specVersion": "1.0.0",
  "counts": { "paths": 46, "operations": 65, "schemas": 139, "capabilityFields": 254 },
  "lastChecked": "2026-08-20",
  "note": "The spec URL is content-addressed: resolve it with scripts/resolve_blob.py, never hardcode it."
}
```

Three things earn their place: the **hash**, because it answers "did the source change" without
diffing; the **counts**, because they answer "did we lose anything" without re-extracting; and the
**note**, because it records the gotcha no field can express.

## `--check` and `--apply`

- **`--check`** compares upstream against the state file and reports drift. Read-only, so it is safe
  to run anywhere, and it is what belongs in CI.
- **`--apply`** re-extracts and updates the state file. Writes, so it is a deliberate act.

Keeping them separate matters: a check that silently updates the thing it is checking always passes.

## Nothing polls at session start

No hook, no `SessionStart` script, no network call when a session opens. Three reasons, and the first
is sufficient:

- A session-start network call runs before the user has asked for anything, and it fails on an
  offline machine.
- A `UserPromptSubmit` or `SessionStart` hook that reaches its timeout has its output **discarded**,
  so an unreliable check is worse than none.
- Drift is slow. A source changes over weeks; checking it per session pays a constant cost for a rare
  event.

Drift is checked when someone asks, by a command.

## What counts as drift

| Signal | Means |
|---|---|
| hash changed, counts equal | prose or formatting moved; re-read, probably no structural change |
| counts changed | something was added or removed; extraction has to run |
| URL 404 | the source moved; the citation is now unverifiable and the plugin is unmaintainable until fixed |
| quotation no longer verbatim | the upstream rewrote the sentence a rule rests on |

The last one is the subtle case: the fact may still be true while the wording that grounds it is gone.
Re-read the page and re-quote, rather than keeping a quotation that no longer exists.

## Record the mirror

The audit reads a mirror, so its hash belongs in the state file too. That is what makes a coverage
claim reproducible: a reader months later can confirm the audit ran against the same bytes.

## Source

Shape taken from `plugins/octo-api/.spec-state.json` in this marketplace, read 2026-08-21. Hook
timeout behaviour from [hooks](https://code.claude.com/docs/en/hooks), retrieved 2026-08-21.
