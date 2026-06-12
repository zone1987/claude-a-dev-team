---
name: sw-scss-catalog
description: >
  Introspektions-Skill: scannt alle SCSS-Dateien eines konkreten Shopware-Projekts
  (Core + Plugins + aktives Theme) und legt einen Katalog in `.shopware-catalog/scss.md` ab.
  Nutze diesen Skill bei: "welche SCSS-Variablen gibt es im Projekt",
  "SCSS-Katalog erstellen", "alle Variablen meines Themes auflisten",
  "welche CSS-Variablen werden in meinem Projekt definiert".
---

# SW SCSS-Katalog — Projekt-Introspektions-Skill

Dieser Skill scannt ein konkretes Shopware-6-Projekt und erstellt einen vollständigen
SCSS-Katalog unter `.shopware-catalog/scss.md`.

## Wann verwenden

- Du willst wissen, welche SCSS/CSS-Variablen in **deinem** Projekt (inkl. aktives Theme, Plugins) definiert sind
- Du willst einen Überblick über alle SCSS-Dateien und ihren Zweck haben
- Du willst prüfen, ob ein Plugin oder Theme bestimmte Core-Variablen überschreibt

## Mechanik — Schritt für Schritt

### 1. Alle relevanten SCSS-Dateien finden

```bash
# Alle SCSS-Dateien im Projekt (Core + Plugins + Themes)
find . -path "*/Resources/app/storefront/src/scss/**/*.scss" | sort
```

Typische Pfade:
- `vendor/shopware/storefront/src/Storefront/Resources/app/storefront/src/scss/` (Core)
- `custom/plugins/MyPlugin/src/Resources/app/storefront/src/scss/` (Plugin)
- `custom/static-plugins/MyTheme/src/Resources/app/storefront/src/scss/` (Theme)

### 2. SCSS-Variablen extrahieren

```bash
# Alle $variablen-Definitionen mit Wert
grep -rn '^\$[a-z][a-z0-9_-]*:' \
  --include="*.scss" \
  ./vendor/shopware/storefront \
  ./custom/plugins \
  ./custom/static-plugins \
  | grep -v '//.*\$' \
  | sort
```

Regulärer Ausdruck für SCSS-Variable-Definitionen:
```
\$[a-z][a-z0-9_-]*:\s*.+?(!default)?;
```

### 3. CSS Custom Properties extrahieren

```bash
# Alle --custom-property Definitionen
grep -rn '--[a-z][a-z0-9_-]*:' \
  --include="*.scss" \
  ./vendor/shopware/storefront \
  ./custom/plugins \
  ./custom/static-plugins \
  | sort
```

### 4. Theme-Variablen aus theme.json

```bash
# Alle konfigurierbaren Theme-Felder
find . -name "theme.json" | xargs grep -l "config" | head -10
```

Auslesen der `config.fields`-Keys:
```bash
cat custom/static-plugins/MyTheme/src/Resources/theme.json \
  | python3 -c "import sys,json; d=json.load(sys.stdin); [print(k) for k in d.get('config',{}).get('fields',{}).keys()]"
```

### 5. Override-Kette analysieren

Reihenfolge der Variablen-Ladung (wer kann wen überschreiben):

```
1. Core abstract/variables/_bootstrap.scss  (strukturelle Bootstrap-Overrides)
2. Skin/Theme abstract/variables/_theme.scss  (sw-* Theme-Variablen)
3. Skin/Theme abstract/variables/_bootstrap.scss  (Bootstrap-Overrides MIT Farben)
4. Skin/Theme abstract/variables/_custom.scss  (Skin-Custom-Variablen)
5. Bootstrap scss/variables  (Bootstrap-Defaults)
6. Core abstract/variables/_custom.scss  (Framework-Variablen)
7. Plugin variables.scss  (Plugin-Overrides — müssen OHNE !default sein)
```

**Wichtig**: SCSS-Variablen mit `!default` können nur überschrieben werden,
wenn die überschreibende Definition **vorher geladen** wird und **kein `!default`** hat.

### 6. Katalog-Datei erstellen

Erstelle `.shopware-catalog/scss.md` mit folgendem Inhalt:

```markdown
# SCSS-Katalog — [Projektname]
Erstellt: [Datum]

## SCSS-Dateien

| Pfad | Layer | Zweck |
|---|---|---|
| ... | core/plugin/theme | ... |

## SCSS-Variablen

### Theme-Variablen ($sw-*)
| Variable | Wert | Herkunft |
|---|---|---|

### Bootstrap-Overrides
| Variable | Wert | Herkunft |
|---|---|---|

### Plugin/Theme-Overrides
| Variable | Wert | Herkunft | Überschreibt |
|---|---|---|---|

## CSS Custom Properties

| Property | Wert | Datei |
|---|---|---|

## Override-Konflikte
[Variablen die mehrfach definiert werden, mit Ladereihenfolgensanalyse]
```

## Automatisierung (Bash-Skript)

```bash
#!/bin/bash
# .shopware-catalog/refresh-scss.sh

OUTPUT=".shopware-catalog/scss.md"
mkdir -p .shopware-catalog

echo "# SCSS-Katalog" > "$OUTPUT"
echo "Erstellt: $(date)" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "## SCSS-Dateien" >> "$OUTPUT"
echo "" >> "$OUTPUT"
find . -path "*/Resources/app/storefront/src/scss/**/*.scss" \
  -not -path "*/vendor/bootstrap/*" \
  -not -path "*/vendor/tiny-slider/*" \
  -not -path "*/vendor/flatpickr/*" \
  | sort \
  | while read f; do
    echo "- \`$f\`" >> "$OUTPUT"
  done

echo "" >> "$OUTPUT"
echo "## SCSS-Variablen" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo '```' >> "$OUTPUT"
grep -rn '^\$[a-z][a-z0-9_-]*:' \
  --include="*.scss" \
  $(find . -path "*/Resources/app/storefront/src/scss" -type d) \
  2>/dev/null \
  | grep -v vendor \
  | sort >> "$OUTPUT"
echo '```' >> "$OUTPUT"

echo "" >> "$OUTPUT"
echo "## CSS Custom Properties" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo '```' >> "$OUTPUT"
grep -rn '\-\-[a-z][a-z0-9_-]*:' \
  --include="*.scss" \
  $(find . -path "*/Resources/app/storefront/src/scss" -type d) \
  2>/dev/null \
  | grep -v vendor \
  | sort >> "$OUTPUT"
echo '```' >> "$OUTPUT"

echo "Katalog erstellt: $OUTPUT"
```

## Hinweise zur theme.json-Integration

Jede in `theme.json` unter `config.fields` definierte Variable wird vom ThemeCompiler
als SCSS-Variable injiziert. Der Variablenname entspricht dem Key (kebab-case):

```json
"sw-color-brand-primary": { "type": "color", "value": "#0042a0" }
```

→ wird zu `$sw-color-brand-primary: #0042a0` in SCSS injiziert (OHNE `!default`).

Das bedeutet: Theme-Konfigurationswerte aus dem Admin **überschreiben immer** die
`!default`-Werte in `_theme.scss`, weil sie ohne `!default` injiziert werden.
