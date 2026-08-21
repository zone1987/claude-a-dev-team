# Enumerating a source

The inventory is the denominator. Without it, "we covered everything" is a claim nobody can check,
and a page added upstream next month goes unnoticed. Rules: `SOURCE-01`, `COV-01`, `COV-05`, `COV-09`, `COV-10`.

## Contents

- [Prefer the original](#prefer-the-original)
- [Docs site](#docs-site)
- [OpenAPI or JSON Schema](#openapi-or-json-schema)
- [GitHub or GitLab](#github-or-gitlab)
- [Typed export or CLI](#typed-export-or-cli)
- [Mirror it](#mirror-it)
- [Write the map](#write-the-map)
- [Record it in INVENTORY.json](#record-it-in-inventory.json)
- [Source](#source)

## Prefer the original

The upstream documentation or a pinned commit, never a third-party write-up. A secondary source dates
silently and cannot be re-checked against the thing it describes. This is not theoretical: the
catalogue behind this plugin needed five factual corrections, each found by reading the primary page
after working from a distilled copy of it. `SRC-05`

## Docs site

Try the sitemap in this order, and stop at the first that lists **pages** rather than sections:

1. `/sitemap.xml`
2. `/sitemap-pages.xml` — GitBook splits by content type, so this is often the real page list
3. `/sitemap_index.xml` — an index of sitemaps; follow each `<loc>`
4. `/sitemap-0.xml`, `/sitemap1.xml` — numbered shards
5. `robots.txt` — names the sitemap when the path is unusual

```bash
curl -sS https://docs.example.com/sitemap.xml \
  | python3 -c "import re,sys; print('\n'.join(re.findall(r'<loc>([^<]+)</loc>', sys.stdin.read())))"
```

**Read the markdown twin where one exists.** Many documentation platforms serve the source markdown
at the same path plus `.md`. It is a fraction of the bytes of rendered HTML and needs no tag
stripping, which removes a whole class of extraction bug.

## OpenAPI or JSON Schema

The document **is** the inventory: paths, operations, schemas, enums, and their counts. Resolve it to
a local file first and record its hash, because a spec served from a content-addressed URL changes
location without changing content, and the reverse also happens.

Count everything before extracting, and keep the counts: they are the completion criterion.

```bash
python3 -c "
import json,yaml,sys
s=yaml.safe_load(open(sys.argv[1]))
print('paths', len(s.get('paths',{})))
print('operations', sum(1 for p in s['paths'].values() for m in p if m in
      ('get','post','put','patch','delete')))
print('schemas', len(s.get('components',{}).get('schemas',{})))" openapi.yaml
```

## GitHub or GitLab

**No `sitemap.xml` exists.** Neither host serves one for a repository, so enumerate differently:

- List the tree at a **pinned ref**: `git ls-tree -r --name-only <sha>`, or the API's tree endpoint.
- Narrow to what the plugin claims: `docs/`, `src/`, the ADR directory.
- **The commit sha is the version**, and it takes the place of a retrieval date, because it is exact
  where a date is approximate.

## Typed export or CLI

Prefer the environment over a document restating it: type declarations, `--help` output, a config
schema. These cannot go stale relative to the tool, which is the property a copied doc loses.

## Mirror it

The audit reads a **local mirror**, not the live site, so a verdict is reproducible and the check does
not depend on the network. Record the mirror's hash in the state file. `COV-05`

```bash
mkdir -p /tmp/mirror
for u in $(cat pages.txt); do
  slug=$(printf '%s' "${u#https://}" | sed 's/[^a-zA-Z0-9]\+/-/g')
  curl -sS "${u%/}.md" -o "/tmp/mirror/$slug.md" || curl -sS "$u" -o "/tmp/mirror/$slug.html"
done
```

A re-run that gives a different verdict with no change to the plugin means the audit is reading the
live site. That is the tell.

## Write the map

`--write` emits a `DOCUMENTATION-MAP.md` pairing each source unit with the file covering it. That
table is the artefact a reviewer checks, and the thing that makes a later gap obvious.

## Record it in INVENTORY.json

The map says which file covers which page. The inventory says **when**, and against **what**:

```bash
python3 scripts/inventory.py --plugin <name> --write --pages <mirror>
```

Per page it stores the URL, the content hash, the covering files, the term count and the extraction
date. `COV-09` One line of it:

```json
{ "page": "https://docs.ventrata.com/getting-started/headers",
  "sha256": "445c442d…", "covers": ["skills/octo-protocol/references/HEADERS.md"],
  "terms": 20, "extracted": "2026-08-21" }
```

**Why the hash and not just the date.** The next audit reads this file before fetching anything and
compares each hash against the live page. `COV-10` Pages that match need no work, whatever the date
says; only changed, new or missing pages are re-extracted. On `plugins/octo-api` that settled 39
pages and 1,163 terms in 6.5 seconds, with no page content entering context — against mirroring
304 KB before any decision could be made. Age decides only when the source is unreachable, where a
record over 30 days old counts as unproven.

Write the inventory in the same run as the audit. Written later, from memory of what was covered, it
records a belief rather than a measurement.

## Source

Method generalised from `plugins/octo-api/scripts/check_sitemap.py` and `audit_pages.py` in this
marketplace, read 2026-08-21, which enumerate `docs.ventrata.com/sitemap-pages.xml` and mirror each
page before auditing it.
