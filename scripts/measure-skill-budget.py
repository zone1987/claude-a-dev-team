#!/usr/bin/env python3
"""Measure the skill listing cost of every plugin in this marketplace.
Cost per skill = len(description) + len(when_to_use) + 109 (measured overhead).
Budget = 1% of the context window = 8000 chars at 200k."""
import os, sys, glob, re

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
OVERHEAD = 109
BUDGET = 8000

def frontmatter(path):
    try:
        txt = open(path, encoding='utf-8', errors='replace').read()
    except Exception:
        return {}
    if not txt.startswith('---'):
        return {}
    end = txt.find('\n---', 3)
    if end < 0:
        return {}
    fm = txt[3:end]
    out, key, buf = {}, None, []
    for line in fm.splitlines():
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if m:
            if key:
                out[key] = ' '.join(buf).strip()
            key = m.group(1)
            v = m.group(2).strip()
            buf = [] if v in ('>', '|', '>-', '|-', '') else [v]
        elif key is not None:
            buf.append(line.strip().lstrip('- '))
    if key:
        out[key] = ' '.join(buf).strip()
    # Strip the quotes YAML needs around a description containing a colon. They are syntax, not
    # content, and counting them overstates the listing cost: octo-api measures 2,392 with them
    # and 2,376 without.
    for k, v in out.items():
        if len(v) > 1 and v[0] == v[-1] and v[0] in '"\'':
            out[k] = v[1:-1]
    return out

rows = []
for pdir in sorted(glob.glob(os.path.join(ROOT, 'plugins', '*'))):
    if not os.path.isdir(pdir):
        continue
    name = os.path.basename(pdir)
    n = chars = 0
    for sk in sorted(glob.glob(os.path.join(pdir, 'skills', '*', 'SKILL.md'))):
        fm = frontmatter(sk)
        d = fm.get('description', '')
        w = fm.get('when_to_use', '')
        if fm.get('disable-model-invocation', '').lower() in ('true', 'yes', 'on', '1'):
            # Not free: "The listing always contains every skill name", so the description leaves
            # context but the name stays. Count the name and skip the overhead.
            chars += len(fm.get('name', os.path.basename(os.path.dirname(sk))))
            continue
        n += 1
        chars += len(d) + len(w) + OVERHEAD
    if n:
        rows.append((name, n, chars, round((chars - n * OVERHEAD) / n)))

rows.sort(key=lambda r: -r[2])
ts = tn = 0
print(f"{'plugin':34} {'skills':>6} {'chars':>8} {'avg desc':>9} {'% budget':>9}")
print('-' * 70)
for name, n, chars, avg in rows:
    ts += chars; tn += n
    print(f"{name:34} {n:6} {chars:8} {avg:9} {chars/BUDGET*100:8.1f}%")
print('-' * 70)
print(f"{'TOTAL':34} {tn:6} {ts:8} {round((ts-tn*OVERHEAD)/tn):9} {ts/BUDGET*100:8.1f}%")
