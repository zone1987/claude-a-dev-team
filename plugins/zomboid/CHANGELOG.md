# Changelog

All notable changes to the `zomboid` plugin.

## 1.2.0 — 2026-09-02

### Added

- **`ITEM-ICONS.md`** in `pz-items/references/`: where the item icons actually are. The game ships
  about a hundred loose in `media/ui/` and packs the other ~4,400 into sprite atlases under
  `media/texturepacks/`, so anything that displays a real icon outside the game has to unpack them.
  Documents both pack layouts (legacy and PZPK), the exact read procedure field by field, a verified
  byte trace of `UI.pack` so a new reader can be checked offset by offset, and the three traps that
  make a hand-written reader return ~60 sprites instead of 4,400: everything is little-endian (a
  big-endian misread only surfaces at the *next* field), a reserved word follows the sprite count,
  and pages are separated by `0xDEADBEEF`. Also records that an icon name cannot be derived from the
  item id — `Base.Disinfectant` is `Item_Alcohol`, `Base.Saw` is `Item_Handsaw` — so the `Icon`
  property has to be read, never constructed.

- **`scripts/extract_item_icons.py`**: extracts them. `--list` to see what is there (no
  dependencies), `--only` for a subset, `--webp` to keep 4,363 icons at 18 MB. Measured on build
  42.20.2: 4,475 `Item_*` sprites across 15 atlas pages in 5 packs, 4,363 distinct names.

### Changed

- `pz-dev.md` routes icon questions to `ITEM-ICONS.md` and gains an **assets are not text** note:
  icons, tiles and models live in packed atlases, so a task that needs to *show* something from the
  game needs extraction, not a lookup. The local-sources listing now names `media/texturepacks/`
  and `media/ui/`.
- `pz-items` describes the icon reference in its map, and its description mentions icon extraction.
- `INVENTORY.json` records the icon packs as a source part with their hash and sprite counts, and
  `extract_item_icons.py` as a generator — flagged as producing assets rather than a reference
  table, since its output must stay out of the repository.

## 1.1.0 — 2026-08-27

### Added

- **`SAVEGAME-FORMAT.md`** in `pz-server/references/`: the on-disk save format. Every file and folder
  with the class that writes it, the `map/<X>/<Y>.bin` chunk addressing (`CHUNK_DIM = 8`), the
  `map_visited_server/<user>.zip` fog-of-war bit layout, corpse-removal semantics
  (`IsoDeadBody.updateBodies()` runs every tick, not only on chunk load), and the cost drivers behind
  slow starts and backups. Written from CFR-decompiled bytecode and cross-checked byte-for-byte
  against a live save; unverified gaps are marked rather than filled.
- **`/pz-savegame-fog`**: reads the revealed share per player, and with `--reveal` writes a fully
  explored bitmap. Documents why `Map.MapAllKnown`, RCON and deleting the file all fail to do this.

- **`scripts/pz_ftp.sh` and `/pz-server-ftp`**: read and write a hosted server's filesystem over
  plain FTP — `check`, `ls`, `get`, `put` (re-downloads and compares byte-for-byte before reporting
  success), `tail` for the end of a large log, `logs` for `server-console.txt` plus all `Logs/*.txt`.
  Credentials come from `PZ_FTP_*` (falling back to `FTP_*`) and are handed to curl via `--config`,
  never as arguments, so they stay out of `ps` and shell history; no value is ever printed.

### Fixed

- Recorded two traps that cost real debugging time: `id_manager_data.bin` counters (`ObjectID
  type=DeadBody last=…`) are monotonic ID allocations, **not** live object counts — a `Vehicle`
  counter of 9,100 against 3,083 rows in `vehicles.db` proves it; and `ZombieThumpGeneric` in a chunk
  binary is a furniture sound attribute, not a corpse marker.

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
