---
name: pz-tooling
description: "Project Zomboid modding tools: debug mode, the Lua console, hot reload, testing a mod and reading crash logs. Use when debugging a Project Zomboid mod or naming its console.txt."
---

# Project Zomboid modding tools

Zomboid gives a modder a console log, a debug mode and an in-game Lua console. It gives no test
framework and no external debugger, so the workflow is: read the log, reproduce in game, and keep
logic in functions small enough to exercise from the console.

## The three things to know first

1. **`~/Zomboid/console.txt` holds every Lua error**, and it is truncated at each launch. Copy it
   before relaunching or the evidence is gone.
2. **A nonexistent Java method returns `nil`, it does not raise.** So the error surfaces at the next
   use of that `nil`, one or more frames from the real mistake. When a stack trace makes no sense,
   verify the method name first — call the Skill tool with `pz-java-api`.
3. **Singleplayer hides side mistakes** because it loads both client and server Lua. The install
   ships a dedicated server (`StartServer.command`, needs a JDK), and running it locally is the only
   way to see them.

## Reference map

- **[references/DEBUGGING.md](references/DEBUGGING.md)**: every path the game writes to on each OS, debug mode and what it adds, how to read a Lua stack trace and a Java exception, exactly what reloads without a restart and what does not, how to run the shipped dedicated server and RCON client locally, a table of eight failure signatures with their usual cause, and a plain statement of what the game does not provide.

## Related

Call the Skill tool with "pz-modding" for the layout a mod must have to load at all, "pz-lua-api" for
the code the log is reporting on, "pz-multiplayer" for the side split a local server exposes, and
"pz-server" for the server configuration the first launch writes.

## Source

Distilled from Project Zomboid build **42.20.2** (revision `ffe7a8a4b1`), installed at
`~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java`,
with the user data directory at `~/Zomboid`, retrieved 2026-08-26.

The game's own files are the primary source; the API is cross-checked against the build 42 JavaDocs at <https://projectzomboid.com/modding/index.html> and the unofficial build <https://github.com/demiurgeQuantified/ProjectZomboidJavaDocs>.
