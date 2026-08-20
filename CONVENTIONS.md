# Konventionen — Plugin-Marketplace

Verbindliche Regeln für Aufbau, Benennung und Layout aller Plugins, Skills, Agents, Commands und
Hooks in diesem Marketplace.

**`CLAUDE.md` ist die übergeordnete Effizienz-Referenz und gewinnt bei Widerspruch.** Dieses
Dokument übersetzt sie in konkrete Namens- und Layout-Regeln. Lies beide, bevor du einen Skill
anlegst oder änderst.

Kanonische Wissensquelle **je Plugin** (nicht repo-weit):

| Plugin-Familie | Kanonische Quelle |
|---|---|
| `shopware-*` | Shopware-6.7-Trunk-Source (`src/`, `adr/`, `coding-guidelines/`, `AGENTS.md`, `UPGRADE-*`, `RELEASE_INFO-*`, `changelog/`) |
| `octo-api` | Ventrata-OpenAPI-Spezifikation + `docs.ventrata.com` |
| `contao` | Contao-5-Source + offizielles Handbuch |
| `shadcn`, `shadcn-vue`, `swiper`, `flatpickr`, `playwright`, `panther`, `gotenberg` | jeweiliges Upstream-Repo + offizielle Doku |

## Marketplace-Layout

```
claude-a-dev-team/
├── CLAUDE.md                           # Effizienz-Regelwerk (übergeordnet)
├── CONVENTIONS.md                      # dieses Dokument
├── README.md
├── scripts/measure-skill-budget.py     # Listing-Kosten je Plugin messen
├── .claude-plugin/marketplace.json     # registriert alle Plugins + deren Skills
└── plugins/
    └── <plugin>/
        ├── .claude-plugin/plugin.json  # name, version, description, author, license,
        │                               # keywords, category, skills[]  ← skills[] ist Pflicht
        ├── README.md
        ├── CHANGELOG.md                # bei SemVer-relevanten Änderungen
        ├── .gitignore
        ├── skills/<skill>/SKILL.md     # + flache SCREAMING-CASE.md-Siblings
        ├── agents/<agent>.md           # auto-discovered
        ├── commands/<command>.md       # auto-discovered
        ├── hooks/hooks.json            # optional
        ├── scripts/                    # optional: Generatoren, Verifikation
        └── .<name>-state.json          # optional: Drift-Tracking der Upstream-Quelle
```

`skills[]` muss in **`plugin.json` und `marketplace.json`** stehen und in beiden identisch sein.
Es definiert das ausgelieferte Set — Arbeitsstände dürfen im Repo liegen, ohne ins Listing-Budget
zu zählen. **Ein Pfad auf ein nicht existierendes Skill-Verzeichnis bricht das Laden des Plugins.**

## Naming

| Artefakt | Schema | Beispiel |
|---|---|---|
| Plugin | `<produkt>-<thema>` | `shopware-data`, `octo-api` |
| Skill | `<produkt-prefix>-<thema>` | `sw-entity-definition`, `octo-products` |
| Agent | `<produkt>-<rolle>` | `shopware-dal-expert`, `octo-integrator` |
| Command | `/<prefix>-<verb-objekt>` | `/sw-entity`, `/octo-lookup` |
| Referenz-Datei | `SCREAMING-CASE.md` | `PRODUCT-SCHEMA.md`, `ADR-FORMAT.md` |
| Katalog-Datei (Introspektion) | `.<produkt>-catalog/<thema>.md` | `.shopware-catalog/entities.md` |

Alles kebab-case. Keine Agentur-, Kunden- oder Projektkürzel in Identifiern — dieses Repo ist
öffentlich.

**Der Skill-Name ist selbst ein Trigger-Anker.** `octo-products` trägt das Markenwort und ist damit
matchbar; ein prefixloses `products` wäre es nicht.

## Token-Sparsamkeit (zentral)

Die harte Grenze ist das **Skill-Listing-Budget**: `len(description) + 109` je Skill gegen
**8.000 Zeichen** (1 % des Kontextfensters bei 200k). Bei Überlauf verlieren die *am seltensten
genutzten* Skills ihre Description und triggern nie mehr automatisch. Herleitung, Quellen und der
gemessene Ist-Stand des Repos: `CLAUDE.md`.

