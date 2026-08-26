# Sides, commands and getting data out of the game

## Contents

- [Which side runs what](#which-side-runs-what)
- [Detecting the side at runtime](#detecting-the-side-at-runtime)
- [Commands between client and server](#commands-between-client-and-server)
- [Getting data out of the game process](#getting-data-out-of-the-game-process)
- [What Lua cannot do](#what-lua-cannot-do)

## Which side runs what

The directory a Lua file sits in decides where it executes, and there is no runtime override:

| Directory | Dedicated server | Client connected to one | Singleplayer |
| --- | --- | --- | --- |
| `media/lua/client/` | not loaded | loaded | loaded |
| `media/lua/server/` | loaded | not loaded | loaded |
| `media/lua/shared/` | loaded | loaded | loaded |

Singleplayer loads both sides in one process. That is why a side mistake works perfectly in
singleplayer and fails only once a dedicated server is involved, which makes it one of the most
expensive classes of bug in Zomboid modding.

## Detecting the side at runtime

Four predicates, with their measured frequency in the game's own 1,395 Lua files — the frequency is
a good guide to which one the game itself trusts:

| Function | Uses in game code | Means |
| --- | ---: | --- |
| `isClient()` | 614 | this process is a client connected to a server. **False in singleplayer.** |
| `isServer()` | 281 | this process is a dedicated or hosted server |
| `isAdmin()` | 11 | the local player has admin rights |
| `isDedicated()` | 5 | this process is a dedicated server specifically |
| `isCoopHost()` | 2 | this process hosts a co-op game |

The trap is `isClient()` returning false in singleplayer: code guarded by `if isClient() then` does
not run there. For "am I not the authority", test `isClient()`; for "is there a separate server",
combine the predicates rather than assuming one implies another.

## Commands between client and server

There is no way for a mod to define its own network packet — the packet classes in
`zombie.network.packets` are Java and fixed. What a mod has instead is a generic command channel,
and it is sufficient for everything a mod normally needs.

**Client to server:**

```lua
-- client
sendClientCommand(player, "MyMod", "requestNearestItem", { itemType = "Base.Shovel" })

-- server
local function onClientCommand(module, command, player, args)
    if module ~= "MyMod" then return end
    if command == "requestNearestItem" then
        -- do the work, then answer
        sendServerCommand(player, "MyMod", "nearestItem", { x = 1234, y = 5678, z = 0 })
    end
end
Events.OnClientCommand.Add(onClientCommand)
```

**Server to client** is `sendServerCommand`, received through `OnServerCommand` with the same
`(module, command, args)` shape. The `module` string is a namespace: use your mod's id so two mods
cannot collide on a command name.

The game's own dispatcher for this is `media/lua/server/ClientCommands.lua`, 1,260 lines, and it is
the reference implementation worth reading before writing your own.

**The arguments table crosses a serialisation boundary.** Plain tables of strings, numbers and
booleans travel; anything else needs establishing before relying on it. A value that does not
serialise arrives as `nil` rather than raising, so a handler must check its arguments rather than
assume them.

**The server is authoritative.** A client command is a *request*. Validate every field server-side —
a client can send any value, including one your UI would never produce.

## Getting data out of the game process

This is the mechanism question for any external tool: a Discord bot, a control panel, a dashboard.

**The supported channel is the filesystem.** Two globals write files, and they are the only outbound
write path exposed to Lua:

| Global | Signature | Writes to |
| --- | --- | --- |
| `getFileWriter` | `getFileWriter(String filename, boolean createIfNull, boolean append)` | the Zomboid data directory |
| `getModFileWriter` | `getModFileWriter(String modId, String filename, boolean createIfNull, boolean append)` | that mod's directory under the Zomboid data folder |

Their reading counterparts are `getFileReader` and `getModFileReader`. On this machine the Zomboid
data directory is `~/Zomboid`.

The shape that works for a bridge:

```lua
local function emit(line)
    local w = getModFileWriter("MyMod", "events.log", true, true)  -- append
    if w then
        w:write(line .. "\n")
        w:close()
    end
end
```

**Append, never rewrite.** A consumer tailing the file survives a server restart and can never read a
half-written state file. A rewritten state file can be read mid-write, and that failure is
intermittent, which is the worst kind.

**One stream, many consumers.** Emit one structured line per record and let each outside tool read
it. Three mods writing three formats triples the game-side surface that breaks on an update.

**The other direction** — the outside world telling the game something — is RCON for anything that
maps to an admin command, and a file the mod polls for anything that does not. Call the Skill tool
with `pz-server` for the RCON side.

## What Lua cannot do

Established by searching every global the engine exposes to Lua and the whole of the game's own Lua:

- **No HTTP client.** There is no `httpRequest`, no URL fetch, no REST call available to a mod. The
  only network-shaped globals are Steam server-browser queries (`steamRequestInternetServersList`,
  `steamRequestServerDetails` and siblings), which query the Steam master server list and are not a
  general-purpose HTTP facility.
- **No socket API.** No listener, no outbound connection.
- **No custom network packet.** The packet layer is Java and closed to mods.

So an outside tool is never called *by* the game; it reads what the game wrote, or it drives the game
through RCON. Design the architecture around that from the start rather than discovering it late.

## Source

Distilled from Project Zomboid build 42, installed at
`~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java`,
retrieved 2026-08-26. Side-predicate frequencies counted across `media/lua` (1,395 files); the
absence of an HTTP facility established by searching the `LuaManager.GlobalObject` global list and
the whole of `media/lua`.
