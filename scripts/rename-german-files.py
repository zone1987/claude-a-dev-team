#!/usr/bin/env python3
"""Rename German file names to English and repair every reference to them.

A rename that leaves a dangling link behind is worse than the German name it
removed, so both halves happen in one pass. The script refuses to act while any
word is still untranslated or any target name is already taken — a half-applied
rename is the one outcome worse than doing nothing.

Case is preserved per word: UEBERBLICK -> OVERVIEW, Uebersicht -> Overview,
uebersicht -> overview. Only the German words are replaced; everything else in
the name is left byte-identical.

    python3 scripts/rename-german-files.py            # report
    python3 scripts/rename-german-files.py --apply
"""
import argparse, os, re, subprocess, sys
from collections import Counter

# German -> English, lower case keys. Case is restored from the source word.
WORDS = {
    'ueberblick': 'overview', 'uebersicht': 'overview', 'ubersicht': 'overview',
    'kategorieubersicht': 'category-overview',
    'kundenuebersicht': 'customer-overview',
    'erweiterungen': 'extensions', 'erweiterte': 'advanced',
    'kundenspezifische': 'customer-specific',
    'profileinstellungen': 'profile-settings',
    'grundeinstellungen': 'basic-settings',
    'allgemeineeinstellungen': 'general-settings',
    'einstellungen': 'settings', 'zahlungsarten': 'payment-methods',
    'zahlungsart': 'payment-method', 'versandarten': 'shipping-methods',
    'stammdaten': 'master-data', 'empfaenger': 'recipients',
    'bestellungen': 'orders', 'bestellung': 'order',
    'bestelldetails': 'order-details', 'schnellbesteller': 'quick-order',
    'regelungen': 'regulations', 'beispiele': 'examples', 'beispiel': 'example',
    'beispielregel': 'example-rule', 'produkte': 'products', 'produkt': 'product',
    'betrieb': 'operations', 'kosten': 'costs', 'meine': 'my', 'preise': 'prices',
    'suche': 'search', 'firma': 'company', 'allgemeines': 'general',
    'allgemein': 'general', 'kategorie': 'category', 'lieferbarkeit': 'availability',
    'erstellen': 'create', 'ersetzen': 'replace', 'verwendung': 'usage',
    'metadaten': 'metadata', 'medien': 'media', 'ordner': 'folder',
    'sektions': 'section', 'klassifizierung': 'classification',
    'kundengruppen': 'customer-groups', 'kundengruppe': 'customer-group',
    'kundenaccount': 'customer-account', 'kunden': 'customers', 'kunde': 'customer',
    'anmelden': 'login', 'anlegen': 'create', 'bearbeiten': 'edit',
    'adressen': 'addresses', 'abonnements': 'subscriptions', 'profil': 'profile',
    'optionen': 'options', 'registrierungsformular': 'registration-form',
    'ansicht': 'view', 'vorlagen': 'templates', 'konfiguration': 'configuration',
    'erlebniswelten': 'shopping-experiences', 'galerie': 'gallery',
    'dokumente': 'documents', 'dokument': 'document',
    'lieferstatus': 'delivery-status', 'hinzufuegen': 'add', 'retoure': 'return',
    'stornierungen': 'cancellations', 'zuweisung': 'assignment',
    'loeschen': 'delete', 'reiter': 'tab', 'verwalten': 'manage',
    'bedienung': 'usage', 'voraussetzungen': 'prerequisites', 'auswahl': 'selection',
    'regeln': 'rules', 'regelnteilen': 'sharing-rules', 'prozent': 'percent',
    'kaufe3zahle2': 'buy3pay2', 'lager': 'stock', 'formular': 'form',
    'netto': 'net', 'deaktivieren': 'disable', 'inhaltselement': 'content-element',
    'auflistung': 'listing', 'menue': 'menu', 'menueleiste': 'menu-bar',
    'kontextmenue': 'context-menu', 'individuelle': 'individual',
    'individuellen': 'individual', 'neues': 'new', 'neuer': 'new', 'neue': 'new',
    'rabatte': 'discounts', 'rabatt': 'discount', 'warenkorb': 'cart',
    'aktionscodes': 'promotion-codes', 'szene': 'scene', 'bild': 'image',
    'aenderung': 'change', 'mehrfachaenderung': 'bulk-change',
    'aktualisieren': 'update', 'anmeldung': 'login', 'auspraegung': 'variant',
    'auszeichnung': 'labelling', 'bedingung': 'condition', 'breite': 'width',
    'hoehe': 'height', 'datenschutz': 'privacy', 'dynamische': 'dynamic',
    'editieren': 'edit', 'eigenschaften': 'properties',
    'ersteinrichtung': 'initial-setup', 'erzeugen': 'create',
    'exportieren': 'export', 'importieren': 'import', 'farben': 'colors',
    'farbe': 'color', 'felder': 'fields', 'feld': 'field',
    'generierung': 'generation', 'gutschrift': 'credit-note',
    'internationalisierung': 'internationalisation', 'kanal': 'channel',
    'verkaufskanal': 'sales-channel', 'kategorieseite': 'category-page',
    'produktdetailseite': 'product-detail-page', 'produktgruppe': 'product-group',
    'shopseite': 'shop-page', 'seitenstruktur': 'page-structure',
    'rechnung': 'invoice', 'stornorechnung': 'cancellation-invoice',
    'steuerberechnung': 'tax-calculation', 'steuern': 'taxes',
    'sichtbarkeit': 'visibility', 'unterschiedlich': 'different',
    'vorbereitung': 'preparation', 'vorschau': 'preview', 'vorher': 'before',
    'nachher': 'after', 'werkzeuge': 'tools', 'zahlung': 'payment',
    'zwischensumme': 'subtotal', 'schuhe': 'shoes', 'typografie': 'typography',
    'seite': 'page', 'zeile': 'row', 'spalte': 'column', 'liste': 'list',
    'gruppe': 'group', 'datei': 'file', 'wert': 'value',
    'gebuchte': 'booked', 'edition': 'edition', 'verbinden': 'connect',
    'verknuepft': 'linked', 'verknuepfen': 'link', 'aktionen': 'actions',
    'individuell': 'individual', 'testkonto': 'test-account',
    'manuelle': 'manual', 'aktionen': 'actions', 'abonnement': 'subscription',
    'beispiel1': 'example1', 'beispiel2': 'example2', 'beispiel3': 'example3',
    'zugang': 'access', 'produktdetails': 'product-details', 'code': 'code',
    'auswaehlen': 'select', 'vk': 'sales-channel', 'das': 'the', 'und': 'and',
    'oder': 'or', 'mit': 'with', 'ohne': 'without', 'fuer': 'for', 'von': 'from',
}

