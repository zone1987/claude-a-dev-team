# zomboid

Source of truth for **Project Zomboid build 42.20.2** modding — extracted from the game itself, not
from recollection.

Project Zomboid's API is Java under the hood and Lua on the surface, grown over a decade without a
naming convention and largely undocumented. A plausible-looking method name is usually wrong, and
Lua calling a nonexistent Java method returns `nil` rather than raising — so the failure surfaces
frames away from the mistake. That is why everything here is a lookup rather than a memory.

## Coverage

| Source | Covered |
|---|---|
| Build 42 JavaDocs | **3,965 classes, 72,831 members**, 267 packages |
| Game Lua | **1,395 files, 439,296 lines** — 189 globals, 1,055 classes, 15,667 methods |
| ISUI widget library | **296 classes, 4,720 methods**, 87,624 lines |
| Script definitions | **15,138 blocks** in 28 types — 5,105 items, 969 recipes, 241 vehicles, 219 entities, 61 fluids |
| Tile definitions | **583 tilesets, 37,060 world objects**, 230 properties |
| XML data | **8,016 files** — clothing, action groups, animation sets, hair, voices, radio |
| Server | **67 admin commands, 144 INI options** |
| Events | **209 names**, 174 with a handler signature recovered from the game's own code |
| Mod format | **34 installed mods** surveyed, 16 `mod.info` keys with frequencies |

**Roughly 150,000 lines of reference**, and the large majority is generated rather than written:
15 scripts in `scripts/` turn the game's files into references with no model in the path. A model
asked to transcribe 72,831 member signatures paraphrases a type or drops an overload silently; a
script cannot.

```bash
python3 scripts/verify_references.py        # every reference reachable, every link resolves
python3 scripts/verify_orchestrator.py      # the orchestrator knows every skill and agent
python3 ../zone-claude-forge/scripts/validate_plugin.py --plugin zomboid --strict
```

`INVENTORY.json` records every source with a content hash, so "is this still current?" is a hash
comparison rather than a re-read.

## Skills

Twelve skills, **3,368 characters** of the listing budget — 42 %. The depth sits in reference files,
which cost nothing until read.

| Skill | Covers |
|---|---|
| `pz-modding` | Mod folder layout, `mod.info`, load order, Workshop packaging. **Start here** — a mod with the wrong layout does not load at all |
| `pz-lua-api` | The 1,395 game Lua files indexed, the injected globals, `ISBaseObject`, override patterns, Kahlua's differences from standard Lua |
| `pz-java-api` | All 3,965 Java classes reachable from Lua, every member signature, across 78 files |
| `pz-events` | Every event with its handler signature, and the negative catalogue: what has **no** event, and what to do instead |
| `pz-items` | Every script property with its legal values, all 5,105 items, the 239 runtime `Item` fields and which have setters |
| `pz-world` | Coordinates, cells, chunks, squares, buildings, basements, all 37,060 world objects, and finding a thing by position |
| `pz-server` | RCON, all 67 admin commands, 144 server options, sandbox vars, logs, adding your own command |
| `pz-multiplayer` | The client/server split, the command channel, permissions, and how state leaves the game process |
| `pz-ui` | All 296 ISUI classes with their derivation chains — building your own panels, context menus, map overlays |
| `pz-crafting` | `craftRecipe`, the build 42 entity/component system, fluids, evolved recipes |
| `pz-vehicles` | All 241 vehicles, parts, wheels, passengers, `BaseVehicle` |
| `pz-tooling` | Debug mode, `console.txt`, reading a stack trace, what reloads, running a local dedicated server |

## Agents

| Agent | For |
|---|---|
| `pz-dev` | **Orchestrator and entry point.** Routes to the right skills and specialists, decomposes a feature into its data/access/surface layers, and names the four questions that decide any Zomboid task |
| `pz-api-expert` | Looking up an exact class, signature, event argument or property. Read-only |
| `pz-mod-builder` | Writing and reviewing mod code, with the folder layout and side split right |
| `pz-server-dev` | Server work: commands, state queries, and bridges to external tools |

## Commands

| Command | For |
|---|---|
| `/pz-lookup <term>` | Print what the references say about a class, method, event, item, property or command — with the source file named |
| `/pz-mod-new <what it does>` | Scaffold a mod with the correct layout and the client/server split the feature needs |
| `/pz-server-tool <what it does>` | Build a server-side command, a state query, or a bridge |
| `/pz-savegame-fog <save folder>` | Read or fully reveal the per-player fog of war in a dedicated-server save (`--reveal` to write) |
| `/pz-server-ftp <what to do>` | Fetch logs or saves from a hosted server over FTP, or upload config to a stopped one |

## The four questions that decide a Zomboid task

The orchestrator asks these first, because each has a silent failure mode:

1. **Which side runs this?** `client/`, `server/` or `shared/`. Singleplayer loads both, so a side
   mistake works while testing alone and fails on a dedicated server.
2. **Is the data loaded?** The world exists in chunks around players. A square in an unloaded chunk is
   `nil`, not empty — so a whole-map query is usually a "wherever players are" query.
3. **Does an event exist?** Many things have none. `pz-events` carries the negative catalogue and the
   polling pattern that replaces a missing hook.
4. **Does it need to sync?** A client-side change the server does not know about is a desync.

## Reaching the game from outside

For a Discord bot, a control panel or a dashboard, one fact settles the architecture:
**Lua has no HTTP client and no socket API.** Verified against every global the engine exposes and
the whole of the game's own Lua. The game is never the caller.

What works instead: a mod appends structured lines with `getModFileWriter`, and a separate process
tails the file and speaks whatever protocol the outside world wants. Inbound, RCON drives anything
that maps to an admin command. `pz-multiplayer` and `pz-server` carry the detail.

## Source

Extracted from the local installation at
`~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java`
— build **42.20.2**, revision `ffe7a8a4b1` — cross-checked against
[the official JavaDocs](https://projectzomboid.com/modding/index.html) (generated 2026-08-19) and
[demiurgeQuantified/ProjectZomboidJavaDocs](https://github.com/demiurgeQuantified/ProjectZomboidJavaDocs)
commit `edcb2c482b`. Retrieved 2026-08-26.

Project Zomboid is developed by The Indie Stone, which owns the game and its documentation; the
unofficial JavaDoc build is by demiurgeQuantified. This distillation is licensed MIT as part of this
marketplace. Per-source hashes and the file-to-source mapping are in
[`INVENTORY.json`](INVENTORY.json).
