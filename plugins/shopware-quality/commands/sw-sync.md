---
name: sw-sync
description: Prüft das Upstream-Repo shopware/shopware auf neue Versionen/Releases (GitHub releases/tags API) und Trunk-Drift und aktualisiert die sw-*-Skill-Bibliothek. --check = nur Report, --apply = Skills aktualisieren.
argument-hint: [--check|--apply]
allowed-tools: Read, Grep, Glob, Bash, Edit, Write, WebFetch, Task
model: sonnet
---

# /sw-sync

Synchronisiere die Skill-Bibliothek mit dem aktuellen Shopware-Stand. Delegiere an den Agent `shopware-librarian`
(Skill `sw-knowledge-sync`).

## Ablauf
1. State lesen (`plugins/shopware-quality/.sync-state.json`).
2. **Versionen**: `https://api.github.com/repos/shopware/shopware/tags` + `/releases` → neueste vs. gespeicherte Version.
3. **Trunk-Drift**: lokaler Trunk-Pull / GitHub-Compare seit `lastCommit`; `changelog/`, neue `adr/`.
4. Betroffene Skills mappen (Regeln aus `sw-knowledge-sync`).
5. Modus:
   - `--check` (Default): Report (aktuelle vs. neueste Version, Drift, betroffene Skills, Vorschläge) — keine Änderungen.
   - `--apply`: Skills aktualisieren/ergänzen/entfernen, `marketplace.json` + Plugin-Version + Changelog pflegen,
     `.sync-state.json` updaten; danach validieren.

Bei Unklarheit/großen BC-Brüchen stoppen und berichten. Nichts erfinden — gegen die Quelle prüfen.
