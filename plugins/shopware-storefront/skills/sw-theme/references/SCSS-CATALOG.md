# SW SCSS catalog — project introspection skill

This skill scans a concrete Shopware 6 project and creates a full
SCSS catalog at `.shopware-catalog/scss.md`.

## Contents

- [When to use](#when-to-use)
- [Mechanics — step by step](#mechanics--step-by-step)
- [SCSS files](#scss-files)
- [SCSS variables](#scss-variables)
- [CSS Custom Properties](#css-custom-properties)
- [Override conflicts](#override-conflicts)
- [Automation (bash script)](#automation-bash-script)
- [Notes on theme.json integration](#notes-on-themejson-integration)

## When to use

- You want to know which SCSS/CSS variables are defined in **your** project (incl. active theme, plugins)
- You want an overview of all SCSS files and their purpose
- You want to check whether a plugin or theme overrides particular core variables

## Mechanics — step by step

### 1. Find all relevant SCSS files

```bash
# All SCSS files in the project (core + plugins + themes)
find . -path "*/Resources/app/storefront/src/scss/**/*.scss" | sort
```

Typical paths:
- `vendor/shopware/storefront/src/Storefront/Resources/app/storefront/src/scss/` (Core)
- `custom/plugins/MyPlugin/src/Resources/app/storefront/src/scss/` (Plugin)
- `custom/static-plugins/MyTheme/src/Resources/app/storefront/src/scss/` (Theme)

### 2. Extract SCSS variables

```bash
# All $variable definitions with their value
grep -rn '^\$[a-z][a-z0-9_-]*:' \
  --include="*.scss" \
  ./vendor/shopware/storefront \
  ./custom/plugins \
  ./custom/static-plugins \
  | grep -v '//.*\$' \
  | sort
```

Regular expression for SCSS variable definitions:
```
\$[a-z][a-z0-9_-]*:\s*.+?(!default)?;
```

### 3. Extract CSS custom properties

```bash
# All --custom-property definitions
grep -rn '--[a-z][a-z0-9_-]*:' \
  --include="*.scss" \
  ./vendor/shopware/storefront \
  ./custom/plugins \
  ./custom/static-plugins \
  | sort
```

### 4. Theme variables from theme.json

```bash
# All configurable theme fields
find . -name "theme.json" | xargs grep -l "config" | head -10
```

Reading out the `config.fields` keys:
```bash
cat custom/static-plugins/MyTheme/src/Resources/theme.json \
  | python3 -c "import sys,json; d=json.load(sys.stdin); [print(k) for k in d.get('config',{}).get('fields',{}).keys()]"
```

### 5. Analyze the override chain

Order in which variables are loaded (who can override whom):

```
1. Core abstract/variables/_bootstrap.scss  (structural Bootstrap overrides)
2. Skin/theme abstract/variables/_theme.scss  (sw-* theme variables)
3. Skin/theme abstract/variables/_bootstrap.scss  (Bootstrap overrides WITH colors)
4. Skin/theme abstract/variables/_custom.scss  (skin custom variables)
5. Bootstrap scss/variables  (Bootstrap defaults)
6. Core abstract/variables/_custom.scss  (framework variables)
7. Plugin variables.scss  (plugin overrides — must be WITHOUT !default)
```

**Important**: SCSS variables with `!default` can only be overridden
if the overriding definition is **loaded earlier** and has **no `!default`**.

### 6. Create the catalog file

Create `.shopware-catalog/scss.md` with the following content:

```markdown
# SCSS catalog — [project name]
Created: [date]

## SCSS files

| Path | Layer | Purpose |
|---|---|---|
| ... | core/plugin/theme | ... |

## SCSS variables

### Theme variables ($sw-*)
| Variable | Value | Origin |
|---|---|---|

### Bootstrap overrides
| Variable | Value | Origin |
|---|---|---|

### Plugin/theme overrides
| Variable | Value | Origin | Overrides |
|---|---|---|---|

## CSS Custom Properties

| Property | Value | File |
|---|---|---|

## Override conflicts
[variables defined more than once, with load-order analysis]
```

## Automation (bash script)

```bash
#!/bin/bash
# .shopware-catalog/refresh-scss.sh

OUTPUT=".shopware-catalog/scss.md"
mkdir -p .shopware-catalog

echo "# SCSS catalog" > "$OUTPUT"
echo "Created: $(date)" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "## SCSS files" >> "$OUTPUT"
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
echo "## SCSS variables" >> "$OUTPUT"
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

echo "Catalog created: $OUTPUT"
```

## Notes on theme.json integration

Every variable defined in `theme.json` under `config.fields` is injected by the ThemeCompiler
as a SCSS variable. The variable name matches the key (kebab-case):

```json
"sw-color-brand-primary": { "type": "color", "value": "#0042a0" }
```

→ is injected into SCSS as `$sw-color-brand-primary: #0042a0` (WITHOUT `!default`).

This means: theme configuration values from the admin **always override** the
`!default` values in `_theme.scss`, because they are injected without `!default`.
