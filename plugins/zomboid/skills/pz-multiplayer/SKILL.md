---
name: pz-multiplayer
description: "Project Zomboid multiplayer: client and server commands, packets, sync and permissions. Use when the request names sendClientCommand or Zomboid multiplayer sync."
---

# Project Zomboid multiplayer

Two processes, one world, and the server decides. Almost every multiplayer bug in a mod comes from
one of two mistakes: code placed on the wrong side, or a client trusted with a decision.

## The side is decided by the directory

`media/lua/client/` runs on clients, `media/lua/server/` on servers, `media/lua/shared/` on both.
There is no runtime override. **Singleplayer loads both**, which is why a side mistake works while
testing alone and breaks the moment a dedicated server is involved.

At runtime the predicates are `isClient()`, `isServer()`, `isDedicated()`, `isCoopHost()` and
`isAdmin()`. The trap worth knowing before anything else: **`isClient()` returns false in
singleplayer**, so code guarded by it silently does not run there.

## Client and server talk through commands, not packets

A mod cannot define a network packet — the packet layer is Java and closed. What it has is a generic,
namespaced command channel, and it is enough:

```lua
-- client asks
sendClientCommand(player, "MyMod", "requestSomething", { key = "value" })

-- server answers
Events.OnClientCommand.Add(function(module, command, player, args)
    if module ~= "MyMod" then return end
    sendServerCommand(player, "MyMod", "answer", { result = 42 })
end)
```

Use your mod's id as the module so two mods cannot collide. **Validate every argument server-side**:
a client can send any value, and an argument that failed to serialise arrives as `nil` rather than
raising.

## Reference map

- **[references/SIDES-AND-BRIDGING.md](references/SIDES-AND-BRIDGING.md)**: which side loads what, the five side predicates with their measured frequency in the game's own code, the full command round trip with the serialisation caveat, the two file-writing globals with their signatures, and the verified list of what Lua **cannot** do — no HTTP client, no sockets, no custom packets.

## Reaching an external tool

**Lua has no HTTP client and no socket API.** That is verified against every global the engine exposes
and the whole of the game's own Lua, and it is the single most important architectural fact for
anyone building a Discord bot or a control panel: the game is never the caller.

The supported path out is the filesystem — `getFileWriter` and `getModFileWriter`, appending one
structured line per record, with something outside tailing the file. The path in is RCON for anything
that maps to an admin command, and a polled file for anything that does not.

Design for that shape from the start: a small mod that appends lines, and a separate process that
reads them and speaks whatever protocol the outside world wants.

## Related

Call the Skill tool with "pz-server" for RCON and the admin commands, "pz-events" for what a mod can
react to before sending, "pz-lua-api" for where these files belong, and "pz-world" for the
loaded-chunk constraint on anything positional.

## Source

Distilled from Project Zomboid build **42.20.2** (revision `ffe7a8a4b1`), installed at
`~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java`,
retrieved 2026-08-26. Side-predicate counts measured across `media/lua` (1,395 files); the absence of
HTTP and socket facilities established by searching the exposed global list and the game's own Lua.

The game's own files are the primary source; the API is cross-checked against the build 42 JavaDocs at <https://projectzomboid.com/modding/index.html> and the unofficial build <https://github.com/demiurgeQuantified/ProjectZomboidJavaDocs>.
