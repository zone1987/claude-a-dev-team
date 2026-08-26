---
name: pz-mod-new
description: Scaffold a Project Zomboid build 42 mod with the correct folder layout, mod.info and the client/server split the feature needs.
argument-hint: <what the mod should do> [--name ModName] [--server-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Edit
model: sonnet
---

# /pz-mod-new

Scaffold a build 42 mod for what $ARGUMENTS describes. Ask one question at a time, and skip whatever
the arguments already answer.

## Establish first (one question at a time)

1. **What it does**, concretely — the behaviour, not the implementation.
2. **Which side it runs on.** Client for UI and input, server for authority and world writes, both
   for most real features. This decides the folder layout, so settle it before writing anything.
3. **Does it need to persist or sync?** That decides whether `ModData` and a command channel are
   part of the scaffold.
4. **The mod's id and display name**, if `--name` did not give them.

## Then derive from the reference files, not from memory

Call the Skill tool with `pz-modding` for the layout and `mod.info`, then whichever the feature needs:
`pz-events` for hooks, `pz-items` or `pz-crafting` for definitions, `pz-ui` for panels,
`pz-world` for anything positional, `pz-multiplayer` for the client/server channel,
`pz-server` for a server command.

State before writing:
- the exact **folder layout** for build 42, including the versioned directories,
- every **`mod.info` key** the mod needs, with its value,
- which **events** the feature hooks and their exact arguments,
- which **side** each file belongs on, and why.

## Then write

- the folder tree with `mod.info` filled in,
- one Lua file per concern, each under the correct side directory,
- every event handler with nil-guards on its arguments,
- a `ModData` accessor if state persists,
- a client/server command pair if the feature crosses the boundary,
- no work in `OnTick` — use a timer or a coarser event.

## Close by reporting

The files written, the folder layout with each file's side, the events hooked with their arguments,
what to enable in game to test it, and the exact reference file each non-obvious value came from.

Invent no API. Take every class, method, event and property name from the reference files verbatim.