1. **Description ≤ 200 Zeichen**, einzeilig, englisch, dritte Person, Muster
   `<Statement>. Use when <anchor>, <anchor>.` Kein `when_to_use` (zählt auf denselben Cap).
2. **≤ 12 modell-sichtbare Skills je Plugin.** Mehr Themen → nach Domänen bündeln und die Tiefe in
   Referenzdateien schieben. Reine Nachschlage-Skills können `disable-model-invocation: true`
   tragen: sie kosten **null** Listing-Budget und sind über einen Router-Skill oder
   `/<plugin>:<skill>` erreichbar.
3. **Trigger-Anker müssen eindeutig sein.** Generische Vokabeln (`product`, `booking`, `pricing`,
   `availability`, `cart`, `component`, `test`, `theme`) gehören **nie** in den `Use when`-Teil —
   sie kollidieren über Plugins hinweg. An ein Markenwort binden: `OCTO or Ventrata products`.
4. **Skills haben kein `model:`-Feld.** Sparsamkeit entsteht durch **progressive disclosure**:
   - `SKILL.md` ≤ **120 Zeilen**: Zweck, Kernmodell, Referenz-Karte.
   - Tiefe (vollständige Schemas, lange Beispiele, Edge-Cases) in flachen Siblings, **eine** Ebene
     tief. Tiefer verschachtelte Dateien werden nur per `head -100` gelesen — alles ab Zeile 101
     ist unsichtbar. Deshalb **kein** `references/deep/`.
   - Inhaltsverzeichnis am Kopf jeder Datei über 100 Zeilen.
5. **Tragendes zuerst.** Nach einer Kompaktierung werden nur die ersten 5.000 Token je Skill wieder
   angehängt (gemeinsames Budget 25.000 Token).
6. **Commands/Agents wählen das günstigste taugliche Model:**
   - `haiku` → mechanisch/Template-getrieben: Scaffolder (`/sw-config-create`), Mapper
     (`shopware-entity-mapper`), Lookup (`/octo-lookup`).
   - `sonnet` → fokussierte Spezialisten und urteilende Commands (`/sw-entity`, `octo-integrator`).
   - `opus` → nur Orchestrator (`shopware-dev`), Migrator (`shopware-migrator`), Knowledge-Sync
     (`shopware-librarian`).
7. **Wissen einbetten, nicht verlinken.** Referenzdateien enthalten destilliertes Wissen — keine
   Verweise auf Upstream-Pfade, die im Nutzerprojekt nicht vorliegen.
8. **Andere Skills per Tool-Call erreichen**, nicht per Pfad:
   `Call the Skill tool with "octo-protocol".` Ein relativer Link in ein anderes Skill-Verzeichnis
   ist keine Invokation und lädt nichts.

## Frontmatter-Templates

### Skill — `skills/<name>/SKILL.md`

Nur `name` und `description`. Kein `triggers:` (existiert nicht), kein `model:`, kein
`when_to_use:`, kein `context: fork` auf Referenz-Skills (Guidelines ohne Task liefern nichts),
kein `paths:` auf prosa-getriggerte Wissens-Skills (Filter, kein Verstärker).

```markdown
---
name: octo-products
description: OCTO/Ventrata product catalogue: GET /products, Product, Option and Unit schemas, every field, enum and capability extension. Use when the request names OCTO or Ventrata products, options, units, or availabilityType.
---

# OCTO Products

<1–3 Sätze Zweck. Tragendes zuerst.>

## <Kernmodell / Endpunkte / Enums>

- **fieldName** (string, required): Bedeutung.

## Reference map

- **[PRODUCT-SCHEMA.md](PRODUCT-SCHEMA.md)**: alle 23 Basisfelder, Enums, Sub-Schemas.
- **[CAPABILITY-EXTENSIONS.md](CAPABILITY-EXTENSIONS.md)**: die 16 capability-abhängigen Felder.

## Related

Call the Skill tool with "octo-protocol" for headers and error codes.

## Source

Distilled from the [Ventrata OCTO API specification](https://docs.ventrata.com) —
`openapi.yaml` 3.0.3, sha256 `d7bec97a…`, retrieved 2026-08-20.
Reference files in this directory are generated; see `scripts/extract_spec.py`.
```

