# Debugging and testing a Project Zomboid mod

## Contents

- [Where the files are](#where-the-files-are)
- [Debug mode](#debug-mode)
- [Reading an error](#reading-an-error)
- [Reloading without a restart](#reloading-without-a-restart)
- [Running a local dedicated server](#running-a-local-dedicated-server)
- [Failure signatures](#failure-signatures)
- [What the game does not provide](#what-the-game-does-not-provide)

## Where the files are

On macOS everything the game writes lives under `~/Zomboid`:

| Path | Holds |
| --- | --- |
| `~/Zomboid/console.txt` | the current run's console output, including every Lua error |
| `~/Zomboid/Logs/` | dated log directories plus `*_DebugLog.txt` files |
| `~/Zomboid/Lua/` | Lua-written data, the default target of `getFileWriter` |
| `~/Zomboid/mods/` | locally installed mods |
| `~/Zomboid/Saves/` | save games, one directory per world |
| `~/Zomboid/Server/` | dedicated server configuration: the INI, sandbox vars, spawn regions |
| `~/Zomboid/options.ini` | client options |
| `~/Zomboid/version.txt` | the installed build, which is what to quote when reporting a bug |

On Windows this is `%UserProfile%\Zomboid`, on Linux `~/Zomboid`. The install directory is separate
and holds no user data — editing a file there is not how a mod is installed.

**`console.txt` is truncated at each launch.** Copy it before relaunching, or the error is gone.

## Debug mode

Debug mode adds the debug toolstrip, entity and world inspectors, teleporting, item spawning and
the Lua debugger UI. The game's own Lua tests it in 43 places through `isDebugEnabled()` and reads
its settings through `DebugOptions`, referenced 59 times — so a mod can branch on it too, which is
useful for developer-only panels.

It is enabled by launching the game with the debug flag rather than from a setting inside the game.

## Reading an error

A Lua error in `console.txt` carries the message, then a stack of `function: file line N` frames,
innermost first. Two things make it readable:

- **The innermost frame is where it threw, not necessarily where the bug is.** A `nil` argument
  usually originates one or two frames out.
- **`attempt to index a nil value` on a Java call means the method does not exist.** Lua calling a
  nonexistent Java method returns `nil` rather than raising, so the failure appears at the next use.
  Verify the name — call the Skill tool with `pz-java-api` and grep it.

A Java exception in the log is an engine-level failure and carries a Java stack trace instead. If a
mod triggered it, the Lua frames appear above it.

## Reloading without a restart

- **Lua files** can be reloaded in game from the debug menu, which re-executes them. State held in
  locals is lost and event handlers registered at file scope are registered again — so a reload can
  leave two handlers attached where one is wanted. Guard registration if you rely on reloading.
- **Script files** under `media/scripts` are read at load. A change to an item or recipe needs a
  restart.
- **A new file** the game has not seen needs a restart.
- **`mod.info`** changes need a restart.

## Running a local dedicated server

The install ships the server: `StartServer.command` (and `StartServerSteam.command`) in the game's
directory. It needs a JDK — the script says so on launch. That gives a real client/server split on
one machine, which is the only honest way to test multiplayer behaviour, since singleplayer loads
both sides and hides side mistakes.

First launch writes the configuration into `~/Zomboid/Server/`, and `RCON.command` in the same
directory is the shipped RCON client.

## Failure signatures

| What you see | What it usually means |
| --- | --- |
| The mod does not appear in the mod list | `mod.info` missing, malformed, or the directory is not directly under `mods/` |
| The mod appears but nothing happens | the Lua is in the wrong side directory for what it does |
| Works in singleplayer, not on a server | the same, exposed: singleplayer loaded both sides |
| `attempt to index a nil value` on a Java object | the method or field does not exist under that name |
| An event handler runs once and never again | it threw; the error is in `console.txt` above the silence |
| A value arrives `nil` across `sendClientCommand` | it did not serialise; only plain tables of primitives travel |
| A world query returns nothing on an empty server | correct: no players means no loaded chunks |
| The server lags after installing the mod | work in `OnTick` or `OnPlayerUpdate` |

## What the game does not provide

Stated plainly, because looking for these costs time:

- **No unit-test framework.** There is no test runner, no assertion library and no headless mode for
  running Lua outside the game. Testing means launching, and for multiplayer behaviour it means
  launching a local server as well.
- **No breakpoint debugger** in the ordinary sense from an external editor. The in-game Lua debugger
  UI in debug mode is what exists.
- **No hot reload of script files.** Only Lua reloads.

The practical consequence is that a mod's structure carries the testing burden: small functions that
take their inputs as arguments can be exercised from the Lua console, while logic buried in an event
handler can only be tested by playing.

## Source

Distilled from Project Zomboid build 42, installed at
`~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java`,
with the user data directory at `~/Zomboid`, retrieved 2026-08-26. `isDebugEnabled` and
`DebugOptions` frequencies counted across `media/lua` (1,395 files).
