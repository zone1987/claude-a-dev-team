#!/usr/bin/env python3
"""Extract a reui.io docs page as markdown, keeping code blocks and prop tables intact."""
import re, html, sys


def _code(mo):
    lang = ''
    lm = re.search(r'language-([a-z0-9]+)', mo.group(0))
    if lm:
        lang = lm.group(1)
    inner = mo.group(2)
    # shiki renders each source line as its own span; keep those breaks
    inner = re.sub(r'<span[^>]*data-line[^>]*>', '\n', inner)
    inner = re.sub(r'<span class="line[^"]*">', '\n', inner)
    inner = re.sub(r'</?div[^>]*>', '\n', inner)
    inner = re.sub(r'<[^>]+>', '', inner)
    text = re.sub(r'\n{3,}', '\n\n', html.unescape(inner))
    return '\n```' + lang + '\n' + text.strip('\n') + '\n```\n'


def extract(path):
    h = open(path, encoding='utf-8', errors='replace').read()
    h = re.sub(r'<(script|style|svg|noscript)\b[^>]*>.*?</\1>', '', h, flags=re.S | re.I)

    # the doc body starts at the page h1 and ends at the "next page" pager
    start = h.find('<h1')
    if start == -1:
        return ''
    end = len(h)
    for marker in ('data-slot="doc-pager"', 'aria-label="Pagination"', '<footer'):
        i = h.find(marker, start)
        if i != -1:
            end = min(end, i)
    b = h[start:end]

    blocks = []

    def stash(mo):
        blocks.append(_code(mo))
        return '\x00BLOCK%d\x00' % (len(blocks) - 1)

    b = re.sub(r'<(pre)\b[^>]*>(.*?)</\1>', stash, b, flags=re.S | re.I)
    b = re.sub(r'<code\b[^>]*>(.*?)</code>',
               lambda x: '`' + re.sub(r'<[^>]+>', '', x.group(1)).strip() + '`', b, flags=re.S | re.I)

    def row(mo):
        cells = re.findall(r'<t[hd]\b[^>]*>(.*?)</t[hd]>', mo.group(1), re.S | re.I)
        cells = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', c))).strip() for c in cells]
        return '\n| ' + ' | '.join(cells) + ' |' if cells else ''

    b = re.sub(r'<tr\b[^>]*>(.*?)</tr>', row, b, flags=re.S | re.I)
    b = re.sub(r'<h([1-6])\b[^>]*>(.*?)</h\1>',
               lambda x: '\n\n' + '#' * int(x.group(1)) + ' '
                         + re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', x.group(2))).replace('​', '').strip() + '\n',
               b, flags=re.S | re.I)
    b = re.sub(r'<li\b[^>]*>', '\n- ', b, flags=re.I)
    b = re.sub(r'</(p|div|li|tr|table|ul|ol)>', '\n', b, flags=re.I)
    b = re.sub(r'<br\s*/?>', '\n', b, flags=re.I)
    b = re.sub(r'<[^>]+>', '', b)
    t = html.unescape(b).replace('​', '')
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n[ \t]+', '\n', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    for n, blk in enumerate(blocks):
        t = t.replace('\x00BLOCK%d\x00' % n, blk)
    return t.strip() + '\n'


if __name__ == '__main__':
    print(extract(sys.argv[1]))
