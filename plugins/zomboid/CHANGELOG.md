# Changelog

All notable changes to the `zomboid` plugin.

## 1.0.0 — 2026-08-26

First release. Project Zomboid build **42.20.2** (revision `ffe7a8a4b1`) modding, extracted from the
game itself.

### Added

- **Twelve skills**: `pz-modding`, `pz-lua-api`, `pz-java-api`, `pz-events`, `pz-items`, `pz-world`,
  `pz-server`, `pz-multiplayer`, `pz-ui`, `pz-crafting`, `pz-vehicles`, `pz-tooling`.
- **Four agents**: `pz-dev` (orchestrator and entry point), `pz-api-expert` (lookup, read-only),
  `pz-mod-builder` (implementation), `pz-server-dev` (server, RCON and bridges).
- **Three commands**: `/pz-lookup`, `/pz-mod-new`, `/pz-server-tool`.
- **15 generator and verification scripts.** Every large reference is generated from the game's own
  files with no model in the path, so a signature or a property list cannot be a paraphrase.

### Extracted

| Source | Covered |
|---|---|
| Build 42 JavaDocs | 3,965 classes, 72,831 members, 267 packages |
| Game Lua | 1,395 files, 439,296 lines, 189 globals, 1,055 classes, 15,667 methods |
| ISUI widget library | 296 classes, 4,720 methods, 87,624 lines |
| Script definitions | 15,138 blocks in 28 types — 5,105 items, 969 recipes, 241 vehicles, 219 entities |
| Tile definitions | 583 tilesets, 37,060 world objects, 230 properties |
| XML data | 8,016 files — clothing, action groups, animation sets, hair, voices, radio |
| Server | 67 admin commands, 144 INI options |
| Events | 209 names, 174 with a handler signature |
| Mod format | 34 installed mods surveyed, 16 `mod.info` keys |

### Verified at release

- Forge validator `--strict`: **clean** — 0 errors, 0 warnings.
- Every reference file reachable from its `SKILL.md`; every relative link resolves.
- `scripts/verify_orchestrator.py` proves the orchestrator names every skill and every agent with a
  stated purpose — an omitted skill would otherwise never be routed to.
- Listing cost 3,368 characters, 42.1 % of budget.

### Corrections made during extraction

Recorded because each was a plausible claim the sources disproved:

- The item count is **5,105**, not the 10,123 an initial grep suggested — that figure counted recipe
  ingredient lines as item definitions.
- Build 42's versioned mod layout (`common/` plus `42/`) is **optional**. Most surveyed mods declaring
  `versionMin=42.x` ship `media/` alone and load; the versioned form serves mods spanning two builds.
- **Lua has no HTTP client and no socket API.** Verified against every exposed global and the whole of
  the game's Lua. The only outbound path is `getFileWriter` / `getModFileWriter`.
- **The helicopter has no Lua event.** It is `zombie.iso.Helicopter` plus `ChopperCommand`, so a hook
  requires polling.

### Source

The local game installation at
`~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java`,
build 42.20.2, cross-checked against
[the official JavaDocs](https://projectzomboid.com/modding/index.html) and
[demiurgeQuantified/ProjectZomboidJavaDocs](https://github.com/demiurgeQuantified/ProjectZomboidJavaDocs)
commit `edcb2c482b`. Per-source hashes are in [`INVENTORY.json`](INVENTORY.json).
