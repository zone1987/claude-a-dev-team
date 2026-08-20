#!/usr/bin/env python3
"""Repair every agent's `skills:` frontmatter after the domain restructuring.

The restructuring folded 831 skills into 117 domain skills but never touched
`agents/`, so 45 of 47 agents preload skill names that no longer exist. A name
that does not resolve is silently dropped, so those agents start without the
knowledge their body assumes they have.

The mapping is not guessed: `scripts/domain-skills/<plugin>.map` records which
old skills went into which domain, and that is what the restructuring itself
used. Old names are translated through it; names already valid are kept.

    python3 scripts/fix-agent-skills.py            # report
    python3 scripts/fix-agent-skills.py --apply
"""
import argparse, glob, os, re, sys
from collections import OrderedDict

def load_map(plugin):
    """old-skill-name -> domain-skill-name, from the restructuring's own map."""
    path = f'scripts/domain-skills/{plugin}.map'
    if not os.path.exists(path): return {}, None
    prefix, out, domain = None, {}, None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip()
        if not line or line.lstrip().startswith('#'):
            m = re.search(r'prefix[:= ]+([a-z0-9-]+)', line)
            if m: prefix = m.group(1)
            continue
        m = re.match(r'^(\S+):\s*(.*)$', line)
        if m:                                 # new domain starts
            domain, rest = m.group(1), m.group(2)
        else:                                 # continuation line
            rest = line.strip()
        if domain is None: continue
        for old in rest.split():
            out[old] = domain
    return out, prefix

def domain_prefix(plugin):
    """The prefix the plugin's real skill directories actually use."""
    dirs = [os.path.basename(d) for d in glob.glob(f'plugins/{plugin}/skills/*')
            if os.path.isdir(d)]
    if not dirs: return None, []
    # Longest common leading token, e.g. sw-merchant- for sw-merchant-catalog.
    parts = [d.split('-') for d in dirs]
    common = []
    for i in range(min(len(p) for p in parts)):
        tok = parts[0][i]
        if all(p[i] == tok for p in parts) and i < min(len(p) for p in parts) - 1:
            common.append(tok)
        else:
            break
    return ('-'.join(common) if common else None), dirs

def resolve(plugin, names):
    """Map a list of skill names onto skills that exist in this plugin.

    The .map files store old skills WITHOUT their plugin prefix (`intro`, not
    `playwright-intro`), because the prefix was uniform. So a name is looked up
    both verbatim and with every plausible prefix stripped.
    """
    have = {os.path.basename(d) for d in glob.glob(f'plugins/{plugin}/skills/*')
            if os.path.isdir(d)}
    mapping, map_prefix = load_map(plugin)
    prefix, _ = domain_prefix(plugin)
    # Prefixes an old name may carry: the domain prefix, the map's own, the
    # plugin name, and `sw` for the shopware family.
    strips = [s for s in {prefix, map_prefix, plugin, 'sw'} if s]
    kept, unresolved = OrderedDict(), []
    for n in names:
        if n in have:                                  # already correct
            kept[n] = None; continue
        keys = [n] + [n[len(s) + 1:] for s in strips if n.startswith(s + '-')]
        dom = next((mapping[k] for k in keys if k in mapping), None)
        if dom:
            for cand in ([f'{prefix}-{dom}'] if prefix else []) + [dom, f'{plugin}-{dom}']:
                if cand in have:
                    kept[cand] = None; break
            else:
                unresolved.append(n)
        else:
            unresolved.append(n)
    return list(kept), unresolved, sorted(have)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    changed = unresolvable = 0
    for path in sorted(glob.glob('plugins/*/agents/*.md')):
        plugin = path.split('/')[1]
        txt = open(path, encoding='utf-8').read()
        m = re.search(r'^(---\n.*?\n)(skills:[^\n]*\n)(.*?^---\n)', txt, re.S | re.M)
        if not m:
            m2 = re.search(r'^skills:[^\n]*$', txt, re.M)
            if not m2: continue
        line = re.search(r'^skills:\s*(.+)$', txt, re.M)
        if not line: continue
        names = [s.strip() for s in line.group(1).split(',') if s.strip()]
        kept, unresolved, have = resolve(plugin, names)
        if kept == names and not unresolved: continue

        # `skills:` injects the FULL body, not the description, so preloading
        # every domain of a plugin defeats the point. Keep the first few — the
        # resolver preserves the agent's own ordering, which is its priority —
        # and let the body reach the rest through the Skill tool.
        CAP = 3
        dropped = kept[CAP:]
        kept = kept[:CAP]

        print(f"\n{path}")
        print(f"  before ({len(names)}): {', '.join(names)}")
        print(f"  after  ({len(kept)}): {', '.join(kept) or '(none)'}")
        if dropped:
            print(f"  not preloaded (reachable via the Skill tool): {', '.join(dropped)}")
        if unresolved:
            print(f"  UNRESOLVED: {', '.join(unresolved)}")
            print(f"  available:  {', '.join(have)}")
            unresolvable += 1
        changed += 1
        if args.apply and kept:
            new = txt[:line.start()] + f"skills: {', '.join(kept)}" + txt[line.end():]
            assert new.count('\n') == txt.count('\n'), path
            open(path, 'w', encoding='utf-8').write(new)

    print(f"\n{changed} agents need changes, {unresolvable} have unresolvable names")
    return 0

if __name__ == '__main__':
    sys.exit(main())
