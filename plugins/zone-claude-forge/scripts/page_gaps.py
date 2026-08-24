#!/usr/bin/env python3
"""For one page: print the source context of every identifier the plugin lacks."""
import re, sys, subprocess, importlib.util, glob
spec=importlib.util.spec_from_file_location('ex','plugins/zone-claude-forge/scripts/extract_page.py')
ex=importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)
page, pattern = sys.argv[1], sys.argv[2]
out=subprocess.run(['python3','/tmp/coverage.py',page,pattern],capture_output=True,text=True).stdout
if 'missing:' not in out:
    print(out.strip()); sys.exit()
miss=[x.strip(" '[]") for x in out.split('missing:')[1].strip().rstrip(']').split(',')]
src=ex.extract(page).splitlines()
for m in miss:
    hits=[i for i,l in enumerate(src) if m in l]
    print(f'--- {m} ({len(hits)} hit)')
    for i in hits[:2]:
        print('   ', src[i].strip()[:150])
