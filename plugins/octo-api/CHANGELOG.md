# Changelog

## 2.1.0 — 2026-08-20

Completeness pass: all 39 documentation pages read in full, not just the OpenAPI document.

### Added

- **Every page of the documentation is now covered**, verified by `scripts/audit_pages.py`
  (1,162 of 1,162 terms) and mapped in `skills/octo-protocol/DOCUMENTATION-MAP.md`.
- **`ENUMERATED-VALUES.md`** — every value a value-like field can carry, split into *declared*
  (the specification lists an `enum`, so the set is closed) and *observed* (a plain string with an
  example, so the set is open). 43 declared plus 32 observed fields, each value with its meaning.
- **`CAPABILITY-ERRORS.md`** — the 21 error codes the capability pages document in prose only,
  each with the condition that triggers it.
- **`AUTHENTICATION.md`, `TESTING.md`, `GLOSSARY.md`, `INTEGRATION-STEPS.md`** — the four
  getting-started pages that had no home before.
- **`AFTER-CONFIRMATION.md`, `LISTING-BOOKINGS.md`** — which fields to read after a confirm, and the
  mandatory primary filter on `GET /bookings`.
- **`REMAINING-SCHEMAS-1/2.md`** — the request wrappers, list envelopes and action results the
  domain skills do not lay out, so all 139 schemas are rendered somewhere.
- **Integration notes on 22 capability files** — the routes each capability extends, the payload
  paths its fields appear at, the conditional rules, and the documentation's own callouts.
- **`scripts/extract_enums.py`, `extract_remaining.py`, `extract_cap_errors.py`,
  `extract_cap_prose.py`, `extract_gocity.py`, `audit_pages.py`, `check_sitemap.py`.**

### Fixed

- **Same-named enums were merged.** `status` is a different value set on `Booking` than on
  `Availability`; the old output listed all fifteen values together, which would have sent
  `status=SOLD_OUT` to `GET /bookings`. Each set is now separate and cross-references the other.
- **Fields lost their value set** when the specification declared the enum on one schema and a bare
  string on another (`BookingUnitItem.status`, the `GET /bookings` filter). An enum registry now
  attaches the set wherever the example makes the match unambiguous, and names where it came from.
- **Examples were suppressed on enum fields.** A field now shows both its allowed values and a
  typical one.
- **Optionality was implicit.** Every rendered field states `required` or `optional` outright.
- **Array examples read as scalars.** `deliveryMethods` now shows `["VOUCHER", "TICKET"]`, so a
  client author can tell an array from a string.
- **Capability schemas sat in the catch-all file.** The eight `CardPayment*` schemas — 50 fields —
  now live in `CARD-PAYMENTS.md` beside the capability they belong to.
- **Coverage checks passed on false evidence.** A schema counted as documented when its field names
  appeared anywhere; `CheckInLookupRequest` was "covered" while its own definition was missing. The
  check now compares field sets per schema heading.

## 2.0.0 — 2026-08-20

Complete rewrite. **Breaking:** every skill ID changed.

### Why

The previous layout had 38 skills costing 14,523 characters of the skill listing budget — 182 % of
the 8,000 available at a 200k context. Claude Code truncates descriptions on overflow, starting with
the least-used skills, so the rarely needed OCTO skills silently stopped auto-activating. On top of
that, all reference material sat two directory levels deep in `references/deep/`, where files are
only partially read: most of the 11,855 lines were unreachable.

### Changed

- **38 skills → 8**, grouped by domain. Listing cost 14,523 → 2,376 characters (182 % → 30 %).
- **References are flat siblings** beside `SKILL.md`, one level deep, with a table of contents in
  any file over 100 lines.
- **Facts are generated, not written.** `scripts/extract_spec.py` and `scripts/extract_caps.py`
  render endpoints, parameters, schemas, enums and capability attribution from the Ventrata
  OpenAPI document. `scripts/verify_spec.py` checks both directions: every specified field is
  documented, and every documented field exists in the specification.
- **All 65 operations, 139 schemas and 254 capability fields are covered** and verified.
- **English throughout.** The previous skills were German.
- **`license` MIT** (was `proprietary`, contradictory in a public repository); author reduced to a
  GitHub handle.

### Added

- `octo-protocol` — auth, the mandatory `Octo-Capabilities` header, all 10 error codes, capability
  discovery, localization.
- `/octo-spec-sync` — drift detection against the upstream specification, `--check` or `--apply`.
- `hooks/octo-anchor.py` — a `UserPromptSubmit` hook that matches brand anchors only (`octo`,
  `ventrata`, `go city`, `Octo-Capabilities`, `availabilityId`) and deliberately ignores generic
  commerce vocabulary such as `product`, `booking` or `pricing`.
- `.spec-state.json` — source URL, content hash and entity counts for drift detection.
- `scripts/resolve_blob.py` — resolves the content-addressed specification URL, which changes on
  every upstream publish.

### Removed

- `agents/octo-api-expert.md`, replaced by `agents/octo-integrator.md` (fewer preloaded skills, no
  write access).
- The 8 Go City skills, condensed into one `octo-gocity` delta overlay.
- `references/deep/` throughout.

### Skill mapping

| Old | New |
|---|---|
| `octo-overview`, `octo-endpoints`, `octo-headers`, `octo-errors`, `octo-localization` | `octo-protocol` |
| `octo-products` | `octo-products` |
| `octo-availability` | `octo-availability` |
| `octo-bookings` | `octo-bookings` |
| `octo-pricing`, `octo-offers`, `octo-cart`, `octo-packages`, `octo-card-payments`, `octo-gift-vouchers`, `octo-adjustments` | `octo-capabilities-commerce` |
| `octo-redemption`, `octo-extras`, `octo-pickups`, `octo-rentals`, `octo-resources`, `octo-waivers`, `octo-questions`, `octo-online-check-in` | `octo-capabilities-fulfilment` |
| `octo-webhooks`, `octo-notifications`, `octo-content`, `octo-mappings`, `octo-memberships`, `octo-campaigns`, `octo-waitlists`, `octo-identities` | `octo-capabilities-platform` |
| `octo-gocity-*` (5), `octo-ventrata-vs-gocity` | `octo-gocity` |
| `octo-clients-implementations` | moved to `README.md` |

## 1.0.0

Initial release — 38 skills, German, hand-written references.