def restore_case(src, dst):
    """Give dst the case pattern of src."""
    if src.isupper(): return dst.upper()
    if src[:1].isupper(): return '-'.join(w.capitalize() for w in dst.split('-'))
    return dst

# A name still reads German if any of these appears in it.
NEEDLE = re.compile('|'.join(sorted(WORDS, key=len, reverse=True)), re.I)
# Anything with these fragments is German-looking even if not in WORDS.
SUSPECT = re.compile(r'ue|ae|oe|ü|ä|ö|ß', re.I)

def translate_stem(stem):
    """Word-by-word; returns (new_stem, [words that look German but aren't mapped])."""
    parts = re.split(r'([_\-.\s])', stem)
    out, unknown = [], []
    for p in parts:
        if not p or p in '_-. ':
            out.append(p); continue
        hit = WORDS.get(p.lower())
        if hit:
            out.append(restore_case(p, hit))
        else:
            out.append(p)
            # Only flag if it looks German AND is not a known English/technical word.
            if SUSPECT.search(p) and not NEEDLE.search(p):
                unknown.append(p)
    return ''.join(out), unknown

def candidates(root='plugins'):
    for dirpath, dirs, files in os.walk(root):
        if '__pycache__' in dirpath: continue
        for fn in files:
            stem, ext = os.path.splitext(fn)
            if NEEDLE.search(stem):
                yield os.path.join(dirpath, fn), stem, ext

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    renames, unknown_words, collisions = [], Counter(), []
    planned = set()
    for path, stem, ext in candidates():
        new_stem, unknown = translate_stem(stem)
        for u in unknown: unknown_words[u] += 1
        if new_stem == stem: continue
        new_path = os.path.join(os.path.dirname(path), new_stem + ext)
        # Case-insensitive collision check: macOS filesystems fold case.
        if new_path.lower() in planned or (
                os.path.exists(new_path) and new_path.lower() != path.lower()):
            collisions.append((path, new_path)); continue
        planned.add(new_path.lower())
        renames.append((path, new_path))

    print(f"{len(renames)} renames · {len(collisions)} collisions · "
          f"{len(unknown_words)} unmapped German-looking words")
    if unknown_words:
        print("\nUnmapped — add to WORDS before applying:")
        for w, n in unknown_words.most_common(): print(f"  {n:3}  {w}")
    if collisions:
        print("\nTarget name already taken — resolve by hand:")
        for a, b in collisions: print(f"  {a}\n    -> {b}")

    if not args.apply:
        for a, b in renames:
            print(f"  {os.path.basename(a)}  ->  {os.path.basename(b)}")
        return 1 if (unknown_words or collisions) else 0

    if unknown_words or collisions:
        print("\nRefusing to apply while anything above is unresolved.", file=sys.stderr)
        return 1

    for old, new in renames:
        subprocess.run(['git', 'mv', old, new], check=True)

    by_old = {os.path.basename(o): os.path.basename(n) for o, n in renames}
    order = sorted(by_old, key=len, reverse=True)
    touched = 0
    for dirpath, dirs, files in os.walk('.'):
        if '.git' in dirpath.split(os.sep) or '__pycache__' in dirpath: continue
        for fn in files:
            if os.path.splitext(fn)[1] not in {
                    '.md', '.json', '.py', '.txt', '.yml', '.yaml', '.sh'}: continue
            p = os.path.join(dirpath, fn)
            try: src = open(p, encoding='utf-8').read()
            except (UnicodeDecodeError, OSError): continue
            out = src
            for o in order:
                if o in out: out = out.replace(o, by_old[o])
            if out != src:
                assert out.count('\n') == src.count('\n'), p
                open(p, 'w', encoding='utf-8').write(out); touched += 1
    print(f"renamed {len(renames)} files · updated references in {touched} files")
    return 0

if __name__ == '__main__':
    sys.exit(main())
