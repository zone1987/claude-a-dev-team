---
name: pz-savegame-fog
description: Read or fully reveal the per-player fog of war in a Project Zomboid dedicated-server save by editing map_visited_server/<user>.zip.
argument-hint: <path to save folder> [--reveal] [--player <name>]
allowed-tools: Read, Glob, Grep, Bash, Write
model: sonnet
---

# /pz-savegame-fog

Inspect or reveal the world-map fog of war stored per player in a dedicated-server save.
$ARGUMENTS names the save folder (the one holding `map/`, `players.db`, `map_visited_server/`).

Default is **read-only**: report each player's revealed percentage. Only `--reveal` writes.

Call the Skill tool with `pz-server` and read
[references/SAVEGAME-FORMAT.md](../skills/pz-server/references/SAVEGAME-FORMAT.md) before touching a
byte. It carries the verified layout, the bit semantics and the three things that are *not* verified.
Derive the geometry from the save's own `map_worldgen.bin` — never assume the default bounds.

## Why file editing is the only route

State this to the user before writing, because the obvious alternatives do not work:

- **`Map.MapAllKnown` does nothing here.** It is read only in `WorldMapVisited.getInstance()` — the
  client class — sets the KNOWN bit once at character creation, and is absent from
  `WorldMapVisitedServer` entirely. It never applies retroactively to an existing character.
- **No RCON command, admin command or Lua API exists** for revealing the map.
- **Deleting the zip hides everything**, not reveals it: `loadUser()` falls back to a zero-filled
  array, and zero means unexplored.

## Establish first

1. **Which players.** All of `map_visited_server/*.zip`, or the one named by `--player`.
2. **Server stopped, or that player disconnected.** `WorldMapVisitedServer` keeps a decompressed copy
   in `dictionary` for every connected user and writes it back in `saveUser()` on disconnect and on
   the save tick. Editing under a live connection loses the edit. Refuse to write until confirmed.
3. **A backup exists.** Copy the `.zip` files aside first and name the location in the report.

## Reading

Per `<user>.zip`: one entry named exactly like the user, first 4 bytes big-endian world version,
remainder the payload. Compute from `map_worldgen.bin`:

```
widthInCells = maxXCell - minXCell + 1
span         = widthInCells * 8 / 4
payload      = span * (maxYCell - minYCell + 1) * 8
```

Each payload byte packs 4 x-units of 2 bits, low bits first: `0` unexplored, `1` visited,
`2` known, `3` both. Report revealed units as a percentage of `payload * 4`.

To verify the geometry before trusting it, take a player position from
`players.db` (`SELECT username,x,y FROM networkPlayers`) and check that its own unit reads non-zero:

```
ux = (x - minXCell*256) // 32 ;  uy = (y - minYCell*256) // 32
flags = (payload[ux//4 + uy*span] >> ((ux % 4) * 2)) & 3
```

A player standing on `flags == 0` means the geometry is wrong — stop and re-derive it. Do not write.

## Revealing (`--reveal` only)

Keep the first 4 bytes. Set every payload byte to `0xFF` (all four units to `visited+known`; every
byte value is legal, there is no sentinel). Re-zip as a single entry with the **same name** as the
original, and keep the total size identical to the original.

There is no checksum and no length field to maintain.

## Verify before reporting

Re-open each written zip and assert all of: exactly one entry, entry name unchanged, byte size
unchanged, header still the original version int, payload entirely `0xFF`, revealed share 100 %.
Report any file that fails and leave the backup in place rather than claiming success.

## Close by reporting

Per player the before/after revealed percentage, the backup location, the geometry used and where it
came from (`map_worldgen.bin` values), and the restore command — copying the backup zip back.
Then state that the server must be started fresh for clients to receive the new bitmap, since the
sync is server → client on world-map load.

Invent no class, option or command. Where the format is not verified, say so instead of guessing.
