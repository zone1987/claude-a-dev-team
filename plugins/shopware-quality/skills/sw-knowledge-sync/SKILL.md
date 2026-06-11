---
name: sw-knowledge-sync
description: >
  Selbst-Aktualisierung der Shopware-Skill-Bibliothek gegen das Upstream-Repo: neue Versionen/Releases (GitHub
  releases/tags API) + Trunk-Drift (Commits/Changelog/ADRs) erkennen, betroffene Skills anpassen/ergänzen/entfernen,
  State pflegen. Trigger: "Knowledge Sync", "Bibliothek aktualisieren", "neue Shopware Version prüfen", "/sw-sync",
  "Skills gegen Upstream abgleichen", "shopware update check plugin". Meta-Skill.
---

# Shopware-Library — Knowledge-Sync (Selbst-Update)

Hält die `sw-*`-Skills aktuell gegen `shopware/shopware`. Ausführung über den Agent `shopware-librarian` (`/sw-sync`).

## Quellen
- **Releases/Tags** (neue Versionen): `https://api.github.com/repos/shopware/shopware/releases`
  und `https://api.github.com/repos/shopware/shopware/tags` → neueste Version vs. gespeicherter Stand.
- **Trunk-Drift**: GitHub-Compare-API bzw. lokaler Trunk-Pull; zusätzlich `changelog/`, `CHANGELOG.md`,
  `UPGRADE-*`, `RELEASE_INFO-*`, neue/geänderte `adr/`.

## State-Datei (`plugins/shopware-quality/.sync-state.json`)
```json
{ "lastCommit": "<sha>", "lastRelease": "v6.7.x.x", "lastChecked": "<ISO-Datum>" }
```

## Mapping Source → Skill (Beispiele)
`src/Core/Framework/DataAbstractionLayer/**` → shopware-data · `src/Storefront/**` → shopware-storefront ·
`src/Administration/**` → shopware-admin · `src/Core/Checkout/**` → shopware-checkout · `adr/*` → sw-adr-knowledge ·
neue Major → neues `shopware-migration`-Skill.

## Driftkriterien
neue/entfernte Klassen/Methoden, geänderte Signaturen, neue ADRs, deprecations, neue Major/Minor. Bei Unklarheit:
Bericht, kein Auto-Apply.

→ Mechanik/Modi: Command `/sw-sync` (`--check` Report / `--apply`); Agent `shopware-librarian`.
