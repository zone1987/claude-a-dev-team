---
name: octo-lookup
description: Look up an OCTO endpoint, schema, field or capability and print its parameters, required flags and a curl example.
argument-hint: <endpoint|schema|field|capability> [--vendor ventrata|gocity]
allowed-tools: Read, Glob, Grep
model: haiku
---

# /octo-lookup

Resolve `$ARGUMENTS` against this plugin's generated references and print the answer. Nothing else.

## Classify the argument

- Starts with `/` or contains an HTTP method → an **endpoint**. Look in the domain's `ENDPOINTS.md`.
- Starts with `octo/` → a **capability**. Look in `octo-capabilities-*/`, file named after the
  capability.
- Starts with an uppercase letter → a **schema**. Look in `*-SCHEMA.md` or `SUB-SCHEMAS*.md`.
- Otherwise → a **field**. Grep `FIELD-INDEX.json` first to find which schema owns it, then read the
  file that documents that schema.

With `--vendor gocity`, read `skills/octo-gocity/` and report the delta alongside the base answer.

## Search order

1. `grep` the relevant `FIELD-INDEX.json` to locate the owning schema or endpoint.
2. Read only the file that holds it — the `## Reference map` in each `SKILL.md` says which.
3. For protocol questions (headers, errors, capability discovery) read `skills/octo-protocol/`.

## Output

- **Endpoint**: method, path, every parameter with `in` / type / required, request body schema,
  response codes, then a `curl` example with a `<api-key>` placeholder and the mandatory
  `Octo-Capabilities` header.
- **Schema**: required fields first, then all fields with type and description, then which
  capabilities extend it.
- **Field**: owning schema, type, required, description, and the capability that gates it if any.
- **Capability**: the exact header value, the schemas it widens, the endpoints it unlocks.

Report only what the references contain. If a name is not in `FIELD-INDEX.json`, say it does not
exist in the specification rather than offering a similar-looking one. Never print a real
credential.
