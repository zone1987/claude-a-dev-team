#!/usr/bin/env python3
"""Per page: which identifiers of the source are absent from the plugin.

Excludes the documentation's own formatting labels — a VitePress callout renders its kind as
WARNING/DANGER/TIP text, which is presentation, not a fact to carry. Everything else counts.
"""
import re, sys, glob, importlib.util
spec=importlib.util.spec_from_file_location('ex','/tmp/extract2.py')
ex=importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)

CALLOUTS={'WARNING','DANGER','TIP','NOTE','INFO','CAUTION','IMPORTANT','TEXT','JSON','PHP','JS','TWIG','XML','YAML','BASH','SQL','HTML','SCSS','VUE','TS'}

def ids(txt):
    out={t for t in re.findall(r'\b([A-Z][A-Za-z]{2,}[A-Z][A-Za-z]+|[a-z]+[A-Z][A-Za-z]{3,})\b', txt)}
    return {t for t in out if t.upper() not in CALLOUTS}

mirror, pattern = sys.argv[1], sys.argv[2]
plug=''.join(open(f,encoding='utf-8',errors='replace').read() for f in glob.glob(pattern)).lower()
src=ex.extract(mirror)
s=ids(src)
miss=sorted(i for i in s if i.lower() not in plug)
pct=100 if not s else (len(s)-len(miss))*100//len(s)
print(f'{pct}% of {len(s)} ids' + (f' — missing: {miss}' if miss else ' — complete'))
