#!/usr/bin/env python3
"""Rewrite the pz-java-api reference map from the files that actually exist.

The Java reference is generated, and its file count and split points shift whenever the generator
changes. A hand-written map goes stale silently at that moment: a link to a part that no longer
exists, or a part nobody links to. Both are invisible until something looks for a class and cannot
find its file.

So the map is generated too, from the directory listing plus each file's own header counts, and it
replaces everything between the reference-map markers in SKILL.md.

Usage:
    sync_java_api_map.py [--skill FILE] [--refs DIR]
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

PLUGIN = pathlib.Path(__file__).resolve().parent.parent
BEGIN = "<!-- reference-map:start -->"
END = "<!-- reference-map:end -->"

# What each subsystem is for, in one clause. The generator knows counts, not meaning.
PURPOSE = {
    "ZOMBIE-SCRIPTING": "the script model — `Item`, `VehicleScript`, `Recipe`, `ScriptManager`: everything loaded from `media/scripts`",
    "ZOMBIE-ISO": "the world — `IsoGridSquare`, `IsoCell`, `IsoChunk`, `IsoObject`, `IsoWorld`, `BuildingDef`, `RoomDef`",
    "ZOMBIE-CHARACTERS": "`IsoPlayer`, `IsoZombie`, survivors, animals, body and stats",
    "ZOMBIE-NETWORK": "the client/server layer, every packet class, `GameServer`, `GameClient`",
    "ZOMBIE-CORE": "rendering, textures, input, profiling and the low-level primitives",
    "ZOMBIE-INVENTORY": "`InventoryItem` and its subclasses, `ItemContainer` — the runtime side of items",
    "ZOMBIE-COMMANDS": "every admin and server command class",
    "ZOMBIE-WORLDMAP": "the in-game map, its markers and overlays",
    "ZOMBIE-VEHICLES": "`BaseVehicle`, parts and physics",
    "ZOMBIE-ENTITY": "the build 42 entity and component system",
    "ZOMBIE-LUA": "the Lua bridge — `LuaManager`, `LuaEventManager`, `LuaHookManager`, the Kahlua converters",
    "ZOMBIE-AI": "states, behaviours and the AI director",
    "ZOMBIE-UI": "the Java side of the UI layer",
    "ZOMBIE-RANDOMIZEDWORLD": "randomized buildings, vehicle stories and zone stories",
    "ZOMBIE-AUDIO": "sound and the FMOD bridge",
    "ZOMBIE-DEBUG": "the debug facilities",
    "ZOMBIE-BASEMENTS": "build 42 basements",
    "ZOMBIE-MODDING": "the mod loader",
    "ZOMBIE-SANDBOX": "sandbox options",
    "ZOMBIE-CHAT": "chat, its streams and its commands",
    "ZOMBIE-SAVEFILE": "the save format",
    "ZOMBIE-PATHFIND": "pathfinding",
    "ZOMBIE-ZOMBIE": "zombie-specific systems",
    "ZOMBIE-EROSION": "the erosion system",
    "ZOMBIE-RADIO": "radio and television broadcasts",
    "ZOMBIE-POPMAN": "zombie population management",
    "ZOMBIE-GLOBALOBJECTS": "the global object system",
    "ZOMBIE-WORLD": "world-level services",
    "ZOMBIE-UTIL": "helpers and collections",
    "ZOMBIE": "the root package — `GameWindow`, `SandboxOptions`, `GameTime`",
}
COUNTS = re.compile(r"^(\d+) types across (\d+) package\(s\), (\d+) documented members\.$", re.M)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skill", default=str(PLUGIN / "skills/pz-java-api/SKILL.md"))
    ap.add_argument("--refs", default=str(PLUGIN / "skills/pz-java-api/references"))
    args = ap.parse_args()

    refs = pathlib.Path(args.refs)
    skill = pathlib.Path(args.skill)
    files = sorted(p for p in refs.glob("*.md"))
    if not files:
        print(f"no reference files in {refs}", file=sys.stderr)
        return 2

    groups: dict[str, list[pathlib.Path]] = collections.defaultdict(list)
    for f in files:
        base = re.sub(r"-\d+$", "", f.stem)
        groups[base].append(f)

    stats: dict[str, tuple[int, int]] = {}
    for base, fs in groups.items():
        m = COUNTS.search(fs[0].read_text(encoding="utf-8"))
        stats[base] = (int(m.group(1)), int(m.group(3))) if m else (0, 0)

    ordered = sorted(groups, key=lambda b: -stats[b][1])
    lines = [BEGIN, ""]
    for base in ordered:
        fs = sorted(groups[base], key=lambda p: (len(p.stem), p.stem))
        types, members = stats[base]
        purpose = PURPOSE.get(base, f"the `{base.lower().replace('-', '.')}` package")
        if len(fs) == 1:
            link = f"**[references/{fs[0].name}](references/{fs[0].name})**"
        else:
            # Every part is linked, not just the first and last: a reader jumping to a middle part
            # needs a link, and a file nothing links to is unreachable however the range reads.
            parts = ", ".join(f"[{f.name.replace(base + '-', '')[:-3]}](references/{f.name})" for f in fs)
            link = f"**{base}** ({len(fs)} parts: {parts})"
        lines.append(f"- {link}: {types} types, {members:,} members — {purpose}.")
    lines += ["", f"{len(files)} files in total; `ls references/` lists them.", "", END]

    text = skill.read_text(encoding="utf-8")
    if BEGIN in text and END in text:
        new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), "\n".join(lines), text, flags=re.S)
    else:
        new = re.sub(r"(## Reference map\n\n).*?(\n## )", r"\1" + "\n".join(lines) + r"\2",
                     text, count=1, flags=re.S)
    skill.write_text(new, encoding="utf-8")

    print(f"{len(files)} files, {len(groups)} subsystems -> {skill.name}")
    print(f"largest: {ordered[0]} with {stats[ordered[0]][1]:,} members across {len(groups[ordered[0]])} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
