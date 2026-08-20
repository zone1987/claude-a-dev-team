#!/usr/bin/env bash
# Post-bundling steps: drop the source directories, flatten any leftover depth, add tables of
# contents, repair backtick links. Run right after bundle-skills.py --apply.
set -euo pipefail
PLUGIN="$1"
python3 - "$PLUGIN" <<'PY'
import os, shutil, glob, re, sys, json
plugin=sys.argv[1]
base=f'plugins/{plugin}/skills'
# The domain names come from the map file when there is one, and otherwise from the JSON
# spec: a plugin grouped by name prefix has no map, and demanding one made this step fail
# after the bundling had already succeeded.
domains=set()
spec_map=f'scripts/domain-skills/{plugin}.map'
spec_json=f'scripts/domain-skills/{plugin}.json'
if os.path.exists(spec_map):
    for line in open(spec_map,encoding='utf-8'):
        line=line.split('#')[0]
        if ':' in line and not line[:1].isspace():
            domains.add(line.split(':')[0].strip())
elif os.path.exists(spec_json):
    domains=set(json.load(open(spec_json,encoding='utf-8'))['domains'])
else:
    raise SystemExit(f"no scripts/domain-skills/{plugin}.map or .json — cannot tell which "
                     "directories are domains, so refusing to delete anything")
# The domain directories are named <prefix>-<domain>, and the prefix is not always the
# plugin name: shopware-storefront ships sw-* skills. Derive it the same way bundle-skills
# does — from what the directories on disk actually look like.
existing=sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base,d)))
# Only a prefix that explains ALL domain directories counts. Matching any single
# "-<domain>" suffix would treat "sw-storefront-controller" as prefix "sw-storefront",
# and then spare a source directory from deletion.
# Find the prefix that explains the most domain directories. The plugin name is only one
# candidate: shopware-merchant ships sw-merchant-* directories, so assuming the plugin name
# would make the guard reject every real domain and delete nothing.
counts={}
for d in existing:
    for dom in domains:
        if d.endswith('-'+dom):
            counts[d[:-(len(dom)+1)]]=counts.get(d[:-(len(dom)+1)],0)+1
prefixes={p for p,n in counts.items() if n==max(counts.values())} if counts else set()
prefixes.add(plugin)
keep={f'{pre}-{d}' for pre in prefixes for d in domains}
survivors=[d for d in existing if d in keep]
if not survivors:
    raise SystemExit(
        f"refusing to delete: none of the {len(existing)} directories match a domain name. "
        f"Expected one of {sorted(keep)[:4]}…")
n=0
for d in existing:
    p=os.path.join(base,d)
    if d not in keep and os.path.isdir(p):
        shutil.rmtree(p); n+=1
print(f"  {n} source directories removed -> {len(os.listdir(base))} domains")

moved=0
while True:
    # The two globs overlap, so deduplicate: processing a path twice fails on the second pass.
    deep=sorted({f for f in glob.glob(base+'/*/*/**/*.md',recursive=True)
                 + glob.glob(base+'/*/*/*.md') if os.path.exists(f)})
    if not deep: break
    for f in deep:
        parts=f.split('/'); sd='/'.join(parts[:4])
        stem=os.path.splitext(parts[-1])[0].upper().replace('_','-')
        name=stem if parts[4].lower() in ('references','deep') else f"{parts[4].upper()}-{stem}"
        dest=os.path.join(sd,name+'.md'); i=2
        while os.path.exists(dest): dest=os.path.join(sd,f"{name}-{i}.md"); i+=1
        shutil.move(f,dest); moved+=1
print(f"  {moved} files raised one level")
for root,dirs,files in os.walk(base, topdown=False):
    if root.count('/')>=4 and not files and not dirs: os.rmdir(root)

fixed=0
for f in glob.glob(base+'/*/*.md'):
    t=open(f,encoding='utf-8').read()
    n2=re.sub(r'\[`([^`\]]+\.md)`\]\(`\1`\)', r'[\1](\1)', t)
    if n2!=t: open(f,'w',encoding='utf-8').write(n2); fixed+=1
print(f"  {fixed} backtick links repaired")
PY
python3 scripts/add-toc.py --plugin "$PLUGIN"
