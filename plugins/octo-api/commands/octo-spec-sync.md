---
name: octo-spec-sync
description: Check the Ventrata OpenAPI specification for drift against this plugin's generated references, and regenerate them on request.
argument-hint: --check | --apply [--domain products|availability|bookings] [--group commerce|fulfilment|platform]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write
model: sonnet
---

# /octo-spec-sync

Keep the generated references identical to the upstream specification. `--check` is the default and
writes nothing outside `.spec-state.json`.

## Steps

1. **Resolve the specification URL.** `python3 scripts/resolve_blob.py --print-url`. The URL is
   content-addressed, so it changes whenever Ventrata publishes — never use the stored one to fetch.
2. **Download and hash.**
   `python3 scripts/resolve_blob.py --download /tmp/octo-openapi.yaml` prints URL and sha256.
3. **Compare against `.spec-state.json`** — `blobHash`, `specSha256` and the four `counts`
   (`paths`, `operations`, `schemas`, `capabilityFields`). Identical hash means no drift: report that
   and stop.
4. **Verify the current references** against the new specification:
   `python3 scripts/verify_spec.py --spec /tmp/octo-openapi.yaml --all`. Report each failure by
   category — new endpoint, new field, changed `required`, new capability attribution, removed field.
5. **On `--check`, stop here.** Update only `lastChecked` in `.spec-state.json`. Summarise what
   would change.
6. **On `--apply`**, regenerate:
   - `python3 scripts/extract_spec.py --spec /tmp/octo-openapi.yaml --domain <each>`
   - `python3 scripts/extract_caps.py --spec /tmp/octo-openapi.yaml --all`
   - `python3 scripts/extract_remaining.py --spec /tmp/octo-openapi.yaml` — run this **after** the
     two above, since it renders whatever they did not cover.
   - `python3 scripts/extract_enums.py --spec /tmp/octo-openapi.yaml`
   Hand-written prose below the prose marker is preserved automatically.

   If `extract_enums.py` reports a meaning for a value the specification no longer declares, it
   exits non-zero rather than writing: remove the stale entry from `MEANINGS` first. A new value
   with no meaning is listed without one — add it by hand.
7. **Verify again.** `verify_spec.py --all` must pass before you continue. A red verify means stop
   and report, not patch by hand.
8. **Record and document.** Update `.spec-state.json` (hash, counts, `lastChecked`, `specVersion`),
   add a `CHANGELOG.md` entry naming what changed, and bump the plugin version — patch for
   description-only changes, minor for new fields or endpoints, major when something was removed or
   a `required` flag changed.
9. **Update the counts in each `SKILL.md`** if a field count moved. They are quoted in prose and
   would otherwise contradict the references.

## Rules

Never hand-edit above a generated file's prose marker: the next run overwrites it. Never invent a
field to make a verify pass. If the specification became unreachable, report that and leave every
file untouched.
