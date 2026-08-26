---
name: pz-java-api
description: "Project Zomboid Java API exposed to Lua: all 3,965 classes and 72,831 members. Use when the request names IsoPlayer, IsoGridSquare, ItemContainer or another zombie.* class."
---

# Project Zomboid Java API

Project Zomboid's engine is Java; mods are Lua. Almost everything a mod does is a call into a Java
class, so this is the reference behind every other skill in this plugin. It carries **all 3,965 types
and 72,831 members** of build 42, generated from the JavaDoc search indexes with no model in the
path — so a signature here is the signature, not a plausible reconstruction.

## Two rules before you open a file

**A Java method is called from Lua by its own name**, on an object the game handed you:
`square:getObjects()`, `player:getInventory()`. Static methods on `LuaManager.GlobalObject` are
different — they are injected as bare globals, so `getPlayer()` needs no qualifier. Call the Skill
tool with `pz-lua-api` for that boundary in detail.

**A name absent from these files is absent from the API.** Lua calling a nonexistent Java method
yields `nil` rather than an error, and the failure surfaces frames later as something unrelated. So
grep before you write:

```bash
grep -rn "getGridSquare" "${CLAUDE_PLUGIN_ROOT}/skills/pz-java-api/references"
```

If it is not there, report it as undocumented instead of guessing a spelling.

## File naming

One file per subsystem. A subsystem larger than ~2,500 lines is split, and the parts carry a numeric
suffix: `ZOMBIE-ISO-1.md` through `-4.md` are one subsystem, not four. Each file opens with its own
contents list, so a preview shows its scope.

## Reference map

<!-- reference-map:start -->

