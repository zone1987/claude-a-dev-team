#!/usr/bin/env python3
"""Extract every zombie.commands.serverCommands.* admin command from
projectzomboid.jar bytecode: command name, argument regexes, required capability,
help-text translation key, the DisabledCommand marker and the class's own string
constants (its output messages).

Every fact comes out of the class file's RuntimeVisibleAnnotations and constant
pool via `javap`. No model sits between the jar and the JSON this prints.

Usage: parse_admin_commands.py /path/to/projectzomboid.jar [translate-UI.json]
"""
import json
import re
import subprocess
import sys
import zipfile

ANN_BLOCK = re.compile(r"^RuntimeVisibleAnnotations:$")
END_BLOCK = re.compile(r"^(BootstrapMethods|InnerClasses|Signature|RuntimeVisible|\})")
NAME = re.compile(r'^\s*name="(.*)"$')
CAP = re.compile(r"^\s*requiredCapability=Lzombie/characters/Capability;\.(\w+)$")
HELP = re.compile(r'^\s*helpText="(.*)"$')
REQUIRED = re.compile(r"^\s*required=\[(.*)\]$")
OPTIONAL = re.compile(r'^\s*optional="(.*)"$')
ARGNAME = re.compile(r'^\s*argName="(.*)"$')
VARARGS = re.compile(r"^\s*varArgs=(\w+)$")
NAMES_LIST = re.compile(r"^\s*value=\[(.*)\]$")
# A marker annotation with no members renders without parentheses
# (zombie.commands.DisabledCommand), so the "(" must be optional.
ANN_HEAD = re.compile(r"^\s*zombie\.commands\.(\w+)\(?$")
STRING_CONST = re.compile(r"^\s*#\d+ = String\s+#\d+\s+// (.*)$")
CONCAT_ARG = re.compile(r"^\s*#\d+ (.*)$")
SUPER = re.compile(r"^\s*super_class: #\d+\s+// ([\w/]+)$")


def javap(jar, cls, verbose=True):
    args = ["javap", "-p", "-v" if verbose else "", "-cp", jar, cls]
    return subprocess.run([a for a in args if a], capture_output=True, text=True).stdout


def split_strings(raw):
    """Split a javap annotation array body like '"(.+)","(\\w+)"' into members."""
    return [m.group(1) for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', raw)]


def parse_annotations(text):
    """Return the annotation facts for one class, as a dict."""
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if ANN_BLOCK.match(l))
    except StopIteration:
        return {}
    out = {"names": [], "argVariants": [], "help": None, "capability": None,
           "disabled": False}
    current = None          # the CommandArgs variant being filled
    kind = None             # which annotation type we are inside
    for line in lines[start + 1:]:
        if END_BLOCK.match(line):
            break
        m = ANN_HEAD.match(line)
        if m:
            kind = m.group(1)
            if kind == "CommandArgs":
                current = {}
                out["argVariants"].append(current)
            if kind == "DisabledCommand":
                out["disabled"] = True
            continue
        if "@zombie.commands.CommandArgs(" in line:
            kind = "CommandArgs"
            current = {}
            out["argVariants"].append(current)
            continue
        m = NAME.match(line)
        if m:
            out["names"].append(m.group(1))
            continue
        m = CAP.match(line)
        if m:
            out["capability"] = m.group(1)
            continue
        m = HELP.match(line)
        if m:
            out["help"] = m.group(1)
            continue
        m = REQUIRED.match(line)
        if m and current is not None:
            current["required"] = split_strings(m.group(1))
            continue
        m = OPTIONAL.match(line)
        if m and current is not None:
            current["optional"] = m.group(1)
            continue
        m = ARGNAME.match(line)
        if m and current is not None:
            current["argName"] = m.group(1)
            continue
        m = VARARGS.match(line)
        if m and current is not None:
            current["varArgs"] = m.group(1) not in ("false", "0")
            continue
        m = NAMES_LIST.match(line)
        if m and kind == "CommandNames":
            out["names"].extend(split_strings(m.group(1)))
            continue
    return out


def parse_strings(text):
    """Every String constant and every string-concat template in the class."""
    consts, concats = [], []
    in_bsm = False
    for line in text.splitlines():
        m = STRING_CONST.match(line)
        if m:
            consts.append(m.group(1))
        if line.startswith("BootstrapMethods:"):
            in_bsm = True
        elif in_bsm and re.match(r"^(InnerClasses|\})", line):
            in_bsm = False
        elif in_bsm:
            m = CONCAT_ARG.match(line)
            if m and "REF_" not in line and not m.group(1).startswith("("):
                concats.append(m.group(1))
    return consts, concats


def parse_super(text):
    for line in text.splitlines():
        m = SUPER.match(line)
        if m:
            return m.group(1).replace("/", ".")
    return None


def main():
    jar = sys.argv[1]
    ui = {}
    if len(sys.argv) > 2:
        with open(sys.argv[2]) as f:
            ui = json.load(f)

    with zipfile.ZipFile(jar) as z:
        classes = sorted(
            n[:-6].replace("/", ".")
            for n in z.namelist()
            if n.startswith("zombie/commands/serverCommands/")
            and n.endswith(".class")
            and "$" not in n
        )

    records = []
    for cls in classes:
        text = javap(jar, cls)
        ann = parse_annotations(text)
        if not ann.get("names"):
            records.append({"class": cls, "commandName": None,
                            "note": "no CommandName/CommandNames annotation",
                            "super": parse_super(text)})
            continue
        consts, concats = parse_strings(text)
        rec = {
            "class": cls,
            "commandName": ann["names"][0],
            "aliases": ann["names"][1:],
            "argVariants": ann["argVariants"],
            "capability": ann["capability"],
            "helpKey": ann["help"],
            "helpText": ui.get(ann["help"]) if ann["help"] else None,
            "disabled": ann["disabled"],
            "super": parse_super(text),
            "stringConstants": consts,
            "messageTemplates": concats,
        }
        records.append(rec)

    json.dump(records, sys.stdout, indent=1)
    named = [r for r in records if r.get("commandName")]
    print(f"\n{len(records)} classes, {len(named)} with a command name",
          file=sys.stderr)


if __name__ == "__main__":
    main()