**`## Source` ist Pflicht** in jedem Skill: Upstream-URL, Datei/Version/Hash und Abrufdatum. Ein
Leser muss jede Aussage am Original prüfen können, ein Maintainer muss wissen, was ein Refresh neu
lesen muss. Generierte Dateien tragen zusätzlich einen Generator-Stempel in Zeile 1. Details:
[`CLAUDE.md`](./CLAUDE.md) → „Cite the source".

Die Description im Beispiel ist 216 Zeichen — knapp über dem Ziel und damit die Obergrenze des
Vertretbaren. Zeichen zählen: `python3 -c "print(len('...'))"`.

### Agent — `agents/<name>.md`

```markdown
---
name: octo-integrator
description: >
  <Rolle + wann delegieren>. Use proactively when <anchor>, <anchor>.
tools: Read, Grep, Glob, Bash
model: sonnet
skills: octo-protocol, octo-products
---

# <Titel>
<Anweisungen, Leitplanken, Vorgehensweise.>
```

- **`skills:` injiziert den vollen Inhalt**, nicht nur die Description. Nur die zwei bis drei Skills
  vorladen, die der Agent immer braucht; den Rest über das Skill-Tool erreichen.
- **Least privilege bei `tools`.** Ein Nachschlage-Agent braucht kein `Edit`/`Write` — das schützt
  zugleich eine Wahrheitsquelle vor versehentlichen Änderungen.
- **`hooks`, `mcpServers`, `permissionMode` weglassen** — bei Plugin-Subagents werden sie ignoriert.
- **Agent Teams sind nicht ausliefer­bar** (experimentell, zur Laufzeit erzeugt, ignorieren
  `skills:`).

### Command — `commands/<name>.md`

```markdown
---
name: octo-lookup
description: Look up an OCTO endpoint, schema, field, or capability and print parameters, required flags, and a curl example.
argument-hint: <endpoint|schema|field|capability> [--vendor ventrata|gocity]
allowed-tools: Read, Glob, Grep
model: haiku
---

<Anweisungen. Schluss: "Nichts erfinden.">
```

### Hook — `hooks/hooks.json`

Nach einer Datei-Änderung erinnern (`PostToolUse`, mit Matcher):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          { "type": "command", "command": ["python3", "${CLAUDE_PLUGIN_ROOT}/hooks/<name>-reminder.py"] }
        ]
      }
    ]
  }
}
```

Bei einem Prompt-Anker Kontext injizieren (`UserPromptSubmit`, **ohne** Matcher):

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          { "type": "command",
            "command": ["python3", "${CLAUDE_PLUGIN_ROOT}/hooks/<name>-anchor.py"],
            "timeout": 5 }
        ]
      }
    ]
  }
}
```

- **`UserPromptSubmit` unterstützt keinen `matcher`** — er fiele still aus. Die Regex gehört ins
  Skript, mit Early-Return vor jeder weiteren Arbeit.
- **`additionalContext` muss in `hookSpecificOutput` liegen** — auf Top-Level wird es still
  ignoriert. Häufigster Fehler bei diesem Event.
- **Exec-Form** (Array) bei jedem Pfad-Platzhalter.
- **`timeout: 5`** und Exit 0 auf jedem Pfad: der Hook läuft synchron vor jedem Prompt.
- Ein Hook kann **keinen** Skill erzwingen — es gibt keinen solchen Mechanismus. Er erhöht nur die
  Wahrscheinlichkeit.

## Referenz-Skill vs. Introspektion

- **Referenz-Skill** = „wie baut man X" bzw. „was sagt die Spezifikation" — statisch, aus der
  kanonischen Quelle destilliert.
- **Introspektion** = „was existiert in DIESEM Projekt" → ein `haiku`-Mapper-Agent + Command scannt
  das Nutzerprojekt und schreibt einen gecachten Markdown-Katalog nach `.<produkt>-catalog/`.
  Andere Skills/Agents lesen den Katalog.

## Quelle der Wahrheit

Beansprucht ein Plugin Autorität für eine API oder einen Standard, werden Fakten **generiert, nicht
erinnert**:

- **Aus der maschinenlesbaren Quelle generieren** (OpenAPI, JSON-Schema, typisierter Export) per
  Skript in `scripts/`. Zwischen Spezifikation und Referenzdatei liegt kein Modell.