- **ZOMBIE-SCRIPTING** (7 parts: [1](references/ZOMBIE-SCRIPTING-1.md), [2](references/ZOMBIE-SCRIPTING-2.md), [3](references/ZOMBIE-SCRIPTING-3.md), [4](references/ZOMBIE-SCRIPTING-4.md), [5](references/ZOMBIE-SCRIPTING-5.md), [6](references/ZOMBIE-SCRIPTING-6.md), [7](references/ZOMBIE-SCRIPTING-7.md)): 300 types, 21,984 members — the script model — `Item`, `VehicleScript`, `Recipe`, `ScriptManager`: everything loaded from `media/scripts`.
- **ZOMBIE-CORE** (6 parts: [1](references/ZOMBIE-CORE-1.md), [2](references/ZOMBIE-CORE-2.md), [3](references/ZOMBIE-CORE-3.md), [4](references/ZOMBIE-CORE-4.md), [5](references/ZOMBIE-CORE-5.md), [6](references/ZOMBIE-CORE-6.md)): 596 types, 9,440 members — rendering, textures, input, profiling and the low-level primitives.
- **ZOMBIE-ISO** (5 parts: [1](references/ZOMBIE-ISO-1.md), [2](references/ZOMBIE-ISO-2.md), [3](references/ZOMBIE-ISO-3.md), [4](references/ZOMBIE-ISO-4.md), [5](references/ZOMBIE-ISO-5.md)): 454 types, 8,995 members — the world — `IsoGridSquare`, `IsoCell`, `IsoChunk`, `IsoObject`, `IsoWorld`, `BuildingDef`, `RoomDef`.
- **ZOMBIE-CHARACTERS** (4 parts: [1](references/ZOMBIE-CHARACTERS-1.md), [2](references/ZOMBIE-CHARACTERS-2.md), [3](references/ZOMBIE-CHARACTERS-3.md), [4](references/ZOMBIE-CHARACTERS-4.md)): 266 types, 6,501 members — `IsoPlayer`, `IsoZombie`, survivors, animals, body and stats.
- **ZOMBIE-NETWORK** (4 parts: [1](references/ZOMBIE-NETWORK-1.md), [2](references/ZOMBIE-NETWORK-2.md), [3](references/ZOMBIE-NETWORK-3.md), [4](references/ZOMBIE-NETWORK-4.md)): 504 types, 4,653 members — the client/server layer, every packet class, `GameServer`, `GameClient`.
- **ZOMBIE-ENTITY** (2 parts: [1](references/ZOMBIE-ENTITY-1.md), [2](references/ZOMBIE-ENTITY-2.md)): 220 types, 2,765 members — the build 42 entity and component system.
- **ZOMBIE-INVENTORY** (2 parts: [1](references/ZOMBIE-INVENTORY-1.md), [2](references/ZOMBIE-INVENTORY-2.md)): 52 types, 2,380 members — `InventoryItem` and its subclasses, `ItemContainer` — the runtime side of items.
- **[references/ZOMBIE-1.md](references/ZOMBIE-1.md)**: 94 types, 1,837 members — the root package — `GameWindow`, `SandboxOptions`, `GameTime`.
- **[references/ZOMBIE-VEHICLES.md](references/ZOMBIE-VEHICLES.md)**: 75 types, 1,508 members — `BaseVehicle`, parts and physics.
- **[references/ZOMBIE-UI.md](references/ZOMBIE-UI.md)**: 59 types, 1,336 members — the Java side of the UI layer.
- **[references/ZOMBIE-WORLDMAP.md](references/ZOMBIE-WORLDMAP.md)**: 120 types, 1,288 members — the in-game map, its markers and overlays.
- **[references/ZOMBIE-AI.md](references/ZOMBIE-AI.md)**: 111 types, 958 members — states, behaviours and the AI director.
- **[references/ZOMBIE-LUA.md](references/ZOMBIE-LUA.md)**: 14 types, 937 members — the Lua bridge — `LuaManager`, `LuaEventManager`, `LuaHookManager`, the Kahlua converters.
- **[references/ZOMBIE-DEBUG.md](references/ZOMBIE-DEBUG.md)**: 102 types, 908 members — the debug facilities.
- **[references/ZOMBIE-UTIL.md](references/ZOMBIE-UTIL.md)**: 162 types, 849 members — helpers and collections.
- **[references/ZOMBIE-RANDOMIZEDWORLD.md](references/ZOMBIE-RANDOMIZEDWORLD.md)**: 153 types, 837 members — randomized buildings, vehicle stories and zone stories.
- **[references/ZOMBIE-AUDIO.md](references/ZOMBIE-AUDIO.md)**: 138 types, 775 members — sound and the FMOD bridge.
- **[references/ZOMBIE-PATHFIND.md](references/ZOMBIE-PATHFIND.md)**: 49 types, 543 members — pathfinding.
- **[references/ZOMBIE-RADIO.md](references/ZOMBIE-RADIO.md)**: 31 types, 488 members — radio and television broadcasts.
- **[references/ZOMBIE-GAMESTATES.md](references/ZOMBIE-GAMESTATES.md)**: 35 types, 417 members — the `zombie.gamestates` package.
- **[references/ZOMBIE-INPUT.md](references/ZOMBIE-INPUT.md)**: 20 types, 352 members — the `zombie.input` package.
- **[references/ZOMBIE-CHAT.md](references/ZOMBIE-CHAT.md)**: 24 types, 292 members — chat, its streams and its commands.
- **[references/ZOMBIE-EROSION.md](references/ZOMBIE-EROSION.md)**: 32 types, 292 members — the erosion system.
- **[references/ZOMBIE-TILEDEPTH.md](references/ZOMBIE-TILEDEPTH.md)**: 27 types, 267 members — the `zombie.tiledepth` package.
- **[references/ZOMBIE-POPMAN.md](references/ZOMBIE-POPMAN.md)**: 25 types, 239 members — zombie population management.
- **[references/ZOMBIE-WORLD.md](references/ZOMBIE-WORLD.md)**: 35 types, 199 members — world-level services.
- **[references/ZOMBIE-COMBAT.md](references/ZOMBIE-COMBAT.md)**: 9 types, 131 members — the `zombie.combat` package.
- **[references/ZOMBIE-VEHICLESOUND.md](references/ZOMBIE-VEHICLESOUND.md)**: 12 types, 123 members — the `zombie.vehiclesound` package.
- **[references/ZOMBIE-COMMANDS.md](references/ZOMBIE-COMMANDS.md)**: 76 types, 121 members — every admin and server command class.
- **[references/ZOMBIE-CHARACTERTEXTURES.md](references/ZOMBIE-CHARACTERTEXTURES.md)**: 4 types, 116 members — the `zombie.charactertextures` package.
- **[references/ZOMBIE-FILESYSTEM.md](references/ZOMBIE-FILESYSTEM.md)**: 16 types, 114 members — the `zombie.filesystem` package.
- **[references/ZOMBIE-CONFIG.md](references/ZOMBIE-CONFIG.md)**: 9 types, 112 members — the `zombie.config` package.
- **[references/ZOMBIE-GLOBALOBJECTS.md](references/ZOMBIE-GLOBALOBJECTS.md)**: 11 types, 106 members — the global object system.
- **[references/ZOMBIE-SAVEFILE.md](references/ZOMBIE-SAVEFILE.md)**: 8 types, 94 members — the save format.
- **[references/ZOMBIE-ASSET.md](references/ZOMBIE-ASSET.md)**: 18 types, 79 members — the `zombie.asset` package.
- **[references/ZOMBIE-SPNETWORK.md](references/ZOMBIE-SPNETWORK.md)**: 7 types, 78 members — the `zombie.spnetwork` package.
- **[references/ZOMBIE-VEHICLENETWORKSOUND.md](references/ZOMBIE-VEHICLENETWORKSOUND.md)**: 7 types, 71 members — the `zombie.vehiclenetworksound` package.
- **[references/ZOMBIE-STATISTICS.md](references/ZOMBIE-STATISTICS.md)**: 7 types, 69 members — the `zombie.statistics` package.
- **[references/ZOMBIE-GIZMO.md](references/ZOMBIE-GIZMO.md)**: 13 types, 66 members — the `zombie.gizmo` package.
- **[references/ZOMBIE-BUILDINGROOMS.md](references/ZOMBIE-BUILDINGROOMS.md)**: 6 types, 64 members — the `zombie.buildingrooms` package.
- **[references/ZOMBIE-SEATING.md](references/ZOMBIE-SEATING.md)**: 3 types, 59 members — the `zombie.seating` package.
- **[references/ZOMBIE-POT.md](references/ZOMBIE-POT.md)**: 5 types, 54 members — the `zombie.pot` package.
- **[references/ZOMBIE-TEXT.md](references/ZOMBIE-TEXT.md)**: 10 types, 48 members — the `zombie.text` package.
- **[references/ZOMBIE-BASEMENTS.md](references/ZOMBIE-BASEMENTS.md)**: 7 types, 47 members — build 42 basements.
- **[references/ZOMBIE-SEAMS.md](references/ZOMBIE-SEAMS.md)**: 5 types, 46 members — the `zombie.seams` package.
- **[references/ZOMBIE-INTERFACES.md](references/ZOMBIE-INTERFACES.md)**: 6 types, 42 members — the `zombie.interfaces` package.
- **[references/ZOMBIE-PROFANITY.md](references/ZOMBIE-PROFANITY.md)**: 6 types, 42 members — the `zombie.profanity` package.
- **[references/ZOMBIE-MODDING.md](references/ZOMBIE-MODDING.md)**: 3 types, 24 members — the mod loader.
- **[references/ZOMBIE-SANDBOX.md](references/ZOMBIE-SANDBOX.md)**: 7 types, 19 members — sandbox options.
- **[references/ZOMBIE-SPRITEMODEL.md](references/ZOMBIE-SPRITEMODEL.md)**: 2 types, 18 members — the `zombie.spritemodel` package.
- **[references/ZOMBIE-VIEWCONE.md](references/ZOMBIE-VIEWCONE.md)**: 3 types, 16 members — the `zombie.viewcone` package.
- **[references/ZOMBIE-VISPOLY.md](references/ZOMBIE-VISPOLY.md)**: 4 types, 13 members — the `zombie.vispoly` package.
- **[references/ZOMBIE-CREATIVE.md](references/ZOMBIE-CREATIVE.md)**: 1 types, 7 members — the `zombie.creative` package.
- **[references/ZOMBIE-FIREFIGHTING.md](references/ZOMBIE-FIREFIGHTING.md)**: 1 types, 7 members — the `zombie.firefighting` package.
- **[references/ZOMBIE-META.md](references/ZOMBIE-META.md)**: 1 types, 5 members — the `zombie.meta` package.

78 files in total; `ls references/` lists them.

<!-- reference-map:end -->
## Related

Call the Skill tool with "pz-lua-api" for how Lua reaches these classes, "pz-events" for the event
arguments they carry, "pz-world" for the world model these classes implement, and "pz-items" for the
item side.

## Source

Generated by `scripts/build_java_api.py` from the JavaDoc search indexes of
[demiurgeQuantified/ProjectZomboidJavaDocs](https://github.com/demiurgeQuantified/ProjectZomboidJavaDocs),
branch `develop`, commit `edcb2c482b`, retrieved 2026-08-26. The upstream is an unofficial JavaDoc
build of Project Zomboid build 42; the official index is at
[projectzomboid.com/modding](https://projectzomboid.com/modding/index.html).
