# The coverage audit

Two directions, three failure states, and one list that has to carry reasons. Rules: `COV-01` to
`COV-05`.

## The two directions

**Forward**: every enumerated source unit maps to a plugin file. This is what makes a later gap
visible: a page added upstream next month surfaces as `UNCOVERED` instead of going unnoticed.

**Reverse**: every identifier the plugin documents exists in the source. **This is the direction that
catches invention.** A plausible field name added by hand fails here and nowhere else, which is why an
audit with only a forward check is worth much less than half of one.

## Three failure states

| State | Meaning | Usual cause |
|---|---|---|
| `UNCOVERED` | a source unit maps to nothing | the source grew, or extraction stopped early |
| `DANGLING` | a mapping points at a file that does not exist | a rename that did not update the map |
| `STALE` | a mapping survives the unit it covered | the upstream removed or moved a page |

All three are errors. `STALE` is the one people are tempted to ignore, and it is the one that makes a
map lie: it reports coverage of something that no longer exists.

## Term level, not page level

A page counted as covered can still be half-read, so the check goes down to the terms a reader would
look up: backticked identifiers, camelCase fields, `SCREAMING_CASE` values, and table rows. Each must
appear somewhere in the plugin, or be excluded with a reason. `COV-03`

```bash
python3 scripts/audit_coverage.py --plugin <name> --sitemap <url> --pages /tmp/mirror
python3 scripts/audit_coverage.py --plugin <name> --spec openapi.yaml
python3 scripts/audit_coverage.py --plugin <name> --repo <sha>
```

## The exclusion list carries reasons

Not every term on a page belongs in the plugin: asset handles inside image URLs, a vendor's internal
build identifier, a word that merely looks like an identifier. Those go on an explicit exclusion
list, **each with the reason it is excluded**.

An explicit list beats a clever pattern, because every exclusion is then a decision someone can
review. A regex that quietly drops a class of term is indistinguishable from a bug, and it fails
silently in the direction of looking complete.

## Read a mirror

The audit reads a local mirror whose hash is recorded, not the live site, so the verdict is
reproducible months later and the check does not depend on the network. **The tell that this went
wrong**: a re-run gives a different verdict with no change to the plugin. `COV-05`

## The bar is every page

For a plugin that claims a product's developer documentation, the target is **not a percentage**. It
is every page in the sitemap, and every term on every page. `COV-06`

The reason is asymmetric: coverage buys a reader the confidence not to check upstream, and one
missing page destroys that confidence for the whole plugin. Ninety-five per cent coverage still sends
the reader to the site, and once there they stay. `contao` documents 376 of 376 pages for exactly
this reason.

Two pages in that set are thin upstream rather than here, and the reference files say so: one carries
only a package name and a pointer to the vendor's own docs, the other is marked internal by a leading
underscore in its URL. **Documenting a page as thin is coverage; skipping it is not.**

## Counts, not adjectives

Report `39/39 pages mapped`, not "coverage is good". A count is checkable and exhaustive at once, and
it makes the next run's regression obvious.

## Calibrate against a known-good plugin

`octo-api` already passes its own two-direction proof, so a generalised audit must reproduce that
verdict. A disagreement means the generalisation lost something, not that the reference plugin is
wrong.

```bash
cd plugins/octo-api && python3 scripts/check_sitemap.py        # the baseline
python3 ../zone-claude-forge/scripts/audit_coverage.py --plugin octo-api --sitemap <url>
```

## Source

Generalised from `plugins/octo-api/scripts/check_sitemap.py` (forward, with `UNCOVERED`, `DANGLING`
and `STALE`) and `audit_pages.py` (reverse, term level, with a reasoned `EXCLUDED` map) in this
marketplace, read 2026-08-21.
