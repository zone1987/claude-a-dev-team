#!/usr/bin/env python3
"""Parse zombie.network.ServerOptions constructor bytecode into a machine-readable
option table: INI key, Java field, type, default, min, max, public flag.

Input is `javap -p -c -cp projectzomboid.jar zombie.network.ServerOptions`.
No model sits between the class file and the output.
"""
import json
import re
import subprocess
import sys

CTOR_START = re.compile(r"^\s*public zombie\.network\.ServerOptions\(\);")
# javap renders the empty string constant as "// String" with no value after it,
# so the value group must be allowed to be empty.
LDC = re.compile(r"^\s*\d+: ldc(?:_w)?\s+#\d+\s+// (String|int|float|double|long)(?: (.*))?$")
LDC2 = re.compile(r"^\s*\d+: ldc2_w\s+#\d+\s+// (double|long) (.*)$")
PUSH = re.compile(r"^\s*\d+: (iconst_m1|iconst_\d|bipush|sipush)\s*(-?\d+)?")
DCONST = re.compile(r"^\s*\d+: dconst_(\d)")
NEW = re.compile(r"^\s*\d+: new\s+#\d+\s+// class zombie/network/ServerOptions\$(\w+ServerOption)")
INVOKE = re.compile(
    r'^\s*\d+: invokespecial\s+#\d+\s+// Method zombie/network/ServerOptions\$(\w+ServerOption)\."<init>":\((.*)\)V'
)
PUTFIELD = re.compile(r"^\s*\d+: putfield\s+#\d+\s+// Field (\w+):Lzombie/network/ServerOptions\$")
GETSTATIC = re.compile(r"^\s*\d+: getstatic\s+#\d+\s+// Field ([\w/]+)\.(\w+):")
ADD_PUBLIC = re.compile(r'^\s*\d+: ldc(?:_w)?\s+#\d+\s+// String (\w+)$')


def const_value(line):
    """Return a python value for a constant-push instruction, else None."""
    m = LDC2.match(line)
    if m:
        raw = m.group(2).rstrip("dDfFlL")
        return float(raw) if m.group(1) == "double" else int(raw)
    m = LDC.match(line)
    if m:
        kind, raw = m.group(1), m.group(2) or ""
        if kind == "String":
            return raw
        if kind == "int":
            return int(raw)
        return float(raw.rstrip("dDfFlL"))
    m = DCONST.match(line)
    if m:
        return float(m.group(1))
    m = PUSH.match(line)
    if m:
        op = m.group(1)
        if op == "iconst_m1":
            return -1
        if op.startswith("iconst_"):
            return int(op[-1])
        return int(m.group(2))
    return None


def parse(javap_text):
    lines = javap_text.splitlines()
    start = next(i for i, l in enumerate(lines) if CTOR_START.match(l))
    # constructor runs until the next method declaration at the same indent
    end = len(lines)
    for i in range(start + 2, len(lines)):
        if re.match(r"^  (public|private|protected|static|[A-Za-z])", lines[i]) and "invoke" not in lines[i]:
            end = i
            break
    body = lines[start:end]

    options = []
    stack = []          # constant values pushed since the last `new`
    pending = None      # the ServerOption subclass most recently `new`ed
    for line in body:
        m = NEW.match(line)
        if m:
            pending = m.group(1)
            stack = []
            continue
        m = INVOKE.match(line)
        if m and pending:
            options.append({"kind": m.group(1), "args": list(stack), "desc": m.group(2)})
            pending = None
            stack = []
            continue
        m = PUTFIELD.match(line)
        if m and options and "field" not in options[-1]:
            options[-1]["field"] = m.group(1)
            continue
        v = const_value(line)
        if v is not None and pending:
            stack.append(v)
            continue
        m = GETSTATIC.match(line)
        if m and pending:
            # a runtime-computed default: keep the symbol, never guess a literal
            stack.append({"$ref": f"{m.group(1).replace('/', '.')}.{m.group(2)}"})
    return options


# Constructor argument order, taken from the LocalVariableTable of the
# zombie.config.*ConfigOption base constructors (javap -v):
#   BooleanConfigOption(name, defaultValue)
#   StringConfigOption(name, defaultValue, maxLength)
#   IntegerConfigOption(name, min, max, defaultValue)
#   DoubleConfigOption(name, min, max, defaultValue)
#   EnumConfigOption(name, numValues, defaultValue)
SHAPES = {
    "BooleanServerOption": ("boolean", ["name", "default"]),
    "StringServerOption": ("string", ["name", "default", "maxLength"]),
    "TextServerOption": ("text", ["name", "default", "maxLength"]),
    "IntegerServerOption": ("integer", ["name", "min", "max", "default"]),
    "DoubleServerOption": ("double", ["name", "min", "max", "default"]),
    "EnumServerOption": ("enum", ["name", "numValues", "default"]),
}


def normalise(options):
    out = []
    for o in options:
        kind = o["kind"]
        if kind not in SHAPES:
            raise SystemExit(f"unknown option class {kind}")
        typename, names = SHAPES[kind]
        args = o["args"]
        if len(args) != len(names):
            raise SystemExit(f"{o.get('field')}: expected {names}, got {args}")
        rec = {"type": typename, "field": o.get("field")}
        for n, v in zip(names, args):
            rec[n] = v
        if typename == "boolean":
            rec["default"] = bool(rec["default"])
        out.append(rec)
    return out


def main():
    jar = sys.argv[1]
    text = subprocess.run(
        ["javap", "-p", "-c", "-cp", jar, "zombie.network.ServerOptions"],
        capture_output=True, text=True, check=True,
    ).stdout
    opts = normalise(parse(text))
    json.dump(opts, sys.stdout, indent=1)
    print(f"\n{len(opts)} options", file=sys.stderr)


if __name__ == "__main__":
    main()
