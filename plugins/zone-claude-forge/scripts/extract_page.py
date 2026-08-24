#!/usr/bin/env python3
"""Extract a developer.shopware.com page as markdown, keeping code blocks intact."""
import re, html, sys

def extract(path):
    h=open(path,encoding='utf-8',errors='replace').read()
    # a literal <?php in the page must not be read as a processing instruction
    h=h.replace('&lt;?php','\x00PHPOPEN\x00')
    h=re.sub(r'<(script|style|nav|header|footer)\b[^>]*>.*?</\1>','',h,flags=re.S|re.I)
    m=re.search(r'<main[^>]*>(.*?)</main>',h,re.S) or re.search(r'<div class="vp-doc[^"]*"[^>]*>(.*?)</div>\s*</div>',h,re.S)
    b=m.group(1) if m else h

    def code(mo):
        lang=''
        lm=re.search(r'language-([a-z0-9]+)', mo.group(0))
        if lm: lang=lm.group(1)
        inner=mo.group(2)
        # shiki renders each source line as <span class="line">; keep those breaks
        inner=re.sub(r'<span class="line[^"]*">', '\n', inner)
        inner=re.sub(r'<[^>]+>','',inner)
        text=html.unescape(inner)
        text=re.sub(r'\n{3,}','\n\n',text)
        return f'\n```{lang}\n'+text.strip('\n')+'\n```\n'
    blocks=[]

    def stash(mo):
        blocks.append(code(mo))
        return f'\x00BLOCK{len(blocks)-1}\x00'
    b=re.sub(r'<(pre)\b[^>]*>(.*?)</\1>', stash, b, flags=re.S|re.I)
    b=re.sub(r'<code\b[^>]*>(.*?)</code>', lambda x:'`'+re.sub(r'<[^>]+>','',x.group(1)).strip()+'`', b, flags=re.S|re.I)

    # tables, so field/type/default rows survive
    def row(mo):
        cells=re.findall(r'<t[hd]\b[^>]*>(.*?)</t[hd]>', mo.group(1), re.S|re.I)
        cells=[re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',c))).strip() for c in cells]
        return '\n| '+' | '.join(cells)+' |' if cells else ''
    b=re.sub(r'<tr\b[^>]*>(.*?)</tr>', row, b, flags=re.S|re.I)

    b=re.sub(r'<h([1-6])\b[^>]*>(.*?)</h\1>',
             lambda x:'\n\n'+'#'*int(x.group(1))+' '+re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x.group(2))).replace('​','').strip()+'\n', b, flags=re.S|re.I)
    b=re.sub(r'<li\b[^>]*>','\n- ',b,flags=re.I)
    b=re.sub(r'</(p|div|li|tr|table|ul|ol)>','\n',b,flags=re.I)
    b=re.sub(r'<br\s*/?>','\n',b,flags=re.I)
    b=re.sub(r'<[^>]+>','',b)
    t=html.unescape(b).replace('​','')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n[ \t]+','\n',t)
    t=re.sub(r'\n{3,}','\n\n',t)
    for n, blk in enumerate(blocks):
        t=t.replace(f'\x00BLOCK{n}\x00', blk)
    return t.replace('\x00PHPOPEN\x00','<?php').strip()

if __name__=='__main__':
    print(extract(sys.argv[1]))
