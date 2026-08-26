#!/usr/bin/env python3
"""Generate the Lua global function reference from LuaManager$GlobalObject in the game jar.

No model sits between the source and the output. LuaManager.GlobalObject carries 759 public methods,
each of which Kahlua's LuaJavaClassExposer publishes into the Lua global namespace under its own
name. A model asked to transcribe them drops an overload or invents a parameter type; a script
reading `javap` output cannot.

Why javap and not the JavaDoc: JavaDoc's search index records a label such as
`addZombiesInBuilding(BuildingDef, int, String, RoomDef, Integer)` with no return type. javap gives
the fully qualified return type and parameter types from the class file itself, which is the more
complete of the two and needs no network.

Grouping: methods are bucketed by a keyword table over their names, so a reader looking for "how do
I find the player" lands in a section rather than scanning 759 alphabetical entries. Anything the
table does not claim goes to Other, which is listed in full rather than dropped.

Usage:
    build_lua_globals.py --jar PATH --out FILE [--build STR]
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

CLASS = "zombie/Lua/LuaManager$GlobalObject.class"
CLASS_NAME = "zombie.Lua.LuaManager$GlobalObject"

# A javap member line: two spaces, modifiers, then the signature. Constructors and the synthetic
# members javap prints are filtered out by the absence of "(" or by name.
RE_MEMBER = re.compile(
    r"^  public\s+(?:static\s+)?(?:final\s+)?(?:synchronized\s+)?(.+?)\s+"
    r"([A-Za-z_$][A-Za-z0-9_$]*)\((.*)\);$"
)

# Groups in priority order: the first whose pattern matches a name claims the method. Ordering
# matters because names overlap -- getPlayerInventory is inventory, not player.
GROUPS: list[tuple[str, str]] = [
    ("Multiplayer and networking", r"^(send|server|client|isServer|isClient|isCoop|connection|forceDisconnect|backToSinglePlayer|sendPing|checkPermissions|transmit|isAdmin|getAccessLevel|ping|packet|net|Net)"),
    ("Players and characters", r"(player|Player|character|Character|survivor|Survivor|zombie|Zombie|animal|Animal|corpse|Corpse|npc|NPC)"),
    ("Inventory and items", r"(item|Item|inventory|Inventory|container|Container|loot|Loot|clothing|Clothing|weapon|Weapon|fluid|Fluid)"),
    ("World, map and squares", r"(square|Square|cell|Cell|world|World|building|Building|room|Room|tile|Tile|chunk|Chunk|region|Region|zone|Zone|grid|Grid|map|Map|sprite|Sprite|object|Object)"),
    ("Vehicles", r"(vehicle|Vehicle)"),
    ("UI, text and rendering", r"(ui|UI|text|Text|font|Font|draw|Draw|render|Render|screen|Screen|window|Window|panel|Panel|tooltip|Tooltip|colou?r|Colou?r|zoom|Zoom|cursor|Cursor|joypad|Joypad|controller|Controller|mouse|Mouse|key|Key|modal|Modal)"),
    ("Sound, radio and music", r"(sound|Sound|radio|Radio|music|Music|audio|Audio|emitter|Emitter)"),
    ("Time, weather and climate", r"(time|Time|hour|Hour|day|Day|night|Night|month|Month|year|Year|season|Season|weather|Weather|climate|Climate|rain|Rain|snow|Snow|wind|Wind|temperature|Temperature|moon|Moon|sun|Sun)"),
    ("Sandbox, options and config", r"(sandbox|Sandbox|option|Option|config|Config|setting|Setting|difficulty|Difficulty|preset|Preset|gameSpeed|GameSpeed|debug|Debug)"),
    ("Scripts, definitions and managers", r"(script|Script|manager|Manager|definition|Definition|recipe|Recipe|craft|Craft|perk|Perk|trait|Trait|profession|Profession|moodle|Moodle|skill|Skill)"),
    ("Files, mods and Steam", r"(file|File|mod|Mod|steam|Steam|workshop|Workshop|directory|Directory|path|Path|save|Save|load|Load|write|Write|read|Read|cache|Cache|table|Table|serial|Serial)"),
    ("Random and maths", r"(random|Random|Rand|round|floor|ceil|fastfloor|lerp|clamp|distance|Distance|angle|Angle)"),
    ("Reflection and type checks", r"^(instof|typeof|getClassSimpleName|getClassField|getNumClassField|isTable|isFunction|isUserdata|toIndex|toInt|luaClass)"),
]
COMPILED = [(label, re.compile(pat)) for label, pat in GROUPS]
OTHER = "Other"


def short(type_str: str) -> str:
    """Strip package qualifiers from a fully qualified Java type, keeping nested class names.

    `zombie.radio.StorySounds.SLSoundManager` -> `StorySounds.SLSoundManager`, because the nested
    name is what a reader recognises and the package adds nothing at a call site. Generics and
    array/varargs markers are preserved.
    """
    def strip_one(m: re.Match) -> str:
        parts = m.group(0).split(".")
        # Keep the trailing run of capitalised segments: package names are lowercase by convention.
        keep = [p for p in parts if p[:1].isupper()]
        return ".".join(keep) if keep else parts[-1]

    # Match dotted identifier runs; leave <>, [], ... and punctuation alone.
    return re.sub(r"[A-Za-z_$][A-Za-z0-9_$]*(?:\.[A-Za-z_$][A-Za-z0-9_$]*)+", strip_one, type_str)


def group_of(name: str) -> str:
    for label, pat in COMPILED:
        if pat.search(name):
            return label
    return OTHER


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jar", required=True, help="projectzomboid.jar")
    ap.add_argument("--out", required=True)
    ap.add_argument("--build", default="42.20")
    args = ap.parse_args()

    if not shutil.which("javap"):
        print("javap not found; a JDK is required", file=sys.stderr)
        return 1

    jar = pathlib.Path(args.jar)
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(jar) as z:
            try:
                blob = z.read(CLASS)
            except KeyError:
                print(f"{CLASS} not in {jar}", file=sys.stderr)
                return 1
        digest = hashlib.sha256(blob).hexdigest()
        target = pathlib.Path(tmp) / "GlobalObject.class"
        target.write_bytes(blob)
        proc = subprocess.run(
            ["javap", "-p", str(target)], capture_output=True, text=True, check=False
        )
    if proc.returncode != 0:
        print(proc.stderr, file=sys.stderr)
        return 1

    # name -> list of "return type" + "(params)" overloads
    methods: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
    for line in proc.stdout.splitlines():
        m = RE_MEMBER.match(line.rstrip())
        if not m:
            continue
        ret, name, params = m.group(1), m.group(2), m.group(3)
        if name.startswith("access$") or name == "GlobalObject":
            continue
        methods[name].append((short(ret), short(params)))

    buckets: dict[str, list[str]] = collections.defaultdict(list)
    for name in methods:
        buckets[group_of(name)].append(name)

    overloads = sum(len(v) for v in methods.values())
    labels = [lbl for lbl, _ in GROUPS if buckets.get(lbl)] + (
        [OTHER] if buckets.get(OTHER) else []
    )

    out: list[str] = []
    w = out.append
    w(
        f"<!-- generated by scripts/build_lua_globals.py from Project Zomboid build {args.build} "
        f"projectzomboid.jar {CLASS_NAME}, sha256:{digest[:16]} — do not edit -->"
    )
    w("")
    w("# Lua global functions")
    w("")
    w(
        f"The {len(methods)} global functions Project Zomboid exposes to Lua, "
        f"{overloads} signatures counting overloads."
    )
    w("")
    w(
        "**How this was established.** Every public method of "
        f"`{CLASS_NAME}` in `projectzomboid.jar`, read with `javap -p`. Kahlua's "
        "`LuaJavaClassExposer` publishes that class into the Lua global namespace, so each method "
        "below is callable from Lua by its bare name with no receiver: `getPlayer()`, not "
        "`GlobalObject.getPlayer()`."
    )
    w("")
    w(
        "Java types are shown with their package stripped. `KahluaTable` is a Lua table crossing "
        "the boundary; `ArrayList<T>` and other Java collections arrive as Java objects and are "
        "indexed with `:get(i)` from 0, never with `[i]`."
    )
    w("")
    w(
        "A name absent from this file is not a global function of this build. Report that rather "
        "than guessing a spelling."
    )
    w("")
    w("## Contents")
    w("")
    for lbl in labels:
        anchor = lbl.lower().replace(" ", "-").replace(",", "").replace(".", "")
        w(f"- [{lbl}](#{anchor}) ({len(buckets[lbl])})")
    w("")

    for lbl in labels:
        w(f"## {lbl}")
        w("")
        w(f"{len(buckets[lbl])} function(s).")
        w("")
        for name in sorted(buckets[lbl], key=str.lower):
            sigs = methods[name]
            if len(sigs) == 1:
                ret, params = sigs[0]
                w(f"- `{name}({params})` -> `{ret}`")
            else:
                w(f"- `{name}` — {len(sigs)} overload(s):")
                for ret, params in sorted(sigs):
                    w(f"    - `{name}({params})` -> `{ret}`")
        w("")

    w("## Source")
    w("")
    w(
        f"Generated by `scripts/build_lua_globals.py` from `{CLASS_NAME}` in "
        f"`projectzomboid.jar` of Project Zomboid build {args.build}, class sha256 `{digest}`."
    )
    w("")

    pathlib.Path(args.out).write_text("\n".join(out), encoding="utf-8")
    print(f"{len(methods)} names, {overloads} signatures -> {args.out}")
    print(f"class sha256: {digest}")
    for lbl in labels:
        print(f"  {lbl}: {len(buckets[lbl])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