- **Feld-Index + Verify-Skript** mitliefern, das in **beide** Richtungen prüft: jedes spezifizierte
  Feld ist dokumentiert, und jedes dokumentierte Feld existiert in der Spezifikation. Die zweite
  Richtung fängt Halluzinationen.
- **Drift-State-Datei** (`.<name>-state.json`) mit Quell-URL, Content-Hash und Entitäts-Zählern,
  plus ein `--check`/`--apply`-Command. Kein Netzabruf beim Sessionstart.
- **Generierte Dateien stempeln** mit Quell-Hash und Do-not-edit-Hinweis, damit späterer
  Handbetrieb sichtbar bleibt.
- **Prosa erst nach grünem Verify** ergänzen, danach erneut verifizieren.
- **Quelle in jeder Datei nennen** — `## Source` im Skill, Generator-Stempel in generierten Dateien,
  konkrete Seite (nicht die Site-Wurzel) in handgeschriebenen Referenzen, kanonische Quelle plus
  Rechteinhaber in der Plugin-README.

## Sprache & Öffentlichkeit

Dieses Repo ist öffentlich und international.

- **Englisch für alles Ausgelieferte**: Skills, Referenzdateien, Agents, Commands, Plugin-READMEs,
  Code-Kommentare. `CLAUDE.md`, `CONVENTIONS.md` und die Root-`README.md` sind Autoren-Dokumente
  und dürfen deutsch bleiben.
- **Keine personen-, kunden- oder agenturbezogenen Daten** — keine privaten Mailadressen, keine
  internen Projektnamen, keine Agenturkürzel. `author` trägt einen GitHub-Handle.
- **`license` muss der Realität entsprechen.** `proprietary` in einem öffentlichen Repo ist ein
  Widerspruch. Wo Wissen aus fremder Doku destilliert ist, die Quelle in README und in den
  generierten Dateien nennen.

## Vor dem Ausliefern prüfen

```bash
python3 scripts/measure-skill-budget.py .                              # Listing-Kosten je Plugin
find plugins/<name>/skills -mindepth 3 -name '*.md'                    # leer: Referenzen eine Ebene tief
grep -rn 'triggers:\|when_to_use:\|model:' plugins/<name>/skills/*/SKILL.md   # leer
awk 'FNR==1{if(p&&n>120)print p,n; p=FILENAME; n=0} {n++} END{if(n>120)print p,n}' \
  plugins/<name>/skills/*/SKILL.md                                     # kein SKILL.md > 120 Zeilen
python3 -c "import json,sys;[json.load(open(f)) for f in sys.argv[1:]]" \
  .claude-plugin/marketplace.json plugins/<name>/.claude-plugin/plugin.json   # valides JSON
```

In einer Session: `/doctor` schätzt die Listing-Kosten und ihre größten Verursacher, `/context`
zeigt die Skills-Zeile nach Budget-Anwendung, `--debug` protokolliert die Overflow-Warnung.
Trigger **in beide Richtungen** testen: lösen die gewollten Prompts aus, und lösen Prompts aus
Nachbardomänen nicht aus?

## Stack-Fixpunkte

### Shopware-Plugins (Shopware 6.7)

PHP 8.2+, Symfony 7, Doctrine DBAL 4 (kein ORM — DAL + `Criteria`), Vue 3 + Pinia/Vite (Admin,
`mt-*`), Twig + Bootstrap 5 + Webpack (Storefront), MySQL/MariaDB, OpenSearch/ES,
PHPUnit/PHPStan/Jest/Playwright. Extensibilität: **Events vor Decorators**. Drei APIs: `/api/`
(Admin), `/store-api/` (Store), `/api/_action/sync` (Sync).
Lint: `composer ecs[-fix]`, `composer phpstan`, `composer eslint:admin|storefront[:fix]`,
`composer stylelint`, `composer ludtwig:storefront`.

### octo-api

OCTO (Open Connection for Tourism), offener Standard von OCTO Standards NP Inc. Basis-URL der
Ventrata-Implementierung: `https://api.ventrata.com/octo`. Auth: Bearer. **`Octo-Capabilities` ist
Pflicht-Header** — fehlt er, antwortet die API mit HTTP 400; leerer Wert ist erlaubt. Kernfluss:
Products → Availability → reserve/confirm/cancel. Capabilities sind additiv und werden
kommagetrennt im Header angefordert.
