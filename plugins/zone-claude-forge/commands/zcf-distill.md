---
name: zcf-distill
description: Enumerates an upstream source, plans its extraction into reference files and reports coverage against the inventory.
argument-hint: <url|path> --plugin <name> [--apply]
allowed-tools: Read, Glob, Grep, Bash, Write
model: sonnet
---

# /zcf-distill

Turn the source named in $ARGUMENTS into reference files for the given plugin. Without `--apply` this
plans and reports only; nothing is written.

## Steps

1. Call the Skill tool with "zcf-source-distillation" for the method.
2. **Enumerate**, and report the count before extracting anything: a sitemap for a docs site
   (`/sitemap.xml`, then `/sitemap-pages.xml`, `/sitemap_index.xml`), the document itself for OpenAPI
   or JSON Schema, a tree at a pinned sha for a repository. GitHub and GitLab serve no sitemap.
3. **Mirror** the source locally and record its hash, so the audit is reproducible and offline.
4. **Plan** the split into skills and reference files, and show it for approval. State which files a
   script will generate and which need writing by hand.
5. With `--apply`, dispatch `claude-source-distiller`: the extraction spans more pages than this
   conversation should read, and its own context window is the point.
6. **Audit** both directions:

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/audit_coverage.py" --plugin <name> --sitemap <url>
   ```

## Output

The inventory count, the planned or written files, and the audit verdict as counts:
`n/m units mapped`, plus every `UNCOVERED`, `DANGLING` and `STALE` line.

Report only what the source and the files contain. Where the upstream is silent on a facet, say so.
Invent nothing.
