---
name: pz-server-tool
description: Build a Project Zomboid server-side tool - a custom command, a state query, or a bridge that pushes game state to an external consumer.
argument-hint: <what the tool should do> [--channel rcon|command|file]
allowed-tools: Read, Glob, Grep, Bash, Write, Edit
model: sonnet
---

# /pz-server-tool

Build the server-side tool $ARGUMENTS describes. This covers custom admin commands, state queries,
and bridges that carry game state to something outside the game.

## Establish first (one question at a time)

1. **What the tool answers or does**, stated as a single sentence.
2. **Who triggers it** — an admin over RCON, a player in game, a timer, or an in-game event.
3. **Which channel carries the result out**, if anything leaves the game. Call the Skill tool with
   `pz-multiplayer` and read its bridging file before assuming a channel exists; do not presume the
   game can make an outbound request.
4. **What happens with nobody online.** Server tooling runs on an empty server, and a query that
   depends on loaded chunks returns nothing then. Decide whether that is an error or an empty result.

## Then derive from the reference files

Call the Skill tool with `pz-server` and `pz-multiplayer` first, then `pz-world` for anything
positional, `pz-items` for item queries, `pz-events` for event-driven output.

State before writing:
- the **trigger** and its exact registration,
- the **data path**: what is read, from which API, with which constraint (loaded chunks, side),
- the **output shape**: one line per record, with its fields named,
- the **access level** required, if it is a command.

## Then write

- the server-side Lua, under the `server/` directory,
- argument validation on every command, rejecting rather than assuming,
- the empty case handled explicitly and distinguishably from an error,
- append-only output where a consumer tails a file, never a rewritten state file,
- no secret in the mod — a mod ships to clients, so tokens belong to the outside process,
- a timer rather than `OnTick` for anything periodic.

## Close by reporting

The files written and their side, the trigger, the exact output format with a sample line, the access
level required, the constraints that apply (loaded chunks, players online), and the reference file
each API came from.

Invent no command name, API or channel. Where the sources do not support what was asked, say so and
give the closest thing that works.
