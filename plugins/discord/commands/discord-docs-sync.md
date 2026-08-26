---
name: discord-docs-sync
description: Check the Discord documentation for drift against this plugin and report which pages were added, removed or changed.
argument-hint: [--check|--apply]
allowed-tools: Read, Glob, Grep, Bash, Write, Edit
model: sonnet
---

# /discord-docs-sync

Check whether docs.discord.com still matches what this plugin carries. Default to `--check`, which
reports and changes nothing. `--apply` in $ARGUMENTS additionally re-distils the pages that moved.

## Check

1. **Verify the plugin's internal integrity first**, since a drift report is meaningless on a plugin
   that is already broken:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/verify_references.py"
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/verify_page_coverage.py"
   ```
2. **Compare the sitemap against the recorded hash:**
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/verify_page_coverage.py" --refresh-sitemap
   ```
   Use `curl -sSfL` for every fetch. It carries the system trust store and follows redirects, which
   this host requires; other clients report a reachable page as missing.
3. **Diff the page list.** Fetch `https://docs.discord.com/sitemap.xml`, extract every `<loc>`, and
   compare against the `pages` map in `PAGE-COVERAGE.json`:
   - a URL in the sitemap that no skill claims is an **added page**,
   - a claimed path absent from the sitemap is a **removed page**,
   - a `lastmod` newer than the manifest's `retrieved` date is a **changed page**.
4. **Report** each finding with its URL, which skill would own it, and which reference file it
   affects. Report counts, never a guess at what changed inside a page.

## Apply

Only when `--apply` is given, and only for the pages the check named:

1. **Mirror the changed pages** as markdown twins — every page has one at its URL plus `.md`:
   ```bash
   curl -sSfL "https://docs.discord.com/developers/<path>.md" -o <mirror>/<slug>.md
   ```
2. **Re-distil into the owning skill's reference file**, preserving the file's structure: every
   field with its type and optionality, every enum value, every endpoint, every limit. A refresh
   that condenses is a regression — the plugin is complete by design.
3. **Assign an added page** to the skill whose domain it belongs to, add it to `PAGE-COVERAGE.json`,
   and link its reference file from that skill's `SKILL.md`. An unlinked file is unreachable.
4. **Update** the manifest's `sitemap_sha256` and `retrieved` date, and the `## Source` section of
   every skill whose files changed.
5. **Re-run both verify scripts plus the marketplace gate**, and report the result:
   ```bash
   python3 ../zone-claude-forge/scripts/validate_plugin.py --plugin discord --strict
   ```

Report what changed and what you re-read. Never report a page as unchanged without having compared
it, and never delete documented content to resolve a conflict.
